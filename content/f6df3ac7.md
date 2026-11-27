# What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench

- **ID**: f6df3ac7
- **原文链接**: https://arxiv.org/abs/2611.33943
- **PDF**: https://arxiv.org/pdf/2611.33943
- **作者**: Haozhe Zhang, Zhen Long
- **日期**: 2026-11-25
- **更新**: 2026-11-25
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-skills, benchmark-audit, skillsbench, evaluation-noise
- **质量评分**: 5/5
- **抓取时间**: 2026-11-27T15:41:08Z

---

## 中文导读

SkillsBench 说人类精选技能平均抬 16.6pp、个别任务为负，随后有工作按单任务增益删技能。本文做源码级审计：评分器依赖、占位技能目录、harness 注入内置技能、每格至多 3 次运行的抽样噪声——负增益不显著、门控策略的提升是选择效应。

## 为什么值得关注

对维护 agent 技能库的人是直接可操作的警示：技能正负增益都可能量的是评分器和噪声；审计脚本开源，可核对自有技能库的逐任务账目。

条目一句话：SkillsBench 的「技能涨点」混着评分器依赖与抽样噪声，按单任务增益删技能之前先看这份审计账目

## 关键信息

- 标题：What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench
- 作者：Haozhe Zhang, Zhen Long
- 原文：https://arxiv.org/abs/2611.33943
- 发布时间：2026-11-25
- 来源分类：cs.AI, cs.CL, cs.SE
- 备注：2 figures, 6 tables. Code, audit ledgers, and reproduction scripts: https://github.com/rrrrr4788/skillsbench-lift-reanalysis
- 关联标签：agent-skills, benchmark-audit, skillsbench, evaluation-noise

## English Abstract

Agent skills are directories of instructions, reference materials, and scripts loaded on demand by coding agents. According to SkillsBench, although human-curated skills can raise the passing rate by about 16.6 percentage points (pp) on average, they have actually reduced the results for some tasks. Later research has started to gate or eliminate skills according to the above per-task gains. We have audited the above benchmark at the source-code level and analysed 7,554 public trials to form 1,421 paired "(configuration, task) cells". Source-code audit identified two controlled-verified cases of grader dependence and one operational definition gap; the average lift on these three tasks was 74.6 pp, and the overall average lift for the full set was 18.7 pp. The audit also found that four tasks contained placeholder skill directories, and a certain execution harness additionally added 48 built-in skills in most runs. No task-level reduction achieved statistical significance in the pooled reanalysis with multiple-testing correction. As there were at most three runs per condition for each cell, the observed negative differences are very susceptible to run-sampling noise, and arithmetically, 58% of the cells could not have shown a decrease. Therefore, the raw numbers of negative cells cannot show that skills cause harm. A gating strategy based on the skill-free score seems to improve by 2-3 pp in the logs; however, even after shuffling condition labels to remove any skill effect, it still achieves an increase of 4-7 pp. On the held-out runs not used for fitting and decision-making, there was no statistically significant improvement. The audit ledger and analysis scripts have been published by us.

## English Summary

SkillsBench reported that human-curated agent skills raise pass rates by about 16.6pp on average while harming some tasks, prompting follow-up work gating skills by per-task lift. A source-code-level audit pooling 7,554 public trials into 1,421 paired (configuration, task) cells finds two controlled-verified cases of grader dependence and one operational-definition gap — those three average 74.6pp lift versus 18.7pp overall — plus four tasks with placeholder skill directories and an execution harness that injected 48 built-in skills in most runs. With at most three runs per cell, 58% of cells arithmetically could not show a decrease, and no task-level harm survives multiple-testing correction. Skill-gating policies keyed on skill-free scores still improve 4-7pp after condition labels are shuffled, and no held-out gain: the metric largely measures grader dependence and selection noise.

## 证据与来源

opencli arxiv paper 2611.33943 -f json（2026-11-27 抓取，摘要全文在档）+ 论文流水线 2026-11-27 要点摘录。
