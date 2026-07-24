# Don't Trust the Label: License Laundering in AI Supply Chains

- **ID**: 8deae4fb
- **原文链接**: https://arxiv.org/abs/2607.20300
- **PDF**: https://arxiv.org/pdf/2607.20300
- **作者**: James Jewitt, Hao Li, Gopi Krishnan Rajbahadur, Bram Adams, Ahmed E. Hassan
- **日期**: 2026-07-22
- **分类**: cs.SE, cs.AI
- **标签**: ai-supply-chain, license, huggingface, github, governance
- **质量评分**: 5/5
- **抓取时间**: 2026-07-24T12:19:07+08:00

---

## 中文解读

这篇论文把 AI 资产供应链中的许可证洗白量化到 232,270 条 datasetmodelapplication 链路：数据集/模型在 Hugging Face 流转，应用落到 GitHub摘要给出的核心信号是：62.3% 链路至少经过一个无声明许可证资产；带义务的许可证类别端到端存活率都低于 7%，而 Permissive 类别可达 95.1%对模型发布数据治理和企业合规来说，它提示不能只看下游标签，必须追踪来源链路

## 为什么值得关注

- 把 AI 供应链中的许可证传播问题量化到跨平台链路，能直接服务模型/数据治理、合规审查与发布流程设计。

## English Summary

The paper traces 232,270 datasetmodelapplication chains across Hugging Face datasets/models and GitHub applications to measure whether license obligations survive redistribution. The abstract reports two forms of license laundering: unlabeled artifacts gaining definitive downstream labels, and one declared license category replacing another. It finds 62.3% of chains pass through at least one no-license artifact, obligation-bearing categories have under 7% end-to-end survival, while the Permissive category reaches 95.1%.

## Abstract

AI artifacts move through a multi-platform supply chain, spanning datasets and models on Hugging Face and applications on GitHub. While each artifact carries a license whose obligations should propagate through redistribution, no study has yet measured whether those obligations survive the chain or are stripped and replaced as artifacts move downstream. We trace 232,270 dataset$\rightarrow$model$\rightarrow$application chains and quantify two forms of license laundering: when artifacts with no declared license acquire definitive labels downstream, and when one declared license category replaces another during redistribution. We find that 62.3% of chains pass through at least one artifact with no declared license (concentrated in a small set of foundational datasets), and that every obligation-bearing license category falls below 7% end-to-end survival while the Permissive category reaches 95.1%. Based on these findings, we provide actionable recommendations for practitioners, model publishers, rights holders, and platform owners.

## Metadata

- arXiv ID: 2607.20300
- Primary category: cs.SE
- Categories: cs.SE, cs.AI
- Source: OpenCLI arXiv metadata
