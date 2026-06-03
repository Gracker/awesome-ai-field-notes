# Scaling Managed Agents: Decoupling the brain from the hands
# 扩展托管智能体：将大脑与双手解耦

> **来源 / Source**: Anthropic Engineering  
> **URL**: https://www.anthropic.com/engineering/managed-agents  
> **发表日期 / Date**: 2026年4月8日  
> **评分 / Score**: ⭐⭐⭐⭐⭐ 5/5  
> **标签 / Tags**: agents, infrastructure, anthropic, managed-agents, architecture, scale

---

## English Version

A running topic on the Engineering Blog is how to build effective agents and design harnesses for long-running work. A common thread is that harnesses encode assumptions about what Claude can't do on its own. However, those assumptions need to be frequently questioned because they can go stale as models improve.

We built **Managed Agents**: a hosted service in the Claude Platform that runs long-horizon agents through a small set of interfaces meant to outlast any particular implementation.

### The Problem: Pets vs Cattle

We started by placing all agent components into a single container. But by coupling everything into one container, we ran into an old infrastructure problem: we adopted a **pet**. If a container failed, the session was lost. If a container was unresponsive, we had to nurse it back to health.

### Decouple the Brain from the Hands

The solution was to decouple what we thought of as the "brain" (Claude and its harness) from the "hands" (sandboxes and tools) and the "session" (the log of session events).

The harness leaves the container. Decoupling the brain from the hands meant the harness no longer lived inside the container. It called the container the way it called any other tool: `execute(name, input) → string`. The container became **cattle**. If the container died, the harness caught the failure as a tool-call error and passed it back to Claude.

### Many Brains, Many Hands

Decoupling the brain from the hands means that containers are provisioned by the brain via a tool call only if they are needed. Using this architecture, **p50 TTFT dropped ~60% and p95 dropped over 90%**.

Decoupling also enables each brain to connect to **many hands**—Claude must reason about many execution environments and decide where to send work. The interface supports any custom tool, any MCP server, and our own tools.

### Key Insight

The challenge we faced is an old one: how to design a system for "programs as yet unthought of." Operating systems lasted decades by virtualizing hardware into abstractions general enough for programs that didn't exist yet. With Managed Agents, we aimed to design a system that accommodates future harnesses, sandboxes, or other components around Claude.

---

## 中文版

工程博客一直在讨论如何构建有效的智能体和为长期运行的工作设计 harness。一个共同的主题是：harness 编码了关于 Claude 自身无法做什么的假设。然而，这些假设需要经常质疑，因为它们会随着模型的改进而变得过时。

我们构建了**托管智能体（Managed Agents）**：Claude Platform 中的一项托管服务，通过一组小型接口运行长期运行的智能体，这些接口旨在超越任何特定实现。

### 问题：宠物与 cattle

我们最初将所有智能体组件放入单个容器中。但通过将所有内容耦合到一个容器中，我们遇到了一个经典的基础设施问题：我们养了一只**宠物**。如果容器失败，会议话丢失。如果容器无响应，我们必须对其进行修复。

### 将大脑与双手解耦

解决方案是将我们所谓的"大脑"（Claude 及其 harness）与"双手"（沙盒和工具）以及"会话"（会话事件的日志）解耦。

Harness 离开容器。将大脑与双手解耦意味着 harness 不再位于容器内。它通过调用任何其他工具的方式调用容器：`execute(name, input) → string`。容器变成了 **cattle**。如果容器死亡，harness 将失败捕获为工具调用错误并将其传回给 Claude。

### 多个大脑，多双手

将大脑与双手解耦意味着容器仅在需要时由大脑通过工具调用配置。使用这种架构，**p50 TTFT 下降约 60%，p95 下降超过 90%**。

解耦还使每个大脑能够连接到**多双手**——Claude 必须对多个执行环境进行推理，并决定将工作发送到哪里。该接口支持任何自定义工具、任何 MCP 服务器以及我们自己的工具。

### 关键洞察

我们面临的挑战是一个古老的挑战：如何为一个"尚未被想到的程序"设计系统。操作系统通过将硬件虚拟化为足够通用的抽象概念来延续数十年，适用于尚不存在的程序。有了托管智能体，我们旨在设计一个能够适应围绕 Claude 的未来 harness、沙盒或其他组件的系统。

---

> **延伸阅读 / Further**: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
