# Sound Probabilistic Safety Bounds for Large Language Models

- **ID**: e68defdf
- **原文链接**: https://arxiv.org/abs/2607.20286
- **PDF**: https://arxiv.org/pdf/2607.20286v1
- **作者**: Mahdi Nazeri, Anne-Kathrin Schmuck, Sadegh Soudjani, Alessandro Abate
- **日期**: 2026-07-22
- **分类**: cs.CL, cs.AI
- **标签**: llm-safety, certification, pac-bounds, evaluation, harmful-output
- **质量评分**: 4/5
- **抓取时间**: 2026-07-24T20:19:08+08:00

---

## 中文解读

这篇论文把 LLM 安全评估表述为给定 prompt 下产生有害输出的概率边界问题：用 Clopper-Pearson 置信区间构造 PAC bounds，并利用 latent space 特征优先探索自回归生成树中更可能有害的分支摘要强调其 lower bounds 是 sound 的形式上证明低于真实 harmfulness probability，即使真实概率很小也能计算非平凡下界适合作为 LLM 安全认证/统计验证方向的参考

## 为什么值得关注

- 它把安全评估从经验测试推进到带 PAC 语义的概率边界与统计认证，尤其关注低概率有害输出下界；适合跟踪 LLM safety certification / formal evaluation 方向。

## English Summary

This paper proposes a framework for computing rigorous bounds on the probability that an LLM generates harmful output for a given prompt. It applies Clopper-Pearson confidence intervals to obtain PAC bounds and introduces an algorithm that prioritizes branches in the autoregressive generation tree using latent-space features. The abstract emphasizes sound lower bounds: formally proven to be less than the actual harmfulness probability, including cases where the true harm probability is extremely small.

## Abstract

We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt. We study a new application of the Clopper-Pearson confidence intervals to obtain probably approximately correct (PAC) bounds for this problem. As our main technical contribution, we propose an algorithm that leverages features in the latent space to prioritize exploring branches in the auto-regressive generation tree that are more likely to produce harmful outputs. Our approach in particular enables the efficient computation of useful lower bounds, even in scenarios where the true harm probability is extremely small, and crucially, the obtained lower bounds are sound, i.e., formally proven to be less than the actual harmfulness probability: our experimental results demonstrate the effectiveness of our method by computing non-trivial lower bounds on state-of-the-art LLMs. This study newly enables the evaluation and statistical certification of LLMs.

## Metadata

- arXiv ID: 2607.20286
- Published: 2026-07-22
- Updated: 2026-07-22
- Primary category: cs.CL
- Categories: cs.CL, cs.AI
- Comment: The Initial version of this manuscript has been available on OpenReview, see https://openreview.net/forum?id=papImkPLf5
- OpenCLI return code: 0
