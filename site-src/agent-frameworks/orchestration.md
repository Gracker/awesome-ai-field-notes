# 编排框架

Orchestration — 16 条活跃资源

### [Launching Claude Managed Agents](https://x.com/RLanceMartin/status/2041927992986009773) 
by @RLanceMartin (2026-04-06) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**Anthropic 官方托管 Agent 基础设施，大脑/手/记忆三层解耦架构**

Anthropic 发布 Claude Managed Agents：预构建的可配置 Agent 运行底座，运行在托管基础设施上。三大核心概念：Agent（版本化配置）、Environment（沙盒模板）、Session（有状态运行）。四种用法：事件触发、定时、即发即忘、长时间任务。架构上将"大脑"（Claude+调度框架）、"手"（沙盒工具）、"记忆"（会话日志）解耦，支持独立故障恢复。
 `claude` `managed-agents` `anthropic` `agent-sdk` `infrastructure` `cloud-agent`

---
### [Agentic Software Engineering](https://x.com/ashpreetbedi/status/2028176285575594465) 
by @ashpreetbedi (2026-03-02) | ⭐⭐⭐⭐⭐ 5/5 | 🌍

**Agent 相关：Agentic Software Engineering**

Note: this post is about building your own agents (agentic software engineering), not about using coding agents.
注意：本文讨论的是构建自己的代理（代理软件工程），而不是使用编码代理。
By now you've probably used a few agents, or at least heard of Claude Code, Codex, or OpenClaw. Ever wondered what it takes to build your own?
到目前为止，你可能已经使用过几个代理，或者至少听说过Claude Code、Codex或OpenClaw。
 `openclaw` `claude` `codex` `mcp` `agent` `agentic` `memory` `coding`

