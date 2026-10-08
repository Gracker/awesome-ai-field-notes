# ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding

- **ID**: c43ada0f
- **原文链接**: https://arxiv.org/abs/2610.08662
- **PDF**: https://arxiv.org/pdf/2610.08662
- **作者**: Hanjun Luo, Xiucheng Zhang, Zhuoning Xu, Zhimu Huang, Yingbin Jin, Xinfeng Li, Hanan Salam
- **日期**: 2026-10-06
- **更新**: 2026-10-06
- **分类**: agents
- **arXiv 分类**: cs.AI, cs.SE
- **来源类型**: paper
- **标签**: coding-agents, benchmark, risk-management, agent-evaluation, safety
- **质量评分**: 4/5
- **抓取时间**: 2026-10-08T15:41:20Z

---

## 中文导读

Coding agent 越来越自主，但『风险处理是否恰当』此前没有统一评测。ParanoiaEval 借软件工程风险管理的 Avoidance-Transfer-Mitigation-Acceptance 框架，构造 200 对证据受控的仓库级任务对——每对只在定义处理方式的那条证据上不同，并配风险处理违规率与证据响应度两个指标，用人工校准的 agent judge 评分。8 个代表性模型的实验显示：即使证据明确，11.2%-58.7% 的运行仍做了不必要的风险处理；任务能力更强不等于风险处理更得当，违规率还明显伤害开发者体验。

## 为什么值得关注

200 对证据受控任务对的构造方式是 agent 评测方法论的好样本，unnecessary defensive work 度量可以套到自家 agent 体检上。

## 关键信息

- 论文标题：ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding
- 作者：Hanjun Luo, Xiucheng Zhang, Zhuoning Xu, Zhimu Huang, Yingbin Jin, Xinfeng Li, Hanan Salam
- arXiv：https://arxiv.org/abs/2610.08662
- 发布时间：2026-10-06
- arXiv 分类：cs.AI, cs.SE
- 关联标签：coding-agents, benchmark, risk-management, agent-evaluation, safety

## English Abstract

As coding agents increasingly undertake real-world work autonomously, judging whether their risk treatments are warranted has become important. Existing work evaluates related agent behaviors from separate perspectives, but lacks a systematic framework for unifying these behaviors. To bridge this gap, we introduce ParanoiaEval, the first benchmark for unified evaluation of risk-treatment capabilities in coding agents. Grounded in the well-established Avoidance-Transfer-Mitigation-Acceptance framework in software engineering risk management, ParanoiaEval operationalizes its 4 fundamental treatments for coding-agent settings and contains 200 evidence-controlled repository-level task pairs, each differing only in treatment-defining evidence. We further introduce dedicated metrics for risk-treatment violations and evidence responsiveness, using a human-calibrated agentic judge for reliable evaluation. Large-scale experiments on 8 representative models and a post-hoc human study reveal that (I) unnecessary risk treatment occurs in 11.2%-58.7% of runs despite explicit evidence, with substantial variation across agent configurations; (II) stronger task capability does not ensure more appropriate risk treatment, while treatment violations substantially harm developers' experience, establishing risk treatment as an independent capability dimension; and (III) agents exhibit systematic patterns consistent with established risk-management findings, suggesting that knowledge from human practice can guide the diagnosis and improvement of this capability.

## English Summary

ParanoiaEval benchmarks unnecessary defensive work in agentic coding via the software-engineering risk-management framework (Avoidance-Transfer-Mitigation-Acceptance): 200 evidence-controlled repository task pairs differing only in the evidence defining risk handling, scored with violation rate and evidence responsiveness using human-calibrated agent judges. Across 8 representative models, 11.2%-58.7% of runs still performed unnecessary risk handling even with clear evidence; stronger task ability does not imply better risk handling, and violations measurably hurt developer experience.

## Obsidian Notes

- 内容由 `opencli arxiv paper 2610.08662 -f json` 拉取 arXiv 元数据与摘要生成（opencli-first 成功）。
- 中文导读与价值判断锚定在论文摘要、作者、日期与分类信息上；未补充摘要之外的实验细节。
