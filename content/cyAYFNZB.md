# Google 发布面向 Agent 工作流的 Android CLI、Skills 与 Knowledge

来源: https://mp.weixin.qq.com/s?__biz=MzAxMTI4MTkwNQ==&mid=2650856619
官方文档: https://developer.android.com/tools/agents

## 概述

Google 发布 Android CLI、Android Skills 与 Android Knowledge Base 三大工具组件，为 Agent（Gemini、Claude Code、Codex 等）提供标准化的 Android 开发接口，目标是确保在任何开发环境中均可实现高质量 Android 应用构建。

## Android CLI

### 设计目标
为 Agent 提供轻量级、可编程的 SDK 交互能力，支持环境配置、项目创建、设备管理等核心开发任务。

### 核心能力

| 功能类别 | 命令 | 说明 |
|---------|------|------|
| SDK 管理 | android sdk install | 按需下载特定组件 |
| 项目创建 | android create | 基于官方模板生成项目 |
| 设备管理 | android emulator | 创建与管理虚拟设备 |
| 应用部署 | android run | 自动化构建与部署 |
| 版本更新 | android update | 获取最新功能与修复 |

### 性能数据
- Token 使用效率：相比传统工具集减少 **70%** 以上
- 任务完成速度：核心开发任务提升 **3 倍**

## Android Skills

### 设计背景
传统技术文档以描述性为主，适用于人工学习，但 LLM 执行复杂工作流时需要精确、可操作的指令。Android Skills 通过模块化的 SKILL.md 规范填补这一差距。

### 格式规范
- 名称：最多 64 字符（仅小写字母、数字、连字符）
- 描述：最多 1024 字符
- 正文：建议 10,000-20,000 字符（约 2,500-5,000 Token）

### 初始技能列表

| 技能名称 | 功能描述 |
|---------|---------|
| Navigation 3 Setup | Navigation 3 框架的配置与迁移 |
| Edge-to-Edge | 无边框（全屏）UI 实现 |
| AGP 9 Migration | Android Gradle Plugin 9 升级指南 |
| XML-to-Compose | 从 XML 布局迁移至 Jetpack Compose |
| R8 Config Analysis | R8 代码压缩配置分析 |

### 使用方式
```bash
android skills list
android skills add --skill skill-name
android skills add --all
```

## Android Knowledge Base

专门的数据源组件，支持 Agent 搜索与获取最新权威开发者指南。整合 Android 开发者官方文档、Firebase 文档、Google Developers 文档、Kotlin 官方文档。

通过 android docs 命令访问，已集成至 Android Studio。

## 快速开始

```bash
# macOS ARM64 安装
curl -fsSL https://dl.google.com/android/cli/latest/darwin_arm64/install.sh | bash

# 安装全部 Skills
android skills add --all

# 验证安装
android --version
android skills list
```

## 总结

三大工具构成完整的 Agent 开发工具链：Android CLI 提供标准化交互接口，Android Skills 确保遵循最佳实践，Knowledge Base 提供最新权威文档支持。
