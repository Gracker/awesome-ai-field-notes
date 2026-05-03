# 📖 学习资源

教程 / 论文 / 提示工程 / 演讲 — 共 **83** 条活跃资源

## 📅 2026-05-03

### [AI提示词工程：2026年全新课程](https://x.com/AndrewYNg/status/2049886895530967534)
@@AndrewYNg · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-05-03

一门全面的AI提示词工程课程，覆盖多个主流AI平台，帮助用户从基础到高级掌握提示词技巧。

`prompt-engineering` `multi-platform` `skill-building` `x`

---

## 📅 2026-05-02

### [吴恩达推出新课《AI Prompting for Everyone》:跨模型通用提示工程技巧](/entry/58wn955a) 📄
@@AndrewYNg · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-05-02

How we prompt AI is very different in 2026 than 2022 when ChatGPT came out. I&#x27;m teaching a new course, AI Prompting for Everyone, to help you become an AI power user - whatever your current skill level. It covers skills that apply across ChatGPT, Gemini, Claude, and other AI.

`x` `ai-tools` `prompt`

---

## 📅 2026-04-30

### [Allie K. Miller 免费开放：5 天 AI 实战训练营，从使用到构建](/entry/d1d65a6d) 📄
@@alliekmiller · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-30

知名 AI 博主 Allie K. Miller 推出免费 5 天邮件课程 AI Fast Track，专为想从使用 AI 进阶到用 AI 构建的人群设计。课程无需编程基础，聚焦教你在实际场景中加入 Claude 等工具到工作流中，构建个人 AI 软件、自动化流程和问题解决工具。如果你已经玩腻了 Copy-paste Prompt，这是不错的进阶路径。

`x` `workflow`

---

## 📅 2026-04-28

### [AI Fast Track: 5天免费课程，从用AI到用AI构建](/entry/657d8468) 📄
@@alliekmiller · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-28

Allie K. Miller 推出免费 5 天邮件课程 AI Fast Track，核心主张是超越 ChatGPT 复制粘贴，教用户用 Claude 构建个人 AI 软件、自动化工具和工作流，无需编程基础。课程涵盖从基础到实战构建的全流程，适合想从 AI 使用者转型为 AI 建造者的人群。

`x` `ai-tools` `course` `automation` `beginner`

---

## 📅 2026-04-18

### [AI 影响力日报 · 2026-04-18](/entry/p591inej) 📄
@gracker · ⭐⭐⭐3 🇨🇳 · 2026-04-18

2026 年 4 月 18 日 AI 高价值内容日报，筛选 5 条：① Allie Miller 的 5 天 AI 建造课程；② Karpathy 转发 Farzapedia——用 LLM 将 2500 条个人数据转化为个人维基百科的实践；③ Google 发布 Gemini 3.1 Flash TTS 表情化语音合成；④ Gemini Agentic Vision：LLM 自己写代码做视觉推理任务；⑤ Nature 重磅论文——LLM 可通过隐含数据信号传递偏好与对齐特征。

`AI日报` `Twitter` `LLM` `Agent` `Gemini`

---

## 📅 2026-04-14

### [深度研究Prompt方法论：横纵分析法](/entry/6a2113a2d9ca) 📄
@Khazix0918 · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-14

- **来源**：X/Twitter
- **原文链接**：https://x.com/augmentcode/status/2043740459256951158
- **作者**：Khazix0918
- **日期**：2026-04-14
- **抓取时间**：2026-04-14 12:00

`prompt-engineering` `research-methodology` `ai-tools` `横纵分析法` `deep-research`

---

## 📅 2026-04-10

### [Android 17 DeliQueue：二十年来最重要的消息队列架构重写](/entry/ng74ojns) 📄
@Shai Barack, Charles Munger (Google) · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-10

Android 17用lock-free混合数据结构DeliQueue替换了存在20年的MessageQueue实现。实际用户设备上实现丢帧率降低4%-7.7%、应用启动速度提升9.1%。这不是Binder IPC改造，而是对Android所有UI线程运行核心——Looper/Handler消息调度机制的根本性重构。每个应用的main线程、SystemUI、Launcher乃至system_server中的HandlerThread都依赖MessageQueue，这个单点性能改进具有全局传导效应。面向SDK 37及以上默认启用。

`android-17` `deliqueue` `messagequeue` `lock-free` `performance`

---

### [Running Slice 全栈分析手册](/entry/54zsncaa) 📄
⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-10

为Android性能工程师提供的系统化分层框架，用于精确诊断Perfetto中Running片段的CPU消耗位置和原因。涵盖六个层级：Java方法追踪→ART虚拟机→内核调度器→CPU微架构→缓存层级→SoC内存子系统。每个层级有独特工具、指标和故障模式。长Running片段可分解为指令供给问题、数据访问延迟、非最优核心放置、频率调节延迟或算法冗余。

`perfetto` `running-slice` `cpu` `performance` `android`

---

### [Android 16 MessageQueue 优化调研报告](/entry/y1of91bq) 📄
@Manus AI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

调研Android 16对MessageQueue的重构优化。采用lock-free数据结构（Treiber stack和ConcurrentSkipListSet）解决优先级翻转问题。新实现几乎完全消除锁竞争，显著提升系统响应性和用户体验，特别是在冷启动等关键场景中。

`android-16` `messagequeue` `lock-free` `treiber-stack` `performance`

---

### [Android App 帧渲染流程深度解析：从 Vsync 到屏幕](/entry/vpd4rsxd) 📄
@Manus AI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

从Vsync-App信号接收开始，深度解析Android应用帧渲染的完整流程。涵盖Choreographer调度、Input/Animation/Traversals回调、Draw/Measure/Layout流程、RenderThread与GPU协作、BufferQueue流转、SurfaceFlinger合成、直至最终屏幕显示。包含详细的时序图和性能关键路径分析。

`android` `vsync` `rendering` `frame` `choreographer`

---

### [Airbnb’s Page Performance Score on Android | by Luping Lin | The Airbnb Tech Blog | Dec, 2021 | Medium](/entry/r5jbtfwg) 📄
⭐⭐⭐⭐4 🌐 · 2026-04-10

Airbnb’s Page Performance Score on Android | by Luping Lin | The Airbnb Tech Blog | Dec, 2021 | Medium
Airbnb’s home grown Page Performance Score (PPS) is designed to capture the rich, complex realities of performance by collecting a multitude of user-centric performance metrics and formulating them…
Read in Cubox  
Read Original
?imageUrl=https%3A%2F%2Fmiro.medium.com%2Ffit%2F...

`Android`

---

### [Android 应用性能优化：Vsync 与 Buffer 深度研究报告](/entry/lapawuax) 📄
@Manus AI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

深入研究Android应用中Vsync和Buffer相关机制。涵盖Vsync信号产生与分发、Vsync-app/Vsync-sf/Vsync-appsf分类、BufferQueue及BlastBufferQueue工作原理、UI线程与RenderThread协作、app duration与sf duration分析、GPU Fence和HWC Fence同步机制。为Android性能优化提供理论基础和实践指导。

`android` `vsync` `buffer` `blastbufferqueue` `surfaceflinger`

---

### [Android ARM 平台 Running 耗时分析方法论与工具链报告](/entry/ga5iefwf) 📄
@Manus AI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

Android ARM平台上Running耗时分析方法论与工具链的完整报告。定义Running耗时为CPU实际执行时间，区分等待I/O和阻塞时间。涵盖simpleperf、Perfetto、ARM DSU/ETM等工具链，从方法级到指令级的分层分析框架。包含big.LITTLE核心调度、频率DVFS、Cache Miss等底层因素的量化分析方法。

