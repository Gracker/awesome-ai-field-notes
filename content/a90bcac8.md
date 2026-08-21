# Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

- arXiv: [2608.19098](https://arxiv.org/abs/2608.19098)
- Authors: Huan-ang Gao, Haohan Chi, Yong Yan, Shiyuan Feng, Hanlin Wu, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- Published: 2026-08-19; categories: cs.LG, cs.AI, cs.CL

## Abstract

Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) experts into a single generalist student via dense, token-level reward supervision. Despite its practical success, the optimization dynamics governing multi-teacher capability integration remain poorly understood, and open, rigorously reproducible recipes are conspicuously lacking. In this work, we establish a controlled M-OPD benchmark on SmolLM3-3B-Base with oracle routing, isolating capability integration from routing ambiguity. Our investigation reveals a pronounced capability integration gap: standard M-OPD captures only 35.6% of the available headroom relative to a domain-routed oracle ensemble, with concise tasks such as instruction following suffering severe degradation and premature stagnation. Crucially, we show that this failure stems not from gradient conflict, but from a severe misallocation of the token-level optimization budget. This pathology is driven by three orthogonal factors: structural sequence-length disparities across domains, dynamic convergence drift due to non-uniform learning rates, and multi-step reward staleness from asynchronous policy updates. To resolve these imbalances, we introduce Open-MOPD, a principled framework incorporating token-share balancing, gap-aware dynamic budget allocation, and student reward refresh. Together, these mechanisms systematically restore cross-domain balance, elevating headroom recovery from 35.6% to 83.4% in a single deployable student. We fully open-source our end-to-end post-training recipe, training trajectories, and evaluation suites on an academically accessible hardware budget.

## Why it matters (AAIF scan)

Open-MOPD：在 SmolLM3-3B-Base 上用 oracle 路由建立受控的多教师在线蒸馏基准，把能力整合与路由歧义分离。发现标准 M-OPD 仅拿到领域路由 oracle 集成可行余地的 35.6%，病因不是梯度冲突而是 token 级优化预算错配（序列长度失衡、学习率收敛漂移、异步奖励失效）。令牌份额平衡、gap 感知动态预算分配、学生奖励刷新三机制把恢复率提到 83.4%；完整配方、轨迹与评测套件在学术硬件预算上开源。

> Source: https://arxiv.org/abs/2608.19098