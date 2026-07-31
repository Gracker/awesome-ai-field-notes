---
title: "Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents"
source: arxiv
source_url: https://arxiv.org/abs/2607.27083
arxiv_id: 2607.27083
authors: Yicheng Feng, Yan Zhang, Yan Cheng, Wei Qi
published: 2026-07-29
categories: cs.LG, cs.AI
score: 5
fetched: 2026-07-31
---

# Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents

> **Authors:** Yicheng Feng, Yan Zhang, Yan Cheng, Wei Qi
> **Published:** 2026-07-29
> **Categories:** cs.LG, cs.AI
> **arXiv:** [2607.27083](https://arxiv.org/abs/2607.27083)

## Abstract

As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools leaves the task under-informed, while too many adds cost, context load, and privacy exposure. Routers and retrievers can rank candidate tools by relevance, but a ranking alone does not determine how many are worth selecting. Existing approaches leave acquisition under heterogeneous costs unaddressed. We formulate this decision as cost-aware marginal decision-focused stopping (CAM-DF) over ranked tool prefixes, with CAM-DF-lite as a compact interpretable variant. We train directly on the offline gap between stopping now and the best continuation: its sign labels the decision, its magnitude weights each error by the payoff at stake. We prove this objective is Bayes-aligned with the stopping target and that score-only rules are suboptimal under heterogeneous costs. We evaluate on 1,343 tasks across five tool-use domains. On τ-bench Retail, CAM-DF attains the highest payoff among deployable methods. In live execution, CAM-DF exposes the agent to 37% fewer tools than full access while maintaining comparable task success.

## 中文概述

这篇论文将 LLM 代理的工具获取决策形式化为“成本感知的边际决策聚焦停止（CAM-DF）”。核心洞察：工具排名只能告诉你哪个更相关，但无法告诉你“应该选多少个”。CAM-DF 在工具前缀上训练停止决策，在实际执行中减少 37% 的工具暴露同时保持相当的任务成功率。这是一个轻量级前置插件，无需微调底层 LLM 。

## 关键发现

- 工具排名≠获取决策：排名只告诉相关性，不告诉“选多少”
- CAM-DF 直接训练“现在停止 vs 最优继续”的离线差距
- 实际执行中减少 37% 工具暴露，任务成功率不降
- 轻量级前置插件，无需微调底层 LLM

## 信息来源

- 论文链接: [https://arxiv.org/abs/2607.27083](https://arxiv.org/abs/2607.27083)
- PDF: [https://arxiv.org/pdf/2607.27083v1](https://arxiv.org/pdf/2607.27083v1)
- 主要类别: cs.LG, cs.AI
