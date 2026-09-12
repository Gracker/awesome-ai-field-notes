# Habitat: how OpenAI rewrote its Python online-storage service in Rust with two engineers + Codex

> Source: https://openai.com/index/scaling-storage-one-billion-users-part-one/
> Authors: Jon Lee, Chaomin Yu, Ben Ries (Members of Technical Staff, OpenAI)
> Published: 2026-09-11

## 中文摘要

OpenAI 工程博客 Part I（9 月 11 日）公开 Habitat 在线存储平台的核心数据：当前处理 >70M rps、服务 >1B 周活用户、覆盖 ~40 个地理区域、存储 >500PB。2023 年 DevDay 首发时只是 GPTs 用的 Python 客户端库连一个数据库，现在是分布式在线存储系统。Python 路径峰值 >20M rps；2026 Q2 由 2 名工程师 + Codex + GPT-5.5 在不中断在线服务的前提下把整个核心服务用 Rust 改写，新服务已承载 95% 流量，CPU 效率 6×、内存效率 15×（公司自测数据）。Python 路径将在未来几周内彻底下线。

## 关键事实（来自原文）

- 70M+ rps, 1B+ WAU, 500PB+, ~40 regions（blog 开篇）
- Python 峰值 >20M rps（blog 重写节 + 官帖）
- Q2 2026：2 engineers + Codex + GPT-5.5 把 Python 改写成 Rust
- Rust 服务承载 95% 流量；6× CPU、15× mem 效率提升（公司数据）
- Python 路径即将下线
- Part II：存储层与 Azure Cosmos DB

## Obsidian 证据摘要

> 来源：调研/2026-09-12-调研-Habitat-Codex-Rust重写生产存储.md
>
> "唯一问题：Habitat Part I 里 coding agent 重写生产存储可核对哪些数字与边界？ 关键事实：>70M rps / >1B WAU / >500PB / ~40 区域；Python 峰值 >20M；Q2 2026 两人+Codex+GPT-5.5→Rust 95% 流量、6×CPU/15×内存（自述）"
