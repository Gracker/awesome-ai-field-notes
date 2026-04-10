# 端侧与边缘

On-Device & Edge — 4 条活跃资源

### [Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA](https://x.com/TrevinPeterson/status/2027404303749546459) 
by @TrevinPeterson (2026-02-28) | ⭐⭐⭐⭐ 4/5 | 🌐

**双 Mac Studio RDMA 池化跑 Qwen3.5-122B，52 tok/s 稳定吞吐**

24+ 小时调试后，在两台 Mac Studio M4 Max 上通过 Exo + Thunderbolt 5 RDMA 实现了 Qwen3.5-122B-A10B 的完整池化运行。持续吞吐约 52 tok/s，并发 c=2 稳定（p95 约 10.37 秒）。提供了完整的 Day-0 实操指南，包含精确命令与失败检查关卡。
 `qwen` `mac-studio` `rdma` `exo` `local-inference` `thunderbolt`

---
### [MeKi —— 用 ROM 扩展端侧 LLM，而不是继续硬堆计算](#) 
by @允许动态投影、归一化、非线性映射这些复杂结构存在，以保证模型能学到足够好的知识表达；部署前，再把这些东西折叠到静态查表结构里。于是： (2026-03-09) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**端侧 AI 部署的实用研究**

**论文**：MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling  
**精读日期**：2026-03-09  
**定位**：面向 Android / 端侧 AI / 性能优化 / SmartPerfetto 方向的深度解读

---

## 一、论文要解决的问题
### 1.1 真正的问题不是“模型不够大”，而是“手机端的资源结构不匹配”
在服务器上，做大模型最直接的办法就是：
- 增加参数量；
- 增加推理时计算；
- 用更大的显存和更强的 GPU 接住它。

但到了手机端，这套思路就开始失效：
…
 `perfetto` `on-device` `agent` `android` `llm` `paper` `performance` `reasoning`

---
### [V 神本地 LLM 环境配置](https://x.com/fkysly/status/2040976089196167538) 
by @马天翼 (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**V 神的本地 LLM 全栈配置方案，从硬件到离线防幻觉策略。**

V 神分享的本地大模型环境配置博客。从硬件选型开始，详细讨论如何构建一套满足隐私、安全、离线要求的 Local LLM 环境。特别值得注意的细节：为了减少飞机上离线情况下的模型幻觉，他把 1GB 维基百科内容都存了下来方便模型自我核实。同时也考虑了预算有限朋友的硬件推荐方案。
 `本地LLM` `Vitalik` `隐私` `离线` `硬件配置`

---
### [PocketLLM: Enabling On-Device Fine-Tuning for Personalized LLMs](#) 
 (2026-03-08) | ⭐⭐⭐ 3/5 | 🇨🇳

**端侧 AI 部署的实用研究**

## 1. 核心问题
这篇论文解决的是“端侧个性化”中最现实的拦路虎：**微调内存开销**。很多工作证明了“可以做微调”，但通常在树莓派或实验环境，离手机实用化很远。PocketLLM 的价值在于把问题拉回到真实手机场景。

## 2. 论文贡献（按价值排序）
1) **明确瓶颈优先级**：在端侧微调中，内存是可行性门槛；算力更多影响时延。
2) **方法选择正确**：采用无导数优化绕开梯度/优化器状态，直接打掉最大内存项。
3) **实机验证**：在 OPPO Reno 6 上给出可复现实验（RoBERTa-large 与 OPT-1.3B）。

## 3. 关键数据的含义
- RoBERT…
 `perfetto` `on-device` `fine-tuning` `coding` `android` `llm` `paper` `performance`

---