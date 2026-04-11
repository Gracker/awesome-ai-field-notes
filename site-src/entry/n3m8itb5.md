---
title: '破局Agent时代：ARIES RISCV+AI架构分析'
sidebar: false
---

::: info
[← 返回ai-hardware/chip-architecture](/ai-hardware/chip-architecture)
:::

# 破局Agent时代：ARIES RISCV+AI架构分析

> ISSCC 2026 ARIES 芯片深度解析：RISC-V 调度 + CIM 存内计算，14nm 打败 4nm 的 Agent 时代实用主义架构

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=MzUzNzg4Nzc3MQ==&mid=2247485969&idx=1&sn=32449a8c2513a5cb53f1ad2360b58e4a&chksm=fb5995ca0659939a19e7e4ecd431eae703978643af53d7f9345980de179d6c692ed620b8982d) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-11

`risc-v` `ai-chip` `npu` `llm-inference` `agent` `hardware` `cim` `isscc-2026`

---

# 破局Agent时代：ARIES RISCV+AI架构分析

破局Agent时代：ARIES RISCV+AI架构分析

[Read in Cubox](https://cubox.pro/web/card/7442659981851103210)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzUzNzg4Nzc3MQ==&mid=2247485969&idx=1&sn=32449a8c2513a5cb53f1ad2360b58e4a&chksm=fb5995ca0659939a19e7e4ecd431eae703978643af53d7f9345980de179d6c692ed620b8982d&scene=0&xtrack=1)  

---

### **引言：Agent 时代，芯片不仅要"算得快"，更要"想得清"**

看到ISSCC 2026展示的**ARIES** 架构，我最直观的感受是：**AI芯片正在从"算力怪兽"进化为"有脑子的行动派"。**

在Agent（智能体）时代，AI不再仅仅是云端的一个对话框，而是需要具备感知（视觉/多模态）-\> 思考（LLM逻辑推理）-\> 决策（控制流处理）-\> 行动（工具调用）的闭环能力。

这篇博客将深入剖析ARIES如何通过**RISC-V + AI集群** 的异构设计，以及大容量SRAM结合CIM（存内计算）的路径，走出了一条不同于NVIDIA的"实用主义"进阶之路。

## **逻辑与算力的深度融合：从芯片架构看AI Agent的未来**

### **一、 为什么Agent时代需要"有脑子"的NPU？**

在传统的Transformer或CNN推理中，调度是相对静态的。但在**Agent时代** ，系统面临的是极度动态的负载：

1. **控制流复杂化** ：Agent需要频繁进行IF-ELSE逻辑判断（例如：如果视觉识别到障碍物，则调用规划模块；否则继续巡航）。
2. **多模型协同** ：一个Agent任务可能同时运行YOLO（看）、Whisper（听）和Llama（想）。
3. **长序列瓶颈** ：Agent需要维持长期的上下文（Memory），KV Cache的访问压力剧增。

**传统的NPU** 往往是"四肢发达、头脑简单"------矩阵运算极强，但一旦遇到非线性的控制逻辑，就必须频繁跳回Host CPU处理，产生巨大的PCIe时延。

**ARIES的破局点** ：它将**RISC-V CPU** 直接集成在SoC核心区，作为调度与逻辑控制的"前额叶"，配合支持CIM和精细化量化的"肌肉"集群。这种\*\*"逻辑控制+极致算力"\*\*的紧耦合，正是Agent实时响应的关键。

### **二、 架构博弈：为什么 ARIES 不走 PD/AF 分离路线？**

关于 **ARIES** 的细节，特别是对比 NVIDIA 及其收购 Groq 启发后的 LPU 路径（侧重于 Prefill 与 Decode 的物理/逻辑分离，以及 Attention 与 FFN 的专项优化），我发现 ARIES 走了一条极其适合 **Agent 时代** 的"内生型"演进道路。在 Agent 时代，任务流是碎片化且高度依赖逻辑判断的。以下我将从架构师视角，深度拆解 ARIES 这种 **"RISC-V 控制核 + 大容量片内 SRAM + CIM 存内计算"** 组合的实战优势。

AI Agent 与传统聊天机器人最大的区别在于：它需要根据当前输出的 Token 实时决定下一步是调用 API、检索文档还是结束任务。这种**高度分支化** 的特征，使得芯片不能只做一个"吞吐流水线"。

NVIDIA 和类似 Groq 的架构（LPU）倾向于通过 **PD 分离（Prefill/Decode 分离）** 来解决 Transformer 的 Compute-bound（Prefill 阶段）与 Memory-bound（Decode 阶段）不平衡问题；同时在 Decode 阶段尝试 **AF 分离（Attention/FFN 分离）** ，通过专项硬件优化这两类特征截然不同的算子。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ9iazku4kibdDGOqXnqREGczOY0q3hnjsvCX4rjIAN868osPIuFicG3ictWbazO3kbapf8pjb1Jk9AFyCkxOW7q8AOqZlJ0mBGOgj3nNen2PvXE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

但 ARIES 选择了另一条路。在顶级架构师眼中，PD 分离和 AF 分离虽然能压榨极致的算子效率，但其代价是**灵活性损耗** 。

**1. 拒绝 PD 硬件分离：用"统一 Tile + 独立时钟域"对冲瓶颈**

NVIDIA 等方案通常需要极高的带宽（HBM）来支撑 Decode 阶段。而 ARIES通过一个天才的设计避开了物理分离：**在同一个算力 Tile 内，为计算单元和数据搬运单元设置独立的时钟域。**

* **架构师视野** ：在 Prefill 阶段，提升计算域频率；在 Decode 阶段，压低计算频率、全速开启搬运域频率。通过**时钟级动态缩放** ，ARIES 在一套硬件上同时适配了"算力密集"和"访存密集"两种模式。这比物理上分出两个 Core 更省面积，更适合 Agent 那种忽大忽小的负载。

就是说典型的实现- 既要，又要

我们相信这样的PD/AF 融合方案才是体系架构的趋势，NV的PD/AF 分离也许是过度方案。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FZ9iazku4kibdCaMM8CXQk74oU5T4ybiafKZcOz9qFMSIHZhYg7eEOOkf8ug4gdtUbRcGkjpbqt4VEV0OHgMeOtMxOp0rhjXJMLGIFbjBFM6r54%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

**2. 拒绝 AF 专项引擎：用"大 SRAM + CIM"消灭访存鸿沟**

传统的 AF 分离（Attention 与 FFN 分离）是为了应对 Attention 的 KV Cache 读写压力。

* **ARIES 的方案** ：它不分 Attention 或 FFN 专用区，而是直接在片内堆了 **280MB 的超大 SRAM** 。配合 **2D CIM（存内计算）** ，它让 Memory-bound 的 Attention 算子直接在存储单元里完成计算。
* **技术洞察** ：当数据不再需要离开存储器进入 ALU 时，Attention 和 FFN 的边界就模糊了------因为搬运代价都被消灭了。这对于 Agent 这种频繁切换模型上下文的场景，具有更强的泛化能力。

### ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ9iazku4kibdAqHrmPhjYMRmaGtEZxf43adEVHbpcWZ5SclSIB83DickxSIFqNppYCcfzwhuTSgibvltSV0VhgibfvJEpa4FFL0JKx5Ro48aB7A4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FZ9iazku4kibdBgWoicnVOyZodialVnHLBtOdtETkl9X1xeIzUpYoj3WroaNewsJkI6wjx1Z2DemvQlK9K7KcticVeJPnQNabwrg0thZOtnROJ58g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

### **三、 逐图拆解：ARIES架构的技术硬核**

#### 1. 动机与挑战：滑动的瓶颈


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ9iazku4kibdAPHDRkx57ianNXdFkMamnlNibeyJibvQXoBKO8WsDqTQ2eE7vgHFPak8YAiaxzJvZqMh8ibzAwohLNzBl7LssmzpGibZmOdUHGRw4OY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

* **分析** ：上图的"滑块"非常形象。CNN是计算密集型（左），LLM是访存密集型（右）。Agent应用刚好位于中间的动态区域。ARIES的灵活性在于其**TME（张量操作引擎）** ，它能高效处理非规则访存（Gather/Scatter），让LLM在长序列下的效率不至于掉下悬崖。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FZ9iazku4kibdA4Z47JrlfGOsrCGROVfa9AT1URWlXxRwokD2d22va8PaQN7E7QTOPBsUH52rLsZuHCw5bT5l8bl0sUC5WvatWH3ia3oQG42GQc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

#### **2. 三引擎NPU Core：精细化分工**

* **TCE (Compute)** ：4K MAC阵列，负责重活。
* **TME (Manipulation)** ：专门对付非连续内存访问，解决Agent中复杂的张量转置和对齐。
* **VCE (Vector)** ：负责激活函数、归一化。这三个引擎互不阻塞，实现了指令级的并行。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FZ9iazku4kibdBbEcxCn57UvkGGZmhBcPuQBKKnnsTtTnKsvKh57YELexFIgPEKKhGichNtUgOnWCluucTzOOlJq7uZpfsJPGnKsSH3EfTdSNoA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

#### **3. 软硬协同的多级量化**

* **核心创新** ：ARIES支持LUT-based（基于查找表）的量化。
* **分析** ：Agent时代模型巨大，4-bit甚至更低位宽是刚需。传统的均匀量化会导致精度崩塌。ARIES通过离线分析离群值（Outliers），利用LUT实现非均匀映射。这使得它能在14nm工艺下跑出超越4nm GPU的能效比。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FZ9iazku4kibdBkxsno2B8VDMvKdqrCiaa9mKoeFfL4KdjtStRNowibcJ81Dgk9mtsA2X0Pybjr8IKNGwZ3XQEOLKSSw95LuRrBNwVFdjtAjayXM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ9iazku4kibdCtoTiaTOaV44EP49HOx7tVyMb05s1dHFpRJdR3LJmNVrt8T6bbRyexLqOQxNqxfGEWakFxUVQOaGXric5JPRpJDqfTLW99hOELY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

#### **4. RISC-V 调度的硅片实现**


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ9iazku4kibdDvEeVibNibDShQXLtibBbfddxvFwR8DDBzMK3WGA80dk3ZNk8MvAZJ2ujvnAKBRkmM7Vx5ibbpoLECg2PgOTibAqqDQBzcgic1icL7V0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9)

