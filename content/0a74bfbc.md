# Post-Training Language Models for Gold-Medal Performance in Coding Competitions

- **ID**: 0a74bfbc
- **原文链接**: https://arxiv.org/abs/2609.02849
- **PDF**: https://arxiv.org/pdf/2609.02849v1
- **作者**: Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg
- **日期**: 2026-09-02
- **更新**: 2026-09-02
- **分类**: coding
- **来源类型**: paper
- **标签**: competitive-programming, post-training, reinforcement-learning, test-time-compute
- **质量评分**: 4/5
- **抓取时间**: 2026-09-04T04:22:30Z

---

## 中文导读

NVIDIA 团队的竞赛编程端到端专精管线：2.2 万道精选题 + 合成推理轨迹 + SFT + RLNemotron-3-Nano-CC（30B-A3B，SFT+RL）在 IOI 2025 从 130 分提升到 291 分，配合测试时策略 GenCorrect（生成-评估-精炼多样解）达到 468 分，超过金牌线 438.3；550B 的 Ultra-CC 仅用 SFT 达到 502在 IOI 2026 与人类选手同时限同网络同提交约束的前瞻评估中，竞赛特化版 Ultra-CC 得分 535.4/600，超过金牌线 361.12 和人类最高分 498.27据作者称是首个在 IOI 题集上超越人类最高分选手的 AI 系统（cs.LG/cs.AI/cs.SE 等，2026-09-02）

## 为什么值得关注

NVIDIA 团队的竞赛编程端到端专精管线：2. 该工作由 arXiv 摘要直接背书：结论、实验设置与指标均出自摘要原文（2026-09-02 提交，cs.LG, cs.AI, cs.CL, cs.MA, cs.SE），适合关注 coding 方向的近期进展。

## 关键信息

- 论文标题：Post-Training Language Models for Gold-Medal Performance in Coding Competitions
- 作者：Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg
- arXiv：https://arxiv.org/abs/2609.02849
- 发布时间：2026-09-02
- arXiv 分类：cs.LG, cs.AI, cs.CL, cs.MA, cs.SE
- 关联标签：competitive-programming, post-training, reinforcement-learning, test-time-compute

## English Abstract

Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, we train Nemotron-3-Nano-CC (30B-A3B) with SFT and RL and Nemotron-3-Ultra-CC (550B-A55B) with SFT alone. We further introduce GenCorrect, a feedback-driven test-time compute strategy that iteratively generates, evaluates, and refines diverse solutions. On IOI 2025, Nano-CC improves from 130 points to 291 after post-training and to 468 with GenCorrect, exceeding the gold threshold of 438.3 while Ultra-CC reaches 502. Guided by these results, we develop a competition-specific Ultra-CC system and evaluate it prospectively during IOI 2026. Under the same time, internet-access, and submission constraints as human contestants, it scores 535.4 out of 600, exceeding both the gold threshold of 361.12 and the top human score of 498.27. To our knowledge, this is the first AI system to outscore the highest-scoring human contestant on an IOI problem set.

## English Summary

An end-to-end specialization pipeline for competitive programming combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, the NVIDIA team trains Nemotron-3-Nano-CC (30B-A3B) with SFT+RL and Nemotron-3-Ultra-CC (550B-A55B) with SFT alone, plus GenCorrect, a feedback-driven test-time compute strategy that iteratively generates, evaluates, and refines diverse solutions. On IOI 2025, Nano-CC improves from 130 to 291 points after post-training and to 468 with GenCorrect, exceeding the gold threshold of 438.3, while Ultra-CC reaches 502....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
