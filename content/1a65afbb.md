# Harness-Aware Self-Evolving: Co-Evolving Model Weights, Harness, and Task Solutions

> External-scan entry · 2026-07-08 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.03935
- **Source**: arxiv · Haochen Luo, Yi Huang, Sichun Luo, Fengyuan Liu, Lei Li, Zefa Hu
- **Original Date**: 2026-07-07
- **Added**: 2026-07-08
- **Category**: agents
- **Tags**: harness-engineering, self-evolving, agentic-rl, qwen3, claude-code
- **Quality Score**: 4

## 中文摘要

现有 self-evolving 框架通常只优化任务解，harness 当作固定背景 本文提出 HASE 在多轮动作空间里让单一模型既能产出任务解也能改写选定的 harness 组件一个 Qwen3-8B 在文本分类上即可打平用 Claude Code 做 harness 提议方的 GPT-OSS-120B；在 alpha factor mining 上超越已报告的 GPT-OSS-120B 基线；HASE 还能修复不完善的评测组件并在 circle-packing 算法发现上收敛到 SOTA 一句话：harness 与方案通过同一个统一 agentic 过程共同进化

## English Abstract

Self-evolving frameworks usually optimize task solutions while treating the surrounding harness as fixed. We introduce Harness-Aware Self-Evolving (HASE), an agentic reinforcement-learning framework in which a single model can generate task solutions or edit selected harness components in a multi-turn action space. HASE enables a single Qwen3-8B model to match the text-classification performance of a GPT-OSS-120B model that uses Claude Code as the harness proposer. In alpha factor mining, HASE outperforms the reported GPT-OSS-120B baseline; HASE also repairs imperfect evaluation components and converges to state-of-the-art performance in circle-packing algorithm discovery. These results show that HASE improves the harness and the solution through one unified agentic process.

## One-liner

现有 self-evolving 框架通常只优化任务解，harness 当作固定背景 本文提出 HASE 在多轮动作空间里让单一模型既能产出任务解也能改写选定的 harness 组件一个 Qwen3-8B 在文本分类上即可打平用 Claude Code 做 harness 提议方...

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
