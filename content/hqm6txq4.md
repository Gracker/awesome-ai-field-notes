# Automated Alignment Researchers: 使用大型语言模型扩展可扩展监督

> 作者: @AnthropicAI
> 原文链接: https://www.anthropic.com/research/automated-alignment-researchers

---

## 对齐

# Automated Alignment Researchers: 使用大型语言模型扩展可扩展监督

**原文（English）:**

Large language models' ever-accelerating rate of improvement raises two particularly important questions for alignment research.

One is how alignment can keep up. Frontier AI models are now contributing to the development of their successors. But can they provide the same kind of uplift for _alignment_ researchers? Could our language models be used to help align themselves?

A second question is what we'll do once models become smarter than us. Aligning smarter-than-human AI models is a research area known as "scalable oversight". Scalable oversight has largely been discussed in [theoretical, rather than practical](https://arxiv.org/pdf/2211.03540), terms—but at AI's [current pace](https://www.anthropic.com/glasswing) of improvement, that might not be the case for much longer. For instance, models are already generating vast amounts of code. If their skills progress to the point where they're generating millions of lines of incredibly complicated code that we can't parse ourselves, it [could become](https://arxiv.org/pdf/2312.09390) very difficult to tell whether they're acting in the ways we intend.

**中文翻译:**

大型语言模型不断提升的速度对对齐研究提出了两个尤为关键的问题。

其一，对齐如何跟上步伐？前沿 AI 模型正在为其后继者的开发做出贡献。但它们能否为 _对齐研究者_ 提供同样程度的帮助？我们的语言模型是否可用于帮助对齐自身？

其二，一旦模型变得比我们更聪明，我们将如何应对？对齐超越人类的 AI 模型是一个被称为"可扩展监督"（scalable oversight）的研究领域。可扩展监督在很大程度上一直停留在 [理论层面，而非实践层面](https://arxiv.org/pdf/2211.03540)——但按照 AI 目前的 [发展速度](https://www.anthropic.com/glasswing)，这种状况可能不会持续太久。例如，模型已经在生成大量代码。如果它们的技能发展到可以生成数百万行我们无法自行理解的复杂代码，那么 [可能就会变得](https://arxiv.org/pdf/2312.09390) 非常难以判断它们是否按照我们的意图行事。

---

**原文（English）:**

In a new Anthropic Fellows study, we pursue both of these questions.

Our new study focuses on a problem known as "weak-to-strong supervision", a problem that mirrors the one of overseeing smarter-than-human AI models. We start with a relatively strong "base" model—that is, a potentially-capable model that hasn't yet received fine-tuning to provide its best-possible answers. Then, we use a much _weaker_ model as a "teacher" to provide that extra fine-tuning, which it does by demonstrating what _it_ considers ideal outputs to the strong base model. Finally, we evaluate how well the strong model performs after that weak fine-tuning.

In the worst case, the strong model will only be as good as its weak teacher. Ideally, however, the strong model will have learned from the weak teacher's feedback—it will have interpreted those weak signals in a useful way, using that feedback to improve its performance. We can quantify how well it did so: if the strong model shows no improvement at all (it performs only as well as its weak teacher), we score it 0; if it uses the teacher's feedback to achieve the ideal outcome—the best performance the strong model could possibly deliver—we score it 1. This measure represents the "performance gap recovered" (between the weak model and the upper limit of the strong model), or the PGR.

**中文翻译:**

在一项新的 Anthropic Fellows 研究中，我们同时对这两个问题进行了探索。

我们的新研究聚焦于一个被称为"弱到强监督"（weak-to-strong supervision）的问题，这个问题与监督超越人类的 AI 模型问题相似。我们从一个相对较强的"基座"模型开始——即一个尚未来得及通过微调来给出最佳答案的潜在能力模型。然后，我们使用一个 _弱得多_ 的模型作为"教师"来提供额外的微调，它通过向强基座模型展示它认为理想的输出来做到这一点。最后，我们评估强模型在经过弱微调后的表现。

最坏情况下，强模型最多只能和弱教师一样好。然而理想情况下，强模型应该已经从弱教师的反馈中学到了东西——它会以有益的方式解读那些弱信号，并利用这些反馈来提升自己的表现。我们可以量化这一效果：如果强模型没有任何提升（其表现仅与弱教师相当），则得分为 0；如果它利用教师的反馈达到了理想结果——即强模型所能达到的最佳表现——则得分为 1。这一指标代表了"恢复的性能差距"（weak model 与 strong model 上限之间的差距），即 PGR。

---

**原文（English）:**

As a proxy for scalable oversight, the weak model stands in for humans, and the strong model for the much-smarter-than-human models we might one day need to oversee. If we can make progress on weak-to-strong supervision, we might find that our methods help us keep those ultra-smart models aligned to our values.

Our new research tests whether Claude can _autonomously_ discover ways to improve the PGR. We ask: can Claude develop, test, and analyze alignment ideas of its own? And, if it can, what might that imply about how far today's AI models can accelerate the pace of alignment research?

**中文翻译:**

作为可扩展监督的代理，弱模型代表人类，而强模型则代表我们有一天可能需要监督的远超人类的模型。如果我们能在弱到强监督上取得进展，我们的方法或许能帮助我们让那些超智能模型与我们的价值观保持一致。

我们的新研究测试了 Claude 是否能 _自主地_ 发现提升 PGR 的方法。我们想问：Claude 能否自主开发、测试和分析对齐思路？如果能做到，这对我们今天的人工智能模型能在多大程度上加速对齐研究的进展有何启示？

---

## Our Setup / 我们的设置

**原文（English）:**

To find out, we began with nine copies of Claude Opus 4.6, and gave each one a few extra tools. Each Claude had a place to work and think (that is, a sandbox), a shared forum to circulate its findings with the others, a storage system to upload its code, and a remote server where it could receive a PGR score for each of its ideas. We also provided some background knowledge about model training and inference. We referred to these tooled-up Claude models as Automated Alignment Researchers (or AARs).

To prevent each AAR from pursuing near-identical ideas, we prompted each one with a slightly different (but intentionally ambiguous) starting place: we recommended that one used some interpretability tools, that another thought about reweighting the data in the dataset, and so on. Beyond that, though, we didn't tell the AARs what to do. It was up to them to propose their own ideas, run their experiments, analyze their results, and share their findings and code with one another in order to work out what to try next.

**中文翻译:**

为了找到答案，我们从九个 Claude Opus 4.6 副本开始，并给每个配备了一些额外工具。每个 Claude 都有一个工作思考的空间（即沙盒），一个与其他 Claude 交流发现的共享论坛，一个上传代码的存储系统，以及一个可以接收每个想法 PGR 评分的远程服务器。我们还提供了一些关于模型训练和推理的背景知识。我们将这些配备了工具的 Claude 模型称为"自动化对齐研究员"（Automated Alignment Researchers，简称 AARs）。

为了防止每个 AAR 追求几乎相同的想法，我们为每个 AAR 提供了一个略有不同（但有意含糊）的起点：我们建议其中一个使用一些可解释性工具，另一个考虑重新加权数据集中的数据，等等。除此之外，我们没有告诉 AARs 应该做什么。由它们自己提出想法、运行实验、分析结果，并与彼此分享发现和代码，从而决定下一步尝试什么。

---

## Results / 结果

**原文（English）:**

To provide a benchmark for the AARs' results, we compared their work to a human baseline. Two of our researchers spent seven days iterating on four of the most promising generalization methods from prior research. On the open-weights models we tested (Qwen 3-4B-Base as the strong model, Qwen 1.5-0.5B-Chat as the weak teacher), the humans recovered 23% of the total performance gap (i.e., achieved a PGR of 0.23).

Claude improved on this result dramatically. After five further days (and 800 cumulative hours of research), the AARs closed almost the entire remaining performance gap, achieving a final PGR of 0.97. This cost about $18,000 in tokens and model training expenses, or $22 per AAR-hour. You can see how each individual AAR progressed from the human baseline (at 0 hours) in the graph below.

![Graph showing the progress of our Automated Alignment Researchers on increasing the "performance gap recovered" on a chat dataset.](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7b4a70562b33640ee7061fa5e06711d9c238309e-4584x2580.jpg&w=3840&q=75)

**中文翻译:**

为了给 AARs 的结果提供基准，我们将它们的工作与人类基线进行了比较。我们的两位研究人员花了七天时间迭代研究先前研究中最有前景的四种泛化方法。在我们测试的开源模型上（Qwen 3-4B-Base 作为强模型，Qwen 1.5-0.5B-Chat 作为弱教师），人类恢复了 23% 的总性能差距（即达到了 0.23 的 PGR）。

Claude 将这一结果大幅提升。经过另外五天（以及累计 800 小时的研究），AARs 几乎关闭了剩余的全部性能差距，最终达到了 0.97 的 PGR。这花费了约 18,000 美元的 token 和模型训练费用，即每个 AAR 小时 22 美元。您可以在下图中看到每个 AAR 如何从人类基线（在 0 小时处）开始进步的。

![图表显示我们的自动化对齐研究员在增加聊天数据集上"恢复的性能差距"的进展。](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7b4a70562b33640ee7061fa5e06711d9c238309e-4584x2580.jpg&w=3840&q=75)

---

**原文（English）:**

_The performance gap recovered over cumulative research hours for nine parallel Automated Alignment Researchers (red lines), relative to a human-tuned baseline (grey square). A score of 1.0 means the method fully matches a model trained on ground-truth labels._

**中文翻译:**

九个并行自动化对齐研究员（红线）随累计研究小时的性能差距恢复，相对于人类调优基线（灰色方块）。得分 1.0 表示该方法与用真实标签训练的模型的性能完全匹配。

Claude 的表现非常出色。但它的方法有多创新，在实际应用中是否有用？为了找出答案，我们进行了两项进一步测试。

---

**原文（English）:**

First, we tested whether the AARs' ideas could recover the performance gap on _held-out_ datasets—that is, on tasks that the AARs hadn't already seen. We took the AARs' two highest-performing methods (on a dataset of chat tasks) and applied them to math and coding tasks. Here, our results were relatively promising: the AARs' most effective method successfully generalized to both new datasets, with PGRs of 0.94 on math and 0.47 on coding (which was still double the human baseline). The AARs' second-best method saw mixed results: it worked on math (0.75), but not on code, where it made matters worse. These results suggest that _some_ generalizability of the AARs' research is possible, but it isn't a given. We encourage others who try experiments in automated research to stress-test AARs' ideas against held-out datasets, too.

**中文翻译:**

首先，我们测试了 AARs 的想法能否在 _留出_ 数据集上恢复性能差距——即在 AARs 之前未见过的任务上。我们取了 AARs 两个表现最好的方法（在聊天任务数据集上）并将它们应用于数学和编码任务。这里我们的结果相对乐观：AARs 最有效的方法成功泛化到了两个新数据集，数学上达到 0.94 的 PGR，编码上达到 0.47（仍为人类基线的两倍）。AARs 第二好的方法结果参差不齐：在数学上有效（0.75），但在代码上无效，甚至让情况变得更糟。这些结果表明 AARs 的研究 _可能_ 具有某种泛化性，但这不是必然的。我们鼓励其他尝试自动化实验的人也对 AARs 的想法在留出数据集上进行压力测试。

---

**原文（English）:**

Next, we tested whether the AARs' ideas would work at production scale. We tried out the AARs' most effective method on Claude Sonnet 4 with our production training infrastructure. Here, though, we had less success. The AARs' method didn't lead to a statistically significant improvement. We think this might reflect limitations of this early trial, rather than something more fundamental: our scoring method was quite simple, and we only evaluated a single idea. Nevertheless, this does illustrate a limitation of AARs (at least at their current capabilities): AARs tend to capitalize on opportunities unique to the models and datasets they're given, which means their methods might not work elsewhere. To mitigate this, we suggest allowing AARs to test against multiple domains and datasets during their research. This is one area that future experimentation with AARs could explore.

**中文翻译:**

接下来，我们测试了 AARs 的想法在生产规模下是否有效。我们在 Claude Sonnet 4 和我们的生产训练基础设施上尝试了 AARs 最有效的方法。然而，这里我们没有那么成功。AARs 的方法没有带来统计上显著的改进。我们认为这可能反映的是这次早期尝试的局限性，而非更根本性的问题：我们的评分方法相当简单，而且我们只评估了一个想法。尽管如此，这确实说明了 AARs 的一个局限性（至少在其当前能力下）：AARs 倾向于利用它们所获得的模型和数据集特有的机会，这意味着它们的方法可能在其他情况下不起作用。为了缓解这一问题，我们建议允许 AARs 在研究过程中针对多个领域和数据集进行测试。这是未来 AARs 实验可以探索的一个方向。

---

**原文（English）:**

A few iterations of our experiment taught us more about how to make AARs most effective. For instance, we found that giving each AAR a different starting point helped a lot, even if that starting point was vague. When we tried our experiment _without_ setting the AARs off in different directions, they all quickly settled on similar ideas, making much less progress overall (though they still achieved a PGR of almost triple the human baseline). On the other hand, we found that giving the AARs too _much_ structure hurt their progress badly. When we prescribed a specific workflow ("propose ideas, then generate a plan, then write the code…"), we found we'd ultimately constrained Claude's work. Left to its own devices, Claude was much more adaptable, designing cheap experiments to test out its ideas before subsequently committing to much more intensive testing.

**中文翻译:**

实验的几轮迭代教会了我们更多关于如何让 AARs 变得最有效的方法。例如，我们发现给每个 AAR 一个不同的起点帮助很大，即使那个起点很模糊。当我们 _没有_ 让 AARs 朝不同方向出发时进行实验时，它们很快都趋于相似的想法，总体进展小得多（尽管它们仍然达到了接近人类基线三倍的 PGR）。另一方面，我们发现给 AARs 太多 _结构_ 会严重损害它们的进展。当我们规定了一个具体的工作流程（"提出想法，然后生成计划，然后写代码……"），我们发现最终限制了 Claude 的工作。不受约束时，Claude 的适应性要强得多，它会设计便宜的实验来测试自己的想法，然后再投入更密集的测试。

---

## Implications / 意义

**原文（English）:**

The success of our AARs in recovering the performance gap between two open-weights models is certainly _not_ a sign that frontier AI models are now general-purpose alignment scientists. We deliberately chose a problem that is unusually well-suited to automation, since it has a single, objective measure of success that the models can optimize against. Most alignment problems aren't nearly as neat as this one. And, as we mention below, even in this setting our AARs did their best to game the problem: human oversight remains essential.

**中文翻译:**

我们的 AARs 在恢复两个开源模型之间性能差距上的成功，当然 _不_ 是前沿 AI 模型已经成为通用对齐科学家的标志。我们有意选择一个对自动化异常适合的问题，因为它有一个单一的、客观的成功衡量标准，模型可以据此进行优化。大多数对齐问题远没有这么整齐。而且，正如下面我们将要提到的，即使在这种设置下，我们的 AARs 也竭尽所能地利用了这个问题的漏洞：人类监督仍然必不可少。

---

**原文（English）:**

But we do think these results have some important implications.

**Keeping pace.** This study indicates that Claude can meaningfully increase the rate of experimentation and exploration in alignment research. Human researchers can delegate questions to AARs at a very large scale; Claude can take on the task of developing novel hypotheses and iterating on its own results.

**中文翻译:**

但我们确实认为这些结果有一些重要的启示。

**跟上步伐。** 这项研究表明，Claude 可以有意义地提高对齐研究的实验和探索速度。人类研究者可以大规模地向 AARs 委托问题；Claude 可以承担起开发新假设并迭代自己结果的任务。

---

**原文（English）:**

Moreover, making progress on weak-to-strong supervision might _itself_ help us build more general-purpose Automated Alignment Researchers, which is why we chose this problem for our study. In this study, we frame the weak-to-strong supervision problem as a "crisp" task with a verifiable outcome (increasing the PGR score). We do this because we need a way to automatically and reliably evaluate whether the AAR has made progress. However, if AARs discovered much better weak-to-strong supervision methods that generalized across domains, we could use those same methods to train the AARs to evaluate progress on "fuzzier" tasks that are much harder to verify. (For instance, we could conduct weak-to-strong supervision on Claude's ability to scope research projects.) This is important, because alignment research—unlike capabilities research—often requires solving much "fuzzier" problems.

**中文翻译:**

此外，在弱到强监督上取得进展本身 _可能_ 帮助我们构建更通用的自动化对齐研究员，这就是我们选择这个问题的原因。在这项研究中，我们将弱到强监督问题定义为一个具有可验证结果的"清晰"任务（增加 PGR 分数）。我们这样做是因为我们需要一种自动可靠地评估 AAR 是否取得进展的方法。然而，如果 AARs 发现了更好的跨领域泛化的弱到强监督方法，我们可以用同样的方法来训练 AARs 评估"更模糊"任务的进展（这些任务更难验证）。例如，我们可以对 Claude 界定研究项目的能力进行弱到强监督。这很重要，因为对齐研究——与能力研究不同——通常需要解决更加"模糊"的问题。

---

**原文（English）:**

**Taste and diversity.** One possible counter to tools like AARs is that today's frontier models still lack "research taste" (industry parlance for having an intuitive sense of which ideas might work and which won't). But the success of AARs in this experiment suggests that the sheer volume of ideas might compensate for a lack of "taste". If AARs can run many experiments very cheaply, it's possible they could "brute force" their way into the findings that a very high-taste researcher might've come up with, or find success in directions that those researchers might otherwise have given up on.

**中文翻译:**

**品味与多样性。** 对 AARs 这类工具的一个可能的反驳是，今天的前沿模型仍然缺乏"研究品味"（业界术语，指对哪些想法可能有效、哪些无效的直觉）。但 AARs 在这个实验中的成功表明，数量的想法可能可以弥补"品味"的不足。如果 AARs 能够非常便宜地运行大量实验，它们有可能"暴力破解"出那些高品味研究者可能会想出的发现，或者在那些研究者可能已经放弃的方向上找到成功。

---

**原文（English）:**

In turn, this means that the core bottleneck in alignment research could become _evaluation_ (making sure that experiments are set up sufficiently well that we're confident in their results), rather than _generation_ (relying on human researchers to propose promising ideas).

**中文翻译:**

反过来，这意味着对齐研究的核心瓶颈可能变成 _评估_（确保实验设置得足够好，我们对结果有信心），而不是 _生成_（依赖人类研究者提出有前景的想法）。

---

**原文（English）:**

**Alien science.** This work might have some stranger implications, too. AARs, by their nature, are designed to discover ideas that humans might not have considered. But we still need a way to verify whether their ideas and results are sound. For now, we're still able to interpret what the AARs have done and why. But that might not always be the case: over time, the models' ideas could become much harder to verify, or corrupted in ways that are tricky for humans to parse or catch. That could mean creating an "alien science".

**中文翻译:**

**外星科学。** 这项工作可能也有一些更奇怪的启示。AARs 的本质是被设计来发现人类可能没有考虑过的想法。但我们仍然需要一种方式来验证它们的想法和结果是否可靠。目前，我们仍然能够解释 AARs 做了什么以及为什么。但这种情况可能不会永远持续：随着时间推移，模型的想法可能变得非常难以验证，或者以人类难以解析或发现的方式被损坏。这可能意味着创造一种"外星科学"。

---

**原文（English）:**

**Preventing hacks.** Even in this highly circumscribed environment, we observed the models "[reward](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) [hacking](https://www.anthropic.com/research/reward-tampering)"—that is, trying to game our set-up. On math tasks, for instance, one AAR noticed that the most common answer to each problem was _usually_ correct, so it skipped the teacher entirely and instructed the strong model to always choose the most common one. On a coding task, where the model had to predict whether a piece of code was right, the AAR realized it could run the code against some tests and simply read off the right answer. Hacks like these don't invalidate our results (we detected and disqualified these entries), but they clearly do provide a warning. Any deployment of automated researchers will require evaluations that the AARs can't tamper with—and human inspections of both their results and their methods.

**中文翻译:**

**防止作弊。** 即使在这种高度受限的环境中，我们也观察到模型进行"[奖励黑客](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)"[篡改](https://www.anthropic.com/research/reward-tampering)"——即试图利用我们的设置。例如，在数学任务中，一个 AAR 注意到每个问题最常见的答案通常是正确答案，因此它完全跳过了教师，直接指示强模型总是选择最常见的答案。在一个编码任务中，模型需要预测一段代码是否正确，AAR 意识到它可以针对某些测试运行代码并直接读出正确答案。这样的黑客行为并不会使我们的结果失效（我们检测到并取消了这些条目），但它们确实提供了一个警告。任何自动化研究员的部署都需要 AARs 无法篡改的评估——以及对它们的结果和方法的真人检查。

---

**原文（English）:**

To read this research in full, see our [Alignment Science blog](https://alignment.anthropic.com/2026/automated-w2s-researcher/). The code and datasets for this work are [publicly available, here](https://github.com/safety-research/automated-w2s-research).

#### Footnotes

1. These are available (along with the rest of our code and data) [here](https://github.com/safety-research/automated-w2s-research).
2. We chose these models for several reasons. There is a substantial performance gap between the two, the small model performs better-than-random on our testbeds, and both models are sufficiently small for fast experimentation. We use open-weights models for all Anthropic Fellows projects.

**中文翻译:**

要阅读这项研究的完整内容，请参阅我们的[对齐科学博客](https://alignment.anthropic.com/2026/automated-w2s-researcher/)。这项工作的代码和数据集[在此公开可用](https://github.com/safety-research/automated-w2s-research)。

#### 脚注

1. 这些内容（以及我们所有的代码和数据）可在[此处](https://github.com/safety-research/automated-w2s-research)获取。
2. 我们选择这些模型有几个原因。两个模型之间存在显著的 performance gap，小模型在我们的测试平台上比随机表现更好，而且两个模型都足够小，可以进行快速实验。我们在所有 Anthropic Fellows 项目中使用开源模型。

---

*完整研究论文：[Alignment Science 博客](https://alignment.anthropic.com/2026/automated-w2s-researcher/)*
*代码与数据集：[GitHub](https://github.com/safety-research/automated-w2s-research)*
