---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 665 条 · 2 篇有全文
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
    details: 'IDE / CLI / 代码审查 / 工作流 · 164 条'
    link: /coding
  - title: '⚡ 基础设施'
    details: '推理部署 / RAG / 微调 / 评测 / 多模态 · 60 条'
    link: /infra
  - title: '🌍 行业观察'
    details: 'AI 产品 / 大厂战略 / 融资 / 市场分析 · 53 条'
    link: /industry
  - title: '📖 学习资源'
    details: '教程 / 论文 / 提示工程 / 演讲 · 115 条'
    link: /learning
---

## 🆕 最新 10 篇

### [Farzapedia：用日记+笔记训练个人 Wikipedia，LLM 个性化的最佳实践](https://x.com/karpathy/status/2040572272944324650)
@@karpathy · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-22

Andrej Karpathy 转发并点评 Farzapedia 项目——将 2500 条日记、Apple Notes 和 iMessage 对话输入 LLM，生成 400 篇个人 Wikipedia 条目，涵盖朋友、创业项目、研究领域甚至喜欢的动漫及其影响。Karpathy 指出这种方法相比「用越多 AI 越强」的传统范式，优势在于：记忆 artifact 是显式的、可审查的，个性化更精准。可作为构建个人第二大脑的参考架构。

`x` `workflow` `llm` `personal-knowledge` `karpathy`

---

### [Gemini 3.1 Flash TTS 发布：带 Audio Tags 的最可控语音合成](https://x.com/GoogleAI/status/2044447560384102592)
@@GoogleAI · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-22

Google AI 推出 Gemini 3.1 Flash TTS，号称迄今表现力最强、可控性最高的语音合成模型。核心亮点是 Audio Tags（音频标签）功能：用自然语言命令嵌入文本，即可精准控制语速、语调、停顿和表达风格，无需传统 SSML 标记，适合做播客配音、有声书和语音助手场景。已在 Google AI Studio 和 Vertex AI 上线，开发者可直接调用。

`x` `ai-tools` `gemini` `tts` `audio`

---

### [Deep Research Max：Gemini 3.1 Pro 驱动的自主研究代理，支持自有数据](https://x.com/GoogleDeepMind/status/2046627042335060342)
@@GoogleDeepMind · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-22

Google DeepMind 发布 Deep Research 和 Deep Research Max，基于 Gemini 3.1 Pro 的自主研究代理，可安全浏览网页和自定义数据（如内部文档、专业财务数据），自动生成带引用来源的专业级报告。相比传统搜索，它能完成多步骤的调研任务链，输出结构化、可溯源的报告，适合分析师、研究人员和知识工作者。

`x` `ai-tools` `gemini` `research` `agent`

---

### [TRL 异步 GRPO：解耦推理与训练，RL Scaling 新一代方法解析](https://x.com/Thom_Wolf/status/2045817727705628714)
@@Thom_Wolf · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-22

Thomas Wolf 详解 TRL 库新增的 AsyncGRPO 功能，解决了训练前向传播（FP32）与 vLLM 推理服务器（BF16）精度不匹配导致 RL 无法收敛的问题。通过将推理与训练解耦，实现更快、更 hard 的 scaling。附有完整 detective story 风格的技术解析，从问题复现到修复路径均有覆盖，是训练大模型 RLHF 流程的进阶参考。

`x` `ai-tools` `rlhf` `trl` `training`

---

### [免费 5 天课程：从 AI 用户到 AI 建造者](https://x.com/alliekmiller/status/1985834763677286606)
@@alliekmiller · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-22

Allie K. Miller 推出免费 5 天邮件课程「AI Fast Track」，核心主张是：「用 AI」与「用 AI 建造工具」之间存在鸿沟，仅复制粘贴 Prompt 远远不够。课程无需编程基础，手把手教你用 Claude 构建个人 AI 软件、自动化脚本和实用工具。每天一个主题，聚焦可落地的 side project，而非泛泛的 AI 概念，tens of thousands 已经注册，适合想从「消费者」升级为「建造者」的 AI 用户。

`x` `ai-tools` `tutorial` `claude` `automation`

---

### [16 分钟掌握 Claude Design 全套用法：视频/幻灯/网站/App/设计系统](https://x.com/petergyang/status/2045522933943238934)
@@petergyang · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-22

Peter Yang 发布 Claude Design 实操教程 live demo，在 16 分钟内演示了用 Claude Design 创建视频、幻灯片、网站、App 乃至完整设计系统的完整流程。涵盖从概念到可交付物的每一步，展示 Claude 在多模态创意工作中的实际能力边界。视频为实时演示，可直接参考其操作路径用于自己的项目。

`x` `ai-tools` `claude` `design` `tutorial`

---

### [用 Codex 自然语言构建 Web 应用和游戏：Greg Brockman 展示新范式](https://x.com/gdb/status/2045594591584530826)
@@gdb · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-19

Greg Brockman 展示用 OpenAI Codex 完全通过自然语言构建 Web 应用和游戏的新方式。Nicolas Zullo 的实操演示中，游戏内置于 Codex，可使用 Codex 生成的工具进行建筑设计，并支持直接用自然语言提问修改代码。展示了 AI 编程助手从辅助工具向独立开发环境演进的趋势。

`openai` `codex` `webapp` `game` `nlp`

---

### [Codex：用纯自然语言构建 Web 应用和小游戏](https://x.com/gdb/status/2045594591584530826)
@@gdb · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-19

Greg Brockman 展示 Codex 全新用法：完全用自然语言构建 Web 应用和小游戏，无需传统编程。案例中游戏内设计和建筑建模都在 Codex 内完成，AI 直接生成可运行代码。这代表了 AI 编程助手向直接产出可运行产品的进化，显著降低数字产品创作门槛。

`x` `ai-tools` `codex` `webdev` `prototyping`

---

### [2026 AI First 系列（四）：connecting the dots——你的独特人生路径](https://youmind.com/s/pG5sMT6W7UIdIe)
@wquguru · ⭐⭐⭐3 🇨🇳 · 2026-04-18

用Tim Urban的人生方格图和Steve Jobs的connecting dots框架，探讨个体如何在AI时代设计人生路径：向后看理解轨迹，向前看设想可能，活在当下创造每个扎实的dot。核心洞察：在所有宏观因素中，AI几乎是唯一可主动掌握的变量——经济周期、政策走向、行业兴衰都控制不了，但可以选择如何学习、使用和让它创造价值。Build in Public是建立信任飞轮的关键策略。

`ai-first` `life-design` `connecting-dots` `build-in-public` `adaptability`

---

### [Allie Miller推出免费5天课程：从AI用户进化为AI建造者](https://x.com/alliekmiller/status/1985834763677286606)
@@alliekmiller · ⭐⭐⭐3 🌐 · 2026-04-18

Allie Miller推出免费5天课程AI Fast Track，核心观点：使用AI和借助AI建造是两件不同的事——复制粘贴ChatGPT提示词只能帮人走到某个阶段，而学会构建个人AI软件、自动化工具和应用才能真正解决问题。课程已帮助数万人转型为AI builder。

`ai-education` `ai-tools` `course` `career` `vibe-coding`

---
