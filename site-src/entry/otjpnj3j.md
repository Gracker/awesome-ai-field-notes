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

# 搞懂缓存机制，从Gemma4到Claude Code省80%Token

## 缓存机制概述

从广义上讲，缓存是一种存储机制，它将数据保存在一个临时位置，以便在下次需要时能够快速检索，从而避免重新执行昂贵或耗时的获取和计算过程。缓存的原理基于"数据局部性"——在一定时间内，数据访问往往集中在某一部分。当CPU处理数据时，它会首先在缓存中查找，如果数据已存在，则无需从较慢的主内存中重新读取。

缓存通常分为两种主要类型：
* **强制缓存（Strong Cache）**：浏览器在不向服务器发送请求的情况下，直接从缓存中读取资源。服务器通过HTTP响应头中的`Expires`和`Cache-Control`字段来设置强制缓存规则。
* **协商缓存（Negotiation Cache）**：当强制缓存失效后，浏览器会携带缓存标识（如`Last-Modified` / `If-Modified-Since`或`Etag` / `If-None-Match`）向服务器发送请求。服务器根据这些标识判断资源是否更新，如果未更新则返回304状态码，通知浏览器继续使用本地缓存。

### LLM中的缓存机制与Token优化

在大型语言模型中，Token是处理文本的基本单位。LLM的API调用成本通常基于Token使用量，因此Token数量直接影响计算资源消耗、推理速度、上下文理解能力及使用成本。 每次与LLM交互，即使是相同或相似的查询，都可能导致重复的计算和Token消耗。

为了解决这些问题，LLM引入了多种缓存策略：

1. **精确匹配缓存（Exact Key Caching）**：
这种策略最为直接，它存储特定输入查询的LLM响应。如果用户提交完全相同的输入，则直接返回缓存的响应，而不是再次调用LLM。 这种方法对于重复性高、输入不变的查询非常有效，例如对某个产品描述进行总结。

2. **语义缓存（Semantic Caching）**：
精确匹配缓存对输入的微小变动很敏感。为了处理用户可能以不同措辞表达相同意思的情况（例如"总结这段文字"和"能否给我一个摘要"），语义缓存将每个提示嵌入为向量，并对过去的提示执行相似性搜索。如果找到语义上相似的提示，则重用其缓存的响应。 这可以显著提高缓存命中率，但需要额外的向量嵌入和相似性搜索步骤。

3. **提示缓存（Prompt Cache）/KV缓存复用**：
Transformer模型在推理过程中会生成键值（KV）对，这些KV对代表了输入序列的注意力状态。对于包含重叠文本段（如系统消息、模板或上下文文档）的提示，Prompt Cache通过预先计算并存储这些常见文本段的注意力状态，从而在用户提示中快速重用它们，避免重复计算。 Anthropic的Claude模型API已经推出了提示缓存功能，声称可以降低90%的成本和85%的延迟。

### MinLiBuilds与Claude Code的Token优化

根据搜索结果，MinLiBuilds在GitHub上分享了关于大型模型推理优化，特别是KV Cache机制、前缀匹配缓存策略以及Token消耗分析与优化的研究和实践。 他们的"Project Memory"项目针对Claude Code提出了一个持久化知识层，旨在解决Claude Code在每个会话开始时重新读取大量文件、重新解释架构决策以及重复发现API问题的问题。

MinLiBuilds指出，每次Claude Code会话都会从头开始，重新读取多达50多个文件，导致大量的Token消耗。通过"Project Memory"，Claude Code不再需要每次都读取整个代码库（可能达到100K Token），而是通过调用`get_context`获取一个约100 Token的概述，只有在需要更深入查询时才进行。

MinLiBuilds提供了一些实际案例来展示通过这种方法实现的Token节省：
* "哪些文件导入了shared.js？" — 从45,000 Token减少到350 Token（节省99%）。
* "BM25搜索如何工作？" — 从11,000 Token减少到700 Token（节省93%）。
* "为什么我们选择ONNX嵌入？" — 从2,500 Token减少到200 Token（节省92%）。
* 重用复杂脚本 — 从2,000 Token减少到300 Token（节省85%）。

这些显著的Token节省百分比（包括85%）表明，MinLiBuilds主要通过在Claude Code内部实施智能的上下文管理和缓存机制，避免了重复提交大量代码或历史上下文作为输入，从而大幅降低了API调用成本和延迟。

### Gemma4与Claude Code的Token管理考量

Gemma4是Google发布的最新一代开放模型，具有强大的多模态能力、长上下文窗口（最高可达25.6万Token）和针对设备部署的优化。 它支持多步骤规划、自主行动、离线代码生成以及音频-视觉处理。

尽管Gemma4功能强大，但将其作为Claude Code的直接替代品来节省Token时，会面临一些挑战。有用户尝试在本地部署Gemma4以替代因Token消耗膨胀的Claude Code时，遇到了性能问题，例如生成速度慢、首Token延迟高以及上下文窗口（即使是32K）在面对Claude Code高达29000+ Token的系统提示时仍显不足。 这说明Claude Code的设计可能高度依赖其云端模型的超长上下文处理能力和Anthropic自身的优化。

因此，MinLiBuilds所讨论的"从Gemma4到Claude Code省80%Token"更准确的理解可能是在**使用Claude Code时，通过像"Project Memory"这样的高级缓存和上下文管理技术，实现了80%的Token节省**。这并非意味着将Gemma4直接替换Claude Code就能自然地节省Token，而是在特定的工作流和应用场景下，通过精细的Token优化策略，使LLM的使用更加高效和经济。
