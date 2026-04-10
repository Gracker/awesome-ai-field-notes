# 提示技术

Techniques — 12 条活跃资源

### [像 Rust Arena Allocator 一样管理上下文](https://x.com/blackanger/status/2027345330505924638) 
by @blackanger (2026-02-28) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**Agent 上下文管理 = Rust Arena Allocator：append-only、空间局部性、批量释放**

将 Agent 上下文管理类比 Rust Arena Allocator：预留大块连续内存→每次分配指针向前推→所有分配连续排列→整块一起释放。Agent 上下文窗口就是一块有限的、昂贵的内存空间。Prompt Engineering 的核心不是写好文字，而是内存管理。Arena 的核心特性（Append-only、空间局部性、批量释放）直接对应 Agent 上下文设计原则。Pruning 和 RAG 是技巧不是原则。
 `context-management` `rust` `arena-allocator` `agent-design` `prompt-engineering`

---
### [Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) 
by @泊舟 (2026-02-24) | ⭐⭐⭐⭐ 4/5 | 🌍

**上下文工程的开放技能库，按需加载、平台无关**

面向"上下文工程"的开放技能库，管理模型看到的全部输入（系统提示、工具定义、检索文档、消息历史、工具输出）。核心原则：按需加载（启动只加载技能索引，命中任务才加载全文）、保留高信号信息压缩低价值 token。方法平台无关，可迁移到 Claude Code、Cursor 等框架。示例覆盖多 Agent 协作、LLM 评审体系、长期记忆系统。
 `context-engineering` `skills` `agent` `claude-code` `cursor` `lost-in-the-middle`

---
### [How to master prompt engineering](https://x.com/EXM7777/article/2011800604709175808) 
by @Machina (2026-02-26) | ⭐⭐⭐⭐ 4/5 | 🌐

**Prompt 工程的本质是精确的意图建模，不是文字技巧**

核心观点：prompt 工程不是写好的文字，而是精确知道自己想要什么。差距在于你脑中的模糊想法 vs 你能精确表达的程度。文章覆盖了从心理模型到输出精度的完整方法论，强调"看不见的工作"——在坐下来提示之前，先建立清晰的意图模型。
 `prompt-engineering` `mental-model` `precision` `structure`

---
### [2023: AI 的一年 [译]](https://baoyu.io/translations/ai/2023-the-year-of-ai) 
 (2023-12-26) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，techniques 领域相关内容**

2023 年是 AI 领域的关键年份，我们在此聚焦今年对该行业未来发展具有重大影响的主要事件
Read in Cubox  
Read Original
2023 年是 AI 领域的关键年份，我们在此聚焦今年对该行业未来发展具有重大影响的主要事件：
*更正：在 2023 年 12 月 22 日发布的原博客中，标题"AI 发布（AI Releases）"造成了误解，因为内容涵盖了公告、更新及发布等多方面。我们对文本和信息图的标题进行了澄清。Stability AI 对其大语言模型（LLM）开源的提及未出现在信息图中，但保留在文章里，这强调了其在提升可获取性而非仅仅技术改进方面的重要性。信息图最初展示了 xAI 创业公司的成立，现已因不相关而移除。同时，Apple Vision Pro 的提及也被删去，因为文章更侧重于软件。我们还加入了最新发布的 Mid...
 `ChatGPT` `LLM` `Midjourney` `Prompt Engineering` `Vision`

---
### [Google《智能体设计模式》之 智能体推理引擎的内部视角 - 附录F 中翻版](https://mp.weixin.qq.com/s?__biz=MjM5MDExNTY2Nw==&mid=2447768331&idx=1&sn=355262c43a479776e1502d0ca95ae868&chksm=b362dee6a9e871cee8010db2395e017cfccb130cfe10ca12354b043b2dfeb48344dbe8c103ce&mpshare=1&scene=1&srcid=1019OkOWOErLjvi70dEM5m9n&sharer_shareinfo=e0d6e5879044b1fa2169e3ff2bb90d76&sharer_shareinfo_first=e0d6e5879044b1fa2169e3ff2bb90d76) 
 (2025-10-19) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Google 官方智能体设计模式的中文译版**

