# 最佳实践

Best Practices — 29 条活跃资源

### [Running Slice 全栈分析手册](#) 
 | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**Perfetto Running Slice六层诊断框架，从Java到SoC全覆盖**

为Android性能工程师提供的系统化分层框架，用于精确诊断Perfetto中Running片段的CPU消耗位置和原因。涵盖六个层级：Java方法追踪→ART虚拟机→内核调度器→CPU微架构→缓存层级→SoC内存子系统。每个层级有独特工具、指标和故障模式。长Running片段可分解为指令供给问题、数据访问延迟、非最优核心放置、频率调节延迟或算法冗余。
 `perfetto` `running-slice` `cpu` `performance` `android` `trace-analysis`

---
### [OpenClaw 运行报错指南（上篇）](https://x.com/lijiuer92/status/2026639705933328582) 
by @李韭二 (2026-02-27) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**OpenClaw macOS 运行报错排查指南，覆盖 Gateway 全链路**

macOS 上 OpenClaw 运行报错的系统性排查指南。Gateway 是中枢神经，所有消息收发/LLM 调用/工具调度都经过它，挂了=系统瘫痪。覆盖 Gateway 启动失败排查（Node.js 版本、端口占用、launchd 服务注册、JSON 配置）、各类报错的根因分析。适用 macOS Apple Silicon/Intel。
 `openclaw` `troubleshooting` `gateway` `macos` `debug`

---
### [AI时代系统工程师的硬技能升级路线图](#) 
 | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**给系统工程师的AI转型路线图，端侧全栈是最大杠杆点**

面向资深Android系统工程师的技能升级路线图。核心判断：2025-2026年最具杠杆效应的方向是'端侧AI全栈'——将系统底层经验与AI推理优化、On-device ML和AI Agent开发结合。AI技能薪资溢价已达56%，全球AI人才缺口300万。建议投资方向包括：LLM基础能力、Agent开发、端侧推理优化、性能分析与AI结合。原文含具体学习路径和工具推荐。
 `ai-engineer` `system-engineer` `career` `on-device-ai` `skill-upgrade`

---
### [Android adb shell dumpsys meminfo 全面解析指南](#) 
by @Manus AI | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**dumpsys meminfo逐行解析，Android内存分析必备参考**

全面解析adb shell dumpsys meminfo命令的输出格式，详细说明每一栏含义、数据来源、异常判断标准和优化建议。涵盖PSS/USS/VSS/RSS区别、Native/Heap/Stack内存分类、View/Asset/Bitmap内存追踪。帮助开发者和性能分析师精确定位内存问题。
 `android` `meminfo` `memory` `dumpsys` `performance` `debugging`

---
### [Android ARM 平台 Running 耗时分析方法论与工具链报告](#) 
by @Manus AI | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**ARM平台Running耗时分析全套方法论，从方法到指令级**

Android ARM平台上Running耗时分析方法论与工具链的完整报告。定义Running耗时为CPU实际执行时间，区分等待I/O和阻塞时间。涵盖simpleperf、Perfetto、ARM DSU/ETM等工具链，从方法级到指令级的分层分析框架。包含big.LITTLE核心调度、频率DVFS、Cache Miss等底层因素的量化分析方法。
 `android` `arm` `running-time` `cpu` `perfetto` `simpleperf` `performance`

---
### [Android App 帧渲染流程深度解析：从 Vsync 到屏幕](#) 
by @Manus AI | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**从Vsync到屏幕的完整渲染链路解析，Android图形管线全景图**

从Vsync-App信号接收开始，深度解析Android应用帧渲染的完整流程。涵盖Choreographer调度、Input/Animation/Traversals回调、Draw/Measure/Layout流程、RenderThread与GPU协作、BufferQueue流转、SurfaceFlinger合成、直至最终屏幕显示。包含详细的时序图和性能关键路径分析。
 `android` `vsync` `rendering` `frame` `choreographer` `surfaceflinger` `gpu`

