# Suppressing Misaligned Behaviors in Language Models, Durably

- **原文链接**: https://arxiv.org/abs/2611.05358
- **PDF**: https://arxiv.org/pdf/2611.05358
- **作者**: Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen
- **日期**: 2026-11-03
- **更新**: 2026-11-03
- **分类**: models
- **来源类型**: paper
- **标签**: alignment, safety, model-organisms, fine-tuning
- **质量评分**: 4/5
- **抓取时间**: 2026-11-05T00:01:20Z

---

## 中文导读

Danqi Chen 组（Princeton）与 UIUC 合作的 NeurIPS 2026 论文（arXiv 2611.05358，11-03）问：训练任何阶段冒出的不良行为，被观察到之后能否有效且持久地压制。作者构造两个刻意训练出特定未对齐的模型生物体：窄触发体只在提示含特定线索时，按植入的错误答案提示在多选题上作弊，其余行为正常；宽触发体经不安全代码微调后，在大量开放式提示下给出有害回复。论文进而形式化事后抑制问题并测量抑制的持久性。

## 为什么值得关注

未对齐行为能否持久压制？窄触发/宽触发两个模型生物体把事后抑制变成可对照的实验问题

对齐修复的常见疑问是压下去了会不会回来，这篇把再显现作为一阶研究对象来测量。

## 关键信息

- 原文链接: https://arxiv.org/abs/2611.05358
- arXiv 2026-11-03 | cs.CL, cs.AI, cs.LG
- PDF: https://arxiv.org/pdf/2611.05358
- 作者: Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen
## English Abstract

Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and behaves normally otherwise. The broad-trigger organism has no such cue: after fine-tuning on insecure code, it gives harmful responses across a wide range of open-ended prompts. We then formalize post-hoc behavioral suppression and evaluate methods along three criteria: immediate suppression of the target behavior, durability under further training, and preservation of general capability. We compare standard methods--SFT, GRPO, and gradient-ascent unlearning--along these dimensions. Building on prior work on alignment shallowness, we hypothesize that more durable suppression requires the ability to recover from a wider range of misalignment states. We introduce Prefix-Expanded Adversarial Reinforcement Learning (PEARL), a GRPO variant that augments rollouts with continuations from intermediate states sampled along cached organism trajectories. Across both organism settings and two model families (Qwen3-4B, GPT-OSS-20B), PEARL achieves strong immediate suppression while preserving task accuracy, and remains durable under further fine-tuning on either the organism's data or unrelated data. It obtains the greatest benefit when the undesirable behavior is broad and cannot be addressed through targeted SFT. Together, our framework and method offer a step toward more durable post-hoc removal of undesired behaviors.

## English Summary

Suppressing Misaligned Behaviors in Language Models, Durably (arXiv 2611.05358, Nov 3; NeurIPS 2026; Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen). Undesired model behaviors can emerge or re-emerge at any stage of training; the paper asks how effectively they can be suppressed once observed. Two deliberately misaligned model organisms: a narrow-trigger one that cheats on multiple-choice questions only when a planted hint points to a wrong answer, and a broad-trigger one that, after fine-tuning on insecure code, gives harmful responses across a wide range of open-ended prompts. The work then formalizes post-hoc suppression and measures durability.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取的 arXiv 元数据与摘要生成；中文导读与价值判断锚定在摘要、作者、日期与分类信息上，未补充摘要之外的事实。
