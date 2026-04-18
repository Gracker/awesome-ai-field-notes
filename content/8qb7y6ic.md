# Superpowers — Agentic Skills 框架与软件开发方法论

## English原文

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them. It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it doesn't just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do.

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow.

## 核心理念

Superpowers 是一套完整的软件开发方法论，为编程 agent 设计，基于一组可组合的技能和初始指令。

当你启动编程 agent 时，它就开始工作了。当它发现你要构建什么时，不会直接跳进去写代码，而是退后一步，问你真正想要做什么。

从对话中梳理出规格说明后，它会以足够短的模块形式展示给你阅读和消化。设计获得批准后，agent 会制定一个足够清晰的实现计划——即使是一个品味不佳、缺乏判断力、没有项目背景而且厌恶测试的热情初级工程师也能执行。

## 核心工作流程

### 1. 头脑风暴（brainstorming）
在任何代码编写之前激活。通过提问细化粗糙的想法，探索替代方案，以分块形式展示设计供验证，并保存设计文档。

### 2. 使用 Git Worktree（using-git-worktrees）
设计批准后激活。在新分支上创建隔离的工作空间，运行项目设置，验证干净的测试基线。

### 3. 制定计划（writing-plans）
获得批准的设计后激活。将工作分解为可咬的小任务（每个 2-5 分钟）。每个任务都有确切的文件路径、完整代码和验证步骤。

### 4. 子 Agent 驱动开发（subagent-driven-development）
计划制定后激活。每个任务分配一个全新的子 agent，进行两阶段审查（规格合规性，然后代码质量），或在人工检查点处以批次方式执行。

### 5. 测试驱动开发（test-driven-development）
实现期间激活。强制执行 RED-GREEN-REFACTOR 循环：写失败的测试、看着它失败、写最少的代码、看着它通过、提交。在测试之前写的代码会被删除。

### 6. 请求代码审查（requesting-code-review）
任务之间激活。根据计划审查，发现问题按严重程度报告。关键问题阻塞进度。

### 7. 完成开发分支（finishing-a-development-branch）
任务完成时激活。验证测试，提供选项（合并/PR/保留/丢弃），清理 worktree。

## 技能清单

### 测试
- **test-driven-development**：RED-GREEN-REFACTOR 循环

### 调试
- **systematic-debugging**：4 阶段根因分析过程
- **verification-before-completion**：确保问题真正修复

### 协作
- **brainstorming**：苏格拉底式设计精炼
- **writing-plans**：详细实施计划
- **executing-plans**：带检查点的批次执行
- **dispatching-parallel-agents**：并发子 agent 工作流
- **requesting-code-review**：审查前检查清单
- **receiving-code-review**：响应反馈
- **using-git-worktrees**：并行开发分支
- **finishing-a-development-branch**：合并/PR 决策工作流
- **subagent-driven-development**：两阶段审查的快速迭代

### 元
- **writing-skills**：遵循最佳实践创建新技能
- **using-superpowers**：技能系统介绍

## 设计原则

- **测试驱动开发** — 先写测试，总是这样
- **系统性胜过临时性** — 流程优于猜测
- **降低复杂度** — 简洁性作为主要目标
- **证据优于断言** — 验证后再宣布成功

## 安装

Superpowers 可通过官方 Claude 插件市场安装：

```bash
# Claude Code
/plugin install superpowers@claude-plugins-official

# 或先注册市场
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

其他支持平台：Cursor Agent、Codex、OpenCode、GitHub Copilot、 Gemini。

## 相关链接

- GitHub：https://github.com/obra/superpowers
- Discord：https://discord.gg/35wsABTejz
- 发布公告：https://primeradiant.com/superpowers/

---

来源：[obra/superpowers](https://github.com/obra/superpowers)