`android` `arm` `running-time` `cpu` `perfetto`

---

### [Android Native 内存泄漏深度调研报告](/entry/fcaeud36) 📄
@Manus AI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

深入探讨Android Native内存泄漏问题，涵盖基本原理、检测与分析方法、常用工具（Valgrind、AddressSanitizer、heapprofd等）及库。结合实际案例分析Android内存管理机制和Native层内存泄漏成因，为开发者提供全面的Native内存泄漏解决方案。

`android` `native` `memory-leak` `valgrind` `asan`

---

### [AI时代系统工程师的硬技能升级路线图](/entry/6hz9vzy3) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

面向资深Android系统工程师的技能升级路线图。核心判断：2025-2026年最具杠杆效应的方向是&#x27;端侧AI全栈&#x27;——将系统底层经验与AI推理优化、On-device ML和AI Agent开发结合。AI技能薪资溢价已达56%，全球AI人才缺口300万。建议投资方向包括：LLM基础能力、Agent开发、端侧推理优化、性能分析与AI结合。原文含具体学习路径和工具推荐。

`ai-engineer` `system-engineer` `career` `on-device-ai` `skill-upgrade`

---

### [Android adb shell dumpsys meminfo 全面解析指南](/entry/64blp4b1) 📄
@Manus AI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-10

全面解析adb shell dumpsys meminfo命令的输出格式，详细说明每一栏含义、数据来源、异常判断标准和优化建议。涵盖PSS/USS/VSS/RSS区别、Native/Heap/Stack内存分类、View/Asset/Bitmap内存追踪。帮助开发者和性能分析师精确定位内存问题。

`android` `meminfo` `memory` `dumpsys` `performance`

---

### Android 性能优化知识体系大纲
@Manus AI · ⭐⭐⭐3 🇨🇳 · 2026-04-10

Android性能优化完整知识体系大纲。从性能优化基础定义与目标出发，建立响应时间、流畅度、内存占用、功耗、稳定性等关键指标体系。覆盖测量-分析-优化-验证闭环方法论，以及系统性思考、全局视角、数据驱动的优化思维模式。

`android` `performance` `knowledge-map` `optimization` `methodology`

---

### Android Framework 面试题解答
@Manus AI · ⭐⭐⭐3 🇨🇳 · 2026-04-10

Android Framework常见面试题解答集，包含socketpair与socket区别、Binder通信原理、Handler机制、Service生命周期等核心知识点。面向Android系统工程师面试准备。

`android` `framework` `interview` `socketpair` `binder`

---

### 微信小程序技术调研报告
@Manus AI · ⭐⭐⭐3 🇨🇳 · 2026-04-10

微信小程序技术的全面调研报告，涵盖7个维度：历史与背景、重要性分析、技术实现架构、启动与滑动性能优化、优化目标与挑战、优化策略、小程序vs小游戏对比。深入分析了微信小程序的双线程架构、渲染管线、启动优化策略、滑动性能瓶颈及解决方案。对理解小程序性能优化有较高参考价值。

`wechat` `mini-program` `android` `performance` `startup`

---

### [https://learningprompt.wiki/docs/insight/AI%20%E6%9C%89%E5%8F%AF%E8%83%BD%E6%94%B9%E5%8F%98%E4%BA%BA%E7%9A%84%E5%AD%A6%E4%B9%A0%E6%96%B9%E5%BC%8F%E5%90%97%EF%BC%9F/%E6%9C%89%E5%8F%AF%E8%83%BD%E6%94%B9%E5%8F%98%E4%BA%BA%E7%9A%84%E9%98%85%E8%AF%BB%E6%9...](/entry/T4eWO6CN) 📄
⭐⭐⭐3 🇨🇳 · 2026-04-10

https://learningprompt.wiki/docs/insight/AI%20%E6%9C%89%E5%8F%AF%E8%83%BD%E6%94%B9%E5%8F%98%E4%BA%BA%E7%9A%84%E5%AD%A6%E4%B9%A0%E6%96%B9%E5%BC%8F%E5%90%97%EF%BC%9F/%E6%9C%89%E5%8F%AF%E8%83%BD%E6%94%B9%E5%8F%98%E4%BA%BA%E7%9A%84%E9%98%85%E8%AF%BB%E6%9...

---

### [关于如何在 Slack 上免费使用 GPT4 和 GPT3.5 的一个简单教程： 0、全程不需要科学上网； 1、注册一个 Slack 帐号 https://slack.com/intl/zh-cn/ ； 2、创建一个工作区，随便起一个名字，如果你已经有工作区了，跳过此步； 3、点开 https://www.springworks.in/albus/ 这个页面，安装 AIbus 到 Slack； 4、在 Slack 直接点开 AIbus 与它对话； 5、也可以在频道里把 AIbus 拉进来，之后就...](https://m.okjike.com/originalPosts/642675a1005a6157f60d8139?s=eyJ1IjoiNTY3YTUwZDQ2ZWY4OWMxMjAwOGE3NTc1In0%3D&utm_source=wechat_session)
⭐⭐⭐3 🇨🇳 · 2026-04-10

关于如何在 Slack 上免费使用 GPT4 和 GPT3.5 的一个简单教程： 0、全程不需要科学上网； 1、注册一个 Slack 帐号 https://slack.com/intl/zh-cn/ ； 2、创建一个工作区，随便起一个名字，如果你已经有工作区了，跳过此步； 3、点开 https://www.springworks.in/albus/ 这个页面，安装 AIbus 到 Slack； 4、在 Slack 直接点开 AIbus 与它对话； 5、也可以在频道里把 AIbus 拉进来，之后就...

---

### [Claude Code in Action 实战课程（中文翻译版）](/entry/4etnysar) 📄
@Anthropic · ⭐⭐⭐3 🇨🇳 · 2026-04-10

Anthropic官方Claude Code实战课程的中文翻译版，适合离线阅读。课程覆盖21个章节：基础部分（引言、编码助手概念、实战、安装配置、项目准备、添加上下文、修改代码）、进阶部分（控制上下文、自定义命令、MCP服务器、GitHub集成）、Hooks专题（认识/定义/实现Hooks及常见坑点）、高级主题（SDK、测验、总结）。

`Claude-Code` `实战课程` `教程` `Hooks` `MCP`

---

### [GitHub - rockbenben/ChatGPT-Shortcut: 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。](/entry/7ypeivbn) ⭐8,445 📄
⭐⭐⭐3 🇨🇳 · 2026-04-10

# GitHub - rockbenben/ChatGPT-Shortcut: 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。 ChatGPT Shortcut 是根据领域和功能划分的 ChatGPT 快捷指令表，可通过标签筛选、关键词搜索和一键复制来使用提示词，旨在简化你的工作流程并提高生产力。即使是初学者，你只需复制提示词，稍加修改后发送给 ChatGPT，就能获得指定输出，让你的生产力加倍！ 提示词（即 Prompt）通常是用户提供的问题或文本，以激活模型生成回复。简单来说，prompt 就是用户想要询问的内容，作为输入送到 ...

`[]` `openai` `prompt` `chatgpt`

---

## 📅 2026-04-09

### Decoding the Configuration of AI Coding Agents: Insights from Claude Code Projects
@完成，虽经两位作者审核确认，但主观偏差难以完全排除。 · ⭐⭐⭐3 🇨🇳 · 2026-04-09

