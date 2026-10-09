# RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing

- **ID**: dae6cad6
- **原文链接**: https://arxiv.org/abs/2610.10507
- **PDF**: https://arxiv.org/pdf/2610.10507
- **作者**: Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi, Craig Boutilier, Chuchu Fan
- **日期**: 7 Oct 2026
- **更新**: N/A
- **分类**: agents
- **来源类型**: paper
- **标签**: rag, evidence-routing, context-engineering, tool-use, grpo
- **质量评分**: 4/5
- **抓取时间**: 2026-10-09T04:29:21Z
- **元数据来源**: arXiv abs 页面（HTTP 429 回退）

---

## 中文导读

很多任务的证据不在任何单条来源里，要跨多条来源做过滤聚合甚至计算才能得到，而传统 RAG 停在相似度检索agentic 变体也仍以检索为中心RECAST 把证据构建建成异构检索与计算操作上的序贯决策过程：轻量 RouterLM 迭代选择并表述原语操作，或为冻结的 CompilerLM 定制操作再编译成可执行代码，判断证据足够后交给冻结的 AnswerLM 产出答案；RouterLM 先 SFT 再 GRPO 训练六个异构基准族平均成功率 75.6%，超最强 large-model 基线 15.9%；训练后的 Qwen3.5-9B RouterLM 反超免训练的 Gemini 3.5 Flash RouterLM 5.0%；三个 held-out 基准上平均再超最强基线 15.0%，展示跨任务跨异构来源表示的零样本泛化

## 为什么值得关注

条目一句话：证据靠算出来不靠检索出来：RouterLM 学会调度计算操作，六基准族 +15.9%

证据可以靠计算操作构造，绕开相似度检索的天花板。摘要报告：六基准族平均成功率 75.6%，超最强 large-model 基线 15.9%；三个 held-out 基准平均 +15.0%；9B RouterLM 经 SFT+GRPO 训练后反超免训练 Gemini 3.5 Flash RouterLM 5.0%。context engineering 路线从检索转向计算的直接证据。

## 关键信息

- 论文标题：RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing
- 作者：Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi, Craig Boutilier, Chuchu Fan
- arXiv：https://arxiv.org/abs/2610.10507
- 发布时间：7 Oct 2026
- arXiv 分类：Artificial Intelligence (cs.AI)
- 关联标签：rag, evidence-routing, context-engineering, tool-use, grpo

## English Abstract

Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic variants adapt queries and tool use but remain largely retrieval-centric. However, in many tasks, the evidence required for a solution is not explicitly present in any single source item. Instead, it must be derived through filtering, aggregation, or computation across multiple source items. In this work, we introduce RECAST (Routing Evidence through Computation, Access, and Synthesized Tools), a learned framework that formulates evidence construction as a sequential decision process over heterogeneous retrieval and computation operations, allowing evidence to be actively derived rather than merely retrieved. A lightweight RouterLM iteratively selects and formulates primitive operations or specifies customized operations for a frozen CompilerLM to translate into executable code. Once it judges the evidence sufficient, RouterLM passes the accepted evidence to a frozen AnswerLM to produce the final solution. We train RouterLM with supervised fine-tuning (SFT) followed by group relative policy optimization (GRPO). Across six heterogeneous benchmark families, RECAST achieves a mean success rate of 75.6%, outperforming the strongest large-model baseline by 15.9%. Moreover, training enables the Qwen3.5-9B RouterLM to outperform a training-free Gemini 3.5 Flash RouterLM by 5.0%. On three held-out benchmarks, RECAST improves over the strongest baseline by 15.0% on average, demonstrating strong zero-shot generalization across tasks and heterogeneous source representations.

## English Summary

In many tasks the evidence needed for a solution is not present in any single source item - it must be derived through filtering, aggregation, or computation across items - yet conventional RAG stays similarity-centric and agentic variants remain retrieval-centric. RECAST formulates evidence construction as a sequential decision process over heterogeneous retrieval and computation operations: a lightweight RouterLM iteratively selects and formulates primitive operations or specifies custom ones for a frozen CompilerLM to translate into executable code, then hands accepted evidence to a frozen AnswerLM; RouterLM is trained with SFT followed by GRPO....

## Obsidian Notes

- 内容获取路径：优先尝试 `opencli arxiv paper 2610.10507 -f json`；如遇 arXiv API HTTP 429，则改由 arXiv abs 页面元数据与摘要回填。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 本文件写入 canonical content 目录（content/{id}.md），而非 openclaw/content/（project_root symlink 陷阱）。
