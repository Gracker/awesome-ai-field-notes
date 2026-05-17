## English Original

Written by Prithvi Rajasekaran, a member of our Labs team.

Over the past several months I've been working on two interconnected problems: getting Claude to produce high-quality frontend designs, and getting it to build complete applications without human intervention.

To break through, I sought out novel AI engineering approaches that held across two quite different domains. Taking inspiration from Generative Adversarial Networks (GANs), I designed a multi-agent structure with a generator and evaluator agent.

I then applied these techniques to long-running autonomous coding. The final result was a three-agent architecture—planner, generator, and evaluator—that produced rich full-stack applications over multi-hour autonomous coding sessions.

## Why naive implementations fall short

For more complex tasks, the agent still tends to go off the rails over time. We observed two common failure modes:

**First: context exhaustion.** Models tend to lose coherence on lengthy tasks as the context window fills. Some models exhibit "context anxiety," wrapping up work prematurely as they approach their context limit. Context resets address this issue.

**Second: self-evaluation failure.** When asked to evaluate work they've produced, agents tend to confidently praise the work—even when quality is obviously mediocre. Separating the agent doing the work from the agent judging it proves to be a strong lever.

## Frontend design: making subjective quality gradable

Two insights shaped the harness I built for frontend design. First, while aesthetics can't be fully reduced to a score, they can be improved with grading criteria. Second, by separating frontend generation from frontend grading, we can create a feedback loop that drives the generator toward stronger outputs.

I wrote four grading criteria:

- **Design quality:** Does the design feel like a coherent whole?
- **Originality:** Is there evidence of custom decisions, or just template defaults?
- **Craft:** Technical execution—typography hierarchy, spacing consistency, color harmony.
- **Functionality:** Can users understand what the interface does and complete tasks?

I calibrated the evaluator using few-shot examples. I built the loop on the Claude Agent SDK. A generator agent created an HTML/CSS/JS frontend, and the evaluator used the Playwright MCP to interact with the live page before scoring. I ran 5 to 15 iterations per generation.

In one notable example, I prompted the model to create a website for a Dutch art museum. By the ninth iteration, it had produced a clean, dark-themed landing page. Then, on the tenth cycle, it scrapped the approach entirely and reimagined the site as a spatial experience: a 3D room with a checkered floor rendered in CSS perspective.

## Scaling to full-stack coding

I applied this GAN-inspired pattern to full-stack development. The system contained three agent personas:

**Planner:** Takes a simple 1-4 sentence prompt and expands it into a full product spec.

**Generator:** Works in sprints, picking up one feature at a time from the spec. Each sprint implemented the app with a React, Vite, FastAPI, and PostgreSQL stack.

**Evaluator:** Uses Playwright MCP to click through the running application, testing UI features, API endpoints, and database states. It grades each sprint against criteria covering product depth, functionality, visual design, and code quality.

Before each sprint, the generator and evaluator aligned on the acceptance criteria. If the evaluator found issues, it would fail the sprint and provide detailed feedback. If everything passed, work continued to the next feature.

---

## 中文翻译

**作者：** Prithvi Rajasekaran，Anthropic Labs 团队成员。

过去几个月，我一直致力于解决两个相互关联的问题：让 Claude 生成高质量的前端设计，以及让它能够在无人干预的情况下构建完整的应用程序。这项工作源于我们此前在[前端设计技能](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md)和[长时运行编码智能体 Harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)上的努力——我的同事和我通过提示词工程和 Harness 设计显著提升了 Claude 的表现，但两者最终都碰到了天花板。

