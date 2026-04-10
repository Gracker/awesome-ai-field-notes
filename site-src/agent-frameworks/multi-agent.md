# 多Agent框架

Multi-Agent — 3 条活跃资源

### [OpenClaw + Codex/ClaudeCode Agent Swarm: The One-Person Dev Team](https://x.com/elvissun/status/2025920521871716562) 
by @Elvis (2026-02-24) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**一人开发团队的 Agent Swarm 实战：OpenClaw 编排 + 多模型协作**

以 OpenClaw 为编排层，Codex/Claude Code 为编码执行层的双层架构。编排助手 Zoe 负责分配任务、生成提示、跟踪进度、Telegram 通知。核心思想是上下文专业化：编码 Agent 拿代码上下文，编排层掌握业务上下文。94 次提交/日峰值，30 分钟 7 个 PR。流程包含隔离 worktree、tmux 控制、JSON 任务注册、周期巡检、三模型审查（Codex/Gemini/Claude）。
 `openclaw` `codex` `claude-code` `agent-swarm` `orchestration` `tmux`

---
### [Agent Frameworks Are Getting Squeezed](https://x.com/tonykipkemboi/status/2028564120338063859) 
by @tonykipkemboi (2026-03-03) | ⭐⭐⭐⭐⭐ 5/5 | 🌍

**Agent 相关：Agent Frameworks Are Getting Squeezed**

**By @tonykipkemboi (Tony Kipkemboi)**
🕐 Mon Mar 02 20:12:29 +0000 2026
📊 ❤️ 255 🔁 20 🔖 565 👁️ 91,128 💬 19
📐 1,407 words
When you look at what most agent frameworks actually do, it's workflow orchestration. You define tasks, chain them together, route data between steps, add conditional logic, call external APIs. The core mechanics look familiar because we've been doing this with automation platforms for over a decade.
当你看大多数 agent 框架真正做的事情时，本质上就是工作流编排：定义任务、串联步骤、在流程间路由数据、加条件分支、调用外部 API。
 `openclaw` `claude` `agent` `agentic` `automation` `rag`

---
### [2026-03-03-1210-yibie-Shipping-at-Inference-Speed-Notes-2028650995153314299](https://x.com/yibie/status/2028650995153314299) 
by @yibie (2026-03-03) | ⭐⭐⭐ 3/5 | 🌍

**AI 实践：2026-03-03-1210-yibie-Shipping-at-Infere**

**@yibie** (yibie)
🕐 Tue Mar 03 01:57:42 +0000 2026
📊 ❤️ 2 🔁 0 🔖 5 👁️ 153 💬 0
重读 OpenClaw 缔造者 Perter Steinberger 的这篇雄文《Shipping at Inference-Speed》，还有很深的启发，这篇文章是 Perter 说明自己 AI 辅助编程时，他自己工作流、方法、工具选择的转变，而这个转变让他打开与 AI 协作新的大门。
Perter 在 AI 辅助编程的范式转变，是来自他亲自开发的项目 VibeTunnel。年初他花了两个月时间，尝试用Rust、Go 甚至 Zig 重写核心模块，但旧模型一直失败，最终没完成。隔了一段时间，他重新打开这个项目，只给了 codex 两句提示让它把整个转发系统转成 Zig，模型自己跑了五个小时，经过多轮代码压缩，一次就交付了可用的转换。这种事在去年是不可想象的。
 `openclaw` `claude` `codex` `cursor` `agent` `multi-agent` `inference`

---