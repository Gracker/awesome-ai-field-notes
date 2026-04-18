# tenacitOS — OpenClaw Mission Control Dashboard

## English原文

A real-time dashboard and control center for OpenClaw AI agent instances. Built with Next.js, React 19, and Tailwind CSS v4. tenacitOS lives inside your OpenClaw workspace and reads its configuration, agents, sessions, memory, and logs directly from the host. No extra database or backend required — OpenClaw is the backend.

## 概述

tenacitOS 是一个为 OpenClaw AI agent 实例设计的实时仪表盘和控制中心。使用 Next.js、React 19 和 Tailwind CSS v4 构建。tenacitOS 运行在 OpenClaw 工作区内，直接从主机读取配置、agent、会话、记忆和日志。无需额外数据库或后端——OpenClaw 本身就是后端。

## 核心功能

### 📊 系统监控
实时 VPS 指标（CPU、RAM、磁盘、网络）+ PM2/Docker 状态

### 🤖 Agent 仪表盘
所有 agent 及其会话、token 使用量、模型和活动状态

### 💰 成本追踪
从 OpenClaw 会话（SQLite）获取的实时成本分析

### ⏰ Cron 管理器
可视化 Cron 管理器，带周时间线、运行历史和手动触发

### 📋 活动日志
实时 agent 操作日志，带热力图和图表

### 🧠 记忆浏览器
探索、搜索和编辑 agent 记忆文件

### 📁 文件浏览器
导航工作区文件，支持预览和浏览器内编辑

### 🔎 全局搜索
跨记忆和工作区文件的全文搜索

### 🏢 3D 办公室
交互式 3D 办公室，每个 agent 一个工位（React Three Fiber）

## 技术栈

| 层级 | 技术 |
|------|------|
| 框架 | Next.js 15 (App Router) |
| UI | React 19 + Tailwind CSS v4 |
| 3D | React Three Fiber + Drei |
| 图表 | Recharts |
| 数据库 | SQLite (better-sqlite3) |
| 运行时 | Node.js 22 |

## 安装要求

- Node.js 18+（已在 v22 上测试）
- OpenClaw 已安装并在同一主机上运行
- PM2 或 systemd（生产环境推荐）
- Caddy 或其他反向代理（生产环境 HTTPS）

## 安装步骤

```bash
cd /root/.openclaw/workspace
git clone https://github.com/carlosazaustre/tenacitOS.git mission-control
cd mission-control
npm install

# 复制环境配置
cp .env.example .env.local

# 编辑 .env.local 配置密码和密钥
```

### 生成安全密钥

```bash
openssl rand -base64 32  # AUTH_SECRET
openssl rand -base64 18  # ADMIN_PASSWORD
```

### 运行

```bash
# 开发模式
npm run dev

# 生产构建
npm run build
npm start
```

## 安全特性

- 所有路由（包括 /api/*）需要认证
- 公开端点仅限：/api/auth/login 和 /api/health
- 登录限流：5 次失败尝试 → IP 被锁定 15 分钟
- Auth cookie：httpOnly、sameSite:lax、生产环境 secure
- 终端 API 使用严格的命令白名单

## 相关链接

- GitHub：https://github.com/carlosazaustre/tenacitOS
- OpenClaw：https://openclaw.ai

---

来源：[carlosazaustre/tenacitOS](https://github.com/carlosazaustre/tenacitOS)
