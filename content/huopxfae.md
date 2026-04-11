## 如何从零开始写一个 OpenClaw -- 关于我用 Rust 写一只🦀🦞(CrabClaw)的开发手记

### English
This article details the development process of building CrabClaw, an OpenClaw-compatible agentic coding toolchain written in Rust. It covers the motivations, technical implementation, and key features of this Rust-based alternative to Node.js OpenClaw.

### 中文
这篇文章详细介绍了开发 CrabClaw 的过程，这是一个用 Rust 编写的、与 OpenClaw 兼容的代理式编码工具链。文章涵盖了开发动机、技术实现和这个基于 Rust 的 OpenClaw 替代方案的关键特性。

#### 主要特性
- **多通道支持**：CLI、交互式 REPL 和 Telegram 机器人，带有白名单访问控制
- **模型无关性**：支持 OpenAI 兼容接口、原生 Anthropic 消息 API 和 Codex 响应 API
- **AgentLoop 统一抽象**：在单个 handle_input 调用中完成路由 → 模型 → 工具 → 带操作
- **技能引擎**：自动发现 .agent/skills/ 并将它们作为 LLM 可调用工具桥接
- **Shell 执行**：通过 ,git status 或 shell.exec 工具运行 shell 命令，具有故障自纠错
- **文件操作**：file.read、file.write、file.edit、file.list、file.search，具有工作区沙箱安全
- **会话记录系统**：只追加的 JSONL 会话记录，带有锚点、搜索、交接和上下文截断

#### 技术架构
- 系统采用分层设计：配置覆盖 > .agent/system-prompt.md > 内置默认
- 支持多种提供商模式：OpenAI、Anthropic、Codex
- 具有渐进式工具视图和高效的令牌使用
- 支持智能工具调用循环（最多 5 次自主推理）

#### 开发者体验
- 安装稳定 Rust 工具链
- 支持多种认证方式：API Key 或 OAuth（ChatGPT Plus/Pro 订阅）
- 提供多种运行模式：交互式 REPL、一次性 CLI、Telegram 机器人
- 具备完整的测试套件和架构文档

这篇文章为想要从零开始构建类似 OpenClaw 系统的 Rust 开发者提供了详细的实践指南。
