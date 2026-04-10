# 模型架构

Model Architecture — 1 条活跃资源

### [你不知道的大模型训练：原理、路径与新实践](https://x.com/HiTw93/status/2040047268221608281) 
by @Tw93 (2026-04-05) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**2026 年最系统的大模型训练全链路中文长文，从预训练到 Agent 训练一网打尽。**

Tw93 继 Claude Code 和 Agent 深度分析后的第三篇长文，系统梳理大模型训练全链路。核心判断：2026 年拉开差距的不再是预训练本身，而是后训练、评测、奖励、Agent 训练、蒸馏。详细拆解了预训练（数据配方、过训练、tokenizer 设计）、后训练多阶段流水线（冷启动 SFT → GRPO 强化学习 → 拒绝采样微调 → 对齐 RL）、评测-Grader-Reward 反馈回路、推理模型（o1/DeepSeek-R1）、Agent 训练（Kimi K2.5 PARL、Cursor Composer 2、Chroma Context-1）、Meta-Harness（只改 harness code 就能拉出 6x 性能差距）。含大量配图和 14 篇参考文献。
 `大模型训练` `预训练` `后训练` `RLHF` `蒸馏` `Agent训练` `GRPO`

---