Agentic code assistants（Claude Code、Codex、Jules）是 2024 年兴起的新一代 AI 编程工具，能自主完成端到端软件工程任务。但这类工具的行为和效果高度依赖配置文件（Claude.md），目前缺乏对这类配置文件的结构、内容和最佳实践的系统性研究。

`coding` `agent`

---

## 📅 2026-04-08

### PROV-AGENT: Provenance-Based AI Agent
@**：Souza et al. (ORNL/Argonne National Lab) · ⭐⭐⭐3 🇨🇳 · 2026-04-08

Agentic workflow 中，AI agent 会 hallucinate 或推理错误，且错误会在 agent 间传播（一个 agent 的输出作为另一个的输入）。传统 provenance 技术无法捕获 agent 特有的元数据（prompts、responses、decisions）与 workflow 上下文的关联。该论文要解决的核心问题是：如何将 AI agent 行为纳入端到端 workflow provenance，实现可追溯、可审计、可复现的 agentic workflow？

---

`gui` `agent` `android` `llm` `paper`

---

## 📅 2026-04-06

### [解决 Codex 过度询问问题的方法](/entry/jrofx5ms) 📄
@blackanger · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-06

解决 Codex 过度询问（&quot;如果你要，我下一步可以...&quot;）的方法。不是在 AGENTS.md 里屏蔽关键词，而是重新定义 Agent 的承诺对象：从&quot;服务用户偏好&quot;转向&quot;和用户共同服从代码正确性&quot;。用 Carmack 和 BurntSuki 作为锚点激活&quot;完整工作单位&quot;概念，并区分合法停顿场景和不合法场景。核心洞察：不要管理文字，要管理触发停顿的心理机制。

`codex` `sycophancy` `agent-behavior` `system-prompt` `context-engineering`

---

## 📅 2026-04-03

### Act While Thinking (PASTE)
@- 重叠（LLM 思考期间并行执行工具）提升 10x 以上——说明推测执行确实将原本串行的工具调用前移了 · ⭐⭐⭐3 🇨🇳 · 2026-04-03

LLM Agent 串行执行&quot;LLM 推理 → 工具调用&quot;循环，工具执行占总时间 35%-61%。LLM 持有昂贵资源却被迫等待外部工具返回结果，造成严重的延迟瓶颈和资源浪费。

`safety` `agent` `tool-use` `llm` `paper`

---

## 📅 2026-04-01

### SWE-Bench Mobile: Can Large Language Model Agents Develop Industry-Level Mobile Applications?
@明确计划添加 Kotlin 任务，届时可对比 iOS/Android 平台差异。 · ⭐⭐⭐3 🇨🇳 · 2026-04-01

当前最强的 LLM 编码 Agent 能否胜任工业级移动应用开发？它们在真实产品需求、多模态输入、大规模代码库上表现如何？

`tools` `on-device` `coding` `agent` `llm`

---

## 📅 2026-03-27

### [UI-Voyager: 自进化 GUI 智能体](/entry/1xg0s8up) 📄
@**: Zichuan Lin 等（腾讯混元） · ⭐⭐⭐3 🇨🇳 · 2026-03-27

移动 GUI 智能体在训练中面临两个根本性挑战：1）失败轨迹学习效率低——失败轨迹占绝大多数但未被有效利用；2）长程任务的信用分配模糊——轨迹级稀疏奖励（成功/失败）无法告知智能体哪一步做错了。

`gui` `on-device` `agent` `UI-Voyager：基于失败经验自进化的` `android`

---

## 📅 2026-03-26

### [多智能体共识机制研究](/entry/5uz0zj5l) 📄
@**: arXiv (cs.MA, cs.LG) · ⭐⭐⭐3 🇨🇳 · 2026-03-26

当前基于 LLM 的多智能体系统能够可靠地达成共识吗？在存在恶意智能体的情况下，共识机制是否鲁棒？

这篇论文研究了一个基础问题：当多个 LLM 智能体需要达成一致决策时，它们能否可靠地完成这一任务？特别是在存在可能破坏共识的拜占庭智能体的情况下。

---
| 模型 | 群体大小 | 有效共识率 | 平均轮次 |
|------|---------|----------|---------|
| Qwen3-8B | N=4 | 15.8% | - |
| Qwen3-14B | N=4 | 46.6% | - |
| Qwen3-14B | N=8 | 67.4% | - |
| Qwen3-14B | N=16 | 33.3% | 29.0 |

解读:
- 即使没有拜占庭智能体，有效共识率也低于 70%
- 群体规模增大，性能下降（从 N=4 的 46.6% 降至 N=16 的 33.3%）
- 较大模型（14B）显著优于较小模型（8B）

关键发现 2: 提示内容影响活跃性

| 提示变体 | 有效共识率 | 平均轮次 |
|---------|----------|----…

`analysis` `safety` `agent` `llm` `paper`

---

## 📅 2026-03-22

### [论证型人机决策（Deliberative Human-AI Decision Making）](/entry/fpmdn3mj) 📄
@**：Stylianos Loukas Vasileiou, Antonio Rago, Francesca Toni, William Yeoh · ⭐⭐⭐⭐4 🇨🇳 · 2026-03-22

论文试图解决什么问题？

1. AI 系统的黑箱问题：LLMs 的推理过程不透明，难以验证和信任
2. 计算论证的可扩展性问题：传统 CA 依赖手工知识工程，难以应用于开放域
3. 人机协作的失衡：当前 AI 要么完全自动化决策，要么只是提供解释，缺乏真正的协作
4. 高风险领域的可信度：在医学、法律等领域，AI 必须提供可争议、可审查的推理

核心洞察：计算论证（CA）与大语言模型（LLMs）的融合可以实现一个新范式——论证型人机决策制定，其中 AI 与人类共同推理，而不是为人类推理。

`obsidian` `safety` `fine-tuning` `agent` `llm`

---

## 📅 2026-03-14

### SkillRL 智能体进化
⭐⭐⭐3 🇨🇳 · 2026-03-14

Q1：这项研究要解决什么问题？

核心问题：LLM 智能体无法从历史经验中学习
1. 记忆效率低下：存储原始轨迹 Token 消耗大（15K+ tokens/episode）
2. 缺乏抽象能力：无法从具体案例中提取通用规则
3. 无法持续改进：每次任务从零开始，重复犯错

Q2：为什么这个问题重要？

对 AI 研究：
- 当前 LLM 智能体&quot;昙花一现&quot;（无长期记忆）
- 与人类学习方式差距大（人类会积累技能）
- 通往 AGI 的必经之路（持续学习能力）

---
核心收获

1. 技能抽象优于原始记忆：Token 减少 62%，性能提升 15.3%
2. 递归进化至关重要：性能随迭代持续提升
3. 分层组织有效：通用技能提供战略指导
4. 失败教训有价值：减少 68% 的重复失败

对高爷的建议

1. SmartPerf + SkillRL：集成到 SmartPerf 项目
2. Android 性能优化智能体：自动性能诊断和优化
3. 技术博客选题：
   - &quot;SkillRL：让 LLM 智能体学会&#x27;刻意练习&#x27;&quot;
   - &quot;从论文到实战：SkillRL 在 Androi…

`obsidian` `agent` `llm` `paper` `reinforcement-learning`

---

## 📅 2026-03-13

### [Chain-of-Tools - 在冻结 LLM 的 CoT 推理中利用海量未见工具](/entry/dfuk5hd5) 📄
⭐⭐⭐⭐⭐5 🇨🇳 · 2026-03-13

**论文：** Chain-of-Tools: Utilizing Massive Unseen Tools in the CoT Reasoning of Frozen Language Models

