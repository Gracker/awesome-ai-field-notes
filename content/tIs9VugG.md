# Automated Alignment Researchers：利用大语言模型扩展可扩展监督

## 英文原文

Large language models' ever-accelerating rate of improvement raises two particularly important questions for alignment research.
One is how alignment can keep up. Frontier AI models are now contributing to the development of their successors. But can they provide the same kind of uplift for alignment researchers? Could our language models be used to help align themselves?
A second question is what we'll do once models become smarter than us. Aligning smarter-than-human AI models is a research area known as "scalable oversight". Scalable oversight has largely been discussed in theoretical, rather than practical, terms—but at AI's current pace of improvement, that might not be the case for much longer.

## 中文翻译

大语言模型不断提升的速率引发了对齐研究两个特别重要的问题。
其一，对齐研究如何跟上脚步？前沿 AI 模型正在为下一代模型的发展做出贡献。但它们能否为对齐研究人员提供同样的帮助？我们的语言模型能否用来帮助对齐自身？
其二，一旦模型变得比我们更聪明，我们将何去何从？对齐超人类 AI 模型是一个被称为"可扩展监督"的研究领域。可扩展监督在很大程度上一直是理论讨论，而非实践层面的——但按照 AI 目前的进步速度，这种情况可能不会持续太久。

---

## 英文原文

In a new Anthropic Fellows study, we pursue both of these questions.
Our new study focuses on a problem known as "weak-to-strong supervision", a problem that mirrors the one of overseeing smarter-than-human AI models. We start with a relatively strong "base" model—that is, a potentially-capable model that hasn't yet received fine-tuning to provide its best-possible answers. Then, we use a much weaker model as a "teacher" to provide that extra fine-tuning.

## 中文翻译

在一项新的 Anthropic Fellows 研究中，我们同时追求这两个问题。
我们的新研究聚焦于一个被称为"弱到强监督"的问题，这个问题与监督超人类 AI 模型的问题相似。我们从一个相对较强的"基础"模型开始——即一个可能有能力但尚未经过微调以提供最佳答案的模型。然后，我们用一个弱得多的模型作为"教师"来提供额外的微调。

---

## 英文原文

To provide a benchmark for the AARs' results, we compared their work to a human baseline. Two of our researchers spent seven days iterating on four of the most promising generalization methods from prior research. On the open-weights models we tested, the humans recovered 23% of the total performance gap (i.e., achieved a PGR of 0.23).
Claude improved on this result dramatically. After five further days (and 800 cumulative hours of research), the AARs closed almost the entire remaining performance gap, achieving a final PGR of 0.97. This cost about $18,000 in tokens and model training expenses.

## 中文翻译

为了给 AAR 的结果提供基准，我们将它们的工作与人类基线进行比较。我们的两名研究人员花费七天时间迭代了先前研究中四种最有前景的泛化方法。在我们测试的开源模型上，人类恢复了总性能差距的 23%（即实现了 0.23 的 PGR）。
Claude 大幅改进了这一结果。在又五天（以及 800 小时累计研究）后，AAR 几乎关闭了所有剩余的性能差距，达到了 0.97 的最终 PGR。这花费了约 18,000 美元的 Token 和模型训练费用。

---

## 英文原文

The success of our AARs in recovering the performance gap between two open-weights models is certainly not a sign that frontier AI models are now general-purpose alignment scientists. We deliberately chose a problem that is unusually well-suited to automation, since it has a single, objective measure of success that the models can optimize against.
But we do think these results have some important implications. This study indicates that Claude can meaningfully increase the rate of experimentation and exploration in alignment research. Human researchers can delegate questions to AARs at a very large scale; Claude can take on the task of developing novel hypotheses and iterating on its own results.

## 中文翻译

我们的 AAR 在恢复两个开源模型之间性能差距方面的成功，当然不是前沿 AI 模型已经成为通用对齐科学家的标志。我们有意选择一个异常适合自动化的的问题，因为它有一个单一的、客观的成功衡量标准，模型可以据此进行优化。
但我们确实认为这些结果具有一些重要含义。这项研究表明，Claude 可以有意义地提高对齐研究的实验和探索速度。人类研究人员可以大规模地将问题委托给 AAR；Claude 可以承担起制定新假设并迭代自身结果的任务。

---

## 英文原文

One possible counter to tools like AARs is that today's frontier models still lack "research taste" (industry parlance for having an intuitive sense of which ideas might work and which won't). But the success of AARs in this experiment suggests that the sheer volume of ideas might compensate for a lack of "taste". If AARs can run many experiments very cheaply, it's possible they could "brute force" their way into the findings that a very high-taste researcher might've come up with.
In turn, this means that the core bottleneck in alignment research could become evaluation (making sure that experiments are set up sufficiently well that we're confident in their results), rather than generation (relying on human researchers to propose promising ideas).

## 中文翻译

对 AAR 这类工具的一个可能的反驳是，当今的前沿模型仍然缺乏"研究品味"（业界术语，指的是对哪些想法可能有效、哪些无效的直觉）。但 AAR 在这项实验中的成功表明，大量想法可能弥补"品味"的缺乏。如果 AAR 能够非常便宜地运行大量实验，它们有可能通过"暴力计算"获得一位高品味研究人员可能得出的发现。
反过来，这意味着对齐研究的核心瓶颈可能变成评估（确保实验设置得足够好，使我们对结果有信心），而不是生成（依赖人类研究人员提出有前景的想法）。
