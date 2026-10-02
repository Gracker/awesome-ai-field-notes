# How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?

- **ID**: cffce8d9
- **原文链接**: https://arxiv.org/abs/2609.40303
- **PDF**: https://arxiv.org/pdf/2609.40303v1
- **作者：** Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé
- **发布时间**: 2026-09-30
- **更新**: 2026-09-30
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-harness, mle, ablation, coding-agent
- **质量评分**: 5/5
- **抓取时间**: 2026-10-02T04:30:58Z

---

## 中文导读

在相同时间预算与同一 frontier LLM backbone 下，对比开源 SOTA 精心搭建的 MLE agent harness（多 agent 编排专职检索 subagent 等）与只给 read/write/bash 原语的极简单会话 coding agent 基线：前者没有优势，性能主要由 backbone 决定大规模系统性消融显示，在 coding agent 场景里这些机制层是冗余的围绕强模型手工堆 harness 的边际收益在当前 MLE 基准上很差与 Pi 1.0 的极简 harness 路线以及 2609.40330 的实例自适应 harness 优化形成有趣对照：harness 的价值取决于模型强度与任务分布，复杂度本身不等于收益

## 为什么值得关注

同等时间预算同 backbone 下，精密 MLE harness 打不过单会话极简 coding agent，收益主要来自模型本身

The abstract states that under an equal time budget and the same frontier LLM backbone, open-source SOTA harnesses provided no advantage over a single session of a minimal-harness coding agent baseline, and large-scale systematic ablations show the machinery layers become redundant in the coding-agent setting.

## 关键信息

- 论文标题：How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?
- 作者：Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé
- arXiv: https://arxiv.org/abs/2609.40303
- 发布时间：2026-09-30
- arXiv 分类：cs.AI
- 关联标签：agent-harness, mle, ablation, coding-agent

## 英文摘要

Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. Often motivated by progress stagnation over long-horizon cycles and limited Large Language Model (LLM) primitives, modern MLE agents are deployed on top of increasingly elaborate machinery: multi-agent orchestrators, dedicated retrieval subagents, and more. While such harnesses expand, the use of more primitive but improved coding agents - where LLMs have direct access to the execution environment through read, write, and bash primitives - has received little attention in the field. In this paper we find that, under an equal time budget and the same frontier LLM backbone, open-source state-of-the-art harnesses provide no advantages over a single session of a minimal-harness coding agent baseline, pointing to the backbone as the primary driver for performance. Via a series of large-scale systematic ablation studies, we argue that the machinery layers become redundant in the coding agent setting. We conclude that the effort spent elaborating hand-crafted harnesses around strong models yields poor returns for current MLE benchmarks.

## English Summary

Under an equal time budget and the same frontier LLM backbone, open-source state-of-the-art MLE harnesses (multi-agent orchestrators, dedicated retrieval subagents) provide no advantage over a single session of a minimal-harness coding agent with direct read/write/bash primitives; the backbone is the primary performance driver. Large-scale systematic ablations show the machinery layers become redundant in the coding-agent setting, so hand-crafted harness elaboration around strong models yields poor returns on current MLE benchmarks.

## Obsidian Notes

- 本页为内容补齐（content backfill）：条目早已入库，本次补写内容页。
- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锺定在条目已有摘要与本次拉取的论文摘要上，未添加摘要之外的实验细节。
