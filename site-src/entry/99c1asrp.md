---
title: '别再刷了——ClawFeed 帮我每天 5 分钟搞定 5000 人的信息流'
sidebar: false
---

::: info
[← 返回行业观察](/industry)
:::

# 别再刷了——ClawFeed 帮我每天 5 分钟搞定 5000 人的信息流

> 信息过载的自动化筛选方案，5 分钟处理 5000 人信息流

🔗 [原文链接](https://x.com/0xkevinhe/status/2025781752971809010) | @Kevin He | 🇨🇳 | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-02-23

`clawfeed` `information-filtering` `openclaw` `workflow` `automation`

---

## 别再刷了——ClawFeed 帮我每天 5 分钟搞定 5000 人的信息流

### 真实效果

ClawFeed 上线 10 天的数据：

指标数据持续运行10 天简报数量54 份结构化摘要每日耗时5 分钟

Before → After：

BeforeAfter信息处理每天 2 小时刷 feed5 分钟看 AI 摘要焦虑感总觉得错过了什么重要的自动浮出来深度内容收藏 500 篇读 5 篇标记后 AI 直接深度分析噪声100% 暴露AI 过滤 95%

### 怎么做的

ClawFeed 不是一开始就是现在这个样子。它经历了几个关键阶段：

v0 — Markdown + Telegram。让 Agent 生成 markdown 摘要，通过 Telegram 推送。粗糙但能用。

v0.2 — SQLite + API。转折点。有了后端，从"脚本"变成了"服务"。

v0.3 — Web Dashboard。暗色主题 SPA，终于像个产品了。

v0.5 — OAuth 多用户。加了 Google OAuth，别人也能用。

关键取舍

零框架依赖。 没用 Express、Koa、Fastify，直接用 Node.js 原生 HTTP server。依赖列表里只有一个 better-sqlite3。依赖少 = 维护少 = 安全风险少。不到 50MB 内存。

摘要格式：@username + 原话。 "@karpathy 说 transformer 不是终点"比"业界讨论模型架构演进"有用得多。

作为 OpenClaw Skill + Zylos Component 双发布。 标准 SKILL.md / component.json，一行命令安装。OpenClaw 和 Zylos 用户都能直接用——两个 Agent 生态，同一个 ClawFeed。

### 少刷多知。

信息焦虑的本质是筛选成本。把筛选交给 Agent，焦虑就消失了。

开源版 — 完全掌控你的数据
GitHub: kevinho/clawfeed ⭐
MIT 协议，clone 下来装个 better-sqlite3 就能跑。

线上版 — 无需注册，打开即用
clawfeed.kevinhe.io

▶ 30 秒看懂 ClawFeed：

少刷多知。

Built by openclaw.ai 🦞 & zylos.ai 🐙

Twitter: @0xkevinhe
