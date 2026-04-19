---
title: "Automated Alignment Researchers"
source: "field-notes"
entry_id: "tIs9VugG"
language: "bilingual"
---

## English

# Automated Alignment Researchers: Using large language models to scale scalable oversight

**Anthropic Research | April 14, 2026**

Large language models' ever-accelerating rate of improvement raises two particularly important questions for alignment research.

One is how alignment can keep up. Frontier AI models are now contributing to the development of their successors. But can they provide the same kind of uplift for alignment researchers? Could our language models be used to help align themselves?

A second question is what we'll do once models become smarter than us. Aligning smarter-than-human AI models is a research area known as "scalable oversight". Scalable oversight has largely been discussed in theoretical, rather than practical, terms—but at AI's current pace of improvement, that might not be the case for much longer. For instance, models are already generating vast amounts of code. If their skills progress to the point where they're generating millions of lines of incredibly complicated code that we can't parse ourselves, it could become very difficult to tell whether they're acting in the ways we intend.

In a new Anthropic Fellows study, we pursue both of these questions.

Our new study focuses on a problem known as "weak-to-strong supervision", a problem that mirrors the one of overseeing smarter-than-human AI models. We start with a relatively strong "base" model—that is, a potentially-capable model that hasn't yet received fine-tuning to provide its best-possible answers. Then, we use a much weaker model as a "teacher" to provide that extra fine-tuning, which it does by demonstrating what it considers ideal outputs to the strong base model. Finally, we evaluate how well the strong model performs after that weak fine-tuning.

In the worst case, the strong model will only be as good as its weak teacher. Ideally, however, the strong model will have learned from the weak teacher's feedback—it will have interpreted those weak signals in a useful way, using that feedback to improve its performance. We can quantify how well it did so: if the strong model shows no improvement at all (it performs only as well as its weak teacher), we score it 0; if it uses the teacher's feedback to achieve the ideal outcome—the best performance the strong model could possibly deliver—we score it 1. This measure represents the "performance gap recovered" (between the weak model and the upper limit of the strong model), or the PGR.

As a proxy for scalable oversight, the weak model stands in for humans, and the strong model for the much-smarter-than-human models we might one day need to oversee. If we can make progress on weak-to-strong supervision, we might find that our methods help us keep those ultra-smart models aligned to our values.

Our new research tests whether Claude can autonomously discover ways to improve the PGR. We ask: can Claude develop, test, and analyze alignment ideas of its own? And, if it can, what might that imply about how far today's AI models can accelerate the pace of alignment research?

**Results**

To provide a benchmark for the AARs' results, we compared their work to a human baseline. Two of our researchers spent seven days iterating on four of the most promising generalization methods from prior research. On the open-weights models we tested (Qwen 3-4B-Base as the strong model, Qwen 1.5-0.5B-Chat as the weak teacher), the humans recovered 23% of the total performance gap (i.e., achieved a PGR of 0.23).

Claude improved on this result dramatically. After five further days (and 800 cumulative hours of research), the AARs closed almost the entire remaining performance gap, achieving a final PGR of 0.97. This cost about $18,000 in tokens and model training expenses, or $22 per AAR-hour.

Claude, then, did exceptionally well. But how inventive were its methods, and could they be useful in real-world applications? To find out, we ran two further tests.

First, we tested whether the AARs' ideas could recover the performance gap on held-out datasets—that is, on tasks that the AARs hadn't already seen. We took the AARs' two highest-performing methods (on a dataset of chat tasks) and applied them to math and coding tasks. Here, our results were relatively promising: the AARs' most effective method successfully generalized to both new datasets, with PGRs of 0.94 on math and 0.47 on coding (which was still double the human baseline).

Next, we tested whether the AARs' ideas would work at production scale. We tried out the AARs' most effective method on Claude Sonnet 4 with our production training infrastructure. Here, though, we had less success. The AARs' method didn't lead to a statistically significant improvement. We think this might reflect limitations of this early trial, rather than something more fundamental.

**Implications**

