# Locating the source of a mysterious beep with Claude

- **ID**: baaf713b
- **原文链接**: https://simonwillison.net/2026/Nov/9/mysterious-beeps/
- **作者：** Simon Willison
- **发布时间**: 2026-11-09
- **更新**: N/A
- **分类**: coding
- **来源类型**: blog
- **标签**: claude-code, agentic-coding, dsp, hardware
- **质量评分**: 4/5
- **抓取时间**: 2026-11-16T23:47:32+08:00

---

## 中文导读

Willison 把 coding agent 接到物理世界：储物间里间歇蜂鸣、站着听无法定位，他让 Claude Code 造了 Beep Locator，用两台 iPad、一部手机、MacBook Pro 和 Surface 当听音器。确认目标频率后持续监听，由往返时延最小的设备先发短 chirp，其余设备上传 chirp 前后各一段录音做对齐，三角定位锁定到约 40 厘米——翻出一只该换电池的老式一氧化碳探测器。Claude 写第一版 problem.md 时自己找出了 2007 年普渡 BeepBeep 论文；agent 没有原生音频输入，但能跑 FFT 分析并通过 WebSocket 给听音器热更新代码。

## 为什么值得关注

Willison 把 coding agent 接到物理世界：储物间里间歇蜂鸣、站着听无法定位，他让 Claude Code 造了 Beep Locator，用两台 iPad、一部手机、MacBook Pro 和 Surface 当听音器。确认目标频率后持续监听，由往返时延最小的设备先发短 chirp，其余设备上传 chirp 前后各一段录音做对齐，三角定位锁定到约 40 厘米——翻出一只该换电池的老式一氧化碳探测器。Claude 写第一版 problem.md 时自己找出了 2007 年普渡 BeepBeep 论文；agent 没有原生音频输入，但能跑 FFT 分析并通过 WebSocket 给听音器热更新代码。

Willison documents a complete agent-in-the-physical-world experiment: a mystery beep in a storage room, located by a Claude Code-built Beep Locator using two iPads, a phone, a MacBook Pro, and a Surface as listeners. Devices record audio, an FFT plus high-pass filter detects the beep, and the server aligns clips around a chirp from the lowest-round-trip device to trilaterate the source to about 40 cm - an old CO detector needing a battery. Claude itself surfaced the 2007 Purdue BeepBeep paper while writing the first problem.md. The author frames it as giving Claude Code ears: no native audio input, but it can run the analysis stack and hot-reload listener code over a WebSocket channel.

## 关键信息

- 标题：Locating the source of a mysterious beep with Claude
- 作者：Simon Willison
- 来源：https://simonwillison.net/2026/Nov/9/mysterious-beeps/
- 发布时间：2026-11-09
- 标签：claude-code, agentic-coding, dsp, hardware

## 原文摘录（Evidence Excerpts）

> - 作者: Simon Willison - 发布: 2026-11-09 - 原文: https://simonwillison.net/2026/Nov/9/mysterious-beeps/ - 抓取时间: 2026-11-16 (Asia/Shanghai)

> ---

> ---

> 9th November 2026

## Obsidian Notes

- 证据来源：OpenClaw定时任务/AK-RSS-Digest（89源精选）/source/2026-11-16-02-willison-mysterious-beeps.md
- 本页为当日 intake 内容页：事实与数字锚定在上列证据文件与原文链接，未添加证据之外的细节。
