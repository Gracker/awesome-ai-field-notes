---
title: 'Launching Claude Managed Agents'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# Launching Claude Managed Agents

> Anthropic 官方托管 Agent 基础设施，大脑/手/记忆三层解耦架构

🔗 [原文链接](https://x.com/RLanceMartin/status/2041927992986009773) | @RLanceMartin | 🌐 | ⭐⭐⭐⭐⭐ 5 ⭐5 5/5 📅 2026-04-10

`claude` `managed-agents` `anthropic` `agent-sdk` `infrastructure` `cloud-agent`

---

## English

Launching Claude Managed Agents

Anthropic officially launched "Claude Managed Agents" in public beta on April 8, 2026. This new offering is a managed infrastructure service designed to simplify the development and deployment of AI agents powered by Claude models, removing the need for developers to manage underlying infrastructure.

Claude Managed Agents provides features such as secure sandboxing, long-running autonomous sessions, multi-agent coordination, and governance with scoped permissions and execution tracing. It is a suite of composable APIs that handles the operational complexity of running agents at scale, including execution environment, authentication, credential management, and tooling. Anthropic claims it can help enterprises "go from prototype to launch in days rather than months" and build agents "10x faster."

The service is priced on consumption, with standard Claude API token rates plus an additional charge of $0.08 per session-hour for active runtime. Early adopters include companies like Notion, Asana, Rakuten, Sentry, and Atlassian.

## Core Concepts

* **Agent (versioned config)**: Pre-built, configurable agent harness running on managed infrastructure
* **Environment (sandbox template)**: Secure sandbox template for agent execution
* **Session (stateful run)**: Stateful running instance with memory and execution context

## Usage Patterns

* **Event-triggered**: Agents activated by external events
* **Scheduled**: Agents running on predefined schedules  
* **Fire-and-forget**: One-off execution tasks
* **Long-horizon**: Extended duration autonomous tasks

While "RLanceMartin" is not directly credited with the launch, a "Lance's Blog" is mentioned in the context of "Agent design patterns" and discussions around long-running agents, suggesting an individual contributing to the broader conversation and understanding of AI agent development.

## 中文

英文内容翻译（此处需要实际的翻译服务）
