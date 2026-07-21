# When Does Muon Help Agentic Reinforcement Learning?

- source_url: https://arxiv.org/abs/2607.16169
- source_type: paper
- platform: arxiv
- author: Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun
- original_date: 2026-07-17
- added_date: 2026-07-21
- arxiv_id: 2607.16169
- arxiv_categories: cs.LG, cs.AI
- pdf_url: https://arxiv.org/pdf/2607.16169v2
- category: agents
- tags: agentic-rl, optimizer, muon, post-training, alfworld, arxiv
- quality_score: 4

## 摘要（中文）

论文在稀疏奖励 agentic RL 后训练中比较 Muon 与 AdamW：基于 ALFWorld 与 Qwen2.5-0.5B-Instruct 的匹配单 seed 实验显示，在 GiGPO 下只把 Muon 用于 hidden weight matrices，可把最终窗口验证成功率从 0.290 提升到 0.546；效果受 advantage estimator 与 learning rate 明显影响。作者同时报告 GRPO、GraphGPO 不同设置下的 AUC 与收敛速度差异。

## Summary (English)

Muon is competitive with AdamW in large-scale pre-training, but its value for reinforcement-learning (RL) post-training remains unclear. We study vanilla Muon in sparse-reward agentic RL through matched single-seed comparisons with AdamW on ALFWorld using Qwen2.5-0.5B-Instruct. Under Group-in-Group Policy Optimization (GiGPO), applying Muon only to hidden weight matrices raises final-window validation success from 0.290 to 0.546 (+88%); high-rate AdamW controls retain no post-update success. The effect depends on the advantage estimator and learning rate. At 3e-5, Muon improves GRPO from 0.161 to 0.268, whereas GraphGPO's late-window gap narrows near saturation. At 1e-5, GraphGPO Muon reaches 0.901, raises normalized validation AUC from 0.399 to 0.556, and reaches 0.5 and 0.75 success 30 and 60 updates earlier, respectively. These exploratory results show that Muon can benefit agentic RL and motivate studying the policy optimizer, advantage estimator, and learning rate jointly.

## One-liner

优化器选择、advantage estimator 与学习率需要作为 agentic RL 训练栈的一组耦合变量一起看。

## 原文 / 元数据抓取

# When Does Muon Help Agentic Reinforcement Learning?
> 作者: Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun
> 原文链接: https://arxiv.org/abs/2607.16169
> PDF: https://arxiv.org/pdf/2607.16169v2
> 发布时间: 2026-07-17
> 更新时间: 2026-07-20
> 分类: cs.LG, cs.AI

---

Muon is competitive with AdamW in large-scale pre-training, but its value for reinforcement-learning (RL) post-training remains unclear. We study vanilla Muon in sparse-reward agentic RL through matched single-seed comparisons with AdamW on ALFWorld using Qwen2.5-0.5B-Instruct. Under Group-in-Group Policy Optimization (GiGPO), applying Muon only to hidden weight matrices raises final-window validation success from 0.290 to 0.546 (+88%); high-rate AdamW controls retain no post-update success. The effect depends on the advantage estimator and learning rate. At 3e-5, Muon improves GRPO from 0.161 to 0.268, whereas GraphGPO's late-window gap narrows near saturation. At 1e-5, GraphGPO Muon reaches 0.901, raises normalized validation AUC from 0.399 to 0.556, and reaches 0.5 and 0.75 success 30 and 60 updates earlier, respectively. These exploratory results show that Muon can benefit agentic RL and motivate studying the policy optimizer, advantage estimator, and learning rate jointly.

## Obsidian intake evidence excerpt

该内容文件由 AAIF content-fetcher 根据 active/high-score entry 与 OpenCLI arXiv 元数据补齐。

- entry_id: ee0ededa
- title: When Does Muon Help Agentic Reinforcement Learning?
- source: https://arxiv.org/abs/2607.16169
- existing_summary_zh: 论文比较 Muon 与 AdamW 在稀疏奖励 agentic RL 后训练中的表现：在 ALFWorld + Qwen2.5-0.5B-Instruct 设置下，Muon 只作用于 hidden weight matrices 时，GiGPO 最终窗口验证成功率从 0.290 提升到 0.546；不同 advantage estimator 与学习率下收益差异明显收录理由：它把优化器选择优势估计器和学习率放到同一个 agentic RL 实验框架中讨论，适合跟踪智能体训练栈
