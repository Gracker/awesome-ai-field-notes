## English
Launching Claude Managed Agents

TL;DR – Claude Managed Agents is a pre-built, configurable agent harness that runs in managed infrastructure. You define an agent as a template – tools, skills, files / repos, etc. The agent harness and the infrastructure are provided for you. The system is designed to keep pace with Claude's rapidly growing intelligence and support long horizon tasks. Some useful links:

- Claude blog: Usage patterns and customer examples
- Engineering blog: The design of Claude Managed Agents
- Docs: Onboarding, quickstart, overview of the CLI and SKDs

Why Claude Managed Agents

The Claude messages API is a direct gateway to the model: it accepts messages and returns content blocks. Agents built on the messages API use a harness to route Claude's tool calls to handlers and manage context. This poses a few challenges:

- Harnesses need to keep up with Claude – I recently wrote a blog here focused on building agents using Claude API primitives to handle tool orchestration and context management. But agent harnesses encode assumptions about what Claude can't do. These assumptions grow stale as Claude gets more capable and can bottleneck Claude's performance. Harnesses need to be continually updated to keep pace with Claude.

- Claude is running for longer – Claude's task horizon is growing exponentially, already exceeding over 10 human-hours of work on the METR benchmark. This puts pressure on the infrastructure around an agent: it needs to be safe, resilient to infrastructure failures that happen over long horizon tasks, and support scaling (e.g., to many agent teams).

Addressing these challenges is important because we expect future Claude to run over days, weeks, or months on humanity's greatest challenges. The Claude Agent SDK was a first step, providing an excellent general purpose agent harness. Claude Managed Agents is the next step in this progression: a system with the harness and managed infrastructure designed to support safe, reliable execution over the time-horizon that we expect Claude to work.

How to get started

An easy way to onboard is to use our open source claude-api skill, which works out of the box in Claude Code. Get the latest version of Claude Code and run the following sub-command for Claude Managed Agents onboarding. I'm excited about skills as a way to onboard to new features, and have used this skill extensively:

Also see our docs for quickstart with the SDKs or CLI, and prototype agents in Claude Console.

Use cases

You can see our Claude blog for a number of interesting examples. Some of the common patterns I've noticed across these examples and my own work:

- Event-triggered: A service triggers the Managed Agent to do a task. For example, a system flags a bug and a managed agent writes the patch and opens the PR. No human in the loop between flag and action.

- Scheduled: Managed Agent is scheduled to do a task. For example, I and many others use this pattern for scheduled daily briefs (e.g., of X or Github activity, what a team of agents is working on). Here's an example daily brief of X activity that I use.

- Fire-and-forget: Humans trigger the Managed Agent to do a task. For example, assign tasks to the Managed Agent via Slack or Teams and get back deliverables (spreadsheets, slides, apps).

- Long-horizon tasks: Long-running tasks are an area where I think Managed Agents will be particularly useful. I've explored this by forking @karpathy's auto-research repo and exploring a few different ideas. For example, I recently took @_chenglou's excellent pretext library and had a Managed Agent explore ways to apply it to our engineering blog content.

Key concepts

When onboarding, there's three central concepts to understand:

- Agent — A versioned config that houses the agent's identity: model, system prompt, tools, skills, MCP servers, etc. You create it once and reference it by ID.

- Environment — A template describing how to provision the sandbox the agent's tools run in (e.g., runtime type, networking policy, and package config).

- Session — A stateful run using the pre-created agent config and environment. It provisions a fresh sandbox from the environment template, mounts any per-run resources (files, GitHub repos), stores auth in a secure vault (MCP credentials).

Think about an agent as a configuration, an environment as a template describing the sandbox you want the agent to access for code execution, and the session as any agent execution. One agent can have many sessions.

Usage

See docs here:

- SDKs – These are code-facing: import them in your app to drive sessions at runtime. Six languages have Managed Agents support: Python, TypeScript, Java, Go, Ruby, PHP.

- CLI – Terminal-facing: every API resource (agents, environments, sessions, vaults, skills, files) is exposed as a subcommand.

- Common patterns – Use the CLI for setup and SDK for runtime. Agents templates are persistent: you create one, store it (e.g., as a YAML with model, system prompt, tools, MCP servers, skills in git) and have the CLI apply it in your deploy pipeline.

How it works

I wrote an Anthropic engineering blog post with @mc_anthropic, @gcemaj, and @jkeatn on the process of building Claude Managed Agents: a lesson we share in the post is that building agents to scale with Claude's intelligence is an infrastructure challenge, not strictly a matter of harness design.

With this in mind, we didn't design a particular agent harness; we expect agent harnesses to constantly evolve. Instead we decouple what we thought of as the brain (Claude and its harness) from both the hands (sandboxes and tools that perform actions) and the session (the log of session events).

Each became an interface that made few assumptions about the others, and each could fail or be replaced independently. We share how this gives the system reliability, security, and flexibility to add future harnesses, sandboxes, or infrastructure to house sessions.

Conclusion

I'm excited about projects exploring different patterns of multi-agent orchestration or long-running tasks. One of the frustrations I've written about in the past is keeping agent harnesses up with model capabilities. Claude Managed Agents handles the agent harness and infrastructure for you, allowing for explorations on top of the agent as a new core primitive in the Claude API.

## 中文
发布 Claude 托管智能体

TL;DR —— Claude 托管智能体是一个预构建的可配置智能体运行底座，运行在托管基础设施上。你将智能体定义为模板——工具、技能、文件/仓库等。智能体运行底座和基础设施都为你提供。该系统设计为能够跟上 Claude 快速增长的智能并支持长时间任务。一些有用的链接：

