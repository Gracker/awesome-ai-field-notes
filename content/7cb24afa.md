# Extensible Software in the age of LLMs

- **ID**: 7cb24afa
- **原文链接**: https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/
- **作者**: Jeremy Morrell
- **日期**: 2026-08-18
- **来源类型**: blog
- **标签**: llm, extensibility, sandbox, capability-model, web-platform
- **质量评分**: 4/5
- **抓取时间**: 2026-08-20T15:44:49Z

---

## 中文导读

Cloudflare 工程师长文：web 是最成功的软件分发渠道，但静态网页无法承载 LLM 时代用户用自然语言说出的长尾扩展需求。浏览器侧需要一个像 Salesforce Apex 那样能安全运行任意用户代码的机制。文章系统铺开基础设施层的权衡：解释器（Lua/QuickJS）、V8 isolate、MicroVM（Firecracker/libkrun）、WASM+WASI，并论证 capability 模型优于 proxy 加鉴权 token 的设计，给出 Object Capability 协议（Cap'n Web）作为能力而非授权的范式，落点是把 LLM 与 sandbox primitive 拼起来让 SaaS 可被自然语言扩展。

## 为什么值得关注

LLM 时代的 Web 可扩展性设计图谱：从解释器到 MicroVM 的隔离权衡与 capability 模型范式

## 原文摘录 (English Excerpt)

Most of the web software we interact with today is static. The developers have a limited amount of time and attention, and focus on building the features that serve the largest group of users. The top of the demand curve is well-served by existing software, but there is a long-tail of unmet needs that’s different for every user.

[![Chart: long-tail distribution of mapping user needs, from common navigation questions to niche historical queries](https://jeremymorrell.dev/_astro/google-maps-long-tail-diagram.CetMzOur_qQTPR.webp)](https://x.com/tophtucker/status/1280992756278714373)

User needs in mapping software

[Even if the developers were incredibly motivated to shove in every feature, user interfaces can only become so complex before they become unusable.](https://newsletter.getprimitive.ai/p/when-to-design-for-emergence) Every additional feature added complicates the product for every other user. If the market for that feature is small, it can actively make the product worse for e

## Obsidian 证据

- 来源 digest: ClawFeed 24h 一览 2026-08-20（2026-08-20，评分 8.4）
- 原文经 opencli web read / opencli arxiv paper 抓取核对，关键数字与摘要均锚定抓取内容。
