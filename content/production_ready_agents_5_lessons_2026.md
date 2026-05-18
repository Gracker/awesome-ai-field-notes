---
title: "Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith"
date: 2026-04-21
source: google
category: agents
tags: [ADK, production, Pydantic, RAG, OpenTelemetry, circuit-breaker, Titanium]
quality_score: 4
status: fetched
---

## 生产级 AI Agent：重构单体系统的 5 条实战经验

**发布日期：2026年4月21日 | 来源：Google Cloud Blog**

### 概述

在本地机器上构建一个运行良好的 AI Agent 很轻松。但构建一个能经受现实考验的 Agent——处理速率限制、避免无限循环、超越硬编码数据的规模限制——完全是另一回事。

为了解决这些"脆弱架构"模式，AI Agent Clinic 启动了第一个任务：对名为"Titanium"的脆弱销售研究 Agent 进行了完整重构。

以下是从重构中获得的核心问题、修复方案和工程经验。

### 经验 1：用编排式子 Agent 替代单体

**问题：** 原始 Agent 运行在一个庞大的线性 for 循环——单体脚本中。如果某个子任务失败，整个流程就会停滞并静默失败。

**修复：** 我们用 Google 的 Agent Development Kit（ADK）的分布式框架替换了单体。创建了 SequentialAgent 流水线，将工作负载拆分为专门节点：公司研究员、搜索规划师、案例研究员、筛选器和邮件起草员。

**经验：** 分离关注点。专业化的窄任务 Agent 比试图执行大规模多步骤提示的单一 LLM 运行得更可靠。

### 经验 2：用 Pydantic 强制结构化输出

**问题：** 最初，Titanium 通过在提示字符串内部大量硬编码来强制模型输出 JSON。这导致代码混乱、解析脆弱，并且一遍又一遍地浪费 token 描述确切的结构。

**修复：** 切换到 ADK 时，我们将模式格式化指令从提示中清除。相反，我们直接注入原生 Pydantic 对象作为明确的模式定义。

**经验：** 通过将"契约"从模糊的自然语言请求转变为运行时验证的 Python 对象，我们保证了结构完整性并消除了脆弱的自定义解析。

### 经验 3：用动态 RAG 流水线替代硬编码状态

**问题：** Titanium 的上下文语料库人为地很小。它只知道硬编码到 Python 文件中的 12 个案例研究。

**修复：** 我们构建了一个动态数据摄入系统。异步爬虫（Playwright）在后台运行，自主抓取 Google Cloud 客户成功网站并批量发送到 Google Cloud Vector Search。

**经验：** 硬编码适合原型，但生产流水线需要自我刷新。真正的 Agent 价值来自于赋予 Agent 工具来自主获取、扩展和通过向量搜索查询的能力。

### 经验 4：可观测性不可或缺

**问题：** 当 LLM 在标准脚本中困惑时，它是一个"黑箱"。你知道某事失败了，但不知道是哪个组件导致了中断。

**修复：** 我们利用了 ADK 对 Google Cloud 上 OpenTelemetry 的一级支持。开箱即用，ADK 为完整执行流程发出分布式追踪。

**经验：** 不能在没有任何实时诊断的情况下将 Agent 投入生产。

### 经验 5：控制 Token 消耗（成本优化）

**问题：** Agent 循环是昂贵的。如果 Agent 遇到错误并在没有严格边界的情况下不断重试提示，它会在几分钟内耗尽您的 token 预算。

**修复：** 通过大量采用 ADK 的原生编排，我们自动继承了固有的成本优化。该框架原生包含指数退避、超时边界和可配置的重试循环。

**经验：** 始终安装断路器。

---
**参考链接：**
- [观看完整的 AI Agent Clinic 第 1 集](https://www.youtube.com/live/md2VFN6SojQ)
- [Titanium 代码库](https://github.com/ai-agent-clinic/google-agent-clinic)
- [ADK 文档](https://cloud.google.com/agent-builder/docs/overview)

---

## Production-Ready AI Agents: 5 Lessons from Refactoring a Monolith

**Published: April 21, 2026 | Source: Google Cloud Blog**

### Overview

Building an AI agent that works beautifully on your local machine is easy. Building one that survives contact with reality is a completely different beast.

To solve these "fragile architecture" patterns, the AI Agent Clinic launched its first mission: a complete teardown of "Titanium"—a promising but brittle sales research agent.

Here are the core breakdowns, the fixes, and the engineering lessons from the refactoring.

### 1. Ditch the Monolith for Orchestrated Sub-Agents

**The Breakdown:** The original agent was running on a massive, linear for loop. If one sub-task failed, the entire process stalled out and failed silently.

**The Fix:** We ripped out the monolith and installed a distributed framework using Google Agent Development Kit (ADK). We created a SequentialAgent pipeline, splitting the workload into specialized nodes.

**The Lesson:** Separation of concerns. Specialized agents with narrow tasks run more reliably than a single LLM trying to execute a massive, multi-step prompt.

### 2. Force Structured Outputs (via Pydantic)

**The Breakdown:** Originally, Titanium forced JSON outputs via extensive hard-coding inside the prompt string. It resulted in dirty code, fragile parsing, and wasted tokens.

**The Fix:** When swapping to ADK, we eradicated schema formatting instructions from the prompt. Instead, we injected native Pydantic objects directly as explicit schema definitions.

**The Lesson:** By shifting the "contract" from a fuzzy natural language request to a runtime-validated Python object, we guarantee structural integrity.

### 3. Replace Hardcoded State with a Dynamic RAG Pipeline

**The Breakdown:** Titanium only knew about 12 hardcoded case studies. It could not scale or learn without a developer manually updating the code.

**The Fix:** We built a dynamic data intake system. An async crawler (Playwright) runs in the background to autonomously scrape Google Cloud customer success website and batch them to Google Cloud Vector Search.

**The Lesson:** Hardcoding is fine for a prototype, but a production pipeline needs to refresh itself.

### 4. Observability is Non-Negotiable

**The Breakdown:** When an LLM gets confused, it is a "black box." You know something failed, but you have no idea which component caused the break.

**The Fix:** We tapped into ADK first-class support for OpenTelemetry on Google Cloud. ADK emits distributed traces for full execution flows.

**The Lesson:** You cannot put an agent into production without live diagnostics.

### 5. Taming the Token Burn (Cost Optimization)

**The Breakdown:** Agentic loops are expensive. If an agent hits an error and continually retries without strict boundaries, it will burn through your token budget in minutes.

**The Fix:** By standardizing on ADK native orchestration, we inherited intrinsic cost optimizations automatically.

**The Lesson:** Always install circuit breakers.

---
**References:**
- [Watch the full AI Agent Clinic Episode 1](https://www.youtube.com/live/md2VFN6SojQ)
- [Titanium Repo](https://github.com/ai-agent-clinic/google-agent-clinic)
- [ADK Documentation](https://cloud.google.com/agent-builder/docs/overview)
