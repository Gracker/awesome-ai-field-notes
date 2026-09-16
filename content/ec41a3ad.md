---
id: ec41a3ad
title: Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security
arxiv: 2607.18063
authors: Devina Jain, David Hartmann, Chuan Li
primary_category: cs.CR
published: 2026-07-20
updated: 2026-09-11
url: https://arxiv.org/abs/2607.18063
pdf: https://arxiv.org/pdf/2607.18063v2
source: arxiv
tags: [arxiv ai-security benchmark llm-agent]
---

# 适应型对手：针对 LLM 智能体安全的多轮、多 LLM 基准

> Source: [arXiv:2607.18063](https://arxiv.org/abs/2607.18063) · Category: `cs.CR` · Authors: Devina Jain, David Hartmann, Chuan Li

## TL;DR

LLM 智能体需要读取外部内容，从而暴露于提示序注入与多轮操纵。本文提出一个针对跨会话、针对“每轮重启”防御侧 LLM 的 21 场景适应性攻击基准：一个自主 LLM 攻击者观察上一轮防御响应后调整策略，而每个防御响应都被当作独立会话评价。在一个 3×3 的攻防矩阵上调度出 945 场对决。仅第一轮评分时攻击成功率仅 0–1%；允许 15 轮互动后上升到 7.9–16.8%。将三个不同攻击 LLM 池化发现的独特成功输入是最强单个攻击者的 1.7–2.2 倍，但需三倍战斗预算。总体成功率会掩盖业务类别上相反的脆弱点，如会话密钥保护与权限判断。在六个场景上，加入一段“来源 / 溯源”描述可以把 ASR 从 110/270 降到 70/270，但作用在不同任务上明显不均。交互历史与防御者状态控制、冻结重放设计为评估“交互协议如何改变结果”提供了可控变量。还附带一个在固定 gpt-oss-20b 背骨上的 18,422 场 holdout 对决、以及对应的良性任务评测。本基准把攻防侧模型、框架、场景、会话状态、交互预算都拆视为可配置选项，供系统安全评估使用。

## 为什么重要

“多轮 + 适应型”是 LLM 智能体安全评测重点之一：单轮 ASR 仅 0–1%，多轮上升至 16.8%。越多攻击 LLM 池化越能发掘独特输入，说明智能体安全需要多攻击者 + 多轮 + 多场景的系统评测，而不是单点防御。

## 原文摘要（English）

LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. We present a 21-scenario benchmark for adaptive cross-session attacks against fresh-session LLM defenders: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. A controlled 3 x 3 attacker-defender matrix contains 945 battles. Restricting scoring to the first round yields 0-1% attack success rate (ASR); allowing 15 rounds yields 7.9-16.8%. Pooling three attacker LLMs uncovers 1.7-2.2 times as many unique successful inputs as the best single attacker, at three times the battle budget. Aggregate rates conceal opposing scenario-specific weaknesses in session-secret protection and authority handling, preserved in two higher-sample evaluations. On six scenarios, adding one provenance paragraph reduces ASR from 110/270 to 70/270, with selective effects across tasks. History and defender-state controls, together with frozen replay, frozen replay, characterize how the interaction protocol changes the result. A competition adds 18,422 held-out battles on a fixed gpt-oss-20b backbone and complementary benign-task evaluations. The benchmark exposes attacker and defender models, harnesses, scenarios, session state, and interaction budgets as configurable choices for systematic security evaluation.

## 基本信息

| 项 | 值 |
|------|------|
| 论文 ID | `2607.18063` |
| 主分类 | `cs.CR` |
| 发表 | 2026-07-20 |
| 更新 | 2026-09-11 |
| 作者 | Devina Jain, David Hartmann, Chuan Li |
| 备注 | Second Workshop on Agents in the Wild: Safety, Security, and Beyond |
| PDF | [2607.18063](https://arxiv.org/pdf/2607.18063v2) |
| abs | [https://arxiv.org/abs/2607.18063](https://arxiv.org/abs/2607.18063) |

## 参考

- arXiv abs: <https://arxiv.org/abs/2607.18063>
- arXiv PDF: <https://arxiv.org/pdf/2607.18063v2>