* **分析** ：观察硅片布局图，**RISC-V** 位于底部核心区，紧邻PCIe和NPU集群。这种设计允许RISC-V以极低的延迟管理8个NPU Core的同步。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FZ9iazku4kibdDp3JtLuia6bjsgXWicuYicLOTjUKzpF3eicUxBA3SebPqAeZialFBKGOUian4lfC3ovNTpdPlYUSxPMctakoMIdfKbDJib6E63q41Vws%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D10)

* **功耗表现** ：整板25W的TDP，其中NPU核心功耗仅约10W。对于车载或边缘边缘网关这种热设计受限的场景，这是降维打击。

#### **5. 杀手锏：稀疏性与相似性感知**


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ9iazku4kibdBO0cZD1JyyS5oIptqDYKItCEswmYzWvtp0Xqsd0FeSOfPH8ktAzrIpnsxJCsUT4crUrKUvbVNvMWLibLXzxGvTSiardIxECoiazs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D11)

* **TCAM Unit** ：这里提到的**相似性感知TCAM** 是针对Agent长上下文优化的神作。它通过匹配查询向量的相似度，主动跳过那些对结果贡献微小的稀疏算力块（Redundancy Skipping）。
* **点评** ：这本质上是在硬件层实现了"注意力剪枝"，是目前最先进的动态算力调度技术。

