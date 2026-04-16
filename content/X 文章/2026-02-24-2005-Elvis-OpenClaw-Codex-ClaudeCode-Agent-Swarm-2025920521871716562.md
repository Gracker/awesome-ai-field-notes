> **Note**: Original in English. 中文翻译在下方。

---

# OpenClaw + Codex/ClaudeCode Agent Swarm: The One-Person Dev Team [Full Setup]

> Author: Elvis Sun (@elvissun)
> Source: https://x.com/elvissun/status/2025920521871716562
> Date: 2026-02-24

I don't use Codex or Claude Code directly anymore.

I use OpenClaw as my orchestration layer. My orchestrator, Zoe, spawns the agents, writes their prompts, picks the right model for each task, monitors progress, and pings me on Telegram when PRs are ready to merge.

## Proof Points

- **94 commits in one day.** My most productive day - I had 3 client calls and didn't open my editor once. The average is around 50 commits a day.
- **7 PRs in 30 minutes.** Idea to production is blazing fast because coding and validations are mostly automated.
- **Commits → MRR:** I use this for a real B2B SaaS I'm building — bundling it with founder-led sales to deliver most feature requests same-day.

My git history looks like I just hired a dev team. In reality it's just me going from managing claude code, to managing an openclaw agent that manages a fleet of other claude code and codex agents.

**Success rate:** The system one-shots almost all small to medium tasks without any intervention.

**Cost:** ~$100/month for Claude and $90/month for Codex, but you can start with $20.

## Why This Works Better

Codex and Claude Code have very little context about your business. They see code. They don't see the full picture.

OpenClaw changes the equation. It acts as the orchestration layer between you and all agents — it holds all business context (customer data, meeting notes, past decisions, what worked, what failed) inside an Obsidian vault, and translates historical context into precise prompts for each coding agent.

## Why One AI Can't Do Both

Context windows are zero-sum. You have to choose what goes in. Fill it with code → no room for business context. Fill it with customer history → no room for the codebase. This is why the two-tier system works: each AI is loaded with exactly what it needs.

## The Full 8-step Workflow

### Step 1: Customer Request → Scoping with Zoe

After a call, I talk through the request with Zoe. Because all meeting notes sync to my Obsidian vault, zero explanation needed. Zoe then:
1. Tops up credits to unblock customer immediately
2. Pulls customer config from prod database (read-only)
3. Spawns a Codex agent with a detailed prompt containing all the context

### Step 2: Spawn the Agent

Each agent gets its own worktree (isolated branch) and tmux session. The task gets tracked in `.clawdbot/active-tasks.json`.

### Step 3: Monitoring in a Loop

A cron job runs every 10 minutes to babysit all agents. It doesn't poll the agents directly — it runs a deterministic script that:
- Checks if tmux sessions are alive
- Checks for open PRs on tracked branches
- Checks CI status via `gh cli`
- Auto-respawns failed agents (max 3 attempts)
- Only alerts if something needs human attention

### Step 4: Agent Creates PR

The agent commits, pushes, and opens a PR via `gh pr create --fill`.

**Definition of done:**
- PR created
- Branch synced to main (no merge conflicts)
- CI passing (lint, types, unit tests, E2E)
- Codex review passed
- Claude Code review passed
- Gemini review passed
- Screenshots included (if UI changes)

### Step 5: Automated Code Review

Every PR gets reviewed by three AI models:
- **Codex Reviewer** — Exceptional at edge cases. Catches logic errors, race conditions. Very low false positive rate.
- **Gemini Code Assist Reviewer** — Free. Catches security issues, scalability problems.
- **Claude Code Reviewer** — Mostly useless - tends to be overly cautious. Good for validating what other reviewers flag.

### Step 6: Automated Testing

CI pipeline runs: lint, TypeScript checks, unit tests, E2E tests, Playwright tests against a preview environment. If UI changes, screenshots are required in PR description.

### Step 7: Human Review

Telegram notification: "PR #341 ready for review." Review takes 5-10 minutes. Many PRs merged without reading the code — the screenshot shows everything needed.

### Step 8: Merge

PR merges. Daily cron job cleans up orphaned worktrees and task registry.

## The Ralph Loop V2

When an agent fails, Zoe doesn't just respawn with the same prompt. She looks at the failure with full business context:
- Agent ran out of context? "Focus only on these three files."
- Agent went the wrong direction? "Stop. The customer wanted X, not Y."
- Agent needs clarification? "Here's customer's email."

Zoe also finds work proactively:
- Morning: Scans Sentry → finds errors → spawns agents
- After meetings: Scans meeting notes → flags feature requests → spawns agents
- Evening: Scans git log → updates changelog

## Choosing the Right Agent

- **Codex** — Workhorse. Backend logic, complex bugs, multi-file refactors. 90% of tasks.
- **Claude Code** — Faster, better at frontend. Fewer permission issues, great for git operations.
- **Gemini** — Design sensibility. For beautiful UIs, generate HTML/CSS spec first, then hand to Claude Code.

