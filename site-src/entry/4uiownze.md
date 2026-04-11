---
title: '一句话让 Agent 接入全网语义搜索与多平台读取'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# 一句话让 Agent 接入全网语义搜索与多平台读取

> 一键给 Agent 接入多平台数据源，免费且模块可替换

🔗 [原文链接](https://github.com/Panniantong/Agent-Reach) | @Neo Reid | 🇨🇳 | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-04-10

`agent-reach` `multi-platform` `search` `mcp` `data-access`

---

## English

A Python-based mobile automation agent that uses Qwen3-VL vision-language models to understand and interact with Android devices through visual analysis and ADB commands.

- 🤖 Vision-powered automation: Uses Qwen3-VL to visually understand phone screens

- 📱 ADB integration: Controls Android devices via ADB commands

- 🎯 Natural language tasks: Describe what you want in plain English

- 🖥️ Web UI: Built-in Gradio interface for easy control

- 📊 Real-time feedback: Live screenshots and execution logs

## 中文

一个基于 Python 的移动自动化代理，使用 Qwen3-VL 视觉语言模型通过视觉分析和 ADB 命令来理解和交互 Android 设备。

- 🤖 视觉驱动的自动化：使用 Qwen3-VL 视觉理解手机屏幕
- 📱 ADB 集成：通过 ADB 命令控制 Android 设备
- 🎯 自然语言任务：用简单的英语描述你想要什么
- 🖥️ Web 界面：内置 Gradio 界面，便于控制
- 📊 实时反馈：实时截图和执行日志

## 系统要求

- Python 3.10+
- 启用 USB 调试和开发者模式的 Android 设备
- 已安装 ADB (Android Debug Bridge)
- 具有足够 VRAM 的 GPU（在 24GB GPU 上使用 Qwen3-VL-8B 模型测试）

## 安装步骤

### Linux/Ubuntu



创建虚拟环境



安装 Python 依赖

Collecting git+https://github.com/huggingface/transformers
  Cloning https://github.com/huggingface/transformers to /private/var/folders/8b/z1bl0hq97679dkgkj95c9ts00000gn/T/pip-req-build-2URhg9
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'error'
Collecting pillow
  Downloading Pillow-6.2.2-cp27-cp27m-macosx_10_6_intel.whl (3.9 MB)
Collecting gradio
  Downloading gradio-3.0.12.tar.gz (5.1 MB)

## 配置

### Android 设备设置

- 在 Android 设备上启用 USB 调试（设置 → 开发者选项）
- 通过 USB 连接
- 验证连接：



你应该看到你的设备被列出。

### 模型配置

编辑 qwen_vl_agent.py 选择你的模型：



你还需要更改第 61 行：



将其更改为：



### 分辨率配置

代理可以从 Web UI 设置标签页自动检测你的设备分辨率，但也可以在 config.json 中手动配置：



获取设备分辨率：



## 使用方法

### Web 界面启动



导航到 http://localhost:7860 并输入任务：

- "Open Chrome"
- "Search for weather in New York"
- "Open Settings and enable WiFi"

### 命令行使用



示例：



## 工作流程

1. **截图捕获**：通过 ADB 获取手机截图
2. **视觉分析**：Qwen3-VL 分析屏幕以理解 UI 元素
3. **动作规划**：确定最佳动作（点击、滑动、输入等）
4. **执行**：发送 ADB 命令执行动作
5. **重复**：继续直到任务完成或达到最大循环次数

## 关键配置

config.json 中的关键设置：

- **temperature**: 模型创造力（0.0-1.0，默认：0.1）
- **max_tokens**: 最大响应长度（默认：512）
- **step_delay**: 动作间等待时间（秒，默认：1.5）
- **max_retries**: 最大重试次数（默认：3）
- **use_flash_attention**: 启用 Flash Attention 2 以加快推理

## 故障排除

### 设备未检测到

- 确保 USB 调试已启用
- 运行 adb devices 验证连接
- 尝试 adb kill-server && adb start-server

### 点击位置错误

- 在 UI 的设置标签页中自动检测分辨率
- 或手动验证 adb shell wm size

### 模型加载错误

- 确保你有足够的 VRAM
- 尝试使用 8B 模型以降低内存需求
- 检查 transformers 是否从源代码安装

### 内存不足

- 使用 8B 模型而不是 30B
- 减少 config 中的 max_tokens
- 关闭使用 GPU 内存的其他应用程序

## 许可证

Apache License 2.0 - 详见 LICENSE 文件

## 技术栈

- 基于 [Qwen3-VL](https://github.com/QwenLM/Qwen-VL) 由阿里云构建
- 使用 [Gradio](https://gradio.app/) 作为 Web 界面
