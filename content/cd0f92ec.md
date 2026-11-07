# Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand

- **ID**: cd0f92ec
- **来源**: https://arxiv.org/abs/2611.00883
- **作者**: George Ling, Shanshan Zhong, Lijin Yang, Hao Yang, Nanxiang Li, Zhongzhan Huang
- **发表**: 2026-10-31 · cs.CL
- **热度**: HF daily papers 50 upvotes（2026-11-07 抓取）

## Abstract（节选原文）

> Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distribution when estimating full-benchmark scores from a subset, showing that most subsets yield small errors, while a few produce much larger errors, resulting in a long-tailed distribution. … We introduce BestRand, a stable and low-cost benchmark compression method that preserves the efficiency of random sampling while substantially reducing its high-error tail. We validate BestRand on 70+ text, multimodal, and agent benchmarks.

## 中文摘要

随机抽小基准评测：多数子集误差很小，少数子集误差很大，呈长尾；随机抽样高概率表现强但不稳定，且不稳定性是现代基础模型的固有属性，评测更多模型也不消失。BestRand 保留随机抽样的低成本，用选择流程压掉高误差尾部：70+ 文本/多模态/agent 基准上，聚合统计报告高误差风险降 50.2%、估计误差降 16.4%、构造成本为对比方法的 51.3%。

## 边界

- 数字是跨基准聚合结论，不保证任意单个小样本可靠；与 Terminal-Bench 维护论文（2611.08417，AAIF 86099069）同属"评测成本与口径"主线。
