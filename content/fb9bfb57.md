# Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing

- **ID**: fb9bfb57
- **原文链接**: https://arxiv.org/abs/2610.13823
- **PDF**: https://arxiv.org/pdf/2610.13823v1
- **作者**: Oktie Hassanzadeh, Dharmashankar Subramanian
- **日期**: 2026-10-09
- **更新**: 2026-10-09
- **分类**: infra
- **来源类型**: paper
- **标签**: arxiv, evaluation, semantic-query, benchmark-methodology, variance
- **质量评分**: 4/5
- **抓取时间**: 2026-10-13T12:21:15Z

---

## 中文导读

语义查询引擎（semantic query engine）让大模型对每一行数据判断是否满足查询条件，而现有基准通常只在 temperature 0 下运行少量执行、按单次执行的质量来比较引擎优劣。这篇论文量化的是另一个问题：同一查询再跑一次，答案会变多少。作者用 SemBench、LRO-Bench、UDA-Bench 各自的 harness 重跑全部文本与表格工作负载，记录了全部 120 万次模型调用，并重新分析了 SemBench 已发表的执行记录。

核心发现是 temperature 0 并不等于稳定：视模型而定，0.07%–10.2% 的行在五次执行之间翻转算子输出，单个任务上最高达 24.0%；查询计划会按"答案暴露的行数"指数放大这些波动（与可能世界模型的预测一致）——UDA-Bench 上只有百分之几的抽取值发生变化，却有约三分之二的最终答案不同；SemBench 已发表结果中 21% 的文本结果质量随执行改变，其中包括计划本身确定性的引擎。因此论文认定：若干逐查询的系统比较，以及 LRO-Bench 28 项实现建议测试中的 16 项，并没有被基准实际跑过的执行所定论。

机制与缓解方面：易变的行正是模型彼此之间就不一致的行；同一执行内完全相同的请求之间的不一致频率与跨执行相当；单次执行中的决策边际与推理长度可以预测哪些行会翻转。投票（voting）能降低方差但不能消除；作者设计的校准级联（calibrated cascade）在返回行发生变化的情况下仍保持正确性保证。论文最后给出了面向基准的报告规则与面向引擎的设计规则。

## 为什么值得关注

对做语义查询 / text-to-SQL / LLM 数据系统评测的人来说，这篇论文直接质疑了"temperature 0 跑一次就算数"的比较方法：单次执行不足以区分系统优劣，部分基准结论可能是方差的产物，报告基准结果时需要给出多次执行的稳定性证据。对工程侧，论文同时给出了可操作的建议——用投票降低方差、用校准级联在行输出变化时保持保证——并明确了哪些比较是"已定论"、哪些仍是开放问题，可直接用于评估方法学与引擎设计决策。

## 关键信息

- 论文标题：Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing
- 作者：Oktie Hassanzadeh, Dharmashankar Subramanian
- arXiv：https://arxiv.org/abs/2610.13823
- PDF：https://arxiv.org/pdf/2610.13823v1
- 发布时间：2026-10-09
- arXiv 分类：cs.DB, cs.AI
- 代码与数据：https://github.com/semviews/sqp-variance-study
- 关联标签：arxiv, evaluation, semantic-query, benchmark-methodology, variance

## English Abstract

Semantic query engines ask a large language model (LLM) to judge individual rows, and benchmarks compare these engines on the quality of a few executions at temperature 0. We measure how much another execution changes. We re-execute the text and tabular workloads of SemBench, LRO-Bench, and UDA-Bench through their own harnesses, log every one of 1.2 million model calls, and reanalyze SemBench's published executions. At temperature 0, between 0.07% and 10.2% of rows change their operator output over five executions, depending on the model, and up to 24.0% on one task. Plans amplify these changes exponentially in the number of rows an answer exposes, as a possible-worlds model predicts: on UDA-Bench, a few percent of extracted values change, but about two thirds of the answers do. In SemBench's published results, 21% of text results change quality between executions, including on engines whose plans are deterministic. Several per-query system comparisons, and 16 of 28 tests of LRO-Bench's implementation recommendations, are not settled by the executions the benchmarks run. Changing rows are rows on which models disagree with each other; identical requests within one execution disagree as often as across executions; and one execution's decision margin or reasoning length predicts which rows change. Voting reduces the variance but does not remove it, and a calibrated cascade keeps its guarantee while the rows it returns change. We derive reporting rules for benchmarks and design rules for engines.

## English Summary

Semantic query engines use an LLM to judge individual rows, and benchmarks typically compare engines on a few temperature-0 executions. The authors re-execute the text and tabular workloads of SemBench, LRO-Bench, and UDA-Bench through their own harnesses, log all 1.2 million model calls, and reanalyze SemBench's published executions. At temperature 0, 0.07%-10.2% of rows flip their operator output across five executions (up to 24.0% on one task), and query plans amplify these flips exponentially in the number of rows an answer exposes: on UDA-Bench a few percent of extracted values change while about two thirds of final answers do, and 21% of SemBench's published text results change quality between executions. Several per-query system comparisons, and 16 of 28 tests of LRO-Bench's implementation recommendations, are therefore not settled by the executions the benchmarks run. Voting reduces but does not remove the variance, while a calibrated cascade keeps its guarantee as the rows it returns change; the paper closes with reporting rules for benchmarks and design rules for engines.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
