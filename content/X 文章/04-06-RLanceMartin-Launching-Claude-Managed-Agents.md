> **Note**: Original in English. 中文翻译在下方。

---

# Launching Claude Managed Agents

> Author: Lance Martin (@RLanceMartin) | Anthropic
> Source: https://x.com/RLanceMartin/status/2041927992986009773
> Date: 2026-04-08

## TL;DR

Claude Managed Agents is a pre-built, configurable agent harness that runs in managed infrastructure. You define an agent as a template – tools, skills, files / repos, etc. The agent harness and the infrastructure are provided for you. The system is designed to keep pace with Claude's rapidly growing intelligence and support long horizon tasks.

Some useful links:

- Claude blog: Usage patterns and customer examples
- Engineering blog: The design of Claude Managed Agents
- Docs: Onboarding, quickstart, overview of the CLI and SDKs

## Why Claude Managed Agents

The Claude messages API is a direct gateway to the model: it accepts messages and returns content blocks. Agents built on the messages API use a harness to route Claude's tool calls to handlers and manage context. This poses a few challenges:

- **Harnesses need to keep up with Claude** – Agent harnesses encode assumptions about what Claude can't do. These assumptions grow stale as Claude gets more capable and can bottleneck Claude's performance. Harnesses need to be continually updated to keep pace with Claude.

- **Claude is running for longer** – Claude's task horizon is growing exponentially, already exceeding over 10 human-hours of work on the METR benchmark. This puts pressure on the infrastructure around an agent: it needs to be safe, resilient to infrastructure failures that happen over long horizon tasks, and support scaling (e.g., to many agent teams).

Addressing these challenges is important because we expect future Claude to run over days, weeks, or months on humanity's greatest challenges. The Claude Agent SDK was a first step, providing an excellent general purpose agent harness. Claude Managed Agents is the next step in this progression: a system with the harness and managed infrastructure designed to support safe, reliable execution over the time-horizon that we expect Claude to work.

## How to get started

An easy way to onboard is to use our open source claude-api skill, which works out of the box in Claude Code. Get the latest version of Claude Code and run the following sub-command for Claude Managed Agents onboarding.

Also see our docs for quickstart with the SDKs or CLI, and prototype agents in Claude Console.

## Use cases

Some of the common patterns:

- **Event-triggered**: A service triggers the Managed Agent to do a task. For example, a system flags a bug and a managed agent writes the patch and opens the PR. No human in the loop between flag and action.

- **Scheduled**: Managed Agent is scheduled to do a task. For example, scheduled daily briefs (e.g., of X or Github activity, what a team of agents is working on).

- **Fire-and-forget**: Humans trigger the Managed Agent to do a task. For example, assign tasks to the Managed Agent via Slack or Teams and get back deliverables (spreadsheets, slides, apps).

- **Long-horizon tasks**: An area where Managed Agents will be particularly useful. For example, forking an auto-research repo and exploring different ideas.

## Key concepts

When onboarding, there's three central concepts to understand:

- **Agent** — A versioned config that houses the agent's identity: model, system prompt, tools, skills, MCP servers, etc. You create it once and reference it by ID.

- **Environment** — A template describing how to provision the sandbox the agent's tools run in (e.g., runtime type, networking policy, and package config).

- **Session** — A stateful run using the pre-created agent config and environment. It provisions a fresh sandbox from the environment template, mounts any per-run resources (files, GitHub repos), stores auth in a secure vault (MCP credentials).

Think about an agent as a configuration, an environment as a template describing the sandbox you want the agent to access for code execution, and the session as any agent execution. One agent can have many sessions.

## Usage

- **SDKs** – These are code-facing: import them in your app to drive sessions at runtime. Six languages have Managed Agents support: Python, TypeScript, Java, Go, Ruby, PHP.

- **CLI** – Terminal-facing: every API resource (agents, environments, sessions, vaults, skills, files) is exposed as a subcommand.

- **Common patterns** – Use the CLI for setup and SDK for runtime. Agents templates are persistent: you create one, store it (e.g., as a YAML with model, system prompt, tools, MCP servers, skills in git) and have the CLI apply it in your deploy pipeline.

## How it works

Building agents to scale with Claude's intelligence is an infrastructure challenge, not strictly a matter of harness design.

