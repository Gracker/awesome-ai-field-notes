# Sequential Anytime Valid Tests for Efficient Inference-Time Alignment

- **ID**: c17db9bd
- **原文链接**: https://arxiv.org/abs/2611.26413
- **作者**: Vishesh Kumar Singh, Sayak Ray Chowdhury
- **日期**: 2026-11-19
- **分类**: models
- **来源类型**: paper
- **标签**: inference-time-alignment, best-of-n, early-stopping, e-process, statistical-guarantee
- **质量评分**: 4/5
- **抓取时间**: 2026-11-22T15:45:22Z

---

## 中文导读

Best-of-N 这类推理时对齐给每个 prompt 固定采样预算，但各 prompt 所需算力差异巨大，已有自适应早停只有启发式阈值，对停错没有统计控制。作者把「何时停」写成序列检验：候选按最终答案用 reward 加权自一致性分数聚类，给定错误容忍 α 后只在答案被认证为多数派时停止。SPRT-RWSC 实验不错但保证在答案漂移加连续监控下失效；主贡献 e-RWSC 换成 betting supermartingale，把任何时刻认证到非主导答案的概率一致压在 α 以内，认证需 O(log(1/α)/d_KL) 样本。实验验证成本标度，准确率高于基线且 token 成本显著更低。


## 为什么值得关注

推理成本优化的第二条路：不动模型和采样器，只给「何时停」加上统计保证；做 Best-of-N/自一致性类采样的团队可以直接对照。

## 关键信息

- 论文标题：Sequential Anytime Valid Tests for Efficient Inference-Time Alignment
- 作者：Vishesh Kumar Singh, Sayak Ray Chowdhury
- 提交：2026-11-19 | 分类：cs.LG
- 核心机制：RWSC 聚类 + e-process 停机，停错概率一致 ≤ α
- 成本标度：认证一个主导答案约 O(log(1/α)/d_KL) 样本

## English Abstract

Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-valid stopping rule that takes an error tolerance $α$ as input and halts only once an answer is certified to hold a majority ($θ_a > 1/2$) under the generator's distribution. We aggregate candidates by final answer with a reward-weighted self-consistency (RWSC) score and treat stopping as a sequential test over the resulting clusters. Applying Wald's sequential probability ratio test to these clusters yields SPRT-RWSC, which performs well empirically, but its guarantee fails because the leading answer shifts during sampling, and the run is continuously monitored. Our main contribution, e-RWSC, replaces Wald's test with a betting supermartingale (an e-process) for every answer the policy produces, bounding the probability of ever certifying a non-dominant answer by $α$, uniformly over time and across all answers. The RWSC scores drive the bets, so they affect only how quickly a dominant answer $a^\star$ is certified, not validity; certification takes $O(\log(1/α)/d_{\mathrm{KL}}(θ_{a^\star}\|1/2))$ samples. Experiments across several language models, datasets, and reward models confirm the predicted $1/d_{\mathrm{KL}}$ scaling of cost and show that accuracy improves over baselines at substantially lower token cost.


## 来源与证据

摘要取自 opencli arxiv paper 2611.26413 -f json（2026-11-22）；中文导读锚定摘要原文；选题来自当日论文流水线速报（Obsidian：OpenClaw定时任务/论文流水线/2026-11-22）。
