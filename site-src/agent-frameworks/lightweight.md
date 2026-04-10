# 极简实现

Lightweight / Minimal — 1 条活跃资源

### [Pi: The Minimal Agent Within OpenClaw](https://lucumr.pocoo.org/2026/1/31/pi/) 
by @Armin Ronacher (2026-02-26) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**OpenClaw 底层 Pi 的极简哲学：让 Agent 自己扩展自己**

OpenClaw 底层的编码 Agent Pi 详解。Pi 由 Mario Zechner 开发，理念是让 Agent 自己扩展自己而非下载扩展。刻意不支持 MCP（可用 mcporter 桥接），强调代码生成和运行。核心设计：会话是树结构（可分支/回退/导航），内置热重载让 Agent 自己写代码→重载→测试循环。多模型支持、可移植性优先。扩展可注册工具给 LLM 调用，也可渲染自定义 TUI 组件。
 `pi` `openclaw` `coding-agent` `mcp` `session-tree` `hot-reload`

---