# SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent

> Source: https://arxiv.org/abs/2608.07449
> Author: Mingxuan Zheng, Yujin Zhou, Chuxue Cao, et al.
> Date: 2026-08-07
> Category: agents
> Type: paper
> Quality: 4/5
> Tags: agent-skills, self-evolving, textual-gradient, skill-refinement, arxiv

## English Summary

LLM agents increasingly adapt to recurring tasks by accumulating procedural knowledge in skillslightweight, reusable textual artifacts loaded into context without weight updates. SkillProx introduces a proximal-gradient-inspired forward-backward framework: the forward stage re-executes diagnosis-driven edits on the same task batch, rolls back regressions, and feeds outcomes into subsequent diagnoses; the backward stage decomposes skills into auditable knowledge units, estimates contributions via leave-one-out utility audit, and applies validation-gated consolidation, demotion, or removal. Experiments on in-distribution and out-of-distribution benchmarks across multiple backbone LLMs show SkillProx improves average accuracy by 3.0 percentage points over the strongest gradient-based baseline.

## 中文概要

SkillProx 提出了一种受近端梯度启发的前向-后向框架，用于自进化 LLM 代理的技能制品（skills）前向阶段重复执行诊断驱动的编辑并回滚退化，后向阶段将技能分解为可审计的知识单元，通过 leave-one-out 效用审计估计其贡献，并执行验证门控的合并降级或删除在多个后端 LLM 的分布内外基准上，平均准确率较最强梯度基线提升 3.0 个百分点

---

*Added via external-scan on 2026-08-11*
