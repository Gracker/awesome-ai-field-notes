# Git at any scale: Cursor Origin's Continuity storage

- **ID**: cb08e9af
- **原文链接**: https://cursor.com/blog/git-at-any-scale
- **分类**: infra
- **来源类型**: article
- **标签**: git, storage, wal, origin, infrastructure, code-hosting
- **质量评分**: 4/5
- **抓取时间**: 2026-08-20T00:00:00+08:00 (fetched via opencli)

---

## 中文导读

Cursor 发布 Origin 背后的 Git 托管系统 Continuity：核心原语是存 S3 对象存储的 write-ahead log，push 先完整持久化为 WAL entry、绝不提前 ack，可见性由后续 prepare/publish 流程决定；仓库磁盘副本不再是对共识最重要的东西，replica 从 pets 变回 cattle。文中对照 GitHub Spokes 的教训——块级文件系统复制(GFS/DRBD)全部碰壁、磁盘仓库为 source of truth 导致每个副本都是 pets、路由表成为可用性单点。这是“Git 按数据库运维”路线的完整机制文档。

## 为什么值得关注

Git 按数据库运维：WAL 进 S3、push 不持久化不 ack、replica 从 pets 变 cattle

## Summary (English)

Cursor documents Continuity, the storage system behind its Origin code hosting: the core primitive is a write-ahead log in S3-compatible object storage, pushes are fully persisted as WAL entries before being acknowledged and only become visible after an explicit prepare/publish path, and on-disk repository copies stop being sacred - replicas shift from pets back to cattle. The post contrasts lessons from GitHub's Spokes: block-level filesystem replication (GFS, DRBD) hit walls, disk repos as the source of truth made every copy a pet, and the routing table became an availability single point. A full mechanism doc for the run-Git-like-a-database route.

## Excerpt

# Git at any scale · Cursor
> 作者: Vicent Martí
> 发布时间: 2026-08-18T12:00:00.000Z
> 原文链接: https://cursor.com/blog/git-at-any-scale

---

