# AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

- **ID**: 9ccbb6f5
- **原文链接**: https://arxiv.org/abs/2608.12307
- **PDF**: https://arxiv.org/pdf/2608.12307v1
- **作者**: Cheng Qian, Wenting Zhao, Liangwei Yang, Heng Wang, Jielin Qiu, Heng Ji, Silvio Savarese, Huan Wang, Shelby Heinecke
- **日期**: 2026-08-12
- **更新**: 2026-08-12
- **分类**: agents
- **来源类型**: paper
- **标签**: strong-to-weak, harness, distillation, test-time, agent-design, cs.lg, cs.lg-cs.ai-cs.cl
- **质量评分**: 4/5
- **抓取时间**: 2026-08-14T04:19:48Z

---

## 中文导读

论文提出test-time strong-to-weak capability transfer：轻量级 builder 模型为弱目标模型设计推理时 harness，不更新权重在四个 ToM 基准上将目标模型平均分数从 0.49 拉到 0.91，收益来自把不稳定推理述出到确定性代码 + 基准路由 + 严格答案格式纠查，而不是纯让模型拍脑裘多 sample推论：harness 设计是训练时蒸馏以外的补充路径

## 为什么值得关注

训练时蒸馏之外的一条路：inference-time harness 设计可以让弱模型接近强模型的结构性能力

## 关键信息

- 论文标题：AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses
- 作者：Cheng Qian, Wenting Zhao, Liangwei Yang, Heng Wang, Jielin Qiu, Heng Ji, Silvio Savarese, Huan Wang, Shelby Heinecke
- arXiv：https://arxiv.org/abs/2608.12307
- 发布时间：2026-08-12
- arXiv 分类：cs.LG, cs.AI, cs.CL
- 关联标签：strong-to-weak, harness, distillation, test-time, agent-design, cs.lg, cs.lg-cs.ai-cs.cl
- 论文备注：23 Pages, 12 Figures, 6 Tables

## English Abstract

Recent work on distillation transfers the capabilities of large models to smaller ones often by updating the latter's parameters, through teacher forcing, on-policy distillation, and related training-time methods. In this paper, we ask whether such transfer can instead occur at test time. We study strong-to-weak scaffolding: whether a stronger builder model can construct inference-time harnesses that help a weaker target model solve tasks more reliably without any parameter updates. Using four representative Theory-of-Mind benchmarks, each builder model uses 5% of the data as a validation set to iteratively refine its harness over multiple rounds, after which the finalized harness is evaluated on the full test set. Empirically, this form of test-time capability transfer is highly effective, nearly doubling average target-model performance from 0.49 to 0.91. Our analysis shows that the gains come primarily from offloading unstable model reasoning into deterministic code, benchmark-specific routing, and strict answer-format enforcement, rather than from encouraging the target model to reason more extensively or sample more broadly. We further find that builder-model reasoning effort improves harness quality monotonically, platform effects are modest relative to the builder model's own capability, and weaker target models receive the largest gains. These results suggest that inference-time harness design is an important complement to conventional training-time distillation, enabling strong models to transfer cognitive structure to weaker models without retraining.

## English Summary

The paper formalizes strong-to-weak capability transfer at test time: a stronger builder model iteratively designs inference-time harnesses that lift a weaker target model without parameter updates. Across four Theory-of-Mind benchmarks the approach nearly doubles target-model accuracy (0.49 -> 0.91), with gains traced to deterministic code offload, benchmark-specific routing, and strict answer-format enforcement rather than more reasoning samples. Builder reasoning effort scales harness quality monotonically and weakest targets gain the most, framing harness design as a complement to training-time distillation.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
