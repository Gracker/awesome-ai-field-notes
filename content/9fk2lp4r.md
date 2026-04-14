# Building A Generative AI Platform

## English
Building A Generative AI PlatformJul 25, 2024•Chip HuyenAfter studying how companies deploy generative AI applications, I noticed many similarities in their platforms. This post outlines the common components of a generative AI platform, what they do, and how they are implemented. I try my best to keep the architecture general, but certain applications might deviate. This is what the overall architecture looks like.This is a pretty complex system. This post will start from the simplest architecture and progressively add more components. In its simplest form, your application receives a query and sends it to the model. The model generates a response, which is returned to the user. There are no guardrails, no augmented context, and no optimization. TheModel APIbox refers to both third-party APIs (e.g., OpenAI, Google, Anthropic) and self-hosted APIs.From this, you can add more components as needs arise. The order discussed in this post is common, though you don’t need to follow the exact

## 中文
构建生成式AI平台

Chip Huyen
2024年7月25日

在研究了公司如何部署生成式AI应用后，我注意到他们的平台有很多相似之处。本文概述了生成式AI平台的常见组件、它们的功能以及实现方式。我尽力保持架构的通用性，但某些应用可能会有所不同。

...

## 翻译说明
本文为技术文档翻译，采用双语对照格式。原文为Chip Huyen的《Building A Generative AI Platform》，详细介绍了生成式AI平台的架构设计和组件实现。

**原文链接**: https://huyenchip.com/2024/07/25/genai-platform.html?s=09
**质量评分**: 4
**语言**: English -> Chinese
**来源平台**: blog
