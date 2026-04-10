# Superpowers: 编码 Agent 的完整软件开发生命周期工作流

## English
Superpowers is a complete software development workflow for your coding agents, built on top of a set of composable "skills" and some initial instructions that make sure your agent uses them.

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it doesn't just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY.

Next up, once you say "go", it launches a subagent-driven-development process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.

If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider [sponsoring my opensource work](https://github.com/sponsors/obra).

Thanks!

- Jesse

Note: Installation differs by platform. Claude Code or Cursor have built-in plugin marketplaces. Codex and OpenCode require manual setup.

Superpowers is available via the [official Claude plugin marketplace](https://claude.com/plugins/superpowers)

Install the plugin from Claude marketplace:

/plugin install superpowers@claude-plugins-official

In Claude Code, register the marketplace first:

/plugin marketplace add obra/superpowers-marketplace

Then install the plugin from this marketplace:

/plugin install superpowers@superpowers-marketplace

In Cursor Agent chat, install from marketplace:

/add-plugin superpowers

or search for "superpowers" in the plugin marketplace.

Tell Codex:

Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md

Detailed docs: [docs/README.codex.md](/obra/superpowers/blob/main/docs/README.codex.md)

Tell OpenCode:

Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md

Detailed docs: [docs/README.opencode.md](/obra/superpowers/blob/main/docs/README.opencode.md)

copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace

gemini extensions install https://github.com/obra/superpowers

To update:

gemini extensions update superpowers

Start a new session in your chosen platform and ask for something that should trigger a skill (for example, "help me plan this feature" or "let's debug this issue"). The agent should automatically invoke the relevant superpowers skill.

- brainstorming - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.

- using-git-worktrees - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.

- writing-plans - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.

- subagent-driven-development or executing-plans - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.

- test-driven-development - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.

- requesting-code-review - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.

- finishing-a-development-branch - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

The agent checks for relevant skills before any task. Mandatory workflows, not suggestions.

Testing

- test-driven-development - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

Debugging

- systematic-debugging - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)

- verification-before-completion - Ensure it's actually fixed

Collaboration

- brainstorming - Socratic design refinement

- writing-plans - Detailed implementation plans

- executing-plans - Batch execution with checkpoints

- dispatching-parallel-agents - Concurrent subagent workflows

- requesting-code-review - Pre-review checklist

- receiving-code-review - Responding to feedback

- using-git-worktrees - Parallel development branches

- finishing-a-development-branch - Merge/PR decision workflow

- subagent-driven-development - Fast iteration with two-stage review (spec compliance, then code quality)

Meta

- writing-skills - Create new skills following best practices (includes testing methodology)

- using-superpowers - Introduction to the skills system

- Test-Driven Development - Write tests first, always

- Systematic over ad-hoc - Process over guessing

- Complexity reduction - Simplicity as primary goal

- Evidence over claims - Verify before declaring success

Read more: [Superpowers for Claude Code](https://blog.fsck.com/2025/10/09/superpowers/)

Skills live directly in this repository. To contribute:

- Fork the repository

- Create a branch for your skill

- Follow the writing-skills skill for creating and testing new skills

- Submit a PR

See skills/writing-skills/SKILL.md for the complete guide.

Skills update automatically when you update the plugin:

/plugin update superpowers

MIT License - see LICENSE file for details

Superpowers is built by [Jesse Vincent](https://blog.fsck.com) and the rest of the folks at [Prime Radiant](https://primeradiant.com).

- Discord: [Join us](https://discord.gg/35wsABTejz) for community support, questions, and sharing what you're building with Superpowers

- Issues: [https://github.com/obra/superpowers/issues](https://github.com/obra/superpowers/issues)

- Release announcements: [Sign up](https://primeradiant.com/superpowers/) to get notified about new versions

## 中文

Superpowers 是为你的编码代理构建的完整软件开发工作流，建立在一系列可组合的"技能"和一些初始指令之上，确保你的代理使用它们。

从你启动编码代理的那一刻就开始了。一旦它看到你正在构建某个东西，它不会直接跳入尝试编写代码。相反，它会退一步问你你真正想要做什么。

一旦从对话中梳理出规范，它会以足够短的片段展示给你，让你实际阅读和消化。

在你批准设计后，你的代理会制定一个实施计划，这个计划足够清晰，让一个热情但品味不佳、没有判断力、没有项目背景、并且回避测试的初级工程师都能遵循。它强调真正的红/绿 TDD（测试驱动开发）、YAGNI（你不会需要它）和 DRY（不要重复你自己）。

接下来，一旦你说"开始"，它会启动一个子代理驱动的开发过程，让代理完成每个工程任务，检查和审查他们的工作，并继续前进。Claude 能够在很长一段时间内（通常几个小时）自主工作而不偏离你制定的计划，这并不罕见。

这还有很多其他内容，但这是系统的核心。而且因为技能是自动触发的，你不需要做任何特别的事情。你的编码代理就拥有了 Superpowers。

如果 Superpowers 帮助你做了能赚钱的事情，而且你愿意考虑，我将非常感激你能考虑赞助我的开源工作。

谢谢！

- Jesse

注意：安装因平台而异。Claude Code 或 Cursor 有内置的插件市场。Codex 和 OpenCode 需要手动设置。

Superpowers 可以通过 [官方 Claude 插件市场](https://claude.com/plugins/superpowers) 获得

从 Claude 市场安装插件：

/plugin install superpowers@claude-plugins-official

在 Claude Code 中，先注册市场：

/plugin marketplace add obra/superpowers-marketplace

然后从该市场安装插件：

/plugin install superpowers@superpowers-marketplace

在 Cursor Agent 聊天中，从市场安装：

/add-plugin superpowers

或在插件市场中搜索"superpowers"。

告诉 Codex：

从 https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md 获取并遵循说明

详细文档：[docs/README.codex.md](/obra/superpowers/blob/main/docs/README.codex.md)

告诉 OpenCode：

从 https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md 获取并遵循说明

详细文档：[docs/README.opencode.md](/obra/superpowers/blob/main/docs/README.opencode.md)

copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace

gemini extensions install https://github.com/obra/superpowers

更新：

gemini extensions update superpowers

在你选择的平台中启动新会话，并请求应该触发技能的内容（例如，"帮助我规划这个功能"或"让我们调试这个问题"）。代理应该自动调用相关的 superpowers 技能。

- brainstorming - 在编写代码前激活。通过问题完善粗略想法，探索替代方案，以可验证的部分展示设计。保存设计文档。

- using-git-worktrees - 在设计批准后激活。在新分支上创建隔离工作空间，运行项目设置，验证干净的测试基线。

- writing-plans - 在批准的设计后激活。将工作分解为小任务（每个2-5分钟）。每个任务都有确切的文件路径、完整代码、验证步骤。

- subagent-driven-development 或 executing-plans - 在计划激活时激活。为每个任务派遣新的子代理进行两阶段审查（规范符合性，然后代码质量），或分批执行并在人工检查点继续。

- test-driven-development - 在实施过程中激活。强制执行 RED-GREEN-REFACTOR：编写失败的测试，观察失败，编写最少的代码，观察通过，提交。删除测试前编写的代码。

- requesting-code-review - 在任务之间激活。对照计划审查，按严重程度报告问题。关键问题会阻止进展。

- finishing-a-development-branch - 在任务完成时激活。验证测试，提供选项（合并/PR/保留/丢弃），清理工作树。

代理在任何任务前都会检查相关技能。强制性工作流，不是建议。

测试

- test-driven-development - RED-GREEN-REFACTOR 循环（包括测试反模式参考）

调试

- systematic-debugging - 4 阶段根本原因过程（包括根本原因追踪、纵深防御、基于条件的等待技术）

- verification-before-completion - 确保它确实被修复了

协作

- brainstorming - 苏格拉底式设计优化

- writing-plans - 详细的实施计划

- executing-plans - 分批执行与检查点

- dispatching-parallel-agents - 并发子代理工作流

- requesting-code-review - 预审查清单

- receiving-code-review - 响应反馈

- using-git-worktrees - 并行开发分支

- finishing-a-development-branch - 合并/PR 决策工作流

- subagent-driven-development - 快速迭代与两阶段审查（规范符合性，然后代码质量）

元技能

- writing-skills - 遵循最佳实践创建新技能（包括测试方法论）

- using-superpowers - 技能系统介绍

- Test-Driven Development - 总是先写测试

- Systematic over ad-hoc - 过程胜过猜测

- Complexity reduction - 简单性作为主要目标

- Evidence over claims - 验证后再声明成功

阅读更多：[Claude Code 的 Superpowers](https://blog.fsck.com/2025/10/09/superpowers/)

技能直接生活在这个仓库中。要贡献：

- Fork 仓库

- 为你的技能创建分支

- 遵循 writing-skills 技能来创建和测试新技能

- 提交 PR

有关完整指南，请参阅 skills/writing-skills/SKILL.md。

当你更新插件时，技能会自动更新：

/plugin update superpowers

MIT 许可证 - 详见 LICENSE 文件

Superpowers 由 [Jesse Vincent](https://blog.fsck.com) 和 [Prime Radiant](https://primeradiant.com) 的其他人构建。

- Discord：[加入我们](https://discord.gg/35wsABTejz) 获取社区支持、问题分享和用 Superpowers 构建的内容

- 问题：[https://github.com/obra/superpowers/issues](https://github.com/obra/superpowers/issues)

- 发布公告：[注册](https://primeradiant.com/superpowers/) 获取新版本通知


---

*来源：https://github.com/obra/superpowers*
*质量评分：4*
