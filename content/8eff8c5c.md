# The Alignment Illusion in Multimodal Large Language Models

> 原文链接: https://arxiv.org/abs/2609.30210
> 作者: Hong-Han Wang, Yuntao Wang, Hu Ding
> 发布时间: 2026-09-24
> 源: arXiv外部扫描 (2026-09-28)

---

## 摘要

arXiv 2609.30210（NeurIPS 2026 接收）挑战一个流行读法：MLLM 逐层 visual-text similarity 上升并不代表视觉信息被渐进整合到共享表征空间作者在 13 个跨 0.5B72B五大家族的 MLLM 上做控制干预用高斯噪声替换 projector 输出的视觉 token 让任务精度骤降但 CKASVCCAMIR 和首主夹角余弦这四种标量相似度都无法稳定区分被破坏流与原流他们称此为 alignment illusion，溯源到共享语言模型通路：各向异性 MLP 下投影把视觉与文本 token 一起拉到公共输出方向，产生权重诱导对齐论文提出 principal-angle gap（首二主夹角余弦差）来分离权重诱导相似度与多向视觉结构，并在梯度化视觉破坏下比四种标量更稳定地跟踪任务精度

## English Summary

arXiv 2609.30210 (NeurIPS 2026) tests the assumption that layer-wise visual-text similarity in MLLMs reflects content-level cross-modal interaction: across 13 MLLMs from five families (0.5B72B), replacing projector visual tokens with Gaussian noise collapses task accuracy yet CKA, SVCCA, MIR, and top principal-angle cosine fail to separate the corrupted stream from the original. The authors trace this alignment illusion to anisotropic MLP down-projections and propose a principal-angle gap that tracks task accuracy more reliably under graded visual corruption.

## 为什么值得关注

MLLM 各层 visual-text 相似度可能是权重诱导的幻觉，PA gap 把它与真正视觉结构分开

## 信息源

- https://arxiv.org/abs/2609.30210
