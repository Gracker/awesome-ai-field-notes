# ⚡ 基础设施

推理部署 / RAG / 微调 / 评测 / 多模态 — 共 **57** 条活跃资源

## 📅 昨天

### [搞懂缓存机制，从Gemma4到Claude Code省80%Token](/entry/otjpnj3j) 📄
@MinLiBuilds · ⭐⭐⭐⭐⭐5 🇨🇳 · 昨天

从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。

`kv-cache` `claude-code` `token-optimization` `transformer` `caching`

---

### [State of AI | OpenRouter](https://openrouter.ai/state-of-ai)
@OpenRouter + a16z · ⭐⭐⭐⭐⭐5 🌐 · 昨天

OpenRouter 联合 a16z 的 100 万亿 token LLM 使用分析。核心发现：开源模型采用率提升、创意角色扮演和编程是最热门任务、Agent 推理模式兴起、&#x27;Glass Slipper&#x27;留存效应。含开源 vs 闭源、地理分布、成本动态等多维度数据。

`OpenRouter` `a16z` `LLM` `100T-tokens` `agentic`

---

### [用 LLM + Obsidian 构建个人知识库：基于 Karpathy 的&quot;LLM Knowledge Bases&quot;工作流](https://x.com/yanhua1010/status/2039966047378583815)
@yanhua1010 · ⭐⭐⭐⭐4 🇨🇳 · 昨天

基于 Karpathy 的 LLM Knowledge Bases 工作流，将知识库管理类比为 CI/CD：原始资料→编译产物→运行时输出三层分离。用 Obsidian + Claude Code 实现三层目录结构：raw/（摄取）、wiki/（编译成品）、平台目录（发布）。三个摄取入口（Web Clipper、Podwise、手动剪藏），编译环节包含逐篇摘要、概念抽取、索引更新。强调增量编译和质量保障。

`obsidian` `llm` `knowledge-base` `karpathy` `compile`

---

### [Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA](https://x.com/TrevinPeterson/status/2027404303749546459)
@TrevinPeterson · ⭐⭐⭐⭐4 🌐 · 昨天

24+ 小时调试后，在两台 Mac Studio M4 Max 上通过 Exo + Thunderbolt 5 RDMA 实现了 Qwen3.5-122B-A10B 的完整池化运行。持续吞吐约 52 tok/s，并发 c=2 稳定（p95 约 10.37 秒）。提供了完整的 Day-0 实操指南，包含精确命令与失败检查关卡。

`qwen` `mac-studio` `rdma` `exo` `local-inference`

---

### [LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595)
@Andrej Karpathy · ⭐⭐⭐⭐4 🌐 · 昨天

Karpathy 分享他用 LLM 构建个人知识库的工作流：raw/ 目录存放原始文档，LLM 增量&quot;编译&quot;成 .md wiki（含摘要、反向链接、概念分类文章）；用 Obsidian 作为 IDE 前端查看原始数据、编译产物和可视化；wiki 达到约 100 篇文章/40 万字后，可以直接向 LLM agent 提问复杂问题。关键发现：不需要 fancy RAG，LLM 自己会维护索引文件和文档摘要。输出形式包括 Markdown 文件、幻灯片（Marp 格式）、matplotlib 图像。还会用 LLM 做 wiki 健康检查（不一致数据、缺失数据、新文章候选）。

`LLM` `知识库` `Obsidian` `Markdown` `RAG`

---

### [MeKi —— 用 ROM 扩展端侧 LLM，而不是继续硬堆计算](#)
@允许动态投影、归一化、非线性映射这些复杂结构存在，以保证模型能学到足够好的知识表达；部署前，再把这些东西折叠到静态查表结构里。于是： · ⭐⭐⭐⭐4 🇨🇳 · 昨天

**论文**：MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling  
**精读日期**：2026-03-09  
**定位**：面向 Android / 端侧 AI / 性能优化 / SmartPerfetto 方向的深度解读

---

## 一、论文要解决的问题
### 1.1 真正的问题不是“模型不够大”，而是“手机端的资源结构不匹配”
在服务器上，做大模型最直接的办法就是：
- 增加参数量；
- 增加推理时计算；
- 用更大的显存和更强的 GPU 接住它。

但到了手机端，这套思路就开始失效：
…

`perfetto` `on-device` `agent` `android` `llm`

---

### [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise)
@Anthropic Engineering · ⭐⭐⭐⭐4 🌐 · 昨天

Anthropic工程团队量化了Agent编程评测中的基础设施噪声问题。发现即使在相同环境下重复运行相同的Agent评测，结果也会因网络延迟、API负载、容器调度等因素产生显著波动。这对SWE-Bench、Terminal-Bench等评测的可靠性提出了挑战。提出了减少噪声的方法论建议。

`anthropic` `evaluation` `agentic-coding` `benchmarks` `noise`

---

### [0x1 Underlying LLMs](https://juejin.cn/post/7312243176834809908)
⭐⭐⭐⭐4 🇨🇳 · 昨天

Read in Cubox  
Read Original
LLM (Large Language Models) 的风头一时无两，席卷万千行业。业内不乏有关于 LLM 的研究和讨论，但鲜有立足终端的视角。团队上半年曾有过对 GPT 进终端的分析，但 LLM 日新月异，旧分析已经不完全跟得上变化了。适逢年底规划季，尝试重新梳理 LLM 的现状，预判未来变化的趋势，希望能为迷茫的同仁提供思考的角度，也希望获得战斗在一线的友军的指点。
求砖 \&amp; 免砖申明：
不包含 LLM 入门介绍，够时间可以报吴恩达的免费课程和 NVIDIA 与 LlamaIndex 合力出品的；不够时间也有 Andrej Karpathy 的 一小时入门；
非算法出身，如有错漏之处，恳请指正；力争能让 RD、PM、DA 们都能看懂，如果不明处，欢迎讨论；
终端 LLM 应用有一定不...

`LLM` `RAG` `Inference` `LLaMA` `Multimodal`

---

### [2023: The Year of AI](https://t.co/3yCKuXTIKp)
⭐⭐⭐⭐4 🌐 · 昨天

