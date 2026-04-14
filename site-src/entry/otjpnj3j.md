---
title: '搞懂缓存机制，从Gemma4到Claude Code省80%Token'
sidebar: false
---

::: info
[← 返回基础设施](/infra)
:::

# 搞懂缓存机制，从Gemma4到Claude Code省80%Token

> 从 KV 缓存原理到 Claude Code 实战，系统讲透 token 省钱机制

🔗 [原文链接](https://x.com/MinLiBuilds/status/2041178722230030384) | @MinLiBuilds | 🇨🇳 | ⭐⭐⭐⭐⭐ 5 ⭐5 5/5 📅 2026-04-10

`kv-cache` `claude-code` `token-optimization` `transformer` `caching` `prompt-caching`

---

搞懂缓存机制，从Gemma4到Claude Code省80%Token

从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。

## LLM 缓存机制

Caching in LLMs primarily aims to avoid redundant computations and API calls by storing and reusing previous results. Several types of caching are employed:

* **Prompt Caching (KV Cache Reuse / Prefix Matching)**:
  * When an LLM processes a prompt, it generates key-value (KV) cache entries in its attention layers. These represent the relationships between tokens. Normally, this KV cache is recomputed for every request.
  * Prompt caching stores these KV cache entries so that if a subsequent request shares the same prefix (the beginning of the prompt), the model can reuse the cached computation for that portion. This skips redundant "prefill" work, reducing latency and input costs.
  * Providers like Anthropic (for Claude) offer prompt caching, with cache reads priced at a significant discount (e.g., 0.1x the base input cost, equating to a 90% discount). OpenAI also offers automatic caching, leading to up to 50% cost savings.
  * This works best when prompts are structured with stable content (like tool definitions, system prompts, reference documents) first, and variable content (user query) last.

* **Exact Match Caching (Request/Response Caching)**:
  * This is the simplest form, storing the entire LLM response for a specific, identical prompt. If the exact same prompt (and other parameters) is received again, the cached response is returned immediately, bypassing the LLM call entirely.
  * It's highly effective for frequently asked questions or deterministic queries.

* **Semantic Caching**:
  * A more sophisticated approach that understands the *meaning* behind queries, not just exact wording.
  * When a new prompt arrives, its embedding (numerical representation) is generated and compared against cached embeddings. If a sufficiently similar query is found (based on a similarity threshold), the cached response is returned.
  * Semantic caching can bypass LLM calls entirely for similar questions, saving both input and output token costs, making it generally more cost-effective for workloads with varied phrasing of similar questions. It can achieve significant cost reductions, with some reports indicating up to 86%.

## Token Saving Strategies

While "Gemma4" likely refers to Google's Gemma models (e.g., Gemma 1.5 Pro) and "Claude Code" refers to Anthropic's Claude models used for coding, the principles of token optimization are broadly applicable across LLMs. The goal is to reduce the number of tokens processed and generated, which directly impacts cost and latency.

**Strategies for Token Reduction, particularly in a coding context like Claude Code:**

* **Leverage Provider-Side Caching**:
  * Enable and utilize prompt caching features offered by LLM providers. For Anthropic's Claude, this means using `cache_control` markers for explicit caching or benefiting from automatic caching.
  * Anthropic's prompt caching can lead to up to 90% cost reduction for long prompts and 85% latency reduction.

* **Effective Context Management**:
  * **Minimize Input Context**: Only provide the necessary information. Stale or irrelevant context wastes tokens on every message.
  * **Clear Between Tasks**: For interactive environments like Claude Code, use commands like `/clear` to reset the accumulated context when switching to unrelated work.
  * **Summarization/Compaction**: For long conversation histories, summarize them to preserve critical information while reducing token count. Claude Code offers `auto-compaction` to summarize conversation history when approaching context limits.
  * **Structured Documentation (MinLiBuilds/Claude Code)**: Structure documentation so that Claude only loads what's needed. For example, essential files at startup, with other topic-based learnings loaded on demand. This approach can lead to significantly reduced initial context tokens.

* **Prompt Engineering**:
  * **Concise Prompts**: Write prompts that are direct and to the point, avoiding unnecessary verbosity.
  * **Request Concise Output**: Explicitly ask the LLM to "be concise" in its responses to reduce output token count.
  * **Optimize Prompt Structure**: Place stable information (system prompts, tool definitions) at the beginning of your prompt to maximize cache hit rates for prefix matching.

* **Model Selection**:
  * Use the most cost-effective model for the task. For example, using a smaller, cheaper model (like Claude Haiku) for simple tasks and reserving more powerful, expensive models (like Claude Opus) for complex reasoning or architecture reviews. This alone can save 40-70%.

* **Reduce "Thinking" Tokens (Claude Code Specific)**:
  * Claude's "thinking" process consumes tokens you don't directly see. Reducing `MAX_THINKING_TOKENS` from default values (e.g., 31,999) to a lower, sufficient amount (e.g., 10,000 for most coding tasks) can significantly cut hidden costs.

* **Disable Unused Features**:
  * In environments like Claude Code, disable unused tools and connectors, as their definitions can consume thousands of tokens per message.

* **Layered Caching**: Combine multiple caching strategies for maximum benefit. For instance, start with exact-match, then add semantic caching, and leverage provider-level prompt caching for system prompts.

By diligently applying these caching mechanisms and token optimization strategies, developers can achieve significant cost savings and latency improvements, potentially reaching the 80% token reduction target mentioned in the query. MinLiBuilds emphasizes that understanding caching is crucial for managing LLM costs in production, with savings potentially ranging from thousands to tens of thousands of dollars monthly.
