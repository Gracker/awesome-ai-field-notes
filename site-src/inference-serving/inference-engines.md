# 推理引擎

Inference Engines — 5 条活跃资源

### [搞懂缓存机制，从Gemma4到Claude Code省80%Token](https://x.com/MinLiBuilds/status/2041178722230030384) 
by @MinLiBuilds (2026-04-06) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**从 KV 缓存原理到 Claude Code 实战，系统讲透 token 省钱机制**

从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。
 `kv-cache` `claude-code` `token-optimization` `transformer` `caching` `prompt-caching`

---
### [AI 代理可观测性 - 演变标准与最佳实践](https://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247553129&idx=2&sn=b096969e9b11351ee311f13f4cb15c1b&chksm=ed4dcaeea8eed4db84fd7e26c9216b026b402f2de5aa869c09b82f22cc5e1666c3803f56a84f&mpshare=1&scene=1&srcid=0311AblXeZcZnhw5hMg3o7xI&sharer_shareinfo=38ca43ce0163ec0a3d17cf759565d2af&sharer_shareinfo_first=65f12cd27132058e786435d42b931d6c) 
by @Guangya Liu (IBM), Sujay Solomon (Google) (2025-03-11) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，inference-engines 领域相关内容**

AI 代理可观测性 - 演变标准与最佳实践
AI 代理将在 2025 年成为人工智能的下一个重大飞跃，AI 代理的可观测性变得尤为重要，特别是在将这些代理扩展以满足企业需求时。没有适当的监控、追踪和日志记录机制，诊断问题、提高效率和确保 AI 代理驱动应用的可靠性将面临挑战。
Read in Cubox  
Read Original
作者：Guangya Liu (IBM), Sujay Solomon (Google)
AI 代理将在 2025 年成为人工智能的下一个重大飞跃。从自主工作流到智能决策，AI 代理将为各行业的众多应用提供动力。然而，随着这一演变，AI 代理的可观测性变得尤为重要，特别是在将这些代理扩展以满足企业需求时。没有适当的监控、追踪和日志记录机制，诊断问题、提高效率和确保 AI 代理驱动应用的可靠性将面临挑战。
 `Anthropic` `LLM` `Agent` `Inference`

---
### [AI 是一块“五层蛋糕”](https://blogs.nvidia.cn/blog/ai-5-layer-cake/) 
 (2026-03-11) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏文章，inference-engines 领域相关内容**

Read in Cubox  
Read Original
**2026 年 3 月 10 日 作者 黄仁勋**
AI 是塑造当今世界的强大力量之一。它并非仅仅是一款巧妙的应用程序，也不是单一的模型，而是如同电力和互联网一样必不可少的基础设施。
AI 依托真实的硬件、能源和经济体系运行。它可以将原材料大规模地转化为智能。每家公司都将应用 AI， 每个国家/地区都将发展 AI。
要理解 AI 为何以这种方式发展，我们需要从基本原理进行推理，并了解计算领域发生了哪些根本性变化。
 `Inference`

---
### [Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务](https://mp.weixin.qq.com/s?__biz=MzU3NDQ3MDg2MA==&mid=2247484117&idx=1&sn=761c1843850dc13fba1a9ed4f912292c&chksm=fc67b8d086be885fa36535bb6597eb3e56e04234c66ea06f9e387c62c727918252dae421197f&mpshare=1&scene=1&srcid=102051f2hEfpd15fJFVYIXe1&sharer_shareinfo=3b9de612d2a8b9241d53cfcc940ed665&sharer_shareinfo_first=3b9de612d2a8b9241d53cfcc940ed665) 
 (2025-10-20) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**关于 AI Agent 的收藏文章**

Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务
Anthropic 揭秘让 AI 更靠谱的「上下文工程」
Read in Cubox  
Read Original
> https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
你有没有过这样的体验？跟 AI 聊得久了，它突然 "失忆"------ 前面提过的关键信息没了下文，甚至答非所问；让它处理复杂任务，比如分析大数据库、写长代码，它越往后越混乱...... 其实不是 AI "不认真"，而是它的 "注意力" 有限。
 `Anthropic` `LLM` `Agent` `Inference` `Transformer`

---
### [[译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？](https://mp.weixin.qq.com/s?__biz=MzI4MTQyNzkxNw==&mid=2247484077&idx=1&sn=a9ea8f707fe733c43f8c5e8b119efd95&chksm=eaa3bb549d34d9b69fa713d6f5a05ee7aebbe587ddbcc7105cdfb25ececa5bd138a5a140cde0&mpshare=1&scene=1&srcid=0406EAJwfSBv8kNBXXR6T3mD&sharer_shareinfo=1285f5c35b21a56bde53198b6074ed60&sharer_shareinfo_first=1285f5c35b21a56bde53198b6074ed60) 
 (2025-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Cubox 收藏 — [译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？**

AI编译器的根本性权衡：既要通过抽象底层细节来实现易用性和可扩展性，但现代生成式AI工作负载又需要可编程性和硬件控制来实现极致性能。


---