The system decouples the "brain" (Claude and its harness) from both the "hands" (sandboxes and tools that perform actions) and the "session" (the log of session events).

Each became an interface that made few assumptions about the others, and each could fail or be replaced independently. This gives the system reliability, security, and flexibility to add future harnesses, sandboxes, or infrastructure to house sessions.

## Conclusion

Claude Managed Agents handles the agent harness and infrastructure for you, allowing for explorations on top of the agent as a new core primitive in the Claude API.


---

## 中文翻译

# 推出 Claude 托管代理（Managed Agents）

> 作者：Lance Martin (@RLanceMartin) | Anthropic
> 来源：https://x.com/RLanceMartin/status/2041927992986009773
> 日期：2026-04-08

## 概要

Claude 托管代理是一个预构建的、可配置的代理框架，运行在托管基础设施上。你将代理定义为一个模板——工具、技能、文件/仓库等。代理框架和基础设施都由系统提供。该系统旨在跟上 Claude 快速增长的智能水平，并支持长周期任务。

## 为什么需要 Claude 托管代理

Claude 消息 API 是直接访问模型的入口：它接收消息并返回内容块。基于消息 API 构建的代理使用框架来路由 Claude 的工具调用并管理上下文。这带来了几个挑战：

- **框架需要跟上 Claude 的步伐** —— 代理框架编码了对 Claude 不能做什么的假设。随着 Claude 变得更强大，这些假设会过时，并可能成为 Claude 性能的瓶颈。框架需要不断更新才能跟上 Claude。

- **Claude 运行时间更长** —— Claude 的任务周期呈指数级增长，在 METR 基准上已超过 10 个小时的人类工作量。这对代理周围的基础设施施加了压力：它需要安全、能抵御长时间任务中的基础设施故障，并支持扩展（例如扩展到多个代理团队）。

解决这些挑战很重要，因为我们期望未来的 Claude 能在人类最大挑战上运行数天、数周甚至数月。Claude Agent SDK 是第一步，提供了一个出色的通用代理框架。Claude 托管代理是这一进程的下一步：一个带有框架和托管基础设施的系统，旨在支持在我们期望 Claude 工作的时间跨度内安全、可靠地执行。

## 如何开始

最简单的入门方式是使用我们的开源 claude-api skill，它在 Claude Code 中开箱即用。

## 使用场景

常见的模式包括：

- **事件触发**：服务触发托管代理执行任务。例如，系统标记了一个 bug，托管代理编写补丁并创建 PR。标记和操作之间无需人类介入。

- **定时执行**：托管代理被安排执行任务。例如定时每日简报。

- **即发即忘**：人类触发托管代理执行任务。例如通过 Slack 或 Teams 分配任务并获取交付物。

- **长周期任务**：托管代理将特别有用的领域。

## 核心概念

- **代理（Agent）** —— 包含代理身份的版本化配置：模型、系统提示、工具、技能、MCP 服务器等。创建一次，通过 ID 引用。

- **环境（Environment）** —— 描述如何配置代理工具运行的沙箱模板（如运行时类型、网络策略和包配置）。

- **会话（Session）** —— 使用预创建的代理配置和环境的有状态运行。从环境模板配置新的沙箱，挂载每次运行所需的资源（文件、GitHub 仓库），将认证存储在安全保管库中。

## 使用方式

- **SDK** —— 面向代码：在你的应用中导入以在运行时驱动会话。支持六种语言：Python、TypeScript、Java、Go、Ruby、PHP。

- **CLI** —— 面向终端：每个 API 资源都作为子命令暴露。

- **常见模式** —— 使用 CLI 进行设置，使用 SDK 进行运行时控制。

## 工作原理

构建能跟上 Claude 智能的代理是一个基础设施挑战，而不仅仅是框架设计问题。

系统将"大脑"（Claude 及其框架）与"手"（执行操作的沙箱和工具）和"会话"（会话事件的日志）解耦。

每个部分都成为对其他部分做出最少假设的接口，每个部分都可以独立失败或替换。这为系统提供了可靠性、安全性，以及添加未来框架、沙箱或会话基础设施的灵活性。

## 结论

Claude 托管代理为你处理代理框架和基础设施，使代理成为 Claude API 中的一个新的核心原语，你可以在此基础上进行各种探索。
