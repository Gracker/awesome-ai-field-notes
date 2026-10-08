# VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning

- **ID**: e32fbfab
- **原文链接**: https://arxiv.org/abs/2610.08761
- **PDF**: https://arxiv.org/pdf/2610.08761
- **作者**: Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, Thomas Tian, Zheng Lian, Yan Wang, Jiaqi Ma, Boris Ivanovic, Marco Pavone, Wenhao Ding
- **日期**: 2026-10-06
- **更新**: 2026-10-06
- **分类**: agents
- **来源类型**: paper
- **标签**: verification, self-improvement, embodied-agents, rl, reward-models
- **质量评分**: 4/5
- **抓取时间**: 2026-10-08T12:22:39Z

---

## 中文导读

自我改进的策略会不断暴露新失败模式，固定 judge 同时卡住优化反馈与新训练数据发现VeriFine 让 policy课程judge 三者共同进化：Policy Improvement Loop 用 rubric judge 诊断重复失败并构建自适应课程；进展停滞时 Judge Improvement Loop 只在信息量大的失败案例上请求人类指导，通过 coactive calibration 让人机分歧向客观物理推理 rubric 收敛在驾驶与机器人导航任务上，policy 与 judge 在 RL/SFT 两种训练下均持续改进

## 为什么值得关注

自我改进系统的瓶颈正从『会做事』移到『会验证』：固定 judge 同时卡住优化反馈与新训练数据发现。VeriFine 让 policy、课程、judge 三方共同进化，进展停滞时只在信息量大的失败案例上请求人类指导，通过 coactive calibration 让人机分歧向客观物理推理 rubric 收敛；在驾驶与机器人导航任务上展示了 RL 与 SFT 两种训练下 policy 与 judge 的持续改进。

## 关键信息

- 论文标题：VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning
- 作者：Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, Thomas Tian, Zheng Lian, Yan Wang, Jiaqi Ma, Boris Ivanovic, Marco Pavone, Wenhao Ding
- arXiv：https://arxiv.org/abs/2610.08761
- 发布时间：2026-10-06
- arXiv 分类：cs.AI, cs.RO
- 关联标签：verification, self-improvement, embodied-agents, rl, reward-models

## English Abstract

Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales verification through the co-evolution of the policy, training curriculum, and judge. The Policy Improvement Loop uses a rubric judge to diagnose recurring failures, construct an adaptive curriculum, and optimize the policy. When progress plateaus and verification becomes a bottleneck, the Judge Improvement Loop selectively queries human guidance on informative failure cases and refines the judge through coactive calibration, in which humans and agents resolve disagreements and converge toward the objective rubric of physical reasoning. The revised judge then guides the next stage of data selection and policy optimization. Experiments on driving and robot navigation tasks demonstrate continuous self-improvement in both policy and judge capability across reinforcement and supervised fine-tuning. These results show how scaling verification supports continuous self-improvement as policy failure patterns evolve.

## English Summary

Self-improving policies keep exposing new failure patterns, and fixed judges bottleneck both optimization feedback and training-data discovery. VeriFine scales verification by co-evolving policy, curriculum, and judge: a Policy Improvement Loop uses a rubric judge to diagnose recurring failures and build an adaptive curriculum; when progress plateaus, a Judge Improvement Loop queries humans only on informative failures and refines the judge via coactive calibration, converging human-agent disagreements toward an objective physical-reasoning rubric. On driving and robot navigation, both policy and judge keep improving across RL and SFT.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