---
### [Android 应用性能优化：Vsync 与 Buffer 深度研究报告](#) 
by @Manus AI | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Vsync/Buffer/Fence全链路深度解析，Android图形性能优化理论基石**

深入研究Android应用中Vsync和Buffer相关机制。涵盖Vsync信号产生与分发、Vsync-app/Vsync-sf/Vsync-appsf分类、BufferQueue及BlastBufferQueue工作原理、UI线程与RenderThread协作、app duration与sf duration分析、GPU Fence和HWC Fence同步机制。为Android性能优化提供理论基础和实践指导。
 `android` `vsync` `buffer` `blastbufferqueue` `surfaceflinger` `fence` `rendering`

---
### [Android Native 内存泄漏深度调研报告](#) 
by @Manus AI | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Native内存泄漏全链路排查指南，从原理到工具到实战案例**

深入探讨Android Native内存泄漏问题，涵盖基本原理、检测与分析方法、常用工具（Valgrind、AddressSanitizer、heapprofd等）及库。结合实际案例分析Android内存管理机制和Native层内存泄漏成因，为开发者提供全面的Native内存泄漏解决方案。
 `android` `native` `memory-leak` `valgrind` `asan` `heapprofd`

---
### [2026 年 AI 行业预测汇总，AI 将如何改变世界？](https://mp.weixin.qq.com/s?__biz=MzkxMTQ0ODE3Ng==&mid=2247493113&idx=1&sn=254283e9212ff2c0ce7e2de4e2ca6602&chksm=c03fc269c6c77a0e505370331e97994c8832317cebfe7e6ec343b3b0b5d78f2a540c25a77aa5&mpshare=1&scene=1&srcid=0106AHTBdpsFwLVo3QyBVeGA&sharer_shareinfo=0a29b8c4149f9c32593fbe21f1b8aeb1&sharer_shareinfo_first=bf8657f09d3146487995b33ff6b7e0f8) 
 (2026-01-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，best-practices 领域相关内容**

2026 年 AI 行业预测汇总，AI 将如何改变世界？
汇总自 Gartner、SaaStr、a16z、Every、Gary Marcus 和 Forbes 的 26 年 AI 行业分析
Read in Cubox  
Read Original
?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FPEeV2JtM1K5wMHX5fRAvuF6vwsbibiaMNMV6TWp50WP2bwPTzo9ODzTwe18moLv2Qu4exjiaBRAQibCSqZRx0NRYRw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)
**最近看到各大投资机构在 2026 年 AI 行业的预测，我做了一个汇总，把相同点进行整理，不同点里有意思的观点做了摘要。**
 `Claude` `Agent`

---
### [AI 也能"看懂"图片： 移动端相册 AI 搜图的奥秘PicQuery 通过创新的多模态搜索技术，为移动设备上的图片检索 - 掘金](https://juejin.cn/post/7467859145792405531) 
 (2025-02-09) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，best-practices 领域相关内容**

AI 也能"看懂"图片： 移动端相册 AI 搜图的奥秘PicQuery 通过创新的多模态搜索技术，为移动设备上的图片检索 - 掘金
PicQuery 通过创新的多模态搜索技术，为移动设备上的图片检索提供了一个高效、智能的解决方案。是一个非常值得学习，把玩的好项目。
Read in Cubox  
Read Original
其实大概三四个月前就想写一篇文章来介绍移动端 AI 搜图的一些进展，不过由于本人的精力有限和一些其他的原因，没有及时更新。所以也就拖更很久，好在春节有些时间可以把之前的一些知识总结，更好的展现给大家。  
相信用 Android 手机的同学多少都有一些感觉，Android 手机上的相册都多了一个搜图的功能，例如小米手机或是 Oppo 手机都上线了类似的功能，输入文字可以获得相关的图片。下面展示一下小米相册里面的搜图功能：
?ima...
 `OpenAI` `Android` `Multimodal`

---
### [AI 时代下的工程领导力：如何打造高效团队 - 来自谷歌工程负责人、Chrome 开发者的宝贵经验分享](https://mp.weixin.qq.com/s/W56P_HMprc6WVEiCdR8OKw) 
 (2025-03-26) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，best-practices 领域相关内容**

