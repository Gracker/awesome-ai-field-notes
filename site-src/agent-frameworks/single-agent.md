# 单Agent框架

Single-Agent — 6 条活跃资源

### [Hermes 从 0 到 1 教程](https://x.com/Pluvio9yte/status/2041571378021986486) 
by @Pluvio9yte (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Nous Research 开源自改进 Agent 框架，内置持久记忆与 Skill 进化**

介绍 Nous Research 开源的自改进 AI Agent 框架 Hermes。核心特点：内置学习循环，每次完成任务后自动提炼可复用 Skill 存入持久记忆。多层记忆系统（短期+长时+Skills），支持 40+ 工具。与 OpenClaw 对比：Hermes 重单个 Agent 深度自我成长，OpenClaw 强在多平台覆盖和复杂工作流。内置 hermes claw migrate 迁移命令。
 `hermes` `nous-research` `self-improving` `agent` `memory` `openclaw`

---
### [AI 正在推动程序员的进化，而不是灭亡 | 宝玉的分享](https://baoyu.io/blog/ai-is-evolving-programmers) 
 (2025-02-22) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，single-agent 领域相关内容**

AI 正在推动程序员的进化，而不是灭亡 | 宝玉的分享
Read in Cubox  
Read Original
这是纽约时报新刊登的一篇 AI 对程序员影响的文章，有人担心 AI 很快会自动取代数百万个工作岗位，文章主要观点还是认为 AI 正在推动程序员的进化，而不是灭亡，创造力、批判性思维、解决问题的能力、沟通能力、共情能力------这些才是人们在未来需要持续培养的技能。当然，还要学会如何管理和使用好这些 AI 工具。
同时 HackerNews 上关于这篇文章也有不少讨论，一起整理后放在附录中供参考。
微软等公司推出的 AI 工具正辅助编写代码，让软件工程师站在这项技术对劳动力市场所带来冲击的最前沿。
 `ChatGPT` `Agent`

---
### [AI 重构软件工程：OpenAI Harness Engineering，程序员不写代码的时代来了](https://mp.weixin.qq.com/s?__biz=MzIxMzE2OTA1NA==&mid=2247504549&idx=1&sn=1960d1b4f5adc272beafe02769b70080&chksm=9662df573f9f31d5e66ca65058639cc344e2a32d8650454025313de92c8dead3c053a30c7101&mpshare=1&scene=1&srcid=0310AcGnRt8mXm5THdB5S6Y3&sharer_shareinfo=8ce3a2d537351730960ccb449abb2755&sharer_shareinfo_first=d7497129c2be0b41a6e58b76c66a5a05) 
 (2026-03-10) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，single-agent 领域相关内容**

AI 重构软件工程：OpenAI Harness Engineering，程序员不写代码的时代来了
，OpenAI 在工程博客发布的《Harness engineering: leveraging Codex in an agent-first world》，抛出了一个颠覆软件工程界的实验结果：一支初始 3 人的工程师团队，从空 Git 仓库起步，仅用 5 个月时间，依靠 Codex+GPT-5 构建出一款拥有约 100 万行代码的
Read in Cubox  
Read Original
一、百万代码零手写，OpenAI 工程实验
二、驾驭工程：不是 AI 写代码，而是驯服
 `OpenAI` `Agent` `RAG`

---
### [Anthropic：我们如何构建多智能体研究系统](https://mp.weixin.qq.com/s?__biz=Mzk1NzgxMjQ0OA==&mid=2247489816&idx=1&sn=989928020101777361b9c63b8dbffe55&chksm=c20cbcb2151edc3ac638589b0596dd4fe44cd919c177b6033ee9dcefb168fe0edd78c4e5bebb&mpshare=1&scene=1&srcid=0618VxXV1qhfuDCmQJUMYfMO&sharer_shareinfo=da3ecd986cd6fcfad23734ec74fa6282&sharer_shareinfo_first=cd4cf214372e755c614fa457c6332cda) 
 (2025-06-18) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**关于 AI Agent 的收藏文章**

Anthropic：我们如何构建多智能体研究系统
我们的研究（Research）功能利用多个 Claude 智能体，来更有效地探索复杂主题。
Read in Cubox  
Read Original
我们的研究（Research）功能利用多个 Claude 智能体，来更有效地探索复杂主题。在此，我们分享构建这一系统时遇到的工程挑战以及我们学到的经验教训。
现在，Claude 具备了研究能力^\[1\]^，能够横跨网络、Google Workspace 及任何集成应用进行搜索，以完成复杂的任务。
 `Claude` `Anthropic` `Inference` `Performance`

---
### [Trace2Skill](https://arxiv.org/abs/2603.25158) 
 (2026-04-07) | ⭐⭐⭐ 3/5 | 🇨🇳

**LLM 推理能力增强的新方法**

LLM Agent 需要领域特定技能（skills）才能高效处理复杂任务。但技能创建面临三重困境：

1. 人工编写不可扩展：每个领域都需要专家花大量时间写详细的操作指南，随着 Agent 应用场景扩展，这个瓶颈越来越严重
2. 纯 LLM 生成效果差：直接让 LLM 凭参数化知识写技能，缺乏对目标领域具体操作和常见陷阱的了解，收益有限
3. 在线顺序更新导致碎片化：现有在线范式（如 ExpeL、Skill-Gen）按顺序处理每条轨迹，一条轨迹学一个教训就更新一次技能，导致技能碎片化且容易过拟合
 `obsidian` `fine-tuning` `agent` `llm` `paper` `reasoning` `memory` `ai`

---
### [Android 系统上 AI Agent 的一些可能性](https://mp.weixin.qq.com/s?__biz=MjM5Njg5ODU2NA==&mid=2257503010&idx=1&sn=a1337986bbada15f63dbe267d3eed8b4&chksm=a4d3255f3f334e0c66fe400364a60299207afff6b4439a6478704ac5176681af7eaa202627af&mpshare=1&scene=1&srcid=1205CnGTws2OF7LnyRN95gYS&sharer_shareinfo=39c2afd703555e8ad0b770170b5eba98&sharer_shareinfo_first=564c134774d8cff2fe4b03464d899095) 
 (2025-12-05) | ⭐⭐⭐ 3/5 | 🇨🇳

**关于 AI Agent 的收藏文章**

Android 系统上 AI Agent 的一些可能性
Read in Cubox  
Read Original
最近，我注意到手机端 AI Agent 应用的兴起，例如 DroidRun 和 AutoGLM。这类应用能够模拟用户操作，在手机上自动执行任务，全程无需人工干预------比如自动发布一篇小红书笔记，或是在美团上点一杯咖啡。
**对用户而言，这类应用的核心价值在于解放双手、节省时间。** 想象一下，那些每日重复的应用签到、定时的优惠券抢购、或是在不同应用间搬运信息的繁琐操作，都可以交给一个不知疲倦的后台"数字助理"来完成。这不仅极大地提升了个人效率，更让用户能将精力专注于更有创造力和价值的事情上。
然而，这些应用在实现上普遍面临一个核心痛点：**独占屏幕** 。当 Agent 运行时，它会接管手机屏幕，导致用户无法使用自己的手机。加之目...
 `Agent` `Android` `AI Safety`

---