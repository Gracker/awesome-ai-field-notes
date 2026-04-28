---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 731 条 · 11 篇有全文
  actions:
    - theme: brand
      text: 浏览全部
      link: /models
    - theme: alt
      text: GitHub
      link: https://github.com/Gracker/awesome-ai-field-notes

features:
  - title: '🧠 模型'
    details: 'GPT / Claude / Gemini / 开源模型 / 架构 · 94 条'
    link: /models
  - title: '🤖 智能体'
    details: 'Agent 框架 / MCP / A2A / 手机&桌面助手 · 105 条'
    link: /agents
  - title: '💻 AI编程'
    details: 'IDE / CLI / 代码审查 / 工作流 · 167 条'
    link: /coding
  - title: '⚡ 基础设施'
    details: '推理部署 / RAG / 微调 / 评测 / 多模态 · 60 条'
    link: /infra
  - title: '🌍 行业观察'
    details: 'AI 产品 / 大厂战略 / 融资 / 市场分析 · 54 条'
    link: /industry
  - title: '📖 学习资源'
    details: '教程 / 论文 / 提示工程 / 演讲 · 115 条'
    link: /learning
---

## 🆕 最新 10 篇

### [Google 发布 Gemini 3.1 Flash TTS：支持自然语言音频标签控制](https://x.com/GoogleAI/status/2044447560384102592)
@@GoogleAI · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Google 发布了 Gemini 3.1 Flash TTS，号称旗下表现力最强、控制最精细的语音合成模型。其核心亮点是引入了「音频标签」（Audio Tags）机制——可以用自然语言描述来引导语音的风格、节奏和表达方式，比如「用兴奋的语气」「稍微放慢一些」「带点犹豫」。这对需要为 AI 对话、数字人、有声内容生成个性化语音的开发者来说是实打实的新能力，也是目前 TTS 领域少见的控制粒度突破。

`google` `tts` `audio` `ai-tools`

---

### [RAG 在大规模场景下失效：神经符号 AI 是未来方向](https://x.com/DeepLearn007/status/2043784557099471159)
@@DeepLearn007 · ⭐⭐⭐⭐4 🇨🇳 · 昨天

该推文揭示了一个被广泛忽视的 RAG 失效场景：当知识库规模达到临界值，向量相似度搜索会遭遇「语义崩溃」（Semantic Collapse）——语义相近的无关文档被错误召回，真正相关的内容反而被淹没。引用 Stanford 研究后，作者提出未来属于「神经符号 AI」：用本体论处理结构化知识，用确定性层保障事实准确性，用 LLM 做自然语言解释而非直接做检索。

`rag` `ai-tools` `workflow`

---

### [AI 生成图像正在替代传统原型设计，成为产品创意共享新方式](https://x.com/gdb/status/2049120845985923316)
@@gdb · ⭐⭐⭐⭐4 🇨🇳 · 昨天

该推文引述了一个正在发生的趋势：AI 图像生成模型（尤其是 2.0 版本）已经能够高度还原产品界面和视觉 mock，使得团队内部在讨论产品概念时，直接用 AI 生成图像替代传统的原型设计和 PPT 演示。内部产品 idea 的呈现和共创方式因此发生根本变化——不再依赖 Figma 或 Axure，而是让 AI 把想法「画出来」。这对产品经理、UX 设计师和创业者的工作流有直接启发：用好图像生成模型可以极大压缩创意验证周期。

`imagegen` `prototyping` `workflow`

---

### [Anthropic 发布 81,000 用户经济展望与担忧研究](https://x.com/AnthropicAI/status/2047006548149289017)
@@AnthropicAI · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Anthropic 在发布 81,000 人用户调研后，进一步发布了关于这些用户「经济期望与担忧」的研究报告。这是 AI 领域迄今规模最大的定性用户调研之一，揭示了普通用户对 AI 经济影响的真实心态：既期待 AI 提升生产力和收入，又担忧职业替代和技能贬值。这份研究的价值在于：它为 AI 产品设计者、创业者和政策制定者提供了真实的用户心理画像，有助于构建更符合用户期待、更易被市场接受的 AI 产品。

`anthropic` `research` `ai-tools`

---