Explore the significant AI advancements, impactful partnerships, and legal debates that defined 2023.
Read in Cubox  
Read Original
AI has undoubtedly made waves in 2023 and here we spotlight the most significant stories of the year poised to shape the future of this groundbreaking industry:
*Correction: In the original blog post published on December 22, 2023, the title &quot;AI Re...

`ChatGPT` `LLM` `Midjourney`

---

### [2026 AI First 系列（三）：在被替代之前变得有价值——新经济下的生存法则](https://youmind.com/s/ZncQVsVULbYTWU)
⭐⭐⭐⭐4 🇨🇳 · 昨天

2026 AI First 系列（三）：在被替代之前变得有价值——新经济下的生存法则
**第一件事**：你在做reinforcement learning from human feedback（RLHF）。每次你
Read in Cubox  
Read Original
**第一件事**：你在做reinforcement learning from human feedback（RLHF）。每次你修正AI的输出，每次你选择一个答案而不是另一个，你都在教它什么是好的、什么是不好的。
**第二件事**：你在数字化你的直觉。那些你&quot;凭感觉&quot;做出的判断，那些你&quot;基于经验&quot;的决策，正在被转化为数据点。AI在学习你的思维模式。

---

### [70款ChatGPT插件评测：惊艳的开发过程与宏大的商业化愿景 - 知乎](https://zhuanlan.zhihu.com/p/629337429?utm_id=0&utm_source=wechat_session&utm_medium=social&s_r=0)
⭐⭐⭐⭐4 🇨🇳 · 昨天

70款ChatGPT插件评测：惊艳的开发过程与宏大的商业化愿景 - 知乎
TL;DR: 我们对ChatGPT的插件商店中总共70款插件进行了评测。区别于Chrome，AppStore等平台的代码开发范式，开发者仅使用自然语言就可以开发ChatGPT插件，并由GPT模型自行决定在使用过程中是否调用插件。约八成插件…
Read in Cubox  
Read Original
Shimmer: Nutrition Coach
**TL;DR:** 我们对ChatGPT的插件商店中总共70款插件进行了评测。区别于Chrome，AppStore等平台的代码开发范式，开发者仅使用自然语言就可以开发ChatGPT插件，并由GPT模型自行决定在使用过程中是否调用插件。约八成插件集中于购物、餐饮、旅行、住房和求职场景，其余分布在教育、财经咨讯、内容社区和编程技术场景...

`ChatGPT` `OpenAI` `Prompt Engineering` `Benchmark`

---

### [AI 代理可观测性 - 演变标准与最佳实践](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247553129&idx=2&sn=b096969e9b11351ee311f13f4cb15c1b&chksm=ed4dcaeea8eed4db84fd7e26c9216b026b402f2de5aa869c09b82f22cc5e1666c3803f56a84f&mpshare=1&scene=1&srcid=0311AblXeZcZnhw5hMg3o7xI&sharer_shareinfo=38ca43ce0163ec0a3d17cf759565d2af&sharer_shareinfo_first=65f12cd27132058e786435d42b931d6c)
@Guangya Liu (IBM), Sujay Solomon (Google) · ⭐⭐⭐⭐4 🇨🇳 · 昨天

AI 代理可观测性 - 演变标准与最佳实践
AI 代理将在 2025 年成为人工智能的下一个重大飞跃，AI 代理的可观测性变得尤为重要，特别是在将这些代理扩展以满足企业需求时。没有适当的监控、追踪和日志记录机制，诊断问题、提高效率和确保 AI 代理驱动应用的可靠性将面临挑战。
Read in Cubox  
Read Original
作者：Guangya Liu (IBM), Sujay Solomon (Google)
AI 代理将在 2025 年成为人工智能的下一个重大飞跃。从自主工作流到智能决策，AI 代理将为各行业的众多应用提供动力。然而，随着这一演变，AI 代理的可观测性变得尤为重要，特别是在将这些代理扩展以满足企业需求时。没有适当的监控、追踪和日志记录机制，诊断问题、提高效率和确保 AI 代理驱动应用的可靠性将面临挑战。

`Anthropic` `LLM` `Agent` `Inference`

---

### [AI 技术的停滞，是革命的开始 – 虹线](https://1q43.blog/post/10727/)
⭐⭐⭐⭐4 🇨🇳 · 昨天

Read in Cubox  
Read Original
1866 年，西门子的一位工程师发明了人类第一台直流发电机。
40 年后，通用电气在 1906 年开始量产真正让电灯普及的第一代白炽灯泡。
在这两者之间的半个世纪里，人类世界依然黑暗，电气的技术革命好像没有发生。
但，这只是因为我们身处后世，才能如此轻描淡写地将这 40 年一笔带过。对于当时的人们来说，电气技术的发展，是他们眼皮底下一天天展开的：第一条电报线路的铺设，第一个电话的接通，第一辆电车的开动，每一次技术的进步，都在真切地改变着他们的生活，只是它没有快到让当时的每个人都在一个时间点集体惊呼&quot;啊，电气革命终于来了！&quot;

`ChatGPT` `OpenAI` `Fine-tuning` `Inference` `Speech`

---

### [AI 是一块“五层蛋糕”](https://blogs.nvidia.cn/blog/ai-5-layer-cake/)
⭐⭐⭐⭐4 🇨🇳 · 昨天

Read in Cubox  
Read Original
**2026 年 3 月 10 日 作者 黄仁勋**
AI 是塑造当今世界的强大力量之一。它并非仅仅是一款巧妙的应用程序，也不是单一的模型，而是如同电力和互联网一样必不可少的基础设施。
AI 依托真实的硬件、能源和经济体系运行。它可以将原材料大规模地转化为智能。每家公司都将应用 AI， 每个国家/地区都将发展 AI。
要理解 AI 为何以这种方式发展，我们需要从基本原理进行推理，并了解计算领域发生了哪些根本性变化。

`Inference`

---

### [AIGC图像生成的原理综述与落地畅想](https://mp.weixin.qq.com/s?__biz=MzAxNDEwNjk5OQ==&mid=2650503986&idx=1&sn=f92c8986e13e30184cb43e6f76f985d2&chksm=8397b32ab4e03a3c9f6e03e8b03aed5db17f4834d0435c6ac40311ff8d882531682211c5ad3d&mpshare=1&scene=1&srcid=0322KCccdeScAxL5DF5t0BvM&sharer_sharetime=1679479393566&sharer_shareid=b7cc12eb3054f40795517e846030e3c8)
⭐⭐⭐⭐4 🇨🇳 · 昨天

