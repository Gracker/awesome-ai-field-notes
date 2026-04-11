## English

Superpowers is a complete software development workflow for your coding agents, built on top of a set of composable "skills" and some initial instructions that make sure your agent uses them.

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it doesn't just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest.

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY.

Next up, once you say "go", it launches a subagent-driven-development process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.

## 中文

Superpowers 是为您的编码代理提供的完整软件开发工作流，构建在一组可组合的 "技能" 和一些确保您的代理使用它们的初始指令之上。

它从您启动编码代理的那一刻就开始。一旦它看到您正在构建某些东西，它不会直接尝试编写代码。相反，它会后退一步，询问您真正想要做什么。

一旦它从对话中提炼出规范，它会以足够短小的片段展示给您，让您能够真正阅读和理解。

在您批准设计后，您的代理会制定一个实施计划，该计划足够清晰，让一个充满热情但品味欠佳、缺乏判断力、没有项目背景且厌恶测试的初级工程师也能遵循。它强调真正的红绿 TDD、YAGNI（你不会需要它）和 DRY。

接下来，一旦您说 "开始"，它会启动一个由子代理驱动的开发流程，让代理处理每个工程任务，检查和审查他们的工作，并继续前进。Claude 能够在一段时间内自主工作几个小时而不偏离您制定的计划，这并不罕见。

还有更多功能，但这是系统的核心。由于技能会自动触发，您不需要做任何特别的事情。您的编码代理只是拥有 Superpowers。

## 技能系统

Superpowers 包含一系列自动触发的技能，确保代理遵循最佳实践：

### 核心技能
- **brainstorming** - 在编写代码前激活。通过问题完善粗略想法，探索替代方案，以部分形式呈现设计以供验证。保存设计文档。
- **using-git-worktrees** - 设计批准后激活。在新分支上创建隔离工作区，运行项目设置，验证干净的测试基线。
- **writing-plans** - 批准设计时激活。将工作分解为可管理的小任务（每个 2-5 分钟）。每个任务都有确切的文件路径、完整代码和验证步骤。
- **subagent-driven-development** - 计划激活时触发。为每个任务派生新的子代理，进行两阶段审查（规范合规性，然后代码质量），或批量执行带人工检查点。
- **test-driven-development** - 实施过程中激活。强制执行 RED-GREEN-REFACTOR：编写失败测试，观察失败，编写最少代码，观察通过，提交。删除测试前编写的代码。
- **requesting-code-review** - 任务间激活。对照计划审查，按严重性报告问题。关键问题阻止进展。
- **finishing-a-development-branch** - 任务完成时激活。验证测试，提供选项（合并/PR/保留/丢弃），清理工作区。

## 开发方法论

### 测试驱动开发
- **test-driven-development** - RED-GREEN-REFACTOR 循环（包括测试反模式参考）

### 调试
- **systematic-debugging** - 4 阶段根本原因过程（包括根本原因追踪、纵深防御、基于条件的等待技术）
- **verification-before-completion** - 确保真正修复

### 协作
- **brainstorming** - 苏格拉底式设计完善
- **writing-plans** - 详细的实施计划
- **executing-plans** - 批量执行带检查点
- **dispatching-parallel-agents** - 并发子代理工作流
- **requesting-code-review** - 预审查清单
- **receiving-code-review** - 响应反馈

## 核心原则
- **Test-Driven Development** - 先写测试，总是如此
- **Systematic over ad-hoc** - 流程胜过猜测
- **Complexity reduction** - 简洁是首要目标
- **Evidence over claims** - 在宣布成功之前验证

## 安装与使用

Superpowers 支持多个平台：Claude Code、Cursor、Codex、OpenCode 等。安装后，在新会话中触发技能时会自动调用相关技能。
