# ⚡ 推理与部署

Inference & Serving — 共 15 条活跃资源

## 推理引擎 (5)

- [搞懂缓存机制，从Gemma4到Claude Code省80%Token](https://x.com/MinLiBuilds/status/2041178722230030384) by @MinLiBuilds — 从 KV 缓存原理到 Claude Code 实战，系统讲透 token 省钱机制 `kv-cache` `claude-code` `token-optimization` `transformer` `caching` 🇨🇳
- [AI 代理可观测性 - 演变标准与最佳实践](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247553129&idx=2&sn=b096969e9b11351ee311f13f4cb15c1b&chksm=ed4dcaeea8eed4db84fd7e26c9216b026b402f2de5aa869c09b82f22cc5e1666c3803f56a84f&mpshare=1&scene=1&srcid=0311AblXeZcZnhw5hMg3o7xI&sharer_shareinfo=38ca43ce0163ec0a3d17cf759565d2af&sharer_shareinfo_first=65f12cd27132058e786435d42b931d6c) by @Guangya Liu (IBM), Sujay Solomon (Google) — Cubox 收藏文章，inference-engines 领域相关内容 `Anthropic` `LLM` `Agent` `Inference` 🇨🇳
- [AI 是一块“五层蛋糕”](https://blogs.nvidia.cn/blog/ai-5-layer-cake/) — Cubox 收藏文章，inference-engines 领域相关内容 `Inference` 🇨🇳
- [Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务](https://mp.weixin.qq.com/s?__biz=MzU3NDQ3MDg2MA==&mid=2247484117&idx=1&sn=761c1843850dc13fba1a9ed4f912292c&chksm=fc67b8d086be885fa36535bb6597eb3e56e04234c66ea06f9e387c62c727918252dae421197f&mpshare=1&scene=1&srcid=102051f2hEfpd15fJFVYIXe1&sharer_shareinfo=3b9de612d2a8b9241d53cfcc940ed665&sharer_shareinfo_first=3b9de612d2a8b9241d53cfcc940ed665) — 关于 AI Agent 的收藏文章 `Anthropic` `LLM` `Agent` `Inference` `Transformer` 🇨🇳
- [[译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？](https://mp.weixin.qq.com/s?__biz=MzI4MTQyNzkxNw==&mid=2247484077&idx=1&sn=a9ea8f707fe733c43f8c5e8b119efd95&chksm=eaa3bb549d34d9b69fa713d6f5a05ee7aebbe587ddbcc7105cdfb25ececa5bd138a5a140cde0&mpshare=1&scene=1&srcid=0406EAJwfSBv8kNBXXR6T3mD&sharer_shareinfo=1285f5c35b21a56bde53198b6074ed60&sharer_shareinfo_first=1285f5c35b21a56bde53198b6074ed60) — Cubox 收藏 — [译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？ 🇨🇳

## 量化 (1)

- [ChatGPT背后的语言模型简史](https://www.bmpi.dev/dev/deep-learning/nlp-language-models/) — 关于ChatGPT背后的语言模型简史的收藏文章 `[]` `chatgpt` 🇨🇳

## 端侧与边缘 (9)

- [Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA](https://x.com/TrevinPeterson/status/2027404303749546459) by @TrevinPeterson — 双 Mac Studio RDMA 池化跑 Qwen3.5-122B，52 tok/s 稳定吞吐 `qwen` `mac-studio` `rdma` `exo` `local-inference` 🌐
- [MeKi —— 用 ROM 扩展端侧 LLM，而不是继续硬堆计算](#) by @允许动态投影、归一化、非线性映射这些复杂结构存在，以保证模型能学到足够好的知识表达；部署前，再把这些东西折叠到静态查表结构里。于是： — 端侧 AI 部署的实用研究 `perfetto` `on-device` `agent` `android` `llm` 🇨🇳
- [My self-sovereign / local / private / secure LLM setup, April 2026](https://vitalik.eth.limo/general/2026/04/02/secure_llms.html) — Vitalik 以隐私为第一优先级的本地 LLM 方案，硬件选型和软件栈都有参考价值 `local-LLM` `privacy` `security` `Vitalik` `self-sovereign` 🌐
- [V 神本地 LLM 环境配置](https://x.com/fkysly/status/2040976089196167538) by @马天翼 — V 神的本地 LLM 全栈配置方案，从硬件到离线防幻觉策略。 `本地LLM` `Vitalik` `隐私` `离线` `硬件配置` 🇨🇳
- [PocketLLM: Enabling On-Device Fine-Tuning for Personalized LLMs](#) — 端侧 AI 部署的实用研究 `perfetto` `on-device` `fine-tuning` `coding` `android` 🇨🇳
- [Qualcomm Snapdragon X2 Elite微架构](https://mp.weixin.qq.com/s?__biz=MzkzMTA2NjgzMA==&mid=2247488554&idx=1&sn=1e38328c97b182f71c139e0fc69447da) by @亦安 — 高通第三代 Oryon 核心微架构详解，自研 CPU 已具竞争力 `Qualcomm` `Snapdragon` `Oryon` `CPU` `微架构` 🇨🇳
- [快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium与Airtest最为 - 掘金](https://juejin.cn/post/7462305424554590219) — Cubox 收藏 — 快让Appium自动化测试你的App吧适用于移动端的UI自动化测试框架有很多，其中主要以Appium 🇨🇳
- [移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调实现NPU高效部署](https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2449991915&idx=1&sn=da3dd89e182f04dee8c8c5ac2ade9141&chksm=b0f950be96af7bc12328a5ee74bbfc11ed6b5b909d5e2424fbfe181c67021350ab246993d8e0&mpshare=1&scene=1&srcid=0828uXErCxwOEwzSvr55C1dO&sharer_shareinfo=68e9331636d3c4869d8011f376bf8128&sharer_shareinfo_first=68e9331636d3c4869d8011f376bf8128) — Cubox 收藏 — 移动端长文本处理新算法！vivo与联发科提出EdgeInfinite-Instruct，分段监督微调 🇨🇳
- [端侧 AI](https://mp.weixin.qq.com/s?__biz=MzkyMTU4OTE2OA==&mid=2247488655&idx=1&sn=dbf749f318315a561f12f7966be09b84&chksm=c1801050f6f79946a2d6e6a1a04e9cbe0f1fc8364be2e886ac6fa6ec7d54d16db791481279ab&mpshare=1&scene=1&srcid=0620BptoCw1X2FVALZd6If67&sharer_shareinfo=14850c869ec881aeaed27ab4d570556b&sharer_shareinfo_first=e2db0e175c1edf666b0021e55fa7de74) — Cubox 收藏 — 端侧 AI 🇨🇳

## 推理服务平台 (0)

_暂无条目_
