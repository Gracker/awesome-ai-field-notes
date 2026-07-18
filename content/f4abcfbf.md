# StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems

> External-scan entry · 2026-07-09 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.05844
- **Source**: arxiv · Sergey Volkov, Yang Li, Ye Luo
- **Original Date**: 2026-07-07
- **Added**: 2026-07-09
- **Category**: agents
- **Tags**: multi-agent, memory, crdt, conflict-resolution, replicated-state
- **Quality Score**: 4

## 中文摘要

StateFuse 是一套面向多智能体系统的 conflict-aware 复制内存合约，基于标准 OpSet / CRDT merge，但不引入新连接代数，而是在 agent 一侧加一层语义：不可变历史显式 conflict 对象exact / semantic 修正句柄 (claim_id / claim_ref)确定性谓词契约以及"投影期再解析"在 282 题的 MemoryAgentBench 冲突切片上，几种方法在答案准确率上打平，但保留冲突的 surface 能让矛盾可见提早归并会丢失证据；带显式 correction handle 的语义化句柄对高歧义场景更重要论文对 harness 端的可观测可纠正内存设计有直接启发

## English Abstract

Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (claim_id / claim_ref), deterministic predicate contracts, and projection-time resolution that cannot rewrite replicated state. We evaluate StateFuse against flat multi-value, raw-log, provenance-style, and collapsed baselines under matched resolver and verification policies....

## One-liner

StateFuse 是一套面向多智能体系统的 conflict-aware 复制内存合约，基于标准 OpSet / CRDT merge，但不引入新连接代数.

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
