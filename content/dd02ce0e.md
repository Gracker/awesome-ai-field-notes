# RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States

- **ID**: dd02ce0e
- **原文链接**: https://arxiv.org/abs/2608.02508
- **PDF**: https://arxiv.org/pdf/2608.02508v2
- **作者**: Yi Yang, Zhennan Chen, Yihong Zhuang, Tiehan Fan, Yinan Chen, Jian Li, Jian Yang, Ying Tai
- **日期**: 2026-08-03
- **更新**: 2026-08-04
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-memory, reinforcement-learning, self-evolving-agents, alfworld
- **质量评分**: 4/5
- **抓取时间**: 2026-08-05T12:25:56.344927+00:00

---

## 中文导读

RoMeRL 面向自进化 LLM Agent 记忆中的反馈覆盖不足和 memory-reward trap，用固定维度的按任务结果极性和记忆动态分解的 reduced-order utility state 表示不断增长的轨迹效用空间摘要称其在 ALFWorld 和 LifelongAgentBench 上提升性能，Cold-Q ratio 降低 80.0%，反馈密度提升约 6 倍，记忆规模减少 84.4%，LLM 调用减少 21.1%

## 为什么值得关注

RoMeRL reduces reward contamination in self-evolving agent memory.

这条记录适合进入 AAIF 的 agent / AI 系统设计观察池：论文把问题限定在可检查的任务规范、搜索空间和评估方法上，再讨论如何让 LLM、扩散模型、进化算法或强化学习式记忆机制服务于可复现的系统改进。下面内容只基于 arXiv 元数据、摘要和条目既有摘要整理，未补充摘要之外的实验细节。

## 关键信息

- 论文标题：RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States
- 作者：Yi Yang, Zhennan Chen, Yihong Zhuang, Tiehan Fan, Yinan Chen, Jian Li, Jian Yang, Ying Tai
- arXiv：https://arxiv.org/abs/2608.02508
- 发布时间：2026-08-03
- 更新时间：2026-08-04
- arXiv 分类：cs.LG, cs.CL
- 关联标签：agent-memory, reinforcement-learning, self-evolving-agents, alfworld

## English Abstract

Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory Reinforcement Learning (RoMeRL), which represents the growing trajectory-indexed utility space using a fixed-dimensional per-task memory state factorized by outcome polarity and memory dynamics. RoMeRL incorporates new experiences through a fixed set of semantic coordinates whose contents are updated or replaced over time, thereby concentrating feedback over a bounded utility support. Theoretically, we show that this reduced-order parameterization increases the average feedback received by each utility coordinate and characterize the steady-state occupancy of erroneous coordinates under a generic coordinate-transition model. Empirically, across ALFWorld and LifelongAgentBench, RoMeRL improves task performance, reduces the Cold-Q ratio by 80.0%, increases feedback density by approximately 6.0 times, reduces the maintained memory size by 84.4%, and cuts LLM calls by 21.1%. These results show that reduced-order utility states support efficient self-evolving agent memory while limiting persistent reward contamination. Code is available at: https://github.com/YOUNG-fnxm/RoMeRL

## English Summary

Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory Reinforcement Learning (RoMeRL), which represents the growing trajectory-indexed utility space using a fixed-dimensional per-task memory state factorized by outcome polarity and memory dynamics. RoMeRL incorporates new experiences through a fixed set of semantic coordinates whose contents are updated or replaced over time, thereby concentrating feedback over a bounded utility support....

## Obsidian Notes

- 内容由 `opencli arxiv paper 2608.02508 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断锚定在条目已有摘要、论文摘要、作者、日期与分类信息上。
