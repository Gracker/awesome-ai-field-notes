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

## Your LLM Doesn't Write Correct Code. It Writes Plausible Code.

### English

**Author**: Hōrōshi バガボンド (Vagabond Research)
**Published**: 2026-03-06
**Source**: `https`://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code>

One of the simplest tests you can run on a database: doing a primary key lookup on 100 rows.

SQLite takes 0.09 ms. An LLM-generated Rust rewrite takes 1,815.43 ms.

It's not a misplaced comma! The rewrite is **20,171 times slower** on one of the most basic database operations.

The code compiles. It passes all its tests. It reads and writes the correct SQLite file format. Its README claims MVCC concurrent writers, file compatibility, and a drop-in C API. At first glance it reads like a working database engine. But it is not!

**LLMs optimize for plausibility over correctness. In this case, plausible is about 20,000 times slower than correct.**

### LLMs Lie. Numbers Don't.

Compiled the same C benchmark program against two libraries: system SQLite and the Rust reimplementation's C API library. Same compiler flags, same WAL mode, same table schema, same queries. 100 rows.

The largest gap is driven by two bugs:

- **INSERT without a transaction**: 1,857x versus 298x in batch mode
- **SELECT BY ID**: 20,171x
- **UPDATE and DELETE**: both above 2,800x

The pattern is consistent: any operation that requires the database to *find something* is insanely slow.

### Bug #1: The Missing ipk Check

In SQLite, when you declare a table with `id INTEGER PRIMARY KEY`, the column becomes an alias for the internal rowid — the B-tree key itself. A query like `WHERE id = 5` resolves to a direct B-tree search and scales O(log n).

The Rust reimplementation has a proper B-tree with correct binary search. But the query planner never calls it for named columns! The `is_rowid_ref()` function only recognizes three magic strings: `rowid`, `_rowid_`, `oid`. A column declared as `id INTEGER PRIMARY KEY`, even though internally flagged as `is_ipk: true`, doesn't get recognized.

Every `WHERE id = N` query flows through full table scan — O(n²) instead of O(n log n). This is consistent with the ~20,000x result.

### Bug #2: fsync on Every Statement

Every bare INSERT outside a transaction is wrapped in a full autocommit cycle. The commit calls `wal.sync()`, which calls Rust's `fsync(2)`. 100 INSERTs means 100 fsyncs.

SQLite uses `fdatasync(2)` on Linux, which skips syncing file metadata — roughly 1.6 to 2.7 times cheaper on NVMe SSDs.

### The Compound Effect

These two bugs are amplified by individually defensible "safe" choices that compound:

- **AST clone on every cache hit** — SQLite's `sqlite3_prepare_v2()` just returns a reusable handle
- **4KB heap allocation on every read** — `.to_vec()` creates a new allocation even on cache hits; SQLite returns direct pointers into pinned cache memory
- **Schema reload on every autocommit cycle** — walks the entire `sqlite_master` B-tree and re-parses every CREATE TABLE; SQLite checks a schema cookie integer
- **Eager formatting in the hot path** — AST-to-SQL formatting evaluated before guard check
- **New objects on every statement** — SQLite reuses all via a lookaside allocator

Every decision sounds like choosing safety. But the end result is about 2,900x slower. SQLite is not primarily fast because it is written in C. It is fast because **26 years of profiling** have identified which tradeoffs matter.

In the 1980 Turing Award lecture Tony Hoare said: "There are two ways of constructing a software design: one way is to make it so simple that there are obviously no deficiencies, and the other is to make it so complicated that there are no obvious deficiencies." This LLM-generated code falls into the second category. 576,000 lines of Rust — 3.7x more code than SQLite. And yet it still misses the `is_ipk` check.

### Same Method, Same Result

A second project by the same author shows the same dynamic. The solution to disk pressure from Rust build artifacts: a cleanup daemon — 82,000 lines of Rust, 192 dependencies, a 36,000-line terminal dashboard, a Bayesian scoring engine, an EWMA forecaster with PID controller, and an asset download pipeline.

To solve a problem that needs:

```
*/5 * * * * find ~/*/target -type d -name "incremental" -mtime +7 -exec rm -rf {} +
```

A one-line cron job with 0 dependencies. The pattern is the same: the code matches the *intent* but not the *problem*. The LLM generated what was described, not what was needed.

