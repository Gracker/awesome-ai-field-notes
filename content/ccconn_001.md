# cc-connect: Bridge local AI coding agents to messaging platforms

- **ID**: ccconn_001
- **原文链接**: https://github.com/chenhg5/cc-connect
- **作者**: chenhg5
- **平台**: GitHub
- **分类**: agents/frameworks
- **标签**: coding-agent, messaging-bridge, claude-code, feishu, telegram, wechat, multi-agent
- **质量评分**: 4/5
- **抓取时间**: 2026-07-02T12:24:35
- **抓取方式**: opencli web read

---

## 当前最完整的本地编程 Agent 聊天平台桥接方案，零公网 IP 要求让移动端控制 AI 编码助手成为现实

---

## English (Original)

**Control your local AI agents from any chat app. Anywhere, anytime.**

cc-connect bridges AI agents running on your machine to the messaging platforms you already use.
Code review, research, automation, data analysis — anything an AI agent can do,
now accessible from your phone, tablet, or any device with a chat app.

[![CC-Connect Architecture](https://github.com/chenhg5/cc-connect/raw/main/docs/images/connector.png)](https://github.com/chenhg5/cc-connect/blob/main/docs/images/connector.png)

## 🆕 What’s New in v1.3.3

[](#-whats-new-in-v133)

First stable of the 1.3.3 series — stabilizes beta.1 → beta.5 (≈ 235 PRs since v1.3.2) plus 7 post-beta fixes. Highlights:

-   **New agents** — Devin CLI, Google Antigravity (`agy`), GitHub Copilot CLI as first-class agents (#672, #1123, #865). Hardened Cursor / OpenCode / Qoder / Kimi / Pi coverage.
-   **Platform expansion** — QQ (OneBot) file send & receive (#323), QQ Bot inline keyboards (#1131), WeCom `SendFile` in WebSocket (#1199), Feishu audio + video native media (#1202), Slack Assistant API (#844), MAX webhook delivery (#818), DingTalk @mentions / richText / image / file inbound (#1188, #828, #1357), broader Weibo DM, WPS Xiezuo (金山协作).
-   **Long-running turn hardening** — new `max_turn_time_mins` wall-clock cap with soft-stop + force-kill + auto-resume so a long bash / test command can no longer lock a session indefinitely (#1091).
-   **New core commands** — `/timer` (one-shot delayed task), `/cancel` (interrupt current turn), `/ps` (replaces `/btw`, kept as alias), `cron add --silent`, agent-driven TTS.
-   **Multi-user / permissions** — reply-to-unauthorized-IM-senders option, `@Bot/permit` ≡ `/permit` keyword matching, Bridge requires token when enabled.
-   **Provider ecosystem** — NekoCode, VisionCoder, AIHubMix, MiniMax M3 presets; Claude Code 1M-context Opus + `append_system_prompt` + PermissionRequest hooks; Codex `request_user_input` app-server events; configurable `shell` + shell profile for `exec`.
-   **Observability** — blackbox testing framework (P0/P1/P2 + config-switch matrix), CUJ test framework, provider-resume regression suite for codex/opencode/kimi, Pi context-usage reporter in reply footer.

⚠️ **Behavior changes (action may be required)**: Telegram/Discord `progress_style` defaults to `compact` (set `legacy` to revert); QQ Bot default `intents` now include `INTERACTION_CREATE` (custom values must include `1<<26`); DingTalk `msgtype=file` inbound now reaches the agent; engine permission keywords are @mention-tolerant; `reset_on_idle_mins` defaults to 30 min; Bridge with no token configured refuses to start. See `changelogs/v1.3.3.md` for the full themed summary.

No breaking changes. Coming from a v1.3.3-beta.\*, this is a small fix-only upgrade.

---

## 中文摘要

cc-connect 是一个把本地 AI 编程 Agent 桥接到飞书、钉钉、Telegram、Slack、Discord、LINE、企业微信、QQ、微博、Matrix 等 11+ 个聊天平台的开源项目，已稳定到 v1.3.3。用户无需公网 IP 即可在手机上通过聊天工具远程控制 Claude Code、Codex、Cursor Agent、Gemini CLI 等十余种本地编码 Agent，进行代码评审、研究、自动化和数据分析。核心特性包括：

- **多 Agent 支持**：v1.3.3 新增 Devin CLI、Google Antigravity (`agy`)、GitHub Copilot CLI 作为一等公民，并强化了 Cursor / OpenCode / Qoder / Kimi / Pi 等支持。
- **平台扩张**：QQ (OneBot) 文件收发与内联键盘、企业微信 WebSocket SendFile、飞书音视频原生消息、Slack Assistant API、DingTalk 富文本/图片/文件入站、微博 DM 与 WPS 金山协作等。
- **长任务安全**：新增 `max_turn_time_mins` 软停止 + 强制结束 + 自动恢复机制，避免长时间 bash/test 锁死会话。
- **新核心命令**：`/timer`（一次性延时任务）、`/cancel`（中断当前轮）、`/ps`（替代 `/btw`）、`cron add --silent`、Agent 驱动的 TTS。
- **多用户与权限**：reply-to-unauthorized-IM-senders、可与 @Bot/permit 等价的关键词匹配、Bridge 启用时强制 token。
- **Provider 生态**：NekoCode、VisionCoder、AIHubMix、预设 Provider；Claude Code 1M 上下文 Opus 与 `append_system_prompt`、PermissionRequest hooks；Codex `request_user_input`；可配置 shell / shell profile 用于 `exec`。
- **可观测性**：黑盒测试框架（P0/P1/P2 + 配置切换矩阵）、CUJ 测试框架、Provider-resume 回归套件、Pi context-usage reporter 显示在回复页脚。

v1.3.3 是 1.3.3-beta 系列的首个稳定版（自 beta.1 以来 ≈235 个 PR + 7 个 beta 后修复），不引入破坏性变更；行为变化包括：Telegram/Discord 的 `progress_style` 默认改为 `compact`、QQ Bot 默认 intents 包含 `INTERACTION_CREATE`、`reset_on_idle_mins` 默认 30 分钟、Bridge 未配置 token 时拒绝启动等。

零公网 IP 设计让用户可以在任何设备上用聊天 App 控制本地 AI 编码助手，是当下最完整的本地编程 Agent 聊天平台桥接方案。
