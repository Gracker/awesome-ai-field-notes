---
id: 38ccbac9
title: Device Streaming and Android skills - available in Android CLI
url: https://android-developers.googleblog.com/2026/10/android-cli-device-streaming-and-skills.html
source: OpenClaw定时任务/DevRadar/2026-10-17-DevRadar.md
added_date: 2026-10-17
category: coding
quality_score: 3
---

# Device Streaming and Android skills - available in Android CLI

> 原文链接: https://android-developers.googleblog.com/2026/10/android-cli-device-streaming-and-skills.html
> Content fetched: 2026-10-17 — opencli Navigation rejected; curl fallback + HTML text extraction

## 要点 (中文)

Android CLI 接入 Android Device Streaming：agent 经 ADB over SSL 连接远程真机（官方演示 Pixel 10 Pro），可完成选型开机、部署构建、收取日志与 trace、无头截屏，全程不离开终端，支持任意 AI agent 接入。Android skills 仓库扩到 20+ 个结构化 SKILL.md（含 android-cli、Play 政策合规审计、Wear OS Compose Material 3 等），把 developer.android.com 的官方指南、API 参考与架构模式直接注入 agent 上下文，替代模型训练截止内的旧知识，官方强调每个 skill 附带 eval。

## Key claims (English)

Android CLI now includes Android Device Streaming — any AI agent can reach real devices (Pixel 10 Pro demoed) over ADB via SSL to power/boot devices, deploy builds, pull logs and traces, and capture headless screenshots, all from the terminal. The Android skills repository grows past 20 structured SKILL.md files (android-cli, Play policy auditing, Wear OS Compose Material 3, etc.) that ground agents with official developer.android.com guidance, each shipped with evals.

## Obsidian 证据摘录

> agent 经 ADB over SSL 连远程真机（官方演示 Pixel 10 Pro），能选型开机、部署构建、收日志和 trace、无头截屏，全程不离开终端……真机的 log/trace 管道打开后，启动、帧、内存这类采集任务开始能整体交给 agent 跑
> —— OpenClaw定时任务/DevRadar/2026-10-17-DevRadar.md

## 原文抓取

Device Streaming and Android skills - available in Android CLI

As Android developers, you have many choices when it comes to the agents, LLMs, tools, and command-line interfaces (CLI) you use for app development. Our goal is to help you build beautiful, high-quality Android apps, no matter how you choose to build. We’re announcing updates to our Android CLI command-line tooling, including the ability to access real devices through Android Device Streaming. We’re also sharing more Android skills, and giving you a deep dive into the Wear OS Compose Material 3 skill.

Android CLI is our tool to make command-line interface Android development easier. It supports any AI agent or tool in building more efficiently for Android.

Along with the android-cli skill, your agents use Android CLI to create, build, test, and manage Android projects, help you set up the development environment, create and run emulators, and execute test runs.

Android Device Streaming now available in CLI

It’s important to test your app on real devices to catch issues that are hardware- or OS-specific, but sometimes you don’t have access to the ones you need. Android Device Streaming gives you access to real physical devices, remotely. Your agent can now use Android Device Streaming anywhere, through Android CLI.

The agent can interact with physical devices (as if they were plugged in over USB) over a secure ADB over SSL connection. This enables spinning up devices, deploying builds, collecting logs and traces, and even capturing screenshots headlessly—all through the terminal.

To get started, link your project, instruct your agent to list available remote devices and decide which device you want next. Read the documentation to learn more, and see the Android CLI release notes.

To bridge the gap between LLMs’ default knowledge and platform-specific standards and updates, we keep growing our Android skills repository.

Android skills are structured instructions (SKILL.md files) that ground AI agents with our official guidance from developer.android.com. Instead of relying on a model’s training cutoff, skills provide more precise and fresher data, API references and samples, and architectural