**This is the failure mode. Not broken syntax or missing semicolons. The code is syntactically and semantically correct. It does what was asked for. It just does not do what the situation requires.**

### Intent vs. Correctness: Sycophancy

AI alignment research calls it **sycophancy** — the tendency of LLMs to produce outputs that match what the user wants to hear rather than what they need to hear.

- Anthropic's "Towards Understanding Sycophancy in Language Models" (ICLR 2024): five state-of-the-art AI assistants exhibited sycophantic behavior
- **BrokenMath** (NeurIPS 2025): even GPT-5 produced sycophantic "proofs" of false theorems 29% of the time when the user implied the statement was true
- In April 2025, OpenAI rolled back a GPT-4o update that had made the model more sycophantic
- In coding, sycophancy manifests as agents that don't push back with "Are you sure?" but provide enthusiasm towards whatever the user described

### Evidence Beyond Case Studies

- **METR's randomized controlled trial** (July 2025): 16 experienced open-source developers using AI were **19% slower, not faster**. After the measured slowdown, they still believed AI had sped them up by 20%
- **GitClear's analysis** of 211 million changed lines: copy-pasted code increased while refactoring declined
- **Google's DORA 2024 report**: every 25% increase in AI adoption associated with 7.2% decrease in delivery stability
- **Mercury benchmark** (NeurIPS 2024): leading code LLMs achieve ~65% on correctness but under 50% when efficiency is also required

### What Competent Looks Like

SQLite is ~156,000 lines of C with 100% branch coverage and 100% MC/DC (the standard required for Level A aviation software). Its test suite is 590 times larger than the library.

The speed comes from deliberate decisions: zero-copy page cache, prepared statement reuse, schema cookie check (one integer), `fdatasync` instead of `fsync`, and the `iPKey` check — one line in `where.c`.

### Conclusion

LLMs are useful when the person using them knows what correct looks like. The tool is at its best when the developer can define acceptance criteria as specific, measurable conditions. Without those criteria, you are not programming but merely generating tokens and hoping.

**The vibes are not enough. Define what correct means. Then measure.**

---

### 中文

**你的 LLM 写的不是正确的代码，写的是看似合理的代码**

**作者**: Hōrōshi バガボンド (Vagabond Research)
**发布**: 2026-03-06

对数据库最简单的测试之一：对 100 行数据做主键查找。

SQLite 耗时 0.09 毫秒。LLM 生成的 Rust 重写版本耗时 1,815.43 毫秒。

不是少了个逗号！这个重写版本在最基础的数据库操作上慢了 **20,171 倍**。

代码能编译，能通过所有测试，能正确读写 SQLite 文件格式。README 声称支持 MVCC 并发写入、文件兼容性和即插即用的 C API。乍一看就像一个正常工作的数据库引擎。但它不是！

**LLM 优化的是合理性，而非正确性。在这种情况下，"合理"比"正确"慢了约 20,000 倍。**

### LLM 会说谎，数字不会

用同一个 C 基准程序编译两个库：系统 SQLite 和 Rust 重写版的 C API。相同的编译参数、WAL 模式、表结构和查询。100 行数据。

最大差距源于两个 bug：

- **无事务的 INSERT**：比批处理模式慢 1,857 倍
- **按 ID 的 SELECT**：慢 20,171 倍
- **UPDATE 和 DELETE**：都超过 2,800 倍

模式一致：任何需要数据库*查找*的操作都慢得离谱。

### Bug #1：缺失的 ipk 检查

在 SQLite 中，声明 `id INTEGER PRIMARY KEY` 时，该列成为内部 rowid 的别名——即 B-tree 键本身。`WHERE id = 5` 这样的查询会直接走 B-tree 搜索，复杂度 O(log n)。

Rust 重写版有正确的 B-tree 和二分搜索。但查询规划器对命名列从不调用它！`is_rowid_ref()` 函数只识别三个魔法字符串：`rowid`、`_rowid_`、`oid`。即使内部标记了 `is_ipk: true`，也不会被识别。

每个 `WHERE id = N` 查询都走全表扫描——O(n²) 而非 O(n log n)。这与约 20,000 倍的结果一致。

### Bug #2：每条语句都 fsync

每条事务外的 INSERT 都被包装在完整的自动提交周期中。提交调用 `wal.sync()`，进而调用 Rust 的 `fsync(2)`。100 次 INSERT 意味着 100 次 fsync。

