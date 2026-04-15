---
title: 'Your LLM Doesn&#x27;t Write Correct Code. It Writes Plausible Code.'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# Your LLM Doesn&#x27;t Write Correct Code. It Writes Plausible Code.

> 用极端案例精准揭示了 LLM 代码生成的核心缺陷：表面正确 ≠ 实际正确。

🔗 [原文链接](https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code) | @Hōrōshi バガボンド | 🌐 | ⭐⭐⭐⭐⭐ 5 ⭐5 5/5 📅 2026-03-07

`LLM` `代码质量` `SQLite` `性能` `AI对齐` `sycophancy`

---

# Your LLM Doesn't Write Correct Code. It Writes Plausible Code.

## English
Your LLM Doesn't Write Correct Code. It Writes Plausible Code. Vagabond ResearchSubscribeSign inYour LLM Doesn't Write Correct Code. It Writes Plausible Code.Hōrōshi バガボンドMar 06, 2026731912ShareOne of the simplest tests you can run on a database:Doing a primary key lookup on 100 rows.Thanks for reading Vagabond Research! Subscribe for free to receive new posts and support my work.SubscribeSQLite takes 0.09 ms. An LLM-generated Rust rewrite takes 1,815.43 ms.It’s not a misplaced comma! The rewrite is 20,171 times slower on one of the most basic database operations.The thing is though: The code compiles. It passes all its tests. It reads and writes the correct SQLite file format. Its README claims MVCC concurrent writers, file compatibility, and a drop-in C API. At first glance it reads like a working database engine.But it is not!EDIT: Several readers have confused this project with Turso/libsql. They are unrelated. Turso forks the original C SQLite codebase; the project analyzed here is a ground-up LLM-generated rewrite by a single developer. Running the same benchmark against Turso shows performance within 1.2x of SQLite consistent with a mature fork, not a reimplementation.LLMs optimize for plausibility over correctness. In this case, plausible is about 20,000 times slower than correct.I write this as a practitioner, not as a critic. After more than 10 years of professional dev work, I’ve spent the past 6 months integrating LLMs into my daily workflow across multiple projects. LLMs have made it possible for anyone with curiosity and ingenuity to bring their ideas to life quickly, and I really like that! But the number of screenshots of silently wrong output, confidently broken logic, and correct-looking code that fails under scrutiny I have amassed on my disk shows that things are not always as they seem. My conclusion is that LLMs work best when the user defines their acceptance criteria before the first line of code is generated.A note on the projects examined: this is not a criticism of any individual developer. I do not know the author personally. I have nothing against them. I’ve chosen the projects because they are public, representative, and relatively easy to benchmark. The failure patterns I found are produced by the tools, not the author. Evidence from METR’s randomized study and GitClear’s large-scale repository analysis support that these issues are not isolated to one developer when output is not heavily verified. That’s the point I’m trying to make!This article talks about what that gap looks like in practice: the code, the benchmarks, another case study to see if the pattern is accidental, and external research confirming it is not an outlier.LLMs Lie. Numbers Don’t.I compiled the same C benchmark program against two libraries: system SQLite and the Rust reimplementation’s C API library. Same compiler flags, same WAL mode, same table schema, same queries. 100 rows:The benchmark source is available in this repository so you can reproduce the comparison on your own. Absolute timings vary with system load and hardware. Ratios are what matter.I’ll take the TRANSACTION batch row as the baseline because it doesn’t have the same glaring bugs as the others, namely no WHERE clauses and per-statement syncs. In this run that baseline is already 298x, which means even the best-case path is far behind SQLite. Anything above 298x signals a bug.The largest gap beyond our baseline is driven by two bugs:INSERT without a transaction: 1,857x versus 298x in batch mode. SELECT BY ID: 20,171x. UPDATE and DELETE are both above 2,800x. The pattern is consistent: any operation that requires the database to find something is insanely slow.What the Planner Gets WrongI read the source code. Well.. the parts I needed to read based on my benchmark results. The reimplementation is not small: 576,000 lines of Rust code across 625 files. There is a parser, a planner, a VDBE bytecode engine, a B-tree, a pager, a WAL. The modules have all the “correct” names. The architecture also looks correct. But two bugs in the code and a group of smaller issues compound:Bug #1: The Missing ipk CheckIn SQLite, when you declare a table as:CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT, value REAL);the column id becomes an alias for the internal rowid — the B-tree key itself. A query like WHERE id = 5 resolves to a direct B-tree search and scales O(log n). (I already wrote a TLDR piece about how B-trees work here.) The SQLite query planner documentation states: “the time required to look up the desired row is proportional to logN rather than being proportional to N as in a full table scan.” This is not an optimization. It is a fundamental design decision in SQLite’s query optimizer:# `where.c`, in `whereScanInit()` if( iColumn==pIdx->pTable->iPKey ){ iColumn = XN_ROWID; }The line above converts a named column reference to XN_ROWID when it matches the table’s INTEGER PRIMARY KEY column. The VDBE then triggers a SeekRowid operation instead of a full table scan, which makes the whole thing proportional to logN.The Rust reimplementation has a proper B-tree. The table_seek function implements correct binary search descent through its nodes and scales O(log n). It works. But the query planner never calls it for named columns!The is_rowid_ref() function only recognizes three magic strings:fn is_rowid_ref(col_ref: &ColumnRef) -> bool { let name = col_ref.column.to_ascii_lowercase(); name == "rowid" || name == "_rowid_" || name == "oid" }A column declared as id INTEGER PRIMARY KEY, even though it is internally flagged as is_ipk: true, doesn’t get recognized. It is never consulted when choosing between a B-tree search and a full table scan.Every WHERE id = N query flows through codegen_select_full_scan(), which emits linear walks through every row via Rewind / Next / Ne to compare each rowid against the target. At 100 rows with 100 lookups, that is 10,000 row comparisons instead of roughly 700 B-tree steps. O(n²) instead of O(n log n). This is consistent with the ~20,000x result in this run.Every WHERE clause on every column does a full table scan. The only fast path is WHERE rowid = ? using the literal pseudo-column name.Bug #2: fsync on Every StatementThe second bug is responsible for the 1,857x on INSERT. Every bare INSERT outside a transaction is wrapped in a full autocommit cycle: ensure_autocommit_txn() → execute → resolve_autocommit_txn(). The commit calls wal.sync(), which calls Rust’s fsync(2) wrapper. 100 INSERTs means 100 fsyncs.SQLite does the same autocommit, but uses fdatasync(2) on Linux, which skips syncing file metadata when compiled with HAVE_FDATASYNC (the default). This is roughly 1.6 to 2.7 times cheaper on NVMe SSDs. SQLite’s per-statement overhead is also minimal: no schema reload, no AST clone, no VDBE recompile. The Rust reimplementation does all three on every call.Looking at the Rust TRANSACTION batch row, batched inserts (one fsync for 100 inserts) take 32.81 ms, whereas individual inserts (100 fsync calls) take 2,562.99 ms. That’s a 78x overhead from the autocommit.The Compound EffectThese two bugs are not isolated cases. They are amplified by a group of individually defensible “safe” choices that compound:AST clone on every cache hit. The SQL parse is cached, but the AST is .clone()‘d on every sqlite3_exec(), then recompiled to VDBE bytecode from scratch. SQLite’s sqlite3_prepare_v2() just returns a reusable handle.4KB (Vec<u8>) heap allocation on every read. The page cache returns data via .to_vec(), which creates a new allocation and copies it into the Vec even on cache hits. SQLite returns a direct pointer into pinned cache memory, creating zero copies. The Fjall database team measured this exact anti-pattern at 44% of runtime before building a custom ByteView type to eliminate it.Schema reload on every autocommit cycle. After each statement commits, the next statement sees the bumped commit counter and calls reload_memdb_from_pager(), walks the sqlite_master B-tree and then re-parses every CREATE TABLE to rebuild the entire in-memory schema. SQLite checks the schema cookie and only reloads it on change.Eager formatting in the hot path. statement_sql.to_string() (AST-to-SQL formatting) is evaluated on every call before its guard check. This means it does serialization regardless of whether a subscriber is active or not.New objects on every statement. A new SimpleTransaction, a new VdbeProgram, a new MemDatabase, and a new VdbeEngine are allocated and destroyed per statement. SQLite reuses all of these across the connection lifecycle via a lookaside allocator to eliminate malloc/free in the execution loop.Each of these was probably chosen individually with sound general reasoning: “We clone because Rust ownership makes shared references complex.” “We use sync_all because it is the safe default.” “We allocate per page because returning references from a cache requires unsafe.”Every decision sounds like choosing safety. But the end result is about 2,900x slower in this benchmark. A database’s hot path is the one place where you probably shouldn’t choose safety over performance. SQLite is not primarily fast because it is written in C. Well.. that too, but it is fast because 26 years of profiling have identified which tradeoffs matter.In the 1980 Turing Award lecture Tony Hoare said: “There are two ways of constructing a software design: one way is to make it so simple that there are obviously no deficiencies, and the other is to make it so complicated that there are no obvious deficiencies.” This LLM-generated code falls into the second category. The reimplementation is 576,000 lines of Rust (measured via scc, counting code only, without comments or blanks). That is 3.7x more code than SQLite. And yet it still misses the is_ipk check that handles the selection of the correct search operation.Steven Skiena writes in The Algorithm Design Manual: “Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.” It’s not enough that the code looks right. It’s not enough that the tests pass. You have to demonstrate with benchmarks and with proof that the system does what it should. 576,000 lines and no benchmark. That is not “correctness first, optimization later.” That is no correctness at all.Same Method, Same ResultThe SQLite reimplementation is not the only example. A second project by the same author shows the same dynamic in a different domain.The developer’s LLM agents compile Rust projects continuously, filling disks with build artifacts. Rust’s target/ directories consume 2–4 GB each with incremental compilation and debuginfo, a top-three complaint in the annual Rust survey. This is amplified by the projects themselves: a sibling agent-coordination tool in the same portfolio pulls in 846 dependencies and 393,000 lines of Rust. For context, ripgrep has 61; sudo-rs was deliberately reduced from 135 to 3. Properly architected projects are lean.The solution to the disk pressure: a cleanup daemon. 82,000 lines of Rust, 192 dependencies, a 36,000-line terminal dashboard with seven screens and a fuzzy-search command palette, a Bayesian scoring engine with posterior probability calculations, an EWMA forecaster with PID controller, and an asset download pipeline with mirror URLs and offline bundle support.To solve this problem:*/5 * * * * find ~/*/target -type d -name "incremental" -mtime +7 -exec rm -rf {} +A one-line cron job with 0 dependencies. The project’s README claims machines “become unresponsive” when disks fill. It does not once mention Rust’s standard tool for exactly this problem: cargo-sweep. It also fails to consider that operating systems already carry ballast helpers. ext4’s 5% root reservation, reserves blocks for privileged processes by default: on a 500 GB disk, 25 GB remain available to root even when non-root users see “disk full.” That does not guarantee zero impact, but it usually means privileged recovery paths remain available so root can still log in and delete files.The pattern is the same as the SQLite rewrite. The code matches the intent: “Build a sophisticated disk management system” produces a sophisticated disk management system. It has dashboards, algorithms, forecasters. But the problem of deleting old build artifacts is already solved. The LLM generated what was described, not what was needed.THIS is the failure mode. Not broken syntax or missing semicolons. The code is syntactically and semantically correct. It does what was asked for. It just does not do what the situation requires. In the SQLite case, the intent was “implement a query planner” and the result is a query planner that plans every query as a full table scan. In the disk daemon case, the intent was “manage disk space intelligently” and the result is 82,000 lines of intelligence applied to a problem that needs none. Both projects fulfill the prompt. Neither solves the problem.The obvious counterargument is “skill issue, a better engineer would have caught the full table scan.” And that’s true. That’s exactly the point! LLMs are dangerous to people least equipped to verify their output. If you have the skills to catch the is_ipk bug in your query planner, the LLM saves you time. If you don’t, you have no way to know the code is wrong. It compiles, it passes tests, and the LLM will happily tell you that it looks great.EDIT: Some readers have pointed out that the comparison might be unfair with the author claiming the project wasn’t finished and ready for testing yet.The rewrite got actively promoted by its author 1 week before the release of this article using present-tense performance improvement claims over SQLite. The README has since been revised to acknowledge remaining limitations and clarify the project’s current state in this commit and subsequent ones.At the time of writing the repository in question had amassed over 500k lines of code in over 1,600 commits made over 30 days of 24/7 LLM work. “Not finished” usually means work hasn’t been done yet but that’s not the case. Everything was already implemented. It was just wrong.Ironically the “not finished” defense reinforces the thesis. The LLM produced output that looked finished with a complete README, comparison tables and architectural documentation, present-tense performance claims, and was promoted as such. The gap between what it looks like and what it does is exactly the point.The main thesis is not “FrankenSQLite is bad”. It is: “LLMs produce code that looks correct but isn’t”. Whether the bugs get fixed doesn’t change what the LLM output looked like when it shipped.Measuring the Wrong ThingThe tools used to measure LLM output reinforce the illusion. scc‘s COCOMO model estimates the rewrite at $21.4 million in development cost. The same model values print("hello world") at $19.COCOMO was designed to estimate effort for human teams writing original code. Applied to LLM output, it mistakes volume for 

