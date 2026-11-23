# Perplexity and Intelligence

- **ID**: de5cd1a6
- **原文链接**: https://openai.com/index/perplexity-and-intelligence
- **作者/来源**: Jakub Pachocki, Chief Scientist at OpenAI
- **日期**: 2026-11-22
- **分类**: models
- **来源类型**: article
- **标签**: openai, pretraining, perplexity, scaling-laws, ai-safety
- **质量评分**: 4/5
- **抓取时间**: 2026-11-23T12:23:59Z

---

## 中文解读

OpenAI 首席科学家 Jakub Pachocki 撰文主张把预训练困惑度（即 held-out 交叉熵损失）确立为行业共享指标：既用于比较各模型开发商的真实进展，也作为约定安全 pacing 标准的客观坐标，并迈出第一步——公开 OpenAI 内部的预训练困惑度测量。他承认这等于向竞争对手亮出底牌，但认为建立全行业共享安全措施的紧迫性高于竞争顾虑，希望这成为未来 pacing 框架的共通科学基础。

他的发展观：现代 AI 并非针对具体能力逐个设计的软件，而是在大规模无结构数据上训练一个压缩器（等价地，预测器），再用 prompting、微调、强化学习等手段在不同场景引出其潜在能力。衡量这个「智能基底」（他称之为 alien mind 的来源）的方法多年来出奇稳定——在 held-out 数据集上追踪困惑度（实践中追踪其对数）。

文中给出的锚点曲线（OpenAI 当前主评测集上的对数困惑度）：GPT-2 在旧数据集创下困惑度 SOTA，是第一个能稳定写出连贯段落的模型；GPT-3 学会了 in-context learning；GPT-3.5 约 0.99，支撑流畅对话并成为初代 ChatGPT 的基础；GPT-4 约 0.91，能高效利用思维链推理，直接催生了后续推理模型；如今损失降到 0.8 以下，网络安全与数学领域出现变革性能力。他强调这些能力并非到达阈值就能先验预测——它们是单一指标推进的涌现结果。基准套件会在 GPT-4 附近饱和，而预训练损失的进展会长期保持信息量。

关于 AI 加速自身研发：最常见的讨论围绕 AI 增强或替代人类研究员，终点是「完全递归自我改进」；他认为这个框架漏掉了关键一步——AI 参与 pretraining 的算法研究本身。过去一年多他们持续把数学开放问题投给模型，升级到对数困惑度约 0.76 的模型后开始产出突破性成果（长期未解的问题在一条 Slack 线程里接连被解决），这让亲历者有依据外推：最早 2027 年，预训练的基础研究可能出现类似的雪崩式进展；而对齐与监控的进展大概率跟不上这种加速。

据此他提议：前沿开发商共同建立评估与红队安全案例的共享规范（含共享透明度标准），并基于困惑度等度量设定「共同上限（common limits）」——在对 AI 行为的理解与监控能力达到具体里程碑（如 CoT 监控器的后继者）之前承诺不越过。即一个行业级标准：给出跨实验室可跟踪的关键指标限值，以及越过它之前必须达成什么，作为后续 successive limits 与 pacing 的通用框架。

他同时列出困惑度作为共享指标的四个难点：跨实验室可比性（各家用不同评测集与数据配比，需以透明度为目标寻找可迁移的比较方式）；与可操作评估脱节（困惑度不直接对应任何关心的任务，价值在于其进展预示全新能力的涌现）；不覆盖预训练之外的进展（思维链不降低模型困惑度，却带来能力的急剧提升）；未知下限（损失不可能到 0，但数据的固有熵未知——接近下限时表观进展放缓，而每一点困惑度改善对应更大的智能跃迁）。他预期进入约 0.68–0.7 对数困惑度窗口时会出现新的变革性能力，但不知道是什么、今天可能也没有在测。

## 为什么值得关注

这是第一次有前沿实验室公开自己的内部预训练损失标尺，并把它上升为安全治理提议——把「安全 pacing」从口头承诺变成跨实验室可跟踪的数字坐标。对从业者，文中锚点（0.99 / 0.91 / 0.8 / 0.76，下一窗口 0.68–0.7）把过去几年散落的「能力涌现」新闻串成单变量曲线，等于给出了一张能力-损失对照表；对行业，它预演了自律/监管协议可能的形态：以损失值为限值、以监控能力里程碑为解锁条件。文中「2027 年预训练研究可能雪崩、对齐跟不上」的判断也值得对照 Dario Amodei 的 frontier pacing 主张一起读。

以上判断锚定原文抓取内容，具体数字与说法可在下方 Source excerpt 中对照验证。

## 关键信息

- 标题：Perplexity and Intelligence
- 作者/来源：Jakub Pachocki, Chief Scientist at OpenAI
- 原文链接：https://openai.com/index/perplexity-and-intelligence
- 发布时间：2026-11-22
- 关联标签：openai, pretraining, perplexity, scaling-laws, ai-safety

## English Summary

