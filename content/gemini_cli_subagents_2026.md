---
title: "Subagents have arrived in Gemini CLI"
date: 2026-04-15
source: google
category: agents
tags: [Gemini-CLI, subagents, context-window, parallel-execution, MCP]
quality_score: 4
status: fetched
---

## Gemini CLI 迎来 Subagents：子 Agent 重塑复杂任务处理范式

**发布日期：2026年4月15日 | 来源：Google Developers Blog**

### 什么是 Subagents？

Subagents（子代理）是专业化专家 Agent，与您的主 Gemini CLI 会话协同工作。当您向 Gemini CLI 分配一个广泛或复杂的任务时，它扮演战略编排者角色，将具体的子任务委托给最合适的子 Agent。

子 Agent 在隔离环境中运行，拥有独立的工具集、MCP 服务器、系统指令和上下文窗口。整个执行过程（可能涉及数十次工具调用、文件搜索或测试运行）被压缩为单一响应返回给主 Agent。这防止了主上下文窗口被填满，保持后续交互的快速和成本效益。

**子 Agent 的核心优势：**

- 让主 Agent 专注于整体目标、决策和最终响应
- 通过并行运行专业化子 Agent 加速工作：适用于研究、代码探索、分析、测试等
- 避免主会话的上下文腐烂和上下文污染，子 Agent 返回的是摘要或格式化响应

### 构建自定义专家子 Agent

您可以创建自己的专业化团队成员（子 Agent）来自动化特定工作流程、强制执行编码标准，或根据项目需求扮演特定角色。

自定义子 Agent 使用带有 YAML frontmatter 的 Markdown 文件（.md）定义。您可以在全局级别（`~/.gemini/agents`）定义供个人工作流程使用，也可以在项目级别（`.gemini/agents`）提交到代码库与团队共享。

只需将文件放置于 `.gemini/agents/frontend-specialist.md`，Gemini CLI 即可立即获得这个新的专家 Agent。

### 并行执行

比一个专家更好的是什么？一个团队同时工作。 Gemini CLI 支持并行子 Agent，允许您同时分叉多个子 Agent 或同一子 Agent 的多个实例。

> **注意：** 对需要大量代码编辑的任务请谨慎使用并行子 Agent。多个 Agent 同时编辑代码可能导致冲突和相互覆盖。并行子 Agent 也会因跨 Agent 并行发送请求而更快触及使用限制。

### 内置子 Agent

Gemini CLI 附带多个开箱即用的内置子 Agent：

- **generalist（通用型）**：通用型 Agent，有权访问所有工具，非常适合批量重构或高容量输出等轮次密集型任务。
- **cli_help（CLI 帮助）**：Gemini CLI 本身的专家，通过直接访问 Gemini CLI 文档回答功能问题。
- **codebase_investigator（代码库调查员）**：专门用于探索代码库、架构映射、Bug 根因分析和理解系统级依赖的 Agent。

### 如何调用子 Agent

您可以通过在提示中使用 `@agent` 语法来显式委托任务给子 Agent：

- "@frontend-specialist 能审查我们的应用并标记潜在改进吗？"
- "@generalist 更新整个项目的许可证头文件。"
- "@codebase_investigator 绘制认证流程图。"

随时在 Gemini CLI 中运行 `/agents` 可以查看所有已配置的子 Agent。

---
**参考链接：**
- [Subagents 文档](https://geminicli.com/docs/core/subagents/)
- [GitHub 仓库](https://github.com/google-gemini/gemini-cli)

---

## Subagents have arrived in Gemini CLI

**Published: April 15, 2026 | Source: Google Developers Blog**

### What are subagents?

Subagents are specialized, expert agents that operate alongside your primary Gemini CLI session. When you give Gemini CLI a broad or complex task, it acts as a strategic orchestrator, delegating specific sub-tasks to the most relevant subagent.

Subagents act in isolation with their own set of tools, MCP servers, system instructions, and context window. Their entire execution is consolidated into a single response back to the main agent. This prevents your main context window from filling up and keeps your subsequent interactions fast and cost-effective.

**Key benefits of subagents:**

- Keep the primary agent focused on the overall goal, decision making, and final response.
- Speed up work by running specialized subagents in parallel for research, code exploration, analysis, tests, etc.
- Avoid context rot and context pollution in the primary agent's session as subagents return summaries or formatted responses.

### Build your own expert with custom subagents

You can create your own specialized team members (subagents) to automate specific workflows, enforce coding standards, or act with specific personas tailored to your project.

Custom subagents are defined using simple Markdown files (.md) with YAML frontmatter. You can define them globally in `~/.gemini/agents` for your personal workflows or commit them to your repository at the project level in `.gemini/agents`.

By placing this file in `.gemini/agents/frontend-specialist.md`, Gemini CLI instantly gains a new expert it can call upon.

### Parallel execution

What's better than one expert? A whole team of them working simultaneously. Gemini CLI supports parallel subagents, allowing you to spin off multiple subagents or many instances of the same subagent, at the same time.

> **Note:** Exercise caution with parallel subagents for tasks that require heavy code edits. Multiple agents editing code at the same time can lead to conflicts.

### Built-in subagents

Gemini CLI ships with several built-in subagents ready for you to use:

- **generalist**: A general-purpose agent with access to all tools.
- **cli_help**: An expert on Gemini CLI itself, ready to answer questions about features.
- **codebase_investigator**: A specialized agent for exploring codebases, architectural mapping, and bug root-cause analysis.

### How to call subagents

You can explicitly delegate tasks to a subagent by referencing them in your prompt using the `@agent` syntax. To view all configured subagents at any given time, just run `/agents` within Gemini CLI.
