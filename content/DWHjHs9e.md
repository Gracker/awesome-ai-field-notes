# Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding

> 英文原文: https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/

---

## **Overcoming autoregressive bottlenecks**

**EN:**
Standard LLM inference generates text autoregressively. This means the model requires a full forward pass for every single token generated, heavily underutilizing the massive parallel compute capabilities of AI accelerators like TPUs, especially at lower batch sizes.

**Speculative decoding** mitigates this by using a smaller, highly efficient "draft" model (or mechanism) to predict multiple future tokens simultaneously. The larger "target" model then verifies these draft tokens in a single parallel forward pass. If the draft tokens are accurate, the system accepts multiple tokens at the cost of a single step, drastically reducing latency.

However, the promise of speculative decoding is often hindered by the draft model itself. Most existing methods rely on **autoregressive draft mechanisms** that generate candidate tokens sequentially. This means that while the target model's verification is parallel, the drafting phase remains bottlenecked by _O(K)_ serial steps. As a result, the time spent "guessing" tokens begins to eat into the time saved by verification, capping the practical speedup potential.

**ZH:**
> 原文链接: https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/

---
![Gemini_Generated_Image_5uj3px5uj3px5uj3](images/img_001.jpg)

当前大型语言模型（LLM）加速领域主要由自回归投机解码主导，在这种解码中，轻量级草稿模型在目标验证之前**按顺序**预测 token。然而，这种串行起草方法引入了一个根本性的执行瓶颈：它需要 _K_ 次顺序的前向传播来生成 _K_ 个候选 token。这种逐步的依赖关系迫使系统在开始下一个预测之前等待当前 token 预测完成，这从根本上限制了起草阶段的加速潜力。为了打破这一效率天花板，研究人员超越了逐 token 起草的方式，转向**块扩散**（block diffusion），这是一种范式转变，能够在 _O_(1) 的单次前向传播中生成整块候选 token。

