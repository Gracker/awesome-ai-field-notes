---
title: "从 MCP 到 SKILL（II）：把调用层补齐"
source: "field-notes"
entry_id: "re3mcqtn"
language: "zh"
---

# 从 MCP 到 SKILL（II）：把调用层补齐

**By @jolestar**

我在《从 MCP 到 SKILL：关于 Agent 扩展机制的思考》里提过一个很直觉的分工：

- MCP（Model Context Protocol）更像"标准插头"，解决连接标准化
- SKILL 更像"操作手册 + 工作流"，解决编排、状态与闭环

当时我以为，这两者拼起来就会很自然。

但真把它落到工程里，很快会发现：缺的不是理念，而是最后那一段"可执行、可迁移、对 Agent 友好"的、适合写进 SKILL 的通用调用入口。

首先没有一个通用的 SKILL 友好的 MCP CLI。理论上可以用 `curl` 调 MCP HTTP，但对 Agent 来说参数、认证、错误处理都太复杂，稳定性差。于是很多服务放弃了 MCP，直接退化成"纯 REST 接口"。

SKILL 里用 curl 来演示当然能跑通，但这种方式可维护性差：接口变化 AI 无法感知，接口数量多了也很难展示与发现。

所以问题变成了：SKILL 和 CLI 配合得很好，但不可能每个服务都自己带一个高质量 CLI。那能不能有一个通用 CLI？

MCP 的 schema 本身已经足够标准了，如果我们把"CLI 的渐进式披露（progressive disclosure）"复刻出来，这个通用 CLI 就能成立。

于是就有了 `uxc`。

`uxc` 的定位是"统一协议调用 CLI"（Universal X-Protocol CLI），通过渐进式披露：把 schema 接口变成可交互的 CLI。

MCP（以及其它协议）的 schema 往往很大。如果你把它一次性塞进 Agent 的工具上下文，很容易撞上上下文预算（context budget）。而 uxc 的模式是：

```bash
uxc <host> -h
uxc <host> <operation_id> -h
uxc <host> <operation_id> key=value
uxc <host> <operation_id> '{...}'
```

这让"能力发现"变成按需加载：只有在需要的时候才展开某个 tool 的输入输出。

为了方便 AI 使用，还可以通过 `uxc link`：把 endpoint 固化成"稳定的命令名"。

比如：

```bash
uxc link notion-mcp-cli
notion-mcp-cli -h
```

于是后续 SKILL 里就可以像调用"专用 Notion CLI"一样调用：

```bash
notion-mcp-cli notion-search query=ai
```

另外 uxc 默认输出结构化的 JSON envelope，成功/失败的 shape 相对固定，Agent 更容易做自动化判断。认证上 uxc 用 credential + binding 把 endpoint 与凭证的匹配规则外部化，这些细节不必散落在提示词里，也不需要让 AI Agent 填充。

业界也有一些动态 MCP 的方案，但和 SKILL 组合时会遇到困难：

1. SKILL 中没办法"自动给 agent 增加 MCP 配置"
2. MCP server 的名字在不同用户设备上配置不一样，SKILL 无法假定

所以 uxc 不依赖本地配置的 server 名字，直接用 host/endpoint。需要"起名字"时，用 `uxc link` 把 endpoint 固化成一个本地 shortcut，在 SKILL 里就可以稳定引用。

## 小结

我目前更倾向的分层是：

- MCP：标准化能力描述和服务（schema）
- uxc：统一的调用层（渐进披露 + auth binding + link）
- SKILL：把调用嵌入可闭环的工作流

这三层都齐了，MCP 和 SKILL 就可以真的"拼起来"，并且拼出来的东西是可迁移、可维护的。
