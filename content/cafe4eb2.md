# Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations

- **ID**: cafe4eb2
- **原文链接**: https://arxiv.org/abs/2610.32891
- **PDF**: https://arxiv.org/pdf/2610.32891v1
- **作者**: Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi, Gunel Jahangirova, Hugo Araujo, Bernhard Bauer
- **日期**: 2026-10-23
- **更新**: 2026-10-23
- **分类**: coding
- **来源类型**: paper
- **标签**: llm-code-optimization, energy-efficiency, sustainability, effibench, icse2027
- **质量评分**: 4/5
- **抓取时间**: 2026-10-27T12:26:48Z

---

## 中文导读

论文实测 LLM 把代码改快了，但未必更省电：在 EffiBench 全部 1000 题上，对 11 个开源模型 x 4 种解码配置做硬件级能耗测量，单次推理能耗 0.79-8.68 MJ（约合 250-2800 次 GPT-4.1 查询）；限制最大输出 token 可降能耗最多 69%。执行侧 44 个配置中 42 个生成的更快代码单位问题能耗反而高于人类参考实现（+4% 到 +886%），仅有的 2 个例外也要 10^6-10^7 次执行才回本。同等规模下 MoE 架构比稠密模型推理能耗低得多且不损正确率，架构选择比解码参数更是可持续性杠杆。ICSE 2027 接收，工件已开源。

## 为什么值得关注

实测 44 个配置里 42 个的 LLM 优化代码比人类参考更耗能：快不等于省电。对以「性能优化」为默认目标的 LLM self-refinement 流水线，这篇把能耗外部性第一次摆上台面——跑得更多的 agent 循环、更长的思维链都在把执行侧的能耗差放大；MoE 优于稠密的结论则给推理服务的架构选型补了一条可持续性依据。

## 关键信息

- 论文标题: Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations
- 作者: Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi, Gunel Jahangirova, Hugo Araujo, Bernhard Bauer
- arXiv: https://arxiv.org/abs/2610.32891
- 发布时间: 2026-10-23
- arXiv 分类: cs.SE, cs.AI
- 录用信息: Accepted at the 49th IEEE/ACM International Conference on Software Engineering (ICSE 2027)
- 工件: https://doi.org/10.5281/zenodo.23598170
- 关联标签: llm-code-optimization, energy-efficiency, sustainability, effibench, icse2027

## English Abstract

Large Language Models (LLMs) are increasingly used to optimize code for performance. This practice often assumes that improvements in execution speed naturally translate into overall lower energy consumption. We challenge this assumption empirically by measuring whether performance-optimized code produced by LLM self-refinement pipelines is also energy-efficient relative to canonical human reference solutions, and whether the energy cost of the optimization process can be offset by subsequent execution-time savings. We evaluate 11 open-source models across four decoding configurations on all 1,000 problems of EffiBench, a state-of-the-art performance benchmark, while collecting per-process, hardware-level energy measurements throughout. Inference energy spans 0.79 to 8.68 MJ across model-variant pairs, which is roughly equivalent to the energy of 250 to 2800 GPT-4.1 queries. Limiting the maximum number of output tokens has the largest impact, reducing energy use by up to 69% compared to the default configuration. On the execution side, 42 of 44 configurations produce code that consumes more energy per problem than the canonical human reference, with overheads ranging from +4% to +886%. The two exceptions achieve only marginal gains, with break-even points on the order of 10^6 to 10^7 executions. Mixture-of-Experts architectures consume substantially less inference energy than equivalently-sized dense models without sacrificing correctness, making architectural choice a more consequential sustainability lever than decoding parameters. Performance optimization and energy efficiency are not always aligned goals: LLM self-refinement consistently produces faster-seeking but energy-heavier code relative to what a human engineer would write. All artifacts are available at https://doi.org/10.5281/zenodo.23598170.

## 原文摘录 (Excerpts)

> Inference energy spans 0.79 to 8.68 MJ across model-variant pairs, which is roughly equivalent to the energy of 250 to 2800 GPT-4.1 queries.

> On the execution side, 42 of 44 configurations produce code that consumes more energy per problem than the canonical human reference, with overheads ranging from +4% to +886%.

> Mixture-of-Experts architectures consume substantially less inference energy than equivalently-sized dense models without sacrificing correctness, making architectural choice a more consequential sustainability lever than decoding parameters.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取的 arXiv 元数据与摘要生成（2026-10-27 Asia/Shanghai）；导读与价值判断锚定在条目已有摘要、论文摘要、作者、日期与分类信息上，未补充论文摘要之外的实验细节。
