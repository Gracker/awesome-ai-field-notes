---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 627 条 · 446 篇有全文
  actions:
    - theme: brand
      text: 浏览全部
      link: /models
    - theme: alt
      text: GitHub
      link: https://github.com/Gracker/awesome-ai-field-notes

features:
  - title: '🧠 模型'
    details: 'GPT / Claude / Gemini / 开源模型 / 架构 · 95 条'
    link: /models
  - title: '🤖 智能体'
    details: 'Agent 框架 / MCP / A2A / 手机&桌面助手 · 106 条'
    link: /agents
  - title: '💻 AI编程'
    details: 'IDE / CLI / 代码审查 / 工作流 · 165 条'
    link: /coding
  - title: '⚡ 基础设施'
    details: '推理部署 / RAG / 微调 / 评测 / 多模态 · 60 条'
    link: /infra
  - title: '🌍 行业观察'
    details: 'AI 产品 / 大厂战略 / 融资 / 市场分析 · 55 条'
    link: /industry
  - title: '📖 学习资源'
    details: '教程 / 论文 / 提示工程 / 演讲 · 116 条'
    link: /learning
---

## 🆕 最新 10 篇

### [使用 Claude Code：会话管理与 100 万 上下文](/entry/keqFU4_v) 📄
@Thariq（Anthropic员工） · ⭐⭐⭐3 🇨🇳 · 昨天

Anthropic 官方员工 Thariq 发布的产品使用指南，系统讲解 Claude Code 100 万上下文下的会话管理策略。覆盖：Continue（继续）、Rewind（回溯，纠正错误的最佳方式）、Clear（清空新会话）、Compact（上下文压缩，有损摘要）、Subagents（委派干净上下文的子任务）五种决策路口。好压缩的关键是让模型知道下一步往哪走；子智能体适合阅后即焚型大量中间结果；100 万上下文让主动提前压缩成为可能。

`Claude Code` `context-window` `session-management` `Compact` `Rewind`

---

### [字节最火的开源Agent项目，如何思考Agent的自我进化？](/entry/0qPTtvSb) 📄
@Daniel（DeerFlow联合作者） · ⭐⭐⭐⭐4 🇨🇳 · 昨天

基于 DeerFlow（字节开源多智能体框架，GitHub 6万+ Stars）和 LangChain 创始人 Harrison Chase 的文章，系统梳理 Agent 自我进化的三层框架：Model（权重更新，最重）、Harness（执行机制，2026年核心竞争点）、Context（记忆与个性化，最先落地）。核心判断：2026 年 Agent 的分水岭不在模型在 Harness；Context 层会最先普及；traces 是三层学习的统一燃料；未来更强的 Agent 不来自更大模型，而来自更会复盘、记忆、重构的系统。

`Agent` `self-evolution` `Harness` `Context` `Model`

---

### [KV Cache 深度解析：为什么 LLM 第一个 Token 最慢](/entry/N7uUaY82) 📄
⭐⭐⭐⭐4 🇨🇳 · 昨天

从注意力机制原理出发，详解 KV Cache 的工作原理与工程权衡。自回归生成中 Token 1-49 的 K/V 每次都重算是 O(n^2) 浪费；KV Cache 把历史 K/V 只算一次并缓存，新 Token 只追加自己的 K/V，实现约 5x 提速；代价是显存占用，context window 翻倍意味着单请求 cache 翻倍。Prefill 阶段（首个 Token）最贵，因为要一次性算完所有历史 K/V，这就是 TTFT 瓶颈的来源。GQA/MQA 通过共享 K/V head 显著降内存，是大规模服务必用方案。

`KV-Cache` `LLM` `inference` `TTFT` `prefill`

---

### [OpenClaw 落地到生产实际应用的一种可能的路径](/entry/9eJpiC4m) 📄
@Ding Junjie（vivo互联网项目团队） · ⭐⭐⭐⭐4 🇨🇳 · 昨天