基于Stable Diffusion扩散模型的综述
Read in Cubox  
Read Original
AIGC，这个当前的现象级词语。本文尝试从文生图的发展、对其当前主流的 Stable Diffusion 做一个综述。以下为实验按要求生成的不同场景、风格控制下的生成作品。
GAN 系列算法开启了图片生成的新起点。GAN的主要灵感来源于博弈论中零和博弈的思想，通过生成网络G（Generator）和判别网络D（Discriminator）不断博弈，进而使G学习到数据的分布。
1.
   G是一个生成式的网络，它接收一个随机的噪声z（随机数），通过这个噪声生成图像。
2.
   D是一个判别网络，判别一张图片是不是&quot;真实的&quot;。它的输入参数是x，x代表一张图片，输出D（x）代表x为真实图片的概率，如果为1，就代表100%是真实的图片。

`AIGC` `Stable Diffusion` `Embedding` `Transformer` `Diffusion`

---

### [Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务](https://mp.weixin.qq.com/s?__biz=MzU3NDQ3MDg2MA==&mid=2247484117&idx=1&sn=761c1843850dc13fba1a9ed4f912292c&chksm=fc67b8d086be885fa36535bb6597eb3e56e04234c66ea06f9e387c62c727918252dae421197f&mpshare=1&scene=1&srcid=102051f2hEfpd15fJFVYIXe1&sharer_shareinfo=3b9de612d2a8b9241d53cfcc940ed665&sharer_shareinfo_first=3b9de612d2a8b9241d53cfcc940ed665)
⭐⭐⭐⭐4 🇨🇳 · 昨天

Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务
Anthropic 揭秘让 AI 更靠谱的「上下文工程」
Read in Cubox  
Read Original
&gt; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
你有没有过这样的体验？跟 AI 聊得久了，它突然 &quot;失忆&quot;------ 前面提过的关键信息没了下文，甚至答非所问；让它处理复杂任务，比如分析大数据库、写长代码，它越往后越混乱...... 其实不是 AI &quot;不认真&quot;，而是它的 &quot;注意力&quot; 有限。

`Anthropic` `LLM` `Agent` `Inference` `Transformer`

---

### [ChatGPT 算法原理](https://zhuanlan.zhihu.com/p/605835778?utm_medium=social&utm_oi=27871238160384&utm_psn=1608822750822518785&utm_source=ZHShareTargetIDMore)
⭐⭐⭐⭐4 🇨🇳 · 昨天

每一代GPT模型的参数量都爆炸式增长，堪称“越大越好”。2019年2月发布的GPT-2参数量为15亿，而2020年5月的GPT-3，参数量达到了1750亿。 还是有很多读者对于ChatGPT充满期待（幻想？梦想），今天给大家分享技术层… 每一代GPT模型的参数量都爆炸式增长，堪称&quot;越大越好&quot;。2019年2月发布的GPT-2参数量为15亿，而2020年5月的GPT-3，参数量达到了1750亿。 还是有很多读者对于ChatGPT充满期待（幻想？梦想），今天给大家分享技术层面的拆解，读完之后是否是会理性一点呢？enjoy～ 文末推荐几篇直接采访ChatGPT创始人视角的文章，共赏enjoy～ 去年1...

`transformer` `fine-tuning` `[]` `gpt-4` `openai`

---

### [ChatGPT背后的经济账](https://mp.weixin.qq.com/s?__biz=MzU5ODY2MTk3Nw==&mid=2247490676&idx=1&sn=f3f98a7b3b0670e4274dd681dcb44430&chksm=fe419242c9361b5425dd7205f30ceba365dbb05ee0a6f6d8a676357b1295fc341c7371a33860&mpshare=1&scene=1&srcid=0207AYBBvxIgd1vR12H4ipEz&sharer_sharetime=1675754807931&sharer_shareid=b7cc12eb3054f40795517e846030e3c8)
⭐⭐⭐⭐4 🇨🇳 · 昨天

ChatGPT能否取代Google、百度这样的传统搜索引擎？为什么中国不能很快做出ChatGPT？当前，对这些问题的探讨大多囿于大型语言模型（LLM）的技术可行性，忽略或者非常粗糙地估计了实现这些目标背后的经济成本，从而造成对LLM的开发和应用偏离实际的误判。 本文作者从经济学切入，详细推导了类ChatGPT模型搜索的成本、训练GPT-3以及绘制LLM成本轨迹的通用框架，为探讨LLM成本结构和其未来发展提供了可贵的参考视角。 * LLM驱动的搜索已经在经济上可行 ：粗略估计，在现有搜索成本结构的基础上，高性能LLM驱动搜索的成本约占当下预估广告收入/查询的15%。 * 但经济可行并不意味着经济...

`llm` `[]` `prompt` `inference` `chatgpt`

---

### [ChatGPT背后的语言模型简史](https://www.bmpi.dev/dev/deep-learning/nlp-language-models/)
⭐⭐⭐⭐4 🇨🇳 · 昨天

ChatGPT的火爆出圈，让大家对NLP语言模型的发展历程产生了浓厚的兴趣。本文将从深度学习在NLP领域的发展历程，到大语言模型的发展历程，再到大语言模型的未来展望，带你一起了解NLP语言模型的发展历史。 本文处于初稿状态，可能存在很多错误，如果你有不同的看法，欢迎不吝赐教，先行感谢！ ChatGPT的火爆出圈，让大家对自然语言处理（Natural Language Processing）语言模型的发展历程产生了浓厚的兴趣。本文将从深度学习在NLP领域的发展历程，到大语言模型的发展历程，再到大语言模型的未来展望，带你一起了解NLP语言模型的发展历史。 想必很多人对ChatGPT涌现出的多领域能...

`[]` `chatgpt`

---

