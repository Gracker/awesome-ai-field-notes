# MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing

- **ID**: cf1b67ac
- **原文链接**： https://arxiv.org/abs/2611.33119
- **PDF**: https://arxiv.org/pdf/2611.33119v1
- **作者**： Scott Piersall, Yang Gao, Shenyang Liu, Liqiang Wang
- **日期**： 2026-11-24
- **更新**： 2026-11-24
- **分类**： coding
- **来源类型**： paper
- **标签**： meta-learning, code-generation, mpi, skill-optimization
- **质量评分**： 4/5
- **抓取时间**： 2026-11-26T12:21:23Z

---

## 中文导读

MetaFORGE 面向 MPI C 并行代码生成，把提示工程做成执行驱动的元学习：正确性测试编译诊断静态分析运行时与进程级负载不均衡数据折叠成标量奖励，驱动对持久化自然语言技能规格的文本梯度精炼；外部记忆跨轮次沉淀并检索被奖励验证过的优化知识六个 MPI 任务三种负载规模上，其静态分析质量运行时与负载均衡均优于零样本生成，总体超过 TextGrad 迭代基线；精炼模型降到 gpt-4o 优势仍在防泄漏的留出与零更新实验支持优化知识确实留存在技能与外部记忆中

## 为什么值得关注

Execution-grounded meta-learning evolves persistent skill specs for MPI C codegen, beating TextGrad with external memory

Fetched from arXiv (cs.AI; submitted 2026-11-24): the abstract describes execution-grounded meta-learning that folds correctness tests, compiler diagnostics, static analysis, runtime and process-level load imbalance into a scalar reward to iteratively refine persistent natural-language skill specs for MPI C code generation, with external memory carrying validated optimization knowledge across runs.

## 关键信息

- 论文标题： MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for Parallel Computing
- 作者： Scott Piersall, Yang Gao, Shenyang Liu, Liqiang Wang
- arXiv： https://arxiv.org/abs/2611.33119
- PDF： https://arxiv.org/pdf/2611.33119v1
- 发布时间： 2026-11-24
- arXiv 分类： c, s, ., A, I
- 关联标签： meta-learning, code-generation, mpi, skill-optimization

## English Abstract

Large language models (LLMs) can generate parallel programs, but their correctness and performance depend strongly on the instructions that guide generation. We present \textsc{MetaFORGE}, an execution-grounded meta-learning framework that iteratively optimizes persistent natural-language skill specifications for MPI C code generation. \textsc{MetaFORGE} combines correctness testing, compiler diagnostics, static-analysis findings, runtime measurements, and rank-level load-imbalance profiles into a scalar reward that drives textual-gradient refinement, while an external memory distills and retrieves reward-supported optimization knowledge across runs. Across six MPI tasks and three workload sizes, \textsc{MetaFORGE} improves static-analysis quality, runtime, and load balance relative to zero-shot generation and generally exceeds the evaluated \textsc{TextGrad} iterative baseline. A model-matched refinement ablation shows that the MetaFORGE advantage persists when its refinement model is reduced to \texttt{gpt-4o}. An expanded retrieval ablation across all 18 task--workload configurations shows consistent runtime benefit and broad static-analysis and load-balance benefit from retrieved context. Leakage-controlled held-out and zero-update experiments further provide evidence that optimization knowledge persists in both the transferred skill and external memory under the evaluated protocol.

## English Summary

LLM-generated parallel programs live or die on the instructions guiding generation. MetaFORGE iteratively optimizes persistent natural-language skill specifications for MPI C code generation with execution-grounded meta-learning: correctness tests, compiler diagnostics, static analysis, runtime and rank-level load-imbalance data fold into a scalar reward driving textual-gradient refinement; an external memory distills and retrieves reward-supported optimization knowledge across runs. Across six MPI tasks and three workload sizes it improves static-analysis quality, runtime, and load balance over zero-shot generation, generally exceeding the TextGrad baseline; the advantage persists with the refinement model reduced to gpt-4o. Leakage-controlled held-out and zero-update experiments support that optimization knowledge persists in both the transferred skill and the external memory.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- Grounded only in arXiv metadata (title, authors, dates, categories, abstract) and the entry's existing summaries; no experimental details beyond the abstract were added.
