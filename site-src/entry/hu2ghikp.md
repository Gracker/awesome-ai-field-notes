---
title: 'Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库

> 上下文工程的开放技能库，按需加载、平台无关

🔗 [原文链接](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | @泊舟 |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`context-engineering` `skills` `agent` `claude-code` `cursor` `lost-in-the-middle`

---

A comprehensive, open collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any agent platform.

[DeepWiki: Learn more here](https://deepwiki.com/muratcankoylan/Agent-Skills-for-Context-Engineering)

Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting effective instructions, context engineering addresses the holistic curation of all information that enters the model's limited attention budget: system prompts, tool definitions, retrieved documents, message history, and tool outputs.

The fundamental challenge is that context windows are constrained not by raw token capacity but by attention mechanics. As context length increases, models exhibit predictable degradation patterns: the "lost-in-the-middle" phenomenon, U-shaped attention curves, and attention scarcity. Effective context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

This repository is cited in academic research as foundational work on static skill architecture:

"While static skills are well-recognized [Anthropic, 2025b; Muratcan Koylan, 2025], MCE is among the first to dynamically evolve them, bridging manual skill engineering and autonomous self-improvement."

— [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557), Peking University State Key Laboratory of General Artificial Intelligence (2026)

These skills establish the foundational understanding required for all subsequent context engineering work.

### 基础技能 (Fundamental Skills)

| Skill | Description |
|-------|-------------|
| [context-fundamentals](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-fundamentals) | 理解上下文是什么、为什么重要，以及 Agent 系统中上下文的结构 |
| [context-degradation](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-degradation) | 识别上下文失效的模式：丢失在中间、毒化、干扰和冲突 |
| [context-compression](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-compression) | 为长时间运行的会话设计并评估压缩策略 |

### 架构技能 (Architecture Skills)

| Skill | Description |
|-------|-------------|
| [multi-agent-patterns](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/multi-agent-patterns) | 掌握编排器、点对点和分层多 Agent 架构 |
| [memory-systems](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/memory-systems) | 设计短期、长期和基于图的记忆架构 |
| [tool-design](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/tool-design) | 构建 Agent 可以有效使用的工具 |
| [filesystem-context](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/filesystem-context) | 使用文件系统进行动态上下文发现、工具输出卸载和计划持久化 |
| [hosted-agents](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/hosted-agents) | NEW 在沙盒 VM 中构建后台编码 Agent，支持预构建镜像、多人游戏支持和多客户端接口 |

### 优化技能 (Optimization Skills)

| Skill | Description |
|-------|-------------|
| [context-optimization](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-optimization) | 应用压缩、掩蔽和缓存策略 |
| [evaluation](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/evaluation) | 构建 Agent 系统的评估框架 |
| [advanced-evaluation](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/advanced-evaluation) | 掌握 LLM 作为法官的技术：直接评分、成对比较、评分标准生成和偏见缓解 |

### 元级技能 (Meta-level Skills)

| Skill | Description |
|-------|-------------|
| [project-development](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/project-development) | 从概念到部署设计并构建 LLM 项目，包括任务模型匹配分析、流水线架构和结构化输出设计 |

### 认知建模技能 (Cognitive Modeling Skills)

| Skill | Description |
|-------|-------------|
| [bdi-mental-states](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/bdi-mental-states) | NEW 使用正式的 BDI 本体模式将外部 RDF 上下文转换为 Agent 心智状态（信念、愿望、意图），用于推理和可解释性 |

## 技能结构 (Skill Structure)

每个技能都为高效的上下文使用而设计。在启动时，Agent 只加载技能名称和描述。仅在激活相关任务时才加载完整内容。

这些技能专注于可转移的原则，而非供应商特定的实现。这些模式适用于 Claude Code、Cursor 以及任何支持技能或允许自定义指令的 Agent 平台。

## 快速开始 (Quick Start)

### 步骤 1：添加市场 (Step 1: Add the Marketplace)

在 Claude Code 中运行以下命令将此存储库注册为插件源：



### 步骤 2：安装插件 (Step 2: Install the Plugin)

**选项 A - 浏览并安装：**
- 选择浏览和安装插件
- 选择 context-engineering-marketplace
- 选择 context-engineering
- 选择立即安装

**选项 B - 直接安装命令：**



这将安装所有 13 个技能的单个插件。技能会根据您的任务上下文自动激活。

## 示例与案例研究 (Examples & Case Studies)

这个存储库包含完整的系统设计，展示了多个技能在实践中如何协同工作。

### 数字大脑技能 (Digital Brain Skill)
一个创始人和创造者的个人操作系统，包含 6 个模块和 4 个自动化脚本。

### X 到书籍系统 (X-to-Book System)
监控 X 账户并生成日常合成书籍的多 Agent 系统。

### LLM 作为法官技能 (LLM-as-Judge Skills)
具有 TypeScript 实现和生产就绪的 LLM 评估工具，包含 19 个通过测试。

### 书本 SFT 流水线 (Book SFT Pipeline)
训练模型以任何作者的写作风格，包括使用 70% 人类分数在 Pangram 上的格特鲁德·斯坦案例研究，总成本 2 美元。

## 贡献指南 (Contributing)

此存储库遵循 Agent 开源开发模型。欢迎来自更广泛生态系统的贡献。当做出贡献时：

- 遵循 Agent 技能规范
- 确保新技能与现有技能一致
- 提供清晰的文档和示例
- 进行适当的测试和验证

这个项目旨在成为上下文工程实践的综合资源，帮助开发人员构建更有效、更可靠的 AI Agent 系统。
