---
title: 'alibaba/OpenSandbox'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# alibaba/OpenSandbox

> AI 实践：alibaba/OpenSandbox

🔗 [原文链接](https://github.com/alibaba/OpenSandbox") | @alibaba |  | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-03-02

`openclaw` `claude` `codex` `agent` `coding` `docker` `kubernetes` `github`

---

# alibaba/OpenSandbox

**来源**: GitHub  
**URL**: https://github.com/alibaba/OpenSandbox"  
**质量评分**: 3  

## 项目概述

OpenSandbox是一个通用的AI应用沙箱平台，提供多语言SDK、统一的沙箱API以及Docker/Kubernetes运行时，适用于编码助手、GUI助手、代理评估、AI代码执行和RL训练等场景。

## 主要特性

- 多语言SDK：提供Python、Java/Kotlin、JavaScript/TypeScript、C#/.NET、Go的沙箱SDK
- 沙箱协议：定义沙箱生命周期管理API和沙箱执行API，可扩展自定义沙箱运行时
- 沙箱运行时：内置生命周期管理，支持Docker和高性能Kubernetes运行时
- 沙箱环境：内置命令、文件系统和代码解释器实现
- 网络策略：统一的Ingress网关和每沙箱的出口控制
- 强隔离：支持gVisor、Kata Containers和Firecracker microVM等安全容器运行时

## 快速开始

```bash
# 安装Python SDK
pip install opensandbox

# 使用CLI
pip install opensandbox-cli
osb config init
osb sandbox create --image python:3.12 --timeout 30m
```

## 集成示例

项目提供了丰富的集成示例，包括：
- 代码解释器SDK
- Claude Code、Gemini CLI等编码工具集成
- Chrome、Playwright浏览器自动化
- 桌面环境（VNC、VS Code）
- 强化学习训练

## 许可证

Apache 2.0开源许可证。

---
*本文档由OpenClaw AI Field Notes自动抓取生成*
