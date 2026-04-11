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

# TenacitOS: OpenClaw Mission Control Dashboard

## English
A real-time dashboard and control center for OpenClaw AI agent instances. Built with Next.js, React 19, and Tailwind CSS v4.

TenacitOS lives inside your OpenClaw workspace and reads its configuration, agents, sessions, memory, and logs directly from the host. No extra database or backend required — OpenClaw is the backend.

**Core Features:**
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

**Architecture:**
- Reads directly from OpenClaw workspace at /root/.openclaw/
- Auto-discovers agents from openclaw.json
- No database required — uses SQLite for cost tracking
- Built with Next.js 15, React 19, and Tailwind CSS v4
- 3D office powered by React Three Fiber

**Installation:**
```bash
cd /root/.openclaw/workspace
git clone https://github.com/carlosazaustre/tenacitOS.git mission-control
cd mission-control
npm install
cp .env.example .env.local
# Edit .env.local with your configuration
npm run build
npm start
```

**Authentication:**
- Password-protected with strong password requirement
- Rate limiting: 5 failed attempts → 15-minute lockout per IP
- Secure cookies with httpOnly, sameSite: lax, secure in production

## 中文
OpenClaw AI 实例的实时仪表板和控制中心。使用 Next.js、React 19 和 Tailwind CSS v4 构建。

TenacitOS 位于您的 OpenClaw 工作区内，直接从主机读取其配置、代理、会话、内存和日志。不需要额外的数据库或后端——OpenClaw 就是后端。

**核心功能：**
- 📊 系统监控器 - 实时 VPS 指标（CPU、RAM、磁盘、网络）+ PM2/Docker 状态
- 🤖 代理仪表板 - 所有代理、其会话、令牌使用、模型和活动状态
- 💰 成本跟踪 - 来自 OpenClaw 会话的实时成本分析（SQLite）
- ⏰ Cron 管理器 - 可视化 cron 管理器，包含周时间线、运行历史和手动触发器
- 📋 活动源 - 代理操作的实时日志，包含热力图和图表
- 🧠 内存浏览器 - 探索、搜索和编辑代理内存文件
- 📁 文件浏览器 - 浏览工作区文件，支持预览和浏览器内编辑
- 🔎 全局搜索 - 在内存和工作区文件中全文搜索
- 🔔 通知中心 - 实时通知中心，带有未读标记
- 🏢 3D 办公室 - 每个代理一个桌面的交互式 3D 办公室（React Three Fiber）
- 📺 终端 - 用于安全状态命令的只读终端
- 🔐 身份验证 - 密码保护，带有速率限制和安全 cookie

**架构特点：**
- 直接从 /root/.openclaw/ 读取 OpenClaw 工作区
- 从 openclaw.json 自动发现代理
- 不需要数据库 - 使用 SQLite 进行成本跟踪
- 使用 Next.js 15、React 19 和 Tailwind CSS v4 构建
- 3D 办公室由 React Three Fiber 驱动

**安装步骤：**
```bash
cd /root/.openclaw/workspace
git clone https://github.com/carlosazaustre/tenacitOS.git mission-control
cd mission-control
npm install
cp .env.example .env.local
# 编辑 .env.local 配置文件
npm run build
npm start
```

**身份验证：**
- 密码保护，需要强密码
- 速率限制：5次失败尝试 → 每IP 15分钟锁定
- 安全 cookie，生产环境中启用 httpOnly、sameSite: lax、secure

**技术栈：**
- 框架：Next.js 15（应用路由器）
- UI：React 19 + Tailwind CSS v4
- 3D：React Three Fiber + Drei
- 图表：Recharts
- 图标：Lucide React
- 数据库：SQLite（better-sqlite3）
- 运行时：Node.js 22

该项目是 OpenClaw 的官方监控仪表板，提供了全面的管理界面，让用户能够实时监控和管理他们的 AI 代理实例。
