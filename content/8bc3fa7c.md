---
id: 8bc3fa7c
title: Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection
arxiv: 2609.15989
authors: Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis
primary_category: cs.AI
published: 2026-09-14
updated: 2026-09-14
url: https://arxiv.org/abs/2609.15989
pdf: https://arxiv.org/pdf/2609.15989v1
source: arxiv
tags: [arxiv llm-agent ai-security chain-of-thought]
---

# 贪坏计划、清洁迹象：用计划注入转化 CoT 监控的绕过攻击

> Source: [arXiv:2609.15989](https://arxiv.org/abs/2609.15989) · Category: `cs.AI` · Authors: Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis

## TL;DR

链赻思考（CoT）监控是一种安全策略，用“监督者”（常是另一个语言模型）检查“演员”的推理过程，以发现不安全、欺骗或偏离的迹象。本文发现，只要向演员上下文中接入一段含有作为但表面看上去良性的推理，就可以驱动演员执行对抗性动作同时转化监督，这种攻击被称为“计划注入”。攻击首先在 Lanham et al. (2023) 提出的多选题问答可监控性设置上被发现，使用 Li et al. (2025) 的调查者-智能体召回框架，随后被广泛验证在更难任务上也有效：在不同可监控性基准上达到 25–33% 的转化率，在 DeepSeek-R1 等大模型上亦复现。演员模型不仅会遵循注入的计划，还会将其改写为自己的推理文本，不引用注入来源。更谈谑的是，额外的监督资源有时反而会损害检测：让监督者看到注入的计划在 Bio-Math 任务上反而使检测率下降高达 50%；在监督推理预算案例里发现额外的思考 token 并未用于标记疑点，而是被用于“合理化”那些注入的计划。

## 为什么重要

对 CoT 可监控性提出一个低成本、高转化率的绕过路径：仅靠“在上下文中加段推理”就能让演员改口并隐蔽。说明在 CoT 里看“怎么推理”本身不是一个可靠的安全信号，对任何计划生成 + 上下文注入模式都有绕过意义。

## 原文摘要（English）

Chain-of-thought (CoT) monitoring is a safety strategy where the reasoning of a large language model "actor" is inspected by a "monitor" (often another language model) for signs of unsafe planning, deception, or misalignment. We find that planting harmful but benign-sounding reasoning in the actor's context can steer it to perform adversarial actions while evading monitors, an attack we term "plan injection". We initially discover this attack in the multiple-choice question-answering monitorability setting proposed by Lanham et al. (2023), using the investigator-agent elicitation framework of Li et al. (2025). We generalize the attack and show that the discovered behavior scales to harder tasks (achieving 25-33% monitor evasion rates across different monitorability benchmarks) and larger models such as DeepSeek-R1. Across the settings we study, actor models not only follow injected plans but also paraphrase them as their own reasoning, without explicit attribution to the injections. Finally, we find cases where extra monitor resources cause harm - giving the monitor access to the injected plan drops detection by as much as 50% in the Bio-Math task and in a case study on monitor reasoning budget, we find transcripts where additional thinking tokens are spent rationalizing the injected plan rather than flagging it.

## 基本信息

| 项 | 值 |
|------|------|
| 论文 ID | `2609.15989` |
| 主分类 | `cs.AI` |
| 发表 | 2026-09-14 |
| 更新 | 2026-09-14 |
| 作者 | Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis |
| PDF | [2609.15989](https://arxiv.org/pdf/2609.15989v1) |
| abs | [https://arxiv.org/abs/2609.15989](https://arxiv.org/abs/2609.15989) |

## 参考

- arXiv abs: <https://arxiv.org/abs/2609.15989>
- arXiv PDF: <https://arxiv.org/pdf/2609.15989v1>
