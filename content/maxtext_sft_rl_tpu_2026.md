---
title: "MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs"
date: 2026-04-16
source: google
category: infra
tags: [MaxText, TPU, SFT, RL, GRPO, GSPO, post-training, JAX]
quality_score: 4
status: fetched
---

## MaxText 新增后训练能力：单主机 TPU 上的 SFT 和 RL 支持

**发布日期：2026年4月16日 | 来源：Google Developers Blog**

### 概述

在大语言模型（LLM）快速发展的格局中，预训练只是第一步。要将基础模型转化为专业助手或高性能推理引擎，后训练至关重要。

今日，MaxText 宣布了新功能，简化这一过程：监督微调（SFT）和强化学习（RL）现已在单主机 TPU 配置（如 v5p-8 和 v6e-8）上可用。

MaxText 利用 JAX 的强大功能和 Tunix 库的效率，为开发者提供了高性能、可扩展的路径，使用最新的后训练技术来优化模型。

### 监督微调（SFT）：精准调优，简单高效

监督微调是将预训练模型适配以遵循特定指令或擅长特定任务的主要方法。借助新的单主机 SFT 支持，用户现在可以获取现有的 MaxText 或 Hugging Face 检查点，在标注数据集上进行微调，设置极简。

**核心亮点：**

- 无缝集成：原生支持 Hugging Face 数据集（如 ultrachat_200k）。
- 灵活检查点：可直接使用现有 MaxText 检查点或在生态内转换 Hugging Face 模型（如 Gemma 3）。
- 优化执行：由 Tunix 驱动——Tunix 是专为后训练效率设计的基于 JAX 的库。

### 强化学习（RL）：提升推理能力

对于需要复杂逻辑和推理的任务（如数学或编程），强化学习是改变游戏规则的技术。 MaxText 现在支持在单主机 TPU 上使用多种前沿 RL 算法，并在训练循环中利用 vLLM 实现高吞吐量推理。

**Group Relative Policy Optimization（GRPO）：** GRPO 是 PPO（近端策略优化）的内存高效变体。它无需独立的价值函数模型，而是为每个提示生成多个响应，并在组内计算相对优势。这大大降低了硬件占用，使先进 RL 在单 TPU 主机上成为可能。

**Group Sequence Policy Optimization（GSPO）：** GSPO 专注于序列级重要性比率和裁剪。它通过在序列级别奖励模型行为来提高训练稳定性和效率，使在 GSM8K 等基准上的性能提升特别有效。

### 开始使用

```bash
# 安装依赖
uv pip install maxtext[tpu-post-train]==0.2.1 --resolution=lowest

# 运行 SFT：
python3 -m maxtext.trainers.post_train.sft.train_sft \
  model_name=${MODEL?} \
  load_parameters_path=${MAXTEXT_CKPT_PATH?} \
  run_name=${RUN_NAME?} \
  base_output_directory=${BASE_OUTPUT_DIRECTORY?}

# 运行 RL（GRPO/GSPO）：
python3 -m maxtext.trainers.post_train.rl.train_rl \
  model_name=${MODEL?} \
  load_parameters_path=${MAXTEXT_CKPT_PATH?} \
  run_name=${RUN_NAME?} \
  base_output_directory=${BASE_OUTPUT_DIRECTORY?} \
  loss_algo=gspo-token \
  chips_per_vm=${CHIPS_PER_VM?}
```

---
**参考链接：**
- [MaxText GitHub](https://github.com/AI-Hypercomputer/maxtext)
- [SFT 文档](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/tutorials/posttraining/sft.html)
- [RL 文档](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/tutorials/posttraining/rl.html)

---

## MaxText Expands Post-Training Capabilities: Introducing SFT and RL on Single-Host TPUs

**Published: April 16, 2026 | Source: Google Developers Blog**

### Overview

In the rapidly evolving landscape of large language models (LLMs), pre-training is only the first step. To transform a base model into a specialized assistant or a high-performing reasoning engine, post-training is essential.

Today, MaxText announces new features that streamline this process: Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) now available on single-host TPU configurations (such as v5p-8 and v6e-8).

By leveraging the power of JAX and the efficiency of the Tunix library, MaxText provides a high-performance, scalable path for developers to refine their models using the latest post-training techniques.

### Supervised Fine-Tuning (SFT): Precision Tuning Made Simple

Supervised Fine-Tuning is the primary method for adapting a pre-trained model to follow specific instructions or excel at niche tasks. With the new single-host SFT support, users can now take an existing MaxText or Hugging Face checkpoint and fine-tune it on labeled datasets with minimal setup.

**Key Highlights:**

- Seamless Integration: Native support for Hugging Face datasets (e.g., ultrachat_200k).
- Flexible Checkpoints: Use existing MaxText checkpoints or convert Hugging Face models (like Gemma 3) directly within the ecosystem.
- Optimized Execution: Powered by Tunix, a JAX-based library specifically designed for post-training efficiency.

### Reinforcement Learning (RL): Advancing Reasoning Capabilities

For tasks requiring complex logic and reasoning—such as math or coding—Reinforcement Learning is a game-changer. MaxText now supports several state-of-the-art RL algorithms on single-host TPUs, utilizing vLLM for high-throughput inference during the training loop.

**Group Relative Policy Optimization (GRPO):** GRPO is a memory-efficient variant of PPO. It eliminates the need for a separate value function model, instead generating multiple responses per prompt and calculating relative advantages within the group. This significantly reduces the hardware footprint, making advanced RL accessible on a single TPU host.

**Group Sequence Policy Optimization (GSPO):** GSPO focuses on sequence-level importance ratios and clipping. It improves training stability and efficiency by rewarding model behavior at the sequence level, making it particularly effective for enhancing performance on benchmarks like GSM8K.

### Getting Started

```bash
# Install dependencies
uv pip install maxtext[tpu-post-train]==0.2.1 --resolution=lowest

# Running SFT:
python3 -m maxtext.trainers.post_train.sft.train_sft \
  model_name=${MODEL?} \
  load_parameters_path=${MAXTEXT_CKPT_PATH?} \
  run_name=${RUN_NAME?} \
  base_output_directory=${BASE_OUTPUT_DIRECTORY?}

# Running RL (GRPO/GSPO):
python3 -m maxtext.trainers.post_train.rl.train_rl \
  model_name=${MODEL?} \
  load_parameters_path=${MAXTEXT_CKPT_PATH?} \
  run_name=${RUN_NAME?} \
  base_output_directory=${BASE_OUTPUT_DIRECTORY?} \
  loss_algo=gspo-token \
  chips_per_vm=${CHIPS_PER_VM?}
```

---
**References:**
- [MaxText GitHub](https://github.com/AI-Hypercomputer/maxtext)
- [SFT Documentation](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/tutorials/posttraining/sft.html)
- [RL Documentation](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/tutorials/posttraining/rl.html)