AI 时代下的工程领导力：如何打造高效团队 - 来自谷歌工程负责人、Chrome 开发者的宝贵经验分享
AI 是个好帮手，但不能全靠它，团队领导者得搞清楚“更好”到底是啥意思，然后带着团队更快地往那儿走，团队成员也是如此。
Read in Cubox  
Read Original
今天偶然读到 Chrome 开发者、Google 工程负责人、著名技术书籍作者 -Addy Osmani 的一篇文章「Leading Effective Engineering Teams in the Age of GenAI」，讲的特别好，对于产品和研发方向如何变得高效，不管你是团队领导者、还是团队成员，都很有价值，分享给朋友们，可以先看我的阅读笔记，针对自己感兴趣的部门再阅读原文（推荐阅读，作者信息和文章链接放在文末）
?imageUrl=https%3A%2F%2...
 `AI Safety`

---
### [AI狂飙的时代，人还有价值吗？](https://mp.weixin.qq.com/s/7H1FrwbQvsh0HD9z90L0wg) 
 (2023-03-28) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，best-practices 领域相关内容**

Read in Cubox  
Read Original
最近两个月，受到香港中文大学卓越传媒人驻校计划的邀请，我在香港进行了为期八周的访学，并为新闻学院的学生们开设了一个工作坊，主题是关于"如何提问"。就在我们上课的几周时间里，ChatGPT以迅雷不及掩耳的速度进入了大众的视野。我在课上与同学们进行了讨论。有人说，在GPT的时代，会提问可能比会回答更加重要。有人欣喜，认为GPT将大大提高人类工作效率，减少无意义的重复劳动；也有人担忧，认为GPT可能会带来大规模失业，甚至动摇社会的基本结构。
比尔·盖茨称赞，当前这场由ChatGPT衍生开来的人工智能革命是他所见到的自1980年以来最具革命性的技术进步。具体来说，GPT的革命性到底体现在什么地方？当前关于人工智能的讨论有些怎样的误区？它可能会带来什么影响？有什么是它能做的、又有什么是它永远也做不到的...
 `ChatGPT`

---
### [AI辅助下的性能逆向分析](https://zhuanlan.zhihu.com/p/1995678473558176184?share_code=3ev51WrgxnxE&utm_psn=1998177044245271161) 
 (2026-01-23) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，best-practices 领域相关内容**

我在知乎发现了一篇值得思考的文章，一起来看看吧。
Read in Cubox  
Read Original
在性能优化领域，**竞品分析**是一个永恒的话题。然而，现有的分析手段往往存在较大的局限性：
• **指标维度浅层化** ：大多局限于帧率（FPS）、内存占用、CPU 频率及利用率、线程统计等硬件或系统层面的指标。虽然可以通过截帧分析渲染管线，但对于 **CPU 端的具体开销**（如 UI 逻辑、战斗系统、渲染提交等模块的具体耗时）难以进一步拆解。
• **技术壁垒**：在缺乏源代码和符号表的情况下，往往难以洞察竞品底层的具体技术实现。
 `Android` `Performance`

---
### [Airbnb’s Page Performance Score on Android | by Luping Lin | The Airbnb Tech Blog | Dec, 2021 | Medium](https://medium.com/airbnb-engineering/airbnbs-page-performance-score-on-android-f9fd5e733e) 
 | ⭐⭐⭐⭐ 4/5 | 🌐

**Android × AI 交叉领域收藏**

Airbnb’s Page Performance Score on Android | by Luping Lin | The Airbnb Tech Blog | Dec, 2021 | Medium
Airbnb’s home grown Page Performance Score (PPS) is designed to capture the rich, complex realities of performance by collecting a multitude of user-centric performance metrics and formulating them…
Read in Cubox  
Read Original
?imageUrl=https%3A%2F%2Fmiro.medium.com%2Ffit%2F...
 `Android`

