---
id: "bcc5ec91"
title: "When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals"
url: "https://arxiv.org/abs/2607.08065"
authors: "Kaihua Ding"
submitted: "[Submitted on 9 Jul 2026]"
subject: "Artificial Intelligence (cs.AI)"
source_type: "paper"
category: "infra"
quality_score: 4
tags: [llm-as-judge, self-consistency, evaluator-reliability, audit, confidence-calibration]
added_date: "2026-07-11"
---

# When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals

**Source:** [https://arxiv.org/abs/2607.08065](https://arxiv.org/abs/2607.08065)
**Authors:** Kaihua Ding
**Submitted:** [Submitted on 9 Jul 2026]
**Subject:** Artificial Intelligence (cs.AI)

## 中文摘要

针对企业评测管线中越来越常用的 LLM-as-judge 与 judge ensemble，质疑其核心假设——"判官之间一致 = 答案正确"。论文通过受控实验证明，模型自一致性 / 跨模型一致性信号与答案正确性的相关性远弱于业界默认，且容易被格式相似性、风格偏好、prompt 模板诱导偏差系统性放大。提出若干审计维度（判官多样性、判官解耦、置信度分解）作为新一代 LLM 评测体系的必要补丁。

## English Abstract

LLM-as-judge (Zheng et al., 2023) is increasingly the default for evaluating AI systems in enterprise pipelines, often scaled to ensembles (Verga et al., 2024) or "mixture-of-experts" (Shazeer et al., 2017) panels of judges. These systems share a key assumption: that consistency -- agreement among judges, or among a model's own samples -- indicates correctness. We show this assumption is unreliable. Agreement is not accuracy: a model can agree with itself, and different models can agree with each other, out of shared bias, a memorized heuristic, or an option-position prior rather than truth. We ask when agreement is nonetheless a usable proxy, in a large-scale cross-runner study: 53 runners drew K=50 samples for assigned overlapping cases across comparisons of model tier, prompting, and scale on GPQA Diamond and AIME -- 265,000 samples. Using majority-correctness as the deployment label and a hierarchical runner-clustered bootstrap, agreement is a positive but weak predictor (rho 0.20-0.59, all positive under item-clustered resampling) whose usefulness is regime-dependent: best for unsaturated mid-tier models and for allocating compute, and worst -- over-confident yet no more accurate -- for the most consistent frontier model (agreement >=0.8 on 77% of GPQA case-result entries, 48% of those wrong). An exploratory cross-family check on three Claude tiers shows the same frontier over-confidence, with confident errors recurring across providers above a marginal-preserving null. 
