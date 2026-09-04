# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [陈梓立：Agentic Coding 时代，什么是核心竞争力？](https://mp.weixin.qq.com/s?__biz=MzA4NTM4NDc4NQ%3D%3D&mid=2247546058&idx=1&sn=29bf169d86c161ec077d20bd862e8d97&chksm=9e047ff25e2c268c3373e60328f3d7587a106da4d2ad7efe3176d943a48fe6011560feebd2ea) ⭐4 · 2026-09-03 — 陈梓立在 KAIYUANSHE 9 月 3 日文章里围绕Agentic Coding 时代什么是核心竞争力给出三条判断：（1）AI 写代码的价值边界取决于模型是否覆盖你的日常工作基线.
- [Run cloud agents on machines you manage Cursor Self-Hosted Machines](https://cursor.com/blog/self-hosted-machines) ⭐4 · 2026-09-02 — Cursor 博文 2026-09-02 推出 Self-Hosted Machines：loop 与推理仍在 Cursor 云端，但 agent 实际执行落在企业自己管理的 worker / 池上.
- [Red Alert: OpenAI is poised to cross an AI safety redline](https://garymarcus.substack.com/p/red-alert-openai-is-poised-to-cross) ⭐4 · 2026-09-02 — Gary Marcus 9 月 2 日就 The Information 当天爆料做的快评：OpenAI 在 Astra 模型里尝试一种叫 "recurrent depth" 的新推理技术，让模型"思维"过程更接近神经隐喻（neuralese）.
- [Pluralistic: Unpermissioned research](https://pluralistic.net/2026/09/02/scrape-scrope-scrap) ⭐4 · 2026-09-02 — Cory Doctorow 9 月 2 日的长 essay 主题不是 scraping 是否合法，而是"用 property rights 框架去讨论 scraping 会让工人输掉这场仗"他先把财产论拆开：privacy 是人权不是财产权.
- [Let Claude use your computer in Cowork Anthropic help center updated 2026-09-02](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) ⭐4 · 2026-09-02 — Anthropic 帮助中心 2026-09-02 更新条目正式描述了 Cowork 中让 Claude 操作你的电脑能力：Pro / Max 订阅在 macOS 15+ 默认开启桌面后台窗，按应用授权可见性，可触达截屏可见的所有桌面内容.
- [A quote from Rick Brewster (Claude vibe-coded a Direct2D clean-room rewrite for Paint.NET on WIN...](https://simonwillison.net/2026/Sep/2/rick-brewster) ⭐4 · 2026-09-02 — Simon Willison 9 月 2 日转引 Paint.
- [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786) ⭐4 · 2026-09-02 — 论文指出 LLM Agent 的表现由基座模型与 harness 共同决定，安全风险同时存在于最终回复与多步执行轨迹中...
- [Post-Training Language Models for Gold-Medal Performance in Coding Competitions](https://arxiv.org/abs/2609.02849) ⭐4 · 2026-09-02 — NVIDIA 团队的竞赛编程端到端专精管线：2.
- [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885) ⭐4 · 2026-09-02 — 论文针对网页 Agent 测试时动作选择中的世界模型训练错配问题：现有世界模型用监督式下一状态预测（生成 HTML/AXTree 快照）训练.
- [禁用 1M 上下文能让 Claude Code 的 Token 更耐用（Fable 5.1 时代更明显）](https://x.com/dotey/status/2094964831061155845) ⭐3 · 2026-09-02 — dotey 9 月 2 日的工程经验：在 ~/.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 285 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 350 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 194 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 92 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 122 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 86 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2140
- 公开展示卡片: 1266
- 有全文内容: 1176
- 最近 7 天信号: 148
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `security`, `claude-code`, `multi-agent`, `agent-memory`, `agents`, `open-source`, `coding-agent`, `google`, `coding-agents`, `llm`, `safety`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
