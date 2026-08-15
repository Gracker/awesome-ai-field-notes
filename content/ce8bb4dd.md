# SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs

- **ID**: ce8bb4dd
- **原文链接**: https://arxiv.org/abs/2512.09543
- **PDF**: https://arxiv.org/pdf/2512.09543
- **作者**: Arihant Tripathy, Ch Pavan Harshit, Karthik Vaidhyanathan
- **日期**: 2025-12-10
- **更新**: 2025-12-11
- **分类**: coding
- **来源类型**: paper (arxiv)
- **标签**: swe-agents, small-language-models, energy-efficiency, empirical-study, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-15T12:25:21Z

---

## 中文导读

实证研究：把四个主流 agentic issue resolution 框架（SWE-Agent、OpenHands、Mini SWE Agent、AutoCodeRover）刻意约束到两个小语言模型（Gemma-3 4B、Qwen-3 1.7B），在 SWE-bench Verified Mini 上做受控评估，固定硬件上每种配置跑 150 次，测量能耗、时长、token 用量与内存。核心发现：框架架构是能耗的主要驱动因素——最耗能的 AutoCodeRover（Gemma）平均能耗是最低的 OpenHands（Gemma）的 9.4 倍；但任务解决率接近零，能量大量消耗在无效的推理循环上。结论把瓶颈拆成两层：成功率的瓶颈在 SLM 的推理能力，效率的瓶颈在框架设计；面向大 LLM 设计的被动编排框架配 SLM 时既不有效也不高效，可行的低能耗路线需要主动管理 SLM 弱点的架构。

## 为什么值得关注

coding agent 落地选型时能耗/算力维度的稀缺实证数据：150 runs/配置的受控测量给出框架间 9.4 倍能耗差，且明确区分“模型能力瓶颈”与“框架效率瓶颈”两个正交问题。对考虑本地部署、边缘设备跑 SWE agent 的团队，这是少见的 grounded 选型依据；对框架作者，“被动编排 -> 主动管理 SLM 弱点”是明确的架构方向。

## 关键信息

- 论文标题：SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs
- 四个框架：SWE-Agent、OpenHands、Mini SWE Agent、AutoCodeRover
- 两个 SLM：Gemma-3 4B、Qwen-3 1.7B
- 基准与规模：SWE-bench Verified Mini，固定硬件，150 runs/配置
- 测量指标：能耗、时长、token 用量、内存
- 关键数字：AutoCodeRover(Gemma) 平均能耗 = OpenHands(Gemma) 的 9.4 倍；任务解决率接近零
- 结论：框架架构是能耗主因；能量大量浪费在无效推理循环；需要主动管理 SLM 弱点的架构
- arXiv 分类：cs.SE, cs.AI

## English Abstract

Context. LLM-based autonomous agents in software engineering rely on large, proprietary models, limiting local deployment. This has spurred interest in Small Language Models (SLMs), but their practical effectiveness and efficiency within complex agentic frameworks for automated issue resolution remain poorly understood. Goal. We investigate the performance, energy efficiency, and resource consumption of four leading agentic issue resolution frameworks when deliberately constrained to using SLMs. We aim to assess the viability of these systems for this task in resource-limited settings and characterize the resulting trade-offs. Method. We conduct a controlled evaluation of four leading agentic frameworks (SWE-Agent, OpenHands, Mini SWE Agent, AutoCodeRover) using two SLMs (Gemma-3 4B, Qwen-3 1.7B) on the SWE-bench Verified Mini benchmark. On fixed hardware, we measure energy, duration, token usage, and memory over 150 runs per configuration. Results. We find that framework architecture is the primary driver of energy consumption. The most energy-intensive framework, AutoCodeRover (Gemma), consumed 9.4x more energy on average than the least energy-intensive, OpenHands (Gemma). However, this energy is largely wasted. Task resolution rates were near-zero, demonstrating that current frameworks, when paired with SLMs, consume significant energy on unproductive reasoning loops. The SLM's limited reasoning was the bottleneck for success, but the framework's design was the bottleneck for efficiency. Conclusions. Current agentic frameworks, designed for powerful LLMs, fail to operate efficiently with SLMs. We find that framework architecture is the primary driver of energy consumption, but this energy is largely wasted due to the SLMs' limited reasoning. Viable low-energy solutions require shifting from passive orchestration to architectures that actively manage SLM weaknesses.

## English Summary

Empirical study constraining four leading agentic issue resolution frameworks to Small Language Models, measuring performance, energy efficiency, and resource consumption in resource-limited settings to assess the viability of SLM-driven automated issue resolution and characterize the resulting trade-offs.

## Obsidian Notes

- 内容由 `opencli arxiv paper 2512.09543 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断锚定在 arXiv 摘要与条目既有 summary 上；未补充摘要之外的实验细节。
- 条目收录日期：2026-08-15；语言：both。
