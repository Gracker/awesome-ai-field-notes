# SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents

- **ID**: 6b4d1edc
- **原文链接**: https://arxiv.org/abs/2611.21541
- **PDF**: https://arxiv.org/pdf/2611.21541
- **作者**: Brian T. Weston, Alondra Torres Contreras, Aldair E. Gongora
- **日期**: 2026-11-16
- **更新**: 2026-11-16
- **分类**: agents
- **来源类型**: paper
- **标签**: arxiv, benchmark, agents, calibration, scientific-research
- **质量评分**: 4/5
- **抓取时间**: 2026-11-18T04:22:21Z

---

## 中文导读

SciResearch-Eval 用标准实验室问题（加热材料拟合热传导模拟器）考 agent 的科研判断：自己设计实验用可能欠分辨或物理错误的模拟器每个属性给出对齐真值的 95% 区间held-out 93 任务9 模型2,511 回合：程序性陷阱都能处理，但模拟器缺物理时多数模型报错值还自称 95% 置信，区间命中率只有 20-62%（GPT-6 Astra 94%Claude Fable 5.2 99%）；Claude 5.5 默认档很少诊断出缺物理（Opus 35% vs Astra 66%），Astra 和 Fable 会设计温和加热这类让错误模拟器恰好够用的实验

## 为什么值得关注

SciResearch-Eval 用标准实验室问题（加热材料拟合热传导模拟器）考 agent 的科研判断：自己设计实验用可能欠分辨或物理错误的模拟器每个属性给出对齐真值的 95% 区间held-out 93 任务9 模型2,511 回合：程序性陷阱都能处理...

考的不是答题而是用可能有错的仪器得出校准结论这一科研核心动作：缺物理时多数模型区间命中率只有 20-62%，校准好的模型有 94-99%，且加宽区间无效、说明策略才有效——agent 评测正在从任务完成率转向判断质量。

## 关键信息

- 论文标题：SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents
- 作者：Brian T. Weston, Alondra Torres Contreras, Aldair E. Gongora
- arXiv：https://arxiv.org/abs/2611.21541
- 发布时间：2026-11-16
- arXiv 分类：Artificial Intelligence (cs.AI), Machine Learning (cs.LG), Computational Physics (physics.comp-ph)
- 关联标签：arxiv, benchmark, agents, calibration, scientific-research

## English Abstract

We introduce SciResearch-Eval, an interactive benchmark of scientific judgment built on a standard laboratory problem: measuring a material's thermal properties by heating it and fitting a heat-conduction simulator. An agent designs its own experiments, uses a supplied simulator that may be under-resolved or physically wrong, and reports each property with a 95% interval. To our knowledge it is the first benchmark to combine agent-designed experiments, a deliberately flawed simulator, and proper scoring of calibrated intervals against exact ground truth. On a held-out split (93 tasks, 9 models, 2,511 episodes), models handle procedural traps. When the simulator is missing physics, most report wrong values while stating they are 95% sure: their ranges contain the truth in 20-62% of cases, against 94% for GPT-6 Astra and 99% for Claude Fable 5.2. At default effort the failing Claude 5.5 models rarely diagnose the missing physics (Opus in 35% of episodes, against 66% for Astra), and even when they do, their ranges often miss; Astra and Fable design experiments in which the flawed simulator is accurate, such as gentle heating, which keeps Astra calibrated even when it does not name the cause. Asking for wider intervals does not help; stating the strategy improves interval scores 1.6-2.5-fold, replicated on a pre-registered fresh split, but coverage barely moves. A pre-registered effort ablation shows that the correction is latent in the Claude 5.5 models: at maximum effort Opus improves more than tenfold and is no longer detectably behind Astra at default, but only with 13-31 times more reasoning; older and open-weight models gain nothing. Fable 5.2 is the most accurate model at default effort (interval score 1.9 times better than Astra's) but writes 6 times as many tokens, and at Astra's token count it falls short. We release the environment, graders and harness.

## English Summary

SciResearch-Eval is an interactive benchmark of scientific judgment built on heating a material and fitting a heat-conduction simulator. The agent designs its own experiments, works with a simulator that may be under-resolved or physically wrong, and must report each property with a 95% interval against exact ground truth - the first benchmark combining agent-designed experiments, a flawed simulator, and calibrated-interval scoring. Across 93 held-out tasks, 9 models, 2,511 episodes, models handle procedural traps, but when the simulator is missing physics most report wrong values at claimed 95% confidence: intervals contain the truth in only 20-62% of cases, against 94% for GPT-6 Astra and 99% for Claude Fable 5.2. Failing Claude 5.5 models rarely diagnose the missing physics (Opus 35% vs Astra 66%); Astra and Fable design experiments where the flawed simulator happens to be accurate.

## Obsidian Notes

- 内容获取路径：`opencli arxiv paper 2611.21541 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 现代站点生成器按 `content/6b4d1edc.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
