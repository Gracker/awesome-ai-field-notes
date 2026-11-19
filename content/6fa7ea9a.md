# Identifying and Repairing Energy Smells with Agent Skills

- Source: https://arxiv.org/abs/2611.23203
- Author: unknown
- Published: 2026-11-17
- Intake: 2026-11-19 evening (daily-intake-evening, openclaw)
- Evidence: /Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/OpenClaw定时任务/论文流水线/2026-11-19-论文流水线.md

## 中文摘要
能耗坏味道修复被做成编码 agent 的一个 skill：DR. GREENS 给出 12 类能耗坏味道、65 个根因的分类法，沉淀 230 个实测案例的修复指引，并配静态分析器与独立验证器，每次修复都要确认行为不变、能耗确实下降。3 个开源仓库、18 个会话、2 个模型、3 种 skill 配置下的 258 个修复里，68.6% 实测省电，中位节省 24.9%；去掉分类法的对照 skill 在三个仓库、两个模型上找出的可验证节能修复都更少。能耗优化从专家事后 profiling 前移到写代码当场修，独立验证器是省电数字可信的前提。

## English Summary
DR. GREENS packages energy-smell repair as an agent skill for coding agents: a taxonomy of 12 energy-smell categories and 65 root causes grounded in 230 measured cases, plus a static analyzer and an independent verifier so each attempted repair must confirm behavior preservation and real energy savings. Across 18 sessions on three open-source repositories, two models and three skill configurations, 258 measured repairs landed with 68.6% measurably saving power and a median 24.9% reduction; an ablated skill without the taxonomy found fewer verifiable energy-saving fixes on all three repos and both models.

## Abstract (arXiv)
Energy smells are inefficient implementations that waste energy. Once code reaches production, these smells become costlier and riskier to fix, so energy efficiency checks should shift left, i.e., move earlier in the development lifecycle, to where code is written. Existing energy smell tools rely on fixed static rules and do not measure energy savings, whereas LLM-based optimizers mostly target execution time and rarely ground their changes in concrete smell definitions. To address both limitations, we present DR. GREENS, an agent skill that detects and repairs energy smells in Python code within the developer's coding environment. The skill grounds the coding agent in our taxonomy of 12 energy smells and 65 root causes, augmented with repair guidance drawn from 230 measured cases. The skill also encapsulates a static analyzer and an independent verifier to confirm behavior preservation and energy saving for each attempted repair. We evaluated DR. GREENS in 18 sessions on three open-source repositories, with two models and three skill configurations. Of the 258 measured repairs, 68.6% saved energy, with a median saving of 24.9%. Compared with a baseline skill that lacks the taxonomy, the full skill found more energy smells with verified savings in all three repositories with both models. DR. GREENS helps developers detect energy hotspots and fix them reliably without altering program behavior, which makes energy-efficient development more feasible.