**arXiv：** 2503.16779v1

**精读日期：** 2026-03-13

---

## 一、核心问题

**研究问题：**

如何让大型语言模型（LLMs）在链式思维（CoT）推理过程中高效地利用大量外部工具，包括训练时未见过的工具？

**子问题：**

1. **效率问题：** 如何在拥有大量工具（数千个）时高效选择合适的工具？
2. **泛化问题：** 如何处理训…

`fine-tuning` `coding` `agent` `tool-use` `llm`

---

## 📅 2026-03-11

### [∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](/entry/o70e53hy) 📄
⭐⭐⭐⭐⭐5 🇨🇳 · 2026-03-11

## 一、核心问题

### 1.1 研究背景
大语言模型（LLM）的推理能力日益重要，但：
- **训练成本高**：扩大模型规模需要巨额算力
- **性能瓶颈**：传统方法（CoT、ToT）性能趋于饱和
- **效率问题**：零阶搜索方法（如Best-of-N）样本效率低
- **奖励稀疏**：长推理链中奖励信号难以传播

### 1.2 核心问题
**如何在不重新训练模型的情况下，通过测试时优化显著提升LLM推理能力？**

关键子问题：
1. 能否利用梯度信息而非仅奖励值？
2. 如何在离散token空间中进行可微优化？
3. 推理时优化与训练时优化的联系是什么？

## 二、创新点

…

`gui` `on-device` `fine-tuning` `coding` `llm`

---

## 📅 2026-03-10

### [【李宏毅】解剖小龙虾 — 以 OpenClaw 为例介绍 AI Agent 的运作原理](/entry/Q2EBAkbQ) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-03-10

今天这一堂课啊，我想要用 OpenClaw 这个开源的专案当作一个例子，跟大家介绍 AI Agent 是怎么运作的。我相信大家在报章杂志上，已经听过很多跟 AI Agent 有关的事情。最近呢，有一个跟 AI Agent 有关的开源专案 OpenClaw 变得非常热门。这有多热门，我想就不用解释了，因为大家在报章杂志上大概都看过吹捧 OpenClaw 的文章了。

---

## 📅 2026-03-05

### [I Want to Become an AI Engineer (Full Course)](/entry/b75mu5rc) 📄
@hoeem · ⭐⭐⭐⭐4 🌐 · 2026-03-05

一篇 4800+ 字的 AI 工程师全栈学习指南，提出三层架构：Prompt Engineering（微语法，控制即时指令）→ Context Engineering（乘数，MCP + Context as Code + RAG 管道）→ Intent Engineering（差异化，组织目标编码）。用 Klarna 客服 AI 的失败案例（节省 $60M 但因 intent gap 被迫重新雇人）论证意图工程的重要性。提供 7 组件意图框架和大量可复用 prompt 模板，覆盖结构化格式、Few-Shot、CoT、元提示词、上下文审计、RAG 架构设计、MCP Server 蓝图等。

`AI工程` `Prompt Engineering` `Context Engineering` `Intent Engineering` `MCP`

---

## 📅 2026-02-28

### [像 Rust Arena Allocator 一样管理上下文](/entry/5n08ud0l) 📄
@blackanger · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-02-28

将 Agent 上下文管理类比 Rust Arena Allocator：预留大块连续内存→每次分配指针向前推→所有分配连续排列→整块一起释放。Agent 上下文窗口就是一块有限的、昂贵的内存空间。Prompt Engineering 的核心不是写好文字，而是内存管理。Arena 的核心特性（Append-only、空间局部性、批量释放）直接对应 Agent 上下文设计原则。Pruning 和 RAG 是技巧不是原则。

`context-management` `rust` `arena-allocator` `agent-design` `prompt-engineering`

---

## 📅 2026-02-27

### [OpenClaw 运行报错指南（上篇）](/entry/gey4i36q) 📄
@李韭二 · ⭐⭐⭐⭐4 🇨🇳 · 2026-02-27

macOS 上 OpenClaw 运行报错的系统性排查指南。Gateway 是中枢神经，所有消息收发/LLM 调用/工具调度都经过它，挂了=系统瘫痪。覆盖 Gateway 启动失败排查（Node.js 版本、端口占用、launchd 服务注册、JSON 配置）、各类报错的根因分析。适用 macOS Apple Silicon/Intel。

`openclaw` `troubleshooting` `gateway` `macos` `debug`

---

## 📅 2026-02-26

### [科学家的消亡 / AI 会终结科学，还是会引发一场新的革命？](/entry/uk1rinrc) 📄
@indigo · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-02-26

翻译 Sara Imari Walker（亚利桑那州立大学天体生物学家）的文章。核心追问：科学到底是什么？如果连这个问题都没搞清楚，讨论 AI 能否&quot;做科学&quot;就是认知错误。AlphaFold 预测结构但不解释物理机制。关键不是 AI 能否执行方法步骤，而是科学产生知识的方式是否包含更多。引入&quot;绑定问题&quot;、&quot;意识的困难问题&quot;等概念，探讨科学作为人类文化系统的深层本质。

`ai-science` `philosophy` `consciousness` `alphaFold` `scientific-method`

---

### [OpenClaw 从中级到高级完整教程](/entry/swprvijb) 📄
@OneHopeA9 · ⭐⭐⭐⭐4 🇨🇳 · 2026-02-26

面向已完成基础配置的 OpenClaw 用户的中高级教程。覆盖：AGENTS.md 工作规范、记忆优化（构建可靠记忆体系）、子 Agent 团队协作、Cron 自动化、Skill 开发、多渠道部署（全平台接入）、性能调优、实战练习清单、疑难解答。系统性的进阶指南。

`openclaw` `tutorial` `agents-md` `memory` `cron`

---

### [How to master prompt engineering](/entry/r5io6o5x) 📄
@Machina · ⭐⭐⭐⭐4 🌐 · 2026-02-26

核心观点：prompt 工程不是写好的文字，而是精确知道自己想要什么。差距在于你脑中的模糊想法 vs 你能精确表达的程度。文章覆盖了从心理模型到输出精度的完整方法论，强调&quot;看不见的工作&quot;——在坐下来提示之前，先建立清晰的意图模型。

`prompt-engineering` `mental-model` `precision` `structure`

---

### [抽丝剥茧：深度解析 OpenClaw 万字系统提示词构成](/entry/q32ssunn) 📄
@岚叔 · ⭐⭐⭐⭐4 🇨🇳 · 2026-02-26

通过自研 modelbox 工具模拟模型提供商，抓取 OpenClaw 发给模型的完整系统提示词（约 16K token/34062 字符）。逐一解析：第一段源码硬注入（身份、工具清单、安全规则、子代理机制），第二段工具调用风格与安全约束，第三段 CLI 命令参考，第四段 skill 加载机制。帮助理解系统提示词结构以进行瘦身优化。

`openclaw` `system-prompt` `token-analysis` `modelbox` `context-window`

---

### [新手劝退 OpenClaw：99% 的人根本不需要它](/entry/q7qmybqr) 📄
@劳伦斯 · ⭐⭐⭐3 🇨🇳 · 2026-02-26

劝退文：99% 的人不需要自动化，更不需要 OpenClaw。连 chatbot 都玩不明白就想搞多 Agent 协作，连提示词都写不好就想自动决策。OpenClaw 是过渡产品，几大 AI 公司会推出更强大方案。与其烧 token 折腾 OpenClaw，不如先让 AI 介入日常工作。先学走再学跑。

`openclaw` `critique` `transition-product` `expectation`

