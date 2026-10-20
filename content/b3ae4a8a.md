---
id: b3ae4a8a
title: "DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery"
authors: "Yuxing Chen, Zhisheng Zhang, Cheng Tang, Wei Li, Minghui Zhang, Ziyan Huang, Shaocong Wei, Jiawei Chen, Junru Hu, Hongze Zhu, Jianghan Shen, Min Cen, Xinyuan Zhu, Yaxue Zhao, Jubo Wang, Yuqiang Li, Chun-Mei Feng, Zongyuan Ge, Rui Su, Jie Xu, Yirong Chen, Xi Xu, Ming Hu"
original_date: 2026-10-16
url: https://arxiv.org/abs/2610.23791
source: arxiv
tags: [agent-harness drug-discovery skill-induction scientific-ai composable-execution]
---

# DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery

> Source: [https://arxiv.org/abs/2610.23791](https://arxiv.org/abs/2610.23791) · platform: arxiv · authors: Yuxing Chen, Zhisheng Zhang, Cheng Tang, Wei Li, Minghui Zhang, Ziyan Huang, Shaocong Wei, Jiawei Chen, Junru Hu, Hongze Zhu, Jianghan Shen, Min Cen, Xinyuan Zhu, Yaxue Zhao, Jubo Wang, Yuqiang Li, Chun-Mei Feng, Zongyuan Ge, Rui Su, Jie Xu, Yirong Chen, Xi Xu, Ming Hu · date: 2026-10-16

## TL;DR（中文摘要）

药物发现要求智能体组合科学操作并适应不断变化的证据与约束DrugHarness 是一个可演化 agent harness：环境集成 80 余种科学操作生物医学资源与任务代码，并保留候选物-结果-产物之间的关联；从执行轨迹与结果反馈中归纳带适用条件推荐动作和支持证据的 action hypotheses，实现条件化技能归纳是把 harness 设计与技能积累放到垂直科学领域的具体案例

## Summary (English)

Computational drug discovery requires agents to compose scientific operations and adapt to changing evidence and constraints. Here we introduce DrugHarness, an evolvable agent harness coupling composable scientific execution with conditional skill induction. Its environment integrates over 80 scientific operations, biomedical resources and task-specific code, preserving associations among candidates, results and artifacts. From execution trajectories and outcome feedback, DrugHarness induces action hypotheses with observable applicability conditions, recommended actions and supporting evidence. An independent review agent evaluates candidate skills derived from these hypotheses through source verification and, when needed, targeted execution trials. Admitted skills guide subsequent tasks and are revised through feedback. Evaluation on MolBench and SMDD-Bench demonstrates capabilities in molecular screening, optimization and constrained design. Without evolution, DrugHarness exceeds reported MolClaw-CC results by 10.8 percentage points in affinity-comparison accuracy and 55% in mean top-three active hits on MolBench. Retrospective evaluation on skill-development tasks shows that evolution increases Qwen's affinity-comparison accuracy from 62.2% to 81.1% and optimization success from 79.5% to 87.2%. In a prospective HPK1 study, DrugHarness achieves a more favorable median docking score than Biomni among system-specific candidates. A synthesized compound achieves a cellular IC50 of 14.19 nM, a 2.64-fold potency improvement over the best input reference, with activity competitive with two selected compounds designed by experienced medicinal chemists. These results support conditional skill evolution for scientific agents and demonstrate a workflow connecting computational drug design with experimental validation.

## 入库依据（OpenCLI 直接抓取 arXiv 元数据）

opencli arxiv paper 2610.23791 -f json 直出（list 形态已解包），metadata 字段：title/authors/published/primary_category/categories 与 entry 入库字段对齐，无二次推断。 primary_category: cs.AI; categories: cs.AI.