### [GPT-4 重磅发布，有哪些升级和变化？](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649777032&idx=1&sn=703080786e6ce1033dcf237163980010&chksm=beccf0f389bb79e5305da9f2d70830b899516280cc68956c252448d00ce17fd9243bdee6dec7&mpshare=1&scene=1&srcid=0316kvEpO62cz6unedKKfTaC&sharer_sharetime=1678932028379&sharer_shareid=b7cc12eb3054f40795517e846030e3c8)
@qizailiu，腾讯 IEG 算法研究员 · ⭐⭐⭐⭐4 🇨🇳 · 昨天

# GPT-4 重磅发布，有哪些升级和变化？ 作者：qizailiu，腾讯 IEG 算法研究员 &gt; 昨天 OpenAI 发布最新里程碑 AI 语言模型 GPT-4，GPT-4 是一个大型多模态模型（接受图像和文本输入，输出为文本），目前虽然在许多现实世界场景中的能力不如人类，但在各种专业和学术基准上表现出人类水平。 本文主要参考 OpenAI 关于 GPT4 的官方 Blog，目前各公众号关于 GPT4 的内容基本来自官方 Blog、技术报告和官方视频内容。相关内容传送门： 官方 ChatGPT Plus 体验地址：&lt;https://chat.openai.com/auth/login?nex...

`[]` `prompt` `gpt-4` `openai` `chatgpt`

---

### [GPT-4o：OpenAI 发布最强人机交互模型](https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247488719&idx=1&sn=6cd1de66286c6c2d450dde995e542b4a&chksm=e8dd553bdfaadc2d0771fbfb6e676774bdfeccbf4f2d0dded73ccaba49bc26dccb2614304186&mpshare=1&scene=1&srcid=0514msC8tfZenjjKIc24Fyfn&sharer_shareinfo=997aa8739f3d28dbe9bde441d73ff9a2&sharer_shareinfo_first=997aa8739f3d28dbe9bde441d73ff9a2)
⭐⭐⭐⭐4 🇨🇳 · 昨天

# GPT-4o：OpenAI 发布最强人机交互模型 ChatGPT 免费版持续升级中，模型更强，交互更流畅... 早在 5 月 11 日，Sam 就在推文中表示：OpenAI 并没有推出 GPT-5，或搜索引擎，但团队一直在努力研发一些认为大家会喜欢的新东西（感觉就像是魔法一样）！ ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F90Kxd0FAJJeDZbFzQkrjxIfcnRxziahTJZPicyxQOgbg5C88suDBEfiaZg2mjE226NZDIEOxWDr27kHz7fMvNEkSA%2F640%3Fwx_fmt%...

`[]` `gpt-4` `gpt-4o` `openai` `chatgpt`

---

### [GPU到底是如何工作的？这篇AI Infra入门全部告诉你](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649794406&idx=1&sn=a82bddefd373ede0e74b469c424c3ea8&chksm=bf32955ebe2ab04b75d0aa853f7a99280f643248ea9b612833cfcc6bee8ef622a37e4757c15b&mpshare=1&scene=1&srcid=0708WHfDSRgLGj8rXTzQcwtz&sharer_shareinfo=25bd203985012df350edcae33fa026fd&sharer_shareinfo_first=25bd203985012df350edcae33fa026fd)
@binnnliu · ⭐⭐⭐⭐4 🇨🇳 · 昨天

# GPU到底是如何工作的？这篇AI Infra入门全部告诉你 ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2Fj3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg) &gt; 大模型推理服务到底怎么跑起来的？大模型推理服务的运行过程中，CPU和GPU分别负责哪些工作？ &gt; 用GPU一定比CPU跑的快么？哪些场景需要用GPU? GPU最初的使...

`[]` `inference` `大模型`

---

### [Karpathy 最新方法论：把 LLM 当编译器用，知识管理该换个思路了](https://mp.weixin.qq.com/s?__biz=Mzk4ODkzOTY3MA==&mid=2247484735&idx=1&sn=6c93e0c324588762e10a99e915a04678)
⭐⭐⭐⭐4 🇨🇳 · 昨天

解读 Andrej Karpathy 2026 年 4 月提出的 LLM 知识库方法论。核心类比：把 LLM 当编译器，原始资料当源代码，生成 Wiki 当可执行文件。三层目录结构：raw/（原始素材）、wiki/（LLM 编译产出的结构化 Markdown）、output/（查询结果和衍生输出）。四步工作流：摄入（Ingest）到编译（Compile）到查询（Query）到健康检查（Lint）。与 RAG 的关键区别：RAG 是查询时实时检索（临时性），Karpathy 的方法是提前编译（持久性），查询结果自动回写 Wiki。适用规模约 40 万字，不需要向量数据库。

`Karpathy` `knowledge-management` `LLM` `wiki` `obsidian`

---

### [My self-sovereign / local / private / secure LLM setup, April 2026](https://vitalik.eth.limo/general/2026/04/02/secure_llms.html)
⭐⭐⭐⭐4 🌐 · 昨天

Vitalik Buterin 分享其本地私有 LLM 使用方案。隐私安全目标：防止远程模型获取隐私数据、防止 LLM 越狱攻击、防止后门和软件漏洞。硬件测试：NVIDIA 5090 (90 tok/s)、AMD 128GB 统一内存 (51 tok/s)、DGX Spark (60 tok/s)，推荐 5090 或 AMD 方案。软件栈：NixOS + llama-server（替代 Ollama，因能更好利用 GPU）+ llama-swap。Agent 工具方面讨论了 OpenClaw 的安全问题，强调沙箱隔离的重要性。附带 ComfyUI 本地图像/视频生成测试。

`local-LLM` `privacy` `security` `Vitalik` `self-sovereign`

---

### [[译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？](https://mp.weixin.qq.com/s?__biz=MzI4MTQyNzkxNw==&mid=2247484077&idx=1&sn=a9ea8f707fe733c43f8c5e8b119efd95&chksm=eaa3bb549d34d9b69fa713d6f5a05ee7aebbe587ddbcc7105cdfb25ececa5bd138a5a140cde0&mpshare=1&scene=1&srcid=0406EAJwfSBv8kNBXXR6T3mD&sharer_shareinfo=1285f5c35b21a56bde53198b6074ed60&sharer_shareinfo_first=1285f5c35b21a56bde53198b6074ed60)
⭐⭐⭐⭐4 🇨🇳 · 昨天

AI编译器的根本性权衡：既要通过抽象底层细节来实现易用性和可扩展性，但现代生成式AI工作负载又需要可编程性和硬件控制来实现极致性能。

