# OpenComputer: An open-source, faster Devin alternative

- **ID**: 00dcab6d
- **原文链接**: https://github.com/diggerhq/opencomputer
- **作者/来源**: Digger HQ（GitHub: diggerhq）
- **日期**: 2025-12-09（仓库创建）
- **分类**: coding
- **来源类型**: github
- **标签**: open-source, coding-agent, slack, self-hosting
- **质量评分**: 4/5
- **抓取时间**: 2026-11-21T12:26:43Z

---

## 中文解读

diggerhq 开源 OpenComputer：自定位「更快、可自托管的开源 Devin 替代品」。交互形态是在 Slack 线程里 @Computer 派任务，它在自己独立的电脑上干活，团队留在 Slack 里协作；整栈可自托管到你自己的云账号，也可以两分钟起一个 OpenComputer Cloud。Apache-2.0，TypeScript 实现，仓库创建于 2025-12-09；抓取时（2026-11-21）GitHub API 显示 829 stars / 85 forks，此前登上 HN 前页时约 726 stars。文档在 docs.opencomputer.dev，另附「云端智能体与本地一样快」的 benchmark 页。

## 为什么值得关注

闭源 Devin 的开源对标出现，且「Slack 派活 + 智能体自有机器 + 可自托管」的形态可以直接对照；对要自建 coding agent 工程的团队，这是成本和数据边界都握在自己手里的参考实现。

以上判断锚定原文抓取内容，具体数字与说法可在下方 Source excerpt 中对照验证。

## 关键信息

- 标题：OpenComputer: An open-source, faster Devin alternative
- 作者/来源：Digger HQ（GitHub: diggerhq）
- 原文链接：https://github.com/diggerhq/opencomputer
- 发布时间：2025-12-09（仓库创建）
- 关联标签：open-source, coding-agent, slack, self-hosting

## English Summary

diggerhq open-sourced OpenComputer, an Apache-2.0 TypeScript coding agent positioned as an open-source, faster Devin alternative: mention @Computer in a Slack thread with a task and it works on its own computer while the team collaborates in Slack; the stack runs self-hosted in your own cloud account or on OpenComputer Cloud in two minutes. Repo created 2025-12-09; at fetch time (2026-11-21) the GitHub API showed 829 stars / 85 forks (about 726 when it hit the HN front page). Docs at docs.opencomputer.dev plus a benchmark page claiming cloud agents as fast as local ones.

## 原文抓取 / Source excerpt

> 抓取时间: 2026-11-21T12:26:43Z
> 原文链接: https://github.com/diggerhq/opencomputer

<p align="center">
  <img src="docs/images/readme-banner.svg" alt="OpenComputer" width="100%">
</p>

<p align="center">
  The open-source Devin alternative: a coding agent your team works with in Slack, on its own computers, in your cloud or ours.
</p>