SQLite 在 Linux 上使用 `fdatasync(2)`，跳过文件元数据同步——在 NVMe SSD 上大约快 1.6 到 2.7 倍。

### 复合效应

这两个 bug 被一系列看似合理的"安全"选择放大：

- **每次缓存命中都克隆 AST** — SQLite 的 `sqlite3_prepare_v2()` 直接返回可复用的句柄
- **每次读取都做 4KB 堆分配** — `.to_vec()` 即使在缓存命中时也创建新分配；SQLite 返回指向固定缓存内存的直接指针
- **每次自动提交都重载 schema** — 遍历整个 `sqlite_master` B-tree 并重新解析每个 CREATE TABLE；SQLite 只检查一个 schema cookie 整数
- **热路径上的急切格式化** — 在守卫检查之前就执行 AST 到 SQL 的格式化
- **每条语句都创建新对象** — SQLite 通过 lookaside 分配器复用所有对象

每个决定听起来都在选择安全。但最终结果慢了约 2,900 倍。SQLite 快主要不是因为用 C 写的，而是因为 **26 年的性能分析** 找出了哪些取舍重要。

Tony Hoare 在 1980 年图灵奖演讲中说："有两种构造软件设计的方法：一种是让它简单到显然没有缺陷，另一种是让它复杂到没有明显的缺陷。" 这个 LLM 生成的代码属于第二种。576,000 行 Rust——是 SQLite 的 3.7 倍。然而仍然缺少 `is_ipk` 检查。

### 相同方法，相同结果

同一作者的第二个项目显示了相同的模式。解决 Rust 构建产物磁盘压力的方案：一个清理守护进程——82,000 行 Rust、192 个依赖、36,000 行终端仪表板、贝叶斯评分引擎、带 PID 控制器的 EWMA 预测器、资产下载管道。

而实际需要的只是：

```
*/5 * * * * find ~/*/target -type d -name "incremental" -mtime +7 -exec rm -rf {} +
```

一行 cron 任务，0 个依赖。模式相同：代码匹配了*意图*但没有解决*问题*。LLM 生成的是被描述的东西，而不是需要的东西。

**这就是失败模式。不是语法错误或缺分号。代码在语法和语义上都是正确的。它做了被要求做的事。只是没有做实际情况需要的事。**

### 意图 vs 正确性：谄媚

AI 对齐研究称之为**谄媚（sycophancy）**——LLM 倾向于产生用户想听的输出，而非用户需要听的输出。

- Anthropic 的"理解语言模型中的谄媚"（ICLR 2024）：五个顶级 AI 助手都表现出谄媚行为
- **BrokenMath**（NeurIPS 2025）：即使 GPT-5 在用户暗示陈述为真时，29% 的情况下会产生谄媚性的错误"证明"
- 2025 年 4 月，OpenAI 回滚了让 GPT-4o 更谄媚的更新
- 在编码中，谄媚表现为不会反问"你确定吗？"而是对用户描述的任何内容都表示热情

### 案例之外的证据

- **METR 随机对照试验**（2025 年 7 月）：16 名经验丰富的开源开发者使用 AI 后**慢了 19%，而非更快**。即使已经变慢了，他们仍认为 AI 让他们快了 20%
- **GitClear 分析**（2.11 亿行变更代码）：复制粘贴的代码增加，重构减少
- **Google DORA 2024 报告**：AI 采用率每增加 25%，交付稳定性下降约 7.2%
- **Mercury 基准**（NeurIPS 2024）：顶级代码 LLM 在正确性上达到约 65%，但加入效率要求后不到 50%

### 什么叫有能力

SQLite 约 156,000 行 C 代码，100% 分支覆盖率和 100% MC/DC（A 级航空软件要求的标准）。测试套件是库的 590 倍大。

速度来自深思熟虑的决策：零拷贝页面缓存、预处理语句复用、schema cookie 检查（一个整数）、`fdatasync` 而非 `fsync`、`iPKey` 检查——`where.c` 中的一行代码。

### 结论

LLM 在使用者知道什么是正确的时候才有用。当开发者能将验收标准定义为具体的、可衡量的条件时，工具效果最佳。没有这些标准，你不是在编程，只是在生成 token 然后祈祷。

**感觉不够。定义什么是正确。然后去衡量。**