## How to Set This Up

Copy this entire article into OpenClaw and tell it: "Implement this agent swarm setup for my codebase." It'll create everything in 10 minutes.

## The Bottleneck: RAM

Each agent needs its own worktree and `node_modules`. Five agents running simultaneously means five parallel TypeScript compilers. Mac Mini with 16GB tops out at 4-5 agents. Solution: Mac Studio M4 Max with 128GB RAM ($3,500).

## Up Next: The One-Person Million-Dollar Company

The leverage is massive for those who understand how to build recursively self-improving agents. An AI orchestrator as an extension of yourself, delegating work to specialized agents. Engineering, customer support, ops, marketing — each agent focused on what it's good at. You maintain laser focus and full control.

The next generation of entrepreneurs won't hire a team of 10. They'll build like this — staying small, moving fast, shipping daily.

What am I building? Agentic PR — a one-person company taking on enterprise PR incumbents. Agents that help startups get press coverage without a $10k/month retainer.


---

## 中文翻译

# OpenClaw + Codex/ClaudeCode 代理集群：一人开发团队（完整配置）

> 作者：Elvis Sun (@elvissun)
> 来源：https://x.com/elvissun/status/2025920521871716562
> 日期：2026-02-24

我不再直接使用 Codex 或 Claude Code 了。

我用 OpenClaw 作为编排层。我的编排者 Zoe 负责生成代理、编写提示词、为每个任务选择合适的模型、监控进度，并在 PR 可以合并时通过 Telegram 通知我。

## 成果数据

- **一天 94 次提交。** 我最高产的一天——开了 3 个客户会议，一次都没打开编辑器。平均每天约 50 次提交。
- **30 分钟 7 个 PR。** 从想法到上线极快，因为编码和验证大部分是自动化的。
- **提交 → MRR：** 我用这个系统构建真实的 B2B SaaS——结合创始人直销，大部分功能需求当天交付。

## 为什么比直接用更好

Codex 和 Claude Code 对你的业务几乎没有上下文。它们只看代码，看不到全貌。

OpenClaw 改变了这个等式。它作为你和所有代理之间的编排层——在 Obsidian 知识库中保存所有业务上下文（客户数据、会议记录、过往决策），并将历史上下文转化为每个编码代理的精确提示词。

## 为什么一个 AI 做不了两件事

上下文窗口是零和博弈。填满代码 → 没有业务上下文的空间。填满客户历史 → 没有代码库的空间。这就是两层系统有效的原因：每个 AI 只加载它需要的内容。

## 完整 8 步工作流

### 第 1 步：客户需求 → 与 Zoe 一起规划

会议后，Zoe 自动获取会议记录，无需我解释。Zoe 然后：1) 给客户充值 2) 从生产数据库拉取配置（只读）3) 生成一个 Codex 代理

### 第 2 步：生成代理

每个代理有自己的 worktree（隔离分支）和 tmux 会话。

### 第 3 步：循环监控

每 10 分钟运行的 cron 任务检查所有代理。不直接轮询代理——运行确定性脚本检查 tmux 会话状态、PR 状态、CI 状态，仅在有需要时告警。

### 第 4 步：代理创建 PR

代理提交、推送并通过 `gh pr create --fill` 创建 PR。

### 第 5 步：自动化代码审查

每个 PR 由三个 AI 模型审查：Codex（擅长边界情况）、Gemini Code Assist（安全/可扩展性）、Claude Code（验证其他审查者的发现）。

### 第 6 步：自动化测试

CI 管道运行 lint、类型检查、单元测试、E2E 测试、Playwright 测试。

### 第 7 步：人工审查

Telegram 通知："PR #341 准备好审查了。"审查需要 5-10 分钟。

### 第 8 步：合并

PR 合并。每日 cron 清理孤立 worktree。

## Ralph Loop V2

代理失败时，Zoe 不是用相同提示词重新生成。她带着完整的业务上下文分析失败原因，写出更好的提示词。

Zoe 还会主动找工作：早上扫描 Sentry 错误，会后扫描会议记录中的功能需求，晚上更新 changelog。

## 选择合适的代理

- **Codex** — 主力。后端逻辑、复杂 bug、多文件重构。90% 的任务。
- **Claude Code** — 更快，擅长前端。
- **Gemini** — 设计感。先生成 HTML/CSS 规格，再交给 Claude Code 实现。

## 瓶颈：内存

每个代理需要自己的 worktree 和 node_modules。5 个代理同时运行需要 5 个并行的 TypeScript 编译器。16GB Mac Mini 最多跑 4-5 个代理。解决方案：128GB Mac Studio M4 Max。

## 未来：一人百万美元公司

理解如何构建递归自我改进代理的人将获得巨大杠杆。AI 编排者作为你的延伸，将工作委托给专业代理。工程、客服、运营、营销——每个代理专注于自己擅长的领域。
