---
title: 'TenacitOS: OpenClaw Mission Control Dashboard'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# TenacitOS: OpenClaw Mission Control Dashboard

> OpenClaw 的实时监控仪表盘，零后端依赖

🔗 [原文链接](https://github.com/carlosazaustre/tenacitOS) | @geekbb |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`openclaw` `dashboard` `monitoring` `nextjs` `react` `tailwind`

---

A real-time dashboard and control center for OpenClaw AI agent instances. Built with Next.js, React 19, and Tailwind CSS v4.

TenacitOS lives inside your OpenClaw workspace and reads its configuration, agents, sessions, memory, and logs directly from the host. No extra database or backend required — OpenClaw is the backend.

### Features

- 📊 System Monitor — Real-time VPS metrics (CPU, RAM, Disk, Network) + PM2/Docker status
- 🤖 Agent Dashboard — All agents, their sessions, token usage, model, and activity status  
- 💰 Cost Tracking — Real cost analytics from OpenClaw sessions (SQLite)
- ⏰ Cron Manager — Visual cron manager with weekly timeline, run history, and manual triggers
- 📋 Activity Feed — Real-time log of agent actions with heatmap and charts
- 🧠 Memory Browser — Explore, search, and edit agent memory files
- 📁 File Browser — Navigate workspace files with preview and in-browser editing
- 🔎 Global Search — Full-text search across memory and workspace files
- 🔔 Notifications — Real-time notification center with unread badge
- 🏢 Office 3D — Interactive 3D office with one desk per agent (React Three Fiber)
- 📺 Terminal — Read-only terminal for safe status commands
- 🔐 Auth — Password-protected with rate limiting and secure cookie

### Requirements

- Node.js 18+ (tested with v22)
- OpenClaw installed and running on the same host
- PM2 or systemd (recommended for production)
- Caddy or another reverse proxy (for HTTPS in production)

### Installation

1. Clone the repository:

up to date, audited 576 packages in 2s

218 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (4 moderate, 5 high)

To address issues that do not require attention, run:
  npm audit fix

To address all issues, run:
  npm audit fix --force

Run `npm audit` for details.

2. Copy and edit environment:


3. Set authentication:
hRUC2huCvFk0WuMimO27/3QzJ3pnMAHtG0TDUy81UfI=
JIMoX524uFaU6wMMs4n75zdR

4. Copy example data files:


5. Start the application:


### Technology Stack

- **Framework**: Next.js 15 (App Router)
- **UI**: React 19 + Tailwind CSS v4
- **3D**: React Three Fiber + Drei
- **Charts**: Recharts
- **Icons**: Lucide React
- **Database**: SQLite (better-sqlite3)
- **Runtime**: Node.js 22

## 中文

TenacitOS 是一个用于 OpenClaw AI Agent 实例的实时仪表板和控制中心。使用 Next.js、React 19 和 Tailwind CSS v4 构建。

TenacitOS 驻留在您的 OpenClaw 工作区内，直接从主机读取其配置、Agent、会话、记忆和日志。无需额外的数据库或后端——OpenClaw 就是后端。

### 功能特性

- 📊 系统监控器 — 实时 VPS 指标（CPU、RAM、磁盘、网络）+ PM2/Docker 状态
- 🤖 Agent 仪表板 — 所有 Agent、其会话、Token 使用量、模型和活动状态
- 💰 成本追踪 — 来自 OpenClaw 会话的实时成本分析（SQLite）
- ⏰ Cron 管理器 — 可视化 Cron 管理器，包含时间线、运行历史和手动触发
- 📋 活动源 — Agent 操作的实时日志，包含热图和图表
- 🧠 记忆浏览器 — 探索、搜索和编辑 Agent 记忆文件
- 📁 文件浏览器 — 浏览工作区文件，支持预览和浏览器内编辑
- 🔎 全局搜索 — 跨记忆和工作区文件的全文搜索
- 🔔 通知中心 — 实时通知中心，包含未读标记
- 🏢 3D 办公室 — 每个 Agent 一个桌面的交互式 3D 办公室（React Three Fiber）
- 📺 终端 — 安全状态命令的只读终端
- 🔐 身份验证 — 带有速率限制和安全 Cookie 的密码保护

### 要求

- Node.js 18+（已在 v22 上测试）
- OpenClaw 安装并在同一主机上运行
- PM2 或 systemd（生产环境推荐）
- Caddy 或其他反向代理（生产环境 HTTPS）

### 安装

1. 克隆仓库：

up to date, audited 576 packages in 2s

218 packages are looking for funding
  run `npm fund` for details

9 vulnerabilities (4 moderate, 5 high)

To address issues that do not require attention, run:
  npm audit fix

To address all issues, run:
  npm audit fix --force

Run `npm audit` for details.

2. 复制并编辑环境变量：


3. 设置身份验证：
neUIblZo3JpMoN0jJQifeKwV/To4oq1+dc9/XR0nCKU=
ZzFZMGnnAyUNI5iZXyuUT9Zk

4. 复制示例数据文件：


5. 启动应用程序：


### 技术栈

- **框架**: Next.js 15 (App Router)
- **UI**: React 19 + Tailwind CSS v4
- **3D**: React Three Fiber + Drei
- **图表**: Recharts
- **图标**: Lucide React
- **数据库**: SQLite (better-sqlite3)
- **运行时**: Node.js 22

### 安全特性

- 所有路由（包括所有 /api/*）都需要身份验证
- 登录被限制：5 次失败尝试 → 每个 IP 锁定 15 分钟
- Auth cookie 是 httpOnly、sameSite: lax，生产环境中是安全的
- 终端 API 使用严格的命令允许列表 - 阻止 env、curl、wget、node、python
- 永远不要提交 .env.local - 它包含您的凭据

## 许可证

MIT - 查看 [LICENSE](https://github.com/carlosazaustre/tenacitOS/blob/main/LICENSE)

---

相关链接：
- [OpenClaw](https://openclaw.ai) — 这个仪表板构建的 AI Agent 运行时
- [OpenClaw 文档](https://docs.openclaw.ai)
- [Discord 社区](https://discord.com/invite/clawd)
- [GitHub 问题](https://github.com/carlosazaustre/tenacitOS/issues) — 错误报告和功能请求