---

### [【哥飞评站】AI贴纸生成网站 StickerBaker 的SEO评测报告和改进建议（4000字）](https://mp.weixin.qq.com/s/aCNzWnu09jQxPcPHMcswMA?s=09)
⭐⭐⭐⭐4 🇨🇳 · 昨天

受社群里 @damo 老板的启发，哥飞决定从今天开始一个新栏目，不定期点评一些网站，说说他们有哪些做得好的地方，有哪些还值得改进的地方。

---

### [【开放阅读】2021 年度十大数字应用（服务） – Dailyio](https://iois.me/archives/12964.html)
⭐⭐⭐⭐4 🇨🇳 · 昨天

本文选自付费邮件通讯「iPad Power User」，这是一份聚焦 iPad、iPadOS 与个人生产力的邮件通讯产品，通过不断探索与生活、工作息息相关的数字工具与方法论，为订阅读者提供中文互联网领域最优质的数字工具使用技巧、应用（服务）推荐以及数字化思考，欢迎试读、订阅。

---

### [一文读懂 Fragment 的方方面面](https://mp.weixin.qq.com/s?__biz=MzAxMTYzNTIyMA==&mid=2247492557&idx=1&sn=bae1e6b48f166d6d72e95e5608ec2a70&chksm=9bbcbcb6accb35a018e8f0fd173080168663e35735a3fbb27fdb609ce8ab594ad2aa8cacc1c1&mpshare=1&scene=1&srcid=0318iVNE7oNFxaYcBYAgzZke&sharer_sharetime=1647594344743&sharer_shareid=60bd7acea7881a97fbf9a6126d3e88d3)
⭐⭐⭐⭐4 🇨🇳 · 昨天

Fragment 是 Android 中历史十分悠久的一个组件，在 Android 3.0 （API 级别 11）的时候推出，时至今日已成为 Android 开发中最常用的组件之一。在一开始的时候，引入 Fragment 的目的是为了在大屏

---

### [当 AI Agent 开始直接调用数据，基础设施该如何进化？Data for AI Meetup 深圳站回顾](https://mp.weixin.qq.com/s?__biz=MzYzNTQ2OTExNw==&mid=2247483952&idx=1&sn=1b3d79e6954c2ca1c16c29fc4b3da50d&chksm=f126d2bf48847f1c244e82eca9f178a5ca7af229ef8a3bd072d75ac6fdd4141a9001e2acdc87&mpshare=1&scene=1&srcid=033058z9ZM14LnIIEveX4EM1&sharer_shareinfo=58564e21a16753dff1b07f4dd170e28c&sharer_shareinfo_first=52440a3d750e438e1c8d8bc7c90a65c1)
⭐⭐⭐⭐4 🇨🇳 · 昨天

当 AI Agent 开始直接调用数据，基础设施该如何进化？Data for AI Meetup 深圳站回顾

---

### [微信正式发布多模态大模型POINTS1.5](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649787907&idx=1&sn=e37095afd62e779e0d2b0b6356201b80&chksm=bf24d99626cf63fb1cf142d6740b5321f0853a1de019f1210500b7f57fd948c0b1a87feb0251&mpshare=1&scene=1&srcid=1214l9Q9sgMr56MjXRxwjfGh&sharer_shareinfo=8eed771cea5ad1691bbb03ff4506784c&sharer_shareinfo_first=8eed771cea5ad1691bbb03ff4506784c)
⭐⭐⭐⭐4 🇨🇳 · 昨天

?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2Fj3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

---

### [查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金](https://juejin.cn/post/7147526675536969742)
⭐⭐⭐⭐4 🇨🇳 · 昨天

查看浏览器Browsers的内核版本, 可以用 navigator.userAgent 在浏览器控制台输入:navigator.userAgent 几乎所有主要浏览器都支持 navigator.use

---

### [真·万字长文:可能是全网最晚的chatgpt技术总结](https://zhuanlan.zhihu.com/p/613698929?utm_campaign=shareopn&utm_medium=social&utm_oi=761310487785783296&utm_psn=1621196363999485952&utm_source=wechat_session)
⭐⭐⭐⭐4 🇨🇳 · 昨天

最近ChatGPT可以说是火遍了全世界，作为由知名人工智能研究机构OpenAI于2022年11月30日发布的一个大型语言预训练模型，他的核心在于能够理解人类的自然语言，并使用贴近人类语言风格的方式来进行回复。模型开放使用以来，在人工智能领域引起了巨大的轰动，也成功火出了技术圈。从数据上看，ChatGPT用户数在5天内就达到了100万，2个月就达到了1亿；另外，在很多非人工智能领域，已经有机构在尝试用ChatGPT去做一些智能生成的事。…

---

### [黄仁勋领导的 Nvidia 如何推动 AI 革命 [译]](https://baoyu.io/translations/new-yorker/how-jensen-huangs-nvidia-is-powering-the-ai-revolution)
⭐⭐⭐⭐4 🇨🇳 · 昨天

这家公司的 CEO，黄仁勋，把所有筹码压在了一种全新的芯片上。如今 Nvidia 已跻身世界最大公司之列，他的下一步会怎样？

---

### [用 Obsidian + Claude 搭个人知识库：核心架构实践](https://x.com/yanhua1010/status/2041356233819767258)
@yanhua1010 · ⭐⭐⭐3 🇨🇳 · 昨天

Obsidian + Claude 搭建个人知识库的核心架构实践。核心思路：把笔记库当代码仓库来&quot;编译&quot;。三层目录结构：原料/（只读，Claude 不可修改）→ 摘要/（Claude 结构化编译产物）→ 沉淀/（Query 高质量回答落文件）。两个元文件：CLAUDE.md（控制 AI 行为的最高宪法）和 index.md（全局目录 + TLDR，Claude 检索时先扫再深读）。日常工作流三个动作：Ingest（逐篇处理）、Query（好回答存文件）、Lint（定期健康检查）。防腐化底线：重要断言必须有来源、新旧冲突报 diff 不覆盖、区分事实和推论。

`Obsidian` `Claude` `知识库` `CLAUDE.md` `个人知识管理`

---

