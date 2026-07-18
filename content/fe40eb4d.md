# EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer

> External-scan entry · 2026-07-08 · awesome-ai-field-notes

- **URL**: https://arxiv.org/abs/2607.05202
- **Source**: arxiv · Xingze Gao, Chuanrui Hu, Hongda Chen, Pengfei Yao, Zhao Wang, Yi Bai, Zhengwei Wu, Yunyun Han
- **Original Date**: 2026-07-08
- **Added**: 2026-07-08
- **Category**: agents
- **Tags**: agent-benchmark, self-evolution, ability-transfer, experience-encoding
- **Quality Score**: 4

## 中文摘要

EvoAgentBench 把 Agent 自进化评测从单轮解题准确率推向过程级能力迁移：从执行轨迹里抽取 trace-grounded 的 Abilities，规范成可复用的操作单元，再用领域特定 Ability Graph 把共享过程的任务串起来528/267 的训练/测试切分显示，整理好的 Ability 内容可以跨模型家族迁移，但目前没有一种自动方法在所有设置下都能保持正向增益

## English Abstract

Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that prompt LLMs to produce discrete scores for candidate solutions, LLM-as-a-Verifier computes the expectation over the distribution of scoring token logits to generate continuous scores. This probabilistic formulation enables verification to scale along multiple dimensions: (1) score granularity, (2) repeated evaluation, and (3) criteria decomposition. In particular, we show that scaling the scoring granularity leads to better separation between positive and negative solutions, resulting in more calibrated comparisons. Moreover, scaling repeated evaluation and criteria decomposition consistently lead to additional gains in verification accuracy through variance and complexity reduction. We further introduce a cost-efficient ranking algorithm for selecting the best solution among candidates using the verifier&#39;s continuous scores. LLM-as-a-Verifier achieves state-of-the-art performance on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), and MedAgentBench (73.3%). Beyond verification, the fine-grained signals from LLM-as-a-Verifier can also serve as a proxy for estimating task progress. We build an extension for Claude Code, enabling developers to monitor and improve their own agentic systems. Finally, we show that LLM-as-a-Verifier can provide dense feedback for RL, improving the sample efficiency of SAC and GRPO on robotics and mathematical reasoning benchmarks.

## One-liner

EvoAgentBench 把 Agent 自进化评测从单轮解题准确率推向过程级能力迁移：从执行轨迹里抽取 trace-grounded 的 Abilities，规范成可复用的操作单元...

---

> 注：本文件为 external-scan cron 写入的 source body；如需更深入精读，请由 content-fetcher 任务补充完整正文。
