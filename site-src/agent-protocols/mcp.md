# Model Context Protocol

MCP — 4 条活跃资源

### [如何从零开始写一个 OpenClaw -- 关于我用 Rust 写一只🦀🦞(CrabClaw)的开发手记](https://x.com/jakevin7/status/2028499952973099363) 
by @jakevin7 (2026-03-03) | ⭐⭐⭐⭐⭐ 5/5 | 🌍

**OpenClaw 相关：如何从零开始写一个 OpenClaw -- 关于我用 Rust 写一只🦀🦞(Cr**

**By @jakevin7** (卡比卡比) · Mon Mar 02 15:57:31 +0000 2026
📊 ❤️ 74 🔁 4 🔖 92 👁️ 14,471 💬 1
📐 735 words
从 0 到 1，用 AI 辅助开发一个 OpenClaw 类似的 Agentic AI 工具。7 天，73 个 commit，13000+ 行 Rust。
这篇文章记录了整个过程中的思考、踩坑与感悟。
代码在 GitHub。如果你也想造一只属于自己的螃蟹钳子，欢迎 star/fork。我的 GitHub：jackwener，欢迎 follow。
起因
2026 年 2 月，OpenClaw 火了。朋友圈里人人都在聊这只龙虾——一个能在 Telegram 里跟你对话、帮你干活的 AI 智能体。在我看到 Bub 之后，我也起了一个想自己写一个的心
我先简单看了 Nanobot（OpenClaw 的最小复现）了解核心架构，
深入研究了 Bub——PsiACE 的 Agent 项目。Bub 的架构非常优雅：AgentLoop 抽象、Tape 记忆系统、Skills 引擎，每个模块都恰到好处。
 `openclaw` `agent` `agentic` `skill` `context-management` `github`

---
### [6551 开源 X + 全网新闻源 MCP + Skill](https://x.com/cryptoxiao/status/2026956308092453360) 
by @cryptoxiao (2026-02-28) | ⭐⭐⭐ 3/5 | 🇨🇳

**6551 开源 X/新闻/链上数据 MCP，几分钟给 Agent 接入全网信息源**

6551 团队开源了积累一年的数据基础架构：X 数据 + 全网 50+ 实时新闻 + 链上数据的 MCP 和 Skill。Agent 可直接连上 X 数据和全网新闻源，24h 监控分析并触发 Telegram 提醒。无需配置 API 密钥。几分钟部署。
 `mcp` `openclaw` `news-source` `x-api` `skill` `open-source`

---
### [或](https://x.com/Wuming_Mr_/status/2028419040847249428) 
by @WumingMr (2026-03-03) | ⭐⭐⭐ 3/5 | 🌍

**AI 实践：或**

**@Wuming_Mr_** (無名先生)
🕐 Mon Mar 02 10:36:00 +0000 2026
📊 ❤️ 324 🔁 95 🔖 461 👁️ 34,765 💬 17
《我在 ClawHub 折腾一周后，留下这 10 个真香技能》
先说结论：#ClawHub 真的能把 #OpenClaw 从“会聊天的工具”升级成“能干活的员工”。
但前提是——别乱装。
现在生态已经野蛮生长，上万个 Skills 里确实有宝藏，也有雷。我自己踩过两个坑（一个权限乱读文件，一个 prompt 写得离谱），所以这篇是纯个人实战后的筛选清单，不是搬运榜单。
时间：2026年3月
结论：新手按这个顺序装，基本不会翻车。
✅ 第一优先级：保命四件套（先装这 4 个）
1️⃣ Skill Vetter（安全审计）
这玩意必须第一个装。
安装新 skill 前自动扫描风险指令，相当于给 Agent 装个“防毒软件”。
ClawHub 现在下载量≠安全，别太天真。
2️⃣ Tavily / SerpAPI（联网搜索）
没联网的 Agent，本质是信息孤岛。
装完之后才真正“活过来”。
 `openclaw` `agent` `obsidian` `skill` `github`

---
### [2026-03-03-1210-evilcos-OpenClaw-Security-Practice-Guide-2028458311801274671](https://x.com/evilcos/status/2028458311801274671) 
by @evilcos (2026-03-03) | ⭐⭐⭐ 3/5 | 🇨🇳

**OpenClaw 相关：2026-03-03-1210-evilcos-OpenClaw-Securit**

**@evilcos** (Cos(余弦)😶‍🌫️)
🕐 Mon Mar 02 13:12:03 +0000 2026
📊 ❤️ 787 🔁 183 🔖 1,231 👁️ 161,327 💬 45
🦞OpenClaw 极简安全实践指南 (Security Practice Guide) 是面向 OpenClaw 的黑手册。
我尝试了其他一些方式来试图加固 OpenClaw，包括 Skill 方式，但是发现还不如给 OpenClaw 植入一个安全“思想钢印”来的有意思，这个“思想钢印”形成一个 md 文档，包含安全事前、事中、事后需要做的策略，但这里有个前提：
尽量不影响 OpenClaw 的日常使用，安全不要干扰用户体验，需要给这只🦞足够的自由。但是吧，江湖险恶，一只有 Root 权限且诞生才一个多月的🦞，安全不让人放心…
于是，这份面向 OpenClaw 的极简安全实践指南诞生了，目前是 v2.7 版本，此前我们内测了许多版本，也踩了不少坑。
 `openclaw` `skill` `github`

---