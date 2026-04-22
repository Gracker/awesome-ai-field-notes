# Your LLM Doesn't Write Correct Code. It Writes Plausible Code.

> 作者: Hōrōshi バガボンド  
> 原文链接: https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code  
> 语言: 英→中双语

---

## 中文翻译

---
![用户头像](images/img_001.jpeg)

从流浪者研究探索更多

代码猴子

订阅

通过订阅，您同意遵守Substack的[使用条款](https://substack.com/tos)，并承认其[信息收集通知](https://substack.com/ccpa#personal-data-collected)和[隐私政策](https://substack.com/privacy)。

已有账户？登录

# 你的LLM不会编写正确的代码，它会编写看似合理的代码。

[

![Hōrōshi バガボンド的头像](images/img_002.jpeg)


](https://substack.com/@katanaquant)

[Hōrōshi バガボンド](https://substack.com/@katanaquant)

2026年3月6日

73

21

12

分享

你可以对数据库进行的简单测试之一：

对100行进行主键查找。

感谢阅读流浪者研究！免费订阅以获取新帖子并支持我的工作。

订阅

SQLite耗时0.09毫秒。由LLM生成的Rust重写耗时1,815.43毫秒。

这不是一个错位的逗号！重写在一个最基本的数据库操作上慢了20,171倍。

[

![](images/img_003.png)


](https://substackcdn.com/image/fetch/$s_!3Nvv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1a72ec7-4e57-4b89-b528-0a5e402aa25c_1595x300.png)

但问题是：代码可以编译。它通过了所有的测试。它正确地读取和写入SQLite文件格式。它的README声称支持MVCC并发写入、文件兼容性和即插即用的C API。乍一看，它看起来像是一个正在工作的数据库引擎。

但它不是！

**编辑：一些读者将这个项目与[Turso/libsql](https://github.com/tursodatabase/libsql)混淆了。它们是无关的。Turso是C SQLite代码库的分支；这里分析的项目是一个开发者从头开始由LLM生成的重写。对Turso运行相同的基准测试显示性能与SQLite相当，符合成熟的分支，而不是重实现。**

LLMs在合理性上优于正确性。在这种情况下，合理性大约比正确性慢20,000倍。

我以实践者的身份写下这些，而不是批评者的身份。在超过10年的专业开发工作后，我在过去6个月内将LLMs整合到我的多个项目的日常工作中。LLMs使得任何有好奇心和独创性的人都能快速将他们的想法变为现实，我真的喜欢这一点！但我在磁盘上积累的静默错误输出、自信的破坏逻辑和看似正确但经不起推敲的代码截图表明，事情并不总是像它们看起来那样。我的结论是，LLMs在用户在生成第一行代码之前定义他们的验收标准时效果最好。

关于审查的项目：这并非对任何个别开发者的批评。我并不认识作者本人。我对他们没有任何意见。我选择这些项目是因为它们是公开的、具有代表性的，并且相对容易进行基准测试。我发现的失败模式是由工具产生的，而不是作者。METR的随机研究和GitClear的大规模仓库分析的证据表明，当输出未经严格验证时，这些问题并非仅限于某个开发者。这正是我想表达的观点！

本文讨论了在实践中这个差距看起来是什么样子：代码、基准测试、另一个案例研究以查看模式是否是偶然的，以及外部研究证实它不是一个异常值。

## **LLMs撒谎，数字不会**

我针对两个库编译了相同的C基准程序：系统SQLite和Rust重实现的C API库。相同的编译器标志、相同的WAL模式、相同的表模式、相同的查询。100行：

_基准测试源代码可在[这个仓库](https://github.com/KatanaQuant/db_bench_foo)中找到，因此您可以在自己的环境中重现比较。绝对时间会因系统负载和硬件而异。比率才是关键。_

[

![](images/img_004.png)


](https://substackcdn.com/image/fetch/$s_!b3NO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F503cef77-5d11-4c3b-8b94-ef3a09599d87_1212x811.png)

我将使用事务批处理行作为基准，因为它不像其他行那样有明显的错误，即没有WHERE子句和每条语句的同步。在这个运行中，这个基准已经是298倍，这意味着即使是最佳路径也远远落后于SQLite。任何超过298倍的情况都表明存在错误。

超出我们基准的最大差距是由两个错误驱动的：

没有事务的INSERT：批处理模式下的1,857倍与298倍。按ID选择：20,171倍。UPDATE和DELETE都超过2,800倍。模式是一致的：任何需要数据库去_找到_东西的操作都极其缓慢。

## **规划器犯的错误**

我阅读了源代码。嗯...基于我的基准测试结果，我需要阅读的部分。重实现并不小：625个文件中有576,000行Rust代码。有一个解析器、一个规划器、一个VDBE字节码引擎、一个B树、一个页面管理器、一个WAL。模块都有所有“正确”的名称。架构看起来也是正确的。但是代码中的两个错误和一些较小的问题叠加在一起：

### **错误#1：缺少ipk检查**

在SQLite中，当你声明一个表为：

```
CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT, value REAL);
```

关键规则：
- 保留所有 Markdown 格式（## 标题，### 子标题，**粗体**，```代码块```，> 块引用，- 列表，1. 编号列表等）完全不变
- 保留所有 Markdown 格式的链接和图像引用
- 不要添加任何评论或解释
- 不要省略或添加翻译内容之外的内容
- 仅输出中文翻译

要翻译的文本：

列 `id` 成为一个 [内部行 ID 的别名](https://www.sqlite.org/rowidtable.html) — B 树键本身。查询 `WHERE id = 5` 解析为直接 B 树搜索，并按 O(log n) 缩放。([我已经在这里写了一篇关于 B 树如何工作的 TLDR 文章](https://blog.katanaquant.com/p/a-dockerized-crypto-data-hub-part-cfa)。) SQLite 查询计划器文档（https://sqlite.org/queryplanner.html）指出：“查找所需行的所需时间与 logN 成正比，而不是像全表扫描那样与 N 成正比。” 这不是优化。这是 SQLite 查询优化器的一个基本设计决策：

```
# `where.c` 中的 `whereScanInit()`
if( iColumn==pIdx->pTable->iPKey ){
    iColumn = XN_ROWID;
}
```

上面的行在列名与表的 INTEGER PRIMARY KEY 列匹配时将其转换为 `XN_ROWID`。VDBE 然后触发 `SeekRowid` 操作而不是全表扫描，这使得整个过程与 logN 成正比。

Rust 的重新实现有一个正确的 B 树。`table_seek` 函数通过其节点实现正确的二分搜索下降，并按 O(log n) 缩放。它工作。但查询计划器从不为命名列调用它！

`is_rowid_ref()` 函数只识别三个魔法字符串：

```
fn is_rowid_ref(col_ref: &ColumnRef) -> bool {
    let name = col_ref.column.to_ascii_lowercase();
    name == "rowid" || name == "_rowid_" || name == "oid"
}
```

即使列声明为 `id INTEGER PRIMARY KEY`，尽管它在内部被标记为 `is_ipk: true`，也不会被识别。在决定使用 B 树搜索还是全表扫描时，它永远不会被咨询。

每个 `WHERE id = N` 查询都通过 `codegen_select_full_scan()` 流过，该函数通过 `Rewind` / `Next` / `Ne` 发出遍历每一行的线性路径，以比较每个行 ID 与目标。在 100 行和 100 次查找的情况下，这将是 10,000 次行比较，而不是大约 700 个 B 树步骤。O(n²) 而不是 O(n log n)。这与这次运行中 ~20,000 倍的结果一致。

每个列上的每个 WHERE 子句都执行全表扫描。唯一的快速路径是使用字面伪列名 `WHERE rowid = ?`。

### **第 2 个错误：每个语句的 fsync**

第二个错误是导致 INSERT 的 1,857 倍的原因。每个事务外的裸 INSERT 都被包裹在一个完整的自动提交周期中：`ensure_autocommit_txn()` → 执行 → `resolve_autocommit_txn()`。提交调用 `wal.sync()`，它调用 Rust 的 `fsync(2)` 包装器。100 个 INSERT 意味着 100 个 fsync。

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 块引用，- 列表，1. 编号列表等）完全不变
- 保留Markdown格式中的所有链接和图像引用
- 不要添加任何评论或解释
- 不要在翻译中省略或添加内容
- 仅输出中文翻译

要翻译的文本：

SQLite执行相同的自动提交，但在Linux上使用`fdatasync(2)`，当编译时带有`HAVE_FDATASYNC`（默认值）会跳过同步文件元数据。这在NVMe SSD上大约便宜了[1.6到2.7倍](http://smalldatum.blogspot.com/2020/10/innodb-fsync-and-fdatasync-reducing.html)。SQLite的每条语句开销也最小：没有模式重新加载，没有AST克隆，没有VDBE重新编译。Rust的重实现在每个调用上都执行这三个操作。

查看Rust事务批处理行，批处理插入（100次插入一次fsync）需要32.81毫秒，而单个插入（100次fsync调用）需要2,562.99毫秒。这是自动提交的78倍开销。

## **复合效应**

这两个错误不是孤立案例。它们被一系列单独可辩护的“安全”选择放大，这些选择累积：

-   **每次缓存命中时克隆AST。** SQL解析被缓存，但AST在每次`sqlite3_exec()`时都会`.clone()`，然后从头开始重新编译为VDBE字节码。SQLite的`sqlite3_prepare_v2()`只是返回一个可重用的句柄。

-   **每次读取时分配4KB（Vec<u8>）堆空间。** 页面缓存通过`.to_vec()`返回数据，即使在缓存命中时也会创建新的分配并将它复制到Vec中。SQLite返回一个[指向固定缓存内存的直接指针](https://www.sqlite.org/c3ref/pcache_methods2.html)，创建零次复制。Fjall数据库团队[https://fjall-rs.github.io/post/fjall-2-6-byteview/](https://fjall-rs.github.io/post/fjall-2-6-byteview/)测量了这种反模式在构建自定义`ByteView`类型消除之前的运行时为44%。

-   **每次自动提交周期重新加载模式。** 每条语句提交后，下一条语句会看到增加的提交计数器并调用`reload_memdb_from_pager()`，遍历`sqlite_master` B树，然后重新解析每个CREATE TABLE来重建整个内存模式。SQLite检查[schema cookie](https://sqlite.org/fileformat.html)，只有在更改时才重新加载。

-   **热路径上的贪婪格式化。** `statement_sql.to_string()`（AST到SQL格式化）在其守卫检查之前在每次调用时都会评估。这意味着它无论是否有订阅者活动都会进行序列化。

-   **每条语句创建新对象。** 每条语句都会分配一个新的`SimpleTransaction`、一个新的`VdbeProgram`、一个新的`MemDatabase`和一个新的`VdbeEngine`。SQLite通过[旁路分配器](https://www.sqlite.org/malloc.html)在整个连接生命周期中重用所有这些，以消除执行循环中的`malloc`/`free`。


每个选择可能都是基于合理的通用推理单独选择的：“我们克隆，因为Rust的所有权使共享引用变得复杂。” “我们使用sync_all，因为它是最安全的默认值。” “我们按页分配，因为从缓存返回引用需要不安全操作。”

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，1. 编号列表等）的精确格式
- 保留Markdown格式中的所有链接和图片引用
- 不要添加任何评论或解释
- 不要省略或添加翻译内容之外的内容
- 仅输出中文翻译

待翻译文本：

每个决策听起来都像是选择安全。但在这个基准测试中，最终结果要慢约2900倍。数据库的热路径是你可能不应该为了性能而选择安全的地方。SQLite之所以不是主要因为它是用C语言编写的而快速，嗯，这也有道理，但它之所以快是因为[26年的分析](https://sqlite.org/cpu.html)确定了哪些权衡是重要的。

在[1980年图灵奖演讲](https://dl.acm.org/doi/10.1145/358549.358561)中，托尼·霍尔说：“构建软件设计的两种方式：一种方式是让它如此简单，以至于显然没有缺陷；另一种方式是让它如此复杂，以至于没有明显的缺陷。”这个由LLM生成的代码属于第二种。重写后的代码是576,000行Rust（通过[scc](https://github.com/boyter/scc)测量，仅计算代码，不包含注释或空白）。这是SQLite的3.7倍。然而，它仍然缺少处理正确搜索操作选择的`is_ipk`检查。

史蒂文·斯基亚在《[算法设计手册](https://www.amazon.com/Algorithm-Design-Manual-Computer-Science/dp/3030542556?crid=2ZUP4JANEYOFR&sprefix=the+algorithm+design+manual%2Caps%2C186&sr=8-1&linkCode=ll2&tag=katanalarp-20&linkId=85494361bfe8d87d86a57b283eff0873&language=en_US&ref_=as_li_ss_tl)》中写道：“看起来合理的算法很容易是错误的。算法正确性是一个必须仔细证明的性质。”代码看起来正确是不够的。测试通过也不够。你必须通过基准测试和证明来展示系统做了它应该做的事情。576,000行代码和没有基准测试。这不是“先正确，后优化”。这根本不是正确性。

## **同样的方法，同样的结果**

SQLite的重写不是唯一的例子。同一作者的第二个项目在另一个领域展示了同样的动态。

开发者的LLM代理持续编译Rust项目，用构建工件填满磁盘。Rust的`target/`目录，增量编译和调试信息占用2-4GB，这是年度Rust调查中的[前三项投诉](https://blog.rust-lang.org/2025/02/13/2024-State-Of-Rust-Survey-results/)。这被项目本身放大：同一组合中的兄弟代理协调工具拉入了846个依赖项和393,000行Rust。为了对比，[ripgrep](https://github.com/BurntSushi/ripgrep)有61个；[sudo-rs](https://www.memorysafety.org/blog/reducing-dependencies-in-sudo/)故意从135个减少到3个。正确架构的项目是精简的。

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，1. 编号列表等）完全不变
- 保留Markdown格式中的所有链接和图片引用
- 不要添加任何评论或解释
- 不要省略或添加翻译内容
- 仅输出中文翻译

待翻译文本：

磁盘压力的解决方案：一个清理守护进程。82,000行Rust代码，192个依赖项，一个36,000行的终端仪表板，包含七个屏幕和模糊搜索命令面板，一个贝叶斯评分引擎，具有后验概率计算，一个EWMA预测器，带有PID控制器，以及一个带有镜像URL和离线包支持的资产下载管道。

要解决这个问题：

```
*/5 * * * * find ~/*/target -type d -name "incremental" -mtime +7 -exec rm -rf {} +
```

一个一行cron作业，没有依赖项。项目的README声称当磁盘填满时，机器“变得无响应”。它一次也没有提到Rust针对这个问题的标准工具：`cargo-sweep`。它也没有考虑到操作系统已经自带了负载辅助工具。ext4的[5%根预留](https://man7.org/linux/man-pages/man8/mke2fs.8.html)，默认为特权进程预留块：在一个500GB的磁盘上，即使非root用户看到“磁盘已满”，也有25GB的块可供root使用。这并不能保证没有影响，但通常意味着特权恢复路径仍然可用，因此root仍然可以登录并删除文件。

模式与SQLite重写相同。代码与意图相符：“构建一个复杂的磁盘管理系统”产生了一个复杂的磁盘管理系统。它有仪表板、算法、预测器。但删除旧构建工件的问题已经解决。LLM生成的是所描述的内容，而不是所需的内容。

这就是失败模式。不是语法错误或缺少分号。代码在语法和语义上是正确的。它做了要求的事情。但它没有做情况所需要的事情。在SQLite的情况下，意图是“实现查询规划器”，结果是每个查询都作为全表扫描的查询规划器。在磁盘守护进程的情况下，意图是“智能管理磁盘空间”，结果是82,000行智能应用于不需要智能的问题。这两个项目都满足了提示。但都没有解决问题。

明显的反论是“技能问题，更好的工程师会捕捉到全表扫描。”这是真的。这正是重点！LLM对那些最不擅长验证其输出的人是危险的。如果你有捕捉到查询规划器中的`is_ipk`错误的能力，LLM可以为你节省时间。如果你没有，你就无法知道代码是错误的。它可以编译，可以通过测试，LLM会高兴地告诉你它看起来很棒。

_**编辑：**一些读者指出，这种比较可能不公平，因为作者声称项目尚未完成，尚未准备好测试。_

**关键规则**：
- 保留所有Markdown格式（例如：## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，1. 编号列表等）。
- 保留所有Markdown格式的链接和图片引用。
- 不要添加任何评论或解释。
- 不要在翻译中省略或添加内容。
- 仅输出中文翻译。

待翻译文本：

_该重写在其作者[主动推广](https://x.com/doodlestein/status/2027199039490466225)后一周发布本文，声称使用现在时态的性能改进来提升SQLite。README自那时起已修订，以承认剩余的限制并阐明项目的当前状态[在此提交](https://github.com/Dicklesworthstone/frankensqlite/commit/b0eb450419c50a9c57d64c2e3833f297d18f0f42)和随后的提交。[这里](https://github.com/Dicklesworthstone/frankensqlite/commit/6823ad124e13c55177c91ec0403d7dad7b167f42)。_

_在撰写这个仓库时，它已经积累了超过500,000行代码，在30天的24/7 LLM工作中完成了超过1,600次提交。“未完成”通常意味着工作尚未完成，但情况并非如此。一切都已经实现，只是做错了。_

_讽刺的是，“未完成”的辩护加强了论点。LLM生成了看似完成的输出，包括完整的README、比较表和架构文档、现在时态的性能声明，并被以此方式推广。看起来像什么和实际做什么之间的差距正是重点所在。_

_主要论点不是“FrankenSQLite很糟糕”。而是：“LLM生成的代码看起来正确但实际上不是”。无论错误是否得到修复，LLM输出的样子在发布时并没有改变。_

### **衡量错误的东西**

用于衡量LLM输出的工具加强了这种错觉。[scc](https://github.com/boyter/scc)的COCOMO模型估计重写成本为2140万美元。同样的模型将`print("hello world")`的价值评估为19美元。

[

![](images/img_005.png)


](https://x.com/KatanaLarp/status/2020773807481569430)

COCOMO是为了估计编写原始代码的人类团队的工作量而设计的。应用于LLM输出时，它将数量误认为是价值。尽管如此，这些数字通常被作为生产力的证明。

[

![](images/img_006.png)


](https://x.com/garrytan/status/2029603143890391191)

这个指标并没有衡量大多数人认为它所衡量的内容。

## **意图与正确性**

意图和正确性之间的差距有一个名称。AI对齐研究将其称为**谄媚**，这描述了LLM产生输出以匹配用户想听的内容而不是需要听的内容的趋势。

Anthropic的[“Understanding Sycophancy in Language Models”](https://arxiv.org/abs/2310.13548)（ICLR 2024）论文显示，五个最先进的AI助手在多个不同的任务中表现出谄媚行为。当响应符合用户的期望时，它更有可能被人类评估者所偏好。在这些反馈上训练的模型学会了奖励一致性而非正确性。

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，1. 编号列表等）完全不变
- 保留Markdown格式中的所有链接和图片引用
- 不要添加任何评论或解释
- 不要省略或添加翻译内容之外的内容
- 仅输出中文翻译

待翻译文本：

[BrokenMath基准](https://arxiv.org/abs/2510.04721)（NeurIPS 2025 数学-人工智能研讨会）在504个样本中对形式推理进行了测试。即使GPT-5在用户暗示陈述为真时，也有29%的时间产生了谄媚的“证明”来证明错误定理。模型生成一个令人信服但错误的证明，因为用户表示结论应该是积极的。GPT-5不是一个早期模型。它也是BrokenMath表中最不谄媚的。问题是[与RLHF的结构性相关](https://arxiv.org/abs/2602.01002)：偏好数据包含一个一致性偏差。奖励模型学习将令人满意的输出评分更高，优化扩大了差距。在RLHF之前的基础模型[在一项分析中被报告为在测试的所有规模上都没有可测量的谄媚](https://www.lesswrong.com/posts/3ou8DayvDXxufkjHD/openai-api-base-models-are-not-sycophantic-at-any-size)。只有在微调之后，谄媚才进入聊天。（字面意思）

2025年4月，[OpenAI撤销了GPT-4o的更新](https://openai.com/index/sycophancy-in-gpt-4o/)，这使得模型变得更加谄媚。它对一种被描述为“棍子上的屎”的商业想法感到震惊，并支持停止精神药物。基于点赞/点踩数据的额外奖励信号“削弱了\[...\]主要奖励信号的影响力，该信号一直控制着谄媚。”

在编码的背景下，谄媚表现为Addy Osmani [在他的2026年AI编码工作流程](https://addyosmani.com/blog/ai-coding-workflow/)中描述的内容：不提出“你确定吗？”或“你考虑过...？”等反对意见的代理，而是对用户描述的任何内容都表现出热情，即使描述不完整或矛盾。

这也适用于LLM生成的评估。要求同一个LLM审查它生成的代码，它将告诉你架构是合理的，模块边界清晰，错误处理全面。有时它甚至会赞扬测试覆盖率。除非被要求，否则它不会注意到每个查询都进行了完整的表扫描。同样的RLHF奖励使得模型生成你想要听到的内容，也使得它_评估_你想要听到的。你不应该仅依赖工具本身进行审计。它作为审查员和作者一样，具有相同的偏见。

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，1. 编号列表等）完全不变
- 保留Markdown格式中的所有链接和图片引用
- 不要添加任何评论或解释
- 不要在翻译中省略或添加内容
- 仅输出中文翻译

待翻译文本：

提示LLM实现“在Rust中实现SQLite”将生成看起来像在Rust中实现SQLite的代码。它将具有正确的模块结构和函数名。但它不能神奇地生成由于有人分析了真实工作负载并找到了瓶颈而存在的性能不变量。[水星基准](https://arxiv.org/abs/2402.07844)（NeurIPS 2024）从经验上证实了这一点：领先的代码LLM在正确性方面达到约65%，但在需要效率时不到50%。

SQLite文档说INTEGER PRIMARY KEY查找速度快。它没有说如何构建使它们快速的查询规划器。这些细节存在于26年的提交历史中，这仅仅是因为真实用户遇到了真实性能瓶颈。

现在，两个案例研究并不构成证据。我听到了！当两个来自相同方法的项目显示出相同的差距时，下一步是测试是否在更广泛的群体中出现了类似的效果。下面的研究使用混合方法来减少我们的单样本偏差。

## **案例研究之外的证据**

问题变成了类似的效果是否会在更广泛的数据库中出现。最近的研究表明，它们确实会出现，尽管效果大小不同。

2025年2月，Andrej Karpathy [推文](https://x.com/karpathy/status/1886192184808149383)： “有一种新的编码方式，我称之为‘感觉编码’，你完全屈服于感觉，拥抱指数增长，并忘记代码甚至存在。”

Karpathy可能是指那些一次性周末项目（我怎么能评判他的意思呢），但感觉行业听到了其他的东西。Simon Willison [划了一条更清晰的界限](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)：“如果我不能向别人解释清楚代码的功能，我就不会将任何代码提交到我的仓库。” Willison将LLM视为“一个过于自信的代码伙伴”，它犯下“有时微妙，有时巨大”的错误，却完全自信。

当那条线没有划出来时发生的数据：

**[METR的随机对照试验](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)**（2025年7月；更新于2026年2月24日）有16位经验丰富的开源开发者参与，发现使用AI的参与者比没有使用AI的参与者**慢了19%，而不是更快**。开发者们期望AI能加快他们的速度，在已经发生测量的减速之后，他们仍然认为AI使他们加快了20%。这些不是初级开发者，而是经验丰富的开源维护者。如果即使是他们在这个设置中也无法判断，那么仅凭主观印象可能不是可靠的性能衡量标准。

**[GitClear的分析](https://www.gitclear.com/ai_assistant_code_quality_2025_research)** 对2.11亿行变更代码（2020-2024）的研究报告显示，复制粘贴的代码增加，重构代码减少。首次，复制粘贴的代码行数超过了重构代码行数。

其影响不再仅仅是“恐惧”。2025年7月，[Replit的AI代理删除了一个包含1200多名高管数据的生产数据库](https://www.theverge.com/ai/2025/7/10/replit-ai-deletes-database)，然后伪造了4000名虚构用户来掩盖删除行为。

[谷歌的DORA 2024报告](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)显示，团队层面AI采用率每增加25%，预计交付稳定性将降低7.2%。

## **什么是合格的样子**

SQLite展示了正确是什么样的，以及为什么差距如此难以缩小。

SQLite是[约156,000行C代码](https://www.sqlite.org/testing.html)。其自身文档将其列为任何类型的[前五名最广泛部署的软件模块](https://www.sqlite.org/mostdeployed.html)，全球估计有1万亿个活跃数据库。它有100%的分支覆盖率，100%的[MC/DC](https://en.wikipedia.org/wiki/Modified_condition/decision_coverage)（修改条件/决策覆盖率，是[DO-178C](https://en.wikipedia.org/wiki/DO-178C)下A级航空软件所需的标准）。其[测试套件比库大590倍](https://www.sqlite.org/testing.html)。MC/DC不仅检查每个分支是否被覆盖，而且证明每个单独的表达式独立地影响结果。这就是“测试通过”和“测试证明正确性”之间的区别。重新实现没有这两个指标。

速度来自有意的决策：

**零复制页面缓存。** `pcache`返回直接指向固定内存的指针。没有复制。生产Rust数据库也解决了这个问题。[sled](https://github.com/spacejam/sled)使用内联或Arc支持的`IVec`缓冲区，Fjall构建了一个自定义的`ByteView`类型，[redb](https://github.com/cberner/redb)在约565行中编写了一个[用户空间页面缓存](https://github.com/cberner/redb/blob/master/src/tree_store/page_store/cached_file.rs)。`.to_vec()`反模式已知并已记录。重新实现仍然使用了它。

**预编译语句重用。** `sqlite3_prepare_v2()`只编译一次。`sqlite3_step()` / `sqlite3_reset()`重用编译后的代码。SQL到字节码编译的成本几乎为零。重新实现每次调用都会重新编译。

**关键规则**：
- 保留所有Markdown格式（##标题，###子标题，**粗体**，```代码块```，>引用块，-项目符号列表，1.编号列表等）。
- 保留所有Markdown格式的链接和图片引用。
- 不要添加任何评论或解释。
- 不要省略或添加翻译内容之外的内容。
- 仅输出中文翻译。

待翻译文本：

**模式cookie检查**。使用文件头中特定偏移量处的整数来读取它并进行比较。重新实现遍历整个`sqlite_master` B树，并在每次自动提交后重新解析每个CREATE TABLE语句。

`fdatasync` **代替** `fsync**`。仅数据同步而不进行元数据日志记录可以节省每次提交的可测量时间。重新实现使用`sync_all()`，因为它是一个安全的默认值。

**iPKey检查**。`where.c`中的一行。重新实现在其`ColumnInfo`结构体中将`is_ipk: true`设置正确，但在查询规划期间从未检查它。

能力不是写576,000行代码。数据库持续（并处理）数据。这就是它所做的一切。并且它必须在规模上可靠地完成。在最常见的访问模式中，O(log n)和O(n)之间的差异不是一个优化细节，它是帮助系统在10,000、100,000甚至1,000,000行或更多行上工作的性能不变量，而不是崩溃。知道这个不变量存在于一行代码中，并知道是哪一行，这就是能力。这是知道`fdatasync`存在，并且安全的默认值并不总是正确的默认值。

## **衡量重要的事情**

`is_rowid_ref()`函数是4行Rust代码。它检查三个字符串。但它遗漏了最重要的案例：每个SQLite教程都使用且每个应用程序都依赖的命名INTEGER PRIMARY KEY列。

这个检查存在于SQLite中，因为有人，可能是20年前的Richard Hipp，分析了真实的工作负载，注意到命名主键列没有命中B树搜索路径，并在`where.c`中写了一行来修复它。这一行并不花哨。它没有出现在任何API文档中。但任何在文档和Stack Overflow答案上训练的LLM都不会神奇地知道这一点。

这就是差距！不是在C和Rust（或任何其他语言）之间。不是在旧的和新的之间。而是在由测量过的人构建的系统与由模式匹配的工具构建的系统之间。LLM产生合理的架构。它们不会产生所有关键细节。

如果你正在使用LLM编写代码（到2026年，我们中大多数人可能都在这样做），问题不是输出是否可以编译。而是你是否能自己找到错误。提示“找出所有错误并修复它们”是不起作用的。这不是一个语法错误。这是一个语义错误：错误的算法和错误的系统调用。如果你提示了代码，却无法解释为什么它选择了全表扫描而不是B树搜索，你就没有工具。直到你足够了解它以至于可以破坏它，代码才属于你。

关键规则：
- 精确保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，1. 编号列表等）
- 保留所有Markdown格式的链接和图片引用
- 不要添加任何评论或解释
- 不要省略或添加超出翻译的内容
- 仅输出中文翻译

待翻译文本：

LLMs很有用。当使用它们的人知道正确是什么样的时，它们可以创造一个非常高效的工作流程。一位经验丰富的数据库工程师使用LLM来构建B树时，会在代码审查中捕捉到`is_ipk`错误，因为他们知道查询计划应该输出什么。一位经验丰富的运维工程师永远不会接受82000行代码而不是一个cron作业的单行命令。当开发者可以将验收标准定义为具体、可衡量的条件，以帮助区分正常和错误时，这个工具表现得最好。在这种情况下，使用LLM生成解决方案可以更快且更正确。没有这些标准，你并不是在编程，而只是在生成标记并抱有希望。

感觉还不够。定义什么是正确。然后衡量。

在外面要小心！

# **\- Hōrōshi バガボンド**

* * *

本次修订的当前基准数据来自`bench.png`（在Linux x86\_64机器上捕获的100行运行）。SQLite 3.x（系统libsqlite3）与Rust重实现的C API（发布构建，-O2）比较。行数通过[scc](https://github.com/boyter/scc)（仅代码——不包括空白和注释）测量。所有源代码声明均与写作时的存储库进行核对。

* * *

## **来源**

### **主要研究**

-   Sharma, M. 等人。[“理解语言模型中谄媚的途径。”](https://arxiv.org/abs/2310.13548) ICLR 2024。

-   Shapira, Benade, Procaccia。[“RLHF如何放大谄媚。”](https://arxiv.org/abs/2602.01002) arXiv，2026。

-   BrokenMath：[“定理证明中谄媚的基准。”](https://arxiv.org/abs/2510.04721) NeurIPS 2025 数学-AI 工作坊。

-   Mercury：[“代码效率基准。”](https://arxiv.org/abs/2402.07844) NeurIPS 2024。

-   [“揭示LLM生成代码中的低效。”](https://arxiv.org/abs/2503.06327) arXiv，2025。

-   METR。[“衡量2025年早期AI对经验丰富的开源开发者生产率的影响。”](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) 2025年7月（更新于2026年2月24日）。

-   GitClear。[“2025年AI代码质量研究。”](https://www.gitclear.com/ai_assistant_code_quality_2025_research) 2025。

-   Google。[“DORA报告2024。”](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) 2024。


### **行业评论**

-   Osmani, A。[“我的2026年LLM编码工作流程。”](https://addyosmani.com/blog/ai-coding-workflow/) addyosmani.com。

-   Willison, S。[“我是如何使用LLM进行代码开发的。”](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) 2025年3月。

-   OpenAI。[“GPT-4o中的谄媚：发生了什么。”](https://openai.com/index/sycophancy-in-gpt-4o/) 2025年4月。

**重要规则**：
- 精确保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 块引用，- 列表，1. 编号列表等）
- 保留所有Markdown格式的链接和图片引用
- 不要添加任何评论或解释
- 不要在翻译中省略或添加内容
- 仅输出中文翻译

待翻译文本：

-   Karpathy, A. [“Vibe Coding.”](https://x.com/karpathy/status/1886192184808149383) 2025年2月2日。

### **事件**

-   Replit数据库删除。[The Verge](https://www.theverge.com/ai/2025/7/10/replit-ai-deletes-database)，2025年7月。

### **Rust生态系统**

-   Rust基金会。[“2024年Rust调查结果。”](https://blog.rust-lang.org/2025/02/13/2024-State-Of-Rust-Survey-results/) 2025年2月。

-   ISRG / Thalheim, J. [“在sudo-rs中减少依赖。”](https://www.memorysafety.org/blog/reducing-dependencies-in-sudo/) memorysafety.org。

### **数据库工程**

-   SQLite文档：[rowidtable.html](https://www.sqlite.org/rowidtable.html)，[queryplanner.html](https://www.sqlite.org/queryplanner.html)，[cpu.html](https://sqlite.org/cpu.html)，[testing.html](https://www.sqlite.org/testing.html)，[mostdeployed.html](https://www.sqlite.org/mostdeployed.html)，[malloc.html](https://sqlite.org/malloc.html)，[cintro.html](https://sqlite.org/cintro.html)，[pcache\_methods2](https://www.sqlite.org/c3ref/pcache_methods2.html)，[fileformat.html](https://sqlite.org/fileformat.html)，[fileformat2.html](https://sqlite.org/fileformat2.html)

-   Callaghan, M. [“InnoDB, fsync和fdatasync — 减少提交延迟。”](http://smalldatum.blogspot.com/2020/10/innodb-fsync-and-fdatasync-reducing.html) Small Datum，2020。

-   Gunther, N. [“通用可扩展性定律。”](https://www.perfdynamics.com/Manifesto/USLscalability.html) perfdynamics.com。

-   Fjall. [“ByteView: 消除.to\_vec()反模式。”](https://fjall-rs.github.io/post/fjall-2-6-byteview/) fjall-rs.github.io。

-   [sled](https://github.com/spacejam/sled) — 嵌入式数据库，支持inline或Arc-backed IVec。

-   [redb](https://github.com/cberner/redb) — 纯Rust嵌入式数据库，具有用户空间页面缓存。

### **参考文献**

-   Skiena, S.S. _[算法设计手册。](https://www.amazon.com/Algorithm-Design-Manual-Computer-Science/dp/3030542556?crid=2ZUP4JANEYOFR&sprefix=the+algorithm+design+manual%2Caps%2C186&sr=8-1&linkCode=ll2&tag=katanalarp-20&linkId=85494361bfe8d87d86a57b283eff0873&language=en_US&ref_=as_li_ss_tl)_ 第3版。Springer，2020。

-   Winand, M. _[SQL性能解释。](https://www.amazon.com/Performance-Explained-Everything-Developers-about/dp/3950307826?crid=2VNI4OOTWLX0T&sprefix=sql+performance+explained%2Caps%2C190&sr=8-1&linkCode=ll2&tag=katanalarp-20&linkId=206fbed47a442c5c79d2a43e283967b0&language=en_US&ref_=as_li_ss_tl)_ 自出版，2012。

-   Hoare, C.A.R. [“皇帝的新装。”](https://dl.acm.org/doi/10.1145/358549.358561) _Communications of the ACM_ 24(2)，1981。（1980年图灵奖演讲）


感谢阅读Vagabond Research！免费订阅以获取新文章并支持我的工作。

订阅

* * *

#### 订阅流浪研究

作者：Hōrōshi バガボンド

代码猴子

订阅

通过订阅，您同意遵守Substack的[使用条款](https://substack.com/tos)，并承认其[信息收集通知](https://substack.com/ccpa#personal-data-collected)和[隐私政策](https://substack.com/privacy)。

[

![Abed的头像](images/img_007.jpeg)


](https://substack.com/profile/263692805-abed)[

![a9x的头像](images/img_008.png)


](https://substack.com/profile/25110200-a9x)[

![Freemen Muad'dib的头像](images/img_009.png)


](https://substack.com/profile/147710568-freemen-muaddib)[

![bharat的头像](images/img_010.png)


](https://substack.com/profile/2048737-bharat)[

![jacket的头像](images/img_011.jpeg)


](https://substack.com/profile/13988168-jacket)

73个赞∙

[12次重装](https://substack.com/note/p-190103552/restacks?utm_source=substack&utm_content=facepile-restacks)

73

21

12

分享

上一页下一页

---

## English Original

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

73

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

THIS is the failure mode. Not broken syntax or missing semicolons. The code is syntactically and semantically correct. It does what was asked for. It just does not do what the situation _requires_. In the SQLite case, the intent was “implement a query planner” and the result is a query planner that plans every query as a full table scan. In the disk daemon case, the intent was “manage disk space intelligently” and the result is 82,000 lines of intelligence applied to a problem that needs none. Both projects fulfill the prompt. Neither solves the problem.

The obvious counterargument is “skill issue, a better engineer would have caught the full table scan.” And that’s true. That’s exactly the point! LLMs are dangerous to people least equipped to verify their output. If you have the skills to catch the `is_ipk` bug in your query planner, the LLM saves you time. If you don’t, you have no way to know the code is wrong. It compiles, it passes tests, and the LLM will happily tell you that it looks great.

_**EDIT:** Some readers have pointed out that the comparison might be unfair with the author claiming the project wasn’t finished and ready for testing yet._

_The rewrite got [actively promoted by its author](https://x.com/doodlestein/status/2027199039490466225) 1 week before the release of this article using present-tense performance improvement claims over SQLite. The README has since been revised to acknowledge remaining limitations and clarify the project’s current state [in this commit](https://github.com/Dicklesworthstone/frankensqlite/commit/b0eb450419c50a9c57d64c2e3833f297d18f0f42) and [subsequent ones.](https://github.com/Dicklesworthstone/frankensqlite/commit/6823ad124e13c55177c91ec0403d7dad7b167f42)_

_At the time of writing the repository in question had amassed over 500k lines of code in over 1,600 commits made over 30 days of 24/7 LLM work. “Not finished” usually means work hasn’t been done yet but that’s not the case. Everything was already implemented. It was just wrong._

_Ironically the “not finished” defense reinforces the thesis. The LLM produced output that looked finished with a complete README, comparison tables and architectural documentation, present-tense performance claims, and was promoted as such. The gap between what it looks like and what it does is exactly the point._

_The main thesis is not “FrankenSQLite is bad”. It is: “LLMs produce code that looks correct but isn’t”. Whether the bugs get fixed doesn’t change what the LLM output looked like when it shipped._

### **Measuring the Wrong Thing**

The tools used to measure LLM output reinforce the illusion. [scc](https://github.com/boyter/scc)‘s COCOMO model estimates the rewrite at $21.4 million in development cost. The same model values `print("hello world")` at $19.

[

![](images/img_005.png)


](https://x.com/KatanaLarp/status/2020773807481569430)

COCOMO was designed to estimate effort for human teams writing original code. Applied to LLM output, it mistakes volume for value. Still these numbers are often presented as proof of productivity.

[

![](images/img_006.png)


](https://x.com/garrytan/status/2029603143890391191)

The metric is not measuring what most think it is measuring.

## **Intent vs. Correctness**

This gap between intent and correctness has a name. AI alignment research calls it **sycophancy**, which describes the tendency of LLMs to produce outputs that match what the user wants to hear rather than what they need to hear.

Anthropic’s [“Towards Understanding Sycophancy in Language Models”](https://arxiv.org/abs/2310.13548) (ICLR 2024) paper showed that five state-of-the-art AI assistants exhibited sycophantic behavior across a number of different tasks. When a response matched a user’s expectation, it was more likely to be preferred by human evaluators. The models trained on this feedback learned to reward agreement over correctness.

The [BrokenMath benchmark](https://arxiv.org/abs/2510.04721) (NeurIPS 2025 Math-AI Workshop) tested this in formal reasoning across 504 samples. Even GPT-5 produced sycophantic “proofs” of false theorems 29% of the time when the user implied the statement was true. The model generates a convincing but false proof because the user signaled that the conclusion should be positive. GPT-5 is not an early model. It’s also the least sycophantic in the BrokenMath table. The problem is [structural to RLHF](https://arxiv.org/abs/2602.01002): preference data contains an agreement bias. Reward models learn to score agreeable outputs higher, and optimization widens the gap. Base models before RLHF [were reported in one analysis to show no measurable sycophancy across tested sizes](https://www.lesswrong.com/posts/3ou8DayvDXxufkjHD/openai-api-base-models-are-not-sycophantic-at-any-size). Only after fine-tuning did sycophancy enter the chat. (literally)

In April 2025, [OpenAI rolled back a GPT-4o update](https://openai.com/index/sycophancy-in-gpt-4o/) that had made the model more sycophantic. It was flabbergasted by a business idea described as “shit on a stick” and endorsed stopping psychiatric medication. An additional reward signal based on thumbs-up/thumbs-down data “weakened the influence of \[...\] primary reward signal, which had been holding sycophancy in check.”

In the context of coding, sycophancy manifests as what Addy Osmani [described in his 2026 AI coding workflow](https://addyosmani.com/blog/ai-coding-workflow/): agents that don’t push back with “Are you sure?” or “Have you considered...?” but instead provide enthusiasm towards whatever the user described, even when the description was incomplete or contradictory.

This also applies to LLM-generated evaluation. Ask the same LLM to review the code it generated and it will tell you the architecture is sound, the module boundaries clean and the error handling is thorough. It will sometimes even praise the test coverage. It will not notice that every query does a full table scan if not asked for. The same RLHF reward that makes the model generate what you want to hear makes it _evaluate_ what you want to hear. You should not rely on the tool alone to audit itself. It has the same bias as a reviewer as it has as an author.

An LLM prompted to “implement SQLite in Rust” will generate code that looks like an implementation of SQLite in Rust. It will have the right module structure and function names. But it can not magically generate the performance invariants that exist because someone profiled a real workload and found the bottleneck. The [Mercury benchmark](https://arxiv.org/abs/2402.07844) (NeurIPS 2024) confirmed this empirically: leading code LLMs achieve ~65% on correctness but under 50% when efficiency is also required.

The SQLite documentation says INTEGER PRIMARY KEY lookups are fast. It does not say how to build a query planner that makes them fast. Those details live in 26 years of commit history that only exists because real users hit real performance walls.

Now 2 case studies are not proof. I hear you! When two projects from the same methodology show the same gap, the next step is to test whether similar effects appear in the broader population. The studies below use mixed methods to reduce our single-sample bias.

## **Evidence Beyond Case Studies**

The question becomes whether similar effects show up in broader datasets. Recent studies suggest they do, though effect sizes vary.

In February 2025, Andrej Karpathy [tweeted](https://x.com/karpathy/status/1886192184808149383): “There’s a new kind of coding I call ‘vibe coding’, where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.”

Karpathy probably meant it for throwaway weekend projects (who am I to judge what he means anyway), but it feels like the industry heard something else. Simon Willison [drew the line more clearly](https://simonwillison.net/2025/Mar/11/using-llms-for-code/): “I won’t commit any code to my repository if I couldn’t explain exactly what it does to somebody else.” Willison treats LLMs as “an over-confident pair programming assistant” that makes mistakes “sometimes subtle, sometimes huge” with complete confidence.

The data on what happens when that line is not drawn:

**[METR’s randomized controlled trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)** (July 2025; updated February 24, 2026) with 16 experienced open-source developers found that participants using AI were **19% slower, not faster**. Developers expected AI to speed them up, and after the measured slowdown had already occurred, they still believed AI had sped them up by 20%. These were not junior developers but experienced open-source maintainers. If even THEY could not tell in this setup, subjective impressions alone are probably not a reliable performance measure.

**[GitClear’s analysis](https://www.gitclear.com/ai_assistant_code_quality_2025_research)** of 211 million changed lines (2020–2024) reported that copy-pasted code increased while refactoring declined. For the first time ever, copy-pasted lines exceeded refactored lines.

The implications are no longer just a “fear”. In July 2025, [Replit’s AI agent deleted a production database](https://www.theverge.com/ai/2025/7/10/replit-ai-deletes-database) containing data for 1,200+ executives, then fabricated 4,000 fictional users to mask the deletion.

[Google’s DORA 2024 report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) reported that every 25% increase in AI adoption at the team level was associated with an estimated 7.2% decrease in delivery stability.

## **What Competent Looks Like**

SQLite shows what correct looks like and why the gap is so hard to close.

SQLite is [~156,000 lines of C](https://www.sqlite.org/testing.html). Its own documentation places it among the [top five most deployed software modules](https://www.sqlite.org/mostdeployed.html) of any type, with an estimated one trillion active databases worldwide. It has 100% branch coverage and 100% [MC/DC](https://en.wikipedia.org/wiki/Modified_condition/decision_coverage) (Modified Condition/Decision Coverage the standard required for Level A aviation software under [DO-178C](https://en.wikipedia.org/wiki/DO-178C)). Its [test suite is 590 times larger](https://www.sqlite.org/testing.html) than the library. MC/DC does not just check that every branch is covered. but proves that every individual expression independently affects the outcome. That’s the difference between “the tests pass” and “the tests prove correctness.” The reimplementation has neither metric.

The speed comes from deliberate decisions:

**Zero-copy page cache.** The `pcache` returns direct pointers into pinned memory. No copies. Production Rust databases have solved this too. [sled](https://github.com/spacejam/sled) uses inline-or-Arc-backed `IVec` buffers, Fjall built a custom `ByteView` type, [redb](https://github.com/cberner/redb) wrote a [user-space page cache](https://github.com/cberner/redb/blob/master/src/tree_store/page_store/cached_file.rs) in ~565 lines. The `.to_vec()` anti-pattern is known and documented. The reimplementation used it anyway.

**Prepared statement reuse.** `sqlite3_prepare_v2()` compiles once. `sqlite3_step()` / `sqlite3_reset()` reuse the compiled code. The cost of SQL-to-bytecode compilation cancels out to near zero. The reimplementation recompiles on every call.

**Schema cookie check.** uses one integer at a specific offset in the file header to read it and compare it. The reimplementation walks the entire `sqlite_master` B-tree and re-parses every CREATE TABLE statement after every autocommit.

`fdatasync` **instead of** `fsync`**.** Data-only sync wihtout metadata journaling saves measurable time per commit. The reimplementation uses `sync_all()` because it is the safe default.

**The** `iPKey` **check.** One line in `where.c`. The reimplementation has `is_ipk: true` set correctly in its `ColumnInfo` struct but never checks it during query planning.

Competence is not writing 576,000 lines. A database persists (and processes) data. That is all it does. And it must do it reliably at scale. The difference between O(log n) and O(n) on the most common access pattern is not an optimization detail, it is the performance invariant that helps the system work at 10,000, 100,000 or even 1,000,000 or more rows instead of collapsing. Knowing that this invariant lives in one line of code, and knowing which line, is what competence means. It is knowing that `fdatasync` exists and that the safe default is not always the right default.

## **Measure What Matters**

The `is_rowid_ref()` function is 4 lines of Rust. It checks three strings. But it misses the most important case: the named INTEGER PRIMARY KEY column that every SQLite tutorial uses and every application depends on.

That check exists in SQLite because someone, probably Richard Hipp 20 years ago, profiled a real workload, noticed that named primary key columns were not hitting the B-tree search path, and wrote one line in `where.c` to fix it. The line is not fancy. It doesn’t appear in any API documentation. But no LLM trained on documentation and Stack Overflow answers will magically know about it.

That’s the gap! Not between C and Rust (or any other language). Not between old and new. But between systems that were built by people who measured, and systems that were built by tools that pattern-match. LLMs produce plausible architecture. They do not produce all the critical details.

If you are using LLMs to write code (which in 2026 probably most of us are), the question is not whether the output compiles. It is whether you could find the bug yourself. Prompting with “find all bugs and fix them” won’t work. This is not a syntax error. It is a semantic bug: the wrong algorithm and the wrong syscall. If you prompted the code and cannot explain why it chose a full table scan over a B-tree search, you do not have a tool. The code is not yours until you understand it well enough to break it.

LLMs are useful. They make for a very productive flow when the person using them knows what correct looks like. An experienced database engineer using an LLM to scaffold a B-tree would have caught the `is_ipk` bug in code review because they know what a query plan _should_ emit. An experienced ops engineer would never have accepted 82,000 lines instead of a cron job one-liner. The tool is at its best when the developer can define the acceptance criteria as specific, measurable conditions that help distinguish working from broken. Using the LLM to generate the solution in this case can be faster while also being correct. Without those criteria, you are not programming but merely generating tokens and hoping.

The vibes are not enough. Define what correct means. Then measure.

Stay safe out there!

# **\- Hōrōshi バガボンド**

* * *

_Current benchmark figures in this revision are from the 100-row run shown in_ `bench.png` _(captured on a Linux x86\_64 machine). SQLite 3.x (system libsqlite3) vs. the Rust reimplementation’s C API (release build, -O2). Line counts measured via [scc](https://github.com/boyter/scc) (code only — excluding blanks and comments). All source code claims verified against the repository at time of writing._

* * *

## **Sources**

### **Primary Research**

-   Sharma, M. et al. [“Towards Understanding Sycophancy in Language Models.”](https://arxiv.org/abs/2310.13548) ICLR 2024.

-   Shapira, Benade, Procaccia. [“How RLHF Amplifies Sycophancy.”](https://arxiv.org/abs/2602.01002) arXiv, 2026.

-   BrokenMath: [“A Benchmark for Sycophancy in Theorem Proving.”](https://arxiv.org/abs/2510.04721) NeurIPS 2025 Math-AI Workshop.

-   Mercury: [“A Code Efficiency Benchmark.”](https://arxiv.org/abs/2402.07844) NeurIPS 2024.

-   [“Unveiling Inefficiencies in LLM-Generated Code.”](https://arxiv.org/abs/2503.06327) arXiv, 2025.

-   METR. [“Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.”](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) July 2025 (updated February 24, 2026).

-   GitClear. [“AI Code Quality Research 2025.”](https://www.gitclear.com/ai_assistant_code_quality_2025_research) 2025.

-   Google. [“DORA Report 2024.”](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) 2024.


### **Industry Commentary**

-   Osmani, A. [“My LLM Coding Workflow Going Into 2026.”](https://addyosmani.com/blog/ai-coding-workflow/) addyosmani.com.

-   Willison, S. [“How I Use LLMs for Code.”](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) March 2025.

-   OpenAI. [“Sycophancy in GPT-4o: What Happened.”](https://openai.com/index/sycophancy-in-gpt-4o/) April 2025.

-   Karpathy, A. [“Vibe Coding.”](https://x.com/karpathy/status/1886192184808149383) February 2, 2025.


### **Incidents**

-   Replit database deletion. [The Verge](https://www.theverge.com/ai/2025/7/10/replit-ai-deletes-database), July 2025.


### **Rust Ecosystem**

-   Rust Foundation. [“2024 State of Rust Survey Results.”](https://blog.rust-lang.org/2025/02/13/2024-State-Of-Rust-Survey-results/) February 2025.

-   ISRG / Thalheim, J. [“Reducing Dependencies in sudo-rs.”](https://www.memorysafety.org/blog/reducing-dependencies-in-sudo/) memorysafety.org.


### **Database Engineering**

-   SQLite Documentation: [rowidtable.html](https://www.sqlite.org/rowidtable.html), [queryplanner.html](https://www.sqlite.org/queryplanner.html), [cpu.html](https://sqlite.org/cpu.html), [testing.html](https://www.sqlite.org/testing.html), [mostdeployed.html](https://www.sqlite.org/mostdeployed.html), [malloc.html](https://www.sqlite.org/malloc.html), [cintro.html](https://sqlite.org/cintro.html), [pcache\_methods2](https://www.sqlite.org/c3ref/pcache_methods2.html), [fileformat.html](https://sqlite.org/fileformat.html), [fileformat2.html](https://sqlite.org/fileformat2.html)

-   Callaghan, M. [“InnoDB, fsync and fdatasync — Reducing Commit Latency.”](http://smalldatum.blogspot.com/2020/10/innodb-fsync-and-fdatasync-reducing.html) Small Datum, 2020.

-   Gunther, N. [“Universal Scalability Law.”](https://www.perfdynamics.com/Manifesto/USLscalability.html) perfdynamics.com.

-   Fjall. [“ByteView: Eliminating the .to\_vec() Anti-Pattern.”](https://fjall-rs.github.io/post/fjall-2-6-byteview/) fjall-rs.github.io.

-   [sled](https://github.com/spacejam/sled) — embedded database with inline-or-Arc-backed IVec.

-   [redb](https://github.com/cberner/redb) — pure-Rust embedded database with user-space page cache.


### **Books Referenced**

-   Skiena, S.S. _[The Algorithm Design Manual.](https://www.amazon.com/Algorithm-Design-Manual-Computer-Science/dp/3030542556?crid=2ZUP4JANEYOFR&sprefix=the+algorithm+design+manual%2Caps%2C186&sr=8-1&linkCode=ll2&tag=katanalarp-20&linkId=85494361bfe8d87d86a57b283eff0873&language=en_US&ref_=as_li_ss_tl)_ 3rd ed. Springer, 2020.

-   Winand, M. _[SQL Performance Explained.](https://www.amazon.com/Performance-Explained-Everything-Developers-about/dp/3950307826?crid=2VNI4OOTWLX0T&sprefix=sql+performance+explained%2Caps%2C190&sr=8-1&linkCode=ll2&tag=katanalarp-20&linkId=206fbed47a442c5c79d2a43e283967b0&language=en_US&ref_=as_li_ss_tl)_ Self-published, 2012.

-   Hoare, C.A.R. [“The Emperor’s Old Clothes.”](https://dl.acm.org/doi/10.1145/358549.358561) _Communications of the ACM_ 24(2), 1981. (1980 Turing Award Lecture)


Thanks for reading Vagabond Research! Subscribe for free to receive new posts and support my work.

Subscribe

* * *

#### Subscribe to Vagabond Research

By Hōrōshi バガボンド

code monkey

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[

![Abed's avatar](images/img_007.jpeg)


](https://substack.com/profile/263692805-abed)[

![a9x's avatar](images/img_008.png)


](https://substack.com/profile/25110200-a9x)[

![Freemen Muad'dib's avatar](images/img_009.png)


](https://substack.com/profile/147710568-freemen-muaddib)[

![bharat's avatar](images/img_010.png)


](https://substack.com/profile/2048737-bharat)[

![jacket's avatar](images/img_011.jpeg)


](https://substack.com/profile/13988168-jacket)

73 Likes∙

[12 Restacks](https://substack.com/note/p-190103552/restacks?utm_source=substack&utm_content=facepile-restacks)

73

21

12

Share

PreviousNext