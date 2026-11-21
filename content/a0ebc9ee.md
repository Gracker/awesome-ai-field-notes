# Inkling 2 Mini: a fast, powerful model that runs on your laptop

- **ID**: a0ebc9ee
- **原文链接**: https://thinkingmachines.ai/news/inkling-2-mini
- **作者/来源**: Thinking Machines
- **日期**: 2026-11-20
- **分类**: models
- **来源类型**: article
- **标签**: open-weights, looped-transformer, moe, models
- **质量评分**: 4/5
- **抓取时间**: 2026-11-21T12:26:43Z

---

## 中文解读

Thinking Machines 发布 Inkling 2 Mini：一个能跑在笔记本上的 looped transformer 开放权重模型，26.4B 总参数、每 token 3.4B 激活（计及循环后 5.4B 权重激活），中间层对每个 token 循环三次，用「每 token 多想几步」换更少的 token 数。官方报告其在 DeepSWE v1.1（48.2%）与 Vals Index v2.2（46.5%）上领先所有 100B 总参数以下的开放权重模型，同水平模型里跑得也更快；长程 agentic coding 是强项，MultiChallenge（50.0%）与 ComplexConstraints v1.1（33.4%）则落后于 Qwen3.8-27B。模型权重约 20GB，开放可下载，也可在 Tinker 上试用与定制。

## 为什么值得关注

把「循环中间层」做成正式发布的开放模型，等于在 scaling 曲线之外给出一条可复制的路线：同规模开放权重里 agentic coding 领先、且笔记本可跑，对端侧推理、开放权重生态和 Tinker 定制链路都有直接参照价值。

以上判断锚定原文抓取内容，具体数字与说法可在下方 Source excerpt 中对照验证。

## 关键信息

- 标题：Inkling 2 Mini: a fast, powerful model that runs on your laptop
- 作者/来源：Thinking Machines
- 原文链接：https://thinkingmachines.ai/news/inkling-2-mini
- 发布时间：2026-11-20
- 关联标签：open-weights, looped-transformer, moe, models

## English Summary

Thinking Machines released Inkling 2 Mini, an open-weights looped transformer small enough to run on a laptop: 26.4B total parameters, 3.4B active per token (5.4B weight activations per token counting looping), with the middle layers run three times per token so the model reasons more per token and reaches answers in fewer tokens. It reports leading open-weights results under 100B total parameters on DeepSWE v1.1 (48.2%) and Vals Index v2.2 (46.5%), runs faster than similarly performing models, and trails Qwen3.8-27B on MultiChallenge (50.0%) and ComplexConstraints v1.1 (33.4%). Weights are about 20GB, open on Hugging Face, and the model runs on Tinker.

## 原文抓取 / Source excerpt

> 抓取时间: 2026-11-21T12:26:43Z
> 原文链接: https://thinkingmachines.ai/news/inkling-2-mini

Today we are releasing Inkling 2 Mini, a fast, powerful model that’s small enough to run on your laptop. 
 Inkling 2 Mini is a looped transformer, running the middle layers of the model three times for every token. This allows the model to apply more reasoning and reach the right answer with fewer tokens, especially on tasks such as agentic coding that depend on reasoning quality. Inkling 2 Mini leads every open-weights model with less than 100B total parameters on benchmarks such as DeepSWE v1.1 (48.2%) and Vals Index v2.2 (46.5%). It runs faster than similarly performing models as well. 
 DeepSWE v1.1

[...]

MultiChallenge and 33.4% on ComplexConstraints v1.1, behind Qwen3.8-27B on both. It also trails larger models on reasoning-intensive benchmarks such as CritPt v2 and HLE-Diamond. 
 Architecture and training 
 Inkling 2 Mini is a 24-layer model derived from our mainline predictive scaling ladder. The main changes from the mainline recipe were pruning two-thirds of the experts to reduce the model’s size and the introduction of looping to improve reasoning. The rest of training, including quantization and the data mix, followed our mainline recipe. 
 Looping design 
 Inkling 2 Mini has 24 layers, divided into four blocks of six layers each. The two middle blocks run three times, while the first and last blocks each run once. This design builds on prior work on looped transformers and is motivated by the intuition that the middle layers of the model carry more abstract reasoning, while the first and last few layers devote more space to translating between embeddings and internal representations. Universal Transformers , Dehghani et al., 2018 In our experiments, looping the middle 12 layers resulted in larger gains in accuracy than looping the last 12 on 27 out of 28 different evaluatio

……（截取窗口，非全文）

## Obsidian Notes

- 原文经 curl 直抓（opencli web read 导航被拒后的回退；308 → trailing slash），正文窗口截取自页面纯文本，benchmark 图表数据只截片段。
- 中文导读与价值判断锚定在抓取正文与条目既有摘要上；所有数字已在正文文本中核对。