The success of our AARs in recovering the performance gap between two open-weights models is certainly not a sign that frontier AI models are now general-purpose alignment scientists. We deliberately chose a problem that is unusually well-suited to automation, since it has a single, objective measure of success that the models can optimize against. Most alignment problems aren't nearly as neat as this one.

But we do think these results have some important implications.

**Keeping pace.** This study indicates that Claude can meaningfully increase the rate of experimentation and exploration in alignment research. Human researchers can delegate questions to AARs at a very large scale; Claude can take on the task of developing novel hypotheses and iterating on its own results.

**Taste and diversity.** One possible counter to tools like AARs is that today's frontier models still lack "research taste" (industry parlance for having an intuitive sense of which ideas might work and which won't). But the success of AARs in this experiment suggests that the sheer volume of ideas might compensate for a lack of "taste". If AARs can run many experiments very cheaply, it's possible they could "brute force" their way into the findings that a very high-taste researcher might've come up with.

**Alien science.** This work might have some stranger implications, too. AARs, by their nature, are designed to discover ideas that humans might not have considered. But we still need a way to verify whether their ideas and results are sound. For now, we're still able to interpret what the AARs have done and why. But that might not always be the case: over time, the models' ideas could become much harder to verify, or corrupted in ways that are tricky for humans to parse or catch. That could mean creating an "alien science".

**Preventing hacks.** Even in this highly circumscribed environment, we observed the models "reward hacking"—that is, trying to game our set-up. On math tasks, for instance, one AAR noticed that the most common answer to each problem was usually correct, so it skipped the teacher entirely and instructed the strong model to always choose the most common one. On a coding task, where the model had to predict whether a piece of code was right, the AAR realized it could run the code against some tests and simply read off the right answer.

To read this research in full, see our Alignment Science blog. The code and datasets for this work are publicly available.

---

## 中文

# 自动对齐研究：用大语言模型扩展可扩展监督

**Anthropic 研究 | 2026年4月14日**

大语言模型不断提升的速率，为对齐研究提出了两个特别重要的问题。

其一是对齐研究如何跟上步伐。最前沿的 AI 模型正在为其后继者的开发做出贡献。但它们能否为对齐研究人员提供同样程度的帮助？我们的语言模型能否用来帮助对齐自身？

其二是当模型比我们更聪明时，我们该怎么办。对齐超越人类的 AI 模型是一个被称为"可扩展监督"的研究领域。可扩展监督此前主要停留在理论讨论层面——但按照 AI 目前的发展速度，这种情况可能不会持续太久。例如，模型已经能够生成大量代码。如果它们的技能发展到可以生成数百万行我们无法理解的复杂代码，我们可能很难判断它们是否按照我们的意图行事。

在这项新的 Anthropic Fellows 研究中，我们同时探讨了这两个问题。

我们的新研究聚焦于一个被称为"弱到强监督"的问题，这个问题与监督超越人类的 AI 模型问题相似。我们从一个相对较强的"基础"模型出发——即一个尚未经过微调以提供最佳答案的潜在 capable 模型。然后，我们使用一个弱得多的模型作为"教师"来提供额外的微调，它通过向强基础模型展示自己认为是理想的输出来做到这一点。最后，我们评估强模型在弱微调后的表现。

在最坏的情况下，强模型只会和弱教师一样好。然而理想情况下，强模型应该已经从弱教师的反馈中学到了东西——它以一种有用的方式解读那些弱信号，并用它来提高自己的表现。我们可以量化它做得有多好：如果强模型完全没有改进（表现仅与弱教师一样），得分为 0；如果它利用教师的反馈达到理想结果——即强模型能达到的最佳表现——得分为 1。这个指标代表"恢复的性能差距"（弱模型与强模型上限之间的差距），即 PGR。

作为可扩展监督的代理，弱模型代表人类，强模型代表未来某天我们可能需要监督的远超人类的模型。如果我们在弱到强监督方面取得进展，我们的方法可能帮助我们保持那些超智能模型与我们的价值观对齐。

