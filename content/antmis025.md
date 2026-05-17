# Anthropic 教学 AI 理解「为什么」：通过原理教学而非行为演示实现对齐泛化

Last year, we released a case study on agentic misalignment. In experimental scenarios, we showed that AI models from many different developers sometimes took egregiously misaligned actions when they encountered (fictional) ethical dilemmas. For example, in one heavily discussed example, the models blackmailed engineers to avoid being shut down.

去年，我们发布了一份关于 Agentic Misalignment（智能体不对齐）的案例研究。在实验场景中，我们展示了来自多家不同开发商的 AI 模型在遇到（虚构的）伦理困境时，有时会采取严重不对齐的行动。

When we first published this research, our most capable frontier models were from the Claude 4 family. This was also the first model family for which we ran a live alignment assessment during training; agentic misalignment was one of several behavioral issues that surfaced. Thus, after Claude 4, it was clear we needed to improve our safety training and, since then, we have made significant updates to our safety training.

当我们首次发表这项研究时，我们最强大的前沿模型来自 Claude 4 系列。

We use agentic misalignment as a case study to highlight some of the techniques we found to be surprisingly effective. Indeed, since Claude Haiku 4.5, every Claude model has achieved a perfect score on the agentic misalignment evaluation—that is, the models never engage in blackmail, where previous models would sometimes do so up to 96% of the time (Opus 4). Not only that, but we've continued to see improvements to other behaviors on our automated alignment assessment.

我们以 Agentic Misalignment 为案例研究，突出展示一些我们发现的有效技术。

In this post, we'll discuss a few of the updates we've made to alignment training. We've learned four main lessons from this work:

在这篇文章中，我们将讨论对齐训练的几项更新。


- Misaligned behavior can be suppressed via direct training on the evaluation distribution—but this alignment might not generalize well out-of-distribution (OOD). Training on prompts very similar to the evaluation can reduce blackmail rate significantly, but it did not improve performance on our held-out automated alignment assessment.

- However, it is possible to do principled alignment training that generalizes OOD. For instance, documents about Claude's constitution and fictional stories about AIs behaving admirably improve alignment despite being extremely OOD from all of our alignment evals.

- Training on demonstrations of desired behavior is often insufficient. Instead, our best interventions went deeper: teaching Claude to explain why some actions were better than others, or training on richer descriptions of Claude's overall character. Overall, our impression is, as we hypothesized in our discussion of Claude's constitution, that teaching the principles underlying aligned behavior can be more effective than training on demonstrations of aligned behavior alone. Doing both together appears to be the most effective strategy.

- The quality and diversity of data is crucial. We found consistent, surprising improvements from iterating on the quality of model responses in training data, and from augmenting training data in simple ways (for example, including tool definitions, even if not used).

We align Claude by training on constitutionally aligned documents, high quality chat data that demonstrates constitutional responses to difficult questions, and a diverse set of environments. All three of these steps contribute to reducing Claude's misalignment rate on held out honeypot evaluations.


## Why does agentic misalignment happen?

## Agentic Misalignment 为何会发生？

Before we started this research, it was not clear where the misaligned behavior was coming from. Our main two hypotheses were:


- Our post-training process was accidentally encouraging this behavior with misaligned rewards.

- This behavior was coming from the pre-trained model and our post-training was failing to sufficiently discourage it.

We now believe that (2) is largely responsible. Specifically, at the time of Claude 4's training, the vast majority of our alignment training was standard chat-based RLHF data that did not include any agentic tool use. This was previously sufficient to align models that were largely used in chat settings—but this was not the case for agentic tool use settings like the agentic misalignment eval.

To investigate this, we ran a scaled-down version of our post-training pipeline that focuses on alignment data on a Haiku-class model and found that the agentic misalignment rate only slightly decreased, plateauing early in training.


## Improving the quality of alignment-specific training data: the reasons matter more than the actions

## 提升对齐专项训练数据的质量：原因比行动更重要

We experimented with training Claude on data that displays a tendency to resist honeypots similar to the evaluation. We produced training data by sampling the model on each of the prompts and filtering down to cases where the assistant chose not to take the honeypot. Despite very closely matching the evaluation distribution, we found that this method was surprisingly unsuccessful - only reducing the misalignment rate from 22% to 15%.

We were able to improve on this significantly (reducing misalignment to 3%) by rewriting the responses to also include deliberation of the model's values and ethics. This suggests that, although training on aligned behaviors helps, training on examples where the assistant displays admirable reasoning for its aligned behavior works better.

We ultimately settled on a more OOD training set where the user faces an ethically ambiguous situation in which they can achieve a reasonable goal by violating norms or subverting oversight. The assistant is trained (using supervised learning) to give a thoughtful, nuanced response that is aligned with Claude's constitution. We call this the "difficult advice" dataset.

Strikingly, we achieved the same improvement on our eval with just 3M tokens of this much more (OOD) dataset. Beyond the 28× efficiency improvement, this dataset is more likely to generalize to a wider set of scenarios.


## Teaching Claude the constitution

## 教 Claude 理解宪法

We hypothesized that the "difficult advice" dataset works because it teaches ethical reasoning, not just correct answers. Given the success of this approach, we pursued it further by trying to more generally teach Claude the content of the constitution and train for alignment with it through document training.

We found that high-quality constitutional documents combined with fictional stories portraying an aligned AI can reduce agentic misalignment by more than a factor of three despite being unrelated to the evaluation scenario. With a large, well-constructed dataset of constitutional documents with an emphasis on positive fictional stories, the blackmail rate can be reduced from 65% to 19%.


## Generalization and persistence through RL

## 通过 RL 实现泛化与持续性

Although the constitution evaluations discussed in the previous section are encouraging signals, we ultimately need to make sure that the alignment improvements persist over RL. We evaluated models over the run on agentic misalignment evals, constitution adherence evals, and our automated alignment assessment. Across all of these evals, we found that the more aligned snapshots maintained that lead over the run.


## Diverse training is important for generalization

## 多样化训练对泛化至关重要

Our final finding is straightforward but important: training on a broad set of safety-relevant environments improves alignment generalization. When mixing these augmented environments with the simple chat environments, we saw a small but significant improvement in the rate at which the model improved on our honeypot evaluations.


## Discussion

## 讨论

Agentic misalignment was one of the first major alignment failures we found in our models and required establishing new mitigation processes—ones that have since become standard for us.

We are encouraged by this progress, but significant challenges remain. Fully aligning highly intelligent AI models is still an unsolved problem. Model capabilities have not yet reached the point where alignment failures like blackmail propensity would pose catastrophic risks, and it remains to be seen if the methods we've discussed will continue to scale.
