# Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation

- **ID**: 6df7d1df
- **原文链接**: https://arxiv.org/abs/2610.28586
- **PDF**: https://arxiv.org/pdf/2610.28586v1
- **作者**: Shu Zhao, Tan Yu
- **日期**: 2026-10-20
- **更新**: 2026-10-20
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-training, distillation, on-policy, reward-free
- **质量评分**: 4/5
- **抓取时间**: 2026-10-22T04:21:44Z

---

## 中文导读

Agentic on-policy distillation 让学生在自己轨迹上训练教师逐 token 打分主流解释是 compounding error，本文证明不完整：在学生最偏离教师的状态上，教师亲自接管仍能完成任务，而按教师 token 分数训练的学生却总耗尽回合根源是 next-token 打分的短视教师看不到回合结局，容忍了 outcome RL 会以零奖励惩罚的安全拖延动作；作者称之为 rollout-scorer gapR2S 先修打分器再蒸馏：从未训练学生的轨迹挖高分歧状态从这些状态跑教师接管以共识或 LLM judge 等 reward-free 检查筛选状态再微调教师使其在没有接管上下文时也对每个 assistant token 给出接管知情的分数；修复后的教师冻结为唯一打分器，修复与训练全程不需任务奖励3 环境2 教师4 学生共 12 个组合全胜三种 SOTA agentic-OPD 方法，较各自最优平均 +12.8 成功率项目页：tree-shu-zhao.github.io/r2s

## 为什么值得关注

Agentic 蒸馏的病根是打分短视而非误差复合：R2S 先用教师接管修复打分器再蒸馏，3 环境2 教师4 学生 12 格全胜，平均 +12.8 成功率

论文于 2026-10-20 提交 arXiv（cs.CL, cs.AI），摘要与元数据均来自 arXiv 官方页面。

## 关键信息

- 论文标题：Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation
- 作者：Shu Zhao, Tan Yu
- arXiv：https://arxiv.org/abs/2610.28586
- 发布时间：2026-10-20
- arXiv 分类：cs.CL, cs.AI
- 关联标签：agent-training, distillation, on-policy, reward-free

## English Abstract

Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From the states where the student departs most from the teacher, the teacher's own takeovers still finish the task, yet the student trained on its token scores keeps running out of turns. We attribute this to the myopia of next-token scoring. The teacher rates each token without seeing where the episode ends, so its scores let through the safe, delaying moves that outcome-based RL would punish with zero reward, a penalty agentic OPD lacks. We call this difference between what the teacher does and what it scores the rollout-scorer gap. We propose Rollout-to-Scorer Distillation (R2S), which repairs the scorer before distillation by mining high-disagreement states from the untrained student, running teacher takeovers from them, keeping the states where enough takeovers pass a reward-free check such as consensus or an LLM judge, and fine-tuning the teacher to give its takeover-informed scores on every assistant token from the divergence turn onward, without the takeover in context. The repaired teacher is frozen as the sole scorer for standard OPD, requiring no task reward during repair or training. Across three environments, two teachers and four students, R2S outperforms three state-of-the-art agentic-OPD methods in all twelve teacher-student-environment cells, by 12.8 success points on average over the best of them in each cell. Project page: https://tree-shu-zhao.github.io/r2s/.

## English Summary

Agentic on-policy distillation trains a student on its own trajectories with a teacher scoring every token. The authors show the standard compounding-error explanation is incomplete: from the states where the student departs most, teacher takeovers still finish the task, yet students trained on the teacher's token scores run out of turns. The cause is next-token scoring myopia: the teacher never sees where the episode ends, letting through safe delaying moves that outcome RL would punish with zero reward (the rollout-scorer gap). R2S repairs the scorer before distillation: mine high-disagreement states from the untrained student, run teacher takeovers, keep states passing reward-free checks (consensus or LLM judge), and fine-tune the teacher to give takeover-informed scores on every assistant token without the takeover in context....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
