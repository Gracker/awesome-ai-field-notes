# GPT-5.5: OpenAI's Smartest Model Yet for Coding, Research, and Data Analysis

- **来源**: OpenAI
- **原文链接**: https://openai.com/index/introducing-gpt-5-5
- **作者**: OpenAI
- **日期**: 2026-04-23
- **分类**: models
- **标签**: GPT-5.5, OpenAI, coding, research, data-analysis, agentic, 2026
- **抓取时间**: 2026-06-13 04:28

---

## English Original

**Note**: The OpenAI announcement page at openai.com is gated behind Cloudflare Turnstile (bot challenge) and could not be fetched directly. Content below is compiled from the OpenAI API model documentation at developers.openai.com/api/docs/models/gpt-5.5 plus the Wikipedia entry on GPT-5.5 (which cites OpenAI's announcement directly).

---

GPT-5.5 (Generative Pre-trained Transformer 5.5) is a large language model released by OpenAI on April 23, 2026. The model is also known by its codename "Spud".

## Overview

GPT-5.5 is OpenAI's newest frontier model designed for the most complex professional work, with particular strength in coding, research, and data analysis across tools. OpenAI called it their "smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools."

## Model Variants

- **GPT-5.5** — base model, available in ChatGPT and Codex starting April 23, 2026 (API from April 24).
- **GPT-5.5 Pro** — higher-quality variant released alongside GPT-5.5 on April 23.
- **GPT-5.5 Thinking** — reasoning mode released April 23, supports reasoning effort levels: none, low, medium (default), high, and xhigh.
- **GPT-5.5 Instant** — released to free-tier ChatGPT users on May 5, 2026, replacing GPT-5.3 Instant as the default model.
- **GPT-5.5-Cyber** — limited-preview variant for vetted cybersecurity teams, announced May 7, 2026 under OpenAI's Trusted Access for Cyber program.

## Specifications (from OpenAI API docs)

- **Context window**: 1,050,000 tokens
- **Max output**: 128,000 tokens
- **Knowledge cutoff**: Dec 01, 2025
- **Modalities**: text + image input, text output
- **Pricing**: $5.00 / 1M input, $0.50 / 1M cached input, $30.00 / 1M output (prompts over 272K tokens priced at 2× input and 1.5× output)
- **Snapshots**: `gpt-5.5`, `gpt-5.5-2026-04-23`
- **Reasoning**: supports `reasoning_effort` parameter

## Benchmark Scores (per OpenAI's announcement)

- Terminal-Bench 2.0: 82.7%
- FrontierMath Tier 1–3: 51.7%
- FrontierMath Tier 4: 35.4%

These are presented as narrowly beating Anthropic's Claude Opus 4.7 and Gemini 3.1 Pro on Terminal-Bench 2.0.

## Capabilities

GPT-5.5 reduces safety issues, supports agentic autonomy and reasoning, and integrates into ChatGPT and Codex. Key use cases highlighted:

- Faster understanding of user intent
- Writing and debugging code
- Online research
- Data analysis
- Document creation
- Improved token efficiency

## Reception

ZDNET praised GPT-5.5 for its polished answers and "[s]trong performance across writing, coding, and reasoning tasks". Compared to its predecessor, the website described GPT-5.5 as better, faster, and showing "improvements in agentic coding, conceptual clarity, scientific research ability, and accuracy during knowledge work."

The AI Security Institute reported that GPT-5.5 had a 71.4% (±8.0%, one standard error) average pass rate on its expert-level cyber tasks, compared with 68.6% (±8.7%) for Anthropic's Claude Mythos Preview, and said GPT-5.5 "may be the strongest model we have tested" on that measure.

## The Goblin Story

In a notable side-story, OpenAI acknowledged that a recurring tendency in its models to mention goblins, gremlins, and other creatures began with GPT-5.1 and became noticeable in GPT-5.5's Codex testing. The company attributed the behavior to rewards used when training the "Nerdy" personality, which favored creature-word outputs and transferred beyond that personality during later training. OpenAI said it retired the Nerdy personality, removed the goblin-affine reward signal, filtered training data containing creature words, and added a developer-prompt instruction for GPT-5.5 in Codex to not mention goblins unless the user prompt requires it.

## API and Tools

GPT-5.5 supports the Responses API, Chat Completions, Batch, Realtime (and realtime translation/transcription), Assistants, Embeddings, Image generation, Image edit, Speech generation, Transcription, Translation, and Moderations endpoints. Tool support includes: Web search, File search, Image generation, Code interpreter, Hosted shell, Apply patch, Skills, Computer use, MCP, Tool search.


---

## 中文翻译

**说明**：OpenAI 发布页 openai.com 受到 Cloudflare Turnstile（机器人挑战）保护，无法直接抓取。以下内容综合自 OpenAI 开发者文档 developers.openai.com/api/docs/models/gpt-5.5 以及 Wikipedia 上的 GPT-5.5 条目（其中直接引用了 OpenAI 的公告）。

---

GPT-5.5（Generative Pre-trained Transformer 5.5）是 OpenAI 于 2026 年 4 月 23 日发布的大语言模型，开发代号 "Spud"。

## 概述

GPT-5.5 是 OpenAI 最新的前沿模型，专为最复杂的专业工作设计，在编码、研究与跨工具数据分析方面表现尤为突出。OpenAI 称其为"迄今为止最聪明的模型——更快、更强，专为编码、研究、跨工具数据分析等复杂任务而生"。

## 模型变体

- **GPT-5.5**：基础模型，2026 年 4 月 23 日起在 ChatGPT 与 Codex 中可用（API 4 月 24 日开放）。
- **GPT-5.5 Pro**：与 GPT-5.5 同日发布的更高质量版本。
- **GPT-5.5 Thinking**：4 月 23 日发布的推理模式，支持 reasoning effort 等级：none、low、medium（默认）、high、xhigh。
- **GPT-5.5 Instant**：2026 年 5 月 5 日发布给免费用户，替代 GPT-5.3 Instant 成为 ChatGPT 默认模型。
- **GPT-5.5-Cyber**：2026 年 5 月 7 日发布的有限预览版，面向通过 OpenAI "Trusted Access for Cyber" 计划审核的网络安全团队。

## 规格（来自 OpenAI API 文档）

- **上下文窗口**：1,050,000 tokens
- **最大输出**：128,000 tokens
- **知识截止**：2025 年 12 月 1 日
- **模态**：文本 + 图像输入，文本输出
- **定价**：$5.00 / 百万输入 tokens，$0.50 / 百万缓存输入 tokens，$30.00 / 百万输出 tokens（输入超过 272K tokens 时按 2× 输入 + 1.5× 输出计费）
- **快照版本**：`gpt-5.5`、`gpt-5.5-2026-04-23`
- **推理**：支持 `reasoning_effort` 参数

## 基准测试（OpenAI 公告数据）

- Terminal-Bench 2.0：82.7%
- FrontierMath Tier 1–3：51.7%
- FrontierMath Tier 4：35.4%

OpenAI 称这些成绩在 Terminal-Bench 2.0 上以微弱优势领先 Anthropic 的 Claude Opus 4.7 与 Gemini 3.1 Pro。

## 主要能力

GPT-5.5 减少了安全问题，支持代理自主性与推理能力，已集成到 ChatGPT 与 Codex 中。重点用例：

- 更快理解用户意图
- 编写与调试代码
- 在线研究
- 数据分析
- 文档创建
- token 效率提升

## 行业反响

ZDNET 称赞 GPT-5.5 答案流畅，在写作、编码与推理任务上"表现强劲"。相比前代，该网站描述 GPT-5.5 更优、更快，并在"代理编码、概念清晰度、科研能力与知识工作准确性"方面均有提升。

AI Security Institute 报告 GPT-5.5 在其专家级网络任务上的平均通过率为 71.4%（±8.0%，一个标准误差），而 Anthropic Claude Mythos Preview 为 68.6%（±8.7%），并表示 GPT-5.5 在该指标上"可能是我们测试过的最强模型"。

## "哥布林"趣闻

一件值得记录的轶事：OpenAI 承认其模型中反复出现提及哥布林（goblins）、 gremlins 等生物的倾向始于 GPT-5.1，并在 GPT-5.5 的 Codex 测试中变得明显。OpenAI 将该行为归因于训练"Nerdy"人格时使用的奖励——偏好产生"生物词"的输出，并在后续训练中外溢到其他人格。OpenAI 表示已停用 Nerdy 人格、移除偏好哥布林的奖励信号、过滤训练数据中的"生物词"，并在 Codex 中为 GPT-5.5 添加了开发者提示指令：除非用户提示要求，否则不提及哥布林。

## API 与工具

GPT-5.5 支持 Responses API、Chat Completions、Batch、Realtime（含实时翻译/转录）、Assistants、Embeddings、图像生成、图像编辑、语音生成、转录、翻译、Moderation 等端点。工具支持包括：Web 搜索、文件搜索、图像生成、代码解释器、托管 Shell、Apply patch、Skills、Computer use、MCP、Tool search。