### [NotebookLM 来源自动标签与分类：5 个以上文档智能整理](https://x.com/joshwoodward/status/2047795981534847413)
@@joshwoodward · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Google NotebookLM 新增来源自动标签与分类功能，当用户有 5 个以上来源时自动打标签和归类，减少滚动时间，提升学习和研究效率。支持重命名、重组和 emoji 自定义。该功能解决了研究材料多了反而混乱的核心痛点，对学术研究和内容创作者特别有用，可作为信息管理流程的一部分。

`x` `ai-tools` `notebooklm` `research` `workflow`

---

### [Gemini 3.1 Flash TTS：支持自然语言音频标签控制的语音合成 API](https://x.com/GoogleAI/status/2044447560384102592)
@@GoogleAI · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Google 发布 Gemini 3.1 Flash TTS，旗下最具表现力和可控性的文本转语音模型，亮点是支持音频标签（Audio Tags）——用自然语言命令嵌入文本，直接控制语速、风格、停顿和表达方式，无需调参。兼容 API 方式调用，适合构建有声内容、语音助手、无障碍应用等场景，是目前最具可控性的 TTS 方案之一。

`x` `ai-tools` `tts` `google` `api`

---

### [Allie K. Miller 推出免费 5 天课程：AI Fast Track](https://x.com/alliekmiller/status/1985834763677286606)
@@alliekmiller · ⭐⭐⭐⭐⭐5 🇨🇳 · 昨天

Allie K. Miller 宣布推出「AI Fast Track」免费 5 天邮件课程，面向想超越 ChatGPT 简单调用的用户。课程无需编程基础，教授如何将 Claude 加入个人工具箱，构建属于自己的 AI 软件、自动化脚本和实用工具。区别于单纯使用 AI 的粘贴复制，该课程强调亲手构建，填补了广大用户「会用 AI」到「会用 AI 构建」之间的鸿沟。对于想系统性提升 AI 生产力的个人用户，这是目前少有的免费高质量入门路径。

`ai-tools` `learning` `workflow`

---

### [Karpathy：本地 Demo 到线上产品，DevOps 是最难的部分](https://x.com/karpathy/status/2037200624450936940)
@@karpathy · ⭐⭐⭐⭐⭐5 🇨🇳 · 昨天

Karpathy 在回顾 MenuGen 开发历程时指出：构建一个真正上线的 AI 应用，最难的部分从来不是模型或代码本身，而是需要像 IKEA 家具一样组装各种第三方服务的 DevOps 工作——支付网关、用户认证、数据库、安全防护、域名配置等。这些基础设施的拼装和调试占据了大量工程时间，往往比训练模型更让人「痛苦」。这提醒所有 AI 开发者：Demo 和产品之间隔着一整个 DevOps 世界，vibe coding 的快乐止步于本地运行。

`ai-tools` `devops` `workflow`

---

### [AI Fast Track: 5天免费课程，从用AI到用AI构建](https://x.com/alliekmiller/status/1985834763677286606)
@@alliekmiller · ⭐⭐⭐⭐⭐5 🇨🇳 · 昨天

Allie K. Miller 推出免费 5 天邮件课程 AI Fast Track，核心主张是超越 ChatGPT 复制粘贴，教用户用 Claude 构建个人 AI 软件、自动化工具和工作流，无需编程基础。课程涵盖从基础到实战构建的全流程，适合想从 AI 使用者转型为 AI 建造者的人群。

`x` `ai-tools` `course` `automation` `beginner`

---

### [Glean 推出 Waldo：首个 Agentic 搜索模型，NVIDIA Nemotron 3 Nano 驱动](https://x.com/NVIDIAAI/status/2049131895552963023)
@@NVIDIAAI · ⭐⭐⭐⭐⭐5 🇨🇳 · 昨天

Glean 推出 Waldo，首个 Agentic 搜索模型，基于 NVIDIA Nemotron 3 Nano 构建，专门针对搜索规划做后训练。Waldo 能自主分解查询、决定调用哪些工具、阅读哪些内容、何时停止并返回结果，实现真正代理式企业搜索。与传统 RAG 不同，Waldo 有主动规划能力，适合知识密集型企业场景。

`x` `ai-tools` `agentic` `search` `nvidia`

---
