---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 637 条 · 0 篇有全文
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

### [AI开发工具链完整方案推荐](https://x.com/RookieRicardoR/status/2044630408894271549)
@RookieRicardoR · ⭐⭐⭐3 🇨🇳 · 今天

RookieRicardoR 系统梳理当前 AI Agent 开发工具链全貌:底层(模型协议层)推荐 Claude Agent SDK(子进程方式兼容所有 Claude 协议模型)和 OpenAI Agent SDK / Vercel AI SDK / Pi-mono;上层 Runtime 推荐 assistant-ui + tools.ui(完整事件流+UI组件);开源完整方案推荐 CodePilot;记忆层建议可插拔设计(better sqlite + F5，或 markdown)。线程讨论深入，延伸至 Human-in-the-loop 审批、Wiki 模式不是真正记忆层等工程细节。

`agent-sdk` `claude-agent-sdk` `openai-agent-sdk` `vercel-ai-sdk` `assistant-ui`

---

### [Claude Code 最强配置单: 12个 GitHub 项目推荐](https://x.com/wsl8297/status/2044582054780895599)
@wsl8297 · ⭐⭐⭐3 🇨🇳 · 今天

wsl8297 推荐 12 个 GitHub 项目用于配置 Claude Code: LightRAG(知识图谱)、Superpowers(Claude 增强)、Obsidian Skills(上下文管理)、Everything Claude Code(功能汇总)、Claude Mem(记忆)、n8n-MCP(自动化集成)、Awesome Claude Code(用法汇总)、UI UX Pro Max(设计审美)、GSD(目标导向执行)等。社区补充 Oh My Claude Code 应排第一;GSD 中 Nyquist 规则(每步60s内验证)被单独点名实用。引发 1189 次点赞、260 次转发的高热度讨论。

`claude-code` `github` `lightrag` `superpowers` `obsidian-skills`

---

### [Research we co-authored on subliminal learning—...](https://x.com/AnthropicAI/status/2044493337835802948)
@@AnthropicAI · ⭐⭐⭐⭐4 🇨🇳 · 今天

Research we co-authored on subliminal learning—how LLMs can pass on traits like preferences or misalignment through hidden signals in data—was published today in Quote Owain Evans

`x` `ai-tools` `ai-news` `daily-digest`

---

### [Claude Code vs Codex: 两种AI编程助手的深度对比](https://x.com/shao__meng/status/2044769904608604295)
@shao__meng · ⭐⭐⭐⭐4 🇨🇳 · 今天

基于 Reddit 真实数据(Claude Code Opus 4.6 ~100小时 vs Codex GPT-5.4 ~20小时，8万行 Python/TypeScript，2800测试用例)的深度对比。发现两种截然不同的工程师人格:Claude Code 像赶工期的资深工程师，速度快3-4倍但倾向堆砌技术债务;Codex 像稳妥的5-6年经验开发者，深思熟虑但交付质量更高。作者提出实用的互补工作流:用 Claude Code 快速原型探索，Codex 重构架构补测试。核心结论:AI 编程助手是放大器而非替代品，Claude 需要技艺精湛的驾驶员，Codex 对实时介入要求更低。

`claude-code` `codex` `openai` `coding-agents` `anthropic`

---

### [Claude Opus 4.7 实用技巧与工作流程](https://x.com/dotey/status/2044868344256381254)
@dotey · ⭐⭐⭐⭐4 🇨🇳 · 今天

Boris Cherny 深度使用 Claude Opus 4.7 后分享的实用技巧总结。核心功能包括:Auto mode(Claude 自动判断命令安全性并批准执行)、/fewer-permission-prompts(智能白名单)、Recaps(任务回顾)、Focus mode(隐藏中间步骤)、灵活的努力程度设定(低-max)。推荐工作流:让 Claude 验证自己的工作成果(端到端测试)，结合 /go 自定义技能实现自我测试+精简代码+PR 提交流程。引发 211 次点赞和 41 次转发的热门讨论。

`claude` `claude-opus` `anthropic` `claude-code` `workflow`

---

### [This is a great report that provides a thoughtf...](https://x.com/geoffreyhinton/status/2019532085233611207)
@@geoffreyhinton · ⭐⭐⭐⭐⭐5 🇨🇳 · 今天

This is a great report that provides a thoughtful, detailed and very well researched description of the risks of AI. It is essential reading for anyone who wants to write or talk about AI risks. Qu...

`x` `ai-tools` `ai-news` `daily-digest`

---

### [Movement Matters – A Turing Test for Robot Inte...](https://x.com/petitegeek/status/1953082338029781441)
@@petitegeek · ⭐⭐⭐⭐⭐5 🇨🇳 · 今天

Movement Matters – A Turing Test for Robot Interaction 2.6K ](

`x` `ai-tools` `ai-news` `daily-digest`

---

### [Our most expressive and steerable TTS model yet...](https://x.com/demishassabis/status/2044599020690010217)
@@demishassabis · ⭐⭐⭐⭐⭐⭐6 🇨🇳 · 今天

Our most expressive and steerable TTS model yet! Designed to give builders granular control over AI-generated speech, Gemini 3.1 Flash TTS is really fun to play with! Available in preview today - f...

`x` `ai-tools` `ai-news` `daily-digest`

---

### [There&#x27;s a difference between using AI and build...](https://x.com/alliekmiller/status/1985834763677286606)
@@alliekmiller · ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐12 🇨🇳 · 今天

There&#x27;s a difference between using AI and building with it. Copy-pasting ChatGPT prompts will only get you so far. I want to help you learn to build personal AI software, automations, and tools tha...

`x` `ai-tools` `ai-news` `daily-digest`

---

### [使用 Claude Code：会话管理与 100 万 上下文](https://mp.weixin.qq.com/s?__biz=Mzk1NzgxMjQ0OA==&mid=2247494620&idx=1&sn=21e3dd0dff3cf2c79222351ff4f5e4fb)
@Thariq（Anthropic员工） · ⭐⭐⭐3 🇨🇳 · 昨天

Anthropic 官方员工 Thariq 发布的产品使用指南，系统讲解 Claude Code 100 万上下文下的会话管理策略。覆盖：Continue（继续）、Rewind（回溯，纠正错误的最佳方式）、Clear（清空新会话）、Compact（上下文压缩，有损摘要）、Subagents（委派干净上下文的子任务）五种决策路口。好压缩的关键是让模型知道下一步往哪走；子智能体适合阅后即焚型大量中间结果；100 万上下文让主动提前压缩成为可能。

`Claude Code` `context-window` `session-management` `Compact` `Rewind`

---
