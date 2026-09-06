# Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR

> Original: https://arxiv.org/abs/2609.04108
> Source platform: arxiv
> Author: Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye
> Original date: 2026-09-03

## summary_zh

Boyan Li 等 9 月 3 日 arXiv (cs.CL) 投稿RLVR 与 On-Policy Distillation (OPD) 是当下 post-training 推理模型的两条主线，过去的工作把 OPD 的 token-level dense 信号和 RL 的 sparse reward 一步内加权加或 teacher-modulated rescale 混合本文给出一个干净的反例：先 OPD 后 RL 两阶段，跨逻辑/数学推理 benchmark 全面优于纯 OPD纯 RLVR 与所有 joint baseline；并从 pass@klearning dynamics参数更新三个角度给出统一解释：OPD 扩 teacher-supported solution 的覆盖，RL 在覆盖里锐化，一步同时优化会互相干扰判定切到 RL 的实操信号是 OPD validation score，且 OPD 比 SFT 是更好的 RL cold start

## summary_en

Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs. Prior work uses OPD's dense token-level supervision to complement the sparse RL reward, fusing the two signals within a single step: either as a \emph{weighted-additive combination} or a \emph{teacher-modulated rescaling} of the RL advantage. In this paper, we show that a simple two-stage scheme, OPD-then-RL, consistently outperforms pure OPD, pure RLVR, and all such joint baselines across logic and math reasoning benchmarks. Beyond the empirical results, we further provide a systematic understanding of this through pass@$k$ behavior, learning dynamics, and parameter updates, yielding a consistent explanation: OPD expands the student's coverage of teacher-supported solutions and RL sharpens within that support, while jointly optimiz

## one_liner

把"OPD + RL 该不该一起做"的工程争论用一组统一实验关掉：SFT cold start OPD cold start RL 应成 Agent RL 训练默认 pipeline
