# You don't need long context

- **ID**: 2be6aba3
- **原文链接**: https://arxiv.org/abs/2611.05306
- **作者**: Peter Belcak et al. (NVIDIA)
- **日期**: 2026-11-03
- **分类**: models
- **来源类型**: paper
- **标签**: long-context, context-compaction, efficiency, semantic-state-space, agent-systems
- **质量评分**: 4/5
- **抓取时间**: 2026-11-05T23:54:07

---

## 中文导读

NVIDIA 团队 31 页技术报告质疑长上下文模型的必要性：前沿开源权重模型上，靠后 token 的生成成本最高可达靠前的 7 倍；通过频繁压缩上下文，模型在广泛的长程与长输入任务上几乎不损失精度。甚至在长程软件工程任务上每个上下文只执行一个动作，性能也不崩，由此提出语义状态空间模型（SSSM）概念。阅读时的关键问题是压缩摘要保留了哪些状态、哪些任务丢了分——需要精确回查原始信息的任务仍依赖完整上下文，报告并未证明所有任务都不再需要长上下文窗口。

## 为什么值得关注

7 倍 token 成本差加频繁压缩几乎不掉点，直接质疑长上下文模型的必要性；「精确回查原始信息」类任务仍是例外

## English Summary

Later tokens cost more to generate than earlier ones - up to 7x on frontier open-weight models. This NVIDIA technical report (31 pages) shows that with frequent context compaction, frontier LLMs sacrifice little to no accuracy across a broad range of long-horizon and long-input tasks, and that performance does not collapse on long-horizon software engineering even when taking at most one action per context. From this they outline semantic state space models (SSSMs), questioning the need for long-context language models. Open question: which state survives compaction and which tasks lose points - tasks requiring exact retrieval of earlier raw context still need it.

## 原文

- arXiv ID: 2611.05306 (cs.AI)
- Authors: Peter Belcak, Saurav Muralidharan, Jindong Jiang, Yonggan Fu, Wonmin Byeon, Hanrong Ye, Ryan Angilly, Ali Taghibakhshi, Shih-Yang Liu, Siru Ouyang, Greg Heinrich, Pavlo Molchanov
- Submitted: 2026-11-03 (updated 2026-11-03)
- PDF: https://arxiv.org/pdf/2611.05306v1

## Abstract (原文)

Later tokens are costlier to generate than earlier tokens. On frontier open weight models, the disparity in cost may rise to as much as 7x. Through frequent compaction, we show across a broad range of long-horizon and long-input tasks that frontier language models sacrifice little to no task accuracy when maintaining short contexts. We further demonstrate that LLM performance does not collapse on long-horizon software engineering tasks even when taking at most one action per context, and based on that we outline the concept of semantic state space models (SSSMs). Our findings question the need for long-context language models.

（抓取于 2026-11-05T23:54:07，来源见上方原文链接）
