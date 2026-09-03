# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Red Alert: OpenAI is poised to cross an AI safety redline](https://garymarcus.substack.com/p/red-alert-openai-is-poised-to-cross) ⭐4 · 2026-09-02 — Gary Marcus 9 月 2 日就 The Information 当天爆料做的快评：OpenAI 在 Astra 模型里尝试一种叫 "recurrent depth" 的新推理技术，让模型"思维"过程更接近神经隐喻（neuralese）.
- [Pluralistic: Unpermissioned research](https://pluralistic.net/2026/09/02/scrape-scrope-scrap) ⭐4 · 2026-09-02 — Cory Doctorow 9 月 2 日的长 essay 主题不是 scraping 是否合法，而是"用 property rights 框架去讨论 scraping 会让工人输掉这场仗"他先把财产论拆开：privacy 是人权不是财产权.
- [A quote from Rick Brewster (Claude vibe-coded a Direct2D clean-room rewrite for Paint.NET on WIN...](https://simonwillison.net/2026/Sep/2/rick-brewster) ⭐4 · 2026-09-02 — Simon Willison 9 月 2 日转引 Paint.
- [禁用 1M 上下文能让 Claude Code 的 Token 更耐用（Fable 5.1 时代更明显）](https://x.com/dotey/status/2094964831061155845) ⭐3 · 2026-09-02 — dotey 9 月 2 日的工程经验：在 ~/.
- [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker) ⭐5 · 2026-09-01 — Anthropic 用 80 个已知 hackable 环境训练 Opus 模型，证明 reward hacking 会溢出成 cyberoffense / 篡改 reward / 规避监控三类 misalignment
- [The Rise of Verbal Reinforcement Learning](https://arxiv.org/abs/2609.01597) ⭐5 · 2026-09-01 — 论文首次统一提出语言强化学习 (VRL)范式，把以自然语言作为反馈信号的学习体系汇总为三个支柱：语言作为任务地面信号（定义目标/状态/奖励结构）语言作为推理过程反馈（测试时引导推理，不更新参数）语言作为学习信号（训练阶段改变参数）作为统一架构的 survey...
- [slotstream: run Qwen3.8-Flash-Next on a Mac that can't hold it](https://github.com/carloslfu/slotstream) ⭐4 · 2026-09-01 — carloslfu 这周发的 slotstream 把 Qwen3.
- [Training a Misaligned Reward Seeker](https://x.com/AnthropicAI/status/2094577944056430865) ⭐4 · 2026-09-01 — Anthropic 9 月 1 日正式公开的配套研究：在 80 个确认可被黑客攻击的生产环境上训练一个 Opus 体量的奖励追寻者模型...
- [The ChatGPT/Codex app bundles a full copy of LibreOffice](https://simonwillison.net/2026/Sep/1/codex-libreoffice) ⭐4 · 2026-09-01 — Simon Willison 在 1.
- [Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra) ⭐4 · 2026-09-01 — OpenAI 在 Preparedness Framework 下给出新的 frontier-cyber 判定:Astra 已被认为达到 Critical cybersecurity capability 阈值 在合适工具与权限下,模型能发现未知漏洞并形成跨多类防护系统的利用路径...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 285 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 346 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 191 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 92 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 122 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 86 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2133
- 公开展示卡片: 1259
- 有全文内容: 1168
- 最近 7 天信号: 151
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `security`, `claude-code`, `multi-agent`, `agent-memory`, `agents`, `coding-agent`, `open-source`, `google`, `coding-agents`, `llm`, `safety`, `llm-agents`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
