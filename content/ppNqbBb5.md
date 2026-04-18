# 做AI产品两年，我得出的实操经验

> 公众号: 多睡觉多学习就好咯
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s/HsFhXMLejsQWjTghUYdKFA

---
前段时间我去QCon北京全球软件大会分享了一个专题：

**AI****时代的新范式：如何构建****AI****产品？**

**观众反响特别好，想着要不把分享的内容公开出来，所以整理了这篇文章。本篇内容是对我过去两年时间，做了无数个AI产品demo的一个阶段性的总结，主要聚焦这三个方面的经验：**

**

**为什么AI产品这么难做？**

**提示词工程被极大低估**

**AI 产品团队如何构建**

**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwdcHVkJvDBmmvxsoxacDzvOvgUKrHx1iaptfoIL6UIibnicNwYBd7TumEA/640?wx_fmt=jpeg&from=appmsg#imgIndex=0)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw4kfTXhPLk2qSQxSe2DI8RLafGLs75LCybh36fDOCVM61aRSNrCnPVA/640?wx_fmt=png&from=appmsg#imgIndex=1)

谨小认知，仅供参考。写给所有AI路上的朋友们。

* * *

**简单自我介绍，我是ONE2X AI全栈工程师，AI视频剪辑效果负责人。负责ONE2X的Medeo（AI视频剪辑工具）的视频自动化制作工作流全流程搭建、工具产品的设计及创新AI应用场景探索。**

22年11月GPT刚出后，就开始尝试做各种各样的AI产品，23年年中毕设做的是AI情感陪伴、暑假在做企业知识库Chatbot智能客服、23年年底到24年年中在大厂做低代码编排AI工具和智能医疗、24年年中到现在在AI创业工作做AI自动剪辑。途中还做过大大小小的project，包括AI写遗嘱、AI Agent做动画等等……也算是积累了很多实操经验了。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw50icReO8nQROTEMoiaLY86hqJibicyAoktpdEWd1lS6QIQeLvd1ny6zibWA/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

✨一、**为什么AI产品这么难做？**

**让我们轻松的聊聊AI与产品**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwn7BNR29U9cxv7YeM1WVDrdXlcKJUV8V4SAj11dhop9LR2v4lEibKAmg/640?wx_fmt=png&from=appmsg#imgIndex=3)

认知截止到20250411

**A Joke：先从一个笑话开始，你能看懂吗？**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwS9eENXYPWLfQC528DYRzGdN740YXU77vBrH7jzljXEFib1Ld70jsumQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

**如果你知道每一条背后的原因，那么恭喜你上道了！**

**所以为什么AI产品这么难做？**

AI时代的产品和传统的产品不一样的是什么？

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwnkNJJicSPiaHAgvtRFbUgLrja7rs2x3uNju7GugQur8ufxL9gkby2Utw/640?wx_fmt=png&from=appmsg#imgIndex=5)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwnFTicxuenUBFEOahsV1mmfBzvdmb1gbQiaBef07e4728sKHFUf846TgA/640?wx_fmt=png&from=appmsg#imgIndex=6)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwyd5H8ptbSDWjqiaZo47kMFf1hJL9PjLpR1dycNrwYtv3vpWeiaRVbAww/640?wx_fmt=png&from=appmsg#imgIndex=7)

**基础流程是什么？**

**所有流程可枚举全部已知**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwjmzu353wFEUQngnZn3JKQqOboNiaaDcFicCibQpCj2ghM40MYUXcEmQmw/640?wx_fmt=jpeg#imgIndex=8)

-   流程的自动化的定义是什么，什么流程可以被SOP化，就可以做成产品。那AI产品，首先肯定是产品，其次它还会完成**以前人类才能完成的某种任务。**这个任务如果需要AI完成，那就发生了**范式转移**