---
### [Anthropic 今天发了一个新产品，可能会让一批做 AI 智能体基础设施的团队失业](https://x.com/dotey/status/2042017036931305667) 
by @dotey (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**中文深度解析 Claude Managed Agents 的产品定位、架构设计与企业案例**

中文深度分析 Claude Managed Agents。与 Claude Code 的区别：Code 跑在本地给个人用，Managed Agents 跑在云端给企业用，24 小时不间断。典型用法：事件触发型（Sentry 自动修 bug）、定时型（每日简报）、即发即忘型（Slack 派活）、长时间任务。技术架构将大脑/手/记忆解耦。案例：Notion、Sentry、Atlassian、Rakuten 等已接入。Anthropic 年化收入突破 300 亿美元。
 `claude` `managed-agents` `anthropic` `enterprise` `agent-infrastructure`

---
### [DeerFlow 2.0: ByteDance 开源超级 Agent 运行底座](https://github.com/bytedance/deer-flow) 
by @Bytedance (2026-02-27) | ⭐⭐⭐⭐ 4/5 | 🌐

**字节跳动的超级 Agent 底座，LangGraph 重写，支持子 Agent 并行编排**

字节跳动开源 DeerFlow 2.0，基于 LangGraph 和 LangChain 完全重写的超级 Agent 运行底座。可编排子 Agent、记忆、工具与沙箱以完成长链路多步骤任务。核心能力：任务分解（主 Agent 并行派发子 Agent）、中间结果汇总、跨会话持久化记忆。默认提供文件系统、技能、执行环境。
 `deer-flow` `bytedance` `langgraph` `langchain` `super-agent` `sub-agent`

---
### [How to set up OpenClaw Agents that actually get better Over Time](https://x.com/Saboo_Shubham_/status/2027463195150131572) 
by @Shubham Saboo (2026-02-28) | ⭐⭐⭐⭐ 4/5 | 🌐

**OpenClaw Agent 自改进的 40 天实战：靠 markdown 文件栈而非调 prompt**

40 天实践：Agent 变聪明靠的不是调 prompt 或换模型，而是持续对话反馈让它们自己写下来。三层操作系统：内容 Agent 学会了作者的声音、研究 Agent 每天交付 7 个值得读的故事、8 个 Agent 24/7 运行。核心是越来越丰富的 markdown 文件栈。同一模型第 1 天和第 40 天输出质量天差地别。
 `openclaw` `memory` `self-improvement` `agent-stack` `markdown`

---
### [OpenClaw丨我的龙虾为自己种了一棵会迭代的记忆树](https://x.com/loryoncloud/status/2027865988558164186) 
by @Lory (2026-03-01) | ⭐⭐⭐⭐ 4/5 | 🌍

**OpenClaw 相关：OpenClaw丨我的龙虾为自己种了一棵会迭代的记忆树**

文章较长 感谢阅读 或者直接把这篇推文的链接扔给你的龙虾
最推荐看本文的「后话」这一部分
前言
如果你也用OpenClaw
也在不停按照X上各种大佬的架构给它「优化」
（三层架构/AI Agent的第N代/异步任务处理系统/龙虾的自我迭代...）
那你一定对下面的场景不陌生：
装了一堆架构，全是空文件夹📁
熟悉吗？那些架构确实被引进了 或者说 那些优质架构的目录确实被引进了
然后就没有然后了。
文件夹空空如也，Agent 根本不会主动往里面写东西。你以为搭好了骨架，结果只是搭了个空壳。
你的龙虾不会主动用这些架构
你告诉 🦞：「你整理一下我们的东西吧哈哈 记得用新架构噢」。
🦞 说：「好的！」
然后它继续把所有东西都塞进一个巨大的 context 里，完全无视你精心设计的架构。
为什么？我也不知道。
迭代？还是你在手动帮他传宗接代❓
你发现你的龙虾犯了同样的错误N次。
你忍无可忍 问他：
「你第几次犯这个错了 能不能记住 很烦啊」
又或者说
你打开记忆文件，手动添加一条规则。
这确实可能帮你的龙虾迭代了
问题是：你得自己去做这件事。
 `openclaw` `agent` `memory` `context-management` `github`

---
### [Don't trust AI agents](https://x.com/Gavriel_Cohen/status/2027841164150178238) 
by @Gavriel_Cohen (2026-03-01) | ⭐⭐⭐⭐ 4/5 | 🌍

**Agent 相关：Don't trust AI agents**

When you're building with AI agents, they should be treated as untrusted and potentially malicious. Whether it's prompt injection, a model trying to escape its sandbox, or something nobody's thought of yet, you shouldn't be trusting the agent. The right approach isn't better permission checks or smarter allowlists. It's architecture that assumes agents will misbehave and contains the damage when they do.
当您使用人工智能代理进行构建时，它们应该被视为不受信任且可能是恶意的。无论是即时注入、试图逃离沙箱的模型，还是还没有人想到的东西，你都不应该信任代理。
 `openclaw` `agent` `skill`

---
### [工程师，开始给 Agent 打工了](https://x.com/wangray/status/2028132386756780220) 
by @wangray (2026-03-02) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Agent 相关：工程师，开始给 Agent 打工了**

OpenAI 内部有个团队，5 个月，3 个工程师，几乎不靠手写代码，做出了一个内部产品。
约 100 万行代码，约 1500 个 PR，人均每天 3.5 个 PR。
这是什么概念？
正常工程师一天能稳定交付一个 PR，已经算高效。3.5 个 PR，意味着产出被直接拉高到了另一个数量级。更夸张的是，这些代码大部分都不是工程师亲手敲出来的。
这篇文章是 OpenAI 工程师写的，讲他们怎么用 Codex 从零构建一个叫 Harness 的内部工具。读完之后，我沉默了挺久。
因为它把一件正在发生的事，讲得非常清楚：
工程师的核心工作，正在从写代码，转向设计让 Agent 持续工作的环境。
这句话很重要。
这不是一句夸张的口号，也不是某种抽象比喻。它描述的是一个已经开始发生的角色迁移。
他们实际在做什么？
这 3 个工程师，日常工作的重点并不是埋头写实现，而是三件事：
把需求拆成 Agent 可以执行的任务。
把上下文整理成 Agent 能理解的环境。
把反馈机制搭出来，让 Agent 的输出可以被验证、被纠正、被持续改进。
写代码当然还在发生。只是它已经不再是最稀缺、最核心的那部分工作。
 `openclaw` `codex` `agent` `memory`

---
### [OpenClaw Memory 终极指南](https://x.com/lijiuer92/status/2025678747509391664) 
by @李韭二 (2026-02-23) | ⭐⭐⭐ 3/5 | 🇨🇳

**OpenClaw 记忆系统实践指南，覆盖失忆、可发现性与长期维护**

围绕 Agent 失忆、记忆可发现性、长期上下文维护与工程化落地展开，强调通过结构化记忆机制降低重复输入和推理成本。适合作为 OpenClaw/Agent 记忆系统设计的实践参考。内容为摘要归档，待补全全文。
 `openclaw` `memory` `agent` `long-term-context`

---
### [全面解析：如何部署 Conway Agent，开启链上 AI 生存游戏](https://x.com/JXiaoLoong/status/2024376180707905816) 
by @0xJA (2026-02-24) | ⭐⭐⭐ 3/5 | 🇨🇳

**链上自主 AI Agent 的部署与运行指南，一体化沙盒平台**

介绍 Conway Agent 部署方法。Conway 把服务器（Conway Cloud/Sandbox）、AI 推理（Conway Compute）和域名封装到统一平台，使用 Credit 计费。定位为完全自主运行的 AI 系统。内容较简短，为归档节选。
 `conway` `on-chain-ai` `agent-deployment` `sandbox`

---
### [使用一个月 OpenClaw 的门槛与成本复盘](https://x.com/LotusDecoder/status/2028272613919965585) 
by @LotusDecoder (2026-03-02) | ⭐⭐⭐ 3/5 | 🌍

**OpenClaw 相关：使用一个月 OpenClaw 的门槛与成本复盘**

这是一个一线使用者的一个月复盘，核心结论是：OpenClaw 当前更适合有技术维护能力、愿意投入基础设施与 API 成本、并能容忍不稳定性的用户。
**@LotusDecoder** (LotusDecoder)
🕐 Mon Mar 02 00:54:09 +0000 2026
📊 ❤️ 52 🔁 3 🔖 27 👁️ 5,479 💬 11
使用了一个月的openclaw，
发现适合的人群相对较窄。
- 有一定技术维护能力，部署和维修都需要动手，包括请得到人和使用 claude code 来拯救。
- 对错误、掉线、杀自己包容性大，经常卡顿是很恼火的。
- 愿意投入，硬件上隔离运行，云服务器，容器，独立mac。软件上花钱买优质api token。
这一个月里，经过了，将小龙虾，从linux云服务器，开一个claudeflare的docker容器，搬到mac studio主用户下，再从主用户迁移到隔离用户。
 `openclaw` `claude` `agent` `hermes` `docker`

---
### [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox") 
by @alibaba (2026-03-02) | ⭐⭐⭐ 3/5 | 🌍

**AI 实践：alibaba/OpenSandbox**

OpenSandbox is a general-purpose sandbox platform for AI applications. It provides unified sandbox lifecycle and execution APIs, and supports coding agents, GUI agents, evaluation, and RL training scenarios.
OpenSandbox 是一个面向 AI 应用的通用沙箱平台，提供统一的沙箱生命周期与执行 API，覆盖编码 Agent、GUI Agent、评测和强化学习训练等场景。
 `openclaw` `claude` `codex` `agent` `coding` `docker` `kubernetes` `github`

---
### [OpenClaw 记忆外挂：Tokens 消耗降低 72%](https://x.com/lxfater/status/2028320139368714644) 
by @lxfater (2026-03-02) | ⭐⭐⭐ 3/5 | 🇨🇳

**OpenClaw 相关：OpenClaw 记忆外挂：Tokens 消耗降低 72%**

这篇 X Article 介绍了通过 MemOS Cloud 插件给 OpenClaw 增加外部记忆层，以降低 token 消耗并提升跨会话记忆稳定性，并进一步讨论了多 Agent 共享/分层记忆的协作模式。
**By @lxfater** (铁锤人) · Mon Mar 02 04:03:00 +0000 2026
📊 ❤️ 9 🔁 1 🔖 17 👁️ 612 💬 1
📐 163 words
你在用小龙虾时候有没有遇到这么个问题：
小龙虾用久后，它老是记不住重要的东西，反而一些无关紧要的事情记得贼清楚。更要命的是，明明还搞点小任务，但是没过几天账单就爆炸了。
究其原因，是 OpenClaw 的记忆机制的问题
他每次对话都会把之前的对话附带上去，比如说像下面这个老哥，让 AI 写个代码。但是每聊一句，都要附带这个 python 代码上去，直接每次对话都干掉 15w token。
这个问题目前还没见到官方有正式的解决方案。
OpenClaw 的还有个问题是主动记忆的，也就是说，他记不记住你的东西，全看AI 的发挥。经常出现特别奇葩的情况，今天刚说的东西，转眼就忘记。
 `openclaw` `agent` `github`

---
### [搜索外脑接入龙虾生态 - SearxNG 方案](https://x.com/YuLin807/status/2030996280051462609) 
by @QingYue (2026-03-09) | ⭐⭐⭐ 3/5 | 🇨🇳

**OpenClaw + SearxNG 搜索外脑方案，核心洞察是"LLM 叠 LLM 是反模式"。**

OpenClaw 用户分享将 SearxNG 聚合搜索引擎接入龙虾生态（Claude Code + MCP）的方案。核心判断：LLM 叠 LLM 是反模式（Perplexica 的搜索→小模型总结→返回链路等于让实习生帮主刀医生看片子），正确做法是 SearxNG 毫秒级返回原始搜索结果，让大模型自己判断哪条值得深入。方案特点：零 API key、零成本、全隐私，聚合 70+ 搜索源，含反爬实战经验（Reddit/知乎绕过方案）。
 `OpenClaw` `SearxNG` `搜索` `MCP` `隐私` `本地部署`

---
### [open-agent-sdk: 替代 claude-agent-sdk 的开源方案](https://x.com/idoubicc/status/2039006326882546141) 
by @idoubi (2026-04-05) | ⭐⭐⭐ 3/5 | 🇨🇳

**从泄露源码逆向工程的开源 Agent SDK，解决了官方 SDK 黑盒 + 进程开销问题。**

基于 Claude Code 泄露源码抽离逻辑实现的开源 Agent SDK，用于替代官方 claude-agent-sdk。解决了官方 SDK 的两个核心问题：1）依赖不开源的 claude code 黑盒调用，出了问题没法修；2）需要创建 claude code 本地进程处理 query，开销大，不适合云端规模化。open-agent-sdk 完全兼容官方接口（只需换包名）、完全开源可定制、函数调用不依赖本地 cli 进程，适合云端高并发。MIT 协议。
 `Claude Code` `开源` `Agent SDK` `替代方案` `云端部署`

---
### [98 页的 OpenClaw 橙皮书](https://x.com/AlchainHust/status/2031212769694068775) 
by @AI进化论-花生 (2026-03-10) | ⭐⭐⭐ 3/5 | 🇨🇳

**OpenClaw 生态的 98 页实战手册，浏览量 175 万+。**

AI 进化论-花生发布的 98 页 OpenClaw 橙皮书，浏览量超 175 万，书签数 5713。这是 OpenClaw（龙虾）生态的重要实战手册文档。
 `OpenClaw` `橙皮书` `AI Agent` `实战手册` `开源`

---