## 中文
**你的 LLM 不会写正确的代码。它只会写看起来合理的代码。**

### 核心观点
作者通过一个实际的案例展示了 LLM 生成代码的一个重要问题：代码看起来是正确的，但实际上可能是错误的，性能可能相差数万倍。

### 主要发现

#### 1. 性能差距惊人
- **SQLite**：0.09 毫秒完成主键查找
- **LLM 生成的 Rust 重写**：1,815.43 毫秒
- **性能差距**：20,171 倍

#### 2. 代码看起来正确
- 代码能够编译通过
- 所有测试都能通过
- 能够读写正确的 SQLite 文件格式
- README 声称支持 MVCC 并发写入、文件兼容性和 C API

#### 3. 实际问题严重
- 查询规划器缺少对主键的检查
- 每个语句都进行 fsync 操作
- 复杂的 AST 克隆和内存分配
- 架构过于复杂，缺少核心优化

### 深层次分析

#### LLM 的工作原理
- LLM 优化的是"看起来合理"而不是"正确"
- 生成的代码在语法和语义上可能都是正确的
- 但在性能和实际效果上可能存在严重问题

#### 问题根源
1. **表面正确性**：代码通过了基本测试
2. **过度设计**：为了表面的完整性而添加不必要的复杂性
3. **缺乏验证**：没有足够的性能测试和验证