# Google《智能体设计模式》之 智能体推理引擎的内部视角 - 附录F 中翻版 让大模型自己从内部视角讲解「推理引擎」的运作机制，哪家模型更合你心意？ ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FwV3O1yUmU2QIt4G7kicG7ZdH56SOsxLDLY4HDgOLaMnhxL3gXEo8O23QtLg6sCBIQnWckmxsFcyg0ap6MwecmtQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D0) 前言：这本由谷歌资深工程主管Antonio Gulli免...
 `deepseek` `llm` `大模型` `[]` `agent` `rag` `inference` `gemini`

---
### [去 AI 味的方法 - Agent Skills 写作风格](https://x.com/gkxspace/status/2023173476702728479) 
by @余温 (2026-02-15) | ⭐⭐⭐ 3/5 | 🇨🇳

**实用的去 AI 味方法论：用 Agent Skills 迭代逼近个人写作风格，比提示词更持久有效。**

宝玉老师分享的去 AI 味方法：给 AI 一份持续更新的"写作风格 Skill"（几十到上百行），定义用词偏好、句式习惯、禁止清单、标点规范。具体步骤：1）用 AI 分析自己满意的原创文章生成初版 Skill；2）用 Skill 写一篇文章后自己逐句修改；3）把 AI 原文和修改版发给 AI 分析差异规律并更新 Skill；4）反复迭代，第一次改一半以上，第三次核心风格开始对，第十次 AI 的输出比你自己写的还像你的风格。核心观点：提示词是死的，Skill 是活的，越用越精确。
 `AI写作` `Agent Skills` `去AI味` `写作风格` `Claude Code`

---
### [CHATGPT API（降价 90%）对 LLM 领域的影响 | 高策](http://gaocegege.com/Blog/chatgpt-api) 
 (2023-03-03) | ⭐⭐⭐ 3/5 | 🇨🇳

**关于CHATGPT API（降价 90%）对 LLM 领域的影响的收藏文章**

# CHATGPT API（降价 90%）对 LLM 领域的影响 | 高策 最近人工智能领域一个礼拜一个大新闻，毫不夸张。今天 OpenAI 宣布上线 ChatGPT API，并且相比于 GPT3 davinci 要便宜 90%，跟 curie 价格相同。OpenAI 相当于在 Chat Model 这个领域推出了 ChatGPT 能力的模型，但是价格只有之前的 90%。 因为身处相关行业，所以对这次降价的动作很感兴趣。我想知道这次降价会对 LLM 领域有什么影响，以及对于其他的 AI 产品会有什么影响。以下纯属个人在得知新闻的三个小时内形成的观点，仅供参考。 在 Hacker News 上 ...
 `llm` `[]` `prompt` `openai` `inference` `chatgpt`

---
### [ChatGPT-Siri/README-zh_CN.md at main · Yue-Yang/ChatGPT-Siri · GitHub](https://github.com/Yue-Yang/ChatGPT-Siri/blob/main/README-zh_CN.md) 
 (2023-03-20) | ⭐⭐⭐ 3/5 | 🇨🇳

**关于ChatGPT-Siri/README-zh_CN.md a的收藏文章**

# ChatGPT-Siri/README-zh_CN.md at main · Yue-Yang/ChatGPT-Siri · GitHub 通过 Siri 启动「快捷指令」连接 ChatGPT API，让 Siri 变身 AI 聊天助手。你可以直接和 Siri 说出你的问题，Siri 会回答你。现在我们的 Siri 终于变得智能了，可以和我们对答如流！而这一切只需要一个快捷指令和 API key 就可以做到了。 * 确保网络能正常访问 https://api.openai.com 域名 * 确保 API 帐户有足够余额：<https://platform.openai.com/accoun...
 `[]` `prompt` `gpt-4` `openai` `chatgpt`

---
### [ChatGPT为什么这么强](https://mp.weixin.qq.com/s?__biz=Mzg5MTczODA1OQ==&mid=2247485543&idx=1&sn=979d9efdff1990fb86e2830aadf147b6&chksm=cfc98ac3f8be03d53c15684f7f5afa5a8c24e0a7d70f0092b5d84d8026ac7fee8f6e1b4ead45&mpshare=1&scene=1&srcid=1204kbvTtohAet6jNyPx5e7P&sharer_sharetime=1670221323965&sharer_shareid=b7cc12eb3054f40795517e846030e3c8) 
 (2022-12-05) | ⭐⭐⭐ 3/5 | 🇨🇳

