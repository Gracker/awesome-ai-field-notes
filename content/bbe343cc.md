# ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills

- **ID**: bbe343cc
- **原文链接**: https://arxiv.org/abs/2610.12403
- **PDF**: https://arxiv.org/pdf/2610.12403v1
- **作者**: Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- **日期**: 2026-10-08
- **更新**: 2026-10-08
- **分类**: agents
- **来源类型**: paper
- **标签**: vlm-agents, skill-library, visual-native, reward-shaping, closed-loop
- **质量评分**: 4/5
- **抓取时间**: 2026-10-11T12:21:43Z

---

## 中文导读

技能增强 agent 通常把成功轨迹蒸馏成可复用策略来提升样本效率，但多数做法以文本为中心，把空间布局和动作-状态对应线性化成语言，丢掉关键几何结构。ViSkill 是一个视觉原生技能学习框架：把成功交互编码成 VLM agent 可直接访问的复合视觉技能卡，检索到的技能同时引导推理和奖励塑形，成功轨迹再蒸馏回技能库，形成技能积累与策略提升互相强化的闭环；可选的冷启动机制进一步加速早期学习。在 Sokoban、FrozenLake、PrimitiveSkill 上，ViSkill 总成功率 0.89，冷启动初始化后升到 0.91，超过所有受测专有与开源基线，且比标准 PPO 收敛更快。代码开源于 github.com/ZJU-REAL/ViSkill。

## 为什么值得关注

视觉原生技能卡：ViSkill 让 VLM agent 技能库与策略共同进化。

监控与技能库是 agent 系统走向长期自主运行的两块基础件：前者决定出问题时多快被发现（OnTrack 把判定压到每步约一毫秒，用历史成功轨迹做参照），后者决定 agent 能不能把成功经验变成可复用资产（ViSkill 把技能留在视觉模态里，避免文本化丢几何结构）。两篇都给出了可复现的量化证据。

## 关键信息

- 论文标题：ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills
- 作者：Hongxing Li, Dingming Li, Yixin Li, Yong Du, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- arXiv：https://arxiv.org/abs/2610.12403
- 发布时间：2026-10-08
- arXiv 分类：cs.CV, cs.CL
- 关联标签：vlm-agents, skill-library, visual-native, reward-shaping, closed-loop

## English Abstract

Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their mutual improvement underexplored. We propose ViSkill, a visual-native skill learning framework that encodes successful interactions as composite visual skill cards directly accessible to VLM agents. Retrieved skills guide both inference and reward shaping, while successful trajectories are distilled back into the library, forming a closed feedback loop in which skill accumulation and policy improvement reinforce each other. An optional cold-start mechanism further accelerates early-stage learning. Evaluated on Sokoban, FrozenLake, and PrimitiveSkill, ViSkill achieves an overall success rate of 0.89, rising to 0.91 with cold-start initialization, outperforming all evaluated proprietary and open-source baselines while converging faster than standard PPO. Our code is available at https://github.com/ZJU-REAL/ViSkill.

## English Summary

Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their mutual improvement underexplored. We propose ViSkill, a visual-native skill learning framework that encodes successful interactions as composite visual skill cards directly accessible to VLM agents. Retrieved skills guide both inference and reward shaping, while successful trajectories are distilled back into the library, forming a closed feedback loop in which skill accumulation and policy improvement reinforce each other. An optional cold-start mechanism further accelerates early-stage learning. Evaluated on Sokoban, FrozenLake, and PrimitiveSkill, ViSkill achieves an overall success rate of 0.89, rising to 0.91 with cold-start initialization, outperforming all evaluated proprietary and open-source baselines while converging faster than standard PPO. Our code is available at https://github.com/ZJU-REAL/ViSkill.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
