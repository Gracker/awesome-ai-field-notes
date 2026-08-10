# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [The bureaucratic AI arms-race is mutually assured destruction](https://pluralistic.net/2026/08/10/deep-state-wopr) ⭐5 · 2026-08-10 — 当服务系统主要优化反欺诈，它就不再是服务系统，而是拒付系统
- [Addy Osmani 2026 LLM coding workflow: spec-first, chunked, human-supervised](https://x.com/yibie/status/2085536770758996033) ⭐5 · 2026-08-10 — 模型越能写代码，人的规格上下文和审查越不能省
- [活人感写作skill：去 AI 味不能停在词表](https://x.com/Khazix0918/status/2084919577562255639) ⭐5 · 2026-08-09 — 义理考据辞章，去 AI 味不能只停在辞章
- [Advanced AI sycophancy: models can flatter through refutable disagreement](https://seangoedecke.com/advanced-ai-sycophancy) ⭐5 · 2026-08-09 — 诽媚不一定是奉承，也可以是给你一个刚好能反驳的批评
- [The Problem With Vibe: when you can't trust the weekend tinkerer](https://tedium.co/2026/08/09/vibe-coding-insincerity) ⭐4 · 2026-08-09 — vibe coding 最大的问题未必是代码质量，而是信任归属
- [SQLite compressed text-history prototypes: 20.4MB to 80.3KB](https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype) ⭐4 · 2026-08-09 — 把 1000 次修订压成一个 blob，再用 chunk 分段避免全量解压缩
- [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow) ⭐5 · 2026-08-07 — AI 编码越强，规格上下文测试和责任边界越要前置
- [Managing AI Coding Costs at Scale](https://www.databricks.com/blog/managing-ai-coding-costs-scale) ⭐5 · 2026-08-07 — AI coding 的规模化落地开始从模型能力转向成本可见性路由和网关治理
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) ⭐4 · 2026-08-07 — 团队级 agent 记忆的核心是把经验治理成可复用资产
- [The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping](https://arxiv.org/abs/2608.06361) ⭐5 · 2026-08-06 — VLM evaluation needs timestamp-level event traces because final counts can improve without faithful temporal understanding.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 254 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 227 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 127 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 43 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 63 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 48 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1732
- 公开展示卡片: 912
- 有全文内容: 828
- 最近 7 天信号: 77
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `evaluation`, `openai`, `arxiv`, `attention`, `anthropic`, `google`, `coding-agents`, `security`, `optimization`, `agent-security`, `claude-code`, `coding-agent`, `2026`, `agent-memory`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
