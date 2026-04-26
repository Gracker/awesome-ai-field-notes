# Your LLM Doesn't Write Correct Code. It Writes Plausible Code.

> 作者: Hōrōshi バガボンド
> 发布时间: 2025-01-12T07:01:56.594Z
> 原文链接: https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code

---
![User's avatar](images/img_001.jpeg)

Discover more from Vagabond Research

code monkey

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

Already have an account? Sign in

# Your LLM Doesn't Write Correct Code. It Writes Plausible Code.

[

![Hōrōshi バガボンド's avatar](images/img_002.jpeg)


](https://substack.com/@katanaquant)

[Hōrōshi バガボンド](https://substack.com/@katanaquant)

Mar 06, 2026

74

21

12

Share

One of the simplest tests you can run on a database:

Doing a primary key lookup on 100 rows.

Thanks for reading Vagabond Research! Subscribe for free to receive new posts and support my work.

Subscribe

SQLite takes 0.09 ms. An LLM-generated Rust rewrite takes 1,815.43 ms.

It’s not a misplaced comma! The rewrite is 20,171 times slower on one of the most basic database operations.

[

![](images/img_003.png)


](https://substackcdn.com/image/fetch/$s_!3Nvv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1a72ec7-4e57-4b89-b528-0a5e402aa25c_1595x300.png)

The thing is though: The code compiles. It passes all its tests. It reads and writes the correct SQLite file format. Its README claims MVCC concurrent writers, file compatibility, and a drop-in C API. At first glance it reads like a working database engine.

But it is not!

**EDIT: Several readers have confused this project with [Turso/libsql](https://github.com/tursodatabase/libsql). They are unrelated. Turso forks the original C SQLite codebase; the project analyzed here is a ground-up LLM-generated rewrite by a single developer. Running the same benchmark against Turso shows performance within 1.2x of SQLite consistent with a mature fork, not a reimplementation.**

LLMs optimize for plausibility over correctness. In this case, plausible is about 20,000 times slower than correct.

I write this as a practitioner, not as a critic. After more than 10 years of professional dev work, I’ve spent the past 6 months integrating LLMs into my daily workflow across multiple projects. LLMs have made it possible for anyone with curiosity and ingenuity to bring their ideas to life quickly, and I really like that! But the number of screenshots of silently wrong output, confidently broken logic, and correct-looking code that fails under scrutiny I have amassed on my disk shows that things are not always as they seem. My conclusion is that LLMs work best when the user defines their acceptance criteria before the first line of code is generated.

A note on the projects examined: this is not a criticism of any individual developer. I do not know the author personally. I have nothing against them. I’ve chosen the projects because they are public, representative, and relatively easy to benchmark. The failure patterns I found are produced by the tools, not the author. Evidence from METR’s randomized study and GitClear’s large-scale repository analysis support that these issues are not isolated to one developer when output is not heavily verified. That’s the point I’m trying to make!

This article talks about what that gap looks like in practice: the code, the benchmarks, another case study to see if the pattern is accidental, and external research confirming it is not an outlier.

## **LLMs Lie. Numbers Don’t.**

I compiled the same C benchmark program against two libraries: system SQLite and the Rust reimplementation’s C API library. Same compiler flags, same WAL mode, same table schema, same queries. 100 rows:

_The benchmark source is available in [this repository](https://github.com/KatanaQuant/db_bench_foo) so you can reproduce the comparison on your own. Absolute timings vary with system load and hardware. Ratios are what matter._

[

![](images/img_004.png)


](https://substackcdn.com/image/fetch/$s_!b3NO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F503cef77-5d11-4c3b-8b94-ef3a09599d87_1212x811.png)

I’ll take the TRANSACTION batch row as the baseline because it doesn’t have the same glaring bugs as the others, namely no WHERE clauses and per-statement syncs. In this run that baseline is already 298x, which means even the best-case path is far behind SQLite. Anything above 298x signals a bug.

The largest gap beyond our baseline is driven by two bugs:

INSERT without a transaction: 1,857x versus 298x in batch mode. SELECT BY ID: 20,171x. UPDATE and DELETE are both above 2,800x. The pattern is consistent: any operation that requires the database to _find something_ is insanely slow.

## **What the Planner Gets Wrong**

I read the source code. Well.. the parts I needed to read based on my benchmark results. The reimplementation is not small: 576,000 lines of Rust code across 625 files. There is a parser, a planner, a VDBE bytecode engine, a B-tree, a pager, a WAL. The modules have all the “correct” names. The architecture also looks correct. But two bugs in the code and a group of smaller issues compound:

### **Bug #1: The Missing ipk Check**

In SQLite, when you declare a table as:

```
CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT, value REAL);
```

the column `id` becomes an [alias for the internal rowid](https://www.sqlite.org/rowidtable.html) — the B-tree key itself. A query like `WHERE id = 5` resolves to a direct B-tree search and scales O(log n). ([I already wrote a TLDR piece about how B-trees work here](https://blog.katanaquant.com/p/a-dockerized-crypto-data-hub-part-cfa).) The [SQLite query planner documentation](https://sqlite.org/queryplanner.html) states: “the time required to look up the desired row is proportional to logN rather than being proportional to N as in a full table scan.” This is not an optimization. It is a fundamental design decision in SQLite’s query optimizer:

```
# `where.c`, in `whereScanInit()`
if( iColumn==pIdx->pTable->iPKey ){
    iColumn = XN_ROWID;
}
```

The line above converts a named column reference to `XN_ROWID` when it matches the table’s INTEGER PRIMARY KEY column. The VDBE then triggers a `SeekRowid` operation instead of a full table scan, which makes the whole thing proportional to logN.

The Rust reimplementation has a proper B-tree. The `table_seek` function implements correct binary search descent through its nodes and scales O(log n). It works. But the query planner never calls it for named columns!

The `is_rowid_ref()` function only recognizes three magic strings:

```
fn is_rowid_ref(col_ref: &ColumnRef) -> bool {
    let name = col_ref.column.to_ascii_lowercase();
    name == "rowid" || name == "_rowid_" || name == "oid"
}
```

A column declared as `id INTEGER PRIMARY KEY`, even though it is internally flagged as `is_ipk: true`, doesn’t get recognized. It is never consulted when choosing between a B-tree search and a full table scan.

Every `WHERE id = N` query flows through `codegen_select_full_scan()`, which emits linear walks through every row via `Rewind` / `Next` / `Ne` to compare each rowid against the target. At 100 rows with 100 lookups, that is 10,000 row comparisons instead of roughly 700 B-tree steps. O(n²) instead of O(n log n). This is consistent with the ~20,000x result in this run.

Every WHERE clause on every column does a full table scan. The only fast path is `WHERE rowid = ?` using the literal pseudo-column name.

### **Bug #2: fsync on Every Statement**

The second bug is responsible for the 1,857x on INSERT. Every bare INSERT outside a transaction is wrapped in a full autocommit cycle: `ensure_autocommit_txn()` → execute → `resolve_autocommit_txn()`. The commit calls `wal.sync()`, which calls Rust’s `fsync(2)` wrapper. 100 INSERTs means 100 fsyncs.

SQLite does the same autocommit, but uses `fdatasync(2)` on Linux, which skips syncing file metadata when compiled with `HAVE_FDATASYNC` (the default). This is roughly [1.6 to 2.7 times cheaper](http://smalldatum.blogspot.com/2020/10/innodb-fsync-and-fdatasync-reducing.html) on NVMe SSDs. SQLite’s per-statement overhead is also minimal: no schema reload, no AST clone, no VDBE recompile. The Rust reimplementation does all three on every call.

Looking at the Rust TRANSACTION batch row, batched inserts (one fsync for 100 inserts) take 32.81 ms, whereas individual inserts (100 fsync calls) take 2,562.99 ms. That’s a 78x overhead from the autocommit.

## **The Compound Effect**

These two bugs are not isolated cases. They are amplified by a group of individually defensible “safe” choices that compound:

-   **AST clone on every cache hit.** The SQL parse is cached, but the AST is `.clone()`‘d on every `sqlite3_exec()`, then recompiled to VDBE bytecode from scratch. SQLite’s `sqlite3_prepare_v2()` just returns a reusable handle.

-   **4KB (Vec<u8>) heap allocation on every read.** The page cache returns data via `.to_vec()`, which creates a new allocation and copies it into the Vec even on cache hits. SQLite returns a [direct pointer into pinned cache memory](https://www.sqlite.org/c3ref/pcache_methods2.html), creating zero copies. The [Fjall database team](https://fjall-rs.github.io/post/fjall-2-6-byteview/) measured this exact anti-pattern at 44% of runtime before building a custom `ByteView` type to eliminate it.

-   **Schema reload on every autocommit cycle.** After each statement commits, the next statement sees the bumped commit counter and calls `reload_memdb_from_pager()`, walks the `sqlite_master` B-tree and then re-parses every CREATE TABLE to rebuild the entire in-memory schema. SQLite checks the [schema cookie](https://sqlite.org/fileformat.html) and only reloads it on change.

-   **Eager formatting in the hot path.** `statement_sql.to_string()` (AST-to-SQL formatting) is evaluated on every call before its guard check. This means it does serialization regardless of whether a subscriber is active or not.

-   **New objects on every statement.** A new `SimpleTransaction`, a new `VdbeProgram`, a new `MemDatabase`, and a new `VdbeEngine` are allocated and destroyed per statement. SQLite reuses all of these across the connection lifecycle via a [lookaside allocator](https://www.sqlite.org/malloc.html) to eliminate `malloc`/`free` in the execution loop.


Each of these was probably chosen individually with sound general reasoning: “We clone because Rust ownership makes shared references complex.” “We use sync\_all because it is the safe default.” “We allocate per page because returning references from a cache requires unsafe.”

Every decision sounds like choosing safety. But the end result is about 2,900x slower in this benchmark. A database’s hot path is the one place where you probably shouldn’t choose safety over performance. SQLite is not primarily fast because it is written in C. Well.. that too, but it is fast because [26 years of profiling](https://sqlite.org/cpu.html) have identified which tradeoffs matter.

In the [1980 Turing Award lecture](https://dl.acm.org/doi/10.1145/358549.358561) Tony Hoare said: “There are two ways of constructing a software design: one way is to make it so simple that there are obviously no deficiencies, and the other is to make it so complicated that there are no obvious deficiencies.” This LLM-generated code falls into the second category. The reimplementation is 576,000 lines of Rust (measured via [scc](https://github.com/boyter/scc), counting code only, without comments or blanks). That is 3.7x more code than SQLite. And yet it still misses the `is_ipk` check that handles the selection of the correct search operation.

Steven Skiena writes in _[The Algorithm Design Manual](https://www.amazon.com/Algorithm-Design-Manual-Computer-Science/dp/3030542556?crid=2ZUP4JANEYOFR&sprefix=the+algorithm+design+manual%2Caps%2C186&sr=8-1&linkCode=ll2&tag=katanalarp-20&linkId=85494361bfe8d87d86a57b283eff0873&language=en_US&ref_=as_li_ss_tl)_: “Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.” It’s not enough that the code looks right. It’s not enough that the tests pass. You have to demonstrate with benchmarks and with proof that the system does what it should. 576,000 lines and no benchmark. That is not “correctness first, optimization later.” That is no correctness at all.

## **Same Method, Same Result**

The SQLite reimplementation is not the only example. A second project by the same author shows the same dynamic in a different domain.

The developer’s LLM agents compile Rust projects continuously, filling disks with build artifacts. Rust’s `target/` directories consume 2–4 GB each with incremental compilation and debuginfo, a [top-three complaint](https://blog.rust-lang.org/2025/02/13/2024-State-Of-Rust-Survey-results/) in the annual Rust survey. This is amplified by the projects themselves: a sibling agent-coordination tool in the same portfolio pulls in 846 dependencies and 393,000 lines of Rust. For context, [ripgrep](https://github.com/BurntSushi/ripgrep) has 61; [sudo-rs](https://www.memorysafety.org/blog/reducing-dependencies-in-sudo/) was deliberately reduced from 135 to 3. Properly architected projects are lean.

The solution to the disk pressure: a cleanup daemon. 82,000 lines of Rust, 192 dependencies, a 36,000-line terminal dashboard with seven screens and a fuzzy-search command palette, a Bayesian scoring engine with posterior probability calculations, an EWMA forecaster with PID controller, and an asset download pipeline with mirror URLs and offline bundle support.

To solve this problem:

```
*/5 * * * * find ~/*/target -type d -name "incremental" -mtime +7 -exec rm -rf {} +
```

A one-line cron job with 0 dependencies. The project’s README claims machines “become unresponsive” when disks fill. It does not once mention Rust’s standard tool for exactly this problem: `cargo-sweep`. It also fails to consider that operating systems already carry ballast helpers. ext4’s [5% root reservation](https://man7.org/linux/man-pages/man8/mke2fs.8.html), reserves blocks for privileged processes by default: on a 500 GB disk, 25 GB remain available to root even when non-root users see “disk full.” That does not guarantee zero impact, but it usually means privileged recovery paths remain available so root can still log in and delete files.

The pattern is the same as the SQLite rewrite. The code matches the _intent_: “Build a sophisticated disk management system” produces a sophisticated disk management system. It has dashboards, algorithms, forecasters. But the _problem_ of deleting old build artifacts is already solved. The LLM generated what was described, not what was needed.

THIS is the failure mode. Not broken 