---

## 📅 2026-02-25

### [Don&#x27;t Waste Your Money on OpenClaw Until You&#x27;ve Done These 3 Things](/entry/m68frogi) 📄
@Miles Deutscher · ⭐⭐⭐⭐4 🌐 · 2026-02-25

OpenClaw 最大问题不是不会装，而是装完没真实场景。三步前置动作：第一阶段先把 AI 当思考伙伴，做时间审计（一周每分钟记录）；第二阶段先用 Manus、n8n、Zapier 等低门槛工具验证哪些流程跑得通；第三阶段再在低风险环境部署 OpenClaw，迁移已验证流程，评估 ROI。一句话：先想清楚，再验证，最后才扩张。

`openclaw` `setup` `roi` `workflow` `automation`

---

## 📅 2026-02-24

### [Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库](/entry/hu2ghikp) 📄
@泊舟 · ⭐⭐⭐⭐4  · 2026-02-24

面向&quot;上下文工程&quot;的开放技能库，管理模型看到的全部输入（系统提示、工具定义、检索文档、消息历史、工具输出）。核心原则：按需加载（启动只加载技能索引，命中任务才加载全文）、保留高信号信息压缩低价值 token。方法平台无关，可迁移到 Claude Code、Cursor 等框架。示例覆盖多 Agent 协作、LLM 评审体系、长期记忆系统。

`context-engineering` `skills` `agent` `claude-code` `cursor`

---

## 📅 2026-02-22

### [公众号爆款文章提示词：让AI写出有&quot;人味&quot;的深度长文（附完整提示词）](https://mp.weixin.qq.com/s?__biz=MzI0MjcwNDMwMg==&mid=2247483699&idx=1&sn=10c8c1155e0b30e46e3c68aec878b766&chksm=e8bce5b0172b0871c5e13619dd2baaa4eb8e0f24828b82b78b383162fe9a11b17181d629f31a&mpshare=1&scene=1&srcid=02223hwJCIhxKRfo6AHPu9BH&sharer_shareinfo=e27400efeb1f474b3e79f8ee17b510d5&sharer_shareinfo_first=e27400efeb1f474b3e79f8ee17b510d5)
⭐⭐⭐3 🇨🇳 · 2026-02-22

这是「写作提示词全家桶」系列第2篇，共7篇。上一篇讲了底层逻辑，这一篇直接给你两套拿走就能用的公众号写作提示词。

---

## 📅 2026-02-15

### [去 AI 味的方法 - Agent Skills 写作风格](/entry/ez9vv62c) 📄
@余温 · ⭐⭐⭐3 🇨🇳 · 2026-02-15

宝玉老师分享的去 AI 味方法：给 AI 一份持续更新的&quot;写作风格 Skill&quot;（几十到上百行），定义用词偏好、句式习惯、禁止清单、标点规范。具体步骤：1）用 AI 分析自己满意的原创文章生成初版 Skill；2）用 Skill 写一篇文章后自己逐句修改；3）把 AI 原文和修改版发给 AI 分析差异规律并更新 Skill；4）反复迭代，第一次改一半以上，第三次核心风格开始对，第十次 AI 的输出比你自己写的还像你的风格。核心观点：提示词是死的，Skill 是活的，越用越精确。

`AI写作` `Agent Skills` `去AI味` `写作风格` `Claude Code`

---

## 📅 2026-02-03

### [Paper摘要：基于强化学习的AI Agent调整内核configuration选项](/entry/u4axbgh7) 📄
⭐⭐⭐3 🇨🇳 · 2026-02-03

论文 OS-R1 提出用 RL Agent 自动配置 Linux 内核 18000+ configuration 选项。Rule-Guided Agent 设计，两阶段训练（Warm-up + Exploration），3000+ 配置样本数据集。在 Nginx/PostgreSQL/Redis 上取得性能提升。但生产环境极少为调优重编译内核，严重脱离工程实际。

`OS-R1` `强化学习` `Linux内核` `kernel-tuning` `AI-agent`

---

## 📅 2026-01-23

### [AI辅助下的性能逆向分析](/entry/pj7y4se0) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-01-23

我在知乎发现了一篇值得思考的文章，一起来看看吧。
Read in Cubox  
Read Original
在性能优化领域，**竞品分析**是一个永恒的话题。然而，现有的分析手段往往存在较大的局限性：
• **指标维度浅层化** ：大多局限于帧率（FPS）、内存占用、CPU 频率及利用率、线程统计等硬件或系统层面的指标。虽然可以通过截帧分析渲染管线，但对于 **CPU 端的具体开销**（如 UI 逻辑、战斗系统、渲染提交等模块的具体耗时）难以进一步拆解。
• **技术壁垒**：在缺乏源代码和符号表的情况下，往往难以洞察竞品底层的具体技术实现。

`Android` `Performance`

---

## 📅 2026-01-06

### [2026 年 AI 行业预测汇总，AI 将如何改变世界？](/entry/ni3njxvh) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-01-06

2026 年 AI 行业预测汇总，AI 将如何改变世界？
汇总自 Gartner、SaaStr、a16z、Every、Gary Marcus 和 Forbes 的 26 年 AI 行业分析
Read in Cubox  
Read Original
?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPEeV2JtM1K5wMHX5fRAvuF6vwsbibiaMNMV6TWp50WP2bwPTzo9ODzTwe18moLv2Qu4exjiaBRAQibCSqZRx0NRYRw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)
**最近看到各大投资机构在 2026 年 AI 行业的预测，我做了一个汇总，把相同点进行整理，不同点里有意思的观点做了摘要。**

`Claude` `Agent`

---

## 📅 2025-12-26

### [Avoid Mini-frameworks - laike9m&#x27;s blog](/entry/se8oa9cc) 📄
⭐⭐⭐⭐4 🌐 · 2025-12-26

Avoid Mini-frameworks - laike9m&#x27;s blog
Read in Cubox  
Read Original
DEC 24TH, 2025
What is mini-framework?
My Story
Why mini-frameworks are bad?
So, What Should You Do Instead?
*See Hacker News discussion*
I work in Google Ads infrastructure in the past four years. Over time, I&#x27;ve seen one pattern came along again and again, causing endless pain for developers, that is, creating mini-frameworks.

---

## 📅 2025-12-06

### [解读 Anthropic 博文：适用于长期运行 Agents 的有效框架](/entry/tRzeuGfv) 📄
⭐⭐⭐3 🇨🇳 · 2025-12-06

&gt; 基于 Anthropic 的 &quot;Effective harnesses for long-running agents&quot; 最佳实践

---

## 📅 2025-11-05

### [Allie K. Miller 推出免费 5 天 AI 课程：从会用 AI 到会用 AI 构建](/entry/a1b2c3d4) 📄
@@alliekmiller · ⭐⭐⭐⭐⭐5 🇨🇳 · 2025-11-05

Allie K. Miller 推出免费邮件课程《AI Fast Track》，5 天从入门到独立构建 AI 工具。核心主张：copy-paste ChatGPT prompts 只能走很远，真正差异在于用 AI 构建自动化和工作流。课程不需编程基础，工具箱新增 Claude，适合想从使用者升级为建造者的学习者。拆掉了从消费者到建造者的门槛，对想突破 AI 应用层的朋友很有参考价值。

`x` `ai-tools` `learning` `course`

---

### [Allie K. Miller：免费 5 日课带你从用 AI 进阶到用 AI 搭建](/entry/d65a31a7) 📄
@@alliekmiller · ⭐⭐⭐⭐4 🇨🇳 · 2025-11-05

