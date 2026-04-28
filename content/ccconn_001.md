# cc-connect: Bridge local AI coding agents to messaging platforms

GitHub: https://github.com/chenhg5/cc-connect
Stars: 6424 (截至 2026-04-27)
License: MIT

## 项目概述

cc-connect bridges AI agents running on your machine to the messaging platforms you already use. Code review, research, automation, data analysis — anything an AI agent can do, now accessible from your phone, tablet, or any device with a chat app.

## 支持的 AI Agent（10+）

Claude Code, Codex, Cursor Agent, Kimi CLI, Qoder CLI, Gemini CLI, OpenCode, iFlow CLI, Pi, Devin — plus any agent that supports the Agent Client Protocol (ACP).

## 支持的聊天平台（11个）

Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, Weibo, LINE, QQ, QQ Bot (Official), Weixin (personal).

## 核心特性

### 🌐 Web Admin UI (v1.3.0)
Full management dashboard embedded in the binary — no extra dependencies. Create and edit projects, manage providers, monitor sessions, edit cron jobs, and chat with your agent directly from the browser.

### 🤖 Universal Agent Support
10+ AI Agents 支持，跨平台统一接入。

### 📱 Platform Flexibility
Most platforms need zero public IP.

### 🔄 Multi-Agent Orchestration
Multi-Bot Relay — Bind multiple bots in a group chat and let them communicate with each other.

### 🎮 Complete Chat Control
Switch models (`/model`), tune reasoning (`/reasoning`), change permission modes (`/mode`), manage sessions, all via slash commands.

### 🧠 Persistent Memory
Read and write agent instruction files (`/memory`) without touching the terminal.

### ⏰ Intelligent Scheduling
Set up cron jobs in natural language.

### 🎤 Multimodal Support
Voice & Images — Send voice messages or screenshots.

## 安装方式

- npm: `npm install -g cc-connect`
- Homebrew: `brew install cc-connect`
- Binary from GitHub Releases
- Build from source (requires Go 1.22+)

## v1.3.0 新特性

- Lifecycle Event Hooks
- Skill Management
- Global Provider Management
- Personal WeChat 支持（ilink long-polling）
- Weibo DM 支持
- Feishu 增强（@name mentions, reply chains）
- Kimi CLI 和 Pi agent 支持

> 备注：原文抓取自 GitHub README。
