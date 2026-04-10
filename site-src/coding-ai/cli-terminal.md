# 命令行工具

CLI & Terminal — 5 条活跃资源

### [Lessons from Building Claude Code: Seeing like an Agent](https://x.com/trq212/status/2027463795355095314) 
by @Thariq (2026-02-28) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**Claude Code 核心开发者：设计 Agent 工具要匹配模型能力，三次迭代的经验**

Claude Code 核心开发者分享构建经验。设计 Agent 工具的关键框架：想象自己面对数学题——纸笔（基础但受限）→计算器（更好但需知识）→电脑（最快最强但需技能）。工具要匹配 Agent 能力。AskUserQuestion 工具的三次迭代：修改 ExitPlanTool（Claude 困惑）→修改输出格式（不可靠）→独立工具（成功，可引导结构化输出、确保多选项、支持 SDK/Skill 集成）。
 `claude-code` `agent-design` `tool-calling` `elicitation` `agent-harness`

---
### [Codex, in Plain English](https://x.com/gabrielchua/article/2026832978056458383) 
by @Gabriel Chua (2026-02-26) | ⭐⭐⭐⭐ 4/5 | 🌐

**非程序员的 Codex 入门：AI 编码 Agent 是通用数字工作工具**

面向非程序员的 Codex 解释：大多数计算机工作是手动操作软件（点击菜单、复制粘贴、拖文件），理论上都可自动化但需要写代码。Codex 是 OpenAI 的编码 Agent，用自然语言描述需求，它能拆步骤、选工具、写代码、运行、交付结果。不再是程序员的专利，而是通用数字工作工具。
 `codex` `openai` `coding-agent` `non-programmer` `automation`

---
### [Claude Code 核心开发者分享：构建 Claude Code 的经验教训——像 Agent 一样看世界](https://x.com/fkysly/status/2027610329530712204) 
by @马天翼 (2026-02-28) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Claude Code 核心开发经验的中文翻译版**

Thariq 原文的中文翻译。构建 agent 框架最难的部分是设计行动空间。工具设计要匹配 Agent 能力（纸笔→计算器→电脑的类比）。AskUserQuestion 工具三次迭代：修改 ExitPlanTool（Claude 困惑）→修改输出格式（不可靠）→独立工具（成功）。最终方案可引导结构化输出、确保多选项、支持 SDK 集成。
 `claude-code` `agent-design` `tool-calling` `chinese-translation`

---
### [oh my codex 使用教程](https://x.com/oragnes/status/2041876228949602347) 
by @oragnes (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**Codex 长任务增强工具，内置分阶段执行与并行模式**

介绍 oh-my-codex 工具，用于增强 OpenAI Codex 的长任务能力。安装命令 npm install -g @openai/codex oh-my-codex。核心命令：$deep-interview（澄清）、$ralplan（方案审批）、$ralph（推进执行）、$team 3:executor（并行执行）。亲测可有效处理长任务。
 `codex` `oh-my-codex` `coding-agent` `task-management`

---
### [高级自主软件化身（Elite Autonomous Developer Agent）](https://x.com/123olp/status/2025704271921213731) 
by @123olp (2026-02-24) | ⭐⭐⭐ 3/5 | 🇨🇳

**主任工程师级 Agent 角色设定模板，覆盖软件全生命周期**

主任工程师级自主 Agent 角色设定模板，覆盖软件全生命周期而非仅写代码。以系统级操作守则保障交付质量、逻辑严密性、执行稳定性。借鉴 Claude Code 实践，强化工程流程与规范沉淀。适合用于团队 Agent 提示词基座、工程治理标准化、复杂任务自动化执行框架。
 `autonomous-agent` `system-prompt` `engineering-practice` `claude-code`

---