---
### [American Idle — Remains of the Day](https://www.eugenewei.com/blog/2021/2/15/american-idle) 
 (2023-07-11) | ⭐⭐⭐⭐ 4/5 | 🌐

**Cubox 收藏文章，best-practices 领域相关内容**

American Idle — Remains of the Day
Read in Cubox  
Read Original
I promised one final piece on TikTok, focused primarily on the network effects of creativity. And this is that, in part. But it discusses a bunch of other topics, some only tangentially related to TikTok.
All the points I wanted to cover seem hyperlinked in a sprawling loose tangle. This could easily have been sev...


---
### [Android 车载应用开发与分析 （4）- 编写基于AIDL 的 SDK - 掘金](https://juejin.cn/post/7083140299916050468) 
 (2022-04-21) | ⭐⭐⭐⭐ 4/5 | 🌐

**Android × AI 交叉领域收藏**

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
### [Android11+ AIDL：专为提升应用性能而生！](https://mp.weixin.qq.com/s?__biz=MzU2NTI3NDI5MQ==&mid=2247485515&idx=1&sn=518a69ed57f50e2a6675a8bc0410df2d&chksm=fcbf7b97cbc8f2810e7cbb013767378563937226c743baca48d671b434fc55d195ea9948b28a&mpshare=1&scene=1&srcid=1227pxgVglGnado7UkDIzguc&sharer_shareinfo=da081d1cd009b4bc161160a43b2c28e9&sharer_shareinfo_first=b45e7a2ede5c265c0ade4a6ccf27bd06) 
 (2023-12-27) | ⭐⭐⭐⭐ 4/5 | 🌐

**Android × AI 交叉领域收藏**

Android11+ AIDL：专为提升应用性能而生！
Android新版本AIDL性能再提升化！
Read in Cubox  
Read Original
**点击下方👇关注****Android系统攻城狮**
每日充电：OS+MultiMedia学习之旅
 `Android` `Performance`

---
### [Android×鸿蒙×AI 技术刊#第12期：Android 16新特性、Compose与Flutter对比、ART机制揭秘](https://mp.weixin.qq.com/s?__biz=MzAxMTI4MTkwNQ==&mid=2650855054&idx=1&sn=f94e827e2edbcf601307e0af1a02daf8&chksm=81487e4a5b6eec8ab351548a8e639839480b7a15077f5d7d3bc7bd3ba2038fef12baf2f426b7&mpshare=1&scene=1&srcid=0623wmsG2IWAIhURcGT5AL7j&sharer_shareinfo=d36fb92e8ce207ed7f0596daf77fc0d8&sharer_shareinfo_first=d36fb92e8ce207ed7f0596daf77fc0d8) 
 (2025-06-23) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Android × AI 交叉领域收藏**

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
### [Android中AIDL和HIDL的区别，Google为什么更推荐AIDL？](https://mp.weixin.qq.com/s?__biz=Mzg5OTMwOTQ3MQ==&mid=2247484134&idx=1&sn=6db5ce7eaabef40dc5404faa160c1506&chksm=c19544c4be5953b5ca97df8e15d4c129f8dbf4b7784d166286fba2707d5a67c36771dc84799e&mpshare=1&scene=1&srcid=0204XY7LY08hRUEx9L00mj8e&sharer_shareinfo=06b8d9404f5eab0b11011016f8206341&sharer_shareinfo_first=06b8d9404f5eab0b11011016f8206341) 
 (2025-02-04) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Android × AI 交叉领域收藏**

Android中AIDL和HIDL的区别，Google为什么更推荐AIDL？
Read in Cubox  
Read Original
在Android中，AIDL（Android Interface Definition Language） 和 HIDL（HAL Interface Definition Language） 是两种用于定义跨进程通信接口的语言。AIDL 是 Android 系统最早支持的 IPC（进程间通信）机制，而 HIDL 是从 Android 8.0 开始引入，用于 HAL（Hardware Abstraction Layer）模块的接口定义。
随着 Android 的发展，Google 决定从 Android 11 开始将新的 HAL 统
一使用 AIDL 接口，而逐步放弃 HIDL。这种转变背后的原因涉及技术复杂度、性能、开发效率和生态统一性等多个方面。
 `Android` `Performance`

