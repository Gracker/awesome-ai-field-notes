# 技能与工作流

Skills & Workflows — 31 条活跃资源

### [从 Vibe Coding 到 Agentic Engineering：开发者角色正在重写](https://x.com/yanhua1010/status/2028737821855580662) 
by @yanhua1010 (2026-03-03) | ⭐⭐⭐⭐⭐ 5/5 | 🌍

**Agent 相关：从 Vibe Coding 到 Agentic Engineering：开发者角**

**By @yanhua1010** (Yanhua) · Tue Mar 03 07:42:43 +0000 2026
📊 ❤️ 54 🔁 8 🔖 55 👁️ 4,683 💬 1
📐 228 words
说实话，读完 Anthropic Claude Code 团队最近分享的这篇构建经验，我盯着屏幕想了很久。
不是因为技术多复杂。恰恰相反，整篇文章最让我震动的一句话极其朴素：
「你要学会像智能体一样看世界。」
这句话来自 Claude Code 的核心开发者。一个每天跟 AI 智能体打交道的人，他给出的最重要建议，不是什么架构方案或框架选型，而是一种认知方式的转变。
这让我想到一个更大的问题：2026 年了，我们跟 AI 协作的方式，是不是从根上就搞错了？
一、给 AI 一把锤子，它不一定能盖房子
Claude Code 团队讲了一个特别生动的类比。
想象你面前有一道很难的数学题。你希望有什么工具来帮忙？
如果你只会心算，给你纸和笔就够了。如果你会用计算器，给你一台计算器效率更高。如果你会编程，那直接给你一台电脑是最快的。
工具的上限，取决于使用者的能力。
 `claude` `agent` `karpathy` `vibe-coding` `agentic` `skill` `coding` `rag`

---
### [The Ultimate Beginner's Guide to Claude (March 2026)](https://x.com/aiedge_/status/2029233676111008061) 
by @AIEdge (2026-03-06) | ⭐⭐⭐⭐⭐ 5/5 | 🌍

**Claude 相关：The Ultimate Beginner's Guide to Claude **

