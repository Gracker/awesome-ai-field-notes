# Weak-to-Strong Generalization via Direct On-Policy Distillation

> External-scan entry · 2026-07-08 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.05394
- **Source**: arxiv · Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang
- **Original Date**: 2026-07-07
- **Added**: 2026-07-08
- **Category**: learning
- **Tags**: rlvr, distillation, weak-to-strong, post-training
- **Quality Score**: 4

## 中文摘要

本文把 RLVR 当作一个跨模型的隐式奖励信号来迁移：先在算力廉价的小模型上跑 RL，再把 RL 前后策略分布对数比作为密集奖励蒸馏到更大的学生模型上作者提出 Direct-OPD 在学生 on-policy 状态上施加教师"RL 引起的策略位移"，避免显式奖励建模和稀疏目标端 RL；8 张 A100 训练 4 小时将 Qwen3-1.7B 在 AIME 2024 从 48.3% 提升到 62.4%，并支持多步策略位移的串接

## English Abstract

Reinforcement learning with verifiable rewards (RLVR) is expensive to repeat for each new strong model because the target must generate many rollouts. We study a weak-to-strong alternative: run RL on a cheaper small model and reuse the RL-induced policy shift as an implicit reward for the stronger student. We propose Direct On-Policy Distillation (Direct-OPD), which transfers the teacher RL-induced policy shift rather than its final policy. Direct-OPD compares the post-RL teacher with its own pre-RL reference and treats their log-ratio as a dense implicit reward on the student's on-policy states. Direct-OPD boosts Qwen3-1.7B from 48.3% to 62.4% on AIME 2024 in 4 hours on 8 A100 GPUs and supports sequential composition of multiple policy shifts, showing that RL outcomes can be reused across model scales as implicit reward signals.

## One-liner

本文把 RLVR 当作一个跨模型的隐式奖励信号来迁移：先在算力廉价的小模型上跑 RL，再把 RL 前后策略分布对数比作为密集奖励蒸馏到更大的学生模型上作者提出 Direct-OPD 在学生 on-policy 状态上施加教师"RL 引起的策略位移"...

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
