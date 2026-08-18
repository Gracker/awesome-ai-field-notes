# Split the Labor: Separating Evidence Interpretation from Decision Aggregation

- **ID**: fbe0b37f
- **原文链接**: https://arxiv.org/abs/2608.14509
- **PDF**: https://arxiv.org/pdf/2608.14509v1
- **作者**: Zhelun Wu
- **日期**: 2026-08-14
- **更新**: 2026-08-14
- **分类**: models
- **来源类型**: paper
- **标签**: evidence-aggregation, reasoning, llm-systems, calibration, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-18T05:28:55Z

---

## 中文导读

让语言模型从多个来源得出结论的系统通常把来源拼接进同一个提示，这混淆了两种需求不同的操作：解读来源奖励容量与上下文，聚合解读则奖励固定算术跨实例可比性以及允许返回空作者提出四字段证据元组（假设可靠性分桶理由出处）作为两半之间的接口，并揭示聚合失效模式 count-scale drift：对未归一化权重求和后设阈值，等价于后验阈值化，但工作点随咨询来源数量滑动随读者可靠性增大；当来源可靠性不同时，投票规则与后验对实例的排序不同，任何阈值都无法调和校准对数似然比的汇总可同时解决这两个问题；该修正属于算术层面而非架构层面，适用于评分求和的分诊引擎按阳性计数打分的诊断面板与加性多信号检测器等一类规则

## 为什么值得关注

把证据解读与决策聚合分离：四字段证据元组做接口，校准对数似然比修复 count-scale drift

该论文发表于 2026-08-14，作者为 Zhelun Wu，arXiv 分类 cs.AI, cs.CL, cs.LG；以上判断基于论文摘要所述内容。

## 关键信息

- 论文标题： Split the Labor: Separating Evidence Interpretation from Decision Aggregation
- 作者： Zhelun Wu
- arXiv： https://arxiv.org/abs/2608.14509
- 发布时间： 2026-08-14
- arXiv 分类： cs.AI, cs.CL, cs.LG
- 备注： Atlassian. 22 pages, 2 figures
- 关联标签： evidence-aggregation, reasoning, llm-systems, calibration, arxiv

## English Abstract

Systems that ask a language model to reach a conclusion from many sources usually concatenate them into one prompt. This conflates two operations with different requirements. Interpreting a source rewards capacity and context. Combining interpretations rewards fixed arithmetic, comparability across instances, and the option to return nothing. Once separated, the design problem becomes the interface between them. We propose a four-field evidence tuple (hypothesis, reliability bucket, rationale, provenance) and show that fixing it determines both halves. The separation also reveals a failure mode in how such systems combine, which we call count-scale drift. Thresholding a sum of unnormalized weights is exactly posterior thresholding, but at an operating point that slides with the number of sources consulted. The slide grows with reader reliability. When source reliabilities differ, the vote rule and the posterior order instances differently, and no threshold reconciles them. Pooling calibrated log-likelihood ratios addresses both problems. The fix is arithmetic rather than architectural, and applies to a class of rules beyond language models: score-summing triage engines, diagnostic panels scored by counting positives, and additive multi-signal detectors. We then instantiate the principle twice on one longitudinal corpus, once after outcomes resolve and once before. The same partition helps in both, at different granularities: over reading in the first, over learning capacity in the second. There, a small sequence encoder on an easy auxiliary objective plus a tree ensemble carrying the censored survival loss reaches 0.921 AUPRC against 0.805 for a hand-crafted baseline. We separate what transfers from what must be re-estimated per domain, and state five predictions that would falsify the framework, three negative results, and which comparisons remain confounded.

## English Summary

Systems that ask a language model to reach a conclusion from many sources usually concatenate them into one prompt, conflating two operations with different requirements: interpreting a source rewards capacity and context, while combining interpretations rewards fixed arithmetic, comparability across instances, and the option to return nothing. The author proposes a four-field evidence tuple (hypothesis, reliability bucket, rationale, provenance) as the interface between the two halves, and identifies a failure mode called count-scale drift: thresholding a sum of unnormalized weights is exactly posterior thresholding, but at an operating point that slides with the number of sources consulted and grows with reader reliability; when source reliabilities differ, the vote rule and the posterior order instances differently and no threshold reconciles them....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
