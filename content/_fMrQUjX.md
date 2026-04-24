---
id: "7446850313253816551"
cubox_url: https://cubox.pro/web/card/7446850313253816551
url: https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484077&idx=1&sn=ee3fd75a3799b07df9c08fcbda2b21e4&chksm=972981b6636211d172b8caed0a982796a0f7d39c477e1c9991bb9b717db4548df20aa22cd114&mpshare=1&scene=1&srcid=0423loGxXEgvr9SaWycvYrHQ&sharer_shareinfo=688d8fb09649fbaef375238b86ccb1fb&sharer_shareinfo_first=688d8fb09649fbaef375238b86ccb1fb
tags: []

---
# AI Agent 工程化实践指南：如何构建可靠的 Harness 系统

Harness的价值不只是在帮助我们总结已有经验，也在提醒我们，AI 时代很多技术工作的重心，正在从单点能力转向对整体系统的组织、约束和协同。

[Read in Cubox](https://cubox.pro/web/card/7446850313253816551)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484077&idx=1&sn=ee3fd75a3799b07df9c08fcbda2b21e4&chksm=972981b6636211d172b8caed0a982796a0f7d39c477e1c9991bb9b717db4548df20aa22cd114&mpshare=1&scene=1&srcid=0423loGxXEgvr9SaWycvYrHQ&sharer_shareinfo=688d8fb09649fbaef375238b86ccb1fb&sharer_shareinfo_first=688d8fb09649fbaef375238b86ccb1fb)  

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


最近很多人都在讨论 Harness。也有人会觉得，这是不是又一次"新瓶装旧酒"。

这种反应其实很正常。每当一个新概念出现，很多人第一反应往往都是先去问：它和原来那些东西到底有什么不同？会不会只是把已有的方法重新换了个名字。这种谨慎我很能理解，毕竟在一个新术语不断冒出来的领域里，先保留判断，本来就是一种必要的敏感度。

虽然 Harness 是一个新词，但它里面包含的内容，比如 Prompt 工程化、Context 管理、工具系统设计、工作流编排，其实一直都是我们在关注和实践的，这些东西本身并不新。对我来说，它的意义还在于，它把一些原本已经隐约存在的变化更清楚地说了出来。之前我也在小红书上分享过，AI 时代技术人员需要 focus 的重点，可能已经在发生转移，只是当时还没有一个特别合适的词去概括。现在回头看，Harness 某种程度上正好把这些分散的实践和判断收拢成了一个更完整的框架。它的价值不只是在帮助我们总结已有经验，也在提醒我们，AI 时代很多技术工作的重心，正在从单点能力转向对整体系统的组织、约束和协同。

所以，我们真正应该关注的，不是去争论一个概念是否"新"，而是去理解它是否真的有解释力和指导价值。如果你是带着这种疑虑进来的，我希望接下来的内容能够回答这个问题。


Harness Engineering 是什么

## 从"让它生成"到"让它完成"

当模型主要被当作回答工具使用时，大家往往更关注输出质量本身；但当模型开始真正作为 Agent 持续执行任务，工程重心就会明显转向运行环境、反馈机制和执行约束的设计。

举个例子，在比较模型的 Coding 能力时，人们往往只在乎它是否写出了正确的代码。但如果是一个 coding agent，这显然还不够。因为就算它把代码写出来了，你也不知道代码有没有跑起来，测试有没有通过，功能有没有真正实现。所以，当模型从问答工具变成 Agent，工程重心也会随之变化。问题不再只是"它能不能生成"，而是"怎样设计一个系统，让它真的完成任务，并且能够验证结果"。这正是 Harness Engineering 出现的背景。

## 重新定义"评估"

理解 Harness Engineering 的一个关键入口，是重新理解什么是"评估"。

传统上，我们评估一个模型，往往是给它一个任务，然后看输出质量。这种方式默认了一件事：模型的表现可以被当作一种相对独立的内在能力来测量。

但到了 agent 场景里，这个前提开始松动。因为当模型真正去执行任务时，影响结果的已经不只是模型本身，还包括上下文怎么组织、工具怎么接入、约束怎么设置、错误怎么被发现和修正。换句话说，我们实际测到的，往往是模型和 agent harness 的组合表现。至于 evaluation harness，更接近运行评测本身的基础设施，这里先不展开。

LangChain 的实验很能说明问题。只调整 harness 设计，不换模型，就能让 Deep Agents 在 Terminal Bench 2.0 上的表现从 52.8 提升到 66.5。这说明在很多真实任务里，系统设计对 Agent 表现的影响，已经不只是辅助项，而是结果的一部分。

在这里我会联想到强化学习。不是因为两者可以直接等同，而是因为它们都在说明一件事：一个智能体最终能表现到什么程度，不只取决于它自身的能力边界，也取决于外部系统给它提供了什么样的环境、反馈机制和执行约束。

Harness 的四个维度

我自己会把 Harness Engineering 暂时拆成四个彼此关联的工程维度来看：Prompt、Context、Tools、Workflow。

这不是某种严格的官方分类，而是因为一个 agent 真正开始做事时，工程上绕不开的其实就是这几类问题：

* Prompt：你到底怎么把任务交代给它

* Context：你到底让它看到哪些信息

* Tools：你到底给了它什么行动和验证能力

* Workflow：你到底怎么组织它把一件事持续做完

这四者并不是彼此割裂的。

Prompt 决定任务如何被表达，Context 决定模型能基于什么信息做判断，Tools 决定它能做什么、怎么验证自己做得对不对，Workflow 则决定这些能力如何被串起来，变成一个真正能跑下去的任务系统。

所以如果要理解 Harness Engineering，我觉得与其把它看成某个单点技巧，不如把它看成一整套围绕"如何让 agent 真正完成任务"展开的系统设计。

## Prompt 工程化：不是塞得越多越好

提到 Harness，很多人的第一反应是写一个无所不包的 System Prompt，把所有规则、约束、注意事项全都塞进去。这是一种直观的做法，但往往适得其反。OpenAI 在一篇关于 Harness Engineering 的工程复盘里，就提到过类似的问题。他们尝试把所有规则都堆进一个大的 AGENTS.md，结果发现这会造成上下文污染，文档本身越来越臃肿，Agent 反而抓不住重点。

后来他们调整为"渐进式披露"的策略：AGENTS.md 变成一个入口目录，详细的设计文档、架构决策和变更历史放到 docs/ 目录下，Agent 需要时再去查阅。这本质上不是在管理文档，而是在设计 Agent 的信息视野------什么时候该看到什么，什么不应该一上来就压进上下文里。

这会让人联想到强化学习里一个很常见的问题：智能体到底应该看到什么。对一个智能体来说，不是看得越多越好。关键信息和噪声混在一起，反而可能让决策变差。

**核心原则：Prompt 工程化不是要把所有信息都塞进去，而是要设计一套按需暴露的信息结构。**

## Context 工程化：状态外置与跨 Session 延续

当 Agent 处理的任务变长，一个根本性的问题浮现出来：上下文窗口会耗尽。长任务中，Agent 面临着"失忆"和"信息过载"的双重挑战。

Anthropic 在处理长任务时，提供了一种工程化的解决思路：不要继续往系统提示里塞更多规则，而是把状态从上下文窗口里搬出来，变成外部可恢复的工件。具体做法是：让一个初始化 Agent 先建立环境，生成状态文件，后面的 coding agent 每次启动时，先读取这些状态文件、查看 Git 日志、确认当前进度，然后只推进下一个优先级最高的任务。

另一个值得注意的现象是"Context Anxiety"------某些模型（尤其是 Sonnet 4.5）在接近上下文窗口上限时，会过早地开始收尾，即使任务尚未完成。这种行为背后是一种"我能处理多少"的隐含判断。Context Reset（清除整个上下文窗口并重新开始）可以解决这个问题，但代价是增加了编排复杂度和 token 开销。后来随着模型版本更新（如 Opus 4.6），这种行为大幅改善，Harness 设计也需要相应调整。

**核心原则：长任务不是靠"更强 Prompt"硬撑出来的，而是靠外部状态管理撑出来的。**

## Tools 工程化：扩展 Agent 的能力边界

Tools 是 Agent 与外部世界交互的桥梁。一个 Agent 能调用什么样的工具，直接决定了它能完成什么样的任务。这个维度涉及到几个关键问题：工具的选择与暴露、工具接口的设计、工具的组合与编排。

但有一个趋势比"让 Agent 能做什么"更值得关注------让 Agent 能看到自己的结果。很多 agent 不是不会做，而是太容易在"差不多可以了"这个地方提前停下来。写完代码就自信地宣布完成，但实际上页面没起来、底层逻辑没通、测试根本没跑。

解决这个问题的办法，是给 Agent 接入能够验证结果的工具：OpenAI 给 agent 接了 Chrome DevTools Protocol、本地日志和指标查询；Anthropic 用了 Puppeteer MCP；LangChain 用 trace analysis 去找 agent 的失败轨迹，再用 middleware 拦住它过早结束任务。

根本的问题在于 self-evaluation。很多时候，Agent 不是不会做，而是太容易对自己的结果过度宽容。所以在工程实践里，一个常见做法是把执行和评估拆给不同的 Agent：一个负责生成，另一个负责检查和反馈。

**核心原则：工具工程化的目标不仅是"让 Agent 能做什么"，更是"让 Agent 能看到自己的结果"，以及让独立的评估者来判断结果的质量。**

## Workflow 工程化：构建可靠的执行路径

Workflow 是 Harness 的顶层架构，它定义了 Agent 如何分解任务、如何组织执行步骤、如何处理异常和回退。

一个好的工作流设计需要考虑：任务分解------复杂任务需要拆分成 Agent 能处理的原子单元；执行顺序------哪些任务必须串行、哪些可以并行；检查点与恢复------每个关键步骤之后都应该有检查点；反馈回路------每个步骤的执行结果应该反馈给 Agent。

核心原则：工作流设计的目标不是让 Agent"自己看着办"，而是为它构建一条可靠的执行路径。

如果说前面四个维度讨论的，主要还是单个 Agent 的运行条件，那么当任务复杂度继续上升时，问题就会进一步变成：这些被设计好的能力，如何在多个 Agent 之间被分配、协调和连接。也正是在这里，Harness 开始从单体设计走向系统协作。

多 Agent 系统

当单个 Agent 的执行路径已经比较稳定之后，工程问题往往不会停在这里。更复杂的任务，通常需要多个 Agent 分工协作，而这时 Harness 要解决的，就不再只是单个 Agent 的执行质量，而是整个系统的协调成本。

Anthropic 有一个很受关注的实验：让 16 个并行运行的 Claude agent 协作，从零写出一个 Rust 实现的 C 编译器，而这个编译器最终能够编译 Linux 6.9 内核。整个项目跨越了接近 2000 次 Claude Code 会话，消耗约 2 万美元成本，最终生成了约 10 万行代码。

这个实验展示了多 Agent 系统的潜力，但也暴露了它面临的独特问题。最核心的问题是协调。一旦系统里不止一个 Agent，问题就不再只是"怎么让单个 Agent 更聪明"，而是"怎么让它们共享状态、避免冲突、减少重复劳动"。

Anthropic 的做法是建立最基础的协作秩序：在 current_tasks/ 下维护任务文件，让 Agent 在启动时先认领任务。这个机制的目的不是禁止任何人碰同一个文件，而是先建立最基本的"交通规则"。

### Generator-Evaluator 模式

除了任务协调，另一种值得关注的协作模式是 Generator-Evaluator。它的灵感来自生成对抗网络（GANs），将任务执行和任务评估分离成两个独立的 Agent。

Anthropic 在前端设计和全栈开发任务中验证了这种模式的有效性。在前端设计中，他们定义了四个评估维度：设计质量（整体感与氛围）、原创性（是否有定制化决策而非模板）、工艺（技术执行力）、功能性（可用性）。Evaluator Agent 持有 Playwright MCP，可以直接与运行中的页面交互、截图、研究实现细节，然后对每个维度打分并写出详细反馈。这些反馈作为下一轮迭代的输入。

在全栈开发中，这种模式映射到软件开发生命周期：代码审查和 QA 扮演着设计 Evaluator 的角色。Generator 负责构建，Evaluator 负责通过测试用例和功能验证来检验质量。他们设计了一个包含 Planner、Generator 和 Evaluator 的三 Agent 架构：Planner 将用户的简单 prompt 扩展为完整的产品规格；Generator 每次实现一个功能特性；Evaluator 使用 Playwright MCP 点击运行中的应用，测试 UI 特性、API 端点和数据库状态，然后对照既定的验收标准进行打分。

这种模式的成功关键在于：让独立的评估者来判断结果质量，比让同一个 Agent 既当运动员又当裁判更有效。调优 Evaluator 的方法是读取它的日志，找出它的判断与人类预期不一致的例子，然后更新 Evaluator 的 prompt 来解决这些问题。

核心原则：执行与评估的分离是处理复杂任务的有效策略，它解决了 Agent 自我评估时的"自信偏差"问题。

从工程实现上看，多 Agent 协作常见地可以粗略分成几类，例如串行模式、并行模式、层次模式，以及带有广播或路由特征的模式。每种模式都有其适用场景和设计考量。

评估与迭代

既然 Harness 如此重要，它本身也需要被评估。但评估 Harness 比评估模型更复杂，因为我们需要在"模型+Harness"的组合语境下衡量表现。

LangChain 展示了一种直接的评估思路：保持模型不变，只改 Harness，然后看性能指标的变化。他们用这种方法说明了一件很重要的事：只调整 harness 设计，也可能带来非常显著的提升。

评估 Harness 的常见维度包括：任务完成率、执行效率、结果质量、鲁棒性和可观测性。

基于评估结果，Harness 的迭代优化通常遵循以下思路：识别瓶颈、通过 trace 分析和失败模式分析找出 Agent 最常卡在哪里；针对性优化、针对识别出的瓶颈调整相应的 Harness 组件；A/B 测试、如果条件允许，可以同时运行多个 Harness 版本。

Anthropic 有一个非常具体的迭代案例，展示了如何逐步精简 Harness。最初的完整架构包含 Planner、Generator、Evaluator 三个 Agent，加上 sprint 分解机制。在使用 Opus 4.5 时，这个架构能产生高质量输出，但成本很高（6 小时，$ $9。随着模型版本更新到 Opus 4.6，模型本身的能力大幅提升------更擅长规划、能更可靠地维持长时间任务、更好的代码审查和调试能力。于是他们开始逐步移除不必要的组件：首先去掉 sprint 机制，因为模型已经能原生处理任务分解；然后调整 Evaluator 的触发频率，从每个 sprint 一次改为只在任务边界处检查。这种"按需增加复杂度"的原则值得注意：Harness 中的每个组件都对应着模型某个能力的不足，当模型进步时，这些假设需要被重新检验。

为什么是现在

Harness 这个概念为什么在最近被反复提起？一个比较合理的解释是：模型能力已经跨过了一个门槛，开始能够真正作为 Agent 工作了。在那之前，优化重点自然在模型本身；但当模型能做的事情变多之后，围绕它的系统设计就突然变得关键起来。

这和软件工程的演进轨迹很像。早期的焦点是写出能运行的代码，后来焦点慢慢转向如何构建能够持续演化、维护和扩展的系统。AI 工程也在经历类似的转折------模型能力固然重要，但运行环境正在成为决定成败的关键因素。

## References

1. Lopopolo, Ryan. "Harness engineering: leveraging Codex in an agent-first world." OpenAI, February 11, 2026.  
   Link:https://openai.com/index/harness-engineering/

2. Anthropic. "Demystifying evals for AI agents." Anthropic Engineering, January 9, 2026.  
   Link:https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

3. LangChain. "Improving Deep Agents with harness engineering." LangChain Blog, February 17, 2026.  
   Link:https://blog.langchain.com/improving-deep-agents-with-harness-engineering/

4. Anthropic. "Effective harnesses for long-running agents." Anthropic Engineering, November 26, 2025.  
   Link:https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

5. Anthropic. "Harness design for long-running application development." Anthropic Engineering, March 24, 2026.  
   Link:https://www.anthropic.com/engineering/harness-design-long-running-apps

6. Anthropic. "Building a C compiler with a team of parallel Claudes." Anthropic Engineering, February 5, 2026.  
   Link:https://www.anthropic.com/engineering/building-c-compiler