[Blog](https://cursor.com/blog) / [research](https://cursor.com/blog/topic/research)

<video src="https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/blog-demo-video-VTNpYhXb8NpKWmdHZbN9vtvsvGuCuI.mp4" controls poster="https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/blog-demo-animation-2ntJbzDU6xSEoHctbbXf2VUO4b2nxK.gif"></video>

Hosting Git repositories at scale is a nightmare. When Linus Torvalds designed the first version of _the information manager from hell_ (that's actually the tagline for Git, [look it up](https://github.com/git/git/commit/e83c5163316)), he had a very specific use case in mind: his own. He wanted to replace BitKeeper, the distributed version control system that was being used to develop the Linux Kernel. Of course, the replacement had to be distributed too. The Kernel is an unusual software project; it is extremely decentralized, with many different maintainers for its many different subsystems. A distributed version control system is a natural fit for this workflow.

Twenty years later, Git has become an industry standard, but the truth is that its distributed nature is more of a hindrance than an advantage. The average open-source software project doesn't operate with a decentralized workflow. The average company definitely doesn't. They use the many advantages of the distributed model (such as being able to work offline, delay pushes, etc) but they very much rely on a centralized host. And hosting a Git repository, it turns out, is an incredibly hard thing to do.

## [#](#whats-hard-about-git)What's hard about Git?

The challenge in hosting Git repositories at scale is inherent in the design of Git itself: a _distributed_ version control system means that all instances of a repository are identical. There's nothing special about the repository on a Git server that doesn't apply to a repository on a developer's laptop. Although at first it may appear that this makes hosting Git repositories straightforward (simply put an HTTP daemon in front of an on-disk copy of a repository and you've got a Git server going!), there are many hard scalability and reliability challenges that make this quite the opposite.

In a normal Git repository, your code and metadata (files, commits, trees) are compressed and stored in _packfiles_ — a simple binary serialization format which is convenient to deal with on a local machine, but not ideal to manage at scale on a server. Packfiles are the fundamental building block of Git storage _and_ Git networking. When you push or fetch data from a repository, it's transferred as a packfile.

This is how Git works by design, but it would be fair to think that it needn't be that way. After all, you do not control the Git client (at least not without annoying your users and adding a lot of friction), but within the walls of your own server, you can do _anything_ you want. Nothing ties you to using packfiles — Linus is not going to come over and check. The only restriction is that you do need to receive and send _packfiles_ over the network for all Git operations.

Over the years, companies that tried hosting Git repositories at scale noticed that this _packfile_\-based design was a major limitation on both availability and scalability. Packfiles are large binary files that must exist on a filesystem for Git to access them. The simple approach of having an HTTP server in front of a repository on disk has a very low ceiling. Ideally you'd want the repository to exist on many disks and many machines (this lets you run many Git operations in parallel, and keeps your repository available when a server crashes). But how do you do that?

There are broadly three possible approaches to accomplish this, in increasing order of complexity: distribute the filesystem, distribute the packfiles, or distribute Git itself.

## [#](#git-without-packfiles)Git without packfiles

Git is a content-addressable data store. All objects in a Git repository (blobs, trees, commits, etc) are keyed by the SHA-1 of their contents. This is something that intuitively maps very well to a distributed key-value store (the key is the SHA-1; the value is the actual object), and could provide a clean way to scale out the storage of a repository. But this actually doesn't work.

Here's the issue: the actual layout of a Git repository is a directed acyclic graph (DAG for short). You can look up any object via its SHA, but to perform even the most trivial operation in the repo, you must actually walk the DAG step by step.

If you want to do an operation like listing the recent changes in a repository, you must process its commits. When you process a commit, you get a pointer to the root of its tree. From that tree, you get pointers to each file and each subtree. From the original commit, you get a pointer to its parent (the one that comes before it in the history). Crucially, at every step of this walk, you don't know the value of the next pointer until you fetch the previous one. If every fetch requires a round trip to a distributed store, things become very expensive very fast.

This approach to distributing Git at the object level has been tried before, many times, and it often fails at scale. The most promising implementation was attempted by my former mentor Shawn Pearce when he was working on the version control systems team at Google. His approach was [storing the objects in a distributed hash table](https://www.eclipse.org/lists/jgit-dev/msg01189.html). This was only possible thanks to JGit, a custom Git implementation in Java. Like any good ol' Java library, JGit provides enough interfaces and factories and interface factories to abstract all the details of a normal Git repository, including replacing its on-disk packfiles with a DHT. Although the system worked and results were good enough for normal Git operations, the limitations of the Git protocol (which again, require _packfiles_ to be sent over the network regardless of how you store data on the server) made the `git clone` performance bad enough to discard the design altogether.

## [#](#github-and-filesystems)GitHub and filesystems

A couple years after Git started to escape its Linux Kernel bubble, a scrappy startup was born in San Francisco. GitHub was founded in 2008 as a social coding platform with a very prescient tagline, "Git repository hosting: no longer a pain in the ass." I'm not joking here either, [look it up](https://web.archive.org/web/20080514210148/http://github.com/). There was, all the way back in 2008, a broad consensus that despite (or perhaps because of) Git's distributed design, you actually needed a centralized way to host Git repositories to make them user-friendly, and doing this was very painful. GitHub was set on changing that.

Its platform started as (and mostly still is) a Rails monolith. The very first versions were running off a single, albeit beefy, machine, with a Ruby server and copies of the repositories on disk next to it. Scaling a Rails app is easy: deploy more instances of it. But in this particular case, since Git is involved, they quickly ran into the recurring question we're trying to solve here: If the Rails app needs to access the Git repositories on disk, how do you deploy more copies of them?

Being a thrifty bunch of misfits, the early systems engineers at GitHub tried the simplest approach that could possibly fix their scaling problems. The thinking was that, if they focused on distributing the _filesystem_ (instead of packfiles, or Git itself), they could keep the Rails app unchanged and spend their time shipping more features for the ever-growing user base, instead of doing weird stuff with Git. Very pragmatic. It didn't work.

The team attempted many approaches to a distributed filesystem for Git data: the most obvious one, using NFS to store all repositories on a centralized server, was quickly discarded. The default implementation of Git makes a lot of assumptions about filesystem semantics (locking, tearing, reading, syncing...) that ensure decent performance on the local filesystem of a slow developer laptop, but pay no attention to how they behave over a networked filesystem. It was slow, and it was buggy.

Further attempts were made with (frankly, in retrospect, horrific) technologies that replicated the filesystem at the block level. A short-lived deployment with [GFS](https://en.wikipedia.org/wiki/GFS2). A longer-lived deployment based on [DRBD](https://en.wikipedia.org/wiki/DRBD). They all hit a wall. They were _terrible_ to operate day to day, and they didn't make up for it with good performance. It all boils down to the design of _packfiles_ on disk.

We've already seen how Git's graph-like data structures make round-trips prohibitively expensive. Unfortunately, a very similar principle also applies to the underlying data on-disk

[... truncated for content page ...]
