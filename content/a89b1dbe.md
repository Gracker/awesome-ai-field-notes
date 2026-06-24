# Interactions API: our primary interface for Gemini models and agents

> 抓取时间：2026-06-24
> 源站：Google Blog
> 主题：Interactions API GA

---

## English Original

# Interactions API: our primary interface for Gemini models and agents

> Authors: Ali Çevik (Group Product Manager, Google DeepMind), Philipp Schmid (Developer Relations Engineer, Google DeepMind)
> Published: 2026-06-22
> Source: https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability

A single unified endpoint for Gemini models and agents with server-side state, background execution, tool combination and multimodal generation.

Today we're announcing that the Interactions API has reached general availability and is now our primary API for interacting with Gemini models and agents. We launched its public beta in December 2025, and it has quickly become developers' favorite way to build applications with Gemini. With this GA release, the API now has a stable schema and we also added major new capabilities that developers asked for, including Managed Agents, background execution, Gemini Omni (soon) and more. All of our documentation now defaults to Interactions API and we are working with ecosystem partners to make it the default interface across 3P SDKs and Libraries.

## The simplest way to build with Gemini

Whether you're calling a model or running an agent, the Interactions API gets you there in a few lines of code. Pass a model ID for inference, an agent ID for autonomous tasks, set `background=True` for anything long-running.

## Key updates since December

- **Managed Agents**: A single API call provisions a remote Linux sandbox where an agent can reason, execute code, browse the web and manage files. The Antigravity agent ships as the default, and you can define your own custom agents with instructions, skills and data sources.
- **Background execution**: Set `background=True` on any call. The server runs the interaction asynchronously.
- **Tool improvements**: Mix built-in tools, such as Google Search, Google Maps with your own functions in one request. Tool results can now return images alongside text.
- **Deep Research upgrades**: Two new agent versions (speed vs. depth), collaborative planning, native charts and infographics, and multimodal grounding with images, PDFs and audio.
- **Media generation**: Image generation with Nano Banana 2 and Google Image Search grounding, music with Lyria 3, and expressive speech with multi-speaker TTS.
- **From Roles to Steps**: Simplified schema where every action (user_input, thought, function_call, model_output, etc.) is its own typed step, replacing the old role structure.
- **Cost and developer optimizations**: Flex and Priority tiers let you optimize for cost or latency (Flex offers 50% cost reduction). Errors now pinpoint the exact field. Past interactions are retrievable with 55-day retention on the paid tier.

## The new standard for development

The Interactions API is now the default for Google AI Studio, the Gemini API, and all our documentation, which includes a toggle to switch snippets back to the legacy format. We recommend using the Interactions API for all new projects and applications. While the legacy generateContent API remains fully supported and will continue to receive new mainline Gemini models for the foreseeable future, we expect frontier capabilities for long-running models and agents to increasingly land exclusively on the Interactions API. This is because it is designed from the ground up for stateful, agentic workflows. We have published a migration guide to help you transition at your own pace.

## An agent-first ecosystem

Most developers are now using coding agents (such as Antigravity) to build applications. To make it easier for agents to stay up to date with the latest API patterns, we built the gemini-interactions-api Skill. It injects best-practice patterns for Interactions API development into your agent's context (streaming, function calling, structured output, Deep Research and more).

## Get started

The Interactions API is available through the Python and JavaScript SDKs. If you're already building with one of our supported partners, LiteLLM, Eigent or Agno, you can start using their Interactions API integrations today. Grab your API key from Google AI Studio and follow the Interactions API documentation to get started. If you're migrating from generateContent, our migration guide maps every field to the new schema. You can also view the full API Reference.

The Interactions API was built based on developer feedback, and that focus won't change with general availability. Tell us what you need on the developer forum.


---

## 中文翻译

# Interactions API：面向 Gemini 模型与智能体的统一主接口

> 作者：Ali Çevik（Google DeepMind 产品组经理）、Philipp Schmid（Google DeepMind 开发者关系工程师）
> 发布时间：2026 年 6 月 22 日
> 原文链接：https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability

