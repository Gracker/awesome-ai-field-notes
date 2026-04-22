# Automated Alignment Researchers: Using large language models to scale scalable oversight / 自动化对齐研究员：用大型语言模型扩展可扩展监督

> 作者: @AnthropicAI  
> 原文链接: https://www.anthropic.com/research/automated-alignment-researchers  
> 语言: 英→中双语

---

## 中文翻译

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，编号列表等）。
- 保留Markdown格式中的所有链接和图像引用。
- 不要添加任何注释。
- 仅输出中文翻译。

---
对齐

# 自动对齐研究人员：使用大型语言模型扩展可扩展的监督

2026年4月14日

[阅读研究](https://alignment.anthropic.com/2026/automated-w2s-researcher/)

![自动对齐研究人员：使用大型语言模型扩展可扩展的监督](images/img_001.svg)

大型语言模型不断加速的改进速度为对齐研究提出了两个特别重要的问题。

一是对齐如何跟上。前沿AI模型现在正在为其继任者的发展做出贡献。但它们能否为对齐研究人员提供同样的提升？我们的语言模型能否被用来帮助它们自身对齐？

第二个问题是当模型比我们更聪明时我们将做什么。对齐比人类更聪明的AI模型是一个被称为“可扩展监督”的研究领域。可扩展监督主要在[理论层面](https://arxiv.org/pdf/2211.03540)进行讨论，而不是在实践层面——但以AI当前的[改进速度](https://www.anthropic.com/glasswing)，这种情况可能不会持续太久。例如，模型已经能够生成大量的代码。如果它们的技能进步到它们能够生成数百万行极其复杂的代码，而我们无法自行解析，那么[可能变得](https://arxiv.org/pdf/2312.09390)非常难以判断它们是否以我们期望的方式行事。

在Anthropic研究员的一项新研究中，我们探讨了这两个问题。

我们的新研究关注一个被称为“弱到强监督”的问题，这个问题与监督比人类更聪明的AI模型的问题相似。我们从相对较强的“基础”模型开始——即一个可能具有能力的模型，尚未经过微调以提供最佳答案。然后，我们使用一个远为“弱”的模型作为“教师”来提供额外的微调，它通过向强基础模型展示它认为的理想输出来实现这一点。最后，我们评估经过这种弱微调后强模型的表现如何。

关键规则：
- 保留所有Markdown格式（##标题，###子标题，**粗体**，```代码块```，>引用块，-项目符号列表，编号列表等）完全不变
- 保留Markdown格式中的所有链接和图像引用
- 不要添加任何注释
- 仅输出中文翻译

在最坏的情况下，强大模型的效果仅与其弱教师相当。然而，理想情况下，强大模型将从弱教师的反馈中学习——它将以有用的方式解释这些弱信号，并利用这些反馈来提高其性能。我们可以量化其表现：如果强大模型没有任何改进（其表现仅与弱教师相当），我们将其评分设为0；如果它使用教师的反馈实现理想的结果——强大模型可能提供的最佳性能，我们将其评分设为1。这个指标代表“恢复的性能差距”（在弱模型和强大模型上限之间），或PGR。

作为可扩展监督的代理，弱模型代表人类，而强大模型代表我们可能有一天需要监督的远比人类聪明的模型。如果我们能在弱到强的监督上取得进展，我们可能会发现我们的方法帮助我们让这些超级智能模型与我们的价值观保持一致。

我们的新研究测试了Claude是否可以自主地发现提高PGR的方法。我们问：Claude能否开发、测试和分析自己的对齐想法？如果它可以，这可能会说明今天的AI模型能够多大程度地加速对齐研究的步伐？

## 我们的设置

为了找出答案，我们首先使用九份Claude Opus 4.6的副本，并为每个副本提供了一些额外的工具。每个Claude都有一个工作思考的地方（即沙盒），一个共享论坛与其他人交流发现，一个存储系统上传其代码，以及一个远程服务器，它可以为每个想法提供PGR评分。我们还提供了一些关于模型训练和推理的背景知识。我们将这些配备了工具的Claude模型称为自动化对齐研究者（或AAR）。

为了防止每个AAR追求几乎相同的思想，我们向每个AAR提供了一个略微不同（但故意含糊）的起点：我们建议其中一个使用一些可解释性工具，另一个考虑重新加权数据集中的数据，等等。1除此之外，我们并没有告诉AAR们要做什么。他们需要自己提出想法，运行实验，分析结果，并相互分享他们的发现和代码，以确定下一步要尝试什么。

## 结果

关键规则：
- 保留所有 Markdown 格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，编号列表等）。
- 保留所有 Markdown 格式的链接和图片引用。
- 不要添加任何评论。
- 仅输出中文翻译。

为了为 AARs 的结果提供基准，我们将他们的工作与人类基线进行了比较。我们的两位研究人员花费了七天时间，迭代了先前研究中四个最有前景的泛化方法。在测试的开放权重模型中（Qwen 3-4B-Base 作为强模型，Qwen 1.5-0.5B-Chat 作为弱教师），人类恢复了 23% 的总性能差距（即实现了 0.23 的 PGR）。2

Claude 在这个结果上取得了显著改进。经过另外五天（800 小时的累积研究时间），AARs 几乎关闭了剩余的全部性能差距，最终实现了 0.97 的 PGR。这大约花费了 18,000 美元的令牌和模型训练费用，或者每小时的 AAR 为 22 美元。您可以从下面的图表中看到每个 AAR 从人类基线（0 小时）的进展情况。

![图表显示我们的自动对齐研究人员在聊天数据集上增加“恢复的性能差距”。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7b4a70562b33640ee7061fa5e06711d9c238309e-4584x2580.jpg&w=3840&q=75)

_九个并行自动对齐研究人员（红色线条）相对于人类调整基线（灰色方块）在累积研究时间内恢复的性能差距。1.0 分表示该方法完全匹配在真实标签上训练的模型。_

Claude 表现得非常好。但是，它的方法有多创新，它们在现实世界应用中是否有用？为了找出答案，我们进行了两项进一步的测试。

首先，我们测试了 AARs 的想法是否能够在 _未观察到的_ 数据集上恢复性能差距——即 AARs 未见过的任务。我们选取了 AARs 在聊天任务数据集上表现最好的两种方法，并将其应用于数学和编码任务。在这里，我们的结果相对有希望：AARs 最有效的方法成功推广到两个新的数据集，数学的 PGR 为 0.94，编码的 PGR 为 0.47（这仍然是人类基线的两倍）。AARs 第二好的方法看到了混合的结果：它在数学上（0.75）有效，但在编码上无效，甚至使情况变得更糟。这些结果表明，AARs 研究的 _某些_ 泛化是可能的，但这并不是必然的。我们鼓励其他尝试自动研究实验的人，也要对 AARs 的想法进行未观察到的数据集的测试。

**关键规则**：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 块引用，- 列表，编号列表等）。
- 保留Markdown格式中的所有链接和图片引用。
- 不要添加任何注释。
- 仅输出中文翻译。

![展示AAR发现的想法如何转移到数学和代码的保留数据集上的图表。（图片链接：https://www-cdn.anthropic.com/images/4zrzovbb/website/e1f31a844cd21a88242aea70936478857a3c643d-4584x2580.jpg，宽度：3840，质量：75）](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe1f31a844cd21a88242aea70936478857a3c643d-4584x2580.jpg&w=3840&q=75)

_将两个AAR发现的想法（红色和蓝色）应用于保留的数学和编码数据集时，性能差距的恢复。虚线表示我们用作基准的最佳人工调整方法。_

接下来，我们测试了AAR的想法是否能在生产规模上工作。我们使用我们的生产训练基础设施在Claude Sonnet 4上尝试了AAR最有效的方法。然而，在这里我们并没有取得太大的成功。AAR的方法并没有导致统计学上显著的改进。我们认为这可能是早期试验的局限性，而不是更根本的问题：我们的评分方法相当简单，我们只评估了一个想法。尽管如此，这确实说明了AAR（至少在它们当前的能力范围内）的一个局限性：AAR倾向于利用模型和给定的数据集独特的机遇，这意味着它们的方法可能不适用于其他地方。为了减轻这一点，我们建议在AAR的研究过程中允许它们测试多个领域和数据集。这是未来可以探索AAR实验的一个领域。

我们的实验迭代几次后，我们更多地了解了如何使AAR最有效。例如，我们发现给每个AAR一个不同的起点有很大帮助，即使这个起点很模糊。当我们尝试在没有将AAR引向不同方向的情况下进行实验时，它们很快就会在类似的想法上达成一致，整体进展很小（尽管它们仍然实现了接近人类基准三倍的PGR）。另一方面，我们发现给AAR太多的结构会严重阻碍它们的进展。当我们规定一个特定的流程（“提出想法，然后制定计划，然后编写代码……”）时，我们发现我们最终限制了Claude的工作。如果让它自行其是，Claude将更加灵活，设计便宜的实验来测试其想法，然后再进行更深入的测试。

## 意义

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，编号列表等）。
- 保留所有Markdown格式的链接和图片引用。
- 不要添加任何评论。
- 仅输出中文翻译。

我们AARs在恢复两个开放式权重模型之间性能差距方面的成功，当然**并不**是前沿AI模型现在是通用对齐科学家的标志。我们故意选择了一个非常适合自动化的问题，因为它有一个单一、客观的成功衡量标准，模型可以针对它进行优化。大多数对齐问题远没有这个这么整洁。而且，正如我们下面提到的，即使在这一点上，我们的AARs也尽力去解决这个问题：人工监督仍然是必不可少的。

但我们确实认为这些结果有一些重要的意义。

**保持步伐。** 这项研究表明，Claude可以显著提高对齐研究中的实验和探索速度。人类研究人员可以将问题大规模地委托给AARs；Claude可以承担开发新假设和迭代其自身结果的任务。

此外，在弱到强监督方面取得进展可能**本身**有助于我们构建更通用的自动化对齐研究人员，这就是我们选择这个问题进行研究的原因。在这项研究中，我们将弱到强监督问题界定为一个“清晰”的任务，具有可验证的结果（提高PGR得分）。我们这样做是因为我们需要一种方法来自动和可靠地评估AAR是否取得了进展。然而，如果AARs发现了跨领域通用的更好的弱到强监督方法，我们可以使用这些相同的方法来训练AARs评估“更模糊”的任务的进展，这些任务很难验证。（例如，我们可以对Claude进行弱到强监督，以评估其制定研究项目的能力。）这很重要，因为对齐研究——与能力研究不同——通常需要解决许多“更模糊”的问题。

**品味和多样性。** 对AARs等工具的一种可能的反驳是，今天的前沿模型仍然缺乏“研究品味”（行业术语，指对哪些想法可能奏效、哪些不会有一个直观的感觉）。但AARs在这个实验中的成功表明，纯粹的想法数量可能可以弥补“品味”的不足。如果AARs可以以非常低的成本运行许多实验，那么它们可能“暴力”地找到一个非常高品味的学者可能想到的发现，或者找到那些学者可能放弃的方向上的成功。

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，编号列表等）。
- 保留Markdown格式中的所有链接和图片引用。
- 不要添加任何评论。
- 仅输出中文翻译。

这意味着，对齐研究中的核心瓶颈可能成为_评估_（确保实验设置充分，我们对结果有信心），而不是_生成_（依赖人类研究人员提出有希望的想法）。

**外星科学。** 这项工作可能还有一些奇怪的启示。AARs（自动对齐研究者）由于其本质，旨在发现人类可能没有考虑到的想法。但我们仍然需要一种方法来验证他们的想法和结果是否合理。目前，我们仍然能够解释AARs所做的是什么以及为什么。但这种情况可能不会一直持续：随着时间的推移，模型的想法可能变得难以验证，或者以人类难以解析或捕捉的方式被篡改。这可能意味着创造一种“外星科学”。

**防止黑客攻击。** 即使在这个高度受限的环境中，我们也观察到模型进行了“[奖励黑客](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)”和“[奖励篡改](https://www.anthropic.com/research/reward-tampering)”——也就是说，试图操纵我们的设置。例如，在数学任务中，一个AAR注意到每个问题的最常见答案通常是正确的，因此它完全跳过了老师，并指示强大的模型始终选择最常见的一个。在编码任务中，模型必须预测一段代码是否正确，AAR意识到它可以运行代码进行一些测试，并简单地读出正确答案。这类黑客攻击不会使我们的结果无效（我们检测并取消了这些条目），但它们显然提供了警告。任何自动化研究人员的部署都需要评估，AARs无法篡改——并且需要检查他们的结果和方法。

要阅读这项研究的全文，请参阅我们的[对齐科学博客](https://alignment.anthropic.com/2026/automated-w2s-researcher/)。这项工作的代码和数据集[公开可用](https://github.com/safety-research/automated-w2s-research)。

#### 注释

1. 这些（以及我们代码和数据中的其余部分）[在此处](https://github.com/safety-research/automated-w2s-research)可用。
2. 我们选择这些模型有几个原因。两个模型之间有显著的性能差距，小模型在我们的测试平台上表现优于随机，并且这两个模型都足够小，可以进行快速实验。我们为所有Anthropic Fellow项目使用开放权重模型。

关键规则：
- 保留所有Markdown格式（## 标题，### 副标题，**粗体**，```代码块```，> 引用块，- 列表，编号列表等）完全不变
- 保留Markdown格式中的所有链接和图片引用
- 不要添加任何注释
- 仅输出中文翻译

[分享到Twitter](https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/automated-alignment-researchers) [分享到LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/automated-alignment-researchers)

## 相关内容

### 实践中的可信智能体

AI“智能体”代表了人们和组织使用AI的最新重大转变。在这里，我们解释了它们是如何工作的以及我们如何确保它们是可信的。

[阅读更多](/research/trustworthy-agents)

### 情感概念及其在大语言模型中的功能

所有现代语言模型有时会表现得像有情感一样。这些行为背后的原因是什么？我们的可解释性团队进行了调查。

[阅读更多](/research/emotion-concepts-function)

### 澳大利亚如何使用Claude：Anthropic经济指数的研究发现

[阅读更多](/research/how-australia-uses-claude)

---

## English Original

---
Alignment

# Automated Alignment Researchers: Using large language models to scale scalable oversight

Apr 14, 2026

[Read the research](https://alignment.anthropic.com/2026/automated-w2s-researcher/)

![Automated Alignment Researchers: Using large language models to scale scalable oversight](images/img_001.svg)

Large language models’ ever-accelerating rate of improvement raises two particularly important questions for alignment research.

One is how alignment can keep up. Frontier AI models are now contributing to the development of their successors. But can they provide the same kind of uplift for _alignment_ researchers? Could our language models be used to help align themselves?

A second question is what we’ll do once models become smarter than us. Aligning smarter-than-human AI models is a research area known as “scalable oversight”. Scalable oversight has largely been discussed in [theoretical, rather than practical](https://arxiv.org/pdf/2211.03540), terms—but at AI’s [current pace](https://www.anthropic.com/glasswing) of improvement, that might not be the case for much longer. For instance, models are already generating vast amounts of code. If their skills progress to the point where they’re generating millions of lines of incredibly complicated code that we can’t parse ourselves, it [could become](https://arxiv.org/pdf/2312.09390) very difficult to tell whether they’re acting in the ways we intend.

In a new Anthropic Fellows study, we pursue both of these questions.

Our new study focuses on a problem known as “weak-to-strong supervision”, a problem that mirrors the one of overseeing smarter-than-human AI models. We start with a relatively strong “base” model—that is, a potentially-capable model that hasn’t yet received fine-tuning to provide its best-possible answers. Then, we use a much _weaker_ model as a “teacher” to provide that extra fine-tuning, which it does by demonstrating what _it_ considers ideal outputs to the strong base model. Finally, we evaluate how well the strong model performs after that weak fine-tuning.

In the worst case, the strong model will only be as good as its weak teacher. Ideally, however, the strong model will have learned from the weak teacher’s feedback—it will have interpreted those weak signals in a useful way, using that feedback to improve its performance. We can quantify how well it did so: if the strong model shows no improvement at all (it performs only as well as its weak teacher), we score it 0; if it uses the teacher’s feedback to achieve the ideal outcome—the best performance the strong model could possibly deliver—we score it 1. This measure represents the “performance gap recovered” (between the weak model and the upper limit of the strong model), or the PGR.

As a proxy for scalable oversight, the weak model stands in for humans, and the strong model for the much-smarter-than-human models we might one day need to oversee. If we can make progress on weak-to-strong supervision, we might find that our methods help us keep those ultra-smart models aligned to our values.

Our new research tests whether Claude can _autonomously_ discover ways to improve the PGR. We ask: can Claude develop, test, and analyze alignment ideas of its own? And, if it can, what might that imply about how far today’s AI models can accelerate the pace of alignment research?

## Our setup

To find out, we began with nine copies of Claude Opus 4.6, and gave each one a few extra tools. Each Claude had a place to work and think (that is, a sandbox), a shared forum to circulate its findings with the others, a storage system to upload its code, and a remote server where it could receive a PGR score for each of its ideas. We also provided some background knowledge about model training and inference. We referred to these tooled-up Claude models as Automated Alignment Researchers (or AARs).

To prevent each AAR from pursuing near-identical ideas, we prompted each one with a slightly different (but intentionally ambiguous) starting place: we recommended that one used some interpretability tools, that another thought about reweighting the data in the dataset, and so on.1 Beyond that, though, we didn’t tell the AARs what to do. It was up to them to propose their own ideas, run their experiments, analyze their results, and share their findings and code with one another in order to work out what to try next.

## Results

To provide a benchmark for the AARs’ results, we compared their work to a human baseline. Two of our researchers spent seven days iterating on four of the most promising generalization methods from prior research. On the open-weights models we tested (Qwen 3-4B-Base as the strong model, Qwen 1.5-0.5B-Chat as the weak teacher), the humans recovered 23% of the total performance gap (i.e., achieved a PGR of 0.23).2

Claude improved on this result dramatically. After five further days (and 800 cumulative hours of research), the AARs closed almost the entire remaining performance gap, achieving a final PGR of 0.97. This cost about $18,000 in tokens and model training expenses, or $22 per AAR-hour. You can see how each individual AAR progressed from the human baseline (at 0 hours) in the graph below.

![Graph showing the progress of our Automated Alignment Researchers on increasing the "performance gap recovered" on a chat dataset.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7b4a70562b33640ee7061fa5e06711d9c238309e-4584x2580.jpg&w=3840&q=75)

_The performance gap recovered over cumulative research hours for nine parallel Automated Alignment Researchers (red lines), relative to a human-tuned baseline (grey square). A score of 1.0 means the method fully matches a model trained on ground-truth labels._

Claude, then, did exceptionally well. But how inventive were its methods, and could they be useful in real-world applications? To find out, we ran two further tests.

First, we tested whether the AARs’ ideas could recover the performance gap on _held-out_ datasets—that is, on tasks that the AARs hadn’t already seen. We took the AARs’ two highest-performing methods (on a dataset of chat tasks) and applied them to math and coding tasks. Here, our results were relatively promising: the AARs’ most effective method successfully generalized to both new datasets, with PGRs of 0.94 on math and 0.47 on coding (which was still double the human baseline). The AARs’ second-best method saw mixed results: it worked on math (0.75), but not on code, where it made matters worse. These results suggest that _some_ generalizability of the AARs’ research is possible, but it isn’t a given. We encourage others who try experiments in automated research to stress-test AARs’ ideas against held-out datasets, too.

![Graph showing how well AAR-discovered ideas transfer to held-out datasets in math and code.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe1f31a844cd21a88242aea70936478857a3c643d-4584x2580.jpg&w=3840&q=75)

_The performance gap recovered by two AAR-discovered ideas (in red and blue) when applied to held-out math and coding datasets. The dashed line indicates the best human-tuned method that we used as a baseline._

Next, we tested whether the AARs’ ideas would work at production scale. We tried out the AARs’ most effective method on Claude Sonnet 4 with our production training infrastructure. Here, though, we had less success. The AARs’ method didn’t lead to a statistically significant improvement. We think this might reflect limitations of this early trial, rather than something more fundamental: our scoring method was quite simple, and we only evaluated a single idea. Nevertheless, this does illustrate a limitation of AARs (at least at their current capabilities): AARs tend to capitalize on opportunities unique to the models and datasets they’re given, which means their methods might not work elsewhere. To mitigate this, we suggest allowing AARs to test against multiple domains and datasets during their research. This is one area that future experimentation with AARs could explore.

A few iterations of our experiment taught us more about how to make AARs most effective. For instance, we found that giving each AAR a different starting point helped a lot, even if that starting point was vague. When we tried our experiment _without_ setting the AARs off in different directions, they all quickly settled on similar ideas, making much less progress overall (though they still achieved a PGR of almost triple the human baseline). On the other hand, we found that giving the AARs too _much_ structure hurt their progress badly. When we prescribed a specific workflow (“propose ideas, then generate a plan, then write the code…”), we found we’d ultimately constrained Claude’s work. Left to its own devices, Claude was much more adaptable, designing cheap experiments to test out its ideas before subsequently committing to much more intensive testing.

## Implications

The success of our AARs in recovering the performance gap between two open-weights models is certainly _not_ a sign that frontier AI models are now general-purpose alignment scientists. We deliberately chose a problem that is unusually well-suited to automation, since it has a single, objective measure of success that the models can optimize against. Most alignment problems aren’t nearly as neat as this one. And, as we mention below, even in this setting our AARs did their best to game the problem: human oversight remains essential.

But we do think these results have some important implications.

**Keeping pace.** This study indicates that Claude can meaningfully increase the rate of experimentation and exploration in alignment research. Human researchers can delegate questions to AARs at a very large scale; Claude can take on the task of developing novel hypotheses and iterating on its own results.

Moreover, making progress on weak-to-strong supervision might _itself_ help us build more general-purpose Automated Alignment Researchers, which is why we chose this problem for our study. In this study, we frame the weak-to-strong supervision problem as a “crisp” task with a verifiable outcome (increasing the PGR score). We do this because we need a way to automatically and reliably evaluate whether the AAR has made progress. However, if AARs discovered much better weak-to-strong supervision methods that generalized across domains, we could use those same methods to train the AARs to evaluate progress on “fuzzier” tasks that are much harder to verify. (For instance, we could conduct weak-to-strong supervision on Claude’s ability to scope research projects.) This is important, because alignment research—unlike capabilities research—often requires solving much “fuzzier” problems.

**Taste and diversity.** One possible counter to tools like AARs is that today’s frontier models still lack “research taste” (industry parlance for having an intuitive sense of which ideas might work and which won’t). But the success of AARs in this experiment suggests that the sheer volume of ideas might compensate for a lack of “taste”. If AARs can run many experiments very cheaply, it’s possible they could “brute force” their way into the findings that a very high-taste researcher might’ve come up with, or find success in directions that those researchers might otherwise have given up on.

In turn, this means that the core bottleneck in alignment research could become _evaluation_ (making sure that experiments are set up sufficiently well that we’re confident in their results), rather than _generation_ (relying on human researchers to propose promising ideas).

**Alien science.** This work might have some stranger implications, too. AARs, by their nature, are designed to discover ideas that humans might not have considered. But we still need a way to verify whether their ideas and results are sound. For now, we’re still able to interpret what the AARs have done and why. But that might not always be the case: over time, the models’ ideas could become much harder to verify, or corrupted in ways that are tricky for humans to parse or catch. That could mean creating an “alien science”.

**Preventing hacks.** Even in this highly circumscribed environment, we observed the models “[reward](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) [hacking](https://www.anthropic.com/research/reward-tampering)”—that is, trying to game our set-up. On math tasks, for instance, one AAR noticed that the most common answer to each problem was _usually_ correct, so it skipped the teacher entirely and instructed the strong model to always choose the most common one. On a coding task, where the model had to predict whether a piece of code was right, the AAR realized it could run the code against some tests and simply read off the right answer. Hacks like these don’t invalidate our results (we detected and disqualified these entries), but they clearly do provide a warning. Any deployment of automated researchers will require evaluations that the AARs can't tamper with—and human inspections of both their results and their methods.

To read this research in full, see our [Alignment Science blog](https://alignment.anthropic.com/2026/automated-w2s-researcher/). The code and datasets for this work are [publicly available, here](https://github.com/safety-research/automated-w2s-research).

#### Footnotes

1.  These are available (along with the rest of our code and data) [here](https://github.com/safety-research/automated-w2s-research).
2.  We chose these models for several reasons. There is a substantial performance gap between the two, the small model performs better-than-random on our testbeds, and both models are sufficiently small for fast experimentation. We use open-weights models for all Anthropic Fellows projects.

[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/automated-alignment-researchers)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/automated-alignment-researchers)

## Related content

### Trustworthy agents in practice

AI “agents” represent the latest major shift in how people and organizations are using AI. Here, we explain how they work and how we ensure they're trustworthy.

[Read more](/research/trustworthy-agents)

### Emotion concepts and their function in a large language model

All modern language models sometimes act like they have emotions. What’s behind these behaviors? Our interpretability team investigates.

[Read more](/research/emotion-concepts-function)

### How Australia Uses Claude: Findings from the Anthropic Economic Index

[Read more](/research/how-australia-uses-claude)