<p align="center">
  <a href="https://app.opencomputer.dev">Cloud</a> | <a href="https://docs.opencomputer.dev/self-hosting/overview">Self-hosting</a> | <a href="https://docs.opencomputer.dev">Docs</a> | <a href="https://opencomputer.dev">Website</a> | <a href="https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/">Benchmark</a> | <a href="https://join.slack.com/t/opencomputercommunity/shared_invite/zt-4gtztz4io-~LZMreyHyTryoEVhs2hUPA">Community</a> | <a href="https://x.com/opencomputerHQ">X</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/diggerhq/opencomputer?style=for-the-badge"></a>
  <a href="https://github.com/diggerhq/opencomputer/releases"><img alt="Release" src="https://img.shields.io/github/v/release/diggerhq/opencomputer?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="https://app.opencomputer.dev"><img alt="Try OpenComputer in Slack" src="https://img.shields.io/badge/Try_OpenComputer_in_Slack-4A154B?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BPHRpdGxlPlNsYWNrPC90aXRsZT48cGF0aCBkPSJNNS4wNDIgMTUuMTY1YTIuNTI4IDIuNTI4IDAgMCAxLTIuNTIgMi41MjNBMi41MjggMi41MjggMCAwIDEgMCAxNS4xNjVhMi41MjcgMi41MjcgMCAwIDEgMi41MjItMi41MmgyLjUydjIuNTJ6TTYuMzEzIDE1LjE2NWEyLjUyNyAyLjUyNyAwIDAgMSAyLjUyMS0yLjUyIDIuNTI3IDIuNTI3IDAgMCAxIDIuNTIxIDIuNTJ2Ni4zMTNBMi41MjggMi41MjggMCAwIDEgOC44MzQgMjRhMi41MjggMi41MjggMCAwIDEtMi41MjEtMi41MjJ2LTYuMzEzek04LjgzNCA1LjA0MmEyLjUyOCAyLjUyOCAwIDAgMS0yLjUyMS0yLjUyQTIuNTI4IDIuNTI4IDAgMCAxIDguODM0IDBhMi41MjggMi41MjggMCAwIDEgMi41MjEgMi41MjJ2Mi41Mkg4LjgzNHpNOC44MzQgNi4zMTNhMi41MjggMi41MjggMCAwIDEgMi41MjEgMi41MjEgMi41MjggMi41MjggMCAwIDEtMi41MjEgMi41MjFIMi41MjJBMi41MjggMi41MjggMCAwIDEgMCA4LjgzNGEyLjUyOCAyLjUyOCAwIDAgMSAyLjUyMi0yLjUyMWg2LjMxMnpNMTguOTU2IDguODM0YTIuNTI4IDIuNTI4IDAgMCAxIDIuNTIyLTIuNTIxQTIuNTI4IDIuNTI4IDAgMCAxIDI0IDguODM0YTIuNTI4IDIuNTI4IDAgMCAxLTIuNTIyIDIuNTIxaC0yLjUyMlY4LjgzNHpNMTcuNjg4IDguODM0YTIuNTI4IDIuNTI4IDAgMCAxLTIuNTIzIDIuNTIxIDIuNTI3IDIuNTI3IDAgMCAxLTIuNTItMi41MjFWMi41MjJBMi41MjcgMi41MjcgMCAwIDEgMTUuMTY1IDBhMi41MjggMi41MjggMCAwIDEgMi41MjMgMi41MjJ2Ni4zMTJ6TTE1LjE2NSAxOC45NTZhMi41MjggMi41MjggMCAwIDEgMi41MjMgMi41MjJBMi41MjggMi41MjggMCAwIDEgMTUuMTY1IDI0YTIuNTI3IDIuNTI3IDAgMCAxLTIuNTItMi41MjJ2LTIuNTIyaDIuNTJ6TTE1LjE2NSAxNy42ODhhMi41MjcgMi41MjcgMCAwIDEtMi41Mi0yLjUyMyAyLjUyNiAyLjUyNiAwIDAgMSAyLjUyLTIuNTJoNi4zMTNBMi41MjcgMi41MjcgMCAwIDEgMjQgMTUuMTY1YTIuNTI4IDIuNTI4IDAgMCAxLTIuNTIyIDIuNTIzaC02LjMxM3oiLz48L3N2Zz4%3D"></a>
</p>

<!-- TODO: point each self-host button at its guide once the self-hosting docs are live. -->
<p align="center">
  <a href="https://docs.opencomputer.dev/self-hosting/aws"><img alt="Self-host on AWS" src="docs/images/badge-self-host-aws.svg"></a>
  <a href="https://docs.opencomputer.dev/self-hosting/gcp"><img alt="Self-host on GCP" src="https://img.shields.io/badge/Self--host_on_GCP-4285F4?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BPHRpdGxlPkdvb2dsZSBDbG91ZDwvdGl0bGU%2BPHBhdGggZD0iTTEyLjE5IDIuMzhhOS4zNDQgOS4zNDQgMCAwIDAtOS4yMzQgNi44OTNjLjA1My0uMDItLjA1NS4wMTMgMCAwLTMuODc1IDIuNTUxLTMuOTIyIDguMTEtLjI0NyAxMC45NDFsLjAwNi0uMDA3LS4wMDcuMDNhNi43MTcgNi43MTcgMCAwIDAgNC4wNzcgMS4zNTZoNS4xNzNsLjAzLjAzaDUuMTkyYzYuNjg3LjA1MyA5LjM3Ni04LjYwNSAzLjgzNS0xMi4zNWE5LjM2NSA5LjM2NSAwIDAgMC0yLjgyMS00LjU1MmwtLjA0My4wNDMuMDA2LS4wNUE5LjM0NCA5LjM0NCAwIDAgMCAxMi4xOSAyLjM4em0tLjM1OCA0LjE0NmMxLjI0NC0uMDQgMi41MTguMzY4IDMuNDg2IDEuMTVhNS4xODYgNS4xODYgMCAwIDEgMS44NjIgNC4wNzh2LjUxOGMzLjUzLS4wNyAzLjUzIDUuMjYyIDAgNS4xOTNoLTUuMTkzbC0uMDA4LjAwOXYtLjA0SDYuNzg1YTIuNTkgMi41OSAwIDAgMS0xLjA2Ny0uMjNoLjAwMWEyLjU5NyAyLjU5NyAwIDEgMSAzLjQzNy0zLjQzN2wzLjAxMy0zLjAxMkE2Ljc0NyA2Ljc0NyAwIDAgMCA4LjExIDguMjRjLjAxOC0uMDEuMDQtLjAyNi4wNTQtLjAyM2E1LjE4NiA1LjE4NiAwIDAgMSAzLjY3LTEuNjl6Ii8%2BPC9zdmc%2B"></a>
  <a href="https://docs.opencomputer.dev/self-hosting/azure"><img alt="Self-host on Azure" src="https://img.shields.io/badge/Self--host_on_Azure-0078D4?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BPHRpdGxlPk1pY3Jvc29mdCBBenVyZTwvdGl0bGU%2BPHBhdGggZD0iTTIyLjM3OSAyMy4zNDNhMS42MiAxLjYyIDAgMCAwIDEuNTM2LTIuMTR2LjAwMkwxNy4zNSAxLjc2QTEuNjIgMS42MiAwIDAgMCAxNS44MTYuNjU3SDguMTg0QTEuNjIgMS42MiAwIDAgMCA2LjY1IDEuNzZMLjA4NiAyMS4yMDRhMS42MiAxLjYyIDAgMCAwIDEuNTM2IDIuMTM5aDQuNzQxYTEuNjIgMS42MiAwIDAgMCAxLjUzNS0xLjEwM2wuOTc3LTIuODkyIDQuOTQ3IDMuNjc1Yy4yOC4yMDguNjE4LjMyLjk2Ni4zMm0tMy4wODQtMTIuNTMxIDMuNjI0IDEwLjczOWEuNTQuNTQgMCAwIDEtLjUxLjcxM3YtLjAwMWgtLjAzYS41NC41NCAwIDAgMS0uMzIyLS4xMDZsLTkuMjg3LTYuOWg0Ljg1M202LjMxMyA3LjAwNmMuMTE2LS4zMjYuMTMtLjY5NC4wMDctMS4wNThMOS43OSAxLjc2YTEuNzIyIDEuNzIyIDAgMCAwLS4wMDctLjAyaDYuMDM0YS41NC41NCAwIDAgMSAuNTEyLjM2Nmw2LjU2MiAxOS40NDVhLjU0LjU0IDAgMCAxLS4zMzguNjg0Ii8%2BPC9zdmc%2B"></a>
