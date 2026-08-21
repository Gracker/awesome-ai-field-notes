# What is Missing from AI Post-Training AI: An Empirical Analysis

- arXiv: [2608.19072](https://arxiv.org/abs/2608.19072)
- Authors: Joy Jia Yin Lim, Xin Huang, Hao Peng, Yaxi Lu, Xin Cong, Zhong Zhang, Maosong Sun, Yankai Lin
- Published: 2026-08-19; categories: cs.AI, cs.CL, cs.LG

## Abstract

Large language model (LLM) agents can now post-train an LLM end-to-end. They can write code, launch training, evaluate checkpoints, and improve downstream performance, raising the prospect of AI-for-AI. We argue that this picture conflates two distinct capabilities: execution-level capability, iterating within a selected training strategy; and strategy-level capability, revising the high-level judgment as experimental evidence accumulates. Analyzing a large corpus of publicly released post-training trajectories, we find that across different tasks, the agent's training strategy is locked in at the very beginning, and the entire remaining budget is spent on local adjustments within the selected strategy. We then examine three natural explanations--missing experience, missing guidance, and insufficient reasoning--with escalating interventions. Extensive experiments show that (1) an experience-driven scaffold improves execution across the board (+12.6 points on GSM8K and +40.8 on HumanEval) but leaves the strategy static; (2) human guidance effectively redirects the initial strategy, yet the agent falls back into local adjustment loops once training starts; and (3) additional inference compute pays off on easier tasks but yields almost no gain on the hardest one. In conclusion, what agents lack is neither experience, guidance, nor reasoning compute, but a mechanism for spontaneously reevaluating their strategy during execution.

## Why it matters (AAIF scan)

对公开发布的 post-training 轨迹做实证分析：LLM agent 能端到端执行选定的训练策略，但策略在最开头就锁定，剩余预算全部花在局部调整。递进式干预实验显示：经验脚手架提升执行（GSM8K +12.6、HumanEval +40.8）但策略不变；人类指导能改变初始策略但训练一开始就回落局部循环；额外推理算力只在简单任务有效。结论：缺的是执行中自发重新审视策略的机制。

> Source: https://arxiv.org/abs/2608.19072