---
id: bb4d61db
title: Claude Code v2.1.271: Remote Fast Mode, /fast, per-command allowed_domains
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
source: GitHub Releases v2.1.271 + Obsidian last30days brief
added_date: 2026-09-15
---

# Claude Code v2.1.271: Remote Fast Mode, /fast, per-command allowed_domains

## Release 摘要 (中文)

anthropics/claude-code v2.1.271（2026-09-14）。可写行为：Claude Code Remote（云 + 自建 runner）支持 host fast 设置或会话内 `/fast`；fullscreen `/config` 可用鼠标滚轮和点击；auto + 沙箱下 Bash/PowerShell/Monitor 可按命令批 `allowed_domains`，只给该命令开需要的主机；子 agent 可加 `omitClaudeMd`；插件安装可用 `--accept-command <sha256>` 精确接受上一次 `--json` 展示的命令，而不是笼统 `-y`；`modelPricing` multiplier 最高 10；一批 org policy / MCP OAuth / Bash 权限 / 网关 text-plain 修复。GitHub Latest v2.1.272 body 只有 bugfix；装版以 `claude --version` 与 Latest tag 为准，能力叙事以 271 的 notes 为准。

## Key claims (English)

anthropics/claude-code v2.1.271 (GitHub Releases; 2026-09-14): Claude Code Remote (cloud and self-hosted runners) supports the host's fast setting or /fast in-session; fullscreen /config is mouse-scrollable and clickable; under auto + sandbox, Bash/PowerShell/Monitor can grant allowed_domains per command, opening only the hosts the command needs; sub-agents accept omitClaudeMd; plugin install can use --accept-command <sha256> to accept the exact command from the previous --json output instead of a blanket -y; modelPricing multiplier up to 10; plus a batch of org policy / MCP OAuth / Bash permission / gateway text-plain fixes. Pin version with `claude --version` and the GitHub Latest tag; the Latest is v2.1.272 (body is bugfix-only, so capability narrative anchors on 271's notes).

## Obsidian 证据摘录

> 「GitHub Latest 是 v2.1.272，release body 只有 bugfix。前一档 v2.1.271 才有可写行为：Claude Code Remote（云和自建 runner）支持 host 的 fast 设置或会话里 `/fast`；fullscreen 的 `/config` 可用鼠标滚轮和点击；auto + 沙箱下 Bash/PowerShell/Monitor 可按命令批 `allowed_domains`，只给该命令开需要的主机；子 agent 可加 `omitClaudeMd`；插件安装可用 `--accept-command <sha256>` 精确接受上一次 `--json` 展示的命令，而不是笼统 `-y`。」——Hermes 定时任务/last30days/2026-09-15-ai-coding-agents-brief.md L43-45

## 链接

- Release：https://github.com/anthropics/claude-code/releases/tag/v2.1.271
- brief：Hermes 定时任务/last30days/2026-09-15-ai-coding-agents-brief.md
