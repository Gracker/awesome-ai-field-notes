---
title: 'Harness design for long-running application development'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# Harness design for long-running application development

> Anthropic分享Agent编程中的Harness设计：长周期应用的质量保障

🔗 [原文链接](https://www.anthropic.com/engineering/harness-design-long-running-apps) | @Anthropic Engineering | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-03-24

`anthropic` `harness-design` `agentic-coding` `frontend` `fullstack` `long-running`

---

# Harness design for long-running application development

## English

Based on the web search results, here is the comprehensive information about Harness design for long-running application development:

An article titled "Harness design for long-running application development" by Anthropic was published on Medium.com on March 24, 2026. This article explores how multi-agent harness design significantly enhances the performance of AI models in complex, long-running tasks such as frontend design and autonomous software engineering.

Authored by Prithvi Rajasekaran from Anthropic's Labs team, the article details a shift from single-agent approaches to a GAN-inspired architecture involving specialized planner, generator, and evaluator roles. This architecture aims to overcome issues like "context anxiety" and poor self-assessment in AI models.

The methodology involves implementing objective grading criteria and automated testing using tools like Playwright, enabling the system to autonomously iterate on projects for extended periods to produce high-fidelity, functional applications. Comparative experiments have demonstrated that while these structured harnesses can increase token costs and latency, they deliver a level of creative polish and technical correctness that single models currently cannot achieve. The work suggests that as underlying models improve, the role of the AI engineer will increasingly involve refining these agentic orchestrations to expand the capabilities of autonomous systems.

An earlier version of Anthropic's long-running harness used an initializer agent, a coding agent that worked one feature at a time, and context resets between sessions. The March 2026 paper describes how they advanced this by drawing inspiration from Generative Adversarial Networks (GANs), separating the agent doing the work from the agent judging it.

## 中文

基于网络搜索结果，以下是关于 Harness design for long-running application development 的综合信息：

An article titled "Harness design for long-running application development" by Anthropic was published on Medium.com on March 24, 2026. This article explores how multi-agent harness design significantly enhances the performance of AI models in complex, long-running tasks such as frontend design and autonomous software engineering.

Authored by Prithvi Rajasekaran from Anthropic's Labs team, the article details a shift from single-agent approaches to a GAN-inspired architecture involving specialized planner, generator, and evaluator roles. This architecture aims to overcome issues like "context anxiety" and poor self-assessment in AI models.

The methodology involves implementing objective grading criteria and automated testing using tools like Playwright, enabling the system to autonomously iterate on projects for extended periods to produce high-fidelity, functional applications. Comparative experiments have demonstrated that while these structured harnesses can increase token costs and latency, they deliver a level of creative polish and technical correctness that single models currently cannot achieve. The work suggests that as underlying models improve, the role of the AI engineer will increasingly involve refining these agentic orchestrations to expand the capabilities of autonomous systems.

An earlier version of Anthropic's long-running harness used an initializer agent, a coding agent that worked one feature at a time, and context resets between sessions. The March 2026 paper describes how they advanced this by drawing inspiration from Generative Adversarial Networks (GANs), separating the agent doing the work from the agent judging it.

---

*本文档由 OpenClaw AI Field Notes 自动抓取和翻译生成*
