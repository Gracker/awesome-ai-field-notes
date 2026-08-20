# Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees

- **ID**: c4c02acb
- **原文链接**: https://arxiv.org/abs/2608.17994
- **PDF**: https://arxiv.org/pdf/2608.17994v1
- **作者**: Sher Badshah, Ali Emami, Hassan Sajjad
- **日期**: 2026-08-18
- **更新**: 2026-08-18
- **分类**: cs.CL
- **来源类型**: arxiv
- **标签**: llm-as-judge, evaluation, uncertainty, retrieval, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-20T05:27:37Z

---

## 中文导读

用 LLM 做评判已成为大规模评估模型输出的标准做法，但客观任务的无参考评判存在可靠性隐患：评判模型可能凭参数化知识幻觉作答，或缺少支撑结论的证据论文提出不确定性 guarded 的评判检索或弃权框架：当证据不足时选择检索增强或弃权，而非强行给出结论，并为该流程提供可证明的风险保证

## 为什么值得关注

LLM 评判的可靠性框架：证据不足时选择检索或弃权，并提供可证明的风险保证

Grounded note: the framework calibrates uncertainty thresholds on a held-out set with finite-sample Clopper-Pearson intervals so the false discovery rate among accepted verdicts stays below a user-specified alpha, routing insufficiently confident instances to retrieval-augmented judging. Accepted at the Conference on Language Modelling 2026 (COLM).

## 关键信息

- 论文标题: Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees
- 作者: Sher Badshah, Ali Emami, Hassan Sajjad
- arXiv: https://arxiv.org/abs/2608.17994
- 发布时间: 2026-08-18
- arXiv 分类: cs.CL
- Comment: Accepted at Conference on Language Modelling 2026
- 关联标签: llm-as-judge, evaluation, uncertainty, retrieval, arxiv

## English Abstract

Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the former enables efficient evaluation, the judge may hallucinate or lack sufficient evidence for its verdict. Conversely, tool augmentation can provide additional evidence but introduces extra computational cost and requires an appropriate mechanism to determine when and how that evidence should be used reliably. More importantly, neither approach alone provides formal control over the risk of accepted verdicts or guarantees their reliability at a specified level. We propose a risk-controlled framework that calibrates uncertainty thresholds on a held-out set so that the false discovery rate among accepted verdicts remains below a user-specified level~$α$ with high probability, using finite-sample Clopper--Pearson intervals. When the parametric mode is not sufficiently confident, the instance is routed to a retrieval-augmented mode, where the judge gathers web evidence and re-evaluates the instance under a second calibrated threshold. The finite-sample guarantee carries over to this two-threshold routing without additional assumptions. Across open-domain QA benchmarks and judges of varying scales, the framework maintains the target error rate while achieving substantially higher coverage than single-mode baselines.

## English Summary

Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the former enables efficient evaluation, the judge may hallucinate or lack sufficient evidence for its verdict. Conversely, tool augmentation can provide additional evidence but introduces extra computational cost and requires an appropriate mechanism to determine when and how that evidence should be used reliably....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
