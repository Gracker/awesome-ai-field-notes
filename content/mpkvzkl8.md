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

With this in mind, we didn't design a particular agent harness; we expect agent harnesses to constantly evolve. Instead we decoupled what we thought of as the "brain" (Claude and its harness) from both the "hands" (sandboxes and tools that perform actions) and the "session" (the log of session events).

Each became an interface that made few assumptions about the others, and each could fail or be replaced independently. We share how this gives the system reliability, security, and flexibility to add future harnesses, sandboxes, or infrastructure to house sessions.

Conclusion

I'm excited about projects exploring different patterns of multi-agent orchestration or long-running tasks. One of the frustrations I've written about in the past is keeping agent harnesses up with model capabilities. Claude Managed Agents handles the agent harness and infrastructure for you, allowing for explorations on top of the agent as a new core primitive in the Claude API.

## 中文

发布 Claude Managed Agents

长话短说——Claude Managed Agents 是一个预构建的、可配置的代理运行平台，运行在托管基础设施上。您将代理定义为模板——工具、技能、文件/仓库等。代理运行平台和基础设施都为您提供。该系统旨在跟上 Claude 快速增长的智能，并支持长时间任务。一些有用的链接：

- Claude 博客：使用模式和客户案例
- 工程博客：Claude Managed Agents 的设计
- 文档：入门、快速开始、CLI 和 SDK 概览

为什么需要 Claude Managed Agents

Claude messages API 是模型的直接网关：它接受消息并返回内容块。基于 messages API 构建的代理使用运行平台来路由 Claude 的工具调用到处理器并管理上下文。这带来了一些挑战：

- 运行平台需要跟上 Claude 的步伐——我最近写了一篇博客，重点介绍了使用 Claude API 原语构建代理来处理工具编排和上下文管理。但代理运行平台编码了关于 Claude 不能做什么的假设。随着 Claude 能力的增强，这些假设会变得过时，并可能成为 Claude 性能的瓶颈。运行平台需要不断更新以跟上 Claude 的步伐。

- Claude 运行时间更长——Claude 的任务范围呈指数级增长，在 METR 基准测试中已超过 10 个人类工作小时。这给代理周围的基础设施带来压力：它需要安全，能够承受长时间任务中发生的基础设施故障，并支持扩展（例如，到许多代理团队）。

解决这些挑战很重要，因为我们期望未来的 Claude 在人类最大的挑战上运行数天、数周甚至数月。Claude Agent SDK 是第一步，提供了一个优秀的通用代理运行平台。Claude Managed Agents 是这个进程中的下一步：一个具有运行平台和托管基础设施的系统，旨在支持我们期望 Claude 工作的长时间范围内的安全、可靠执行。

如何开始入门

一个简单的方法是使用我们的开源 claude-api 技能，它在 Claude Code 中开箱即用。获取 Claude Code 的最新版本，并运行以下子命令进行 Claude Managed Agents 入门。我对技能作为一种入门新功能的方式感到兴奋，并且广泛使用了这个技能：

另请参阅我们的文档，了解使用 SDK 或 CLI 的快速入门，以及在 Claude Console 中原型化代理。

使用案例

您可以在我们的 Claude 博客中看到许多有趣的案例。我在这些案例和我自己的工作中注意到的一些常见模式：

- 事件触发：服务触发 Managed Agent 执行任务。例如，系统标记一个错误，Managed Agent 编写补丁并打开 PR。在标记和操作之间没有人参与。

- 计划任务：计划 Managed Agent 执行任务。例如，我和许多人使用这个模式进行计划中的每日简报（例如，X 或 Github 活动，团队代理正在做什么）。这是我使用的 X 活动每日简报示例。

- 即发即忘：人类触发 Managed Agent 执行任务。例如，通过 Slack 或 Teams 向 Managed Agent 分配任务，并获取交付物（电子表格、演示文稿、应用程序）。

- 长时间任务：长时间运行是我认为 Managed Agent 特别有用的领域。我通过分叉 @karpathy 的 auto-repo 探索了这一点，并探索了几个不同的想法。例如，我最近采用了 @_chenglou 的优秀 pretext 库，并让 Managed Agent 探索将其应用于我们工程博客内容的方法。

核心概念

入门时，有三个核心概念需要理解：

- Agent —— 一个版本化的配置，包含代理的身份：模型、系统提示、工具、技能、MCP 服务器等。您创建一次并按 ID 引用。

- Environment —— 描述如何配置代理工具运行的沙箱的模板（例如，运行时类型、网络策略和包配置）。

- Session —— 使用预先创建的代理配置和环境进行的状态化运行。它从环境模板配置一个新的沙箱，挂载任何运行时资源（文件、GitHub 仓库），将身份验证存储在安全保险库中（MCP 凭据）。

可以把代理视为配置，环境视为您希望代理访问用于代码执行的沙箱的模板，会话视为任何代理执行。一个代理可以有多个会话。

使用方式

在此处查看文档：

- SDK —— 这些是面向代码的：在您的应用程序中导入它们以在运行时驱动会话。六种语言支持 Managed Agents：Python、TypeScript、Java、Go、Ruby、PHP。

- CLI —— 面向终端：每个 API 资源（代理、环境、会话、保险库、技能、文件）都作为子命令暴露。

- 常见模式 —— 使用 CLI 进行设置，使用 SDK 进行运行时。代理模板是持久的：您创建一个，存储它（例如，作为包含模型、系统提示、工具、MCP 服务器、技能的 YAML 并放在 git 中），并让 CLI 在您的部署管道中应用它。

工作原理

我和 @mc_anthropic、@gcemaj、@jkeatn 一起在 Anthropic 工程博客上写了一篇关于构建 Claude Managed Agents 过程的文章：我们在文章中分享的一个经验是，构建能够跟上 Claude 智能的代理是一个基础设施挑战，而不仅仅是运行平台设计的问题。

考虑到这一点，我们没有设计特定的代理运行平台；我们期望代理运行平台不断演变。相反，我们将我们所谓的"大脑"（Claude 及其运行平台）与"手"（执行动作的沙箱和工具）和"会话"（会话事件的日志）解耦。

每个都成为一个对其他人做很少假设的接口，每个都可以独立失败或被替换。我们分享了这如何为系统提供可靠性、安全性，以及添加未来运行平台、沙箱或来容纳会话的基础设施的灵活性。

结论

我对探索多代理编排或长时间任务的不同模式的项目感到兴奋。我过去写过的一个挫折是保持代理运行平台跟上模型的能力。Claude Managed Agents 为您处理代理运行平台和基础设施，允许您在 Claude API 中作为新的核心原语探索代理。