我们很自豪能够支持不断突破 AI 硬件边界的外部研究人员。今天，我们非常高兴地重点介绍由加州大学圣地亚哥分校（UCSD）研究人员取得的一项重大开源里程碑，该团队由 [分页注意力](https://arxiv.org/abs/2309.06180) 和 [预填充/解码解耦服务](https://arxiv.org/abs/2401.09670) 的共同发明人**张浩**领导。他们**在 Google TPU 上成功实现了块扩散投机解码（即**[**DFlash**](https://arxiv.org/abs/2602.06036)**，一种由 Zhijian Liu、Jian Chen 等人在**[**UCSD Z Lab**](https://z-lab.ai/)**中开发的卓越的扩散式投机解码）**。

通过将这种新颖的架构直接集成到开源的 **vLLM TPU 推理**生态系统中，UCSD 团队实现了在 TPU v5p 上每秒生成 token 数平均**提升 3.13 倍**，在复杂数学任务中的峰值加速接近 **6 倍**。在 **TPU v5p** 上 DFlash 与 EAGLE-3 的直接服务对比中，[**DFlash**](https://arxiv.org/abs/2602.06036) 实现了 2.29 倍的端到端服务加速，**几乎翻倍**于 [**EAGLE-3**](https://arxiv.org/abs/2503.01840) 1.30 倍的性能提升。

以下是来自 UCSD 研究人员的技术深度解析，详细介绍了他们是如何构建该系统的、他们的性能基准测试结果，以及这对 Google TPU 生态系统的未来意味着什么。

---

## **Diffusion-style drafting on Google TPUs**

**EN:**
Diffusion LLMs (dLLMs) fundamentally change the game by replacing this sequential process with a **block diffusion** mechanism. Instead of guessing the next word, dLLM "paints" the entire block. A notable dLLM-based drafting method is DFlash. By leveraging the hidden features extracted from the target model, DFlash can generate an entire block of draft tokens in a single forward pass. This shift from _O(K)_ to _O_(1) complexity reduces drafting latency to nearly negligible levels, making it the perfect architectural fit for the TPU's high-bandwidth Matrix Multiplication Units (MXUs).

The UCSD research team integrated **DFlash** into the **vLLM TPU Inference framework**. DFlash is a novel approach to speculative decoding that leverages block-diffusion mechanisms to propose draft tokens with exceptionally high acceptance lengths (_T_).

Implementing this on Google TPUs required deep optimization. With architectural guidance from Google Cloud engineers, the UCSD team minimized the overhead to ensure that the memory bandwidth and matrix multiplication units were fully saturated. By mapping the DFlash proposer and the verification pipeline efficiently to the TPU architecture, they minimized the overhead of the drafting phase while maximizing the parallel verification throughput of the target model.

**ZH:**
标准的 LLM 推理以自回归的方式生成文本。这意味着模型每生成一个 token 都需要一次完整的前向传播，这严重未能充分利用 TPU 等 AI 加速器强大的并行计算能力，尤其是在较低的批大小下。

**投机解码**通过使用一个更小、高效的“草稿”模型（或机制）同时预测多个未来的 token 来缓解这一问题。随后，较大的“目标”模型在单次并行前向传播中验证这些草稿 token。如果草稿 token 准确无误，系统将以单步的代价接受多个 token，从而大幅降低延迟。

然而，投机解码的前景往往受制于草稿模型本身。大多数现有方法依赖于**自回归草稿机制**，按顺序生成候选 token。这意味着，尽管目标模型的验证是并行的，但起草阶段仍然受到 _O(K)_ 个串行步骤的瓶颈限制。结果，“猜测” token 所花费的时间开始蚕食验证所节省的时间，从而限制了实际的加速潜力。

---

## **Bringing DFlash to TPU/JAX**

**EN:**
Porting DFlash from its original GPU/PyTorch implementation to the Google TPU/[JAX AI Stack](https://docs.cloud.google.com/tpu/docs/jax-ai-stack) ecosystem wasn't just a simple code translation; it required re-engineering the system to align with the unique architectural strengths of TPUs. Here is how the UCSD team tackled the three primary technical hurdles.

### **The "dual-cache" solution for attention**

In the PyTorch world, DFlash relies on simple, dynamic KV management. However, high-performance TPU serving via [tpu-inference](https://github.com/vllm-project/tpu-inference) uses paged attention with Pallas kernels—a system that breaks memory into fixed-size pages to maximize efficiency.

The catch? DFlash's non-causal block diffusion—the very thing that lets it "paint" a block of tokens—is fundamentally incompatible with standard paged attention. To solve this, the researchers designed a dual-cache architecture. **The target model** continues to use a paged KV cache, ensuring it benefits from the high-performance Pallas kernels required for large-scale serving. **The draft model** uses a specialized path with static on-device JAX arrays, successfully mirroring the original DFlash design while maintaining TPU-native performance.

### **Intelligent context management**

DFlash is unique because the draft model is "target-conditioned"—it stays smart by watching the target model's intermediate reasoning steps. These "hidden states" are stored in a **context buffer** that grows over time.

To keep communication between the host CPU and the TPU accelerator as fast as possible, the team implemented a **power-of-2 padding** strategy. This ensures that as newly projected features are appended to the buffer, they are transferred in optimized chunks. By meticulously tracking exactly how much context the draft model has already "consumed," they prevent any duplicate processing or data loss, keeping the parallel drafting highly accurate.

### **Bridging the metadata gap in TPU inference**

Unlike standard drafting methods, DFlash is uniquely stateful, relying on **persistent state** across iterations (including context buffers, KV cache positions, and RoPE offsets) to maintain its parallel block predictions. In the TPU-optimized vLLM pipeline, the metadata forwarded to the proposer included the draft tokens currently under verification. While this is standard for most models, for a diffusion-based architecture, it resulted in "sequence length inflation"—a misalignment where the internal draft state drifted away from the target model's reality.

By re-engineering the proposer to synchronize strictly with the true accepted token count, the research team restored perfect **alignment** between the two models. This adjustment allowed the block diffusion logic to operate with full mathematical precision on TPU hardware, unlocking the dramatic speedups they see in the final results.

**ZH:**
扩散语言模型从根本上改变了游戏规则，它用**块扩散**机制取代了这种顺序过程。dLLM 不是猜测下一个词，而是“描绘”整个块。一种值得注意的基于 dLLM 的起草方法是 DFlash。通过利用从目标模型中提取的隐藏特征，DFlash 可以生成整块 d在单次前向传播中生成草稿 token。这种从 _O(K)_ 到 _O_(1) 复杂度的转变，将草稿生成延迟降低到了几乎可以忽略不计的水平，使其成为 TPU 高带宽矩阵乘法单元 (MXU) 完美的架构契合者。

UCSD 研究团队将 **DFlash** 集成到了 **vLLM TPU 推理框架**中。DFlash 是一种新颖的推测解码方法，它利用块扩散机制来提出具有极高接受长度（_T_）的草稿 token。

在 Google TPU 上实现这一点需要深度优化。在 Google Cloud 工程师的架构指导下，UCSD 团队将开销降至最低，以确保内存带宽和矩阵乘法单元得到充分饱和。通过将 DFlash 提议器和验证流水线高效地映射到 TPU 架构上，他们最小化了草稿生成阶段的开销，同时最大化了目标模型的并行验证吞吐量。

---

## **Benchmarking the future of TPU serving**

**EN:**
### **A head-to-head showdown: DFlash vs. EAGLE-3 on TPU v5p**

To ensure a rigorous and fair comparison, the UCSD researchers benchmarked DFlash against the current mainstream speculative decoding method on TPUs: EAGLE-3. In this comparative study, the researchers used the exact same hardware (TPU v5p) and the same target model (Llama-3.1-8B) for both.

![table1](images/img_002.png)

DFlash vs. Eagle3 on the vLLM TPU pipeline & v5p TPUs Model: Llama-3.1-8B-Instruct (target) + z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat (DFlash draft, K=10) / yuhuili/EAGLE3-LLaMA3.1-Instruct-8B (EAGLE-3 draft, K=2)

This setup represents the most practical deployment scenario for both methods, as the choice of K values is based on their respective official open-source checkpoints, used **out-of-the-box** without additional fine-tuning or re-configuration. Autoregressive drafters like EAGLE-3 incur a sequential latency penalty that grows linearly with K, which typically constrains them to smaller speculation budgets to maintain low per-token latency. In contrast, DFlash uses parallel block diffusion to predict all tokens in a single forward pass, making the drafting cost largely insensitive to K. The results were decisive: DFlash achieved a 2.29x speedup, while EAGLE-3 provided a 1.30x gain. On coding tasks like mbpp, DFlash compressed the generation time from 9.81ms per token down to 3.48ms, a 2.83x improvement.

Why is the gap so large? EAGLE-3 predicts **2 tokens per step** autoregressively, requiring sequential forward passes with Python orchestration overhead between each. DFlash instead produces **a block of 10 high-quality candidate tokens** in a single forward pass, eliminating this serial bottleneck entirely. On TPUs, this "high-quality, high-quantity" draft output translates directly into a higher average acceptance length, turning the TPU's massive compute potential into real-world serving throughput.

### **Benchmark results on TPU v5p**

To evaluate the impact of DFlash on Google TPUs, the UCSD team benchmarked their implementation across a variety of domains on TPU v5p, focusing heavily on complex reasoning, mathematics, and coding—areas where long-context generation typically suffers from high latency.

The UCSD team built a **standalone JAX benchmark** to evaluate DFlash results. By stripping away the serving layer overhead, they could isolate the raw power of the DFlash-on-TPU algorithm. They observed an **average speedup of 3.13x** across all datasets, with remarkable peaks in mathematical reasoning.

![table2](images/img_003.png)

Benchmark results on v5p TPUs Models: Qwen/Qwen3-4B (target) + z-lab/Qwen3-4B-DFlash-b16 (draft, K=16); greedy decoding

For rigorous math tasks like _math500_, DFlash pushed the generation time down from 8.02ms per token to **1.40ms per token**. In coding evaluations like _humaneval_, generation speeds improved by over 3.5x.

**ZH:**
将 DFlash 从最初的 GPU/PyTorch 实现移植到 Google TPU/[JAX AI Stack](https://docs.cloud.google.com/tpu/docs/jax-ai-stack) 生态系统，不仅仅是简单的代码翻译；它需要对系统进行重新工程化，以契合 TPU 独特的架构优势。以下是 UCSD 团队如何解决三大主要技术障碍的。

### **注意力机制的“双缓存”解决方案**

在 PyTorch 领域，DFlash 依赖于简单、动态的 KV 管理。然而，通过 [tpu-inference](https://github.com/vllm-project/tpu-inference) 进行的 TPU 高性能服务，使用的是带有 Pallas 内核的分页注意力——这是一种将内存划分为固定大小页面以最大化效率的系统。

问题在哪？DFlash 的非因果块扩散——正是这一特性让它能够“绘制”一个 token 块——与标准的分页注意力根本不兼容。为了解决这个问题，研究人员设计了一种双缓存架构。**目标模型**继续使用分页 KV 缓存，确保其受益于大规模服务所需的高性能 Pallas 内核。**草稿模型**则使用带有设备内静态 JAX 数组的专用路径，成功复刻了最初的 DFlash 设计，同时保持了 TPU 原生的性能。

### **智能上下文管理**

DFlash 的独特之处在于草稿模型是“以目标为条件的”——它通过观察目标模型的中间推理步骤来保持智能。这些“隐藏状态”存储在一个随时间增长的**上下文缓冲区**中。

为了使主机 CPU 和 TPU 加速器之间的通信尽可能快，团队实施了**2 的幂次填充**策略。这确保了当新投影的特征被追加到缓冲区时，它们以优化的块形式进行传输。通过精确跟踪草稿模型已经“消耗”了多少上下文，他们避免了任何重复处理或数据丢失，从而保持并行草稿生成的高度准确性。

### **弥合 TPU 推理中的元数据差距**

与标准的草稿生成方法不同，DFlash 具有独特的有状态性，它依赖于跨迭代保持的**持久状态**（包括上下文缓冲区、KV 缓存位置和 RoPE 偏移量）来维持其并行的块预测。在针对 TPU 优化的 vLLM 流水线中，转发给提议器的元数据包含了当前正在验证的草稿 token。虽然这对大多数模型来说是标准做法，但对于基于扩散的架构，这导致了“序列长度膨胀”——一种内部草稿状态偏离目标模型实际情况的错位现象。

通过对提议器进行重新工程化，使其与真实接受的 token 数量严格同步，研究团队恢复了两个模型之间完美的**对齐**。这一调整使得块扩散逻辑能够在 TPU 硬件上以完全的数学精度运行，从而释放了他们在最终结果中看到的显著加速。

---

## **Deep insights into speculative efficiency**

**EN:**
### **The "K-Flat" breakthrough: Why wider is free**

During the optimization process, the research team uncovered a hardware characteristic that changes how engineers think about speculation limits: **K-Flat verification.**

On datacenter-grade accelerators like the TPU v5p, their systematic experiments revealed a surprising reality: **the cost of verifying 1024 tokens is almost identical to the cost of verifying just 16 tokens**. This phenomenon occurs because, on high-end hardware, the time spent is dominated by loading model weights rather than the raw math of the attention mechanism for these sequence lengths. In other words, the hardware's computational ceiling is so high that the extra work of checking a much longer "guess" is essentially free.

This discovery shifts the entire research frontier. It proves that the bottleneck for speculative decoding isn't "verification cost," but rather "draft quality." Knowing that wider blocks are computationally free allows developers to boldly scale draft block size, leveraging richer bidirectional context to improve accuracy without fear of slowing down the hardware.

### **Scaling theory: Quality over quantity**

While datacenter-grade AI accelerators make increasing the block size (_K_) virtually "free," their scaling theory reveals that simply adding more tokens yields diminishing returns. At their current operating points, a block size of K=16 already captures over 90% of the theoretical maximum speedup. In fact, scaling K from 16 all the way to 128 would likely net less than one additional accepted token per step.

The true lever for performance is **quality over quantity**. Their analysis shows that improving the per-position acceptance probability (_a_) is **2–3x more valuable** than increasing the block size _K_. This shifts the research focus: in an environment where verification cost is constant, the primary bottleneck is no longer how many tokens systems can check, but how accurately they can predict them. The next frontier of LLM serving lies in smarter draft training, not just wider speculation windows.

### **The predictability factor: Task-driven speedups**

Acceptance probability is deeply tied to the **predictability** of the task. The team observed a natural "positional decay" where tokens at the end of a block are harder to guess than those at the start. In logic-driven fields like **math and coding**, this decay is remarkably slow, maintaining high acceptance rates even deep into the block. Conversational chat, however, is more random, with accuracy dropping sharply after the first few tokens.

This predictability directly drives speedup. Because structured reasoning yields more predictable sequences, math and code tasks allow for much longer accepted blocks, more effectively saturating the TPU's parallel verification power. Consequently

...[内容已截断]