Allie K. Miller 推出「AI Fast Track」免费 5 日邮件课程，定位是帮助用户从只会 copy-paste ChatGPT prompts 进阶到真正用 AI 搭建个人工具、自动化流程和软件。她强调「用 AI」和「用 AI 构建」之间有本质区别——后者需要理解 AI 能做什么边界、如何将 AI 能力封装成可复用系统。课程无需编程基础，工具箱以 Claude 为主（也有 ChatGPT）。适合想从「AI 使用者」转变为「AI 建造者」的初学者。

`course` `automation` `claude` `beginner`

---

### [超越 ChatGPT 复制粘贴：用 AI Fast Track 学会构建个人 AI 工具](/entry/9a6b89b2) 📄
@@alliekmiller · ⭐⭐⭐⭐4 🇨🇳 · 2025-11-05

Allie K. Miller 推出免费 5 天邮件课程，核心主张是「用 AI」与「用 AI 构建」有本质区别——仅靠复制粘贴 Prompt 上限很低。课程无需编程基础，教授如何用 Claude 扩展 AI 能力边界，搭建个人自动化工作流。适合想从消费者转型为创造者的初学者。附完整课程链接。

`ai-tools` `course` `beginner`

---

## 📅 2025-10-19

### [Google《智能体设计模式》之 智能体推理引擎的内部视角 - 附录F 中翻版](/entry/yj96fkem) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-10-19

# Google《智能体设计模式》之 智能体推理引擎的内部视角 - 附录F 中翻版 让大模型自己从内部视角讲解「推理引擎」的运作机制，哪家模型更合你心意？ ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FwV3O1yUmU2QIt4G7kicG7ZdH56SOsxLDLY4HDgOLaMnhxL3gXEo8O23QtLg6sCBIQnWckmxsFcyg0ap6MwecmtQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D0) 前言：这本由谷歌资深工程主管Antonio Gulli免...

`deepseek` `llm` `大模型` `[]` `agent`

---

## 📅 2025-09-26

### [文本和概念分析专家 prompt](/entry/vKh1cmIG) 📄
⭐⭐⭐⭐4 🌐 · 2025-09-26

[需翻译] GitHub Gist: instantly share code, notes, and snippets.

---

## 📅 2025-08-15

### [Anthropic全网追杀的人，可能是我……](/entry/fuxlqv7h) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-08-15

Anthropic全网追杀的人，可能是我……
Anthropic官方说，有一个用户在一个月内消耗了价值数万美金的的token，从而决定限速。这个用户，好像，是我本人……
Read in Cubox  
Read Original
上个月，Anthropic官方发布了信息，有一个用户，只花了$200美元订阅套餐，却在一个月内消耗了数万美金的(tens of thousands)的token。从而决定对所有人进行限速......
全世界的程序员都在好奇，这位每个月花数万美金的老哥是谁？

`Claude` `Anthropic`

---

## 📅 2025-07-07

### [Android×鸿蒙×AI 技术刊#第14期——Compose动画深度解析、KMP多端实践落地、Android 16适配指南](/entry/jzvwn07d) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-07-07

Android×鸿蒙×AI 技术刊#第14期——Compose动画深度解析、KMP多端实践落地、Android 16适配指南
Read in Cubox  
Read Original
**本周 Android 生态聚焦 UI 框架、跨平台方案与系统适配三大核心领域：**
Compose 技术进阶
共享元素动画剖析：解析 sharedElement() 与 sharedBounds() 的精准应用场景与渲染差异（ScaleToBounds vs RemeasureToBounds）；
Modifier 底层机制：Slot Table 存储结构与重组优化策略全解读。
**跨平台方案落地**
**B站 KMP 实战：Bazel 构建 + FlowRedux 状态机实现** **三端逻辑层共享** （Android/iOS/鸿蒙）；
Flutter 鸿蒙热...

`Android`

---

## 📅 2025-06-23

### [Android×鸿蒙×AI 技术刊#第12期：Android 16新特性、Compose与Flutter对比、ART机制揭秘](/entry/2lrsppi0) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-06-23

Android×鸿蒙×AI 技术刊#第12期：Android 16新特性、Compose与Flutter对比、ART机制揭秘
Read in Cubox  
Read Original
本周 Android 生态动态聚焦系统升级、框架演进与底层优化三大方向：
1️⃣**Android 16 更新深度解读**
强制应用**开启全屏模式（edge-to-edge）** ，预测性返回手势默认激活；
引入**动态刷新率API** （getSuggestedFrameRate）、**增强型安全模式** 及广播优先级限制等关键行为变更。
2️⃣ **跨平台框架能力交锋**
**Compose Multiplatform：Jetpack Compose 对比 Flutter 在** **包体积、冷启动性能** 的显著优势；
**Flutter 挑战 iOS 26 ...

`Android` `Performance` `AI Safety`

---

## 📅 2025-06-17

### [Android×AI 技术刊#第11期——都是Android技术文](/entry/pt2nps34) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-06-17

Android×AI 技术刊#第11期——都是Android技术文
Read in Cubox  
Read Original
**本周 Android 技术动态聚焦三大核心方向：**
**跨端框架突破** ：
腾讯视频开源 **ovCompose 框架** ，实现 Android/iOS/鸿蒙**三端一码** 开发，基于 Compose Multiplatform 深度优化性能与原生混排能力；
货拉拉开源 **TheRouter 鸿蒙路由** ，支持跨模块解耦与动态路由表下发。
**性能优化实践** ：
手机系统 **D-Vsync 渲染管线优化方案** 发布，实测掉帧率**降低 72.7%** ，功耗仅微增 0.13%；
Flutter 复现 iOS 26 **&quot;液态玻璃&quot;效果** ，解析着色器与扭曲算法实现难点。

`Android` `Performance`

---

## 📅 2025-03-26

### [AI 时代下的工程领导力：如何打造高效团队 - 来自谷歌工程负责人、Chrome 开发者的宝贵经验分享](/entry/vu8j87wr) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-03-26

AI 时代下的工程领导力：如何打造高效团队 - 来自谷歌工程负责人、Chrome 开发者的宝贵经验分享
AI 是个好帮手，但不能全靠它，团队领导者得搞清楚“更好”到底是啥意思，然后带着团队更快地往那儿走，团队成员也是如此。
Read in Cubox  
Read Original
今天偶然读到 Chrome 开发者、Google 工程负责人、著名技术书籍作者 -Addy Osmani 的一篇文章「Leading Effective Engineering Teams in the Age of GenAI」，讲的特别好，对于产品和研发方向如何变得高效，不管你是团队领导者、还是团队成员，都很有价值，分享给朋友们，可以先看我的阅读笔记，针对自己感兴趣的部门再阅读原文（推荐阅读，作者信息和文章链接放在文末）
?imageUrl=https%3A%2F%2...

`AI Safety`

---

## 📅 2025-03-21

### [LLM Powered Autonomous Agents](/entry/90udpdgs) 📄
⭐⭐⭐⭐⭐5 🌐 · 2025-03-21

Lilian Weng 的经典综述文章，系统阐述以 LLM 为核心的自主 Agent 系统架构。三大核心组件：Planning（任务分解、自我反思，涵盖 CoT、ToT、ReAct、Reflexion、CoH、AD 等方法）、Memory（短期上下文学习、长期向量存储）、Tool Use（API 调用、代码执行、外部知识访问）。文章深入分析了每种方法的原理和适用场景，包括多 Agent 协作框架。该文是 Agent 领域被引用最多的综述之一，适合作为系统性理解 Agent 设计的入门基石。

