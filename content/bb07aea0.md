# Test iOS apps in the simulator (Claude Code Desktop)

- source_url: https://code.claude.com/docs/en/desktop-ios-simulator
- source_type: article
- platform: anthropic
- author: Anthropic / Claude Code Docs
- original_date: 2026-07-21
- added_date: 2026-07-22
- category: coding
- tags: claude-code, ios-simulator, device-loop, desktop, permissions
- quality_score: 4

## 摘要（中文）

Claude Code Desktop 公开 beta：会话旁 iOS Simulator pane，build/run/检查 app 时自动打开并直播模拟器画面。Desktop pane 直驱模拟器，不走 computer use、不抢屏；CLI 仍经 CU。要求 macOS、Desktop ≥ v1.24012.0、Xcode iOS platform；Pro/Max/Team，非 Enterprise；仅 local session。权限：首次 per-device 同意控制+截图；打开 URL 与 xcodebuild 仍跟 session permission；截图上云，模拟器勿登真实账号。设备归属 session，最多 4 pane。这是专用设备环产品化，不是又一次 CU。

## Summary (English)

Public beta docs for the iOS Simulator pane in Claude Code Desktop on macOS (Pro/Max/Team; not Enterprise). The pane opens beside the conversation when Claude builds, installs, launches, or checks an app, streaming the device live. Desktop drives the simulator directly without computer use or taking over the screen; CLI still reaches the simulator via computer use. Requires Desktop ≥ v1.24012.0, a Mac, and Xcode iOS platform; local sessions only. First-use per-device consent for control+screenshots; opening URLs and builds still follow session permission mode; screenshots go to Anthropic—do not log into real accounts on Claude-used simulators. Session-scoped devices, up to four panes. A vertical device loop, not generic computer use.

## One-liner

Claude Desktop 把 iOS 模拟器做成专用 pane：设备环，不是再抢一次全屏 CU。

## Source body / metadata

Fetched via opencli web read / official docs during evening intake. Key claims are grounded in the source page and same-day Obsidian digest notes.

Public beta docs for the iOS Simulator pane in Claude Code Desktop on macOS (Pro/Max/Team; not Enterprise). The pane opens beside the conversation when Claude builds, installs, launches, or checks an app, streaming the device live. Desktop drives the simulator directly without computer use or taking over the screen; CLI still reaches the simulator via computer use. Requires Desktop ≥ v1.24012.0, a Mac, and Xcode iOS platform; local sessions only. First-use per-device consent for control+screenshots; opening URLs and builds still follow session permission mode; screenshots go to Anthropic—do not log into real accounts on Claude-used simulators. Session-scoped devices, up to four panes. A vertical device loop, not generic computer use.

## Obsidian evidence

- local_note: 调研/2026-07-22-Claude-Code-iOS模拟器-设备环与权限边界.md
- intake_run: daily-intake-evening 2026-07-22

