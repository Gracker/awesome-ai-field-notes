---
entry_id: 24bbaf0f
title: "When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents"
source_type: paper
platform: arxiv
url: https://arxiv.org/abs/2608.27146
pdf: https://arxiv.org/pdf/2608.27146
authors: "Xiaokun Guo, Zhen Xu, Dongdong Huo, Yanqiu Zhang, Wei Wang, Qinfu Yang, Dongjin Yu, Yu Wang"
published: 2026-08-27
updated: 2026-08-27
categories: "cs.AI, cs.SE"
added: 2026-08-31
quality_score: 4
tags: [agent-security, authorization, tool-use, provenance, defenses]
---

# When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

> 摘要中文导览（来自条目评分时的双语摘要，基于论文摘要原文提炼）：

- 工具增强 LLM agent 必须依赖不可信的运行时 Observation 完成开放任务；当工具输出不再只是数据、而开始规定具体动作时，它就变成能驱动超出用户意图的现实副作用的“命令”。论文主张风险源于把动作诱导（action induction）与执行授权（execution authorization）混为一谈，提出 SARA：在 Observation 侧用上下文隔离的 Action Probe 暴露动作诱导语义并跨步骤持久记录动作来源作为审查信号；在执行侧，实际工具调用只依据用户目标和来自已授权成功执行的审计证据进行授权，同时要求目标、执行链与参数级支持。No-History-Promotion 机制防止历史复现把动作来源“洗白”成执行权限。在 AgentDojo 与 AgentDyn 上，SARA 在四个主要评测设置中把 ASR 限制在 0.63% 以内并保持有竞争力的任务效用，且在更多 agent 骨干上持续降低 ASR。

## 论文信息

- **arXiv ID**: 2608.27146
- **作者**: Xiaokun Guo, Zhen Xu, Dongdong Huo, Yanqiu Zhang, Wei Wang, Qinfu Yang, Dongjin Yu, Yu Wang
- **发表**: 2026-08-27（更新：2026-08-27）
- **分类**: cs.AI, cs.SE
- **原文链接**: https://arxiv.org/abs/2608.27146
- **PDF**: https://arxiv.org/pdf/2608.27146
- **标签**: `agent-security` `authorization` `tool-use` `provenance` `defenses`

## Abstract（原文）

Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become ``commands'' that can drive real-world side effects beyond user intent. We argue that this risk arises from conflating action induction with execution authorization. To address this distinction, we propose SARA, which treats action induction and execution authorization as distinct runtime roles and separates action provenance from execution authority. On the Observation side, a context-isolated Action Probe exposes action-inducing semantics and persistently records action-origin provenance across steps as a review signal; on the execution side, actual tool calls are authorized only against the user objective and audited evidence from authorized successful executions, while satisfying goal, execution-chain, and argument-level support. To preserve this separation across multi-step execution, SARA applies No-History-Promotion to prevent historical recurrence from laundering action origins into execution authority. Across AgentDojo and AgentDyn, SARA limits ASR to no more than \(0.63\%\) across four primary evaluation settings while maintaining competitive task utility, and consistently reduces ASR across additional Agent backbones.

## 核心要点（英文摘要的中文提炼）

- 论文题为 When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents，发表于 arXiv（cs.AI, cs.SE，2026-08-27 提交/更新）。
- 上述中文导览对应摘要中声明的贡献、实验设置与结论，未引入摘要之外的事实。

## Obsidian 证据摘录

入选自 Obsidian《论文流水线 · 2026-08-31》下一步 backlog：工具输出授权分离，ASR 不超过 0.63%。
