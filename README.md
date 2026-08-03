# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [I'm (mostly) picking models on speed now, not intelligence](https://martinalderson.com/posts/speed-vs-intelligence) ⭐4 · 2026-08-02 — 当主流模型已足够聪明时，速度和等待成本开始决定日常模型选择，而不只是能力榜单
- [给 GPT 5.6 Sol 一个真实业务：它撒谎垃圾邮件亏了 447 美元](https://www.bottlenecklabs.com/blog/autonomously-run-businesses) ⭐5 · 2026-07-31 — BottleneckLabs 给 GPT 5.
- [Tailscale in the Hugging Face intrusion: The good news and the bad news](https://tailscale.com/blog/hugging-face-intrusion) ⭐5 · 2026-07-31 — Hugging Face 入侵复盘把 Agent 安全问题落到长期凭据工作负载身份和可观测网络边界上
- [Stateless MCP has recaptured my interest (MCP 2.0)](https://simonwillison.net/2026/Jul/31/stateless-mcp) ⭐5 · 2026-07-31 — MCP 2.0 从有状态改为无状态，实现复杂度断崖下降，同时发布三个工具
- [smevals: a small eval suite for models, prompts, and harnesses](https://simonwillison.net/2026/Jul/31/smevals) ⭐4 · 2026-07-31 — 运行和评分分离的轻量 eval 框架，第三次迭代设计
- [Why do OpenAI's GPT-2 weights beat mine? Part three: testing overtraining](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining) ⭐4 · 2026-07-31 — GPT-2 复现实验通过过训练测试loss 对照和实现排查，展示模型训练差异如何一步步缩小
- [Everyone is building LLM routers, we deprecated ours](https://manifest.build/blog/why-we-deprecated-our-llm-router) ⭐4 · 2026-07-31 — Manifest 的 LLM router 复盘提醒 Agent 基础设施降本不能只看单次调用价格
- [DeepSeek-V4-Flash-0731: 304B params, best value-per-intelligence model](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731) ⭐4 · 2026-07-31 — 同智能指数下成本为同类模型十分之一，帕累托前沿左上角
- [DeepSeek-V4-Flash 官方发版：Agent 能力大幅提升，原生支持 Responses API](https://api-docs.deepseek.com/updates) ⭐4 · 2026-07-31 — DeepSeek 于 7月31日官方发布 V4-Flash API 公测版该版本与 V4-Flash-Preview 保持相同架构和规模，仅进行了重新后训练.
- [DeepSeek V4 Flash 0731 智能性能与价格分析（Artificial Analysis）](https://artificialanalysis.ai/models/deepseek-v4-flash) ⭐4 · 2026-07-31 — Artificial Analysis 对 DeepSeek V4 Flash 0731（Reasoning, Max Effort）的综合评测：智能指数 50（全网第 3/101），远超同类型模型中位数 25价格极具竞争力：输入 $0.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 247 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 194 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 108 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 33 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 59 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 40 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1650
- 公开展示卡片: 831
- 有全文内容: 747
- 最近 7 天信号: 108
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `openai`, `arxiv`, `benchmark`, `attention`, `evaluation`, `anthropic`, `google`, `optimization`, `coding-agent`, `claude-code`, `2026`, `agent-security`, `gemini`, `security`, `agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
