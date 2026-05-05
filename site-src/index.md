---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 892 条 · 503 篇有全文
  actions:
    - theme: brand
      text: 浏览全部
      link: /models
    - theme: alt
      text: GitHub
      link: https://github.com/Gracker/awesome-ai-field-notes

features:
  - title: '🧠 模型'
    details: 'GPT / Claude / Gemini / 开源模型 / 架构 · 80 条'
    link: /models
  - title: '🤖 智能体'
    details: 'Agent 框架 / MCP / A2A / 手机&桌面助手 · 140 条'
    link: /agents
  - title: '💻 AI编程'
    details: 'IDE / CLI / 代码审查 / 工作流 · 178 条'
    link: /coding
  - title: '⚡ 基础设施'
    details: '推理部署 / RAG / 微调 / 评测 / 多模态 · 50 条'
    link: /infra
  - title: '🌍 行业观察'
    details: 'AI 产品 / 大厂战略 / 融资 / 市场分析 · 58 条'
    link: /industry
  - title: '📖 学习资源'
    details: '教程 / 论文 / 提示工程 / 演讲 · 79 条'
    link: /learning
  - title: '🗂️ 未分类'
    details: '待归类但已通过质量门槛的资源 · 47 条'
    link: /uncategorized
---

## 🆕 最新 10 篇

### [MCP-Flow: 自动构建大规模 MCP 工具数据集，让 0.6B 模型在工具调用上超越 GPT-4o](/entry/ehpdysfh) 📄
@TikTok &amp; 上海交大联合研究 · ⭐⭐⭐⭐4 🌐 · 2026-05-04

MCP-Flow 提出全自动 pipeline，从 6 个 MCP 市场自动抓取服务器配置，通过 Slot-Fill Revision + WizardLM Evolution 两阶段数据增强，产出 68733 对 instruction-function call（1166 服务器、11536 工具）。实验表明：GPT-4o 在 10 工具场景下 AST 仅 58.8%，100 工具时 Groq-8B AST 跌至 3%；而 MCP-Flow-Qwen3-0.6B 在同场景下 AST 达 81.2%，全面超越所有大模型。用 MCP-Flow 做 RAG 检索增强后，GPT-4o 在 GAIA 任务上成功率 +17%，步数减少 32%。

`mcp` `tool-calling` `fine-tuning` `dataset` `agent`

---

### [Greg Brockman 详解 Codex 验证创业想法的 Skill](/entry/c1887e9a) 📄
@@gdb · ⭐⭐⭐⭐4 🇨🇳 · 2026-05-04

Greg Brockman 分享了一个 Codex Skill，可以对创业想法进行压力测试。用户只需输入创业想法，Codex 会自动找到核心假设、暴露致命缺陷、检查问题是否真实存在，并给出坦诚的批判性评估。这个 Skill 解决了一个常见痛点：大多数创业想法听起来都不错，但缺乏系统性的验证机制。对于独立开发者、天使投资人以及正在构思 MVP 的创业者，这个工具提供了一个低成本的初期验证手段，可以快速筛选出想法中的致命漏洞。

`x` `prompt` `startup` `codex` `validation`

---

### [Google Gemini Embedding 2 多模态嵌入模型](/entry/d9a0a60c) 📄
@@GoogleAI · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-05-03

Google推出的首个原生多模态嵌入模型，支持视频分析、视觉购物助手等多种应用场景，已向公众开放使用。

`google` `multimodal` `embedding` `developer-tools` `x`

---

### [Pete Yang对话前Tinder CPO：构建AI产品的3层context系统](/entry/bd777cd2) 📄
@@petergyang · ⭐⭐⭐⭐4 🇨🇳 · 2026-05-03

Pete Yang 与前 Tinder CPO Ravi Mehta 合作，提出构建有用 AI 产品的3层 context 系统：Functional 层（应用做什么）、Visual 层（应用长什么样）和 Context 层（当前交互上下文）。Pete 指出目前 AI 使用中最常见的错误是不主动管理 context——模型无法有效利用历史信息，导致输出质量下降。这套3层框架可帮助产品经理和开发者系统性地设计 AI 产品的信息架构，避免常见的信息流混乱问题，是一个可复用的产品方法论。

