---
title: '一句话让 Agent 接入全网语义搜索与多平台读取'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# 一句话让 Agent 接入全网语义搜索与多平台读取

> 一键给 Agent 接入多平台数据源，免费且模块可替换

🔗 [原文链接](https://github.com/Panniantong/Agent-Reach) | @Neo Reid | 🇨🇳 | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-02-25

`agent-reach` `multi-platform` `search` `mcp` `data-access`

---

## English

## 中文

Agent-Reach：给 AI Agent 一键装上互联网能力

Agent-Reach 是一个开源项目，让你的 AI Agent 能够轻松访问整个互联网。通过一个 CLI 命令零 API 费用地读取和搜索 Twitter、Reddit、YouTube、GitHub、B站、小红书等平台。

## 问题背景

AI Agent 已经能帮你写代码、改文档、管项目——但你让它去网上找点东西，它就抓瞎了：

- 📺 "帮我看看这个 YouTube 教程讲了什么" → 看不了，拿不到字幕
- 🐦 "帮我搜一下推特上大家怎么评价这个产品" → 搜不了，Twitter API 要付费
- 📖 "去 Reddit 上看看有没有人遇到过同样的 bug" → 403 被封，服务器 IP 被拒
- 📕 "帮我看看小红书上这个品的口碑" → 打不开，必须登录才能看
- 📺 "B站上有个技术视频，帮我总结一下" → 连不上，海外/服务器 IP 被屏蔽
- 🔍 "帮我在网上搜一下最新的 LLM 框架对比" → 没有好用的搜索，要么付费要么质量差

## 解决方案

Agent-Reach 把这件事变成一句话：帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

复制给你的 Agent，几分钟后它就能读推特、搜 Reddit、看 YouTube、刷小红书了。

## 核心特性

💰 完全免费
所有工具开源、所有 API 免费。唯一可能花钱的是服务器代理（$1/月），本地电脑不需要

🔒 隐私安全
Cookie 只存在你本地，不上传不外传。代码完全开源，随时可审查

🔄 持续更新
底层工具（yt-dlp、twitter-cli、rdt-cli、Jina Reader 等）定期追踪更新到最新版，你不用自己盯

🤖 兼容所有 Agent
Claude Code、OpenClaw、Cursor、Windsurf……任何能跑命令行的 Agent 都能用

🩺 自带诊断
agent-reach doctor 一条命令告诉你哪个通、哪个不通、怎么修

## 支持的平台

| 平台 | 状态 | 说明 |
|------|------|------|
| 🌐 网页 | 装好即用 | 阅读任意网页，无需配置 |
| 📺 YouTube | 装好即用 | 字幕提取 + 视频搜索，无需配置 |
| 📡 RSS | 装好即用 | 阅读任意 RSS/Atom 源，无需配置 |
| 🔍 全网搜索 | 装好即用 | 全网语义搜索，自动配置（MCP 接入，免费无需 Key） |
| 📦 GitHub | 装好即用 | 读公开仓库 + 搜索，私有仓库需配置 |
| 🐦 Twitter/X | 配置后解锁 | 读单条推文、搜索推文、浏览时间线、发推 |
| 📺 B站 | 配置后解锁 | 本地：字幕提取 + 搜索，服务器也能用 |
| 📖 Reddit | 配置后解锁 | 搜索 + 读帖子和评论，需要登录认证 |
| 📕 小红书 | 配置后解锁 | 阅读、搜索、发帖、评论、点赞 |
| 🎵 抖音 | 配置后解锁 | 视频解析、无水印下载链接获取 |
| 💼 LinkedIn | 配置后解锁 | Jina Reader 读公开页面，Profile详情、公司页面 |
| 💬 微信公众号 | 装好即用 | 搜索 + 阅读公众号文章（全文 Markdown） |
| 📰 微博 | 装好即用 | 热搜、搜索内容/用户/话题、用户动态、评论 |
| 💻 V2EX | 装好即用 | 热门帖子、节点帖子、帖子详情+回复、用户信息 |
| 📈 雪球 | 配置后解锁 | 股票行情、搜索股票、热门帖子、热门股票排行 |
| 🎙️ 小宇宙播客 | 配置后解锁 | 播客音频转文字（Whisper 转录，免费 Key） |

## 使用方法

复制这句话给你的 AI Agent（Claude Code、OpenClaw、Cursor 等）：

帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

就这一步。Agent 会自己完成剩下的所有事情。

🔄 已安装过？更新也是一句话：
帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md

## 安全模式

担心安全？可以用安全模式——不会自动装系统包，只告诉你需要什么：
帮我安装 Agent Reach（安全模式）：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
安装时使用 --safe 参数

## 常用指令

不需要任何配置，告诉 Agent 就行：
- "帮我看看这个链接" → curl https://r.jina.ai/URL 读任意网页
- "这个 GitHub 仓库是做什么的" → gh repo view owner/repo
- "这个视频讲了什么" → yt-dlp --dump-json URL 提取字幕
- "帮我看看这条推文" → twitter tweet URL
- "订阅这个 RSS" → feedparser 解析
- "搜一下 GitHub 上有什么 LLM 框架" → gh search repos "LLM framework"

不需要记命令。Agent 读了 SKILL.md 之后自己知道该调什么。

Agent Reach 是一个脚手架（scaffolding），目标是让 AI Agent 能看到整个互联网，而不需要你一个个去踩坑装工具。
