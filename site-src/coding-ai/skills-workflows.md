# 技能与工作流

Skills & Workflows — 20 条活跃资源

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