### [V 神本地 LLM 环境配置](https://x.com/fkysly/status/2040976089196167538)
@马天翼 · ⭐⭐⭐3 🇨🇳 · 昨天

V 神分享的本地大模型环境配置博客。从硬件选型开始，详细讨论如何构建一套满足隐私、安全、离线要求的 Local LLM 环境。特别值得注意的细节：为了减少飞机上离线情况下的模型幻觉，他把 1GB 维基百科内容都存了下来方便模型自我核实。同时也考虑了预算有限朋友的硬件推荐方案。

`本地LLM` `Vitalik` `隐私` `离线` `硬件配置`

---

### [PocketLLM: Enabling On-Device Fine-Tuning for Personalized LLMs](#)
⭐⭐⭐3 🇨🇳 · 昨天

## 1. 核心问题
这篇论文解决的是“端侧个性化”中最现实的拦路虎：**微调内存开销**。很多工作证明了“可以做微调”，但通常在树莓派或实验环境，离手机实用化很远。PocketLLM 的价值在于把问题拉回到真实手机场景。

## 2. 论文贡献（按价值排序）
1) **明确瓶颈优先级**：在端侧微调中，内存是可行性门槛；算力更多影响时延。
2) **方法选择正确**：采用无导数优化绕开梯度/优化器状态，直接打掉最大内存项。
3) **实机验证**：在 OPPO Reno 6 上给出可复现实验（RoBERTa-large 与 OPT-1.3B）。

## 3. 关键数据的含义
- RoBERT…

`perfetto` `on-device` `fine-tuning` `coding` `android`

---

### [(1 条消息) 如何评价 2023 年 2 月 AI 绘画的最新水平？ - 知乎](https://www.zhihu.com/question/584053473/answer/2900010564)
⭐⭐⭐3 🌐 · 昨天

(1 条消息) 如何评价 2023 年 2 月 AI 绘画的最新水平？ - 知乎
更新：文末有简单复现的步骤——————————————20230220更新：Stable diffusion + chilloutmix…
Read in Cubox  
Read Original
------------------------------------------
Stable diffusion + chilloutmix

`Stable Diffusion` `Diffusion`

---

### [&quot;Philosophers warn us not to be satisfied with mere learning, but to add practice and then training.&quot; | Revue](https://newsletter.stoicallytyped.com/issues/philosophers-warn-us-not-to-be-satisfied-with-mere-learning-but-to-add-practice-and-then-training-725262#/)
⭐⭐⭐3 🌐 · 昨天

&quot;Philosophers warn us not to be satisfied with mere learning, but to add practice and then training.&quot; | Revue
StoicallyTyped Newsletter - Hey happy Monday!I&#x27;m on vacation! I have some time before I start my new job and am taking advantage of all this free time to visit f
Read in Cubox  
Read Original
&quot;Philosophers warn us not to be satisfied with mere learning, but to add pract...

`Newsletter`

---

### [AIGC对程序员的影响 - Thoughtworks洞见](https://qapodcast.typlog.io/episodes/how-aigc-impact-programmers?s=09)
⭐⭐⭐3 🇨🇳 · 昨天

AIGC对程序员的影响 - Thoughtworks洞见
本期播客是参与 #2023技术播客节 共创共建的一期内容。12月4日至8日，每天围绕一个主题，带来8～11期的内容，更多详情也可关注官网 https://podfest.tech，或者微信公众号、即刻、X搜索「2023技术播客节」，欢迎大家...
Read in Cubox  
Read Original
本期播客是参与 #2023技术播客节 共创共建的一期内容。12月4日至8日，每天围绕一个主题，带来8～11期的内容，更多详情也可关注官网 https://podfest.tech，或者微信公众号、即刻、X搜索「2023技术播客节」，欢迎大家多多关注，一键多连！
在这一期的播客中，我们将探讨AI技术，尤其是ChatGPT和AIGC，如何改变软件工程的面貌。我们会聚焦于AI模型的不稳定性给开发者...

`ChatGPT` `AIGC`

---

### [AI绘画会不会抢画师饭碗](https://mp.weixin.qq.com/s?__biz=MjM5MjAzODU2MA==&mid=2652789693&idx=1&sn=bc16194dca73c8472ed7bbb149585879&chksm=bd4690728a311964aaa3234e175b0c3523f168be7230a8f20d13e8c49cb88d764a34a042877c&mpshare=1&scene=1&srcid=0808RVMuXMWPK4gL1C3CsZ3l&sharer_sharetime=1659925286253&sharer_shareid=b7cc12eb3054f40795517e846030e3c8)
⭐⭐⭐3 🇨🇳 · 昨天

还差10天，我成为艺术家这件事就要满3个月了。近3个月以来，几乎每天都会有人留言问我：AI绘画会不会取代画家？
Read in Cubox  
Read Original
还差10天，我成为艺术家这件事就要满3个月了。近3个月以来，几乎每天都会有人留言问我：AI绘画会不会取代画家、插画师的工作？
以前不好回答这个问题，因为我才开始接触AI绘画，哪里能说出个一二三四。我说能或者不能，你信么？你若信，我信么？现在，鉴于我已经成为季度级艺术家，有了一些个人的实际体验，这里我想谈谈我的个人看法。
首先，结论是不会抢饭碗。乐观一点来说，也许还会增加了大米供应。

---

### [ChatGPT Apps - Ranking ~ ...](https://ossinsight.io/collections/chat-gpt-apps/)
⭐⭐⭐3 🌐 · 昨天

# ChatGPT Apps - Ranking ~ ... ChatGPT Apps - Ranking ~ https://ossinsight.io/collections/chat-gpt-apps/ 想玩chatgpt项目的可以在这里找找思路 Last 28 Days / Month-to-Month Ranking The following table ranks repositories using three metrics: stars, pull requests, and issues. The table compares last 28 days or the mo...

`rag` `[]` `openai` `chatgpt`

---

### [ChatGPT应用开发小记](https://www.bmpi.dev/dev/chatgpt-development-notes/my-gpt-reader/)
⭐⭐⭐3 🇨🇳 · 昨天

