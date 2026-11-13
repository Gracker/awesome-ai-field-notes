# Apple Foundation Models framework: native Swift API for on-device and Private Cloud Compute LLMs

- **ID**: 1dba3a3e
- **原文链接**: https://developer.apple.com/foundation-models-framework
- **作者**: Apple Developer
- **日期**: 2026-11-12
- **更新**: N/A
- **分类**: coding
- **来源类型**: product
- **标签**: apple, on-device, llm, swift, framework, private-cloud-compute, tool-calling
- **质量评分**: 4/5
- **抓取时间**: 2026-11-13T04:23:05+00:00

---

## 中文导读

Apple 开发者页系统介绍 Foundation Models framework：原生 Swift API，可在应用内使用任意大模型，包括直连设备端 Apple 基础模型与 Private Cloud Compute，定位从快速摘要到动态 agent 的标准接法页面列出引导式生成tool calling图像理解Dynamic Profiles服务端模型支持与评测框架等能力，并附 WWDC 2025/2026 视频与生成式 AI HIG 指南HN 讨论（88 分）聚焦能否搭配非 API 订阅的 Claude/ChatGPT，以及与 Firebase 直连 LLM 方案的对比

## 为什么值得关注

Apple 开发者页系统介绍 Foundation Models framework：原生 Swift API，可在应用内使用任意大模型，包括直连设备端 Apple 基础模型与 Private Cloud Compute.

中文导读与价值判断锚定在条目已有摘要与抓取到的正文/摘要、作者、日期与分类信息上；未补充源摘要之外的实验细节。

## 关键信息

- 标题：Apple Foundation Models framework: native Swift API for on-device and Private Cloud Compute LLMs
- 作者：Apple Developer
- 链接：https://developer.apple.com/foundation-models-framework
- 发布时间：2026-11-12
- 关联标签：apple, on-device, llm, swift, framework, private-cloud-compute, tool-calling

## English Summary

Apple's Foundation Models framework page positions a native Swift API for using any large language model in an app - including direct access to Apple's on-device Foundation Models and Private Cloud Compute - as the standard way to build AI features, from quick summaries to dynamic agents. Built-in capabilities include guided generation, tool calling, image understanding, Dynamic Profiles, server model support, and an evaluations framework, with an open-source section, WWDC 2025/2026 sessions, and Human Interface Guidelines for generative AI. HN discussion (88 points) focuses on whether non-API Claude/ChatGPT subscription plans can be used with it and compares it to calling LLMs directly from iOS via Firebase-based setups.

## English Excerpt

# Foundation Models framework
> 原文链接: https://developer.apple.com/foundation-models-framework

---

![](https://developer.apple.com/assets/elements/icons/foundationmodel/foundationmodel-128x128_2x.png)

# Get started with the Foundation Models framework

The Foundation Models framework is the best way to use any large language model in your app. Whether you’re generating a quick summary or creating dynamic agents, the framework has what you need.

-   [Overview](#overview)
-   [Image understanding](#image-understanding)
-   [Model support](#server-model-support)
-   [Dynamic Profiles](#dynamic-profiles)
-   [Evaluations framework](#evaluations-framework)
-   [CLI](#cli)
-   [Open source](#open-source)
-   [Requirements](#requirements)

## Overview

The Foundation Models framework is a native Swift API for integrating any large language model into your app — including direct access to the Apple Foundation Models on-device and in Private Cloud Compute. Powerful capabilities like guided generation, tool calling, image understanding, and Dynamic Profiles are built in, so you have what you need to build unique experiences.

[

![](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/10764/10764_wide_250x141_2x.jpg)

#### What’s new in the Foundation Models framework

](https://developer.apple.com/videos/play/wwdc2026/241/)[

![](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/5647196D-90F3-4FC0-851F-7CF0F69BE7D2/9965_wide_900x506_2x.jpg)

#### Meet the Foundation Models framework

](https://developer.apple.com/videos/play/wwdc2025/286/)

-   [Foundation Models framework](https://developer.apple.com/documentation/foundationmodels/)
-   [Human Interface Guidelines for Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai/)

## Image understanding

Multimodal prompts let you pass images alongside text so your app can reason about visual content. This opens up new categories of experiences you can build with image understanding — it's as simple as attaching an image to your prompt. The Vision framework is also integrated directly, giving your model purpose-built tools like OCR for precise text extraction and barcode readers for quick code scanning — all on-device.

[

![](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/10760/10760_wide_250x141_2x.jpg)

#### What’s new in image understanding

](https://developer.apple.com/videos/play/wwdc2026/237/)

## Model support

The Foundation Models framework gives you direct access to the on-device foundation model at the core of Apple Intelligence so you can build experiences that are smart, private, and work without internet connectivity.

On-device models are hi

## Obsidian Notes

- 内容由 opencli 拉取源页面/论文元数据后生成。
- 中文导读与价值判断锚定在条目已有摘要与抓取到的正文/摘要、作者、日期与分类信息上；未补充源摘要之外的实验细节。
- fetch: opencli-web
