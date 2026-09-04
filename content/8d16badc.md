# Claude Code v2.1.260：全屏 diff 旁栏 + prompt-cache miss 原因说明

- **ID**: 8d16badc
- **原文链接**: https://github.com/anthropics/claude-code/releases/tag/v2.1.260
- **作者**: anthropics/claude-code
- **日期**: 2026-09-03
- **分类**: coding
- **来源类型**: github
- **标签**: claude-code, release, diff-panel, prompt-cache
- **质量评分**: 4/5
- **Stars**: ~144000
- **抓取时间**: 2026-09-04T08:00:00Z

---

## 中文导读

anthropics/claude-code v2.1.260（2026-09-03 23:48 UTC，144k stars）发布说明要点：全屏模式下 `/diff` 在对话旁栏打开未提交改动；`/cost` 与状态行的 `prompt_cache` 字段会写明缓存 miss 的可能原因；headless 会话多了 `/reload-plugins`，桌面与 SDK 命令列表同步出现；`/advisor` 提供文本形式供桌面、Remote Control 与 headless `-p`/Agent SDK 使用；Claude Apps gateway 增加 `oidc.scope_on_refresh` 与 Fable 5.1 / market place 兼容策略。同一次发布把 2.1.259 套在 Bash 参数上的 `Read()` deny 规则回滚（曾误拒 `npm run build`、让 `cd && grep` 在 auto 也弹窗），并修复带括号路径权限规则被忽略、Fable 5.1 缓存覆盖工具结果后上下文、`/model` picker 不显示 Fable 5.1、`-p --resume` 在 worktree 元数据丢失时反复失败等多项回归。

## 为什么值得关注

这次发版混合了三个层面：可见体验（`/diff` 全屏、状态行 cache miss 说明）、无头/CI 能力（`/reload-plugins`、`/advisor` 文本形式、Auto Mode 未受影响）、以及权限与缓存策略回滚（v2.1.259 的 Bash-Read 套用被撤、Fable 5.1 工具结果后上下文进缓存、`/effort` 改后不再作废缓存）。AIW-Agent-Coding-Log 已记录 v2.1.251，因此同月迭代节奏对持续跟进 Claude Code 的人尤其敏感。

## 关键信息

- 标题：v2.1.260
- Release tag：https://github.com/anthropics/claude-code/releases/tag/v2.1.260
- 发布时间：2026-09-03T23:48:12Z
- 仓库：anthropics/claude-code（≈144k stars）
- 关联标签：claude-code, release, diff-panel, prompt-cache
- 同月相关：v2.1.251（已收录入 entries.json / id `4eb68756`）

## English Summary

anthropics/claude-code v2.1.260 (2026-09-03 23:48 UTC, ~144k stars) adds a fullscreen diff panel via `/diff`, surfaces a likely cause for prompt-cache misses in `/cost` and the status line, brings `/reload-plugins` to headless sessions, exposes a text form of `/advisor` for desktop / Remote Control / headless `-p`-SDK, and adds `oidc.scope_on_refresh` plus Fable 5.1 / marketplace gateway policy. The release also reverts the v2.1.259 Bash-side application of `Read()` deny rules (which had wrongly blocked `npm run build` under `Read(./**/build/**)` and forced `cd && grep` to prompt even in auto), and fixes parentheses-bearing permission paths, Fable 5.1 cache coverage after tool results, `/model` picker missing Fable 5.1, `-p --resume` retry storms on lost worktree metadata, and a long list of smaller regressions.

## Obsidian Notes

- 来源 release body 已通过 GitHub API 抓取；与 last30days brief 中 'v2.1.260 全屏 diff + 缓存 miss 原因' 的描述一致。
- 中文导读与英文摘要均锚定在 release body 与 last30days brief，未补充外部细节。
