# Compact Documentation for Coding Agents: A Benchmark, an Optimizer, and Why It Does Not Transfer

> 原文链接: https://arxiv.org/abs/2609.31587
> 作者: Md Shohel Arman, Igor Molybog
> 发布时间: 2026-09-25
> 源: arXiv外部扫描 (2026-09-29)

---

## 摘要

arXiv 2609.31587 做了一个诚实的负结果研究：先用 roundtrip 基准（从描述再生代码能否通过原测试）证明描述的完整性而非长度决定保真度，并用它作优化信号找到能全保真且泛化到未见文件的描述生成 prompt；但假设检验环节发现在两个模型族十个仓库带阳性对照的评估里，只要源码在场，静态紧凑文档和检索上下文都打不过 issue 本身文档对 coding agent 的增益存在清晰边界

## English Summary

We investigate whether natural-language documentation helps coding agents resolve software issues, and we build the tools to construct and evaluate it. We introduce a roundtrip benchmark that scores code descriptions by whether code regenerated from them passes the original tests, and show that completeness, not length, drives a description's fidelity. Using the benchmark as an optimization signal, we discover a description-writing prompt that reaches full fidelity and generalizes to unseen files. We then test the hypothesis that motivated the work: that better documentation helps an agent resolve real repository issues. Across two model families and ten repositories, and against a positive control confirming that our evaluation can detect a genuine improvement, we find that it does not....

## 为什么值得关注

扩展 AAIF 对应主题线

## 信息源

- https://arxiv.org/abs/2609.31587
