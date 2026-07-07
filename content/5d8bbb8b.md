# G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models

> External-scan entry · 2026-07-07 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.02491
- **Source**: arxiv · Timo Bertram, Sidhant Bhavnani, Richard Freinschlag, Erich Kobler, Andreas Mayr, Gnter Klambauer
- **Original Date**: 2026-07-03
- **Added**: 2026-07-07
- **Category**: learning
- **Tags**: neuro-symbolic, constraint-satisfaction, recurrent-reasoning, symbolic-solver
- **Quality Score**: 3

## 中文摘要

本文聚焦 SE-RRMs（symbol-equivariant recurrent reasoning models），这是一类对符号置换等变的循环推理模型，相对普通 RRM 在外推到更大问题时表现更稳。作者提出神经-符号方法 G-RRM：用 SE-RRM 作为神经求解器生成完整解的候选，再把候选交给经典符号求解器做约束满足验证与修正，让神经推理负责发散式搜索、符号求解器负责最终一致性。在 CSP 基准上的实验显示，这种引导式集成在解的质量与推理步数上都优于纯神经方案。

## English Abstract

In this work, we focus on SE-RRMs, a symbol-equivariant instantiation of RRMs that exhibits improved extrapolation to larger problem sizes. We propose a neuro-symbolic approach, ``Guiding with Recurrent Reasoning Models&#39;&#39; (G-RRM), which integrates SE-RRMs with symbolic solvers for constraint satisfaction problems. SE-RRMs act as neural solvers that generate full solution proposals and guide classical symbolic solvers, such as backtracking or SAT-based methods like Glucose 4.1 and CaDiCaL 3.0.0, that produce globally correct solutions. Centrally, we investigate when neural guidance with G-RRM improves the search efficiency of symbolic solvers....

## One-liner

本文聚焦 SE-RRMs（symbol-equivariant recurrent reasoning models），这是一类对符号置换等变的循环推理模型，相对普通 RRM 在外推到更大问题时表现更稳。

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