### 实际案例对比

#### SQLite vs LLM 重写
- **代码量**：SQLite 约 15 万行 vs LLM 重写 57.6 万行
- **性能**：SQLite 快 20,000 倍
- **架构**：SQLite 精简高效 vs LLM 重写过度复杂

#### 解决方案对比
- **正确方案**：简单的 cron 作业清理构建缓存
- **LLM 方案**：82,000 行的复杂磁盘管理系统

### 关键教训

1. **表面正确 ≠ 实际正确**：代码能编译、能运行不等于性能和正确性有保证
2. **过度设计的危害**：不必要的复杂性会导致性能问题
3. **验证的重要性**：必须通过实际测试和基准测试来验证代码质量
4. **LLM 的局限性**：LLM 擅长生成看起来合理的代码，但不保证实际正确性

### 最佳实践建议

1. **定义验收标准**：在使用 LLM 生成代码前明确定义验收标准
2. **性能测试**：对生成的代码进行性能基准测试
3. **代码审查**：特别是对关键路径的性能审查
4. **实际验证**：在实际环境中测试代码效果

### 结论

LLM 能够快速生成看起来正确的代码，但这并不意味着代码实际上是正确的。在使用 LLM 辅助开发时，必须保持警惕，进行充分的验证和测试，特别是对性能关键的部分。正确的代码不仅要能运行，还要能高效、可靠地运行。

---

**总结**：这篇文章通过 SQLite 的实际案例揭示了 LLM 生成代码的一个重要陷阱：表面正确性不代表实际正确性。开发者在使用 LLM 辅助开发时需要保持批判性思维，通过实际的性能测试和验证来确保代码质量。
