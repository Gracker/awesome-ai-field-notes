---
id: "7446850269666610935"
cubox_url: https://cubox.pro/web/card/7446850269666610935
url: https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484082&idx=1&sn=aac7ea3868e31bcc3d47e58724adeb19&chksm=97b2ecf5f127fbbbbf70455f1b5d00c136d28bf50cdfb275cdf722989d3bc36a669ebe150f66&mpshare=1&scene=1&srcid=0423Ff0YBFnoeDY8moFsXq8X&sharer_shareinfo=df63fd28b814cbc1b9dfff82a70ea4a1&sharer_shareinfo_first=df63fd28b814cbc1b9dfff82a70ea4a1
tags: []

---
# Harness 层怎么自我进化？来自斯坦福大学和 MIT 的一项新研究

Harness 层怎么自我进化？来自斯坦福大学和 MIT 的一项新研究《Meta-Harness: End-to-End Optimization of Model Harnesses》。它讨论的已经不是人类应该怎样手工编写 Harness，是能不能让 Harness 本身进入一种自动化演进的过程。

[Read in Cubox](https://cubox.pro/web/card/7446850269666610935)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484082&idx=1&sn=aac7ea3868e31bcc3d47e58724adeb19&chksm=97b2ecf5f127fbbbbf70455f1b5d00c136d28bf50cdfb275cdf722989d3bc36a669ebe150f66&mpshare=1&scene=1&srcid=0423Ff0YBFnoeDY8moFsXq8X&sharer_shareinfo=df63fd28b814cbc1b9dfff82a70ea4a1&sharer_shareinfo_first=df63fd28b814cbc1b9dfff82a70ea4a1)  

---

![](https://image.cubox.pro/cardImg/5oub73los8rfe6yz66lygabl81r2wlmk06sh9y5w4q3pd2cey3?imageMogr2/quality/90/ignore-error/1)

**Liz的AI冰美式**

冷静理智的AI洞察，一杯 Liz 的冰美式，陪你清醒看世界。"冰美式"没有奶，没有糖，干净利落，不加修饰。也希望我的内容，像一杯冰美式一样，让你在信息过载中提神醒脑。不浓烈，不甜腻，但够纯粹，也够提神。

23篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FLumicyKo9fCuZUcuXkRaKYWHbiaOicXqtAicVKiaKXEGwIby3OBRzBiaWrjSE6rP9vGqFHyibOc9kK2zqbxYyOKoicrSmA%2F640%3Fwx_fmt%3Dgif%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwebp%23imgIndex%3D0)

喜欢就关注我哦～

最近这段时间，大家都在热烈讨论一个概念：什么是 Harness 以及到底该怎么构建一个好的 Harness。此前我也写过一篇综述，专门梳理 OpenAI、Anthropic 和 LangChain 工程博客中提到的 Harness 系统：[AI Agent 工程化实践指南：如何构建可靠的 Harness 系统](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484077&idx=1&sn=ee3fd75a3799b07df9c08fcbda2b21e4&scene=21#wechat_redirect)。正好这两天，随着 Claude Code 内部源码因打包失误被意外暴露引发广泛关注，很多人也第一次更直观地看到，顶级 Agent 之所以能在榜单上持续领先，背后往往并不只是模型本身，而是一整套设计精密的 Harness 在支撑。

从功能上看，Harness 可以理解为一组负责状态管理与执行编排的程序。它要决定什么时候去检索外部信息，怎样组织和拼接上下文，什么时候触发工具调用，以及如何管理多轮对话中的记忆。也正因为如此，对于同一个基座模型来说，外围 Harness 的设计方式不同，最终表现可能会出现非常明显的差异。即便模型本身不变，在相同评测基准上，性能差距也可能达到数倍。

这两天我又看到斯坦福大学和 MIT 的一项新研究《Meta-Harness: End-to-End Optimization of Model Harnesses》，觉得很值得分享。它讨论的已经不再是人类应该怎样手工编写 Harness，而是能不能让 Harness 本身进入一种自动化演进的过程。


现有自动化工具的局限：

被过度压缩的反馈

既然要实现自动化优化，很多人可能会首先想到近两年涌现的一批优秀的文本优化器（如 OPRO、TextGrad、AlphaEvolve 等）。它们在优化 Prompt 或单步逻辑时表现出色，但当被直接用于优化复杂的 Harness 时，往往会显得有些"水土不服"。

问题的核心在于反馈压缩（Feedback Compression）。

Harness 的执行通常是一个跨越长周期的过程。系统在第 50 步由于状态管理错误而陷入死循环，其根本原因可能在于第 1 步检索时写入了不恰当的上下文。但在传统的优化器框架中，几千步的运行轨迹往往被硬性压缩成一个单一的"标量分数"，或者仅仅是几百个 Token 的文本总结。丢失了关键的诊断上下文，系统就很难建立长距离的因果联系。

据统计，现有文本优化器在单步优化中能参考的上下文窗口，通常只有 100 到 30,000 个 Token。这对于诊断复杂的 Harness 错误来说远远不够。相比之下，Meta-Harness 单次评估产生的诊断信息最高可达 1,000 万个 Token。论文将这种差距概括为接近三个数量级。

更深层的问题在于：Harness 的决策具有长时滞效应。一个关于"何时检索、显示什么信息"的选择，可能在许多推理步骤之后才显现其影响。压缩后的反馈恰恰删除了追踪这些因果链条所需的线索。这不是现有优化器的疏忽，而是面对海量信息时的务实妥协------而这种妥协，恰好牺牲了 Harness 优化最需要的东西。


Meta-Harness 的破局思路：

像人类工程师一样"修 Bug"

为了打破这种信息瓶颈，Meta-Harness 放弃了将所有反馈打包塞入一段超长 Prompt 的做法，而是将一个完整的文件系统（Filesystem）开放给了作为提议者（Proposer）的代码代理。

具体的运作方式如下：

每一次评估完一个 Harness（在实验中即一个独立的 Python 脚本），系统就会在文件系统中生成一个新目录。这个目录里原封不动地保存着该方案的 Python 源代码、最终的评估分数，以及极其详尽的执行日志（Execution Traces）------详细记录了基座模型当时看到了什么提示词、调用了什么工具、最后输出了什么。

在进入下一轮迭代时，作为优化器的代码 Agent（实验中使用的是 Claude Code with Opus-4.6）会使用标准的终端命令（比如 grep 和 cat）去翻阅这些历史文件夹。它不仅看分数更重要的是通过阅读底层的执行路径去推理失败的原因。在最 demanding 的设置中，proposer 每轮迭代读取文件数的中位数就有 82 个，同时会参考 20 多个历史候选。学习和思考完毕后，这个 Agent 会亲自编写一段全新的 Python 代码，保存为新的脚本文件，提交给系统作为下一代的 Harness 去跑测试。

这就和人类程序员日常的工作流如出一辙：写代码 → 查报错日志 → 推理 Bug 根因 → 修改逻辑 → 重新编译测试。

这个设计还有一个重要的隐含优势：代码空间本身提供了天然的正则化偏差。Coding model 倾向于生成连贯的算法而非脆弱的硬编码解决方案，这使得搜索自然偏向可复用的上下文管理策略，而非过拟合到特定测试集的技巧。


真实的 Debug 故事：

Agent 的因果推理与环境快照

理论上的设计固然优雅，但真正令人信服的是论文附录中记录的真实搜索轨迹。研究人员让 Meta-Harness 去优化一个极其困难的命令行智能体评测基准 TerminalBench-2，生动展示了系统是如何自动排错的。

在早期版本中，系统存在一个严重的"终端标记泄露与无序循环"问题。底层终端环境为了区分命令执行状态会输出一些控制字符，但由于上下文没处理好，这些底层标记泄露到了大模型的观测窗口里，导致模型陷入死循环。

Agent 在阅读报错日志后发现了这个问题，提出了一套结构性修复（剥离冗余标记、强制打断循环），但同时也顺手修改了 Prompt 模板，加入了一段严厉的清理指令。结果，这两次修改都导致了性能的严重倒退。

如果是传统优化器，可能会直接放弃这个方向。但 Meta-Harness 仔细比对了失败的轨迹记录，得出了极其清晰的因果诊断：
> "前两次的性能倒退，是因为它们都共享了有害的 Prompt 修改......结构性的 Bug 修复其实是有效的，它只是被错误的 Prompt 修改给混淆（Confounded）了。我现在的策略是：仅仅隔离出结构性修复（恢复原始 Prompt），再测一次。"

它成功验证了这个假设。在经历了后续几次修复控制流逻辑的失败尝试后，Agent 总结出修改 Prompt 和补全控制流的风险太高，于是转变思路，采用了一种极为安全的纯增量式修改------编写了一段环境快照（Environment Bootstrapping）代码：在系统开始执行任务前，先静默运行一段 Shell 命令，把工作目录、/app 内容、可用编程语言及其版本、包管理器、可用内存等环境信息打包成一段快照，塞进最初的 Prompt 中。

仅仅增加了约 80 行代码，就使得系统在 Claude Haiku 4.5 上取得了 37.6% 的通过率，位列该基座代理的第一名。这个过程本身就是一种因果推理的实践------而这正是传统优化器完全无法支持的能力。


复杂任务中的策略涌现：

四路路由检索

除了命令行环境，Meta-Harness 在推理任务中也展现出了令人赞叹的代码架构演进能力。

在利用庞大语料库解答 IMO（国际奥林匹克数学竞赛）级别难题的实验中，传统的死板检索往往效果不佳。这里有一个非常精妙的细节：Meta-Harness 并没有抛弃旧技术，也没有引入新的混合检索，它底层依然完全基于纯文本的 BM25 算法。但它通过编写灵活的 Harness 代码，把单一的检索重构成了一套极其聪明的业务逻辑。

在迭代中，Agent 自主编写了一个"四路路由器"（Four-route Router）的 Python 程序。代码会先通过正则表达式和关键词提取，把数学问题分发到"组合数学"、"几何"、"数论"和"默认代数"四个不同的处理通道中。虽然每个通道底层调用的都是 BM25，但 Agent 为它们编写了完全不同的后处理逻辑：

* 遇到几何题，系统发现难度重排序往往会弄巧成拙，因此代码直接把最匹配的 2 个原始 BM25 结果结构化地塞给模型；

* 遇到组合数学，代码则要求先检索 20 个结果，进行去重，然后严格按照难度重新排序，最后只保留最顶尖的 3 个。

这一套由 AI 自主编写的业务路由逻辑，让原本死板的 BM25 焕发了新生，也让 5 个评测模型的平均准确率，相比 no retriever 提升了 4.7 个百分点。其中有 4 个模型，是搜索阶段从未见过的。这个结果也让我觉得，Meta-Harness 发现的可能不只是某个 benchmark 上的小技巧，而是某些更通用的 Harness 设计原则。论文在另一组文本分类的 OOD 评估里，也观察到了类似现象：在 9 个此前未见的数据集上，Meta-Harness 的平均准确率比 ACE 高出 2.9 个百分点。

总结：为技术人带来的长期思考

《Meta-Harness》这篇论文清晰地指出了大语言模型应用开发的一个趋势：在代码空间（Code-space）中进行自由形式的全局优化，远比在有限的模板里填空要强大得多。

对于 AI 应用工程师而言，这项研究是一个重要的信号。如果顺着这篇论文继续往前推，我自己的一个判断是，未来工程师未必还要把大量时间耗费在手动编写检索截断规则，或者反复斟酌 Prompt 里的细节。更关键的，可能会变成如何定义评估指标、准备清晰的工具边界，以及给 AI 圈定一个安全、可搜索、可回溯的探索环境。剩下的长尾报错排查、因果推演与架构重构，将越来越多地交给系统在后台通过阅读大量文件与执行日志来自我迭代。

抛开过度夸张的技术包装，Meta-Harness 展现的是工程优化的朴素本质：给予系统足够全面且原始的观察视角，让改进在持续的试错与归因中自然发生。

**Reference**

Meta-Harness: End-to-End Optimization of Model Harnesses（https://arxiv.org/html/2603.28052v1）



