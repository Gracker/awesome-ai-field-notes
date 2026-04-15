---
title: '从 MCP 到 SKILL（II）：把调用层补齐'
sidebar: false
---

::: info
[← 返回行业观察](/industry)
:::

# 从 MCP 到 SKILL（II）：把调用层补齐

> AI 实践：从 MCP 到 SKILL（II）：把调用层补齐

🔗 [原文链接](https://x.com/jolestar/status/2027717523379261489) | @jolestar |  | ⭐⭐⭐⭐⭐ 5 ⭐5 5/5 📅 2026-03-01

`mcp` `agent` `skill` `coding` `context-management` `github`

---

## 从 MCP 到 SKILL（II）：把调用层补齐

**来源：** x - jolestar (2026-03-01)

**分类：** industry  
**标签：** mcp, agent, skill, coding, context-management, github

---

## 中文摘要

从 MCP 到 SKILL（II）：把调用层补齐
我在《从 MCP 到 SKILL：关于 Agent 扩展机制的思考 https://x.com/jolestar/status/2011461813767155828 》里提过一个很直觉的分工：
- MCP（Model Context Protocol）更像“标准插头”，解决连接标准化
- SKILL 更像“操作手册 + 工作流”，解决编排、状态与闭环
当时我以为，这两者拼起来就会很自然。
但真把它落到工程里，很快会发现：缺的不是理念，而是最后那一段“可执行、可迁移、对 Agent 友好”的、适合写进 SKILL 的通用调用入口。
首先没有一个通用的 SKILL 友好的 MCP CLI。理论上可以用 `curl` 调 MCP HTTP，但对 Agent 来说参数、认证、错误处理都太复杂，稳定性差。于是很多服务放弃了 MCP，直接退化成“纯 REST 接口”。
SKILL 里用 curl 来演示当然能跑通，但这种方式可维护性差：接口变化 AI 无法感知，接口数量多了也很难展示与发现。

---

## 详细内容

基于原始链接的文章内容将在此处展开。由于网络访问限制，此处提供基于摘要的扩展分析：

### 核心观点

AI 实践：从 MCP 到 SKILL（II）：把调用层补齐

### 技术要点

openclaw：AI 实践：从 MCP 到 SKILL（II）：把调用层补齐

### 相关背景

此文章涉及 industry 领域的重要发展，对理解当前 AI 技术趋势具有重要价值。

---

*内容生成时间：2026-04-11T02:15:18.554213*
