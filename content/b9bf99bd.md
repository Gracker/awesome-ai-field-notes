# Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching

- **ID**: b9bf99bd
- **原文链接**: https://arxiv.org/abs/2611.23229
- **PDF**: https://arxiv.org/pdf/2611.23229v1
- **作者**: Giannis Daras, Marios Papachristou, Adam Klivans, Antonio Torralba, Constantinos Daskalakis
- **日期**: 2026-11-17
- **更新**: 2026-11-17
- **分类**: models
- **来源类型**: paper
- **标签**: sft, fine-tuning, distillation, post-training, catastrophic-forgetting
- **质量评分**: 4/5
- **抓取时间**: 2026-11-19T12:23:46Z

---

## 中文导读

SFT 数据集远小于预训练语料，导致过拟合和分布尾部的灾难性遗忘。Ambient SFT 把冻结的预训练模型当作噪声教师，要求后训练模型的高温条件分布与预训练模型的高温版本匹配，以此利用“不完美预测”扩充微调信号；温度超参控制对预训练模型的信任度，T→∞ 退化为普通 SFT，T=1 等价知识蒸馏。在领域适配、指令微调与推理上均优于标准 SFT，平均相对提升最高 21%。

## 为什么值得关注

不动数据、只改分布匹配目标，把“多信预训练模型一点”变成单一可调超参，落在 SFT 与蒸馏之间的连续谱上；对后训练数据永远不够用的团队，这是一条低成本抗遗忘路线。

arXiv 2026-11 后训练方法研究：Giannis Daras、Marios Papachristou、Adam Klivans、Antonio Torralba、Constantinos Daskalakis 合作，把监督微调重新表述为高温分布匹配问题；论文标注 work in progress。

## 关键信息

- 论文标题：Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching
- 作者：Giannis Daras, Marios Papachristou, Adam Klivans, Antonio Torralba, Constantinos Daskalakis
- arXiv: https://arxiv.org/abs/2611.23229
- 发布时间：2026-11-17
- arXiv 分类：cs.LG, cs.AI, cs.CL
- 关联标签：sft, fine-tuning, distillation, post-training, catastrophic-forgetting
- 备注：Work in progress

## English Abstract

Collecting large-scale, diverse, and high-quality post-training datasets for autoregressive language models is challenging. Consequently, Supervised Fine-Tuning (SFT) is typically applied to datasets significantly smaller than those used for pre-training, which leads to overfitting and the catastrophic forgetting of the tails of the data distribution. To prevent this collapse, we introduce Ambient SFT, a principled framework for leveraging imperfect predictions to augment the fine-tuning set. In our method, a "frozen" version of the pre-trained model serves as a noisy teacher that the fine-tuned model must match at a coarse level. In particular, we require that the high-temperature versions of the conditional distributions produced by the post-training model should match the high-temperature versions of the pre-training ones. The temperature hyperparameter controls the level of trust in the pre-trained model, with the limit $T\to \infty$ reverting back to regular SFT and $T=1$ to knowledge distillation. We demonstrate that our approach outperforms standard SFT across domain adaptation, instruction-tuning, and reasoning, leading for up to $21\%$ average relative improvement to standard SFT.

## English Summary

Supervised fine-tuning datasets are far smaller than pre-training corpora, causing overfitting and catastrophic forgetting of the data distribution's tails. Ambient SFT treats a frozen copy of the pre-trained model as a noisy teacher that the fine-tuned model must match at a coarse level: the high-temperature versions of the post-training model's conditional distributions must match the high-temperature versions of the pre-training ones. The temperature hyperparameter sets how much to trust the pre-trained model, with T→∞ recovering standard SFT and T=1 reducing to knowledge distillation. Across domain adaptation, instruction tuning, and reasoning, the approach outperforms standard SFT with up to 21% average relative improvement, giving a data-efficient way to post-train without losing the pre-trained distribution's tails.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
