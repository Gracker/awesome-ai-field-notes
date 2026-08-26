---
id: ff9b22ff
title: "karpathy: Built a new tiny LLM inference engine in 200 lines"
platform: github
author: karpathy
original_date: "2026-02-12"
quality_score: 4
url: "http://karpathy.github.io/2026/02/12/microgpt/"
tags: [LLM, GPT, from-scratch, Python, tutorial, karpathy]
fetch_date: "2026-05-31"
---

## English

# microgpt — A 200-line pure Python GPT

[Andrej Karpathy](https://karpathy.ai/) released **microgpt**: a single file of ~200 lines of pure Python with **no dependencies** that trains and runs inference on a GPT. The file contains the complete algorithmic essence: dataset, tokenizer, autograd engine, GPT-2-like neural network, Adam optimizer, training loop, and inference loop.

The goal: distill the entire algorithmic content of what an LLM needs down to the bare minimum—no efficiency tricks, no GPU requirements, just the math.

## Core Components

**Dataset:** 32,000 names from a text file. Each name is a "document".

**Tokenizer:** Simplest possible—assign one integer ID to each unique character (26 lowercase letters + BOS token = 27 total vocabulary).

**Autograd:** A single `Value` class wraps scalars, tracks computation graph, implements `backward()` via chain rule. This is the same algorithm as PyTorch's `.backward()`, just operating on scalars instead of tensors.

**Architecture:** GPT-2-like Transformer with:
- Token embeddings + position embeddings
- Single-head attention (configurable to multi-head)
- RMSNorm (no LayerNorm), no biases
- ReLU (not GeLU)
- Residual connections

**Training:** 1,000 steps on a tiny model (~4,192 parameters). Loss drops from ~3.3 (random guessing) to ~2.37. Then sample new names:

```
kamon, ann, karai, jaire, vialan, karia, yeran, anna, areli, kaina, conna, keylen, liole, alerin, earan, lenne, kana, lara, alela, anton
```

**Key insight:** Everything in modern LLMs (ChatGPT etc.) is this same loop—predict next token, sample, repeat—just massively scaled up in data, model size, and compute.

## What makes it different from production LLMs?

| Aspect | microgpt | Production LLMs |
|--------|----------|-----------------|
| Data | 32K names | Trillions of tokens |
| Vocab | 27 characters | ~100K subword tokens |
| Parameters | 4,192 | Hundreds of billions |
| Autograd | Pure Python scalars | GPU tensors + CUDA kernels |
| Training | Single-threaded Python | Distributed GPU clusters |
| Post-training | None | SFT + RLHF |

The **core algorithm is identical**. Everything else is engineering at scale.

**Source:** [karpathy.github.io](http://karpathy.github.io/2026/02/12/microgpt/) | [GitHub Gist](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95)

---

## 中文

# microgpt — 仅用200行纯Python实现的GPT

[Andrej Karpathy](https://karpathy.ai/) 发布了 **microgpt**：一个约200行的纯Python文件，**零依赖**，能训练并运行一个GPT做推理。文件包含完整的算法核心：数据集、分词器、自微分引擎、类GPT-2神经网络、Adam优化器、训练循环和推理循环。

目标：将LLM所需的全部算法内容精简到极致——不含任何效率优化、不需要GPU，只有数学。

## 核心组件

**数据集：** 32,000个英文名字组成的文本文件。每个名字视为一个"文档"。

**分词器：** 最简实现——为每个唯一字符分配一个整数ID（26个小写字母 + BOS标记 = 共27个词表）。

**自微分（Autograd）：** 一个 `Value` 类封装标量，跟踪计算图，通过链式法则实现 `backward()`。这与 PyTorch 的 `.backward()` 算法完全相同，只是操作的是标量而非张量。

**架构：** 类GPT-2 Transformer，含：
- 词嵌入 + 位置嵌入
- 单头注意力（可配置为多头）
- RMSNorm（而非LayerNorm），无偏置
- ReLU（而非GeLU）
- 残差连接

**训练：** 小模型（约4,192个参数）训练1,000步。损失从~3.3（随机猜测）降至~2.37。随后采样生成新名字：

```
kamon, ann, karai, jaire, vialan, karia, yeran, anna, areli, kaina, conna, keylen, liole, alerin, earan, lenne, kana, lara, alela, anton
```

**核心洞见：** 现代LLM（如ChatGPT）的全部内容就是这个循环的放大版——预测下一个token、采样、重复——只是在数据、模型规模和算力上极度扩展。

## 与生产级LLM的区别

| 方面 | microgpt | 生产级LLM |
|------|---------|----------|
| 数据 | 32K个名字 | 数万亿token |
| 词表 | 27个字符 | ~100K子词token |
| 参数 | 4,192 | 数千亿 |
| 自微分 | 纯Python标量 | GPU张量 + CUDA内核 |
| 训练 | 单线程Python | 分布式GPU集群 |
| 后训练 | 无 | SFT + RLHF |

**核心算法完全相同**。其他都是大规模工程。

**来源：** [karpathy.github.io](http://karpathy.github.io/2026/02/12/microgpt/) | [GitHub Gist](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95)
