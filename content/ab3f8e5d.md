# fx: Tiny, open, native coding agent

- **ID**: ab3f8e5d
- **原文链接**: https://fx.sh
- **作者**: fx contributors
- **来源类型**: blog
- **标签**: coding-agent, cli, zig, wasm, open-source
- **质量评分**: 3/5
- **抓取时间**: 2026-08-20T15:44:49Z

---

## 中文导读

Zig 编写的实验性 coding agent harness v0.0.4，Apache-2.0 开源，定位是 Unix shell 风格的 agent CLI 而非 IDE 式 TUI。关键数字：6.39 MiB 单二进制、冷启动 10 微秒、常驻内存个位数 MiB、极简系统提示压低 TTFT 与 token 成本。原生支持 WASM 编译（fx.wasm），可在 Safari 27+ 与 Chrome 浏览器内直接运行，网络栈经浏览器 fetch 委托。扩展走 skills、plugins、MCPs，模型无关，本地模型或网关均可接入。

## 为什么值得关注

6.39MiB、10 微秒冷启动的 Zig 版 agent CLI：把 coding agent 做成可嵌入的 Unix 工具

## 原文摘录 (English Excerpt)

fx is a coding agent harness and CLI written in Zig, optimized for research and embeddability as part of larger systems.

It focuses on minimalism and performance across the board, from system prompt design, to its tools, feature set, and 6.39mib binary.

For end users, its CLI output style and form factor aims to be closer to a Unix shell than a heavy "IDE in the terminal" TUI.

It's open source (Apache-2.0), model-agnostic, and suitable for both local and cloud inference.

\*\*\*

## Tiny ~6mb binary

Designed for instant installation and embedding in resource constrained environments and agent sandboxes.

## Instant time to prompt

fx cold starts in 10µs and does no unnecessary work or I/O prior to accepting user input, making it ideal for programmatic use.

## Wasm support

Optimal fx.wasm builds produced by the Zig toolchain, which further reduce fx's size, making the network stack

## Obsidian 证据

- 来源 digest: ClawFeed 24h 一览 2026-08-20（2026-08-20，评分 7.8）
- 原文经 opencli web read / opencli arxiv paper 抓取核对，关键数字与摘要均锚定抓取内容。
