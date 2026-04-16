---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 622 条 · 404 篇有全文
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

### [The AI Knowledge Layer: Making Every Agent Smarter](/entry/iplvrqyc) 📄
@shannholmberg · ⭐⭐⭐3 🌐 · 昨天

作者提出 AI Knowledge Layer 的两层架构：动态知识库层（KBL）和静态品牌基础层（BF）。KBL 让用户将推文、文章、书签等原始素材导入文件夹，由 AI Agent 自动分类、构建结构化 Wiki 页面并维护主索引；BF 则存储用户的声音规则、视觉风格、定位等静态信息，Agent 只读不改。灵感来自 Karpathy 关于将 token 消耗从代码转向知识管理的观点。开源框架，20 分钟即可部署。

`knowledge-layer` `agent-memory` `karpathy` `wiki` `context-engineering`

---

### [Agent Memory 架构本质](/entry/hqm6txq4) 📄
⭐⭐⭐⭐⭐5 🇨🇳 · 昨天

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

### [OpenClaw vs Hermes：一文深入理解两大通用 Agent](/entry/73831b80fee8) 📄
@架构师 · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-14

[Read in Cubox](https://cubox.pro/web/card/7443555272636761265)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&amp;mid=2650409010&amp;idx=1&amp;sn=04b9836fa07ff877c459e300707ddcff&amp;chksm=82e0d2bc0316714983894d249271a025550cdea2e2386283a92323167d29ae7a7879ea919fa0&amp;mpshare=

`openclaw` `hermes-agent` `nous-research` `agent-framework` `memory`

---

### [LLM长期记忆问题](/entry/c9567fc80a61) 📄
@chrysb · ⭐⭐⭐⭐⭐5 🌐 · 2026-04-14

[EN] - **来源**：X/Twitter
- **原文链接**：https://x.com/augmentcode/status/2043740459256951158
- **作者**：chrysb
- **日期**：2026-04-14
- **抓取时间**：2026-04-14 12:00...

`llm` `memory` `context-window` `retrieval` `summarization`

---

### [深度拆解 Claude Code：12 个可复用的 Agentic Harness 设计模式](/entry/480a4f5679ff) 📄
@技术极简主义 · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-14

这次 Claude Code 的泄露，让我们第一次比较完整地看到，这些模式在一个真实、大规模使用的 agent 里是怎么落地的。这样的窗口可能不会一直存在，但这些经验会留下来。

`claude-code` `agentic-harness` `design-patterns` `coding-agent` `bilgin-lbryam`

---

### [2026 年，AI 编程 Agent 的真正分水岭——Harness 详解](/entry/89fa848ed0d4) 📄
@Ai学习的老章 · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-14

[Read in Cubox](https://cubox.pro/web/card/7443555361631504701)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&amp;mid=2649012185&amp;idx=1&amp;sn=e613849d8e706a95d4a3c292b5881a1e&amp;chksm=86dfe794b8bbe007e9e98feae10f476d336e026e8df0819088fa8639d3385dfe3ce872cacff2&amp;mpshare=

`harness-engineering` `oh-my-claudecode` `oh-my-pi` `hashline` `coding-agent`

---