本文分享了笔者使用 chatGPT 开发 myGPTReader 开源项目的过程。 * 生成式预训练模型（GPT: Generative Pre-trained Transformer） * 大语言模型（LLM: Large Language Model） 如何开发一个基于chatGPT的应用？答案就在问题里，那就是用chatGPT来开发基于chatGPT的应用。本文以笔者的一个开源项目 myGPTReader 为例，分享我是如何基于chatGPT去开发这个系统的，这个系统的功能见这篇文章：我的AI阅读助手。 为了探索chatGPT辅助开发的可能性，我在项目开发之初就记录了与chatGPT对话...

`transformer` `llm` `fine-tuning` `[]` `prompt`

---

### [Claude for Chrome 一手体验！自动回复微信、发Twitter、做调研……做AI浏览器的创业者该慌了，比赛已经结束](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498894&idx=1&sn=65bdd89973e4750f9edb33e529813be5&chksm=e83b99637c7fd1cbfcda542b07c524c2d50be42a960bb5888f61f1b2da9f4321bcae6c1c5e35&mpshare=1&scene=1&srcid=09063RMLHnpiiWHHsRoVk1LZ&sharer_shareinfo=fd59ab55729503a9e0f3ed995ba2581b&sharer_shareinfo_first=fd59ab55729503a9e0f3ed995ba2581b)
⭐⭐⭐3  · 昨天

# Claude for Chrome 一手体验！自动回复微信、发Twitter、做调研……做AI浏览器的创业者该慌了，比赛已经结束 Anthropic 这家公司虽然人品不咋地，但是产品能力是真强啊。国产AI得加油了。 今天早上，有幸在朋友的帮助下，用上了Claude for Chrome使用权限，根据全球只有1000人收到了邀请。 ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F607DKnuWzlFHEAiaNibvnpL4MscUY0SMDlicTPj2bqseStSPOnGNuNdqM3lwhX30GcHadSafQKBFDCfC...

`claude` `anthropic`

---

### [DeepSeek-R1 论文解析——人工智能领域的 RL LLM 新时代？](https://mp.weixin.qq.com/s?__biz=MzUzNzg4Nzc3MQ==&mid=2247485126&idx=1&sn=0b59ea812a2f0eedcf7de12986d99cbd&chksm=fbafde0216ffbfe4fbb5099f6ad2c2cb83630ee86c5da54ae9ec7cd75c1ed986d99f28a30760&mpshare=1&scene=1&srcid=0204EBmVUAlccQp8G0Kw32Dm&sharer_shareinfo=a4cb3d9e576db809f2a6e609010b59f5&sharer_shareinfo_first=a4cb3d9e576db809f2a6e609010b59f5)
⭐⭐⭐3 🇨🇳 · 昨天

# DeepSeek-R1 论文解析——人工智能领域的 RL LLM 新时代？ DeepSeek-R1 论文解析——人工智能领域的 RL LLM 新时代？ 近年来，人工智能 (AI) 领域取得了快速发展，大型语言模型 (LLM) 为通用人工智能 (AGI) 铺平了道路。OpenAI的 o1 是 一个出色的模型，它引入了创新的推理时间扩展技术，可显著增强推理能力。然而，它仍然是闭源的。 今天，我们深入研究了 DeepSeek 推出的开创性研究论文 DeepSeek-R1。这篇题为&quot;DeepSeek-R1：通过强化学习激励大型语言模型中的推理能力&quot;的 论文介绍了一种最先进的开源推理模型，以及使用大...

`deepseek` `llm` `fine-tuning` `[]` `openai`

---

### [Google I/O 2024 ：新的 Gem)ini AI 升级、Android 15 和 Pixel 预告](https://mp.weixin.qq.com/s?__biz=MzIyMzg2MzQxNg==&mid=2247487354&idx=1&sn=288273fbf2c559ec7d2e4d467fd29d5e&chksm=e816f86ddf61717bfd28e62f00c7cadba183cee32f1cd962d21d64c4499e07f021cb44865736&mpshare=1&scene=1&srcid=0515qejem0UZ8UjNf5v0DoYn&sharer_shareinfo=34703d8c05f82f0416525405701effdd&sharer_shareinfo_first=34703d8c05f82f0416525405701effdd)
⭐⭐⭐3 🇨🇳 · 昨天

# Google I/O 2024 ：新的 Gem)ini AI 升级、Android 15 和 Pixel 预告 Google I/O 2024大会已经改变了游戏规则，展示了最新的人工智能技术创新，并揭开了备受期待的 And ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F7G6wAxO5rWAadWLvb3SZuXWlwqTicQX35Aule3BhcgxB9L9YyLYzPHwP19z4xq10rnvubg2Bn2Mn9U6yJRTTWiaw%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg&amp;val...

`gemini` `[]` `inference`

---

### [Qualcomm Snapdragon X2 Elite微架构](https://mp.weixin.qq.com/s?__biz=MzkzMTA2NjgzMA==&mid=2247488554&idx=1&sn=1e38328c97b182f71c139e0fc69447da)
@亦安 · ⭐⭐⭐3 🇨🇳 · 昨天

基于 Chip&amp;Cheese PPT 解读高通第三代 Oryon 核心微架构。3 cluster 18 核最高 5GHz，共享 L2 16MB/cluster，9宽 decode/retire，ROB 650+。L1-Miss-L2-Hit 21 cycle，96KB DCache。L2 TLB 标称 8K entry（实测约 1.5K-2K）。前代的渐进优化。

`Qualcomm` `Snapdragon` `Oryon` `CPU` `微架构`

---

### [YOLOv8 模型训练入门指南：手把手搞定目标检测AI](https://mp.weixin.qq.com/s?__biz=MzAxNTA3MDY1NA==&mid=2455889075&idx=2&sn=0b6d2d319183839da8e78fc3787e5cca&chksm=8de8a6e86f55184c2662e5fa24ffd44dcd2ada03059001d473f9fed42d33b3a1b8827f9153b2&mpshare=1&scene=1&srcid=0526AJKtvTBUcyEeSZbjIhJ7&sharer_shareinfo=a9e2fbbc1caacc3a594e52fa5d232d42&sharer_shareinfo_first=386794d521a0d57b35661b763fec48de)
⭐⭐⭐3 🇨🇳 · 昨天

我原本觉得 AI 很高深，直到偶然接触了 YOLOv8 ------ 一款&quot;傻瓜式&quot;的目标检测模型。封装良好、文档详尽，甚至不需要理解太多数学公式，也能训练出能用的视觉模型。