</p>

## Introduction

OpenComputer is the open source, self hostable alternative to Devin. Mention `@Computer` in a Slack thread with a task, it works on its own computer, you & your team can watch and steer it as it goes, and the result lands as a pull request.

It is open source from the compute layer up, so you can run all of it in your own cloud account, or start on OpenComputer Cloud in two minutes.

We built it to feel as fast as Claude Code on your laptop: in our benchmark it opens PRs 3.3x faster than Devin.

## See it work

<p align="center">
  <img src="docs/images/readme-slack.gif" alt="A Slack thread: someone mentions @Computer, and it replies in the thread within seconds" width="70%">
</p>

## As fast as local

<p align="center">
  <img src="docs/images/readme-vs-local.gif" alt="Side-by-side race on the same task: Claude Code on a laptop against @Computer in the cloud; @Computer finishes in 32.0s, local in 36.2s" width="70%">
</p>

## How it works

OpenComputer is built to be simple to self-host without giving up scale or security. The whole stack runs on a single VM, which we recommend locking down to outbound-only network access.

The VM runs the gateway, Calvin: a thin bridge that listens for Slack events and starts a session with Claude Code, Codex or OpenCode, depending on your configuration. Each session is isolated with rootless Podman. Its state is written first to the VM's local disk, then persisted to a git-backed store.

The rest of the stack runs on Cloudflare Workers and Durable Objects. Support for Fly and other platforms is coming soon.

<p align="center">
  <img src="docs/images/readme-architecture.png" alt="Slack sends events to Cloudflare Workers and Durable Objects. Your VM, outbound only, dials out to them over a websocket. On the VM, the Calvin gateway starts a Claude Code, Codex or OpenCode session per thread, each in rootless Podman. State is written to the VM's local disk first, then persisted to a git-backed store." width="100%">
</p>

## Try it in Cloud

The fastest way to experience `@Computer` is to install the Slack app from the cloud: [sign up here](https://app.opencomputer.dev), connect your repos, and install the Slack app to get started.

<p align="center">
  <a href="https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/"><img src="docs/images/readme-benchmark.gif" alt="Slack message to first push, median of 5 runs: @Computer finishes first, ahead of Replicas, Capy, Hoplite and Devin" width="70%"></a>
</p>

- **3.3x faster than Devin**: all 4 PRs open with CI green in 56s vs 185s ([benchmark](https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/))
- **2.6x faster than the average of the 4 most popular cloud agents**: first push in 24s vs a 62s average ([benchmark](https://opencomputer.dev/blog/cloud-agents-as-fast-as-local/))
- **3-day free trial** with 600 work minutes
- **Bring your own ChatGPT / Codex subscription**

## License

Apache 2.0. See [LICENSE](LICENSE).

……（截取窗口，非全文）

## Obsidian Notes

- opencli web read 被拒后改用 GitHub API（repos + readme 端点）抓取；stars/forks/license/语言为 2026-11-21 API 快照。
- 正文 excerpt 为仓库 README 全文。