**关于ChatGPT为什么这么强的收藏文章**

1. 从周五到周末ChatGPT已经疯传开来，其对话能力让人惊艳。从玩梗、写诗、写剧本，到给程序找bug，帮人设计网页，甚至帮你生成AIGC的提示词，一副无所不能的样子。可以去Twitter上看Ben Tossell梳理的一些例子，或者自己去试试！一位MBA老师让ChatGPT回答自己的管理学题目，结论是以后不能再布置可以带回家的作业了。很多人用了以后无法自拔，就如这位所见： Musk问ChatGPT怎么设计Twitter(不得不说还挺有创意）： 2. 有人让ChatGPT参加了智商测试，得分83; SAT测试得分1020，对应人类考生52%分位。要知道ChatGPT并没有对数学方面做过优化，...
 `大模型` `fine-tuning` `[]` `prompt` `openai` `chatgpt`

---
### [Generative AI for Beginners](https://microsoft.github.io/generative-ai-for-beginners/?s=09#/translations/cn/) 
 (2024-07-03) | ⭐⭐⭐ 3/5 | 🌍

**微软出品的生成式 AI 入门课程**

# Generative AI for Beginners 通过 12 章的课程，开启构建生成式 AI 应用程序之路 通过微软云技术布道师团队提供的十二章系列课程，了解构建生成式 AI 应用程序的基础知识。 每章都涵盖了生成式人工智能原理和应用程序开发的一个关键方面。 在整个系列课程中，我们将建立我们自己的生成式人工智能初创公司，以便您可以了解如何实现您的想法。 首先，将 整个 repo fork 到您自己的 GitHub 帐户，以便能够更改任何代码并完成相关学习。 您还可以(🌟)该 Fork以便稍后更容易地找到它！ 前往课程学习环境设置 找到最适合您的设置指南！ 我们相信最好的学习方式之一就...
 `[]`

---
### [GitHub - rockbenben/ChatGPT-Shortcut: 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。](https://github.com/rockbenben/ChatGPT-Shortcut) 
 | ⭐⭐⭐ 3/5 | 🇨🇳

**关于GitHub - rockbenben/ChatGPT-Sh的收藏文章**

# GitHub - rockbenben/ChatGPT-Shortcut: 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。 ChatGPT Shortcut 是根据领域和功能划分的 ChatGPT 快捷指令表，可通过标签筛选、关键词搜索和一键复制来使用提示词，旨在简化你的工作流程并提高生产力。即使是初学者，你只需复制提示词，稍加修改后发送给 ChatGPT，就能获得指定输出，让你的生产力加倍！ 提示词（即 Prompt）通常是用户提供的问题或文本，以激活模型生成回复。简单来说，prompt 就是用户想要询问的内容，作为输入送到 ...
 `[]` `openai` `prompt` `chatgpt`

---
### [Google Gemini 如何加速 Android 开发？](https://juejin.cn/post/7472037829506383906) 
 (2025-02-17) | ⭐⭐⭐ 3/5 | 🌍

**Cubox 收藏: Google Gemini 如何加速 Android 开发？**

# Google Gemini 如何加速 Android 开发？ > 《10. 揭秘 Compose 原理》 > 《2 小时入门 Jetpack Compose》 > 《深入理解 Jetpack Lifecycle（原理篇）》 你好，我是朱涛。今天我们来聊聊 AI 和 Android 开发。近些年，基于大模型的人工智能发展迅猛，OpenAI 有 ChatGPT，国内有 Deepseek。然后，我因为和 Google 接触比较多，有幸成为了 Gemini 的第一批使用者，这些年一直用下来，感觉也非常不错。 Android Studio 在最新的版本迭代中，也在积极引入 Gemini 来强化它的 ...
 `deepseek` `大模型` `[]` `openai` `gemini` `chatgpt`

---