---

### [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
⭐⭐⭐3 🌐 · 昨天

[需翻译] * Todoist Stats in Readme - Daily Todoist Stats on your Profile Readme * Visitor Badge - Count visitors for your README.md, Issues, PRs in GitHub * 1990s style Visitor Counter - Add a 1990s style visitor counter with one line of markdown. * Vistor Co...

---

### [一文带你了解OpenAI Sora](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649782526&idx=1&sn=420ff38a80ff74684d556b77b275fe9f&chksm=becceb8589bb62930ada988238d86bc3569977687ce98f850258c49513316ff66409363c80e7&mpshare=1&scene=1&srcid=0221qJgYnOZE5WqV4grTDb9D&sharer_shareinfo=efd1e8bd8e163e6b9001852a9dc5ad8c&sharer_shareinfo_first=efd1e8bd8e163e6b9001852a9dc5ad8c)
⭐⭐⭐3 🇨🇳 · 昨天

Cubox 收藏 — 一文带你了解OpenAI Sora

---

### [万字长文深度解析Sora的核心技术，解密OpenAI掌控时空的秘密武器](https://weibo.com/ttarticle/p/show?id=2309405003442207719529)
⭐⭐⭐3 🇨🇳 · 昨天

我们大量看到的stablediffusion体系下的animediff，就经常给人一种魔幻变化的感觉，难以投入到稳定的视频生成中。

---

### [关于AI的一些实践和思考 - Rolen&#x27;s Blog](https://rolen.wiki/some-practices-and-thoughts-on-ai/)
⭐⭐⭐3 🇨🇳 · 昨天

这几年，由于AI的出现，我感觉生活节奏开始加速，加速，因为可以做的事情更多了，欲望也更多了，人反而变得更加焦虑了。任何事情都有两面性，好的方面是AI的出现满足了很多我曾经无法完成的事情，或者要掉好几层皮才能完成的事情，现在确实可以很轻松地解决。

---

### [凯哥  |  当ERP遇到ChatGPT，新世界的大门被打开](https://mp.weixin.qq.com/s?__biz=MzU3MTkwMDU1NQ==&mid=2247485023&idx=1&sn=4e73a266370216e5350f92d4acfa4c30&chksm=fcd851bbcbafd8ad13a331d14fb0d34ee7474047a53ebc1b2c2ad6de4be0ba45b2c56b36ffb0&mpshare=1&scene=1&srcid=0211zF7t32ICNtkwoAGzpEk3&sharer_sharetime=1676079405528&sharer_shareid=b7cc12eb3054f40795517e846030e3c8)
⭐⭐⭐3 🇨🇳 · 昨天

关键发现：ChatGPT可以导入私有数据进行训练，从而指导业务优化ChatGPT能够记住每一个回话的内容，从

---

### [快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium与Airtest最为 - 掘金](https://juejin.cn/post/7462305424554590219)
⭐⭐⭐3 🇨🇳 · 昨天

快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium与Airtest最为 - 掘金

---

### [深蹲VS大齿比：力量训练的终极选择题！哪个更好呢？](https://mp.weixin.qq.com/s?__biz=MzI4MDEyMDI2OQ==&mid=2247484717&idx=1&sn=6e1b8f337185004eb961c28b15837476&chksm=eaffa30cfbdc151800bd3947a7413a149599167b72cac924a5ec520971c2d6f2dabfa15cdd8c&mpshare=1&scene=1&srcid=0507tDXMgLXAE0G3ILaueOul&sharer_shareinfo=44c2dbb330282eeaa064ce98c54b0197&sharer_shareinfo_first=44c2dbb330282eeaa064ce98c54b0197)
⭐⭐⭐3 🇨🇳 · 昨天

?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fic4cXMRs0WRtzjrWqaZibg11zc4BSbnaiaryP1JuaFcbuiaT8LZwAU1JKic2qzibsdNO9iaevzRo4vfbJRv7v9Hy4vtkw%2F640%3Fwx_fmt%3Dpng)

---

### [移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调实现NPU高效部署](https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2449991915&idx=1&sn=da3dd89e182f04dee8c8c5ac2ade9141&chksm=b0f950be96af7bc12328a5ee74bbfc11ed6b5b909d5e2424fbfe181c67021350ab246993d8e0&mpshare=1&scene=1&srcid=0828uXErCxwOEwzSvr55C1dO&sharer_shareinfo=68e9331636d3c4869d8011f376bf8128&sharer_shareinfo_first=68e9331636d3c4869d8011f376bf8128)
⭐⭐⭐3 🇨🇳 · 昨天

移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调实现NPU高效部署

---

### [端侧 AI](https://mp.weixin.qq.com/s?__biz=MzkyMTU4OTE2OA==&mid=2247488655&idx=1&sn=dbf749f318315a561f12f7966be09b84&chksm=c1801050f6f79946a2d6e6a1a04e9cbe0f1fc8364be2e886ac6fa6ec7d54d16db791481279ab&mpshare=1&scene=1&srcid=0620BptoCw1X2FVALZd6If67&sharer_shareinfo=14850c869ec881aeaed27ab4d570556b&sharer_shareinfo_first=e2db0e175c1edf666b0021e55fa7de74)
⭐⭐⭐3 🇨🇳 · 昨天

1、端侧LLM性能瓶颈，不是算力，而是内存速度。   -每生成一个token需要把模型在内存中读出一遍，10-15tops算力即可实现7b 10token/s以上的推理速度，功耗也远低于手游，所以无需担心H端侧。   -目前手机最快大概也就是LPDDR5T，9600MT/S，折合76.8 GB/s，理论最高能实现7b int4 下20 token/s，或14b int4下10token/s的输出。   -存量手机大多内存带宽在40-60GB/s。

---

### [面试随想 | tsaiggo&#x27;s blog](https://www.tsaiggo.life/posts/thinking-in-interview/)
⭐⭐⭐3 🇨🇳 · 昨天

20年本科毕业后就加入了滴滴，今年算是自己的第一次社招面试跳槽吧，感觉还挺奇妙的，随手记录一下自己关于社招的随想吧。 **永远谨记：Fake it till you make it.**

---
