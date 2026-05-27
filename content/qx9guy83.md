---
title: "How agents can use filesystems for context engineering"
source: "https://www.langchain.com/blog/how-agents-can-use-filesystems-for-context-engineering"
category: "agents/frameworks"
tags: ["ai", "context-engineering", "filesystems", "langchain"]
date: "2026-05-26"
quality_score: 4
---

# How agents can use filesystems for context engineering

> 原文：[LangChain Blog](https://www.langchain.com/blog/how-agents-can-use-filesystems-for-context-engineering) | 作者：Nick Huang | 抓取时间：2026-05-27

---

## 什么是 Context Engineering

> **EN:** A view of context engineering.

现代 agent 工程师的关键任务：通过 context engineering 的 lens 看待工作。

Agent 通常可以访问大量 context（所有支持文档、所有代码文件等）。为了回答 incoming question，agent 需要一些重要的 context。

Agent 的 context engineering 可能在以下情况"失败"：

1. **Agent 需要的 context 不在 total context 中** → agent 无法成功
2. **Agent 检索的 context 不能 encapsulate 所需的 context** → agent 无法正确回答
3. **Agent 检索的 context 远大于需要的 context** → agent 浪费（时间和 tokens）

我们的工作：**让 agent 检索的 context 成为所需信息的最小超集**（fit red to green）。

---

## 文件系统如何让 agent 变得更好

> **EN:** How can a filesystem make an agent better?

**Filesystem 提供了一个单一接口，通过它 agent 可以灵活地存储、检索和更新无限量的 context。**

### 场景一：Token 过多（Retrieved >> Necessary）

> **EN:** Too many tokens.

不用对话历史来保存所有工具调用结果和笔记，agent 可以将这些写入 filesystem，然后有选择地查找相关信息。

Manus 是最早公开谈论这种方法的人之一：

- Web 搜索返回 10k tokens 的原始内容
- 如果放入消息历史，所有 10k tokens 都会在整个对话中 sitting there
- 如果 offload 到 filesystem，agent 可以智能地 grep 搜索某些关键词，然后只将必要的 context 读入对话

### 场景二：需要大量 Context（Necessary > Context Window）

> **EN:** Needs large amounts of context.

Filesystem 为 LLM 动态存储和提取更多信息提供了很好的抽象：

- **Long horizon answers**：Agent 需要制定计划然后 follow it。通过将计划写入 filesystem，agent 可以在以后 pull 此信息回到上下文窗口
- **Subagents 并行工作**：当 subagents 做工作和学习时，不是 just replying with their learnings，而是可以将知识写入 filesystem（minimize the game of telephone）
- **大量 instructions**：不是将所有 instructions stuff into the system prompt，可以将它们存储为文件并让 agent 动态读取

### 场景三：Finding Niche Information（Retrieved ≠ Necessary）

> **EN:** Finding niche information.

Semantic search 在某些用例中可能有效，但对于某些类型的文档（如 technical API reference、code files），semantic 可能由于文本中语义信息不足而 placed very poorly。

Filesystems 提供了替代方案，让 agent 使用 `ls`、`glob` 和 `grep` 工具智能搜索 context：

- 当前的模型经过专门训练来理解 traversing filesystems
- 信息通常已经逻辑结构化（目录）
- `glob` 和 `grep` 允许 agent 不仅隔离特定文件，还允许隔离特定的行和特定的字符
- `read_file` 工具允许 agent 指定从文件中读取哪些行

### 场景四：Learning Over Time（Total Context ≠ Necessary Context）

> **EN:** Learning over time.

Agent 出错的一个大原因是它们缺少相关 context。改进 agent 的一个好方法是确保它们可以访问正确的 context。

一个 agent 的 instructions（或 skills）与它可能想要使用的任何其他 context 没有区别。**Filesystem 可以作为 agent 存储和更新自己 instructions 的地方。**

在用户反馈后，agent 可以立即写入自己的文件并记住一条重要信息。这对于快速的一次性事实很好，特别是可能特定于用户的内容，如他们的名字、email 或其他偏好。

---

## 总结

> **EN:** Summary.

Filesystem 为 agent 提供了：

| 能力 | 说明 |
|------|------|
| **Scratchpad** | 用于大型 context 的临时存储 |
| **Long-horizon Memory** | 跨 session 保存计划和状态 |
| **Shared Workspace** | Subagents 之间共享知识 |
| **Dynamic Instructions** | Agent 可以随时间更新自己的 skills |
| **Structured Search** | 通过 ls/glob/grep 而非 semantic search 查找 niche 信息 |

---

*相关资源：[Deep Agents (Python)](https://github.com/langchain-ai/deepagents), [Deep Agents (TypeScript)](https://github.com/langchain-ai/deepagentsjs)*