文章分析 OpenClaw 进入真实生产场景还缺的四层能力：可视化层（Agent 在做什么必须清晰可见）、封闭层（把开放业务动作重构为边界明确的工作单元）、验证层（垂直领域的 gate，不通过不能进入完成态）、回滚层（沙盘机制，Amazon agent canvas 的实践）。核心判断：Coding Agent 成功是因为代码世界天然具备可视化/封闭/可验证/可回滚四个特征；业务 Agent 要落地必须先把这四层能力构建出来。

`OpenClaw` `production` `Agent` `visualization` `sandbox`

---

### [The AI Knowledge Layer: Making Every Agent Smarter](/entry/iplvrqyc) 📄
@shannholmberg · ⭐⭐⭐3 🌐 · 2026-04-15

作者提出 AI Knowledge Layer 的两层架构：动态知识库层（KBL）和静态品牌基础层（BF）。KBL 让用户将推文、文章、书签等原始素材导入文件夹，由 AI Agent 自动分类、构建结构化 Wiki 页面并维护主索引；BF 则存储用户的声音规则、视觉风格、定位等静态信息，Agent 只读不改。灵感来自 Karpathy 关于将 token 消耗从代码转向知识管理的观点。开源框架，20 分钟即可部署。

`knowledge-layer` `agent-memory` `karpathy` `wiki` `context-engineering`

---

### [Agent Memory 架构本质](/entry/hqm6txq4) 📄
⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-15

深度解析 Agent Memory 的工程架构。核心观点：Memory 的难点不在容量，在治理。文章厘清了 Memory 与 State/Policy/Profile 的边界，指出蒸馏只是管理链路中的一个操作而非记忆本身。提出四个建模对象：用户模型、任务模型、世界模型、自我模型。定义了记忆的六个维度（内容/类型/置信度/来源/作用域/时间衰减），以及写入-管理-读取三条链路。强调进化=修正+遗忘，评测从 recall 转向 update/abstain/drift/forget。

`agent-memory` `memory-architecture` `distillation` `knowledge-management` `belief-revision`

---

### [Decoding Transformer Architecture](/entry/0bf2b5b84701) 📄
@amitiitbhu · ⭐⭐⭐⭐4 🌐 · 2026-04-14

[EN] - **来源**：X/Twitter
- **原文链接**：https://x.com/augmentcode/status/2043740459256951158
- **作者**：amitiitbhu
- **日期**：2026-04-14
- **抓取时间**：2026-04-14 12:00...

`transformer` `attention` `llm` `architecture` `encoder`

---

### [深度研究Prompt方法论：横纵分析法](/entry/6a2113a2d9ca) 📄
@Khazix0918 · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-14

- **来源**：X/Twitter
- **原文链接**：https://x.com/augmentcode/status/2043740459256951158
- **作者**：Khazix0918
- **日期**：2026-04-14
- **抓取时间**：2026-04-14 12:00

`prompt-engineering` `research-methodology` `ai-tools` `横纵分析法` `deep-research`

---

### [Augment Code: The Era of Multi-Model Engineering](/entry/013eb7fd5ab9) 📄
@augmentcode · ⭐⭐⭐⭐4 🌐 · 2026-04-14

[EN] - **来源**：X/Twitter
- **原文链接**：https://x.com/augmentcode/status/2043740459256951158
- **作者**：augmentcode
- **日期**：2026-04-14
- **抓取时间**：2026-04-14 12:0...

`augment-code` `multi-model` `coding-agent` `harness` `model-agnostic`

---

### [浏览器自动化：从GUI到OpenCLI](/entry/8ee8a8b72ffc) 📄
@阿里妹 · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-14

[Read in Cubox](https://cubox.pro/web/card/7443547423802132834)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&amp;mid=2247559535&amp;idx=1&amp;sn=8eb95438291e8594d674652f6bb7c1df&amp;chksm=e8fb4fcf80f86a815cc31cd017098a604bb2b948524d8652ee631027f8542d6de98f4e06f7d3&amp;mpshare=

`browser-automation` `opencli` `api-mimicry` `agent-tooling` `web-scraping`

---
