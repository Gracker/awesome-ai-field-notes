# Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection

- **ID**: 3addb7c9
- **原文链接**: https://arxiv.org/abs/2608.02560
- **PDF**: https://arxiv.org/pdf/2608.02560v1
- **作者**: Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson, M Anthony Lewis, Jonathan Tapson
- **日期**: 2026-08-03
- **更新**: 2026-08-03
- **分类**: infra
- **来源类型**: paper
- **标签**: rag, ssm, edge-llm, persistent-memory
- **质量评分**: 4/5
- **抓取时间**: 2026-08-05T04:19:03Z

---

## 中文导读

PRECOG/SMC 利用 State-Space Model 固定大小位置无关的隐状态，将文档语料离线预编码为 hidden state，查询时直接注入最匹配的状态，从而把 RAG prefill 成本从 O(L_context) 降到 O(1)摘要以 1.2B TENNs-LLM 演示在边缘硬件上将 prefill 延迟从约 27s 降到 <6ms，同时支持层次化持久记忆

## 为什么值得关注

PRECOG injects precomputed SSM states to make edge RAG prefill O(1).

Grounded relevance: authors, date, arXiv categories, and abstract claims below; no extra experimental claims beyond the abstract/metadata.

## 关键信息

- 论文标题：Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection
- 作者：Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson, M Anthony Lewis, Jonathan Tapson
- arXiv：https://arxiv.org/abs/2608.02560
- 发布时间：2026-08-03
- arXiv 分类：cs.LG, cs.AI, cs.IR
- 关联标签：rag, ssm, edge-llm, persistent-memory

## English Abstract

Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent hidden state is a complete summary of everything the model has read. PRECOG pre-encodes document corpora offline as SSM hidden states and injects the best-matching state directly at query time, bypassing in-context re-ingestion entirely. The same state-injection mechanism enables SMC (Structured Memory Consolidation): a hierarchical persistent memory with cognitive-domain clustering, an adjustable fidelity-vs-storage dial, and $O(1)$ session initialization, which consolidates short-term episodic states into long-term semantic memory and fuses both with retrieved corpus states at query time. We demonstrate the system on TENNs-LLM, a 1.2B-parameter gated-SSM language model with a 192 KB hidden state. PRECOG matches in-context RAG answer quality, reducing prefill latency from $\sim$27 s to $<$6 ms on edge hardware -- a $\sim$4500$\times$ speedup that crosses the threshold from unusable to interactive. The mechanism is architecturally impossible for Transformer KV-caches, which are position-entangled and grow linearly with context length.

## English Summary

Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent hidden state is a complete summary of everything the model has read. PRECOG pre-encodes document corpora offline as SSM hidden states and injects the best-matching state directly at query time, bypassing in-context re-ingestion entirely....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- content-fetcher run; entry id `3addb7c9`; arXiv `2608.02560`.
