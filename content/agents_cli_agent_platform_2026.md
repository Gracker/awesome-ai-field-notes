---
title: "Agents CLI in Agent Platform: create to production in one CLI"
date: 2026-04-22
source: google
category: agents
tags: [Agents-CLI, Agent-Platform, Gemini-CLI, Claude-Code, deployment, Google-Cloud, ADK]
quality_score: 4
status: fetched
---

## Agents CLI in Agent Platform：从原型到生产，一站式 CLI 完成

**发布日期：2026年4月22日 | 来源：Google Cloud Blog**

### 概述

AI Agent 正从实验性脚本过渡到生产服务。但尽管模型越来越智能，构建、评估和部署 Agent 所需的基础设施仍然碎片化严重。

今天，我们发布 Agents CLI in Agent Platform——Google Cloud 上 Agent 开发生命周期（ADLC）的统一编程骨干。

### 用 Agent 构建 Agent

Agent 开发最大的障碍是上下文过载。当您的编码 Agent 必须猜测分散的云组件如何组合时，会导致无限循环和 token 浪费。

借助 Agents CLI，只需运行一个命令即可将捆绑技能直接注入编码环境：

```bash
# 安装 CLI
uvx google-agents-cli setup
```

例如，您可以提示您的编码 Agent："我想创建一个旅行费用 Agent，帮助我自动批准 50 美元以下的费用，并要求人工审批超过 50 美元或任何可能异常的费用。"

```bash
# 您的编码助手使用自动默认值无缝搭建项目
agents-cli create finance-agent -y --deployment-target agent_runtime

# 进入目录
cd finance-agent
```

### 本地模拟与严格评估

Agents CLI 可以运行严格的评估测试框架：

```bash
# 根据真实数据集运行评估
agents-cli eval run

# 比较两次运行的轨迹评分和指标
agents-cli eval compare evals/run_v1.json evals/run_v2.json
```

### 无缝部署到生产环境

从本地原型到安全的全球分布式服务不应该需要 70 天。Agents CLI 可以自动化整个部署阶段：

```bash
# 配置生产基础设施
agents-cli infra single-project

# 将 Agent 部署到 Google Cloud
agents-cli deploy

# 将已部署的 Agent 注册到 Gemini Enterprise 进行分发
agents-cli publish gemini-enterprise
```

### 人类意图 + Agent 执行

虽然 Agents CLI 针对 Agent 消费进行了优化（Agent 模式），但 CLI 完全支持人类模式。

---
**参考链接：**
- [Agents CLI GitHub 仓库](https://github.com/google/agents-cli)
- [文档](https://google.github.io/agents-cli/)

---

## Agents CLI in Agent Platform: create to production in one CLI

**Published: April 22, 2026 | Source: Google Cloud Blog**

### Overview

AI agents are transitioning from experimental scripts to production services. But while models get smarter, the infrastructure required to build, evaluate, and deploy them remains stubbornly fragmented.

Today, we introduce Agents CLI in Agent Platform—the unified programmatic backbone for the Agent Development Lifecycle (ADLC) on Google Cloud.

### Build Agents with Agents

The biggest hurdle in agent development is context overload. When your coding agent has to guess how disparate cloud components fit together, it leads to endless loops and token waste.

With Agents CLI, you simply run one command to inject bundled skills directly into your coding environment:

```bash
# Installing the CLI
uvx google-agents-cli setup
```

For example, you could prompt your coding agent: "I want to create a travel expense agent that can help me auto-approve expenses under $50 and require HITL to approve anything over $50."

```bash
# Your coding agent seamlessly scaffolds the project using automatic defaults
agents-cli create finance-agent -y --deployment-target agent_runtime

# Move into the directory
cd finance-agent
```

### Local Simulation and Rigorous Evaluation

Agents CLI can run rigorous evaluation harnesses:

```bash
# Run evaluations against your ground-truth datasets
agents-cli eval run

# Compare the trajectory scoring and metrics of two runs
agents-cli eval compare evals/run_v1.json evals/run_v2.json
```

### Seamless Deployment to Production

Going from a local prototype to a secure, globally distributed service should not take 70 days. Agents CLI can automate the entire deployment phase:

```bash
# Provision the production infrastructure
agents-cli infra single-project

# Ship the agent to Google Cloud
agents-cli deploy

# Register the deployed agent with Gemini Enterprise for distribution
agents-cli publish gemini-enterprise
```

### Human Intent + Agent Execution

While the Agents CLI is optimized for agent consumption (Agent Mode), the CLI fully supports a Human Mode.

---
**References:**
- [Agents CLI GitHub Repository](https://github.com/google/agents-cli)
- [Documentation](https://google.github.io/agents-cli/)
