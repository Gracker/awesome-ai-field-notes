---
title: 'TenacitOS: OpenClaw Mission Control Dashboard'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# TenacitOS: OpenClaw Mission Control Dashboard

> OpenClaw 的实时监控仪表盘，零后端依赖

🔗 [原文链接](https://github.com/carlosazaustre/tenacitOS) | @geekbb |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-02-26

`openclaw` `dashboard` `monitoring` `nextjs` `react` `tailwind`

---

## English

## 中文

TenacitOS: OpenClaw Mission Control Dashboard

TenacitOS 是一个为 OpenClaw AI 实例提供的实时仪表盘和控制中心，使用 Next.js、React 19 和 Tailwind CSS v4 构建。

TenacitOS 生活在你的 OpenClaw 工作区内，直接从主机读取其配置、代理、会话、记忆和日志。无需额外的数据库或后端——OpenClaw 本身就是后端。

核心功能模块：

- 📊 系统监控器 — 实时 VPS 指标（CPU、RAM、磁盘、网络）+ PM2/Docker 状态
- 🤖 代理仪表盘 — 所有代理、它们的会话、令牌使用情况、模型和活动状态
- 💰 成本追踪 — 来自 OpenClaw 会话的实时成本分析（SQLite）
- ⏰ Cron 管理器 — 可视化 cron 管理器，包含时间线、运行历史和手动触发
- 📋 活动流 — 代理操作的实时日志，包含热图和图表
- 🧠 记忆浏览器 — 浏览、搜索和编辑代理记忆文件
- 📁 文件浏览器 — 使用预览和浏览器内编辑导航工作区文件
- 🔎 全局搜索 — 跨记忆和工作区文件的全文搜索
- 🔔 通知中心 — 实时通知中心，包含未读徽章
- 🏢 办公室 3D — 每个代理一张桌子的交互式 3D 办公室（React Three Fiber）
- 📺 终端 — 用于安全状态命令的只读终端
- 🔐 身份验证 — 带速率限制和安全密码保护的密码保护

部署要求：

- Node.js 18+（已用 v22 测试）
- 在同一主机上安装并运行的 OpenClaw
- PM2 或 systemd（生产环境推荐）
- Caddy 或其他反向代理（生产环境 HTTPS）

TenacitOS 直接从你的 OpenClaw 安装读取：
/root/.openclaw/ ← OPENCLAW_DIR（可配置）
├── openclaw.json ← 代理列表、频道、模型配置
├── workspace/ ← 主要代理工作区（MEMORY.md、SOUL.md 等）
└── workspace/mission-control/ ← TenacitOS 在这里

应用程序使用 OPENCLAW_DIR 来定位 openclaw.json 和所有工作区。无需手动代理配置——代理从 openclaw.json 自动发现。
