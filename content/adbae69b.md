# brew install actions/checkout

- **ID**: adbae69b
- **原文链接**: https://nesbitt.io/2026/08/04/brew-install-actions-checkout.html
- **作者 / 日期**: Andrew Nesbitt | 2026-08-04
- **分类**: infra
- **来源类型**: article
- **标签**: github-actions, supply-chain-security, homebrew, ci, attestation
- **质量评分**: 4/5
- **抓取时间**: 2026-08-05T15:45:26.663004+00:00

---

## 中文导读

Andrew Nesbitt 把 GitHub Actions 的 uses 生态类比为缺少依赖可见性和审查层的包管理器，并提出用 Homebrew tap / OCI artifact 方式包装 actions：formula 可以携带 SHA-256依赖声明auditsigstore attestation 与人工 review文章进一步讨论 composite action 内部 uses 重写runner 本地路径解析自托管 runner cache 和 zizmor index-time audit，适合从 CI 供应链角度重新看 actions/checkout 这类基础依赖

## 为什么值得关注

把 GitHub Actions 当包管理器看，才能补上依赖树锁定审查和 attestation

## English Summary

Andrew Nesbitt argues that GitHub Actions behaves like an under-specified package manager and explores a Homebrew-style index with formulae, hashes, dependency metadata, audits, attestations, and review for actions such as actions/checkout.

## Obsidian Evidence

候选来自 `OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-08-05-AK-RSS-Digest.md` / Gracker RSS 精选。

## Source Extract / Metadata

# brew install actions/checkout
> 作者: Andrew Nesbitt
> 发布时间: 2026-08-04T10:00:00+00:00
> 原文链接: https://nesbitt.io/2026/08/04/brew-install-actions-checkout.html

---

