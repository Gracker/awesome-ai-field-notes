# TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training

> External-scan entry · 2026-07-09 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.05804
- **Source**: arxiv · Yuhang Zhou, Kai Zheng, Haoling Li, Dengyun Peng, Can Xu, Jingjing Chen
- **Original Date**: 2026-07-07
- **Added**: 2026-07-09
- **Category**: agents
- **Tags**: on-policy-distillation, long-horizon, agent-training, rollout-budget, kl-loss
- **Quality Score**: 4

## 中文摘要

TurnOPD 把 agent on-policy distillation 拆成两个 turn-level 预算控制器：自适应 rollout-depth 预算（基于探针的 turn 统计决定 rollout 长度）和渐进式 turn-normalized loss 预算（把 KL 权重从 token 级渐迁移到 turn 平衡监督）文章指出 vanilla agent OPD 的两个低效：完整 rollout 在尾部 turn 上浪费 wall-clock 但提供弱且噪声的 KL 信号；trajectory-level KL 让损失集中在浅层 token，深层决策 turn 训练不足ALFWorld / WebShop / Multi-Hop Search 上以同 wall-clock 预算取得更优 validation accuracy

## English Abstract

On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising framework for language agent training. However, its application to long-horizon agentic tasks remains insufficiently explored. We identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts often waste wall-clock resources on tail turns that provide weak and noisy KL supervision, and (2) trajectory-level KL objectives concentrate most of the loss on shallow tokens, leaving deeper decision turns under-trained once initial behaviors are aligned. To address these challenges, we propose TurnOPD, a turn-level budgeting strategy for efficient on-policy distillation of long-horizon agents....

## One-liner

TurnOPD 把 agent on-policy distillation 拆成两个 turn-level 预算控制器：自适应 rollout-depth 预算（基于探针的 turn 统计决定 rollout 长度）和渐进式 turn-normalized loss 预算（把...

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
