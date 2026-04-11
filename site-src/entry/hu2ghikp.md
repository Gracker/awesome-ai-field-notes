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

# Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库

## English
A comprehensive, open collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any agent platform.

**Context Engineering Fundamentals:**
- Context engineering is the discipline of managing the language model's context window
- Unlike prompt engineering, context engineering addresses holistic curation of all information that enters the model's limited attention budget
- Fundamental challenge: context windows are constrained by attention mechanics, not raw token capacity
- Effective context engineering means finding the smallest possible set of high-signal tokens

**Core Skill Categories:**
1. **Context Fundamentals** - Understanding what context is, why it matters, and anatomy of context in agent systems
2. **Context Degradation** - Recognizing patterns of context failure: lost-in-middle, poisoning, distraction, and clash
3. **Context Compression** - Designing compression strategies for long-running sessions
4. **Multi-Agent Patterns** - Mastering orchestrator, peer-to-peer, and hierarchical multi-agent architectures
5. **Memory Systems** - Designing short-term, long-term, and graph-based memory architectures
6. **Tool Design** - Building tools that agents can use effectively

**Key Features:**
- Each skill is structured for efficient context use
- Agents load only skill names and descriptions at startup
- Full content loads only when a skill is activated for relevant tasks
- Platform-agnostic principles work across Claude Code, Cursor, and any agent platform
- Skills are automatically discovered and activated based on task context

**Integration Examples:**
- Digital Brain Skill: Complete personal operating system with 6 modules and 4 automation scripts
- X-to-Book System: Multi-agent system that monitors X accounts and generates daily synthesized books
- LLM-as-Judge Skills: Production-ready LLM evaluation tools with TypeScript implementation

## 中文
面向上下文工程的开放技能库，专注于构建生产级 AI 代理系统的原则和最佳实践。这些技能教授艺术和科学，用于策划上下文以在任何代理平台上最大化代理的有效性。

**上下文工程基础：**
- 上下文工程是管理语言模型上下文窗口的学科
- 与提示工程不同，上下文工程处理进入模型有限注意力预算的所有信息的整体策划
- 根本挑战：上下文窗口受到注意力机制的限制，而非原始令牌容量
- 有效的上下文工程意味着找到最小的高信号令牌集合

**核心技能类别：**
1. **上下文基础** - 理解什么是上下文、为什么重要以及代理系统中上下文的构成
2. **上下文退化** - 识别上下文失败的模式：中间丢失、中毒、分心和冲突
3. **上下文压缩** - 为长时间运行的会话设计压缩策略
4. **多代理模式** - 掌握编排器、对等和分层多代理架构
5. **记忆系统** - 设计短期、长期和基于图的记忆架构
6. **工具设计** - 构建代理可以有效使用的工具

**主要特性：**
- 每个技能都结构化为高效使用上下文
- 代理在启动时只加载技能名称和描述
- 仅在为相关任务激活技能时才加载完整内容
- 平台无关的原则适用于 Claude Code、Cursor 和任何代理平台
- 技能根据任务上下文自动发现和激活

**集成示例：**
- 数字大脑技能：包含6个模块和4个自动化脚本的完整个人操作系统
- X转书系统：监控X账户并生成每日合成书籍的多代理系统
- LLM作为评判者技能：带有TypeScript实现的生产就绪LLM评估工具

**安装和使用：**
```bash
# 在 Claude Code 中添加插件市场
/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering

# 安装插件
/plugin install context-engineering@context-engineering-marketplace
```

该库已被学术界引用为静态技能架构的基础工作，是构建和优化代理系统的重要资源。
