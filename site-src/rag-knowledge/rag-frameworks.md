# RAG框架

RAG Frameworks — 9 条活跃资源

### [0x1 Underlying LLMs](https://juejin.cn/post/7312243176834809908) 
 (2024-09-03) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，rag-frameworks 领域相关内容**

Read in Cubox  
Read Original
LLM (Large Language Models) 的风头一时无两，席卷万千行业。业内不乏有关于 LLM 的研究和讨论，但鲜有立足终端的视角。团队上半年曾有过对 GPT 进终端的分析，但 LLM 日新月异，旧分析已经不完全跟得上变化了。适逢年底规划季，尝试重新梳理 LLM 的现状，预判未来变化的趋势，希望能为迷茫的同仁提供思考的角度，也希望获得战斗在一线的友军的指点。
求砖 \& 免砖申明：
不包含 LLM 入门介绍，够时间可以报吴恩达的免费课程和 NVIDIA 与 LlamaIndex 合力出品的；不够时间也有 Andrej Karpathy 的 一小时入门；
非算法出身，如有错漏之处，恳请指正；力争能让 RD、PM、DA 们都能看懂，如果不明处，欢迎讨论；
终端 LLM 应用有一定不...
 `LLM` `RAG` `Inference` `LLaMA` `Multimodal`

---
### [AIGC图像生成的原理综述与落地畅想](https://mp.weixin.qq.com/s?__biz=MzAxNDEwNjk5OQ==&mid=2650503986&idx=1&sn=f92c8986e13e30184cb43e6f76f985d2&chksm=8397b32ab4e03a3c9f6e03e8b03aed5db17f4834d0435c6ac40311ff8d882531682211c5ad3d&mpshare=1&scene=1&srcid=0322KCccdeScAxL5DF5t0BvM&sharer_sharetime=1679479393566&sharer_shareid=b7cc12eb3054f40795517e846030e3c8) 
 (2023-03-22) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**AIGC/图像生成相关收藏**

基于Stable Diffusion扩散模型的综述
Read in Cubox  
Read Original
AIGC，这个当前的现象级词语。本文尝试从文生图的发展、对其当前主流的 Stable Diffusion 做一个综述。以下为实验按要求生成的不同场景、风格控制下的生成作品。
GAN 系列算法开启了图片生成的新起点。GAN的主要灵感来源于博弈论中零和博弈的思想，通过生成网络G（Generator）和判别网络D（Discriminator）不断博弈，进而使G学习到数据的分布。
1.
   G是一个生成式的网络，它接收一个随机的噪声z（随机数），通过这个噪声生成图像。
2.
   D是一个判别网络，判别一张图片是不是"真实的"。它的输入参数是x，x代表一张图片，输出D（x）代表x为真实图片的概率，如果为1，就代表100%是真实的图片。
 `AIGC` `Stable Diffusion` `Embedding` `Transformer` `Diffusion` `Vision`

---
### [Karpathy 最新方法论：把 LLM 当编译器用，知识管理该换个思路了](https://mp.weixin.qq.com/s?__biz=Mzk4ODkzOTY3MA==&mid=2247484735&idx=1&sn=6c93e0c324588762e10a99e915a04678) 
 (2026-04-05) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Karpathy 的知识编译方案是对 RAG 思维的范式转换，个人知识管理新方向**

解读 Andrej Karpathy 2026 年 4 月提出的 LLM 知识库方法论。核心类比：把 LLM 当编译器，原始资料当源代码，生成 Wiki 当可执行文件。三层目录结构：raw/（原始素材）、wiki/（LLM 编译产出的结构化 Markdown）、output/（查询结果和衍生输出）。四步工作流：摄入（Ingest）到编译（Compile）到查询（Query）到健康检查（Lint）。与 RAG 的关键区别：RAG 是查询时实时检索（临时性），Karpathy 的方法是提前编译（持久性），查询结果自动回写 Wiki。适用规模约 40 万字，不需要向量数据库。
 `Karpathy` `knowledge-management` `LLM` `wiki` `obsidian` `knowledge-compile` `RAG`

---
### [一文读懂 Fragment 的方方面面](https://mp.weixin.qq.com/s?__biz=MzAxMTYzNTIyMA==&mid=2247492557&idx=1&sn=bae1e6b48f166d6d72e95e5608ec2a70&chksm=9bbcbcb6accb35a018e8f0fd173080168663e35735a3fbb27fdb609ce8ab594ad2aa8cacc1c1&mpshare=1&scene=1&srcid=0318iVNE7oNFxaYcBYAgzZke&sharer_sharetime=1647594344743&sharer_shareid=60bd7acea7881a97fbf9a6126d3e88d3) 
 (2022-03-18) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 一文读懂 Fragment 的方方面面**