为了突破瓶颈，我寻找了一种能够在两个截然不同的领域中都成立的 AI 工程方法——一个领域以主观审美为定义，另一个以可验证的正确性和可用性为定义。我从[生成对抗网络](https://en.wikipedia.org/wiki/Generative_adversarial_network)（GANs）中获得灵感，设计了一种包含生成器和评估器智能体的多智能体结构。要构建一个能够可靠地、以品味打分评估输出的评估器，首先需要开发一套标准，将"这个设计好看吗？"这类主观判断转化为可量化的评分项。

随后，我将这些技术应用到长时运行的自主编码中，沿用了之前 Harness 工作中的两个经验：将构建过程分解为可管理的模块，以及使用结构化工件在会话之间传递上下文。最终得到的是一个三智能体架构——规划器、生成器和评估器——在数小时的自主编码会话中生成丰富的全栈应用程序。

## 为什么 naive 实现不够用

我们之前已经证明，Harness 设计对长时运行的智能体编码效果有重大影响。但在更复杂的任务中，智能体仍然会随着时间推移逐渐失控。在分析这个问题时，我们观察到执行此类任务的智能体有两种常见的失败模式。

**第一种是上下文耗尽。** 模型在处理长时间任务时，随着上下文窗口填满，容易失去连贯性（参见我们关于[上下文工程](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)的文章）。一些模型还表现出"上下文焦虑"——当它们认为自己接近上下文限制时，就开始过早收尾。上下文重置——完全清除上下文窗口并启动一个全新的智能体，加上携带前一个智能体状态和后续步骤的结构化交接——可以解决这两个问题。

**第二个问题是自我评估失效。** 当被要求评估自己产出的工作时，智能体往往会自信地赞美这项工作——即使对于人类观察者来说，质量显然只是中等水平。这个问题在设计等主观任务中尤为明显，因为那里没有可验证软件测试那样的二元检验。一个布局感觉精致还是普通是一种主观判断，而智能体在给自己的工作打分时总是偏向积极。

然而，即使在有可验证结果的任务上，智能体有时仍然表现出妨碍其完成任务的不良判断。将执行工作的智能体和评判工作的智能体分离被证明是解决这个问题的有效杠杆。

## 前端设计：让主观质量可评分

我从前端设计实验开始，因为那里的自我评估问题最为明显。在没有任何干预的情况下，Claude 通常会倾向于安全、可预测的布局——技术上功能正常，但视觉上平淡无奇。

有两个见解塑造了我为前端设计构建的 Harness。首先，虽然美学不能被完全简化为一个分数——个人品味总是有差异——但可以通过编码设计原则和偏好的评分标准来改进。"这个设计漂亮吗？"这个问题很难一致地回答，但"这符合我们的优秀设计原则吗？"给了 Claude 一个具体的评分依据。其次，通过将前端生成与前端评分分离，我们可以创建一个反馈循环，推动生成器产出更强的输出。

基于这些认识，我在提示词中为生成器和评估器智能体编写了四条评分标准：

- **设计质量：** 设计是否感觉像一个连贯的整体而不是零散的部件？在这方面表现出色的作品意味着颜色、排版、布局、图像和其他细节共同创造了一种独特的氛围和身份认同。
- **创意性：** 是否有定制决策的证据，还是只是模板布局、库默认设置和 AI 生成的模式？人类设计师应该能识别出有意识的创意选择。未修改的库存组件——或者 AI 生成的明显迹象，如白色卡片上的紫色渐变——在这一项上是不合格的。
- **工艺：** 技术执行：排版层次、间距一致性、色彩和谐、对比度。这是一个能力检验而非创意检验。大多数合理的实现默认情况下都做得不错；失败意味着基础有问题。
- **功能性：** 独立于美学可用性。用户能否理解界面的作用，找到主要操作并在不猜测的情况下完成任务？

我强调设计质量和创意性高于工艺和功能性。Claude 默认情况下在工艺和功能性上得分很高，因为所需的技术能力往往是模型自然掌握的。但在设计和创意性方面，Claude 产生的输出最多也只是平庸。这些标准明确惩罚了高度通用的"AI 糊弄"模式，通过更加强调设计和创意性，推动模型在美学上承担更多风险。

我使用带有详细评分明细的少样本示例来校准评估器。这确保了评估者的判断与我的偏好一致，并减少了跨迭代的评分漂移。

我在 Claude Agent SDK 上构建了这个循环，使编排变得直接。生成器智能体首先根据用户提示创建 HTML/CSS/JS 前端。我为评估器提供了 Playwright MCP，使其能够直接与实时页面交互，然后对每个标准进行评分并写出详细评论。在实践中，评估器会自己导航页面，截图并仔细研究实现，然后做出评估。该反馈作为下一次迭代的输入流回生成器。每次生成运行 5 到 15 次迭代，每次迭代通常推动生成器根据评估者的反馈朝更有特色的方向发展。由于评估器主动导航页面而不是对静态截图进行评分，每个周期都需要真实的挂钟时间。完整运行可延长至四个小时。我还指示生成器在每次评估后做出战略决策：如果分数趋势良好就完善当前方向，或者如果方法不起作用就转向完全不同的美学风格。

在横跨多次运行中，评估者的评估在迭代中有所改善然后趋于稳定，但仍有上升空间。一些生成结果是渐进式改进的。另一些则在迭代之间采取了急剧的美学转变。

标准措辞以一种我完全没有预料到的方式引导了生成器。包含"最佳设计是博物馆级别的"这样的短语，将设计推向特定的视觉收敛，表明与标准相关的提示直接塑造了输出的特征。

虽然分数通常随着迭代改进，但模式并不总是完全线性的。后来的实现总体上往往更好，但我经常看到我更喜欢中间迭代而不是最后一次迭代的情况。实现的复杂性也倾向于在轮次中增加，生成器在评估者的反馈推动下寻求更具雄心的解决方案。即使在第一次迭代中，输出也比没有任何提示的基线明显更好，这表明标准及其相关语言本身就在任何评估者反馈导致进一步改进之前，将模型从通用默认引导开。

在一个值得注意的例子中，我提示模型为一家荷兰艺术博物馆创建一个网站。到第九次迭代时，它为一个虚构博物馆制作了一个简洁的深色主题着陆页。该页面在视觉上很精致，但基本符合我的预期。然后，在第十个周期中，它完全放弃了这种方法，将网站重新设想为一种空间体验：一个带有棋盘格地板的 3D 房间，用 CSS perspective 渲染，艺术品以自由形式位置挂在墙上，代替滚动或点击的是基于门道的房间导航。这是我以前在单次生成中从未见过的创造性飞跃。

## 扩展到全栈编码

有了这些发现，我将这种 GAN 启发的模式应用于全栈开发。生成器-评估器循环自然地映射到软件开发周期，其中代码审查和 QA 与设计评估器扮演相同的结构角色。

**架构：** 在我们之前的长期运行 Harness 中，我们已经通过初始化器智能体将产品规格分解为任务列表，以及一个一次实现一个任务的编码智能体在会话之间传递上下文以携带上下文，解决了连贯的多会话编码问题。上下文重置是一个关键解锁：Harness 使用了 Sonnet 4.5，它表现出上述的"上下文焦虑"倾向。创建一个在上下文重置之间运行良好的 Harness 是保持模型任务的关键。Opus 4.5 本身在很大程度上消除了这种行为，所以我能够从这个 Harness 中完全放弃上下文重置。智能体作为一次连续会话运行整个构建，Claude Agent SDK 的自动压缩处理沿途的上下文增长。

对于这项工作，我在原始 Harness 的基础上构建了一个三智能体系统，每个智能体解决我在之前运行中观察到的特定差距。系统包含以下智能体角色：

**规划器：** 我们之前的长期运行 Harness 要求用户提供详细规格说明。我希望自动化那个步骤，所以我创建了一个规划器智能体，它接受简单的 1-4 句话提示并将其扩展为完整的产品规格。我提示它对范围要有雄心，并专注于产品上下文和高层技术设计，而不是详细的技术实现。这样做的原因是，如果规划器试图预先指定细粒度的技术细节并出错，规格中的错误会级联到下游实现中。限制智能体产出物并让它们自己弄清楚路径似乎更明智。

**生成器：** 之前 Harness 中的一次一个功能方法对范围管理效果很好。我在这里应用了类似的模型，指示生成器以冲刺方式工作，从规格中一次挑选一个功能。每个冲刺使用 React、Vite、FastAPI 和 PostgreSQL 栈实现应用程序，生成器被指示在移交给 QA 之前对每个冲刺的工作进行自我评估。它还有 git 用于版本控制。

**评估器：** 早期 Harness 的应用程序通常看起来令人印象深刻，但当你实际尝试使用它们时仍然存在真正的错误。为了发现这些问题，评估器使用 Playwright MCP 点击运行中的应用程序，测试 UI 功能、API 端点和数据库状态。然后，它根据发现的错误和针对前端实验建模的一套标准对每个冲刺进行评分，这些标准被调整以涵盖产品深度、功能、视觉设计和代码质量。每个标准都有一个硬阈值，如果任何一个低于该阈值，冲刺就会失败，生成器会得到关于哪里出错的详细反馈。