---
title: 'AI工具设计：为什么需要理解用户心理'
sidebar: false
---

::: info
[← 返回llm-infra/inference-optimization](/llm-infra/inference-optimization)
:::

# AI工具设计：为什么需要理解用户心理

> 目前最详尽的 Prompt Caching 工程实践解析，Claude Code 案例极具说服力

🔗 [原文链接](https://x.com/_avichawla/article/2044670188998803855) | @Avi Chawla | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-06

`prompt-caching` `kv-cache` `claude` `cost-optimization` `agent`

---

备注：opencli 抓取返回非目标内容，以下内容基于 Obsidian 原文提取。

# AI工具设计：为什么需要理解用户心理

A case study on how Claude achieves 92% cache hit-rate.

Every time an AI agent takes a step, it sends the entire conversation history back to the LLM. That includes the system instructions, the tool definitions, and the project context. All of it gets re-read, re-processed, and re-billed on every single turn.

A system prompt with 20,000 tokens running over 50 turns means 1 million tokens of redundant computation billed at full price, producing zero new value.

The fix is prompt caching. Key vectors (K,V) for any given token depend only on the tokens before it, and once computed, they never change. The KV cache persists those tensors on inference servers, indexed by a cryptographic hash of the token sequence. This drops complexity from O(n^2) per generated token to O(n).

Pricing: Cache reads cost 0.1x the base input price (90% discount); cache writes cost 1.25x.

Claude Code built around keeping the cache hot: static prefix stays stable across turns. A real 30-minute coding session: 2 million tokens at $6.00 without caching vs $1.15 with 92% hit rate (81% reduction).

Three rules: (1) Never modify tools during a session, (2) Never switch models mid-session, (3) Never mutate the prefix to update state. Claude Code appends reminder tags to user messages instead.
# AI工具设计：为什么需要理解用户心理

URL: https://x.com/_avichawla/article/2044670188998803855
Author: Avi Chawla
Date: 2026-04-06

## Summary (ZH)
Avi Chawla 通过 Claude Code 案例详细解析了 LLM Prompt Caching 的技术原理与工程实践。核心观点：KV Cache 将计算复杂度从 O(n^2) 降至 O(n)，静态前缀（系统指令、工具定义、项目上下文）可被缓存并以 0.1x 价格读取。Claude Code 实测 92% Cache Hit Rate，实现 81% 成本降低（$6.00 -> $1.15）。三大工程原则：不要在会话中修改工具定义、不要中途切换模型、不要在缓存前缀中注入状态变量。

## Summary (EN)
Detailed case study on how Claude's prompt caching works via KV Cache, reducing computational complexity from O(n^2) to O(n) per token. Static prefix (system instructions, tool definitions, project context) is cached and read at 0.1x price. Claude Code achieves 92% cache hit rate with 81% cost reduction ($6.00->$1.15). Three rules: never modify tools mid-session, never switch models, never mutate the cached prefix.