---
### [Android滚动组件图片加载优化与滚动速度的精确监听 | Paincker](https://www.paincker.com/android-scroll-velocity/#/) 
 (2022-01-19) | ⭐⭐⭐⭐ 4/5 | 🌐

**Android × AI 交叉领域收藏**

Android滚动组件图片加载优化与滚动速度的精确监听 | Paincker
背景 在Android应用中，ListView / RecyclerView / ScrollView 滚动时，如果有过多图片加载容易导致卡顿，特别是快速滚动时，bindView中大量图片加载操作，会导致系统频繁分配回收内存，不仅消耗大量CPU和网络流量资源，而且极端情况下还会因为内存来不及回收产生OOM。
Read in Cubox  
Read Original
在Android应用中，ListView / RecyclerView / ScrollView 滚动时，如果有过多图片加载容易导致卡顿，特别是快速滚动时，bindView中大量图片加载操作，会导致系统频繁分配回收内存，不仅消耗大量CPU和网络流量资源，而且极端情况下还会因为内存来不及回收产生OOM。
一种最基...
 `Android` `Performance`

---
### [Anthropic全网追杀的人，可能是我……](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498537&idx=1&sn=23cafdfedc8297dfa05d46a5bce8db11&chksm=e83b872acc893f6ffb867f3fd3bd14634ae32630344f698f941bfa2f5b65d9f7755e82b8bd9c&mpshare=1&scene=1&srcid=0815evfjgbXaGDetZApIQOyX&sharer_shareinfo=fd637b036a75822befde463b74963297&sharer_shareinfo_first=fd637b036a75822befde463b74963297) 
 (2025-08-15) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Anthropic 公司动态与分析收藏**

Anthropic全网追杀的人，可能是我……
Anthropic官方说，有一个用户在一个月内消耗了价值数万美金的的token，从而决定限速。这个用户，好像，是我本人……
Read in Cubox  
Read Original
上个月，Anthropic官方发布了信息，有一个用户，只花了$200美元订阅套餐，却在一个月内消耗了数万美金的(tens of thousands)的token。从而决定对所有人进行限速......
全世界的程序员都在好奇，这位每个月花数万美金的老哥是谁？
 `Claude` `Anthropic`

---
### [Articels/腹背受敌的中国经济（3 万字长文）.md at main · foreveryh/Articels · GitHub](https://github.com/foreveryh/Articels/blob/main/%E8%85%B9%E8%83%8C%E5%8F%97%E6%95%8C%E7%9A%84%E4%B8%AD%E5%9B%BD%E7%BB%8F%E6%B5%8E%EF%BC%883%20%E4%B8%87%E5%AD%97%E9%95%BF%E6%96%87%EF%BC%89.md) 
 (2024-07-07) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，best-practices 领域相关内容**

Articels/腹背受敌的中国经济（3 万字长文）.md at main · foreveryh/Articels · GitHub
文章转载分享. Contribute to foreveryh/Articels development by creating an account on GitHub.
Read in Cubox  
Read Original
繁华渐逝：腹背受敌的中国经济（3 万字长文）
全文约 3 万字，撰写花了我 14 个月。阅读需要 60 分钟。如果完全读懂，能受益 30 年。


---
### [Avoid Mini-frameworks - laike9m's blog](https://laike9m.com/blog/avoid-mini-frameworks,171/) 
 (2025-12-26) | ⭐⭐⭐⭐ 4/5 | 🌐

**Cubox 收藏文章，best-practices 领域相关内容**

Avoid Mini-frameworks - laike9m's blog
Read in Cubox  
Read Original
DEC 24TH, 2025
What is mini-framework?
My Story
Why mini-frameworks are bad?
So, What Should You Do Instead?
*See Hacker News discussion*
I work in Google Ads infrastructure in the past four years. Over time, I've seen one pattern came along again and again, causing endless pain for developers, that is, creating mini-frameworks.


