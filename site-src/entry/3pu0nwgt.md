---
title: 'Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA'
sidebar: false
---

::: info
[← 返回基础设施](/infra)
:::

# Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA

> 双 Mac Studio RDMA 池化跑 Qwen3.5-122B，52 tok/s 稳定吞吐

🔗 [原文链接](https://x.com/TrevinPeterson/status/2027404303749546459) | @TrevinPeterson | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`qwen` `mac-studio` `rdma` `exo` `local-inference` `thunderbolt`

---

## English

The phrase "Qwen3.5-122B-A10B Dual Mac Studio M4 Max Exo Thunderbolt 5 RDMA Trevor Peterson" refers to a specific, high-performance local AI inference setup. This configuration involves running the Qwen3.5-122B-A10B large language model on a cluster of two Mac Studio M4 Max machines, facilitated by the Exo software and interconnected using Thunderbolt 5 with Remote Direct Memory Access (RDMA), a setup notably documented by Trevor Peterson.

Here's a breakdown of the components:

*   **Qwen3.5-122B-A10B:** This is a large language model (LLM) from Alibaba Cloud's Qwen3.5 series. The "122B" indicates it has 122 billion parameters, with "A10B" signifying 10 billion active parameters per token. This model is recognized for its multimodal capabilities, handling both vision and text, and its built-in reasoning features.
*   **Dual Mac Studio M4 Max:** The setup utilizes two Apple Mac Studio computers, each powered by an M4 Max chip. Apple Silicon, which includes M-series chips, is optimized for running Qwen models efficiently using Apple's MLX machine learning framework.
*   **Exo:** Exo is an open-source tool designed for creating private AI clusters. Developed by "exo labs," it enables the distribution of AI models across multiple devices, allowing for the execution of models that are too large for a single machine and enhancing overall performance. Exo leverages MLX as its inference backend and MLX distributed for inter-device communication.
*   **Thunderbolt 5 RDMA:** This technology is crucial for the cluster's high-speed communication. macOS 26.2 introduced support for RDMA (Remote Direct Memory Access) over Thunderbolt 5. RDMA dramatically reduces latency to between 5 and 9 microseconds and boosts bandwidth to up to 80Gb/s between connected devices. This allows multiple Macs to share memory access with minimal delay, enabling simultaneous processing of AI model layers across different GPUs in the cluster, rather than sequential processing. Thunderbolt 5 is a prerequisite for utilizing RDMA in this context.
*   **Trevor Peterson:** Trevor Peterson has shared his experiences and insights regarding the successful implementation of the Qwen3.5-122B model on a dual Mac Studio M4 Max configuration using Exo and Thunderbolt 5 RDMA. He specifically mentioned using this setup to develop a tutoring application for his children.

This combination of hardware and software represents an advanced local AI inference system, leveraging the capabilities of Apple Silicon and high-speed networking for efficient large language model deployment.

## 中文

"Qwen3.5-122B-A10B 双 Mac Studio M4 Max Exo + Thunderbolt 5 RDMA Trevor Peterson"指的是一个特定的高性能本地AI推理配置。该配置涉及在两台Mac Studio M4 Max机器集群上运行Qwen3.5-122B-A10B大语言模型，通过Exo软件实现，并使用Thunderbolt 5与远程直接内存访问（RDMA）互连，这是Trevor Peterson特别记录的设置。

以下是各组件的详细说明：

*   **Qwen3.5-122B-A10B：** 这是阿里巴巴云Qwen3.5系列的大语言模型（LLM）."122B"表示它有1220亿个参数，"A10B"表示每个token有100亿个活跃参数.该模型以其多模态能力而闻名，能够处理视觉和文本，并具有内置的推理功能.
*   **双Mac Studio M4 Max：** 该设置使用两台Apple Mac Studio计算机，每台都由M4 Max芯片驱动.包括M系列芯片的Apple Silicon针对使用Apple的MLX机器学习框架高效运行Qwen模型进行了优化.
*   **Exo：** Exo是一个为创建私有AI集群而设计的开源工具.由"exo labs"开发，它使AI模型能够在多个设备上分布式执行，允许运行对于单台机器来说太大的模型，并提高整体性能.Exo利用MLX作为推理后端，MLX distributed用于设备间通信.
*   **Thunderbolt 5 RDMA：** 该技术对于集群的高速通信至关重要.macOS 26.2引入了通过Thunderbolt 5支持RDMA（远程直接内存访问）的功能.RDMA将延迟显著降低到5到9微秒之间，并将带宽提升到连接设备之间最高80Gb/s.这使多台Mac能够以最小的延迟共享内存访问，实现跨集群中不同GPU的AI模型层同时处理，而不是顺序处理.Thunderbolt 5是在此上下文中利用RDMA的先决条件.
*   **Trevor Peterson：** Trevor Peterson分享了他关于在双Mac Studio M4 Max配置上使用Exo和Thunderbolt 5 RDMA成功实施Qwen3.5-122B模型的经验和见解.他特别提到使用此设置为他的孩子开发辅导应用程序.

这种硬件和软件的组合代表了一种先进的本地AI推理系统，利用Apple Silicon和高速网络来实现高效的大语言模型部署。
