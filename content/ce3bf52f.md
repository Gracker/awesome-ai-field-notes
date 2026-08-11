# CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG

> Source: https://arxiv.org/abs/2608.07458
> Author: Gyuwan Kim, Cheoneum Park, Tao Yang
> Date: 2026-08-07
> Category: infra
> Type: paper
> Quality: 4/5
> Tags: rag, kv-cache, long-context, inference-optimization, arxiv

## English Summary

CoinRAG optimizes the Pareto frontier of RAG under low prefill latency constraints by compositionally reusing offline-computed, fine-grained nugget caches. Instead of full-chunk encoding, it identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and assembles their sliced KV representations with chunk-level context. Evaluations on LongBench multi-hop QA tasks show CoinRAG significantly reduces operational costs and achieves an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

## 中文概要

CoinRAG 通过复用离线计算的细粒度金块缓存来优化长上下文 RAG 的延迟-质量 Pareto 前沿它不再对整个 chunk 编码，而是通过两阶段检索识别查询相关的语义单元，将其切片 KV 表示与 chunk 级上下文拼装在 LongBench 多跳问答任务上，答案质量 (F1) 平均相对提升 5.3%，同时显著降低运营成本

---

*Added via external-scan on 2026-08-11*
