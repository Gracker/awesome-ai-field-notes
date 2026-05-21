---
id: d68eb0ad
title: "Android CLI: Build Android apps 3x faster using any agent"
source: "android-developers.googleblog.com"
fetched_at: "2026-05-20"
tags: ["android", "cli", "agent", "development-tools"]
quality_score: 4
---

# Android CLI: Build Android apps 3x faster using any agent

## English / 英语

As Android developers, you have many choices when it comes to the agents, tools, and LLMs you use for app development. Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

Today, we are introducing a new suite of Android tools and resources for agentic workflows — Android CLI with Android skills and the Android Knowledge Base. This collection of tools is designed to eliminate the guesswork of core Android development workflows when you direct an agent's work outside of Android Studio, making your agents more efficient, effective, and capable of following the latest recommended patterns and best practices.

## (Re)Introducing the Android CLI

Your agents perform best when they have a lightweight, programmatic interface to interact with the Android SDK and development environment. So, at the heart of this new workflow is a revitalized Android CLI. The new Android CLI serves as the primary interface for Android development from the terminal, featuring commands for environment setup, project creation, and device management—with more modern capabilities and easy updatability in mind.

In our internal experiments, Android CLI improved project and environment setup by reducing LLM token usage by more than 70%, and tasks were completed 3X faster than when agents attempted to navigate these tasks using only the standard toolsets.

Key capabilities:
- **SDK management**: Use `android sdk install` to download only the specific components needed
- **Snappy project creation**: The `android create` command generates new projects from official templates
- **Rapid device creation and deployment**: Create and manage virtual devices with `android emulator` and deploy apps using `android run`
- **Updatability**: Run `android update` to ensure you have the latest capabilities

## Grounding LLMs with official Android Skills

Traditional documentation can be descriptive, conceptual, and high-level. While perfect for learning, LLMs often require precise, actionable instructions to execute complex workflows without using outdated patterns and libraries.

To bridge this gap, we are launching the [Android skills GitHub repository](https://github.com/android/skills). Skills are modular, markdown-based (SKILL.md) instruction sets that provide a technical specification for a task and are designed to trigger automatically when your prompt matches the skill's metadata.

Initial skills include:
- Navigation 3 setup and migration
- Implementing edge-to-edge support
- AGP 9 and XML-to-Compose migrations
- R8 config analysis, and more!

## The Android Knowledge Base

The third component is the Android Knowledge Base. Accessible through the `android docs` command and already available in the latest version of Android Studio, this specialized data source enables agents to search and fetch the latest authoritative developer guidelines.

By accessing the frequently updated knowledge base, agents can ground their responses in the most recent information from Android developer docs, Firebase, Google Developers, and Kotlin docs.

## Get started today

Android CLI is available in preview today, along with a growing set of Android skills and knowledge for agents. To get started, head over to [d.android.com/tools/agents](http://d.android.com/tools/agents).

---

# 中文

作为 Android 开发者，在 app 开发过程中，你可以选择使用多种智能体、工具和大语言模型。无论你使用 Android Studio 中的 Gemini、Gaxti CLI、Antigravity，还是第三方智能体（如 Claude Code 或 Codex），我们的使命都是确保高质量的 Android 开发无处不在。

今天，我们发布了一套全新的 Android 工具和资源，专门为智能体工作流设计——即带有 Android Skills 和 Android Knowledge Base 的 Android CLI。这套工具旨在消除在 Android Studio 之外指挥智能体执行核心 Android 开发工作流时的猜测成本，让你的智能体更高效、更有效，并能够遵循最新推荐的最佳实践。

## （重新）介绍 Android CLI

当智能体拥有轻量级、可编程的界面来与 Android SDK 和开发环境交互时，它们的表现最佳。因此，全新 Android CLI 是这一新工作流的核心。新的 Android CLI 作为终端中 Android 开发的主要接口，提供了环境设置、项目创建和设备管理等功能——并且具备更现代的能力和简易的可更新性。

在我们内部实验中，Android CLI 通过将大语言模型的 token 使用量减少 70% 以上，将任务完成速度提升了 3 倍——相比之下，智能体仅使用标准工具集时无法做到这一点。

主要能力包括：
- **SDK 管理**：使用 `android sdk install` 仅下载所需的特定组件
- **快速项目创建**：`android create` 命令从官方模板生成新项目
- **快速设备创建和部署**：使用 `android emulator` 创建和管理虚拟设备，使用 `android run` 部署应用
- **可更新性**：运行 `android update` 以确保你拥有最新能力

## 用官方 Android Skills 为大语言模型奠基

传统文档可以是描述性的、概念性的和高层次的。虽然适合学习，但大语言模型通常需要精确的、可操作的指令来执行复杂工作流，而不会使用过时的模式和库。

为了弥合这一差距，我们推出了 [Android Skills GitHub 仓库](https://github.com/android/skills)。Skills 是模块化的、基于 Markdown（SKILL.md）的指令集，为任务提供技术规范，并设计为当你的提示词与 skill 的元数据匹配时自动触发。

初始 skills 包括：
- Navigation 3 的设置和迁移
- 实现边缘到边缘支持
- AGP 9 和 XML 到 Compose 的迁移
- R8 配置分析，等等！

## Android Knowledge Base

第三个组件是 Android Knowledge Base。通过 `android docs` 命令访问，且已在最新版本的 Android Studio 中可用，这一专业数据源使智能体能够搜索和获取最新的权威开发者指南。

通过访问频繁更新的 Knowledge Base，智能体可以基于来自 Android 开发者文档、Firebase、Google Developers 和 Kotlin 文档的最新信息来优化其响应。

## 今天就开始

Android CLI 今日以预览版形式发布，同时还有一套不断增长的 Android Skills 和面向智能体的知识。开始使用请访问 [d.android.com/tools/agents](http://d.android.com/tools/agents)。