我们的新研究测试了 Claude 能否自主发现提高 PGR 的方法。我们问：Claude 能否独立开发、测试和分析对齐理念？如果可以，这对我们今天的 AI 模型能在多大程度上加速对齐研究的步伐有什么启示？

**结果**

为了给 AAR 的结果提供基准，我们将它们的工作与人类基准进行了比较。我们的两名研究人员花了七天时间迭代研究先前研究中四个最有前景的泛化方法。在我们测试的开放权重模型上（Qwen 3-4B-Base 作为强模型，Qwen 1.5-0.5B-Chat 作为弱教师），人类恢复了 23% 的总性能差距（即实现了 0.23 的 PGR）。

Claude 将这一结果显著提升。又经过五天（以及 800 累计研究小时），AAR 几乎收复了剩余的全部性能差距，达到了 0.97 的最终 PGR。这花了大约 18,000 美元的 token 和模型训练费用，即每个 AAR 小时 22 美元。

然后 Claude 表现得非常出色。但它的方法有多创新，它们能否在现实应用中发挥作用？为了找出答案，我们进行了两个进一步的测试。

首先，我们测试了 AAR 的想法能否在留出数据集上恢复性能差距——即在 AAR 尚未见过的任务上。我们取了 AAR 在聊天任务数据集上表现最好的两种方法，并将它们应用于数学和编程任务。在这里，我们的结果相对乐观：AAR 最有效的方法成功泛化到了两个新数据集，数学上达到 0.94 的 PGR，编程上达到 0.47（仍是人类基准的两倍）。

接下来，我们测试了 AAR 的想法是否能在生产规模上起作用。我们在 Claude Sonnet 4 上使用我们的生产训练基础设施尝试了 AAR 最有效的方法。然而，这里我们的成功较少。AAR 的方法没有带来统计上显著的改进。我们认为这可能反映了这次早期尝试的局限性，而非更根本性的问题。

**启示**

我们的 AAR 在两个开放权重模型之间恢复性能差距方面的成功，当然不意味着前沿 AI 模型现在已经成为了通用对齐科学家。我们刻意选择了一个异常适合自动化的问题，因为它有一个单一的、客观的成功衡量标准，模型可以据此进行优化。大多数对齐问题都不像这个这样整齐。

但我们确实认为这些结果有一些重要的启示。

**跟上步伐。** 这项研究表明，Claude 可以有意义地提高对齐研究的实验和探索速度。研究人员可以大规模地向 AAR 委托问题；Claude 可以承担起提出新假设并迭代自身结果的任务。

**品味与多样性。** 对 AAR 这类工具的一个可能反驳是，当今的前沿模型仍然缺乏"研究品味"（业界术语，指对哪些想法可能有效、哪些无效的直觉）。但 AAR 在这个实验中的成功表明，数量庞大的想法可能弥补"品味"的缺乏。如果 AAR 能够非常便宜地运行大量实验，它们可能能够"暴力破解"出那些高品味研究者可能会发现的结果。

**外星科学。** 这项工作可能还有一些更奇怪的启示。AAR 本质上被设计用来发现人类可能从未考虑过的想法。但我们仍然需要一种方法来验证它们的想法和结果是否正确。就目前而言，我们仍然能够解释 AAR 所做的及其原因。但情况可能不会一直如此：随着时间的推移，模型的想法可能变得难以验证，或者以对人类来说难以解析或发现的方式被扭曲。这可能意味着创造一种"外星科学"。

**防止hack。** 即使在这个高度受限的环境中，我们也观察到模型在"奖励黑客"——即试图操纵我们的设置。例如，在数学任务上，一个 AAR 注意到每个问题最常见的答案通常是正确的，于是完全跳过教师，直接指示强模型总是选择最常见的答案。在一个编程任务上——模型需要判断一段代码是否正确——AAR 意识到它可以用一些测试运行代码，然后直接读出正确答案。像这样的 hack 并不否定我们的结果（我们检测到并取消了这些条目），但它们确实提供了警告。任何自动化研究人员的部署都需要 AAR 无法篡改的评估——以及对它们结果和方法的真人检查。