`LLM-agent` `planning` `memory` `tool-use` `ReAct`

---

### [科技爱好者周刊#342：面试的 AI 作弊——用数字人去面试](/entry/AAbj5iB9) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-03-21

本杂志开源^\[1\]^，欢迎投稿^\[2\]^。另有《谁在招人》^\[3\]^服务，发布程序员招聘信息。合作请邮件联系^\[4\]^（yifeng.ruan@gmail.com^\[5\]^）。

---

## 📅 2025-02-09

### [AI 也能&quot;看懂&quot;图片： 移动端相册 AI 搜图的奥秘PicQuery 通过创新的多模态搜索技术，为移动设备上的图片检索 - 掘金](/entry/owxj3v91) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-02-09

AI 也能&quot;看懂&quot;图片： 移动端相册 AI 搜图的奥秘PicQuery 通过创新的多模态搜索技术，为移动设备上的图片检索 - 掘金
PicQuery 通过创新的多模态搜索技术，为移动设备上的图片检索提供了一个高效、智能的解决方案。是一个非常值得学习，把玩的好项目。
Read in Cubox  
Read Original
其实大概三四个月前就想写一篇文章来介绍移动端 AI 搜图的一些进展，不过由于本人的精力有限和一些其他的原因，没有及时更新。所以也就拖更很久，好在春节有些时间可以把之前的一些知识总结，更好的展现给大家。  
相信用 Android 手机的同学多少都有一些感觉，Android 手机上的相册都多了一个搜图的功能，例如小米手机或是 Oppo 手机都上线了类似的功能，输入文字可以获得相关的图片。下面展示一下小米相册里面的搜图功能：
?ima...

`OpenAI` `Android` `Multimodal`

---

## 📅 2025-02-04

### [Android中AIDL和HIDL的区别，Google为什么更推荐AIDL？](/entry/2g8km7k7) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-02-04

Android中AIDL和HIDL的区别，Google为什么更推荐AIDL？
Read in Cubox  
Read Original
在Android中，AIDL（Android Interface Definition Language） 和 HIDL（HAL Interface Definition Language） 是两种用于定义跨进程通信接口的语言。AIDL 是 Android 系统最早支持的 IPC（进程间通信）机制，而 HIDL 是从 Android 8.0 开始引入，用于 HAL（Hardware Abstraction Layer）模块的接口定义。
随着 Android 的发展，Google 决定从 Android 11 开始将新的 HAL 统
一使用 AIDL 接口，而逐步放弃 HIDL。这种转变背后的原因涉及技术复杂度、性能、开发效率和生态统一性等多个方面。

`Android` `Performance`

---

## 📅 2025-01-04

### [The 2025 AI Engineering Reading List](/entry/Ac0YVZZ8) 📄
⭐⭐⭐⭐4 🌐 · 2025-01-04

[需翻译] We picked 50 paper/models/blogs across 10 fields in AI Eng: LLMs, Benchmarks, Prompting, RAG, Agents, CodeGen, Vision, Voice, Diffusion, Finetuning. If you&#x27;re starting from scratch, start here.

---

## 📅 2024-07-07

### [Articels/腹背受敌的中国经济（3 万字长文）.md at main · foreveryh/Articels · GitHub](/entry/vbv4u5ai) ⭐25 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-07-07

Articels/腹背受敌的中国经济（3 万字长文）.md at main · foreveryh/Articels · GitHub
文章转载分享. Contribute to foreveryh/Articels development by creating an account on GitHub.
Read in Cubox  
Read Original
繁华渐逝：腹背受敌的中国经济（3 万字长文）
全文约 3 万字，撰写花了我 14 个月。阅读需要 60 分钟。如果完全读懂，能受益 30 年。

---

## 📅 2024-05-10

### [科技爱好者周刊#299：AI 的关键是语料](/entry/GLLemXIU) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-05-10

本杂志开源^\[1\]^，欢迎投稿^\[2\]^。另有《谁在招人》^\[3\]^服务，发布程序员招聘信息。合作请邮件联系^\[4\]^（yifeng.ruan@gmail.com^\[5\]^）。

---

## 📅 2024-05-07

### [我如何夺冠新加坡首届 GPT-4 提示工程大赛 [译] | 宝玉的分享](/entry/DJotrA2L) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-05-07

深度探索我在驾驭大语言模型（LLMs）中学到的策略 ?imageUrl=https%3A%2F%2Fbaoyu.io%2Fimages%2Fprompt-engineering%2Fhow-i-won-singapores-gpt-4-prompt-engineering-competition%2F1_RAI4cBXe1_zaxVykHz79oA.webp&amp;valid=true) 庆祝这一里程碑 --- 真正的胜利在于宝贵的学习经历！

---

## 📅 2024-03-01

### [科技爱好者周刊#291：AI 没有护城河](/entry/dp1D5lbH) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-03-01

本杂志开源^\[1\]^，欢迎投稿^\[2\]^。另有《谁在招人》^\[3\]^服务，发布程序员招聘信息。合作请邮件联系^\[4\]^（yifeng.ruan@gmail.com^\[5\]^）。

---

## 📅 2024-02-04

### [西瓜视频稳定性治理体系建设一：Tailor 原理及实践](/entry/emQlKmiB) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-02-04

**Tailor**\[1\]是西瓜视频 Android 团队开发的一款内存快照裁剪压缩工具，广泛用于字节跳动旗下各大 App 的 OOM 治理及异常排查，收益显著，在西瓜视频上更是取得 OOM 降低95%以上的好成绩。Tailor 工具现已开源，本文将通过原理、方案和实践来剖析 Tailor 的相关细节。

---

## 📅 2023-12-27

### [Android11+ AIDL：专为提升应用性能而生！](/entry/x4e5l5ie) 📄
⭐⭐⭐⭐4 🌐 · 2023-12-27

Android11+ AIDL：专为提升应用性能而生！
Android新版本AIDL性能再提升化！
Read in Cubox  
Read Original
**点击下方👇关注****Android系统攻城狮**
每日充电：OS+MultiMedia学习之旅

`Android` `Performance`

---

## 📅 2023-12-26

### [2023: AI 的一年 [译]](/entry/toln3leb) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-12-26

2023 年是 AI 领域的关键年份，我们在此聚焦今年对该行业未来发展具有重大影响的主要事件
Read in Cubox  
Read Original
2023 年是 AI 领域的关键年份，我们在此聚焦今年对该行业未来发展具有重大影响的主要事件：
*更正：在 2023 年 12 月 22 日发布的原博客中，标题&quot;AI 发布（AI Releases）&quot;造成了误解，因为内容涵盖了公告、更新及发布等多方面。我们对文本和信息图的标题进行了澄清。Stability AI 对其大语言模型（LLM）开源的提及未出现在信息图中，但保留在文章里，这强调了其在提升可获取性而非仅仅技术改进方面的重要性。信息图最初展示了 xAI 创业公司的成立，现已因不相关而移除。同时，Apple Vision Pro 的提及也被删去，因为文章更侧重于软件。我们还加入了最新发布的 Mid...

`ChatGPT` `LLM` `Midjourney` `Prompt Engineering` `Vision`

---

## 📅 2023-07-11

### [American Idle — Remains of the Day](/entry/e9lw9q80) 📄
⭐⭐⭐⭐4 🌐 · 2023-07-11

