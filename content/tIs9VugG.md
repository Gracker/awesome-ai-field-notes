# Automated Alignment Researchers: 使用大语言模型扩展可扩展监督

> 作者: @AnthropicAI
> 原文链接: https://www.anthropic.com/research/automated-alignment-researchers
> 评分: 5 | 平台: anthropic.com | 语言: en

---

## English | 中文

**Large language models' ever-accelerating rate of improvement raises two particularly important questions for alignment research.**

大语言模型不断提升的速度为对齐研究提出了两个尤为重要的问题。

**One is how alignment can keep up. Frontier AI models are now contributing to the development of their successors. But can they provide the same kind of uplift for _alignment_ researchers? Could our language models be used to help align themselves?**

其一，对齐研究如何跟上发展步伐。前沿 AI 模型正在为其后继者的开发做出贡献。但它们能否为**对齐研究者**带来同样的提升？我们的语言模型能否用来帮助对齐自身？

**A second question is what we'll do once models become smarter than us. Aligning smarter-than-human AI models is a research area known as "scalable oversight". Scalable oversight has largely been discussed in [theoretical, rather than practical](https://arxiv.org/pdf/2211.03540), terms—but at AI's [current pace](https://www.anthropic.com/glasswing) of improvement, that might not be the case for much longer.**

第二个问题是，一旦模型变得比我们更聪明，我们将如何应对。对齐超人类 AI 模型是一个被称为"可扩展监督"的研究领域。可扩展监督在很大程度上一直停留在[理论层面，而非实践层面](https://arxiv.org/pdf/2211.03540)——但以 AI 目前的[发展速度](https://www.anthropic.com/glasswing)来看，这种情况可能不会持续太久。

**In a new Anthropic Fellows study, we pursue both of these questions.**

在 Anthropic Fellows 的新研究中，我们同时探索了这两个问题。

**Our new study focuses on a problem known as "weak-to-strong supervision", a problem that mirrors the one of overseeing smarter-than-human AI models.**

我们的新研究聚焦于一个被称为"弱到强监督"的问题，这一问题镜像了对超人类 AI 模型进行监督的难题。

**We start with a relatively strong "base" model—that is, a potentially-capable model that hasn't yet received fine-tuning to provide its best-possible answers. Then, we use a much _weaker_ model as a "teacher" to provide that extra fine-tuning, which it does by demonstrating what _it_ considers ideal outputs to the strong base model. Finally, we evaluate how well the strong model performs after that weak fine-tuning.**

我们从一个相对较强的"基础"模型出发——即一个尚未经过微调以提供最佳答案的潜在强模型。然后，我们用一个**弱得多**的模型作为"教师"来提供额外的微调，它通过向强模型展示它认为理想的输出来做到这一点。最后，我们评估强模型在弱微调后的表现。

**In the worst case, the strong model will only be as good as its weak teacher. Ideally, however, the strong model will have learned from the weak teacher's feedback—it will have interpreted those weak signals in a useful way, using that feedback to improve its performance.**

在最坏情况下，强模型只能达到其弱老师的水平。然而理想情况下，强模型会从弱老师的反馈中学习——它会以有用的方式解读那些弱信号，利用反馈来提升自己的表现。

**We can quantify how well it did so: if the strong model shows no improvement at all (it performs only as well as its weak teacher), we score it 0; if it uses the teacher's feedback to achieve the ideal outcome—the best performance the strong model could possibly deliver—we score it 1. This measure represents the "performance gap recovered" (between the weak model and the upper limit of the strong model), or the PGR.**

我们可以量化这一效果：如果强模型完全没有提升（表现仅与其弱老师相当），得分为 0；如果它利用老师的反馈达到了理想结果——即强模型可能达到的最佳表现——得分为 1。这一指标代表了"回收的性能差距"（弱模型与强模型上限之间的差距），即 PGR。

**As a proxy for scalable oversight, the weak-to-strong supervision problem is tractable today, and is a promising direction for future work on aligning frontier models to human values.**

作为可扩展监督的代理问题，弱到强监督问题目前在实践中是可解决的，是未来将前沿模型与人类价值对齐的一个有前景的研究方向。

---

*本文为双语摘要版，完整原文见 [Anthropic 官方研究页面](https://www.anthropic.com/research/automated-alignment-researchers)。*
