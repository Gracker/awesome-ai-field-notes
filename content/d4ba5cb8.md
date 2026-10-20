---
id: d4ba5cb8
title: "Self-Building Labs"
authors: "Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, Varinia Bernales, Alán Aspuru-Guzik"
original_date: 2026-10-16
url: https://arxiv.org/abs/2610.23826
source: arxiv
tags: [self-driving-labs scientific-discovery agent-autonomy laboratory-automation]
---

# Self-Building Labs

> Source: [https://arxiv.org/abs/2610.23826](https://arxiv.org/abs/2610.23826) · platform: arxiv · authors: Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, Varinia Bernales, Alán Aspuru-Guzik · date: 2026-10-16

## TL;DR（中文摘要）

自动实验室（SDL）的老问题是只能跑建台时预设的流程，换一个实验就要大量人工改造，柔性成为扩展科学发现的瓶颈这篇提出 self-building laboratory（SBL）：给定高层科学目标后，系统自行设计配置并运行实验室本身，起点可以是空房间或既有设备相当于把智能体从提案者升级为建台者，与 agent harness/self-improvement 方向的观察直接相关

## Summary (English)

Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, which makes laboratory flexibility the bottleneck for scaling discovery. We introduce the self-building laboratory (SBL), which designs, configures, and operates its own laboratory setup given a high-level scientific goal. SBL starts from whatever already exists, from an empty room to a working SDL, and builds the missing capabilities: the lab layout, its digital twin, robot skills, and experimental workflows. We demonstrate the system working across different robots and setups, scaling from a single workstation to laboratories with several robots working together. We validate SBL's end-to-end capabilities through a real-world quantum-dot synthesis experiment. By shifting the role of human researchers from manually configuring and programming device automation to specifying scientific objectives, SBL makes scientific automation more accessible, flexible, and scalable. Project website: https://self-building-labs.github.io/

## 入库依据（OpenCLI 直接抓取 arXiv 元数据）

opencli arxiv paper 2610.23826 -f json 直出（list 形态已解包），metadata 字段：title/authors/published/primary_category/categories 与 entry 入库字段对齐，无二次推断。 primary_category: cs.AI; categories: cs.AI, cs.MA, cs.RO.
