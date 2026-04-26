# Prompt Caching in LLMs!
*LLM 中的 Prompt Caching*

**来源:** Avi Chawla, Daily Dose of Data Science
**发布日期:** 2026-03-10
**原文链接:** https://dailydoseofds.com/p/prompt-caching-in-llms

---

**🇬🇧 EN:**

A case study on how Claude achieves 92% cache hit-rate.

## How Prompt Caching Works

Prompt caching is an optimization technique that stores and reuses the unchanging parts of an LLM prompt, often referred to as 'prefixes' or 'static content,' to avoid redundant computation.

**Key mechanism:** When a prompt with caching enabled is sent, the system checks if a prefix of that prompt has been cached from a previous query. If a match is found, the model reuses the stored computational state (KV cache) for that prefix, significantly reducing processing needed for the current request.

## The KV Cache Explained

In Transformer-based LLMs, text generation occurs one token at a time. Each token generates Query (Q), Key (K), and Value (V) vectors. The Query vector represents what the current token is looking for, while the Key and Value vectors represent information contained within past tokens.

**Without optimization:** The model recomputes K and V vectors for all preceding tokens at every generation step — computationally expensive, especially for long sequences.

**With KV cache:** K and V tensors for previously processed tokens are stored in memory. When generating a new token, the model retrieves stored K and V vectors from cache, avoiding redundant computation.

## Claude Code's Caching Strategy

Claude Code employs an aggressive prompt caching strategy. It caches essential components:
- System prompt
- Tool definitions
- CLAUDE.md content
- Segments of conversation history

**Cost savings:** Cache reads can be as low as ~10% of base input token price. There's a ~25% premium for cache writes to cover VRAM allocation.

## Three Rules for High Cache Hit Rate

1. **Never modify tools mid-session** — Adding, removing, or reordering tool definitions invalidates the cache
2. **Never switch models** — Cache is model-specific
3. **Never mutate the cached prefix** — Dynamic elements like telemetry headers or git status injected into prompts can cause cache misses

## Key Benefits

- **Reduced Latency:** Skipping redundant processing gives significantly faster response times
- **Lower Costs:** Reusing cached tokens means fewer tokens processed by the LLM → substantial API savings
- **Improved Efficiency:** Optimizes resource usage, reserving compute for novel prompt content

A 92% cache hit rate in production is considered an uptime-grade metric. It translates directly to 81% cost reduction (Claude Code example: $6.00 → $1.15 per session).

---

**🇨🇳 中文翻译:**

一篇关于 Claude 如何实现 92% 缓存命中率的案例研究。

## Prompt Caching 是如何工作的

Prompt Caching 是一种优化技术，通过存储和复用 LLM prompt 中不变的部分（即「前缀」或「静态内容」），来避免冗余计算。

**核心机制：** 当发送启用了缓存的 prompt 时，系统会检查该 prompt 的前缀是否从之前的查询中被缓存过。如果找到匹配，模型会复用该前缀的存储计算状态（KV cache），从而显著减少当前请求所需的处理量。

## KV Cache 详解

在基于 Transformer 的 LLM 中，文本生成一次产生一个 token。每个 token 会生成 Query (Q)、Key (K) 和 Value (V) 向量。Query 向量代表当前 token 在寻找什么，而 Key 和 Value 向量代表过去 token 中包含的信息。

**无优化时：** 模型在每个生成步骤中都会重新计算所有前序 token 的 K 和 V 向量——这在计算上非常昂贵，尤其是在长序列场景下。

**有 KV cache 时：** 已处理 token 的 K 和 V 张量存储在内存中。当生成新 token 时，模型直接从缓存中检索存储的 K 和 V 向量，避免冗余计算。

## Claude Code 的缓存策略

Claude Code 采用了激进的 prompt caching 策略。它缓存以下关键组件：
- 系统提示词
- 工具定义
- CLAUDE.md 内容
- 对话历史的片段

**成本节省：** 缓存读取价格可低至基础输入 token 价格的约 10%。缓存写入有约 25% 的溢价，用于覆盖 VRAM 分配成本。

## 保持高缓存命中率的三大原则

1. **会话期间绝不修改工具** — 添加、删除或重新排序工具定义会使缓存失效
2. **绝不切换模型** — 缓存是模型特定的
3. **绝不变更缓存前缀** — 动态元素（如注入到 prompt 中的遥测 header 或 git status）可能导致缓存未命中

## 核心优势

- **降低延迟：** 跳过冗余处理，响应速度显著提升
- **降低成本：** 复用缓存 token 意味着 LLM 需要处理的 token 更少 → API 成本大幅节省
- **提升效率：** 优化资源使用，将计算资源留给 prompt 中的新内容

在生产环境中达到 92% 的缓存命中率，被视为一个堪比可用率的关键指标。它直接转化为 81% 的成本降低（Claude Code 案例：$6.00 → $1.15/会话）。