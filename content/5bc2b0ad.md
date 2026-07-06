# Steerability via constraints: a substrate for scalable oversight of coding agents

> External-scan entry · 2026-07-06 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.02389
- **Source**: arxiv · Coding-agent oversight collective
- **Original Date**: 2026-07-03
- **Added**: 2026-07-06
- **Category**: coding
- **Tags**: coding-agent, oversight, substrate, reviewer-model, security
- **Quality Score**: 3

## 中文摘要

论文主张人类团队管理中用了几十年的手段访问控制网络策略由工具强制执行的严格编码规约可以直接平移到 coding agent 上，而且比近年流行的 agentic scaffolding 在 token 上更便宜作者给出端到端草图，并在 Python 代码库上做了一次可控实验：小模型 Gemma 4 e4b 审查含 11 个后门的项目，召回率从无约束无工具的 54.5% 提升到约束 substrate + 约 200 行 docs CLI的 90.9%，substrate 与工具两条路径独立贡献选择 Python 是因为它在不施加约束时保证最少，作者指出原则同样适用于 Rust 等更严的语言

## English Abstract

Argues that the same access control, network policies, and strict coding conventions enforced by tooling that have governed large human engineering teams for decades transfer directly to coding agents and are cheaper (in tokens) than recent agentic scaffolding. The authors sketch an end-to-end system on this principle and report a controlled experiment in scalable oversight: a small reviewer (Gemma 4 e4b) inspects a Python codebase containing 11 inserted backdoors. Recall rises from 54.5% (unconstrained, no tools) to 90.9% (constrained substrate plus a ~200-LoC docs CLI), with substrate and tools contributing independently. Python is chosen deliberately because substrate-level oversight gains are largest where the language gives the fewest guarantees by default, and the same principles extend to Rust.

## One-liner

Coding agent 监管不该只卷 scaffolding，把人类工程团队的访问控制与编码规约当作 substrate 反而更便宜有效

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
