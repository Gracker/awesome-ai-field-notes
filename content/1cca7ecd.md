# Perfetto v59.1

- **ID**: 1cca7ecd
- **原文链接**: https://github.com/google/perfetto/releases/tag/v59.1
- **作者**: google/perfetto
- **日期**: 2026-10-27
- **分类**: infra
- **来源类型**: github
- **标签**: perfetto, tracing, agent-mode, android, release
- **质量评分**: 3/5
- **抓取时间**: 2026-10-27T23:54:36

---

## 中文导读

Perfetto v59.1：Android 配置 persist_trace_across_reboots 后，设备中途重启 trace 文件留在磁盘，下次开机经 --upload-after-reboot 恢复上传；Trace Processor CLI 检测到编码 agent 环境时自动切 agent 模式——查询结果默认 markdown 表格、SQL 错误收成单行 JSON、rustc 风格定位。另有 flamegraph 函数视图、callstack flamechart 轨道与 linux.smaps 数据源；迁移项：交互 shell 的 .dump 等三个命令已删除。

## 为什么值得关注

抓长压测和 agent 辅助分析两条线都值得当天升级：trace 能跨设备重启恢复，trace_processor 给 AI 编码工具加了专用输出模式。

## 原文摘录 (Excerpts)

> This release brings traces that survive device reboots on Android, a much friendlier Trace Processor command line (rustc-style SQL errors, markdown output and a dedicated agent mode for AI coding tools), flamegraphs as call trees and function tables, sampled callstacks over time, a new linux.smaps data source, and a long list of UI, SQL standard library and SDK improvements.

> Set TraceConfig.persist_trace_across_reboots and the trace file is kept on disk if the device reboots mid-trace, then recovered and uploaded.

## 抓取方式

GitHub release 页面直取（v59.1 published 2026-10-27T02:09Z，经 Releases API 复核）。

## 关键信息

- 文章标题: Perfetto v59.1
- 作者: google/perfetto
- 原文链接: https://github.com/google/perfetto/releases/tag/v59.1
- 发布时间: 2026-10-27
- 关联标签: perfetto, tracing, agent-mode, android, release

## Obsidian Notes

- 来源笔记: OpenClaw定时任务/DevRadar/2026-10-27-DevRadar.md
