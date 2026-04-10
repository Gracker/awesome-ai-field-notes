# 端侧与边缘

On-Device & Edge — 9 条活跃资源

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
### [My self-sovereign / local / private / secure LLM setup, April 2026](https://vitalik.eth.limo/general/2026/04/02/secure_llms.html) 
 (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🌐

**Vitalik 以隐私为第一优先级的本地 LLM 方案，硬件选型和软件栈都有参考价值**

Vitalik Buterin 分享其本地私有 LLM 使用方案。隐私安全目标：防止远程模型获取隐私数据、防止 LLM 越狱攻击、防止后门和软件漏洞。硬件测试：NVIDIA 5090 (90 tok/s)、AMD 128GB 统一内存 (51 tok/s)、DGX Spark (60 tok/s)，推荐 5090 或 AMD 方案。软件栈：NixOS + llama-server（替代 Ollama，因能更好利用 GPU）+ llama-swap。Agent 工具方面讨论了 OpenClaw 的安全问题，强调沙箱隔离的重要性。附带 ComfyUI 本地图像/视频生成测试。
 `local-LLM` `privacy` `security` `Vitalik` `self-sovereign` `sandbox` `NixOS` `llama-server`

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
### [Qualcomm Snapdragon X2 Elite微架构](https://mp.weixin.qq.com/s?__biz=MzkzMTA2NjgzMA==&mid=2247488554&idx=1&sn=1e38328c97b182f71c139e0fc69447da) 
by @亦安 (2025-12-03) | ⭐⭐⭐ 3/5 | 🇨🇳

**高通第三代 Oryon 核心微架构详解，自研 CPU 已具竞争力**

基于 Chip&Cheese PPT 解读高通第三代 Oryon 核心微架构。3 cluster 18 核最高 5GHz，共享 L2 16MB/cluster，9宽 decode/retire，ROB 650+。L1-Miss-L2-Hit 21 cycle，96KB DCache。L2 TLB 标称 8K entry（实测约 1.5K-2K）。前代的渐进优化。
 `Qualcomm` `Snapdragon` `Oryon` `CPU` `微架构`

---
### [快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium与Airtest最为 - 掘金](https://juejin.cn/post/7462305424554590219) 
 (2025-01-22) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium**

快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium与Airtest最为 - 掘金


---
### [移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调实现NPU高效部署](https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2449991915&idx=1&sn=da3dd89e182f04dee8c8c5ac2ade9141&chksm=b0f950be96af7bc12328a5ee74bbfc11ed6b5b909d5e2424fbfe181c67021350ab246993d8e0&mpshare=1&scene=1&srcid=0828uXErCxwOEwzSvr55C1dO&sharer_shareinfo=68e9331636d3c4869d8011f376bf8128&sharer_shareinfo_first=68e9331636d3c4869d8011f376bf8128) 
 (2025-08-28) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调**

移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调实现NPU高效部署


---
### [端侧 AI](https://mp.weixin.qq.com/s?__biz=MzkyMTU4OTE2OA==&mid=2247488655&idx=1&sn=dbf749f318315a561f12f7966be09b84&chksm=c1801050f6f79946a2d6e6a1a04e9cbe0f1fc8364be2e886ac6fa6ec7d54d16db791481279ab&mpshare=1&scene=1&srcid=0620BptoCw1X2FVALZd6If67&sharer_shareinfo=14850c869ec881aeaed27ab4d570556b&sharer_shareinfo_first=e2db0e175c1edf666b0021e55fa7de74) 
 (2024-06-20) | ⭐⭐⭐ 3/5 | 🇨🇳

**Cubox 收藏 — 端侧 AI**

1、端侧LLM性能瓶颈，不是算力，而是内存速度。   -每生成一个token需要把模型在内存中读出一遍，10-15tops算力即可实现7b 10token/s以上的推理速度，功耗也远低于手游，所以无需担心H端侧。   -目前手机最快大概也就是LPDDR5T，9600MT/S，折合76.8 GB/s，理论最高能实现7b int4 下20 token/s，或14b int4下10token/s的输出。   -存量手机大多内存带宽在40-60GB/s。


---