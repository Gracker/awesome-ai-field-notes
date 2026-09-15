---
id: b8d1afcf
title: ADK for Kotlin 1.0 GA: Google's Official Kotlin AI Agent Framework
url: https://juejin.cn/post/7684533566942134278
source: Juejin (Carson带你学Android) 2026-09-14 + adk.dev/get-started/kotlin/
added_date: 2026-09-15
---

# ADK for Kotlin 1.0 GA: Google's Official Kotlin AI Agent Framework

## 文章要点 (中文)

Google 发布 ADK for Kotlin 1.0 正式版（Juejin 转载 2026-09-14，原文链接 adk.dev/get-started/kotlin/）。ADK = Agent Development Kit，Google 官方出品的 Kotlin AI Agent 开发框架；定位类比 Retrofit 是网络请求框架，ADK 就是 AI Agent 框架。架构基于 Kotlin Multiplatform（KMP）：核心层 google-adk-kotlin-core 提供 Agent 引擎 / 工具系统 / 编排逻辑；处理器 google-adk-kotlin-processor 用 KSP 在编译期生成 Tool 的 JSON Schema（零运行时反射）；Android 扩展 google-adk-kotlin-core-android 适配 Android 生命周期；端侧推理走 google-adk-kotlin-litert-lm（Gemma 等） + google-adk-kotlin-mlkit-android（ML Kit + Gemini Nano）；云端用 google-adk-kotlin-firebase-android 接 Firebase AI Logic。核心能力：@Tool + KSP 编译期生成 Schema；多 Agent 层级化编排；人在回路（HITL）通过 `@Tool(requireConfirmation = true)` 实现敏感操作的暂停-持久化-恢复；Android 端独有 LiteRT-LM + Room + AppSearch + FileArtifactService 三件套。Kotlin 战场的 Android 开发者获得完整生产级方案，与 Python / JS 版本功能对等；端侧 Agent 是 Kotlin 独占优势。

## Key claims (English)

Google released ADK for Kotlin 1.0 (Juejin mirror 2026-09-14, source https://adk.dev/get-started/kotlin/). ADK (Agent Development Kit) is Google's official Kotlin AI agent framework; the analogy in the post is 'Retrofit is to network calls what ADK is to AI agents'. Architecture is Kotlin Multiplatform (KMP): google-adk-kotlin-core provides the agent engine / tool system / orchestration; google-adk-kotlin-processor uses KSP to generate tool JSON Schemas at compile time (zero runtime reflection); google-adk-kotlin-core-android adapts the lifecycle; on-device inference uses google-adk-kotlin-litert-lm (Gemma etc.) + google-adk-kotlin-mlkit-android (ML Kit + Gemini Nano); cloud goes through google-adk-kotlin-firebase-android on Firebase AI Logic. Core capabilities: @Tool + KSP compile-time schema generation; hierarchical multi-agent orchestration; HITL via @Tool(requireConfirmation = true) for pause/persist/resume of sensitive operations; the Android side uniquely bundles LiteRT-LM + Room + AppSearch + FileArtifactService. For Android engineers in the Kotlin ecosystem this is a production-grade agent stack, feature-parity with the Python / JS versions; on-device agent work is a Kotlin exclusive advantage.

## Obsidian 证据摘录

> 「今日，Google 发布了 ADK for Kotlin 1.0 正式版。这意味着：**Android 开发者可以用 Kotlin 写生产级 AI Agent 了**。……ADK 全称 Agent Development Kit，这是：**Google 官方出品的 Kotlin AI Agent 开发框架**。」——技术文章/source/juejin-android/2026-09-15-76845335-ADK for Kotlin：Google 官方 AI Agent 教程.md L9-11

## 链接

- Juejin 原文：https://juejin.cn/post/7684533566942134278
- Google 官方：https://adk.dev/get-started/kotlin/
- 同步源：技术文章/source/juejin-android/2026-09-15-76845335-ADK for Kotlin：Google 官方 AI Agent 教程.md