### **四、 总结：Agent时代的"实用主义"典范**

我给ARIES的评价是：**它不是在堆料，而是在通过"空间"换"效率"。**

* **RISC-V + AI** ：解决了Agent所需的逻辑判断与算力调度的耦合，不再依赖昂贵的Host CPU。
* **海量SRAM + CIM** ：绕过了HBM的高成本陷阱，用成熟的14nm工艺通过架构创新实现了跨代际的能效比提升（**10.12x higher FPS/W on YOLOs** ）。
* **多精度LUT** ：让模型压缩不再是理论，而是实实在在的带宽节省。

**结论** ：如果说NVIDIA是AI时代的"通用航空发动机"，那么ARIES就是专为Agent时代设计的"高效率混合动力系统"。它证明了：在逻辑控制与极致访存优化面前，制程工艺的领先（14nm vs 4nm）并非不可逾越的鸿沟。对于需要落地、需要能效、需要实时逻辑反馈的智能体应用，ARIES这种架构才是实用主意而非简单COPY 大厂技术路线，实现换到超车，弯道超车，实现你打你的我打我的。

------------------------------------------------------------------------------

**相关文档和资料统一存放在知识星球，加入获得更多相关资料**

**本文根据以下资料撰写，加入星球可获得更多1500+详细资料**

**互动群长按下方二维码即可加入 请注明工作行业和研究方向**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FZ9iazku4kibdDdS5PFnYcVJvvdhTkQlgTTeocjFtibPS9uneHepDAP7Lic8JptiaITrmG0QMkOb6LAZr1puJUgAZNZKE4A406KTh3yP2xcb34SrM%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D12)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FWpHEqW95RcdDD4tRvIpE1064VdOTnMK2iaeq7fwAFbHFzpNhwrOyWzXJKnSIrRiaTxpBclTUu8atS0ibnLYwE3gpQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D13)