Fragment 是 Android 中历史十分悠久的一个组件，在 Android 3.0 （API 级别 11）的时候推出，时至今日已成为 Android 开发中最常用的组件之一。在一开始的时候，引入 Fragment 的目的是为了在大屏


---
### [查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金](https://juejin.cn/post/7147526675536969742) 
 (2024-03-05) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — 查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金**

查看浏览器Browsers的内核版本, 可以用 navigator.userAgent 在浏览器控制台输入:navigator.userAgent 几乎所有主要浏览器都支持 navigator.use


---
### [用 Obsidian + Claude 搭个人知识库：核心架构实践](https://x.com/yanhua1010/status/2041356233819767258) 
by @yanhua1010 (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**Obsidian + Claude 知识库三层层架构，把笔记库当编译器而非堆积场。**

Obsidian + Claude 搭建个人知识库的核心架构实践。核心思路：把笔记库当代码仓库来"编译"。三层目录结构：原料/（只读，Claude 不可修改）→ 摘要/（Claude 结构化编译产物）→ 沉淀/（Query 高质量回答落文件）。两个元文件：CLAUDE.md（控制 AI 行为的最高宪法）和 index.md（全局目录 + TLDR，Claude 检索时先扫再深读）。日常工作流三个动作：Ingest（逐篇处理）、Query（好回答存文件）、Lint（定期健康检查）。防腐化底线：重要断言必须有来源、新旧冲突报 diff 不覆盖、区分事实和推论。
 `Obsidian` `Claude` `知识库` `CLAUDE.md` `个人知识管理`

---
### [ChatGPT Apps - Ranking ~ ...](https://ossinsight.io/collections/chat-gpt-apps/) 
 (2023-03-30) | ⭐⭐⭐ 3/5 | 🌐

**Cubox 收藏: ChatGPT Apps - Ranking ~ ...**

# ChatGPT Apps - Ranking ~ ... ChatGPT Apps - Ranking ~ https://ossinsight.io/collections/chat-gpt-apps/ 想玩chatgpt项目的可以在这里找找思路 Last 28 Days / Month-to-Month Ranking The following table ranks repositories using three metrics: stars, pull requests, and issues. The table compares last 28 days or the mo...
 `rag` `[]` `openai` `chatgpt`

---
### [Claude for Chrome 一手体验！自动回复微信、发Twitter、做调研……做AI浏览器的创业者该慌了，比赛已经结束](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498894&idx=1&sn=65bdd89973e4750f9edb33e529813be5&chksm=e83b99637c7fd1cbfcda542b07c524c2d50be42a960bb5888f61f1b2da9f4321bcae6c1c5e35&mpshare=1&scene=1&srcid=09063RMLHnpiiWHHsRoVk1LZ&sharer_shareinfo=fd59ab55729503a9e0f3ed995ba2581b&sharer_shareinfo_first=fd59ab55729503a9e0f3ed995ba2581b) 
 (2025-09-06) | ⭐⭐⭐ 3/5 | 🌍

**Cubox 收藏: Claude for Chrome 一手体验！自动回复微信、发Twitter、做调研……做AI浏览器**

# Claude for Chrome 一手体验！自动回复微信、发Twitter、做调研……做AI浏览器的创业者该慌了，比赛已经结束 Anthropic 这家公司虽然人品不咋地，但是产品能力是真强啊。国产AI得加油了。 今天早上，有幸在朋友的帮助下，用上了Claude for Chrome使用权限，根据全球只有1000人收到了邀请。 ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F607DKnuWzlFHEAiaNibvnpL4MscUY0SMDlicTPj2bqseStSPOnGNuNdqM3lwhX30GcHadSafQKBFDCfC...
 `claude` `anthropic`

---
### [abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme) 
 (2024-08-26) | ⭐⭐⭐ 3/5 | 🌐

**Cubox 收藏 — abhisheknaiidu/awesome-github-profile-readme**

[需翻译] * Todoist Stats in Readme - Daily Todoist Stats on your Profile Readme * Visitor Badge - Count visitors for your README.md, Issues, PRs in GitHub * 1990s style Visitor Counter - Add a 1990s style visitor counter with one line of markdown. * Vistor Co...


---