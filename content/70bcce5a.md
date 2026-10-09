# Ultrafast mode

- **ID**: 70bcce5a
- **原文链接**: https://developers.openai.com/api/docs/guides/ultrafast-mode
- **作者**: OpenAI
- **日期**: 2026-10-08
- **分类**: models
- **来源类型**: article
- **标签**: openai, api-pricing, latency, service-tier, agents
- **质量评分**: 4/5
- **抓取时间**: %s

---

## 中文导读

OpenAI API 文档正式定义 **Ultrafast mode**：API 最高速服务档，GPT-6 Astra 与 GPT-6.1 Sol 全面开放（GPT-5.6 Sol 为预览）。用法是请求里 model 不变、`service_tier` 设为 `ultrafast`；官方定义是「缩短生成 output token 之间的间隔」——工具调用、跑测试、等沙箱的时间不在承诺范围内。

文档明确两条工程约束：其一，Ultrafast 与 Standard/Fast **分开限流**，上量前先查组织限额；其二，**强烈建议走 WebSocket 长连接**，尤其对连续多工具调用的 agentic 应用——短连接的网络开销会吃掉延迟收益。开放面为全部 API 用户。

价格与门禁（同日公告帖、价目页与 Codex speed 页，本地草稿已逐项核对）：短上下文 Ultrafast 整体 6 倍价（每百万 token 输入 $12、输出 $60；Standard 为 $2/$10），超 272K 长上下文 $24 / $1.20 / $30 / $90，数据驻留端点再 +10%%。Codex 与 ChatGPT Work 走另一套门：Pro $500 或合格 Enterprise/Edu；订阅 included 用量按 8 倍扣、credits 与 Enterprise 按量按 6 倍扣（Fast 对照 2.5 倍 / 2 倍）。「最高约 8 倍」的口径：公告帖对 Sol 生成速度说的；Codex 页写的是 Astra Ultrafast 相对 Astra Standard 最高约 8 倍。AWS Bedrock 同日上线同档。

## 为什么值得关注

对 agent 工程这是一档「用钱买 token 间隔」的显式开关：人在环、每步等模型出字的场景直接受益；墙钟大头在编译/测试/浏览器的任务收益有限。真正的落点在路由策略——6 倍价差意味着 provider 需要按任务阶段分层选档（交互轮次 Ultrafast、后台批次 Standard），而 TPM 独立限额让它成为容量规划变量而不只是价格变量。

## 关键信息

- model id 不变：`gpt-6-astra` / `gpt-6.1-sol` + `service_tier: "ultrafast"`
- 定义边界：只缩短 output token 间隔，不承诺端到端任务秒数
- 限流独立于 Standard/Fast；全部 API 用户可用
- 短上下文价：$12 输入 / $60 输出（6x Standard）；Fast 为 2x
- >272K 长上下文：$24 / $1.20 / $30 / $90；数据驻留 +10%%
- Codex/ChatGPT Work：Pro $500 门禁；included 8x 扣量、credits 6x
- 官方建议：多工具 agent 循环走 WebSocket
- AWS Bedrock 同日可用（实时 coding assistant / 交互式 agent 场景）

## One-liner

Ultrafast mode 文档落地：service_tier 一行开关，6 倍价买 token 间隔，agent 循环官方建议 WebSocket

## English Summary

OpenAI's API docs now define Ultrafast mode, the fastest service tier, broadly available for GPT-6 Astra and GPT-6.1 Sol (preview for GPT-5.6 Sol). Same model id with service_tier=ultrafast; officially defined as shortening the interval between generated output tokens — tool calls, test runs, and sandbox waits are not covered. Ultrafast has separate rate limits from Standard/Fast and is open to all API users; WebSockets are strongly recommended for agentic tool-call loops. Pricing (per announcement and pricing pages): 6x Standard short-context ($12 in / $60 out per 1M tokens), long-context $24/$1.20/$30/$90, data-residency endpoints +10%%. Codex and ChatGPT Work gate the tier to Pro $500 or qualifying Enterprise/Edu, with subscription usage deducted at 8x and credits at 6x. AWS Bedrock added the same tier the same day.

## 原文摘录

> Ultrafast mode is the fastest service tier in the OpenAI API. It is broadly available for GPT-6 Astra and GPT-6.1 Sol, with preview access for GPT-5.6 Sol. Use it when speed justifies the higher cost.

> We strongly recommend WebSockets, especially for agentic applications that make many tool calls in quick succession. Without a persistent connection, network overhead can reduce the latency gains.

---

> 注：本文件为 daily-intake-evening 内容提取（2026-10-09）；文档页与「最高约 8 倍」口径基于 opencli web read 抓取的原文，价格/扣量/Codex 门禁数字来自同日 OpenAI 公告帖与价目页（本地草稿 Content/Drafts/2026-10-09-TG正文-GPT-6.1-Sol-Ultrafast-同一模型买速度.md 已逐项核对）。