In December I went through why [`uses:` is a package manager with no lockfile, no integrity hashes and no transitive visibility](https://nesbitt.io/2025/12/06/github-actions-package-manager.html), and in April through the [run of incidents](https://nesbitt.io/2026/04/28/github-actions-is-the-weakest-link.html) that followed from that. GitHub’s [2026 security roadmap](https://github.blog/news-insights/product-news/whats-coming-to-our-github-actions-2026-security-roadmap/) has since committed to a lockfile, now in preview as [`gh-actions-lock`](https://github.com/github/gh-actions-lock), and made immutable actions the preferred resolution path. Neither of those changes adds any review between an action author tagging a release and the runner executing it. Homebrew has run that kind of curated index for fifteen years and, as of the immutable-actions rollout, stores its artifacts as OCI manifests on ghcr.io alongside the actions themselves, so I spent some time working out how much of a GitHub Actions registry you could assemble from Homebrew parts.

### Shared storage[#](#shared-storage)

Immutable actions and Homebrew bottles are both OCI artifacts on ghcr.io: [`actions/publish-immutable-action`](https://github.com/actions/publish-immutable-action) tars the action directory, pushes it as a layer with `artifactType: application/vnd.github.actions.package.v1+json`, attaches a sigstore bundle through the OCI referrers API, and tags the manifest with the semver, after which a workflow referencing `actions/checkout@4.2.2` [resolves through `pkg.actions.githubusercontent.com`](https://github.blog/changelog/2024-12-05-notice-of-upcoming-releases-and-breaking-changes-for-github-actions/) instead of the git tarball. `brew pr-pull` pushes bottles under the same manifest schema at `ghcr.io/homebrew/core/<name>` with a `com.github.package.type: homebrew_bottle` annotation and a [sigstore attestation](https://blog.trailofbits.com/2024/05/14/a-peek-into-build-provenance-for-homebrew/) that `brew verify` checks against Homebrew’s CI identity, so `crane manifest ghcr.io/homebrew/core/jq:1.7.1` and `crane manifest ghcr.io/actions/checkout:4.2.2` return the same document type, as you’d expect from [last week’s post](https://nesbitt.io/2026/07/30/wheels-bottles-images.html).

The [comparison table in the December post](https://nesbitt.io/2025/12/06/github-actions-package-manager.html) marked Actions ✗ on integrity hashes, transitive visibility, dependency-tree inspection and immutable versions, and homebrew-core provides all four for its 8,400 formulae through the index rather than the storage: each formula pins a source URL to a sha256, declares dependencies that `brew deps --tree` can walk, passes [`brew audit`](https://docs.brew.sh/Formula-Cookbook#audit-the-formula) and human review on every change, gets autobumped by `livecheck` when upstream tags a release, and can carry `deprecate!` or `disable!` when it shouldn’t be installed.

### A tap of actions[#](#a-tap-of-actions)

The index can be a tap, with each formula pinning an action tarball by SHA-256:

```
class ActionsCheckout < Formula
  desc "Checks out a repository for a GitHub Actions workflow"
  homepage "https://github.com/actions/checkout"
  url "https://github.com/actions/checkout/archive/refs/tags/v4.2.2.tar.gz"
  sha256 "63e9c07ff6c9ddf3a3b39d30e59f0bf3a..."
  license "MIT"

  livecheck do
    url :stable
    strategy :github_latest
  end

  def install
    prefix.install Dir.children(".")
  end
end
```

For a JavaScript action that ships a built `dist/` in its release tarball, that’s sufficient: the tarball is pinned to a content hash, `brew audit` and `brew verify` apply as they would to any formula, and `brew bump-formula-pr` opens a reviewed PR when checkout tags v4.2.3. Everything above `def install` is already static data. Homebrew is in the middle of [migrating install hooks to declarative steps](https://github.com/Homebrew/brew/pull/23196) so that bottle and cask installs need no Ruby evaluation at all, at which point an actions tap could be `.json` files with no code execution on install.

The [transitive problem](https://nesbitt.io/2025/12/06/github-actions-package-manager.html) is specific to composite actions, whose `action.yml` carries its own `uses:` lines that the runner re-resolves at execution time regardless of how the outer action was pinned. In a formula those become `depends_on` entries plus an `inreplace` at build time. For a composite that internally calls `actions/cache@v4`:

```
depends_on "actions-cache"

def install
  inreplace "action.yml",
    "uses: actions/cache@v4",
    "uses: ./.brew-actions/actions-cache"
  prefix.install Dir.children(".")
end
```

The resulting bottle has no floating refs left in it, `brew deps --tree` prints the transitive graph that no runner command exposes today, and the tap’s git log records which `actions-cache` revision the composite was built against. Moving that pin requires a reviewed PR; an action author cannot change it with `git tag -f` in someone else’s repository.

Every incident in the [weakest-link post](https://nesbitt.io/2026/04/28/github-actions-is-the-weakest-link.html) would have required a reviewed change to that index before reaching downstream users, where an npm-style per-project lockfile would only have reduced the number of downstream repositories exposed. A workflow that pins `@v4` today has already delegated the version decision to whoever can push a tag to the action repo, and a tap moves that delegation to a reviewer instead. It also matches Homebrew’s rolling-release design, where `Brewfile.lock.json` was [removed in November 2024](https://github.com/Homebrew/homebrew-bundle/pull/1509) and per-project pinning is [currently out of scope](https://docs.brew.sh/Brew-Bundle-and-Brewfile). I’d like to see the lockfile come back this year, and until it does a workflow that needs stricter reproducibility than the tap’s HEAD can pin the tap itself to a commit.

An `audit_formula` extension for the tap would run [zizmor](https://docs.zizmor.sh/) over the extracted `action.yml` and reject anything that trips `dangerous-triggers` or `template-injection`, and reject composites whose internal `uses:` lines aren’t fully covered by `depends_on`. The Marketplace’s “verified creator” badge checks the publisher’s identity and nothing about the action’s contents, so a static-analysis gate at index time would be new. Bottles built from the tap are attested by the tap’s CI the same way homebrew-core bottles are. Each formula’s `url` points at a GitHub repository, which is the input `brew vulns` [already keys OSV lookups on](https://nesbitt.io/2026/07/17/plumbing-homebrew-into-the-vulnerability-ecosystem.html), so an advisory against `actions/download-artifact` surfaces through the same path as one against `openssl`.

### Getting the runner to use it[#](#getting-the-runner-to-use-it)

The runner has three `ActionSourceType` values in [`ActionStepDefinitionReference.cs`](https://github.com/actions/runner/blob/main/src/Sdk/DTPipelines/Pipelines/ActionStepDefinitionReference.cs) (repository, container registry, script) and none of them is “an installed package on disk”, so consuming a Homebrew-installed action means picking one of three integration points at increasing cost.

The runner accepts `uses: ./path/to/action` relative to `$GITHUB_WORKSPACE`. The prototype tap at [andrew/homebrew-actions](https://github.com/andrew/homebrew-actions) packages `actions/checkout`, `actions/cache`, `pre-commit/action` and `actions/first-interaction`. Its setup action runs `brew bundle --file .github/Actionfile` and copies each keg into `./.brew-actions/<name>`, which is where the formula’s `inreplace` above pointed the composite’s dependency. The Actionfile is a normal Brewfile:

```
tap "andrew/actions"
brew "andrew/actions/pre-commit-action"
```

```
steps:
  - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
  - uses: andrew/homebrew-actions@7def8ee0f83dbb7850e9029c9e0e6ccbafdd209e
  - uses: ./.brew-actions/pre-commit-action
```

The four formulae pass `brew audit`, install and test on hosted macOS and Ubuntu runners, and the integration job runs the copied `pre-commit/action` composite through to its rewritten `actions/cache` step. It still costs one round-trip to fetch the setup action itself the old way, and `checkout` stays on a plain SHA pin because it runs before the workspace has anything in it to `uses: ./` from.

Because `./` is anchored at `$GITHUB_WORKSPACE`, the setup action has to copy each keg there and `checkout` has to run first. Runner 2.336.0 [added a `$/` prefix](https://github.blog/changelog/2026-07-30-reference-same-repository-actions-with-self-repository-syntax/) that anchors at the repository containing the defining file, resolved at 

...[truncated by AAIF intake]...
