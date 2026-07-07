# AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents

> External-scan entry · 2026-07-07 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.02255
- **Source**: arxiv · Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, Zizhen Li, Chuanhao Li, Xiangcheng Cao, Yihao Liu, Fanru...
- **Original Date**: 2026-07-03
- **Added**: 2026-07-07
- **Category**: agents
- **Tags**: long-horizon-agent, memory-ablation, agent-eval, bounded-memory
- **Quality Score**: 4

## 中文摘要

长程 LLM Agent 的记忆本质上是一份「未来每一步能看到什么」的契约。最简单的契约是把历史观测、工具调用、反思全部 append 到 prompt，访问容易但变成了混乱的混合物，单一记忆组件的贡献难以隔离。作者提出并实现一个有界契约（bounded-memory）测试床 AgenticSTS，把每条记忆显式声明为固定大小的 budget、显式记录淘汰策略，让研究者可以系统化 ablation 任何一条记忆对最终决策的影响，而不是被迫接受全集 prompt 的混杂效应。

## English Abstract

Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded across runs of any length, and any single layer can be ablated in isolation. We instantiate the contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require hundreds of tactical and strategic decisions....

## One-liner

长程 LLM Agent 的记忆本质上是一份「未来每一步能看到什么」的契约。

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