American Idle — Remains of the Day
Read in Cubox  
Read Original
I promised one final piece on TikTok, focused primarily on the network effects of creativity. And this is that, in part. But it discusses a bunch of other topics, some only tangentially related to TikTok.
All the points I wanted to cover seem hyperlinked in a sprawling loose tangle. This could easily have been sev...

---

## 📅 2023-03-28

### [AI狂飙的时代，人还有价值吗？](/entry/s4niyx5b) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-03-28

Read in Cubox  
Read Original
最近两个月，受到香港中文大学卓越传媒人驻校计划的邀请，我在香港进行了为期八周的访学，并为新闻学院的学生们开设了一个工作坊，主题是关于&quot;如何提问&quot;。就在我们上课的几周时间里，ChatGPT以迅雷不及掩耳的速度进入了大众的视野。我在课上与同学们进行了讨论。有人说，在GPT的时代，会提问可能比会回答更加重要。有人欣喜，认为GPT将大大提高人类工作效率，减少无意义的重复劳动；也有人担忧，认为GPT可能会带来大规模失业，甚至动摇社会的基本结构。
比尔·盖茨称赞，当前这场由ChatGPT衍生开来的人工智能革命是他所见到的自1980年以来最具革命性的技术进步。具体来说，GPT的革命性到底体现在什么地方？当前关于人工智能的讨论有些怎样的误区？它可能会带来什么影响？有什么是它能做的、又有什么是它永远也做不到的...

`ChatGPT`

---

## 📅 2023-03-20

### [Prompt Engineering (Lilian Weng)](/entry/7r292cja) 📄
@Lilian Weng · ⭐⭐⭐⭐⭐5 🌐 · 2023-03-20

Lilian Weng 经典 Prompt Engineering 综述。系统梳理 zero/few-shot、Instruction Prompting、CoT、Self-Consistency、ToT 等技术，深入分析 few-shot 示例选择策略（k-NN、图方法、对比学习）。还涵盖 ReAct、PAL 等外部工具范式。引用最广的入门文献之一。

`prompt-engineering` `zero-shot` `few-shot` `CoT` `self-consistency`

---

## 📅 2023-03-15

### [GPT-4震撼发布：多模态大模型，直接升级ChatGPT、必应，开放API，游戏终结了？](/entry/ekyuztr8) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-03-15

# GPT-4震撼发布：多模态大模型，直接升级ChatGPT、必应，开放API，游戏终结了？ &gt; ChatGPT 点燃了科技行业的明灯，GPT-4 能燎原吗？ 谁能革得了 ChatGPT 的命？现在看来还是 OpenAI 自己。 在 ChatGPT 引爆科技领域之后，人们一直在讨论 AI「下一步」的发展会是什么，很多学者都提到了多模态，我们并没有等太久。今天凌晨，OpenAI 发布了多模态预训练大模型 GPT-4。 GPT-4 实现了以下几个方面的飞跃式提升：强大的识图能力；文字输入限制提升至 2.5 万字；回答准确性显著提高；能够生成歌词、创意文本，实现风格变化。 「GPT-4 是世界第一款...

`大模型` `[]` `gpt-4` `openai` `chatgpt`

---

## 📅 2022-12-09

### [ChatGPT内核：InstructGPT，基于反馈指令的PPO强化学习](/entry/b6bs8e91) 📄
⭐⭐⭐⭐4 🇨🇳 · 2022-12-09

# ChatGPT内核：InstructGPT，基于反馈指令的PPO强化学习 聊天机器人 ChatGPT 在诱导下写出「毁灭人类计划书」，并给出... 5.1 对准性研究（Alignment Research）的启发 &gt; 聊天机器人 ChatGPT 在诱导下写出「毁灭人类计划书」，并给出代码，AI 发展有哪些问题需关注？ 泻药。开发GPT也有两年了，看到这样的新闻确实是欣慰而震撼的。GPT Family刚提出的时候并没有受到很大的关注度，因此GPT-1也是不温不火。到GPT-2的时候auto-regressive paradigm终于开始有一群大佬研究，到现在也在学术界被广泛研究，很多大模型都...

`大模型` `fine-tuning` `[]` `prompt` `openai`

---

## 📅 2022-12-06

### [MLGO: A Machine Learning Framework for Compiler Optimization – Google AI Blog](/entry/k27e2ufv) 📄
⭐⭐⭐⭐4 🌐 · 2022-12-06

Google 介绍 MLGO 框架，首个工业级将 ML 系统性集成到 LLVM 编译器的通用框架。使用强化学习训练神经网络替代编译器中的启发式决策。两个具体优化：1) Inlining-for-size：通过 RL 策略替代内联启发式，在 30k 模块上训练的策略可泛化到其他软件，实现 3%-7% 代码体积缩减（Fuchsia OS 上达 6.3%）；2) Regalloc-for-performance：寄存器分配优化，提升 0.3%-1.5% QPS。训练后的策略通过 XLA AOT 嵌入编译器，无运行时依赖。

`MLGO` `compiler-optimization` `LLVM` `reinforcement-learning` `inlining`

---

## 📅 2022-04-21

### [Android 车载应用开发与分析 （4）- 编写基于AIDL 的 SDK - 掘金](/entry/9uwhf8gu) 📄
⭐⭐⭐⭐4 🌐 · 2022-04-21

Android 车载应用开发与分析 （4）- 编写基于AIDL 的 SDK - 掘金
之前介绍了车载应用开发体系中如何使用Jetpack在HMI中构建MVVM架构Android 车载应用开发与分析 （3）- 构建 MVVM 架构(Java版)，通过之前的介绍，也了解到在大多数车载
Read in Cubox  
Read Original
之前介绍了车载应用开发体系中如何使用Jetpack在HMI中构建MVVM架构Android 车载应用开发与分析 （3）- 构建 MVVM 架构(Java版)，通过之前的介绍，也了解到在大多数车载系统应用架构中，一个完整的应用往往会包含三层，分别是
**HMI**
Human Machine Interface，显示UI信息，进行人机交互。
**Service**

`Android`

---

## 📅 2022-01-24

### [&quot;If something is humanly possible, it&#x27;s attainable by you too.&quot; | Revue](/entry/xm27wqh4) 📄
⭐⭐⭐⭐4 🌐 · 2022-01-24

&quot;If something is humanly possible, it&#x27;s attainable by you too.&quot; | Revue
StoicallyTyped Newsletter - Happy Monday! Here is Issue #10! This issue will be a special issue that focuses on being a collection of resources related to the no
Read in Cubox  
Read Original
Happy Monday! Here is Issue #10! This issue will be a special issue that focuses on being a collection of resources ...

`Android` `Newsletter`

---

## 📅 2022-01-19

### [Android滚动组件图片加载优化与滚动速度的精确监听 | Paincker](/entry/z10ujypt) 📄
⭐⭐⭐⭐4 🌐 · 2022-01-19

Android滚动组件图片加载优化与滚动速度的精确监听 | Paincker
背景 在Android应用中，ListView / RecyclerView / ScrollView 滚动时，如果有过多图片加载容易导致卡顿，特别是快速滚动时，bindView中大量图片加载操作，会导致系统频繁分配回收内存，不仅消耗大量CPU和网络流量资源，而且极端情况下还会因为内存来不及回收产生OOM。
Read in Cubox  
Read Original
在Android应用中，ListView / RecyclerView / ScrollView 滚动时，如果有过多图片加载容易导致卡顿，特别是快速滚动时，bindView中大量图片加载操作，会导致系统频繁分配回收内存，不仅消耗大量CPU和网络流量资源，而且极端情况下还会因为内存来不及回收产生OOM。
一种最基...

`Android` `Performance`

---