---
### [微信小程序技术调研报告](#) 
by @Manus AI | ⭐⭐⭐ 3/5 | 🇨🇳

**微信小程序7维度技术调研：从架构到启动到滑动的性能全分析**

微信小程序技术的全面调研报告，涵盖7个维度：历史与背景、重要性分析、技术实现架构、启动与滑动性能优化、优化目标与挑战、优化策略、小程序vs小游戏对比。深入分析了微信小程序的双线程架构、渲染管线、启动优化策略、滑动性能瓶颈及解决方案。对理解小程序性能优化有较高参考价值。
 `wechat` `mini-program` `android` `performance` `startup` `scrolling` `optimization`

---
### [AI is about to completely change how you use compu...](https://www.gatesnotes.com/AI-agents) 
 (2023-12-14) | ⭐⭐⭐ 3/5 | 🌐

**Cubox 收藏文章，best-practices 领域相关内容**

AI is about to completely change how you use compu...
In 5 years, agents will be able to give health care advice, tutor students, do your shopping, help workers be far more productive, and much more
Read in Cubox  
Read Original
I still love software as much today as I did when Paul Allen and I started Microsoft. But---even though it has improved a lot in the decades since then...
 `Agent`

---
### [How To Remember Everything You Read With AI - Dan Koe](https://thedankoe.com/letters/how-to-remember-everything-you-read-with-ai/) 
 (2025-04-16) | ⭐⭐⭐ 3/5 | 🌐

**反对 AI 摘要替代阅读，提倡用 AI 深化理解的阅读方法论**

Dan Koe 探讨了如何用 AI 深化阅读理解而非替代阅读。核心观点：阅读的价值不在于获取信息（AI 更擅长），而在于改变思维方式。提出两层阅读法：Consumption（摄入）和 Digestion（消化）。具体 AI 用法：1) 用 AI 作为阅读伙伴，在阅读前生成问题框架；2) 阅读后用 AI 撰写结构化摘要和个人反思；3) 让 AI 帮助发现认知盲区和限制性信念；4) 将笔记转化为行动方案。强调 AI 应用于加深理解而非替代思考。
 `reading` `knowledge-management` `AI-learning` `personal-growth` `Dan-Koe`

---
### [Rust写aosp13的AIDL系统级服务](https://mp.weixin.qq.com/s?__biz=Mzk0MjQwMDYyOQ==&mid=2247483679&idx=1&sn=307d2b53c501bcb300c6bee355ffc1e0) 
 (2023-03-13) | ⭐⭐⭐ 3/5 | 🇨🇳

**AOSP 13 Rust AIDL 系统服务实战教程，代码完整可直接复用**

在 AOSP 13 中用 Rust 实现 AIDL 系统级服务的完整教程。包括 AIDL 接口定义、Android.bp 配置（Rust backend）、服务端/客户端实现、编译运行。Google 已建议放弃 HIDL 统一使用 AIDL。
 `Rust` `AOSP` `AIDL` `Android` `系统服务` `Binder`

---
### [我用Coze来掘金 | AI Agent 创意征文大赛来啦！ - 掘金](https://juejin.cn/post/7330295644281962530) 
 (2024-02-01) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 我用Coze来掘金 | AI Agent 创意征文大赛来啦！ - 掘金**

2月1日，扣子国内版已经正式上线啦~赶快来体验一下吧！将使用 扣子 搭建 AI bot 的实践心得和思路分享到掘金，更有 iPhone15、雷蛇机械键盘、京东卡等好礼待你领取！🎁


---
### [解读 Anthropic 博文：适用于长期运行 Agents 的有效框架](https://mp.weixin.qq.com/s/UgTbCsVMcG8N9VC3VRZbMg) 
 (2025-12-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 解读 Anthropic 博文：适用于长期运行 Agents 的有效框架**

> 基于 Anthropic 的 "Effective harnesses for long-running agents" 最佳实践


---