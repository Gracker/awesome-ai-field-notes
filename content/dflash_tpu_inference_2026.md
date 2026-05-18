---
title: "Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding"
date: 2026-05-04
source: google
category: infra
tags: [TPU, inference, speculative-decoding, vLLM, diffusion, DFlash, UCSD]
quality_score: 4
status: fetched
---

## DFlash 块扩散推测解码：TPU LLM 推理速度提升 3 倍，验证成本近乎恒定

**发布日期：2026年5月4日 | 来源：Google Cloud Blog**

### 概述

UCSD 研究团队在 Google TPU 上实现 DFlash（块扩散推测解码），将 LLM 推理速度平均提升 3.13 倍，峰值接近 6 倍。通过在单次前向传播中并行生成整块候选 token，突破传统自回归草稿的 O(K) 串行瓶颈。

DFlash 在 TPU v5p 上相比 EAGLE-3 实现了 2.29 倍端到端加速，代码任务（mbpp）从 9.81ms/token 降至 3.48ms/token。

### 核心突破：打破自回归瓶颈

标准 LLM 推理以自回归方式生成文本——每个 token 都需要一次完整前向传播，严重低估了 AI 加速器（如 TPU）的大规模并行计算能力。

推测解码通过使用更小、更高效的"草稿"模型同时预测多个未来 token 来缓解这一问题。然而，现有的自回归草稿方法存在根本瓶颈：生成 K 个候选 token 需要 O(K) 次串行前向传播。

### 扩散式草稿 on Google TPUs

Diffusion LLMs (dLLMs) 通过用块扩散机制替代这种串行过程，从根本上改变了游戏规则。DFlash 利用从目标模型提取的隐藏特征，在单次前向传播中生成整块草稿 token。这一从 O(K) 到 O(1) 的复杂度转变，使草稿延迟降至几乎可以忽略的水平。

### 深层洞察：K-Flat 突破

研究团队发现，在数据中心级加速器（如 TPU v5p）上，验证 1024 个 token 的成本与验证 16 个 token 的成本几乎相同。这是因为时间主要消耗在加载模型权重上，而非注意力机制的数学运算。

这一发现将整个研究前沿转向：推测解码的瓶颈不是"验证成本"，而是"草稿质量"。

### 开源集成

完整实现已提交至 vLLM tpu-inference 仓库：
- PR #1868：DFlash 模型和提议者架构
- PR #1869：推测解码的端到端流水线集成
- PR #1870：综合 CI 和端到端测试框架

---
**参考链接：**
- [vLLM TPU Inference GitHub](https://github.com/vllm-project/tpu-inference)
- [DFlash 论文 (arXiv:2602.06036)](https://arxiv.org/abs/2602.06036)
- [EAGLE-3 论文 (arXiv:2503.01840)](https://arxiv.org/abs/2503.01840)
- [Colab Notebook](https://colab.research.google.com/drive/1ekk8lY2u843KE9_dpJ36Z_vyv5idL-Pf)

---

## Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding

**Published: May 4, 2026 | Source: Google Cloud Blog**

### Overview

Researchers at UCSD implemented DFlash (block-diffusion speculative decoding) on Google TPUs, achieving an average 3.13x increase in tokens per second on TPU v5p, with peak speedups reaching nearly 6x for complex math tasks.

DFlash achieved a 2.29x end-to-end serving speedup compared to EAGLE-3 on TPU v5p, compressing code task (mbpp) generation time from 9.81ms/token to 3.48ms/token.

### Core Breakthrough: Breaking Autoregressive Bottlenecks

Standard LLM inference generates text autoregressively, requiring a full forward pass for every single token, heavily underutilizing the massive parallel compute capabilities of AI accelerators like TPUs.

Speculative decoding uses a smaller "draft" model to predict multiple future tokens simultaneously, then the larger "target" model verifies them in a single parallel forward pass. However, autoregressive draft methods have a fundamental bottleneck: generating K candidate tokens requires O(K) sequential forward passes.

### Diffusion-style Drafting on Google TPUs

Diffusion LLMs (dLLMs) fundamentally change the game by replacing this sequential process with a block diffusion mechanism. DFlash generates an entire block of draft tokens in a single forward pass using hidden features extracted from the target model. This shift from O(K) to O(1) complexity makes drafting cost nearly negligible.

### Key Insight: K-Flat Discovery

The research team discovered that on datacenter-grade accelerators like TPU v5p, the cost of verifying 1024 tokens is almost identical to verifying just 16 tokens—because time is dominated by loading model weights, not attention math. This shifts the research frontier: the bottleneck is not "verification cost" but "draft quality."

### Open Source

Implementation submitted to vLLM tpu-inference repo with three PRs covering model architecture, end-to-end pipeline integration, and comprehensive testing frameworks.

---
**References:**
- [vLLM TPU Inference GitHub](https://github.com/vllm-project/tpu-inference)
- [DFlash Paper (arXiv:2602.06036)](https://arxiv.org/abs/2602.06036)
- [EAGLE-3 Paper (arXiv:2503.01840)](https://arxiv.org/abs/2503.01840)
- [Colab Notebook](https://colab.research.google.com/drive/1ekk8lY2u843KE9_dpJ36Z_vyv5idL-Pf)
