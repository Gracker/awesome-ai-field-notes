# Cf: The Agentic CLI for the Cloudflare API

> 原文链接: https://blog.cloudflare.com/cloudflare-cf-cli-launch
> 作者: Cloudflare
> 发布时间: 2026-09-28
> 源: arXiv外部扫描 (2026-09-29)

---

## 摘要

Cloudflare 开启 cf CLI 公测：为 agent 而建的命令行，覆盖整个 Cloudflare API（对比 Wrangler 手写的约 280 条命令路径）直接动因是 agent 占 Wrangler 用量从 2026 年 3 月的 25% 涨到上周的 48%，且 agent 每日使用的不同命令数接近人类两倍设计取向明确服务 agent：bespoke search/steering 帮 agent 找命令，JSON 默认接口并为 agent 压缩省上下文，cloudflare.config.ts 用 TypeScript + LSP 做配置校验，Vite 成默认 dev server

## English Summary

Cloudflare launched cf, an open-beta CLI built for agentic development that exposes the entire Cloudflare API rather than Wrangler's ~280 hand-built command paths. The trigger: agents went from a quarter of Wrangler usage in March 2026 to 48% last week, run almost twice as many distinct commands per day, and are four times as likely to use six or more commands. cf ships bespoke search and steering so agents can find any command, JSON as the default interface (condensed for agents to save context), and cloudflare.config.ts as a TypeScript configuration format checked by the language server. Vite becomes the default dev server.

## 为什么值得关注

扩展 AAIF 对应主题线

## 信息源

- https://blog.cloudflare.com/cloudflare-cf-cli-launch
