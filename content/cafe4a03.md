# SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models

- **ID**: cafe4a03
- **原文链接**: https://arxiv.org/abs/2611.15777
- **PDF**: https://arxiv.org/pdf/2611.15777
- **作者：** Lichen Li, Ziping Dong, Sicheng Feng, Qi Li, Xinchao Wang
- **发布时间**: 2026-11-11
- **更新**: 2026-11-11
- **分类**: models
- **来源类型**: paper
- **标签**: arxiv, benchmark, decision-models, system-one, evaluation
- **质量评分**: 4/5
- **抓取时间**: 2026-11-16T23:47:32+08:00

---

## 中文导读

决策/System One 模型追求不开长推理链的快速通用决策，但总分说明不了能力谱与决策可靠性。SO-Arena 覆盖 11 个域、五个能力族：证据接地的评测（可靠来源加参考标注人工核对）、按域细化难度标准、沙箱内迭代执行动作的真实交互评测，并设推理密集任务做 System 1-2 对照。可靠性测两件事：受控选项集变化下的决策稳定性，以及无有效选项时的弃答识别。21 个模型的评测显示 scaling 与额外推理的收益随域差异很大，总分最高不等于决策可靠——表现最好的模型可靠性只排第七。HF 日榜 137 票居首。

## 为什么值得关注

决策/System One 模型追求不开长推理链的快速通用决策，但总分说明不了能力谱与决策可靠性。SO-Arena 覆盖 11 个域、五个能力族：证据接地的评测（可靠来源加参考标注人工核对）、按域细化难度标准、沙箱内迭代执行动作的真实交互评测，并设推理密集任务做 System 1-2 对照。可靠性测两件事：受控选项集变化下的决策稳定性，以及无有效选项时的弃答识别。21 个模型的评测显示 scaling 与额外推理的收益随域差异很大，总分最高不等于决策可靠——表现最好的模型可靠性只排第七。HF 日榜 137 票居首。

System One models promise fast decision-making without lengthy token generation, but aggregate benchmark scores say little about the breadth of capabilities or the reliability of decisions. SO-Arena characterizes both across 11 domains and five capability families: evidence-grounded evaluation with manually verified reference labels, domain-specific difficulty criteria, and interactive sandbox evaluation where models iteratively execute actions; reasoning-intensive tasks enable System One-Two comparison. Decision reliability is measured as stability under controlled option-set changes plus missing-answer recognition when no valid option exists. Across 21 models, the benefits of scaling and extra reasoning vary substantially by domain, and strong overall performance does not imply reliable decisions: the best-performing model ranks only seventh in reliability.

## 关键信息

- 标题：SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models
- 作者：Lichen Li, Ziping Dong, Sicheng Feng, Qi Li, Xinchao Wang
- 来源：https://arxiv.org/abs/2611.15777
- 发布时间：2026-11-11
- 标签：arxiv, benchmark, decision-models, system-one, evaluation

## 英文摘要

System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the breadth of model capabilities and the reliability of their decisions. We introduce SO-Arena, a benchmark characterizing the capability spectrum and decision reliability of System One models across 11 domains and five capability families. For the capability spectrum, SO-Arena offers evidence-grounded evaluation through reliable sources and manual verification of reference labels against model-visible inputs; fine-grained capability assessment through domain-specific difficulty criteria; and realistic interactive evaluation, where models iteratively execute actions in sandboxes. Reasoning-intensive tasks further enable system one-two comparison. Beyond accuracy, SO-Arena assesses decision reliability through two complementary measures: decision stability under controlled option-set changes and missing-answer recognition when no valid option is available. Evaluations across 21 models reveal that the benefits of scaling and additional reasoning vary substantially across domains. More importantly, strong overall performance does not necessarily imply reliable decision-making: the best-performing System One model ranks only seventh in reliability. Together, these findings highlight the need to characterize capability spectrum and decision reliability as complementary dimensions, providing a systematic view of the strengths and limitations of System One models.

## English Summary

System One models promise fast decision-making without lengthy token generation, but aggregate benchmark scores say little about the breadth of capabilities or the reliability of decisions. SO-Arena characterizes both across 11 domains and five capability families: evidence-grounded evaluation with manually verified reference labels, domain-specific difficulty criteria, and interactive sandbox evaluation where models iteratively execute actions; reasoning-intensive tasks enable System One-Two comparison. Decision reliability is measured as stability under controlled option-set changes plus missing-answer recognition when no valid option exists. Across 21 models, the benefits of scaling and extra reasoning vary substantially by domain, and strong overall performance does not imply reliable decisions: the best-performing model ranks only seventh in reliability.

## Obsidian Notes

- 证据来源：Hermes 定时任务/AI-前沿一手源/2026-11-16-AI前沿一手源_周末静默-WorldModel-AA新评.md
- 本页为当日 intake 内容页：事实与数字锚定在上列证据文件与原文链接，未添加证据之外的细节。
