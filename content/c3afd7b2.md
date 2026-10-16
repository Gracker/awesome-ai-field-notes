---
id: c3afd7b2
title: Claude Code issue 102597: background agents re-send full context on every macOS DarkWake overnight (81 requests)
url: https://github.com/anthropics/claude-code/issues/102597
source: Hermes 定时任务/X-每日简报/2026-10-15-X-seeds_Codex0163-Claude301-Hermes0222.md
added_date: 2026-10-17
category: infra
quality_score: 4
---

# Claude Code issue 102597: background agents re-send full context on every macOS DarkWake overnight (81 requests)

> 原文链接: https://github.com/anthropics/claude-code/issues/102597

## 要点 (中文)

macOS 用户报告（2026-10-15）：合盖时后台 subagent 仍在运行，之后 6.5 小时内几乎每次 DarkWake（dasd 睡眠服务约 15 分钟一次的唤醒）都重发每个 agent 的完整对话（400–580K token），而这些唤醒只持续几秒，请求随即再冻结。一晚统计（23:30–06:00 UTC+7）：81 次 /v1/messages 请求、仅 29 次完成、26 次睡眠/唤醒循环、19 次 StreamSuspended 重试。与 2.1.301 的 RETRY_WATCHDOG 用量上限直接相关，是无人值守长任务的费用边界典型案例。

## Key claims (English)

Issue #102597 reports that after closing a MacBook lid on battery, Claude Code background subagents re-sent each agent's full 400-580K-token conversation on almost every macOS DarkWake for 6.5 hours: 81 /v1/messages requests sent, only 29 completed, 26 sleep/wake cycles at ~15-min intervals, 19 StreamSuspended retries - usage consumed while asleep.

## Obsidian 证据摘录

> #102597 描述合盖后 background agent 仍烧请求；最小验证动作：打开 #102597 看复现条件；本机不主动复现烧额度。
> —— Hermes 定时任务/X-每日简报/2026-10-15-X-seeds_Codex0163-Claude301-Hermes0222.md

## 原文抓取

GitHub issue API (created 2026-10-15T23:41:47Z, state open)

Title: [Bug] macOS: background agents re-send full context on every DarkWake after lid close (81 requests sent, 29 completed overnight; usage consumed while asleep)

### What's wrong?

Background subagents were still running when I closed my MacBook lid on battery. For the next 6.5 hours, Claude Code re-sent each agent's full conversation (400–580K tokens) on almost every macOS DarkWake / Sleep Service wake. Those wakes last only a few seconds, so each new request was frozen again almost immediately.

Overnight result, from the extension's `--debug` log and the session transcripts (23:30–06:00 UTC+7, 2026-10-14/15):

| | |
|---|---|
| `/v1/messages` requests sent | **81** |
| Requests that completed (in transcripts) | **29** |
| macOS sleep/wake cycles | 26 (about every 15 min, `dasd` Sleep Service) |
| `StreamSuspended` retries | 19 |
| `404 No thread state was found` → `[tether] forcing create for retry: replay_not_found` | 11 |
| Completed calls that rewrote the whole prompt cache (`cache_read=0`, `cache_creation` 400–580K) | 15, about 7.1M tokens |
| Output tokens produced all night | about 7K |

There was no human input in that window. My subscription's weekly usage went from 20% at 23:30 to 56% at 06:00. I can't tell locally how much of that came from requests that never completed, so I'm asking about billing below.

### Sequence (repeats on every wake)

1. 23:24 local: lid closed on battery → `Entering Sleep state due to 'Clamshell Sleep'`. Two background subagents (`requestShape: background`) are mid-stream.
2. About 15 min later, m
