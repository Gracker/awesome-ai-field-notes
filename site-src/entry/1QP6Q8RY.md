---
title: '抄 Apple Intelligence 作业的思路 文章从 LLM 的近况切入，探讨 Apple Intelligen - 掘金'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# 抄 Apple Intelligence 作业的思路 文章从 LLM 的近况切入，探讨 Apple Intelligen - 掘金

> Cubox 收藏 — 抄 Apple Intelligence 作业的思路 文章从 LLM 的近况切入，探讨 Apple 

🔗 [原文链接](https://juejin.cn/post/7407385581079396389) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

---

# 抄 Apple Intelligence 作业的思路 文章从 LLM 的近况切入，探讨 Apple Intelligen

> 发布时间: 2024-08-27T08:38:20.000Z
> 原文链接: https://juejin.cn/post/7407385581079396389

---


# 抄 Apple Intelligence 作业的思路

[字节跳动\_离青](/user/2585702698590472/posts)

2024-08-27 4,179 阅读50分钟

已关注

> 6 月的 WWDC 7 月刷，7 月的构思 8 月写，着实拖延了些时日，希望成稿之日观点尚能构成参考 _(:з」∠)_

> 字节跳动 Client AI 团队招聘中，业务年均百亿收益，SDK 日均万亿调用，诚邀推荐：
>
> -   社招
>     -   [算法工程师 @北京/杭州/上海](https://link.juejin.cn?target=http%3A%2F%2Fjob.toutiao.com%2Fsociety%2Fposition%2Fdetail%2F6909805440076777735 "http://job.toutiao.com/society/position/detail/6909805440076777735")
>     -   [平台工程师 @北京/深圳](https://link.juejin.cn?target=http%3A%2F%2Fjob.toutiao.com%2Fsociety%2Fposition%2Fdetail%2F7385113819154860314 "http://job.toutiao.com/society/position/detail/7385113819154860314")
>     -   [移动工程师 @北京/深圳](https://link.juejin.cn?target=https%3A%2F%2Fjobs.bytedance.com%2Fexperienced%2Fposition%2F7281479395705407803%2Fdetail "https://jobs.bytedance.com/experienced/position/7281479395705407803/detail")
> -   校招
>     -   [算法工程师 @北京/杭州](https://link.juejin.cn?target=http%3A%2F%2Fjob.toutiao.com%2Fcampus%2Fposition%2Fdetail%2F7395508007599196453 "http://job.toutiao.com/campus/position/detail/7395508007599196453")
> -   实习
>     -   前端工程师 @深圳，限 26 届及以后

## 0x0 前言

本篇讨论 Apple Intelligence，如果还没有围观 WWDC 24，稍作了解有益代入：

> 节选 WWDC 24 与 Apple Intelligence 相关的 Sessions
>
> -   **[WWDC 24 Keynote](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F101%2F%3Ftime%3D3871 "https://developer.apple.com/videos/play/wwdc2024/101/?time=3871")** **|** **[YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DRXeOiIDNNek "https://www.youtube.com/watch?v=RXeOiIDNNek")** **(主会场，Apple Intelligence 压轴，1:04:00 才开始)**
> -   [Apple Intelligence in 5 minutes](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQ_EYoV1kZWk "https://www.youtube.com/watch?v=Q_EYoV1kZWk") (YT only)
> -   [Apple Intelligence | Privacy](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D546ufMY7488 "https://www.youtube.com/watch?v=546ufMY7488") (YT only)
> -   [Platforms State of the Union](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F102%2F "https://developer.apple.com/videos/play/wwdc2024/102/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DYJZ5YcMsgD4 "https://www.youtube.com/watch?v=YJZ5YcMsgD4")
> -   [Bring your app to Siri](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F10133%2F "https://developer.apple.com/videos/play/wwdc2024/10133/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DLb89T7ybCBE "https://www.youtube.com/watch?v=Lb89T7ybCBE")
> -   [Bring your app’s core features to users with App Intents](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F10210%2F "https://developer.apple.com/videos/play/wwdc2024/10210/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DREGJcedvheE "https://www.youtube.com/watch?v=REGJcedvheE")
> -   [What’s new in App Intents](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F10134%2F "https://developer.apple.com/videos/play/wwdc2024/10134/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DwirvkabKh8k "https://www.youtube.com/watch?v=wirvkabKh8k")
> -   [Design App Intents for system experiences](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F10176%2F "https://developer.apple.com/videos/play/wwdc2024/10176/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dyyr4trqPgjo "https://www.youtube.com/watch?v=yyr4trqPgjo")
> -   [Bring expression to your app with Genmoji](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F10220%2F "https://developer.apple.com/videos/play/wwdc2024/10220/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DD58kVm2h4-w "https://www.youtube.com/watch?v=D58kVm2h4-w")
> -   [Get started with Writing Tools](https://link.juejin.cn?target=https%3A%2F%2Fdeveloper.apple.com%2Fvideos%2Fplay%2Fwwdc2024%2F10168%2F "https://developer.apple.com/videos/play/wwdc2024/10168/") | [YT](https://link.juejin.cn?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D79PkqsA_zk8 "https://www.youtube.com/watch?v=79PkqsA_zk8")

本篇将延用前作部分观点，探讨可回溯[重新思考终端 LLMs 和 Agents](https://juejin.cn/post/7312243176834809908 "https://juejin.cn/post/7312243176834809908")，观点如下：

1.  LLM 新增的核心能力是`多模态理解和生成` `内建知识` `推理能力`
2.  终端场景的 LLM 应用可以没有终端模型，终端 Agent 可以采用云端模型

惯例求砖 & 免砖申明：

-   未深入剖析技术细节，力争让 RD、PM、DA 们都能看懂，希望能抛砖引玉，启发思考
-   个人并不从事 LLM 相关工作，算法/工程判断、场景/路径推演与实际不合处，恳请指正
-   文档基于 24 年中时个人的现状认知和思维推断，有效性和有效期未知，请自主判断

> 超级省流版：
>
> -   以技术为基石的应用更要对技术诚实，LLM 幻觉和推理能力不足可以采用移交控制/验证和主动治理/约束策略
> -   并不是所有 AI 都需要以 AGI 为目标，提升现有产品的核心体验/收益也可以作为投入目标
> -   借助 LLM 实现跨 domain 交互在技术上可行，但不同 domain 有不同的商业模式考量

* * *

## 0x1 万象更新

虽然 Apple Intelligence 是本篇主题，但依然想先花点时间梳理 Apple Intelligence 诞生时代的技术背景，在这万象更新之余却又有点儿沉闷的时代。

### 0x10 Scale Up 与基建竞赛

from [Jim Fan](https://link.juejin.cn?target=https%3A%2F%2Fx.com%2FDrJimFan%2Fstatus%2F1805265388256837842 "https://x.com/DrJimFan/status/1805265388256837842")

from [Maxime Labonne](https://link.juejin.cn?target=https%3A%2F%2Fx.com%2Fmaximelabonne%2Fstatus%2F1816416043511808259 "https://x.com/maximelabonne/status/1816416043511808259")

![](images/img_001.jpg)

![](images/img_002.jpg)

Scale Up 依然是 2024 年毋庸置疑的主旋律。闭源方向上，Anthropic Claude、Google Gemini 和 OpenAI GPT-4 的旗舰模型一再扩大，在 Benchmark 榜单上争抢头把交椅，却没谁坐得安稳；开源方向上，[X 314b Grok-1](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fxai-org%2Fgrok-1 "https://github.com/xai-org/grok-1") 先吹响了号角，NVIDIA 迅速跟进 [Nemotron 340b](https://link.juejin.cn?target=https%3A%2F%2Fresearch.nvidia.com%2Fpublication%2F2024-06_nemotron-4-340b "https://research.nvidia.com/publication/2024-06_nemotron-4-340b") 狠狠秀了把肌肉，Meta 又凭借 405b 身躯的 [Llama 3.1](https://link.juejin.cn?target=https%3A%2F%2Fai.meta.com%2Fblog%2Fmeta-llama-3-1%2F "https://ai.meta.com/blog/meta-llama-3-1/") 挤开了一众豪杰，不甘寂寞的 Mistral 在 Llama 3.1 登场的第二天就放出了 [123b 的 Large2](https://link.juejin.cn?target=https%3A%2F%2Fmistral.ai%2Fnews%2Fmistral-large-2407%2F "https://mistral.ai/news/mistral-large-2407/") 并略有针对地表示 "Large Enough"。

狂欢之余，还需要保持清醒。虽然新闻报道多只津津乐道模型参数规模再创新高，毕竟参数规模最易于公众理解和比较，但 Scaling Law 并不只提升参数规模 —— Llama 3.1 在[论文](https://link.juejin.cn?target=https%3A%2F%2Fai.meta.com%2Fresearch%2Fpublications%2Fthe-llama-3-herd-of-models%2F "https://ai.meta.com/research/publications/the-llama-3-herd-of-models/")中着重强调了`data, scale, and managing complexity`，**数据**、**规模**和**复杂度**。露出水面的参数规模之下是一整座冰山。

#### 数据

数据的数量和质量对 pre-training 和 post-training 来说至关重要，以 Llama 为例， Llama 2 使用了 1.8T tokens，Llama 3 则在优化质量的同时，将数据量也提升到了 15T，而根据李沐老师的[分享 #1](https://link.juejin.cn?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1WM4m1y7Uh%2F "https://www.bilibili.com/video/BV1WM4m1y7Uh/")，15T 大概已经是互联网上可以抓取文本数据的上限了，李沐老师的[分享 #2](https://link.juejin.cn?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1u142187S5 "https://www.bilibili.com/video/BV1u142187S5") 全篇都在聊 training data，感兴趣可以自取。

跟据[透露](https://link.juejin.cn?target=https%3A%2F%2Fnew.qq.com%2Frain%2Fa%2F20240726A09AM400 "https://new.qq.com/rain/a/20240726A09AM400")，Llama 3 训练中大量使用了 Llama 2 生产的数据，也即合成数据，这是另一个有意思的命题。[Nature 封面文章](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fl9ka81Cj2LFzNbXXsaEbmA "https://mp.weixin.qq.com/s/l9ka81Cj2LFzNbXXsaEbmA")就质疑了左脚踩右脚螺旋升天的路数，认为放任大模型用自动生成的数据训练自己，在短短几代内 AI 就会陷入模型崩溃。或许 Llama 有应对合成数据的秘辛，但不论有无，似乎区隔数据的来源是一个有备无患的选择。

[Join AI 为合成数据背书文章](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FzUcilzUvgOoRU8plYIJYVw "https://mp.weixin.qq.com/s/zUcilzUvgOoRU8plYIJYVw")中的数据分类，和从`full data`到`the final data u can get`的图示，可以解释采用合成数据的原因以及数据采集工作背后的辛酸：

-   可见，可得，但不可用的数据的隐私数据
-   可遇不可求的 Corner Case
-   可见，可得，但是不免费的采标数据
-   可见、可得、免费但是数量少的可怜的开源数据

![](images/img_003.jpg)

![](images/img_004.jpg)

![](images/img_005.jpg)

![](images/img_006.jpg)

高质量数据是否会耗尽的学术争论还没有结束，不分赛道，工业应用的数据饕餮已然甚嚣尘上，比如[媒体买买买的 OpenAI](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI3MTA0MTk1MA%3D%3D%26mid%3D2652504068%26idx%3D3%26sn%3Ddda30c86836b4dc845bac01b2b121c27%26scene%3D21%23wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652504068&idx=3&sn=dda30c86836b4dc845bac01b2b121c27&scene=21#wechat_redirect")、[重金求声的 Meta](https://link.juejin.cn?target=https%3A%2F%2Fwww.ithome.com%2F0%2F785%2F971.htm "https://www.ithome.com/0/785/971.htm")；也不乏有游走在合法与非法的边缘的事，比如[惨遭多轮光顾的 YouTube](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FfNL8MOGOAWLvN0sMy-i_Lw "https://mp.weixin.qq.com/s/fNL8MOGOAWLvN0sMy-i_Lw")，以及[被大型唱片公司起诉 Udio & Suno](https://link.juejin.cn?target=https%3A%2F%2Fwww.cls.cn%2Fdetail%2F1713321 "https://www.cls.cn/detail/1713321")。

![](images/img_007.jpg)

不过，也不要以为爬虫数据是免费的午餐，例如 [Google 就着过 Reddit 和 Quora 的道](https://link.juejin.cn?target=https%3A%2F%2Fwww.ithome.com%2F0%2F782%2F165.htm "https://www.ithome.com/0/782/165.htm")，在搜索「google cheese not sticking to pizza」的结果里赫然建议「adding 1/8 cup of Elmer's glue」。是 Google 先动的手，自然也只能砸碎钢牙肚里吞了 🐶🐶🐶

#### 规模

Llama 3.1 405B + 15.6T tokens 预训练的开销是 3.8 × 10^25 次浮点运算，足足花了 54 天时间。作为比较，根据 [NVIDIA H100 的规格描述](https://link.juejin.cn?target=https%3A%2F%2Fwww.nvidia.com%2Fen-us%2Fdata-center%2Fh100%2F "https://www.nvidia.com/en-us/data-center/h100/")，在稀疏运算的加持下，H100 SXM FP8 Tensor Core 也不过能达到 3.9 × 10^15 FLOPs。如果只有一张 H100，就算破天荒实现了 GPU 全周期满负载运行，也需要 300+ 年的时间。运算量与运算能力之间至少足足有 10 个数量级差距，能在时间维度节约多少开销，把迭代速度抬上去，就得看其他维度的堆料和优化了。

万卡集群就是这样成为标配的。相较于传统分布式集群，大模型训练集群对计算、存储、传输的性能压榨更极致，乃至需要专门的供电和散热保障，对拓展性、可靠性的要求也都更严苛，新的设计也随之诞生。字节的 [MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs](https://link.juejin.cn?target=https%3A%2F%2Farxiv.org%2Fabs%2F2402.15627 "https://arxiv.org/abs/2402.15627") 也相应介绍了在算法设计、算子加速、计算调度、网络传输、容灾容错等方面的优化，按需了解吧。架构的迭代肯定不会止步于此，[小扎说 Llama4 训练算力得再乘 10](https://link.juejin.cn?target=https%3A%2F%2Fwallstreetcn.com%2Farticles%2F3722168 "https://wallstreetcn.com/articles/3722168")，而[马斯克干脆已经备好了 10 万块 H100](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FQf_p8-0FdgcNNsp5crYaHg "https://mp.weixin.qq.com/s/Qf_p8-0FdgcNNsp5crYaHg")，十万卡集群 is coming。

[Analysis of NVIDIA’s Latest Hardware: B100/B200/GH200/NVL72/SuperPod](https://link.juejin.cn?target=https%3A%2F%2Fwww.fibermall.com%2Fblog%2Fnvidia-b100-b200-gh200-nvl72-superpod.htm "https://www.fibermall.com/blog/nvidia-b100-b200-gh200-nvl72-superpod.htm") ![](images/img_008.jpg)

集群架构之下，计算和存储硬件也在快速迭代。上图为 fibermall 统计的 NVIDIA GPU 单卡性能，以稠密 FP16 计算性能为标尺，从 2020 年的 A100 到 2024 年的 B200 性能提升约 7 倍，功耗提升约 2.5 倍，提升速度甚至还超越了两年翻一番的黄氏定律。饶是如此，依然有 ASIC 玩家想要分 NVIDIA 的蛋糕，先有 [Groq Llama2 70B 刷出 300+ tokens/s 的闪电速度](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FtMDJP234MksYeUu_RUPzBA "https://mp.weixin.qq.com/s/tMDJP234MksYeUu_RUPzBA")，[引得 Yann LeCun 青眼](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FV0AteHwAAP-xFPc-y5BocQ "https://mp.weixin.qq.com/s/V0AteHwAAP-xFPc-y5BocQ")；后有 [Etched 梭哈 Transformer 8xSohu Llama 70b 上 500000 tokens/s](https://link.juejin.cn?target=https%3A%2F%2Fx.com%2FEtched%2Fstatus%2F1805625693113663834 "https://x.com/Etched/status/1805625693113663834")，如果模型结构基本定型，推理加速硬件恐怕还得有一场血战。出于众所周知的原因，此处还得给昇腾的训练和推理鼓鼓劲。

运行于硬件上的训练和推理同样有大幅优化的空间。以推理为例，[无问芯穹与清华、上交联合研究出品的大模型高效推理综述](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F7LKfamTnCyFih6_grf9m3A "https://mp.weixin.qq.com/s/7LKfamTnCyFih6_grf9m3A")，就将大模型的高效推理划分成关注输入输出的数据层优化、关注模型结构和压缩的模型层优化、关注服务调度和推理引擎优化的系统层优化。

单就模型层中的 Transformer 替代架构，就又能延伸出许多研究 —— Mamba、RWKV、TTT 都试图挑战 Transformer，尝试以更低的计算复杂度，更好地 Scale Up 和泛化；而每一个细分模型结构在论文发布后，又往往会激发出更多的研究和探讨。

![](images/img_009.jpg)

#### 复杂性

Llama 3.1 在无 MoE 标准 Transformer 架构、后训练 SFT + 拒绝采样 + DPO 的简化配置下，[在 54 天的训练过程中喜提了每 3 小时 1 次故障](https://link.juejin.cn?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fr8_6lseOkHyACvG8AuH-3g "https://mp.weixin.qq.com/s/r8_6lseOkHyACvG8AuH-3g")。小道消息说，其实 Meta 也尝试了 MoE，只是中道崩殂… 密集的故障多数由 GPU 引发，软件错误、网络故障、温度和电压都可能造成故障，Meta 甚至需要应对电力需求超出电网供给的问题。限制故障范围，及时从故障中恢复，非常考验团队的判断和快速应对能力。

关于电力供给问题，硅谷 101 在[视频](https://link.juejin.cn?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1ax4y1i7GK%2F "https://www.bilibili.com/video/BV1ax4y1i7GK/")和[播客](https://link.juejin.cn?target=https%3A%2F%2Fpodcasts.apple.com%2Fcn%2Fpodcast%2Fe149-%25E7%25A7%2591%25E6%258A%2580%25E5%25B7%25A8%25E5%25A4%25B4%25E4%25BB%25AC%25E5%25BC%2580%25E5%25A7%258B%25E6%258A%25A2%25E7%2594%25B5-%25E8%2581%258A%25E8%2581%258Aai%25E7%2594%25A8%25E7%2594%25B5%25E8%258D%2592%25E5%2592%258C%25E6%25A0%25B8%25E8%2581%259A%25E5%258F%2598%25E5%2588%259B%25E4%25B8%259A%25E7%2583%25AD%2Fid1498541229%3Fi%3D1000653987633 "https://podcasts.apple.com/cn/podcast/e149-%E7%A7%91%E6%8A%80%E5%B7%A8%E5%A4%B4%E4%BB%AC%E5%BC%80%E5%A7%8B%E6%8A%A2%E7%94%B5-%E8%81%8A%E8%81%8Aai%E7%94%A8%E7%94%B5%E8%8D%92%E5%92%8C%E6%A0%B8%E8%81%9A%E5%8F%98%E5%88%9B%E4%B8%9A%E7%83%AD/id1498541229?i=1000653987633")节目中都有深入讨论，修缮电网、保障供应、维持电价无论如何都超出了正常商业公司的经营范畴，或许强大的 AI 背后，还得有强大的国家。

### 0x11 Scale Down 与价格竞赛

如此累屋重架的体系想必烧钱吧，然而价格竞赛的风却席卷了全球：

日期

模型

版本

输入

输出

降幅

05.06

[DeepSeek](https://link.juejin.cn?target=https%3A%2F%2Fwww.deepseek.com%2Fzh "https://www.deepseek.com/zh")

DeepSeek - V2

0.001

0.002

N/A

05.11

[智谱](https://link.juejin.cn?target=https%3A%2F%2Fbigmodel.cn%2Fpricing "https://bigmodel.cn/pricing")

GLM3 - Turbo

0.001

0.001

80%

05.15

[豆包](https://link.juejin.cn?target=https%3A%2F%2Fwww.volcengine.com%2Fproduct%2Fdoubao "https://www.volcengine.com/product/doubao")

通用模型 pro-32k

0.0008

0.0008

N/A

05.21

[通义千问](https://link.juejin.cn?target=https%3A%2F%2Fhelp.aliyun.com%2Fzh%2Fmodel-studio%2Fproduct-overview%2Ftongyi-qianwen-series-models-price-adjustment "https://help.aliyun.com/zh/model-studio/product-overview/tongyi-qianwen-series-models-price-adjustment")

Qwen - Max

0.04

0.12

67%/0%

05.21

通义千问

Qwen - Plus

0.004

0.002

80%/90%

05.21

通义千问

Qwen - Long

0.0005

0.002

N/A

05.21

文心一言

ERNIE - Speed

**0**

**0**

**∞**

05.21

文心一言

ERNIE - Lite

**0**

**0**

**∞**

05.22

[讯飞星火](https://link.juejin.cn?target=https%3A%2F%2Fxinghuo.xfyun.cn%2Fsparkapi%23price "https://xinghuo.xfyun.cn/sparkapi#price")

Spark - Lite

**0**

**0**

**∞**

05.22

讯飞星火

Spark3.5 - Max

0.021 ~ 0.03

0.021 ~ 0.03

?

05.22

[腾讯混元](https://link.juejin.cn?target=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Fhunyuan "https://cloud.tencent.com/product/hunyuan")

lite

**0**

**0**

**∞**

05.22

腾讯混元

standard

0.0045

0.005

55%/45%

05.22

腾讯混元

standard - 256k

0.015

0.06

87.5%/50%

05.22

腾讯混元

pro

0.03

0.1

70%/0%

08.02

[谷歌](https://link.juejin.cn?target=https%3A%2F%2Fai.google.dev%2Fpricing%3Fhl%3Dzh-cn "https://ai.google.dev/pricing?hl=zh-cn")

Gemini Flash

0.0025

> [内容过长，已截断]
