## English

# Scaling Managed Agents: Decoupling the brain from the hands

**Source:** Anthropic Engineering Blog
**URL:** https://www.anthropic.com/engineering/managed-agents
**Published:** Apr 08, 2026

## Core Problem

Harnesses encode assumptions about what Claude can't do on its own. Those assumptions go stale as models improve. Example: Claude Sonnet 4.5 had "context anxiety" — we added context resets. Then Opus 4.5 came out and the behavior was gone. The resets had become dead weight.

## Solution: Virtualized Agent Components

Managed Agents virtualizes three components:
- **Session** — append-only log of everything that happened
- **Harness** — loop that calls Claude and routes tool calls
- **Sandbox** — execution environment where Claude runs code and edits files

Each can fail or be replaced independently. The interfaces outlast any particular implementation.

## Don't Adopt a Pet

In the initial design, all components shared a single container → the server became a "pet." If a container failed, the session was lost. Nursing containers back to health was painful.

**Decoupling the brain from the hands:**
- Harness no longer lives inside the container
- Container called via `execute(name, input) → string` — like any other tool
- Container became "cattle" — if it dies, harness catches failure as tool-call error, Claude retries with new container provisioned via `provision({resources})`

## Security Boundary

In coupled design, untrusted Claude-generated code ran in same container as credentials → prompt injection just needed to convince Claude to read its own environment.

Structural fix: tokens are never reachable from the sandbox where Claude's generated code runs. Auth bundled with resource or held in vault outside sandbox. Git tokens wired into local git remote during sandbox initialization. MCP OAuth tokens stored in secure vault, fetched by dedicated proxy.

## Session ≠ Context Window

The session provides durable context outside Claude's context window. `getEvents()` allows brain to interrogate context by selecting positional slices of the event stream. The harness transforms fetched events before passing to Claude's context window.

## Many Brains, Many Hands

- **TTFT improvement:** p50 dropped ~60%, p95 dropped >90% by decoupling brain from hands
- **Scaling:** many brains just means many stateless harnesses, connected to hands only if needed
- **Many hands:** any tool via `execute(name, input) → string` — harness doesn't know if sandbox is container, phone, or Pokémon emulator

## Key Quote

"Harnesses encode assumptions that go stale as models improve. Managed Agents is built around interfaces that stay stable as harnesses change."


## 中文

# 规模化托管 Agent：将大脑与双手解耦

**来源：** Anthropic 工程博客
**链接：** https://www.anthropic.com/engineering/managed-agents
**发布日期：** 2026年4月8日

## 核心问题

Harness 对 Claude 无法独立完成的事情做了假设。这些假设会随着模型改进而过时。例如：Claude Sonnet 4.5 有"上下文焦虑" — 我们添加了上下文重置。后来 Opus 4.5 出现，这种行为消失了。重置变成了死代码。

## 解决方案：虚拟化 Agent 组件

Managed Agents 将三个组件虚拟化：
- **Session** — 所有事件的仅追加日志
- **Harness** — 调用 Claude 并路由工具调用的循环
- **Sandbox** — Claude 运行代码和编辑文件的执行环境

每个组件都可以独立失败或替换。接口比任何特定实现都更持久。

## 不要养宠物

在最初的设计中，所有组件共享一个容器 → 服务器变成了"宠物"。如果容器失败，session 就丢失了。把容器护理回健康状态是痛苦的。

**将大脑与双手解耦：**
- Harness 不再位于容器内部
- 通过 `execute(name, input) → string` 调用容器 — 和其他工具一样
- 容器变成了"牲口" — 如果死了，harness 将失败捕获为工具调用错误，Claude 重试，新容器通过 `provision({resources})` 初始化

## 安全边界

在耦合设计中，不受信任的 Claude 生成代码在与凭证相同的容器中运行 → 提示注入只需说服 Claude 读取自己的环境即可。

结构性修复：token 永远无法从 Claude 生成代码运行的 sandbox 访问。Auth 与资源捆绑或保存在 sandbox 外的保险库中。Git token 在 sandbox 初始化期间连接到本地 git remote。MCP OAuth token 保存在安全保险库中，由专用代理获取。

## Session ≠ Context Window

Session 在 Claude 的上下文窗口之外提供持久上下文。`getEvents()` 允许大脑通过选择事件流的positional slice 来查询上下文。Harness 在传递到 Claude 上下文窗口之前转换获取的事件。

## 多脑多手

- **TTFT 改进：** 通过将大脑与双手解耦，p50 下降约 60%，p95 下降超过 90%
- **扩展：** 多个大脑只需要多个无状态 harness，仅在需要时连接到手
- **多手：** 任何工具通过 `execute(name, input) → string` — harness 不知道 sandbox 是容器、手机还是宝可梦模拟器

## 关键引言

"Harness 对 Claude 无法独立完成的事情做了假设，这些假设会随着模型改进而过时。Managed Agents 围绕在 harness 变化时保持稳定的接口构建。"