![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwxAD4IdXaoC7wsX6Yt0OT0584icEuIFdicaVpjT1NHMnseIjic7l8ZJArg/640?wx_fmt=png&from=appmsg#imgIndex=9)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwO0rMNIPVAeaOojCTzdrQd2op8mhTtAicLZaWq0rQVhRMdIibZce6wJPw/640?wx_fmt=png&from=appmsg#imgIndex=10)

**你得帮用户做出来这个任务。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwS9Sbo0osDnpLVTDEC53ZtFSvTyc9ozuC0asbeI8LsgnwV8pF5GSlSw/640?wx_fmt=png&from=appmsg#imgIndex=11)

**举个例子，Cursor**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwRCVWLMNn9fUFicIcEmAZlf4ZRjv6D43E95O5LryhSNRg7MzzGaYElPQ/640?wx_fmt=png&from=appmsg#imgIndex=12)

**Cursor是我认为2024年最好的AI产品**

**它解决了三端关系。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw23RDK1lrr7WCkeGa7kcsgWmeiaoncjK00ago5EJ9C5ZJiaP5rF8dzGuw/640?wx_fmt=png&from=appmsg#imgIndex=13)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwfOExFLK5GLVyp2Y9XibC5QVAf3ZPvlfw1tRygZaYRKfzo8kDxIGNFGQ/640?wx_fmt=png&from=appmsg#imgIndex=14)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwGASpxXWxrOoNbXiaicB7B7RX6ibe5TIaavHY4riaJWSXpPJwp01lhaxWaw/640?wx_fmt=jpeg#imgIndex=15)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw2lgB9wibullLsCBL0yyGiakppFaCjIG3iao4fe5qeUicfn1eCxwib9Zxf2Q/640?wx_fmt=png&from=appmsg#imgIndex=16)

**Cursor Team解决了如下问题：**

-   **任务分级：****根据给AI的执行权限不同的不同可控颗粒度的任务**
-   **帮用户完成了任务：****每个任务/功能在用户还没来之前就已知该任务如何完成（Coding，且无论语言，无论项目）**
-   **交互方式：****每个任务/功能与人协同的人机交互方式**
-

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwBeX6JkSAaU2exnSb8KGZBDVTE4D4V4OrAice84btHevwJtqddPLOibyQ/640?wx_fmt=png&from=appmsg#imgIndex=17)

* * *

**✨二、提示词工程被极大低估**

**认知一：Prompt也是代码，所以要测试。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwKDBTY8lkOib6JtqS9UcfP2wHXWZiax0kMiaiahhRb5qfBTMzkSxiaIrOzBg/640?wx_fmt=png&from=appmsg#imgIndex=18)

尊重prompt，同代码享受同等权利，需要git diff

需要对prompt单独进行版本管理

**Prompt也是代码，但有区别？**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwFpuEGkdG2u3cjKwEuwYTL4R1zyGK9WDdB5ZuUiangWGMUMLmguGIJRQ/640?wx_fmt=png&from=appmsg#imgIndex=19)

LLM和函数很类似，它们都是实现某个“计算”的节点。

但它能提供比传统函数能做的更多的事情，提供“智慧类型”计算。

它可以接受非结构化的数据，经过推理，输出非结构化/结构化的数据。

**Prompt也是代码，如何测试……？**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwU9zH1wAz3Mo4bAMe8hzp9Ygz0BDwDOGxCicaCwnJhB2XltOgXPZS44w/640?wx_fmt=png&from=appmsg#imgIndex=20)

函数，我们在运行前，通过IDE或者单测即可完成**功能正确性校验**。

LLM怎么测试呢？

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwn4zavh5mdSSvY5Yaq17ib12wuWEribBks5icU3h0VkJicSNmIDRreCck9w/640?wx_fmt=png&from=appmsg#imgIndex=21)

如果你只是让它完成传统函数的任务，也很好测试，可以使用function call 加上单测。

比如加法任务，只让它输出结果，可以做**正确性校验**。

**但大概率你让LLM做的事情是****非结构化的****。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw5xrqRnJ1mibaapcu7qvTbcULlnpI73QeHxylEIeibOiblsdw6VFoCtvcw/640?wx_fmt=png&from=appmsg#imgIndex=22)

**所以Prompt的好坏怎么测？**

**一：格式正确性**

使用function call / Json mode确保输出**格式不出错**

**任何****LLM****相关的调用，都使用****pydantic****严格校验**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwn8kmMcjbdqQLibLB7IriaDx4Hh8pc0yqLAWk6o41xoichPvOnRDF21VQA/640?wx_fmt=png&from=appmsg#imgIndex=23)

**二：功能****Baseline**

输出内容，通过batch evaluation进行校验。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwU7qz5ecEjskWZ2yUdd9EpCqibWJBwBkEgBmMoAfutrtUunLx6a0ynJw/640?wx_fmt=png&from=appmsg#imgIndex=24)

**三：人工评测结果**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwypBVSh4W8sUvD3NNJypBqibQrkWYHiaviaYDe1sqUXd5LKvfJMSZ7jOtQ/640?wx_fmt=png&from=appmsg#imgIndex=25)

模型的上限，还是取决于人对于结果的要求有多高。

Baseline只是保证功能正常运行，上限在于“人”

**四：放权**

模型可能比你想象中的更强，不要限制它的思考方向，思考内容，knowhow，把prompt当成一种容器，你只是为模型提供必要的信息，而不是教它如何思考。

**总结一下，Prompt也是代码，所以要测试。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwakeOzEHPgxGBHGLDVUmdb3tJehHAGrSE0sPmOHSjvZjVQu7dYVQUbw/640?wx_fmt=png&from=appmsg#imgIndex=26)

**认知二：AI产品就是基于“给模型提供上下文”出发开始的**

首先，不要发现模型做不对任务，就觉得它有问题。接下来以Text2SQL为例。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwpPnG8OU0WpdQ5IZsucZlo4kgHXo2ESJRFHJPZWHczibE9SDhumiaYLCw/640?wx_fmt=png&from=appmsg#imgIndex=27)

做产品的人需要知道这个任务完成本身需要什么上下文，并且努力为模型提供出来。你并不需要那么多Prompt技巧，而是努力为模型提供更多的“必要信息”。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwGX44v9waxHnumYoPZ7jhW8FKECtGDOAsic1YOpTeib7icHuJUKz2Oua3A/640?wx_fmt=png&from=appmsg#imgIndex=28)

你会发现跟人很像。把它当成实习生，你也需要给实习生上下文。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwTicOVjGFVp3RFu8S19ZwV2TLWz7nYD2MfWm1kVwV5xYlkx50kbt5iclg/640?wx_fmt=png&from=appmsg#imgIndex=29)

对于大部分业务场景而言，你不需要“神级Prompt”（如下图），你需要的是对业务的熟悉程度。把业务knowhow沉淀成Prompt。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw9W7Kia1U4Yh9zs0ePrUqlIDbxVw5cAxqNu98jMJSorS35tDFxrheKsA/640?wx_fmt=png&from=appmsg#imgIndex=30)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwq172FAk8zmnOURiba2gSicFa7TXY5MZgvwia5dnMtxaiaud2VGaN2ntkQA/640?wx_fmt=png&from=appmsg#imgIndex=31)

一件事情上下文到底是啥？寻找root变量的过程。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwf9OlV7OMrfcBhF88wxribWMvm6wKBvJ9ibUTYm8Iqq4pQrQpHbmgTaLw/640?wx_fmt=png&from=appmsg#imgIndex=32)

**认知三：如何面向未来进行设计，避免被模型更新所冲击？**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwL2COzjicFFIo5ZhMC9BLU9EJAnnlu3JZCGOBKbgloCgLVBToH87oIMQ/640?wx_fmt=png&from=appmsg#imgIndex=33)

Manus画的AI Model Timeline

模型每天都在更新，我怎么设计提示词和架构？

模型更新之后，提示词会不会失效了呢？

每个模型有什么不同的脾性？

模型越来越智能，未来还需要复杂的提示词吗？

……

**Slow Down，别焦虑。**

**打不过就加入：**用最好的模型的API创建应用。除非自己顺手能训练模型。

**Flow Engineer****：**什么时候拆分任务，什么时候合并任务？

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwbC3oXku7h6bXNXYU8Dam5kE6libjLfqkgPFicldjjHxH5MtAx84XFwxg/640?wx_fmt=png&from=appmsg#imgIndex=34)

**我的体感（纯经验，没有数据支撑，knowledge截至20250321）**

**如果不知道用啥，就先试试Claude**

**通用类型任务：****Claude-3.5-Sonnet / Claude-3.7-Sonnet**

**强推理任务：****Claude / Gemini 2.5 Pro**

**中文语言任务：****DeepSeek**

**图片多模态任务：****Claude / Gemini /** **阶跃**

**视频多模态任务：****Gemini**

**简单任务：****Gemini Flash** **（省钱）**

**中文****B****端本地任务：****Qwen**

**可能的Bad Case:**

**DeepSeek****指令遵循弱**

**Gemini flash****幻觉严重**

**……**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwRsMdicVJQBlicc1DGj6p1L2UMRuxwHbxST886otXDosicWcqjJOXEUuWg/640?wx_fmt=png&from=appmsg#imgIndex=35)

**当然GPT4o生图很好！**

**Flow Engineer**

“Flow Engineering” 是一个最近越来越受欢迎的术语。它第一次被提及作为术语是在 CodiumAI 关于 AlphaCodium 的论文中，他们在论文中使用流工程来产生关于编码问题的最新结果。

推荐看一遍**Langgraph**的ipynb examples

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw8FicdyKGibAKtiaALQmneyreablcWSB4pxNZYSdtgt48BIsyQwXtJ8zYA/640?wx_fmt=png&from=appmsg#imgIndex=36)

**Flow强调的是用整体系统设计去完成任务**

多节点设计，每个节点去实现单一任务。

单一任务简单可靠，一定在LLM可实现范围之内。

当一个任务太难的时候，就拆成两个任务去做。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwugGPiauEibZsLl2fVj7WHxovMpNWxcWmKs4yJeZia8AS96OSNjOYNKgNw/640?wx_fmt=png&from=appmsg#imgIndex=37)

**好像有点像Dify/Coze的意思？**

**对，但不全对。不要忘了传统代码的能效。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwP8BqS11iaNYrUpfNBmlQ2kGMJeSvaPVjxibotACibUoibgKxHoQbc7WveA/640?wx_fmt=png&from=appmsg#imgIndex=38)

你并不需要全部节点都是LLM，你也可以组合function和LLM。

所以推荐使用Dify/Coze验证原型，写代码用LangGraph搭建实际应用。

**当模型更新后，就合并任务。**

在设计Flow的时候，不需要拘泥于优化一个节点的LLM Prompt。

因为模型推理能力不够，大概率三个月后就够了。不需要过度设计。

用几个小的task拆解后完成任务，等模型更新后把整个大任务交给新的模型。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwM5qnEuUvLXdXvTUibCLG7dnRNNVseScosRhibQhx4vEEicqROkI75FBBw/640?wx_fmt=png&from=appmsg#imgIndex=39)

**总结一下，Prompt Engineer的认知**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw4kfTXhPLk2qSQxSe2DI8RLafGLs75LCybh36fDOCVM61aRSNrCnPVA/640?wx_fmt=png&from=appmsg#imgIndex=40)

* * *

**✨三、AI 产品团队如何构建**

**认知一，首先你得成为“创作者”**

Cursor很厉害，也最先落地：

-   懂AI的本来就是程序员。团队懂Coding。

-   团队知道如何拆解任务，每一个任务如何写Prompt的knowhow，团队很清楚。

-   模型Coding能力已经阶跃（Claude3.5） 文本模态Coding任务是最擅长的。


**但还有如此多的业务场景，等着创造。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwDSWlpVr5YrDXBA7BGURXWr2l9SzvmVpoKGU53OkEfKvPsJRicSbibIWQ/640?wx_fmt=png&from=appmsg#imgIndex=41)

**认知二，快速做出Demo最重要**

AI产品最后长成什么样子，已经是无人定义清楚的事情了。

只有当把所有的要素及其，做出一个demo，你才知道这是什么感觉的产品。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw2zA9YicTysNLlYveeXibPKiaOcGLTAcVecHpyrZgURfaaHibCFgdA5zr9g/640?wx_fmt=png&from=appmsg#imgIndex=42)

我做的大大小小的demo

**认知三，产品/开发的界限模糊**

**以前的开发模式，是产品、研发。现在可能变成了一个紧密的团队一起调prompt。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw6JqB1wEwlicvA0H5Uwa3OfLNcolI0tBWnH5ibTgP0DyCvuLXzmPYA3Hw/640?wx_fmt=png&from=appmsg#imgIndex=43)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw58F8iadbN8IgA7W5V6s2P2Y6iaIlMpSoR2ZpmZVhw3eqDyWZOicoQyr4A/640?wx_fmt=png&from=appmsg#imgIndex=44)

这是我在公司内部做的后台，支持任何人追溯每次LLM调用，并且重新调试prompt。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwFpf4Vbfs2zcqsQUA6QyofLd4eHHj9NC89w74eSQRd3gYibufCNgYtiaw/640?wx_fmt=png&from=appmsg#imgIndex=45)

**最好是产品****/****全栈能自己调试****prompt****。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuw8qibZMDulWA151Vo3JPhjMghdsBGsCTQHHFqpPfapUUdKzgccVrRm7g/640?wx_fmt=png&from=appmsg#imgIndex=46)

AI产品需要紧密配合的团队，一起设计架构。

Prompt需要沟通能力，业务能力。代码需要研发能力。

Prompt + 代码是团队之间才能做的事情。

一起创作。

* * *

写在最后

**我们正在见证新范式的出现，很幸运。**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuwibkGfZVKmUUKHbPNL5ESUmzkeouu7ReF1BJaZhxn4zzfNW4JcJ6qklg/640?wx_fmt=png&from=appmsg#imgIndex=47)

有了AI，才有了年轻人的机会，所以我非常感激能在这个时代能有这么多有意思的事情。

谨小认知，仅供参考。

认知截止到20250411

**我正在做的AI产品，也即将发布。**

**AI视频剪辑工具**

**尽情期待！**

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/WK3SUWJYdwQkffXyOXSvMRDREnyO8fuweRQLspF2UVLibOM1zlTQic00egnr3zg8uRvgvrmF2tPibzylibkujArD0w/640?wx_fmt=png&from=appmsg#imgIndex=48)

如果喜欢我的内容的话，别忘了点赞转发！