- Claude 博客：使用模式和客户案例
- 工程博客：Claude 托管智能体的设计
- 文档：入门、快速入门、CLI 和 SDK 概览

为什么需要 Claude 托管智能体

Claude 消息 API 是模型的直接网关：它接受消息并返回内容块。基于消息 API 构建的智能体使用运行底座将 Claude 的工具调用路由到处理器并管理上下文。这带来了一些挑战：

- 运行底座需要跟上 Claude —— 我最近在这里写了一篇博客，专注于使用 Claude API 原语来构建智能体以处理工具编排和上下文管理。但智能体运行底座编码了关于 Claude 不能做什么的假设。这些假设随着 Claude 能力增强而变得过时，可能成为 Claude 性能的瓶颈。运行底座需要不断更新以跟上 Claude 的步伐。

- Claude 运行时间更长 —— Claude 的任务范围呈指数级增长，在 METR 基准测试中已经超过了超过 10 个人类工作小时。这给智能体周围的基础设施带来压力：它需要安全，能够承受长时间任务中发生的基础设施故障，并支持扩展（例如，扩展到许多智能体团队）。

解决这些挑战很重要，因为我们期望未来的 Claude 能够在人类最伟大的挑战上运行数天、数周或数月。Claude 智能体 SDK 是第一步，提供了优秀的通用智能体运行底座。Claude 托管智能体是这一进程的下一步：一个具有运行底座和托管基础设施的系统，旨在支持我们期望 Claude 工作的长时间范围内的安全可靠执行。

如何开始入门

一个简单的方法是使用我们的开源 claude-api 技能，它在 Claude Code 中开箱即用。获取最新版本的 Claude Code 并运行以下子命令来为 Claude 托管智能体入门。我对技能作为新功能入门的方式感到兴奋，并且大量使用了这个技能：

另请参阅我们的文档，了解 SDK 或 CLI 的快速入门，以及在 Claude Console 中原型化智能体。

使用场景

您可以在我们的 Claude 博客中看到许多有趣的例子。在这些例子和我自己的工作中，我注意到的一些常见模式：

- 事件触发：服务触发托管智能体执行任务。例如，系统标记一个错误，托管智能体编写补丁并打开 PR。在标记和操作之间没有人工参与。

- 定时：托管智能体被安排执行任务。例如，我和许多其他人使用这种模式进行定时每日简报（例如，X 或 GitHub 活动，智能体团队正在做什么）。这是我使用的 X 活动每日简报示例。

- 即发即忘：人工触发托管智能体执行任务。例如，通过 Slack 或 Teams 向托管智能体分配任务并获取可交付成果（电子表格、幻灯片、应用程序）。

- 长时间任务：长时间运行是我认为托管智能体特别有用的领域。我通过分叉 @karpathy 的自动研究仓库并探索一些不同的想法来探索这一点。例如，我最近采用了 @_chenglou 优秀的 pretext 库，并让托管智能体探索将其应用于我们工程博客内容的方法。

核心概念

入门时，需要理解三个核心概念：

- 智能体 —— 一个版本化的配置，包含智能体的身份：模型、系统提示、工具、技能、MCP 服务器等。你创建一次并通过 ID 引用。

- 环境 —— 描述如何配置智能体工具运行的沙盒的模板（例如，运行时类型、网络策略和包配置）。

- 会话 —— 使用预先创建的智能体配置和环境的运行状态执行。它从环境模板配置一个全新的沙盒，挂载任何运行时资源（文件、GitHub 仓库），将身份验证存储在安全保险库中（MCP 凭据）。

将智能体视为配置，将环境视为描述你希望智能体访问用于代码执行的沙盒的模板，将会话视为任何智能体执行。一个智能体可以有许多会话。

使用方式

请在此处查看文档：

- SDK —— 这些是面向代码的：在你的应用中导入它们以在运行时驱动会话。六种语言支持托管智能体：Python、TypeScript、Java、Go、Ruby、PHP。

- CLI —— 面向终端：每个 API 资源（智能体、环境、会话、保险库、技能、文件）都作为子命令暴露。

- 常见模式 —— 使用 CLI 进行设置，使用 SDK 进行运行时。智能体模板是持久的：你创建一个，存储它（例如，作为包含模型、系统提示、工具、MCP 服务器、技能的 YAML 文件）并在部署管道中使用 CLI 应用它。

工作原理

我与 @mc_anthropic、@gcemaj 和 @jkeatn 一起撰写了一篇 Anthropic 工程博客文章，介绍了构建 Claude 托管智能体的过程：我们在文章中分享的一个教训是，构建能够扩展 Claude 智能的智能体是一个基础设施挑战，而不仅仅是运行底座设计的问题。

考虑到这一点，我们没有设计特定的智能体运行底座；我们期望智能体运行底座不断演进。相反，我们将所谓的大脑（Claude 及其运行底座）与双手（执行动作的沙盒和工具）以及会话（会话事件的日志）解耦。

每个都成为对其他方面假设很少的接口，并且每个都可以独立失败或替换。我们分享了如何为系统提供可靠性、安全性和灵活性，以添加未来的运行底座、沙盒或基础设施来承载会话。

结论

我对探索多智能体编排或长时间任务的不同模式的项目感到兴奋。我过去写过的沮丧之一是让智能体运行底座跟上模型能力。Claude 托管智能体为你处理智能体运行底座和基础设施，允许你在智能体之上进行探索，将其作为 Claude API 中的新核心原语。