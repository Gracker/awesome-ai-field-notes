---
title: "JetSpec Enables Up to 9.64x Lossless LLM Inference Speedup with Up to 1000TPS"
url: "https://haoailab.com/blogs/parallel-tree-decoding/"
source: "Hao AI Lab"
source_url: "https://haoailab.com/blogs/parallel-tree-decoding/"
original_date: "2026-06-25"
tags: ["speculative-decoding", "inference-optimization", "jetspec", "parallel-tree-decoding", "llm"]
language: "en"
quality_score: 4
one_liner: "Hao AI Lab 的 JetSpec 用并行树形 draft 把投机解码推上 9.64x 无损加速，单卡 1000 TPS"
summary_zh: "Hao AI Lab 发布 JetSpec：用并行树形 draft head 突破传统投机解码的 scaling ceiling，在多个推理任务上取得最高 9.64 倍无损加速，单卡吞吐可达 1000 TPS其关键设计是让 draft 在一次前向中产出大量树节点，并让每个节点以分支前缀而非绝对未来位置为条件，再用冻结的目标模型做树验证，仅承诺其同意的前缀"
---

# JetSpec Enables Up to 9.64x Lossless LLM Inference Speedup with Up to 1000TPS

> 备注：以下为自动提取的正文内容。

Side-by-side comparison of decoding speed among JetSpec, DFlash and AR baseline.

Low drafting cost: generate many tree nodes in one draft-head forward pass.

High acceptance: condition every node on its branch prefix, not just on its absolute future position.

Lossless verification: let the frozen target verify the tree and commit only the prefix it agrees with.

Generalizability: largest gains appear on reasoning-heavy math and coding tasks, in consistent with our training data choice. JetSpec also generalizes with >4x speedup on open-ended conversational tasks.

Non-greedy sampling: gains shrink but remain consistent, showing the causal-tree benefit is not limited to deterministic decoding.

Budget scaling: larger tree budgets help JetSpec more reliably because the draft tree stays branch-conditioned.

In this experiment we compare tree quality with and without causality enforced. The gap is measured the drafter’s log-probability difference, in nats (natural-log units), between its top-ranked branch and the target’s preferred continuation. A small gap means the tree contains the branch the target is more likely to accept and therefore a higher quality. On MATH-500, without loss weighting the block-diffusion head is miscalibrated, accepting a mean 4.84 tokens per round against the causal head’s 9.46.

Website and Demos: https://jetspec-project.github.io/jetspec-web/

