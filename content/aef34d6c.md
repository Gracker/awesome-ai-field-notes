# Codex CLI 0.172.0: exec resume keeps sandbox permissions, slash Tab completion, task-group navigation

- **ID**: aef34d6c
- **原文链接**: https://github.com/openai/codex/releases/tag/rust-v0.172.0
- **作者**: OpenAI
- **日期**: 2026-11-24
- **更新**: 2026-11-24
- **分类**: coding
- **来源类型**: article
- **标签**: codex, sandbox, changelog, cli
- **质量评分**: 3/5
- **抓取时间**: 2026-11-24T15:45:00Z

---

## 中文导读

Codex CLI 正式版从 0.171.0 升到 0.172.0（tag rust-v0.172.0，约 11-24 00:03 UTC）。搜索结果和 transcript 里的 thread 链接可以直接打开已保存对话与嵌套 agent；支持的 slash 命令参数可用 Tab 补全，比如 /mcp lo 补成 /mcp login；agent command center 里 Shift+Up/Down 在任务组之间跳；可选的 stdio MCP 改成首次工具调用时再启动；config.toml 可以给单个 connected app 的工具设审批人；app-server 登录支持 Amazon Bedrock Runtime。运维向最实用的是 codex exec resume 现在会恢复已保存的沙箱权限、工作目录和 workspace roots，显式覆盖除外；父 turn 被打断时，子 agent 已排队的回复留给下一轮，不再丢失。

## 为什么值得关注

exec resume 保住沙箱权限这条直接命中此前"恢复会话丢配置"的痛点，配合懒启动 stdio MCP 和按 app 工具的审批人配置，是 CI/自动化场景里值得跟进的一版。注意 0.173.0-alpha.4 还在 pre-release 线上，不要把 alpha 当 Latest。

## 关键信息

- 版本：0.171.0 → 0.172.0（tag rust-v0.172.0，约 2026-11-24 00:03 UTC）
- 会话：搜索结果与 transcript 内 thread 链接可打开已保存对话与嵌套 agent
- 交互：slash 命令参数 Tab 补全（/mcp lo → /mcp login）；command center Shift+Up/Down 跳任务组
- MCP：可选 stdio MCP 首次工具调用时再启动；config.toml 按单 connected app 工具设审批人
- 后端：app-server 登录可选 Amazon Bedrock Runtime
- 运维：codex exec resume 恢复沙箱权限、工作目录、workspace roots；父 turn 打断后子 agent 排队回复留给下一轮
- 注意：0.173.0-alpha.4 等仍在 pre-release，Latest 以 rust-v0.172.0 为准

## English Summary

Codex CLI's stable release moves from 0.171.0 to 0.172.0. Thread links in search results and transcripts now open saved conversations and nested agents; supported slash command parameters get Tab completion (e.g. /mcp lo completes to /mcp login); Shift+Up/Down jumps between task groups in the agent command center; optional stdio MCP servers now start lazily at first tool call; config.toml can set per-tool approvers for individual connected apps; and app-server login supports Amazon Bedrock Runtime. The most operationally useful change: codex exec resume now restores saved sandbox permissions, working directories, and workspace roots unless explicitly overridden, and when a parent turn is interrupted, queued replies from child agents carry over to the next turn instead of being lost.

## Obsidian Notes

- 内容锚定 Obsidian 简报《Hermes 定时任务/last30days/2026-11-24-ai-coding-agents-brief.md》，功能叙述只采官方 release body。
- 版本时间线出自简报的 gh release list 记录。
- 本页为 release-note 级别条目，行为细节以本机 codex exec resume 实测为准。