`x` `workflow` `ai-product` `context-management`

---

### [OpenClaw 2026.5.2：插件安装更稳、Agent 热路径更轻](/entry/fd791356) 📄
@@steipete · ⭐⭐⭐3  · 2026-05-03

Peter Steinberger 转发 OpenClaw 2026.5.2 发布，重点是修复 npm 安装依赖与速度问题，让插件安装和更新更稳定，并把大部分能力迁入 extensions 以降低包体负担。发布同时提到 Gateway 与 agent hot path 精简，以及 Discord、Slack、Telegram、WhatsApp、TTS、Realtime、web search 等集成修复。

`openclaw` `plugins` `agent` `release` `workflow`

---

### [Tibo独家复盘:9次失败产品后如何做到100万美金/月 五款AI产品从0到1方法论](/entry/9ijpm5tr) 📄
@@petergyang · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-05-02

独立开发者 Tibo 复盘5款AI产品做到100万美金/月 快速验证快速失败是核心

`x` `ai-tools` `workflow`

---

### [OpenAI CFO Sarah Friar：建议将 IPO 推迟至 2027 年，正在管理 Sam Altman](/entry/rc08tdo2) 📄
@Lauren Thomas / Wall Street Journal · ⭐⭐⭐⭐4 🌐 · 2026-05-02

华尔街日报对 OpenAI CFO Sarah Friar 的深度专访。知情人士透露，Friar 私下建议将 OpenAI IPO 推迟至 2027 年，以避免在 Anthropic 之前匆忙上市导致估值受损。她帮助维持了 OpenAI 与微软的关键合作关系，并正在管理 Sam Altman 的雄心与公司实际发展节奏之间的平衡。报道指出 OpenAI 正处于 11 年历史上最关键的发展阶段，走得太快可能透支业务，太慢则可能被 Anthropic 抢先。

`OpenAI` `IPO` `Sarah Friar` `财务策略`

---

### [马斯克诉 OpenAI 案首周遭遇波折](/entry/cudamu2v) 📄
@Bloomberg · ⭐⭐⭐3 🌐 · 2026-05-02

马斯克对 OpenAI 的诉讼在首周审理中遭遇波折。据彭博社报道，庭审过程中出现多个不利信号。这起备受关注的案件被视为 AI 行业治理走向的风向标，涉及 OpenAI 从非营利向营利转型的合法性、创始团队的信义义务等核心问题。案件的走向将对整个 AI 行业的公司治理结构产生深远影响。

`OpenAI` `马斯克` `诉讼` `法律`

---

### [Claude Code 向 Codex 的习惯迁移](/entry/rcrsoyz3) 📄
@串串狗小刊 · ⭐⭐⭐3 🇨🇳 · 2026-05-02

串串狗小刊发布的一篇从 Claude Code 迁移到 Codex 的实践指南。文章对比了两个 AI 编程工具在日常使用中的差异，包括上下文管理、工具调用方式、权限模型等方面的区别，并分享了作者在实际项目中完成迁移的经验和踩坑记录。对于同时使用或考虑切换 AI 编程工具的开发者有直接参考价值。（原文抓取失败，基于 RSS 元数据提取）

`Claude Code` `Codex` `AI编程` `迁移` `工具对比`

---

### [Anthropic 正在与英国 AI 芯片初创 Fractile 洽谈采购推理芯片](/entry/akye56py) 📄
@The Information · ⭐⭐⭐3 🌐 · 2026-05-02

据 The Information 报道，Anthropic 正在与英国 SRAM 基 AI 芯片初创公司 Fractile 进行早期洽谈，计划在 2027 年 Fractile 产品上市后采购其推理芯片。随着 Anthropic 销售额爆发式增长，现有服务器供应（来自 Google、Amazon、Nvidia）已面临压力。此举反映了 AI 公司正在积极多元化芯片供应链，以应对日益增长的推理算力需求。Fractile 的 SRAM 基方案代表了一种不同于传统 GPU 的推理加速路径。

`Anthropic` `AI芯片` `Fractile` `推理` `供应链`

---
