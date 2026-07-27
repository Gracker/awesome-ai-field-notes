# SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents

- **ID**: dce5a2bb
- **原文链接**: https://arxiv.org/abs/2601.16746
- **PDF**: https://arxiv.org/pdf/2601.16746
- **作者**: Yuhang Wang, Yuling Shi, Mo Yang, Rongrui Zhang, Shilin He, Heng Lian, Yuting Chen, Siyu Ye, Kai Cai, Xiaodong Gu
- **日期 / 版本**: Submitted on 23 Jan 2026 (v1), last revised 7 May 2026 (this version, v4)
- **分类**: coding
- **来源类型**: paper
- **arXiv 分类**: Software Engineering (cs.SE); Computation and Language (cs.CL)
- **标签**: coding-agent, context-engineering, swe-bench, context-pruning, software-engineering, 2601-16746
- **质量评分**: 4/5
- **抓取时间**: 2026-07-27T04:25:26.452521+00:00

---

## 中文导读

论文研究软件工程 Agent 在处理代码仓库任务时的上下文选择问题标题和摘要聚焦 self-adaptive context pruning：让 coding agent 根据任务动态裁剪低价值上下文，减少长上下文带来的噪声和成本，适合作为 SWE 类 Agent 的上下文工程参考

## 为什么值得关注

SWE-Pruner 面向 coding agents 的长上下文浪费问题，动态裁剪无关上下文以提升解题效率

这篇论文值得放进 AAIF 的原因，是它把 Agent 系统里的一个具体工程问题讲清楚：论文研究软件工程 Agent 在处理代码仓库任务时的上下文选择问题标题和摘要聚焦 self-adaptive context pruning：让 coding agent 根据任务动态裁剪低价值上下文，减少长上下文带来的噪声和成本，适合作为 SWE 类 Agent 的上下文工程参考。以下内容基于 arXiv 页面元数据、摘要与条目已有摘要整理，未补充论文摘要之外的实验细节。

## 关键信息

- 论文标题：SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents
- 作者：Yuhang Wang, Yuling Shi, Mo Yang, Rongrui Zhang, Shilin He, Heng Lian, Yuting Chen, Siyu Ye, Kai Cai, Xiaodong Gu
- arXiv：https://arxiv.org/abs/2601.16746
- 发布时间 / 修订：Submitted on 23 Jan 2026 (v1), last revised 7 May 2026 (this version, v4)
- arXiv 分类：Software Engineering (cs.SE); Computation and Language (cs.CL)
- arXiv 备注：Code available from the arXiv-linked repository.
- 关联标签：coding-agent, context-engineering, swe-bench, context-pruning, software-engineering, 2601-16746

## English Abstract

LLM agents have demonstrated remarkable capabilities in software development, but their performance is hampered by long interaction contexts, which incur high API costs and latency. While various context compression approaches such as LongLLMLingua have emerged to tackle this challenge, they typically rely on fixed metrics such as PPL, ignoring the task-specific nature of code understanding. As a result, they frequently disrupt syntactic and logical structure and fail to retain critical implementation details. In this paper, we propose SWE-Pruner, a self-adaptive context pruning framework tailored for coding agents. Drawing inspiration from how human programmers "selectively skim" source code during development and debugging, SWE-Pruner performs task-aware adaptive pruning for long contexts. Given the current task, the agent formulates an explicit goal (e.g., "focus on error handling") as a hint to guide the pruning targets. A lightweight neural skimmer (0.6B parameters) is trained to dynamically select relevant lines from the surrounding context given the goal. Evaluations across four benchmarks and multiple models validate SWE-Pruner's effectiveness in various scenarios, achieving 23-54% token reduction on agent tasks like SWE-Bench Verified while even improving success rates, and up to 14.84x compression on single-turn tasks like LongCodeQA with minimal performance impact.

## English Summary

LLM agents have demonstrated remarkable capabilities in software development, but their performance is hampered by long interaction contexts, which incur high API costs and latency. While various context compression approaches such as LongLLMLingua have emerged to tackle this challenge, they typically rely on fixed metrics such as PPL, ignoring the task-specific nature of code understanding. As a result, they frequently disrupt syntactic and logical structure and fail to retain critical implementation details. In this paper, we propose SWE-Pruner, a self-adaptive context pruning framework tailored for coding agents. Drawing inspiration from how human programmers "selectively skim" source code during development and debugging, SWE-Pruner performs task-aware adaptive pruning for long contexts. Given the current task, the agent formulates an explicit goal (e.g., "focus o

## Obsidian Notes

- 内容获取路径：优先尝试 `opencli arxiv paper 2601.16746 -f json`，本轮遭遇 arXiv API HTTP 429 后，改由 arXiv 页面元数据与摘要回填。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上。
- 现代站点生成器按 `content/{entry.id}.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
