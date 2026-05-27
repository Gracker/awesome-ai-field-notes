---
title: "Scaling Managed Agents: Decoupling the brain from the hands"
source: "https://www.anthropic.com/engineering/managed-agents"
category: "agents/frameworks"
tags: ["ai", "agents", "anthropic", "architecture"]
date: "2026-05-26"
quality_score: 5
---

# Scaling Managed Agents: Decoupling the brain from the hands

> 原文：[Anthropic Engineering Blog](https://www.anthropic.com/engineering/managed-agents) | 抓取时间：2026-05-27

---

## 核心问题：如何为"尚未想到的程序"设计系统

> **EN:** The challenge we faced is an old one: how to design a system for "programs as yet unthought of."

 decades ago, operating systems solved this problem by virtualizing hardware into abstractions—process, file—general enough for programs that didn't exist yet.

Managed Agents 遵循相同的模式：虚拟化 agent 的各个组件：**session**（append-only log）、**harness**（调用 Claude 并路由工具调用的循环）、**sandbox**（Claude 运行代码和编辑文件的执行环境）。

---

## 不要收养宠物

> **EN:** Don't adopt a pet.

我们最初将所有 agent 组件放入单个容器，意味着 session、agent harness 和 sandbox 共享一个环境。这种耦合带来了问题：

- 服务器变成了"宠物"——如果容器失败，session 就丢失
- 如果容器无响应，必须 nursing it back to health
- 调试无响应 stuck sessions 非常困难——WebSocket 事件流无法告诉我们失败从哪里产生

### 解决方案：Decouple the brain from the hands

将"brain"（Claude 和 harness）与"hands"（sandboxes 和 tools）以及"session"（事件日志）分离：

```
execute(name, input) → string
```

容器变成了"cattle"。如果容器死了，harness 捕获失败作为 tool-call 错误并传回给 Claude。如果 Claude 决定重试，可以重新初始化一个新容器。

### 恢复 Harness 失败

> **EN:** Recovering from harness failure.

因为 session log 位于 harness 外部，harness 中没有任何东西需要 survive crash。当一个 harness 失败时，可以用 `wake(sessionId)` 启动一个新的，通过 `getSession(id)` 获取事件日志，然后从最后一个事件恢复。

---

## 安全边界

> **EN:** The security boundary.

在耦合设计中，任何 Claude 生成的 untrusted code 都在与 credentials 相同的容器中运行——prompt injection 只需要说服 Claude 读取自己的环境。结构性修复：确保 tokens 永远无法从 Claude 生成代码的 sandbox 中 reach。

**两个模式：**
1. Auth 可以与 resource 捆绑或保存在 vault outside the sandbox
2. 对于 Git，使用每个 repository 的 access token 在 sandbox 初始化期间 clone repo 并 wire 到本地 git remote

---

## Session 不是 Claude 的上下文窗口

> **EN:** The session is not Claude's context window.

长 horizon 任务通常超过 Claude 的上下文窗口长度，标准解决方法都涉及关于保留什么的不可逆决策。

在 Managed Agents 中，session 提供了一个存在于 Claude 上下文窗口之外的上下文对象：`getEvents()` 接口允许 brain 从事件流中选择位置切片。

任何 fetch 的 events 也可以在传递给 Claude 上下文窗口之前在 harness 中转换。这些转换可以包括：
- 上下文组织以实现高 prompt cache hit rate
- 上下文工程

---

## 多 brain，多 hands

> **EN:** Many brains, many hands.

**Many brains：** 将 brain 从容器中分离后解决了早期客户投诉。当团队希望 Claude 处理其 VPC 中的资源时，只需 bridge their network with ours。

**Many hands：** 我们还希望能够将每个 brain 连接到多个 hands。在实践中，这意味着 Claude 必须 reasoning about 许多执行环境并决定在哪里发送 work——比在单个 shell 中操作更困难的认知任务。

因为没有 hand 与任何 brain 耦合，brains 可以相互传递 hands。

---

## 性能提升

> **EN:** Performance improvements.

使用这种架构，我们的 **p50 TTFT 下降了约 60%，p95 下降了超过 90%**。

扩展到 many brains 只是意味着启动 many stateless harnesses，并在需要时才连接它们到 hands。

---

## 结论

> **EN:** Conclusion.

Managed Agents 是一个 meta-harness，与其说是关于特定的 harness，不如说是关于允许许多不同 harness 的通用接口。我们对 Claude 周围的接口做出判断：

- **state manipulation**（session）
- **computation**（sandbox）
- **ability to scale to many brains and many hands**

---

*作者：Lance Martin, Gabe Cemaj, Michael Cohen*