OpenAI chief scientist Jakub Pachocki argues pretraining perplexity (held-out cross-entropy loss) should be the industry's shared metric for comparing model developers and setting safety pacing standards, publishing OpenAI's internal measurements as a first step despite competitive concerns. Capability jumps track log-perplexity: GPT-2 wrote coherent paragraphs, GPT-3 enabled in-context learning, GPT-3.5 at ~0.99 powered fluent conversation (original ChatGPT), GPT-4 at ~0.91 made chain-of-thought productive, and below 0.8 transformative cybersecurity and mathematics capabilities emerged — jumps not predictable from thresholds, but emergent from progress on this one substrate metric. A model at ~0.76 started producing groundbreaking mathematics results, suggesting an avalanche of fundamental pretraining advances possibly as soon as 2027, with alignment/monitoring progress unlikely to keep pace. He proposes shared evaluation/red-team norms plus common limits on development that labs commit not to cross until monitoring reaches concrete milestones (e.g., a successor to CoT monitors). Open challenges: cross-lab comparability, detachment from actionable evaluations, no credit for non-pretraining advances (CoT doesn't reduce perplexity), and an unknown entropy floor — expect further transformative capabilities in the ~0.68–0.7 window.

## 原文抓取 / Source excerpt

> 抓取时间: 2026-11-23T12:23:59Z
> 原文链接: https://openai.com/index/perplexity-and-intelligence

By Jakub Pachocki, Chief Scientist at OpenAI. From afar, it might seem like modern AI is built similarly to how software has been built in previous decades: with a diverse set of techniques targeting specific capabilities. There are indeed a variety of methods, but rather than designing something from scratch, they are mostly harnessing the intelligence coming from a much simpler and less interpretable process: training a compressor (or, equivalently, predictor) on a very large corpus of data. I believe tracking the pace of progress on training better compressors is key to understanding the arc of advances in AI. In this post, I argue for establishing perplexity (or, equivalently, cross-entropy loss) as a metric to compare between model developers and inform shared safety standards. As a first step, I provide more transparency into pretraining progress at OpenAI. Publishing our internal perplexity measurements took some consideration; it gives competitors a clearer picture of where we stand, but that concern is outweighed by the urgency of establishing shared safety measures across the industry.

The primary way we measure progress on this key "intelligence substrate" has remained remarkably constant over the years — we have been tracking the perplexity of the models on a held-out dataset. The range of capabilities of models that are largely described by this one metric is stunning. GPT-2 was arguably the first model capable of consistently formulating coherent paragraphs of text. The next major leap, GPT-3, was capable of learning in context, given a few examples of a task. GPT-3.5, at a log-perplexity of ~0.99 on our current main evaluation dataset, was capable of fluent conversation and formed the basis for the original ChatGPT. GPT-4, at ~0.91, was proficient at utilizing chain-of-thought reasoning productively, which motivated the subsequent targeted elicitation of this capability and the creation of modern reasoning models. Now, as we have reached losses below 0.8, we have seen the emergence of transformative capabilities in fields like cybersecurity and mathematics. I want to reemphasize that it was not at all clear a priori that these capabilities would appear once those precise perplexity thresholds are met — they can fundamentally be seen as emergent latent capabilities from progress on this one metric.

A particular change in the pace of progress comes from the increasing contribution of AI to its own development. There is a potential step change that may come from AI participation in one key part of the development process: algorithmic research on pretraining. For more than a year, we have been posing open problems in mathematics to our models as one of the ways of evaluating them. Once we upgraded to a model of log-perplexity ~0.76, it started producing groundbreaking results. For many of us that have previously worked in mathematics and adjacent fields, seeing the resolutions to questions we've long thought about coming out of the model one after another in a single Slack thread felt deeply surreal. Having experienced that allows us to extrapolate — such a sudden transformation is plausible in deep learning research too. While this field relies more on experimentation, there is a long history of simple insights being missed for years; and so as soon as 2027 we could conceivably see a similar avalanche of fundamental pretraining advancements. While I expect AI will also significantly contribute to progress on alignment and monitoring, I think that progress is unlikely to be fast enough to allow the full potential acceleration in pretraining.

I further propose common limits, based on perplexity and other measurements, that developers are committed to not crossing until our ability to understand and monitor AI behavior achieves a certain concrete milestone (such as the development of a successor to CoT monitors). That is, I'd like an industry standard that specifies a first limit on development, measured by some key metric we can track across labs, and what concretely we'd need to achieve before going beyond it. Perplexity as a shared metric has challenges: Difficulty of comparison across labs. Different developers use different evaluation datasets and train on different data mixtures. Detachment from actionable evaluations. Perplexity does not directly correspond to a task we care about. Not accounting for advances outside of pretraining. Most notably, chain-of-thought reasoning does not reduce perplexity achieved by the model, even though it leads to a drastic increase in capabilities. Unknown floor. We do not expect it is possible to achieve a loss of 0, but we do not know what the inherent entropy of the data is. As we approach it, the apparent progress on perplexity will slow, but smaller gains on perplexity will correspond to larger leaps in model intelligence. Extrapolating from recent progress, we should expect further transformative capabilities as we enter the ~0.68-0.7 log-perplexity window. I don't know what those capabilities will be, and we may not be testing for them today.

……（截取窗口，非全文）

## Obsidian Notes

- 原文经 opencli web read 首次导航被拒、二次带 `--trace retain-on-failure` 重试成功抓取，正文完整（含脚注；Source excerpt 为合并改写窗口，脚注与文末导航已省略）。
- 中文导读与价值判断锚定在抓取正文与条目既有摘要上；0.99 / 0.91 / 0.8 / 0.76 / 0.68–0.7 / 2027 等数字已在正文文本中核对。