> Source: [@aiedge_](https://x.com/aiedge_)
The only guide you need to master Claude from zero.
> 介绍
The only guide you need to master Claude from zero.
**这是从零开始掌握 Claude 的唯一指南。**
Last week, Anthropic shipped its best suite of Claude features yet. If you're still using ChatGPT, this is the nail in the coffin.
**上周，Anthropic 发布了迄今为止最好的 Claude 功能套件。如果你还在使用 ChatGPT，这就是压死骆驼的最后一根稻草。
 `claude` `prompt-engineering` `skill` `context-management` `Claude` `Anthropic` `AI` `Guide`

---
### [Claude 终极入门指南：100 小时实测，一篇讲透](https://x.com/yanhua1010/status/2029748928091148665) 
by @Yanhua (2026-03-06) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**Claude 相关：Claude 终极入门指南：100 小时实测，一篇讲透**

**By @yanhua1010** (Yanhua) · Fri Mar 06 02:40:30 +0000 2026
📊 ❤️ 145 🔁 43 🔖 259 👁️ 10,204 💬 1
📐 400 words
本文受 @aiedge 的 Claude 终极初学者指南 启发创作，结合个人一年多的实战经验。
2026 年 3 月，Anthropic 一口气释放了 Claude 有史以来最强的功能组合。Skills、Cowork、Opus 4.6。
如果你还在观望，或者还停留在"问它一个问题，得到一个回答"的阶段，这篇文章会帮你重新理解 Claude 到底是什么，以及怎么真正用好它。
我用 Claude 超过一年了。从最早的 API 到今天的桌面端、Code、Cowork，几乎每一个功能更新我都第一时间上手。保守估计，我累计投入了上百小时在 Claude 上测试、写作、编程、搭建工作流。
跳过那些产品介绍式的废话，这里只有实践验证过的干货。新手能快速上手，老用户也能查漏补缺。
 `claude` `memory` `skill` `context-management` `archive` `x-bookmarks`

---
### [Your LLM Doesn't Write Correct Code. It Writes Plausible Code.](https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code) 
by @Hōrōshi バガボンド (2026-03-07) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**用极端案例精准揭示了 LLM 代码生成的核心缺陷：表面正确 ≠ 实际正确。**

通过一个极端案例（LLM 重写的 Rust SQLite 实现比原版慢 20,171 倍）揭示 LLM 生成代码的核心问题：优化表面正确性而非实际正确性。详细拆解了两个关键 Bug（缺失 ipk 检查导致 O(n²) vs O(log n)、每次语句都 fsync），以及五个复合性能问题。引用 METR 随机对照试验（AI 用户慢 19%）、GitClear 分析（复制粘贴首次超过重构）等研究，论证 LLM 的 sycophancy 问题。结论：代码不是你的，直到你能自己找到其中的 bug。
 `LLM` `代码质量` `SQLite` `性能` `AI对齐` `sycophancy`

---
### [ClaudeCode 源码深度研究报告](https://x.com/tvytlx/status/2038939480892346699) 
by @Xiao Tan (2026-04-05) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**4756 个源码文件拆出的 Claude Code 架构全景：prompt 动态拼装、Agent 分工、工具治理 pipeline。**

从 Claude Code 泄露的 npm 包中提取 4756 个源码文件的深度拆解。核心发现：system prompt 是动态拼装的（静态宪法 + 动态当期政策），有 cache 边界设计（SYSTEM_PROMPT_DYNAMIC_BOUNDARY）优化 token 经济学；6 个内建 Agent（General、Explore 只读、Plan 只读、Verification adversarial、Guide、Statusline），实现者与验证者分离；工具调用经过 14 步 pipeline（输入校验→风险预判→权限决策→Hook→执行→post-processing）；三套扩展机制（Skill/Plugin/MCP）都让模型感知到自己的能力清单。五条设计原则：不信任模型自觉性、角色拆开、工具治理、上下文是预算、生态关键是模型感知。
 `Claude Code` `源码分析` `Agent架构` `系统设计` `上下文管理`

---
### [Waza：AI 时代工程师的 8 个核心技能工具集](https://x.com/HiTw93/status/2041053321851789629) 
by @HiTw93 (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**一套面向 AI 时代工程师的 8 技能工具集，覆盖思考到维护全流程**

作者开源了 Waza 技能集（日语"技"），包含 8 个核心 skill（/think、/design、/hunt、/check、/read、/write、/learn、/health），对应他认为 AI 时代工程师应具备的 8 个能力：会思考、会设计、会排查、会检查、会阅读、会写作、会学习、会维护。强调简单好用、清楚 Agent 在做什么，不多不少刚好够用。
 `openclaw` `skills` `agent` `engineering` `workflow` `context-engineering`

---
### [What spec-driven development gets wrong](https://x.com/augmentcode/status/2025993446633492725) 
by @Augment Code (2026-02-24) | ⭐⭐⭐⭐ 4/5 | 🌐

**静态规范是 Agent 的陷阱，应该是人机共维护的活文档**

规范驱动开发比临时提示词更好，但若规范是静态文档仍会失败。过期设计文档误导工程师，过期规范误导 Agent 自信地做错事。Augment Code 的解法是"共维护"：人和 Agent 都从同一份规范读取并回写更新。执行前由协调 Agent 拆任务，执行中 Agent 持续回写新发现。核心结论：既然 Agent 能写代码，也应该维护计划本身。
 `spec-driven` `agent` `software-development` `stale-specs` `co-maintenance`

---
### [Superpowers: 编码 Agent 的完整软件开发生命周期工作流](https://github.com/obra/superpowers) 
by @Obra (2026-02-27) | ⭐⭐⭐⭐ 4/5 | 🌐

**编码 Agent 的完整 SDLC 工作流，TDD+子Agent 自动执行**

完整的编码 Agent 软件开发工作流。先澄清目标、从对话抽取规格、设计拆成小段落确认。确认后生成遵循 TDD/YAGNI/DRY 的实现计划，再通过子 Agent 执行并进行分阶段审查。Claude 可自主工作数小时不偏离计划。支持 Claude Code、Cursor、Codex、OpenCode。技能自动触发，不需要特殊操作。
 `superpowers` `skills` `tdd` `subagent` `software-development` `claude-code`

---
### [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent") 
by @XPLUG (2026-03-02) | ⭐⭐⭐⭐ 4/5 | 🌍

**Agent 相关：X-PLUG/MobileAgent**

MobileAgent is Alibaba Tongyi Lab’s GUI-agent project family, covering mobile, desktop, and browser automation through the GUI-Owl model line and multi-agent workflows.
MobileAgent 是阿里通义实验室的 GUI Agent 项目家族，通过 GUI-Owl 模型系与多 Agent 工作流覆盖移动端、桌面端与浏览器自动化。
The repository serves as a unified hub of papers, code, demos, and benchmark updates (e.g., GUI-Owl 1.5, Mobile-Agent-v3/v3.5, UI-S1, and PC-Agent).
该仓库是论文、代码、演示与基准进展的统一入口（如 GUI-Owl 1.5、Mobile-Agent-v3/v3.5、UI-S1、PC-Agent）。
 `agent` `multi-agent` `benchmark` `automation` `github`

---
### [BestBlogs.dev 第 85 期：驾驭工程](https://x.com/hongming731/article/2029843882037715433) 
by @ginobefun (2026-03-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**目前对 AI 时代软件工程范式转移最全面的中文综述，信息密度极高。**

BestBlogs.dev 第 85 期以"驾驭工程"为核心关键词，提出开发者核心工作正从写代码转向构建 Agent 运行所依赖的驾驭工程体系。涵盖 GPT-5.4 发布（首次将推理、编程、计算机操作、深度搜索整合进单一模型）、Qwen3.5 小模型、FireRed-OCR、Martin Fowler 博客上关于 Harness Engineering 的系统性讨论（人在回路上 vs 人在回路中）、以及 Anthropic 设计负责人 Jenny Wen 对设计流程变革的判断。核心结论：执行力不再稀缺，稀缺的是知道该做什么以及判断什么是好的。
 `AI工程` `驾驭工程` `GPT-5.4` `Coding Agent` `Claude Code` `Agent架构`

---
### [My Chief of Staff, Claude Code](https://x.com/jimprosser/article/2029699731539255640) 
by @Jim Prosser (2026-03-08) | ⭐⭐⭐⭐ 4/5 | 🌐

**非程序员用 Claude Code 36 小时搭出完整幕僚长系统，证明系统思维 > 编程能力。**

一位非程序员的技术传播顾问用 Claude Code 在 36 小时内构建了完整的个人幕僚长系统：隔夜自动扫描日历和邮件、早晨 6:15 任务分类（绿/黄/红/灰四档）、6 个子 Agent 并行处理（邮件起草、Obsidian 客户笔记、会议安排、背景研究）、Stream Deck 一键时间块调度。核心设计原则：dispatch/prep/yours/skip 框架，系统从不发送邮件只起草，关键战略文档 100% 人工。月成本仅 $5-10 增量。文章价值在于展示了一个非程序员如何用系统思维（而非编程能力）设计 AI 自动化架构。
 `Claude Code` `自动化` `子Agent` `任务管理` ` productivity` `系统设计`

---
### [How Coding Agents Are Reshaping Engineering, Product and Design](https://x.com/hwchase17/status/2031051115169808685) 
by @Harrison Chase (2026-03-09) | ⭐⭐⭐⭐ 4/5 | 🌐

**LangChain 创始人对 Agent 时代 EPD 角色重塑的清晰判断：Builder vs Reviewer 二分法。**

LangChain 创始人 Harrison Chase 分析 Coding Agent 对工程、产品、设计三大职能的重塑：PRD 流程已死（不再需要 PRD→Mock→Code 的瀑布流），瓶颈从实现转向审查，通用型人才比以往更有价值。核心框架：Builder（用好 coding agent + 产品思维 + 基础设计直觉）vs Reviewer（深度系统思维 + 快速审查能力）。关键判断：coding agent 是必需品而非可选品；好人更好，坏人更坏（差的产品想法现在能快速产生原型但浪费更多审查资源）；系统思维是关键差异化能力。
 `Coding Agent` `EPD` `产品开发` `系统思维` `LangChain`

---
### [Claude Code .claude/ 文件夹完全指南](https://x.com/akshay_pachaar/status/2035341800739877091) 
by @Akshay Pachaar (2026-03-23) | ⭐⭐⭐⭐ 4/5 | 🌐

**Claude Code .claude/ 目录的完整参考，从 CLAUDE.md 到 Skills/Agents/Commands 全覆盖。**

Claude Code .claude/ 文件夹的完整解剖指南：项目级 vs 全局级两个目录、CLAUDE.md（200 行以内，只写项目特有内容）、rules/（路径范围规则模块化）、commands/（自定义斜杠命令，支持嵌入 shell 命令和参数）、skills/（自动触发工作流，与 commands 区别是自动识别触发）、agents/（独立上下文窗口的子 agent，可限制工具和指定模型）、settings.json（allow/deny 权限控制）。推荐：95% 的项目只需要 CLAUDE.md + settings.json + 1-2 个 commands。
 `Claude Code` `CLAUDE.md` `配置指南` `Skills` `Commands` `Agents`

---
### [三大 AI 编程框架对比调研：Superpowers vs GSD vs gstack](https://youtu.be/Y9hR2M4FE4I) 
 (2026-04-02) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**三大AI编程框架的哲学立场对比：Superpowers约束过程、GSD约束环境、gstack约束视角**

三大Claude Code生态AI编程框架的深度对比。Superpowers(124K⭐)通过流程纪律约束过程——强制TDD、苏格拉底式需求澄清、Subagent驱动开发。GSD(47K⭐)通过上下文隔离约束环境——每个子任务独立200K token上下文，解决Context Rot问题。gstack(57K⭐)通过多角色约束视角——23个专业角色交叉验证。核心差异在哲学立场：Superpowers=工程师思维、GSD=创业者思维、gstack=CEO思维。三者共同短板在Build阶段。
 `Superpowers` `GSD` `gstack` `AI编程` `框架对比` `Context-Rot` `TDD` `Claude-Code`

---
### [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) 
by @Anthropic Engineering (2026-03-24) | ⭐⭐⭐⭐ 4/5 | 🌐

**Anthropic分享Agent编程中的Harness设计：长周期应用的质量保障**

Anthropic工程团队分享长时间运行应用开发中的Harness设计经验。讨论如何在Agent驱动的开发流程中设计测试Harness，确保前端和全栈应用在长时间迭代中保持质量。涵盖自动化测试策略、CI/CD集成、以及Agent编程中的质量保障方法论。
 `anthropic` `harness-design` `agentic-coding` `frontend` `fullstack` `long-running`

---
### [OpenClaw + Claude Code 超强教程：一个人就能搭建完整的开发团队！](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247719868&idx=1&sn=c93e0542f8bebb653559315d02841b43) 
 (2026-02-26) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**最完整的 OpenClaw 多 Agent 编排实战案例，双层架构可直接复刻**

独立开发者用 OpenClaw + Codex/Claude Code 搭建 AI Agent 系统的完整案例。双层架构：OpenClaw 编排层持有业务上下文，Agent 执行层专注代码。8步从需求到 PR 合并，含自动监控、三 Agent Code Review、改进版 Ralph Loop（动态调整 prompt）。实测：单日 94 次提交，30 分钟 7 个 PR，月成本 $190。瓶颈是 RAM 不是 token。
 `openclaw` `claude-code` `codex` `agent` `编排` `双层架构` `tmux`

---
### [SmartPerfetto AI Agent 的 Harness Engineering 实战分享](https://mp.weixin.qq.com/s?__biz=MzIwNTQxMjM5MA==&mid=2247487518&idx=1&sn=ec49eac761ffd13acc02cd5e6cea7b94) 
 (2026-03-30) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Android Perfetto trace 分析 AI Agent 完整工程实践，MCP+Skill 三层验证范本**

SmartPerfetto 的 Harness Engineering 实战记录。在 Perfetto UI 加 AI 分析面板，Claude Agent + MCP 调用 trace_processor 执行 SQL 自动分析 Android trace。演进到 20 个 MCP 工具 + 158 个 YAML Skill + 三层验证。含滑动性能分析完整 session log。计划开源。
 `SmartPerfetto` `Perfetto` `Android` `性能优化` `MCP` `Agent` `Harness-Engineering`

---
### [你不知道的 Claude Code：架构、治理与工程实践 - Tw93](https://tw93.fun/2026-03-12/claude.html) 
 (2026-03-21) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 你不知道的 Claude Code：架构、治理与工程实践 - Tw93**

我把我最近半年每个月氪金40刀2个账号的claude code 使用过程中，积累的一些实际经验分享给大伙。这篇文章主要围绕上下文管理、Skills、Hooks、Subagents、Prompt Caching 以及 CLAUDE.md 的设计展开，重点讨论怎样让协作过程更稳定、更可控，偏工程师技术视角的最佳实践，欢迎大伙一起最佳交流。


---
### [吴恩达：从 Agent 到 Agentic Workflow ，AI 的未来何去何从？](https://mp.weixin.qq.com/s?__biz=MjM5NTg1ODg1OA==&mid=2459542397&idx=1&sn=e376ce196a41955734c48377cbc3cc18&chksm=b19f13b886e89aaec7ecb3f44f1de1300473b38346d6f8f54e8f87f4655cd87512eee06bae05&mpshare=1&scene=1&srcid=0623gOaBbHwBnL5vGTxNPHdK&sharer_shareinfo=11ba2c0c5006ec0d14971ced1c09c9c7&sharer_shareinfo_first=17a9447775b586d79d49eeec9285c317) 
 (2024-06-24) | ⭐⭐⭐⭐ 4/5 | 🌐

**Cubox 收藏 — 吴恩达：从 Agent 到 Agentic Workflow ，AI 的未来何去何从？**

[需翻译] *关注**AI 技能**，开启智能生活！* *?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fb96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UibM134tIsO1j5yqHyNhh9arj090oAL7zGhRJRq6cFqFOlDZMleLl4pw%2F640%3Fwx_fmt%3Dpng%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1)*


---
### [学习笔记：从 Agent 到 Skills — AI 智能体架构的范式转变](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247559249&idx=1&sn=7cda1453a5f7f51c39f43b76027696a1&chksm=e8178b0b81a60cb0161a097e5da8dbc326a34f5b041404fa1f9e023950c003fbe9a394c1d0e0&mpshare=1&scene=1&srcid=0331R15fBYxYJco3uMTIEUTw&sharer_shareinfo=327719e3faec950e49ae3605678de77e&sharer_shareinfo_first=327719e3faec950e49ae3605678de77e) 
 (2026-03-31) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 学习笔记：从 Agent 到 Skills — AI 智能体架构的范式转变**

?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FZ6bicxIx5naL7zVHZH429Po1HLpbichP9SLVicPtoxkI2WhMxUibFwG9U1dUOJu33R5KD9ib25hmibaaZLLldnh8dA4A%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D0) > 报告日期：2026-02-28 关键词： Agent Skills, MCP, OpenClaw,...


---
### [深入探讨GPTs和AI Assistant](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649781619&idx=1&sn=6051095ee8c98a93c255002f55dfb2c4&chksm=becce60889bb6f1ee66fdbcf1b5e2bc3e5a5ee7e2d95b59d0e6a913448b5ababd6a4b355d073&mpshare=1&scene=1&srcid=0102uzsvCe5iQSghneuVbOJ9&sharer_shareinfo=f939c224ab77495853e55fc84ad9d533&sharer_shareinfo_first=f939c224ab77495853e55fc84ad9d533) 
 (2024-01-02) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 深入探讨GPTs和AI Assistant**




---
### [深度解析：Claude Code Cowork](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247491350&idx=1&sn=dd3046300378c493810b246656ef33cb&chksm=e9fe92501c4cf67b96861f0e309dd8f987d0d7f2850ce46ff5121da97ab9559a64b0ef64bd08&mpshare=1&scene=1&srcid=0113qsQNgBeulIsuY7h2mPOu&sharer_shareinfo=38fca9920c4a546ed251b9ec529f1811&sharer_shareinfo_first=38fca9920c4a546ed251b9ec529f1811) 
 (2026-01-13) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 深度解析：Claude Code Cowork**

Anthropic 发布 "Cowork" 标志着人工智能产品战略的一个关键转折点（Cowork: Claude Code for the rest of your work^\[1\]^），它不仅是一个针对非编程人员的新工具，更宣告了 Anthropic 从单纯的模型提供商向综合性代理生态系统（Agentic Ecosystem）协调者的转型。我也算架构演变的见证者了，从早期写 MCP、到前段时间写 Skills（深度解析：Anthropic MCP 协议、从 Prompt Engineeri...


---
### [Claude Code 半小时改出 Obsidian Minimal 风博客](https://x.com/onlyice0328/status/2026261405788405767) 
by @zhl (2026-02-25) | ⭐⭐⭐ 3/5 | 🇨🇳

**Claude Code 半小时搞定博客样式改造的实战案例**

直接让 Claude Code 按 Obsidian Minimal Theme 风格改 CSS 与布局，约半小时完成。关键要点：先给 AI 明确目标风格、限定可改范围（CSS/布局/装饰）、人工验收可读性/层级/移动端。低成本提质的高 ROI 实战经验。
 `claude-code` `obsidian` `css` `blog` `vibe-coding`

---
### [CLAUDE CODE 橙皮书开源（75页）](https://x.com/AlchainHust/status/2039169585979539625) 
by @AlchainHust (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**75 页 Claude Code 实战手册开源，从安装到独立产品，面向 AI 编程入门者。**

AI 进化论-花生开源的 75 页《CLAUDE CODE 橙皮书》实战手册，面向想用 AI 编程但不知道从哪开始的人。10 章内容覆盖：核心工作流（Plan/Auto 模式、权限管理）、CLAUDE.md 写法、Skills/Hooks/MCP 扩展能力、多 Agent 并行协作、Computer Use 和 Voice Mode、一章完整的从零到上线产品实战。信息源来自 Claude 官方文档、Boris Cherny 分享、吴恩达 Claude Code 课程及作者用 CC 做十几个产品的经验。
 `Claude Code` `橙皮书` `实战手册` `开源` `AI编程`

---
### [graphify — Claude Code 的图谱 Skill](https://x.com/QingQ77/status/2041113437812511192) 
by @Geek Lite (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**Claude Code 知识图谱 Skill，71.5x token 压缩率，多模态输入自动生成可查询图谱。**

Claude Code 的图谱 Skill，支持将代码、论文、图片自动生成知识图谱。多模态提取：tree-sitter 解析代码、Claude vision 看图片、LLM 读 PDF。每条边标注 EXTRACTED/INFERRED/AMBIGUOUS 三种可信度，在 52 文件场景下实现 71.5x token 压缩率。输出支持交互式 HTML、Obsidian vault、可 Agent 读取的 wiki、持久化 JSON 跨 session 可查询。
 `Claude Code` `知识图谱` `Skill` `tree-sitter` `代码分析`

---
### [Claude Code 这些功能，用了就回不去了](https://x.com/sitinme/status/2040622970432045350) 
by @sitinme (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**Boris Cherny 亲授的 Claude Code 进阶技巧合集，验证 + 并行 + 自动化是三大关键。**

基于 Claude Code 创始人 Boris Cherny 分享的技巧整理的实战指南。核心要点：给 Claude 验证机会（装 Chrome 扩展/Playwright MCP 让它自己看效果，输出质量提升 2-3 倍）；同时开 3-5 个 git worktree 并行；/remote-control 手机遥控；/loop 定时循环和 /schedule 持久化任务；Hooks 是确定性的（绕不过去），CLAUDE.md 规则是建议性的（压力大可能跳过）；/btw 插队提问不进历史；/batch 大规模迁移神器（AI 军团式编程）；/model opus 切换模型省 token。
 `Claude Code` `Boris Cherny` `使用技巧` `worktree` `并行` `自动化`

---
### [Claude Code 推荐 Skills 汇总](#) 
 | ⭐⭐⭐ 3/5 | 🇨🇳

**Claude Code社区推荐Skills清单，按场景分类**

Claude Code推荐Skills汇总整理。Skills是Claude Code中的可复用能力（SOP），存放于.claude/skills/目录。收集了社区和官方推荐的高质量Skills清单，涵盖翻译、代码审查、文档生成等常用场景。
 `claude-code` `skills` `recommended` `tools`

---
### [Micro-optimizations in Kotlin — 1 · Romain Guy](https://www.romainguy.dev/posts/2024/micro-optimizations-in-kotlin-1/) 
 (2024-01-16) | ⭐⭐⭐ 3/5 | 🌐

**Romain Guy 级别的 Kotlin 底层优化，从源码到汇编的逐层剖析**

Android 框架团队传奇工程师 Romain Guy 分享 Kotlin 微优化实践。以 Jetpack Compose 中的 Int.sign 实现为案例，从 Kotlin 源码到 dex 字节码再到 AArch64 汇编逐层分析。发现 Kotlin 标准库的 when 表达式实现生成了冗余的比较指令。三种优化方案：1) 使用 java.lang.Integer.signum() 让 ART 提供优化 intrinsic；2) 用位运算实现无分支版本；3) 等待 Kotlin 2.0 修复。附带 kotlin-explorer 工具（可视化 dex 和 ARM64 汇编）。
 `Kotlin` `micro-optimization` `Android` `Jetpack-Compose` `Romain-Guy` `ARM64` `性能优化`

---
### [别再只写 CLAUDE.md 了：用 Rules 重构 Claude Code 的记忆系统](https://mp.weixin.qq.com/s?__biz=MzIxNTUxNDA5NQ==&mid=2247485928&idx=1&sn=042c59f7e6d9a5ab9cd251a70cae412f&chksm=96db6386a67d57503244639a65388c43c40c7e6670073c5ea1260431946a1fab4a45a1ba9150&mpshare=1&scene=1&srcid=1211ChEBUi9jyC7vCv2mgwRO&sharer_shareinfo=17ac304b7c4d4cde32f0c44fa3eeaeff&sharer_shareinfo_first=17ac304b7c4d4cde32f0c44fa3eeaeff) 
 (2025-12-11) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 别再只写 CLAUDE.md 了：用 Rules 重构 Claude Code 的记忆系统**

Claude Code 支持 Rules 了，Agent 的生态在大融合了，文本化的 Skills + Rules 要占领生态位了


---
### [浅谈Claude Skills，Github已经5.2k Star了](https://mp.weixin.qq.com/s?__biz=Mzg5MTU1NTE1OQ==&mid=2247496737&idx=1&sn=9629efe206466651a83311ad13742c58&chksm=ce92906609f4ad8d313e63d9f3a9cfa60bfa76a6c8ede08a0a0a7f10b51d867e62a5e4b3c69a&mpshare=1&scene=1&srcid=1020vw7J0m2UAIZgijWryasu&sharer_shareinfo=9e560ff6c7b0019f73b2284efd091348&sharer_shareinfo_first=9e560ff6c7b0019f73b2284efd091348) 
 (2025-10-20) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 浅谈Claude Skills，Github已经5.2k Star了**

https://www.zhihu.com/question/1962512846630941008/answer/1963073531265913943     （已授权）


---
### [超级实用！这6大"Skills" 可把 Anthropic Claude Code生产力拉升 50%](https://mp.weixin.qq.com/s?__biz=MzA3MzgzMjA3NA==&mid=2650775721&idx=1&sn=2da480a7aabf68c6ba7d3fe16eccd352&chksm=86751d03275201593e8ef1374bfacd72eb6b7806b790c35874efcd6cf8601e941fc146341c3d&mpshare=1&scene=1&srcid=1229akw1HSF9lJwM5m8Co2hf&sharer_shareinfo=4b78a819a5900c81619edfa0e4b90516&sharer_shareinfo_first=4b78a819a5900c81619edfa0e4b90516) 
 (2025-12-29) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 超级实用！这6大"Skills" 可把 Anthropic Claude Code生产力拉升 50%**

超级实用！这6大"Skills" 可把 Anthropic Claude Code生产力拉升 50%


---