# Towards LLM-Enhanced Android Taint Analysis

- **ID**: 8dfae61d
- **原文链接**: https://arxiv.org/abs/2608.24269
- **PDF**: https://arxiv.org/pdf/2608.24269v1
- **作者**: Nicholas Miazzo, Marco Alecci, Jordan Samhi, Jacques Klein, Eleonora Losiouk
- **日期**: 2026-08-25
- **更新**: 2026-08-25
- **分类**: coding
- **来源类型**: paper
- **标签**: android, security, static-analysis, llm-agent, arxiv
- **质量评分**: 4/5

---

## 中文导读

初步研究：让现成 LLM 以 agent 方式迭代探索代码、沿数据流推理，在 DroidBench 上与 FlowDroid 正面对比。Gemini-3 Flash 拿到 F1 0.96，FlowDroid 为 0.55；在 FlowDroid 公认困难的类目差距更大——跨组件通信 0.95 对 0.17、隐式流 0.94 对 0.00、反射 1.00 对 0.50。在一小组真实应用上，LLM 还报出了 FlowDroid 未覆盖的候选泄露点。作者定位为初步结果，方向是混合管线：LLM 推理当静态分析的补充证据源。注意 DroidBench 属教学基准、真实样本集小，现阶段合理用法是复杂类目出候选加静态工具复核，替代性叙事证据不足。

## 为什么值得关注

LLM agent 在 DroidBench 污点分析上 F1 0.96 对 FlowDroid 0.55，反射/隐式流类目接近满分；教学基准之上先按混合管线评估

## English Abstract

Taint analysis is a fundamental technique for detecting sensitive data leaks in Android apps. However, traditional static tools, such as FlowDroid, still face well-known challenges due to the complexity of accurately modeling the Android framework. In this paper, we investigate whether off-the-shelf Large Language Models (LLMs) can effectively reason about taint flows in Android apps. Our preliminary approach relies on an agentic interaction strategy, enabling the LLM to iteratively explore code and reason about data flows. We conduct an initial evaluation on the DroidBench benchmark against FlowDroid, where our approach outperforms the baseline: Gemini-3 Flash achieves an F1-score of 0.96, compared to 0.55 for FlowDroid. In particular, we observe improvements in challenging categories such as inter-component communication (0.95 vs. 0.17), implicit flows (0.94 vs. 0.00), and reflection (1.00 vs. 0.50), where FlowDroid typically struggles. On a small set of real-world apps, the LLM-based approach also identifies additional potential data leaks not reported by FlowDroid. These preliminary findings suggest that LLM reasoning may effectively complement traditional static taint analysis, motivating future research on hybrid LLM-enhanced taint analysis pipelines.

## Obsidian Notes

- Metadata and abstract fetched via `opencli arxiv paper 2608.24269 -f json` (2026-08-27); response parsed list-or-dict tolerant.
- DroidBench 为教学基准，真实应用样本集小，摘要明确自述 preliminary。
- 中文导读与价值判断锚定在论文摘要上，未补充摘要之外的实验细节。