一个统一的端点，承载 Gemini 模型与智能体交互所需的一切：服务端状态、后台执行、工具组合、多模态生成。

我们今天正式宣布 Interactions API 进入 **GA（General Availability）** 阶段，并已成为我们与 Gemini 模型和智能体交互的**主 API**。该 API 的公开测试版于 2025 年 12 月上线，上线后迅速成为开发者构建 Gemini 应用的首选方式。本次 GA 发布带来了稳定的 schema，并新增了开发者呼声最高的几大能力：**Managed Agents**、**后台执行**、**Gemini Omni**（即将到来）等。我们的全部文档现已默认使用 Interactions API，并正在与生态伙伴合作，让它成为 3P SDK 与库的默认接口。

## 用 Gemini 构建的最简方式

无论你是调用一个模型，还是运行一个智能体，Interactions API 都能用几行代码搞定。传一个 `model_id` 用于推理，传一个 `agent_id` 用于自主任务；任何长时运行的事情，把 `background=True` 打开即可。

## 自去年 12 月以来的关键更新

- **Managed Agents**：一次 API 调用即在远程 Linux 沙箱中预置一个智能体——它可以推理、执行代码、浏览网页、管理文件。Antigravity 智能体作为默认出厂；你也可以通过 instructions、skills、data sources 来定义自己的智能体。
- **后台执行（Background execution）**：在任何调用上加 `background=True`，服务器即异步执行该交互。
- **工具改进**：在一个请求中可同时混用 Google Search、Google Maps 等内置工具与你的自定义函数。工具结果现在可以同时返回图像与文本。
- **Deep Research 升级**：两个新智能体版本（速度优先 / 深度优先）、协作式规划、原生图表与信息图，以及图像/PDF/音频的多模态 grounding。
- **媒体生成**：使用 Nano Banana 2 与 Google Image Search grounding 的图像生成、Lyria 3 音乐生成，以及支持多说话人的表现力 TTS。
- **从 Roles 到 Steps**：全新的精简 schema——每个动作（user_input、thought、function_call、model_output 等）都是其独立的类型化 step，替代旧的 role 结构。
- **成本与开发者优化**：Flex 与 Priority 等级让你在成本与延迟之间取舍（Flex 提供 50% 的成本下降）。错误信息现在能精确定位到具体字段。历史交互在付费档提供 55 天留存可检索。

## 新的开发标准

Interactions API 现在是 Google AI Studio、Gemini API 以及我们所有文档的默认接口，文档中提供了一个开关可以切回旧版代码片段。我们推荐所有新项目和新应用都使用 Interactions API。旧版 generateContent API 仍受到完全支持，并将继续接收新的主线 Gemini 模型，但面向长时间运行模型与智能体的前沿能力，预计会越来越多地**独家登陆 Interactions API**。这是因为 Interactions API 是从一开始就为有状态的、agentic 的工作流设计的。我们已经发布了一篇迁移指南，让你按自己的节奏完成过渡。

## 智能体优先的生态

如今大多数开发者都在用编码智能体（比如 Antigravity）来构建应用。为了让智能体更容易跟上最新的 API 模式，我们构建了 `gemini-interactions-api` **Skill**。它会把 Interactions API 开发的最佳实践模式（流式输出、函数调用、结构化输出、Deep Research 等）注入到你智能体的上下文里。

## 快速上手

Interactions API 通过 Python 与 JavaScript SDK 提供。如果你在用我们支持的合作伙伴——LiteLLM、Eigent 或 Agno——今天就可以直接使用它们的 Interactions API 集成。打开 Google AI Studio 拿到你的 API key，然后跟着 Interactions API 文档开始即可。如果你在从 generateContent 迁移，我们的迁移指南会逐一映射每个字段到新 schema。你也可以查阅完整 API 参考。

Interactions API 是基于开发者反馈构建的，这种以开发者为中心的关注在 GA 后也不会改变。在开发者论坛上告诉我们你的需求。


---

*本文由 openclaw cron 自动抓取/汇总生成。*
