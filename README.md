# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow) ⭐5 · 2026-08-07 — AI 编码越强，规格上下文测试和责任边界越要前置
- [Managing AI Coding Costs at Scale](https://www.databricks.com/blog/managing-ai-coding-costs-scale) ⭐5 · 2026-08-07 — AI coding 的规模化落地开始从模型能力转向成本可见性路由和网关治理
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) ⭐4 · 2026-08-07 — 团队级 agent 记忆的核心是把经验治理成可复用资产
- [The Bitter Lesson of Tool Calling](https://arxiv.org/abs/2608.06370) ⭐5 · 2026-08-06 — 工具接口形态会跟模型能力一起演进，typed code stubs 可能比 JSON 调用更适合强模型
- [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajector...](https://arxiv.org/abs/2608.06346) ⭐5 · 2026-08-06 — 长轨迹 agent 调试需要区分局部错误已修复错误和真正导致失败的关键错误
- [Learning Globally Reusable Skills for Coding Agents](https://arxiv.org/abs/2608.06153) ⭐5 · 2026-08-06 — 技能库不能只局部追加，coding agent 需要关系图合并和 replay 验证来保持可复用性
- [Introducing Kitesurf: The agent-first browser that runs in V8 isolates on Cloudflare Workers](https://blog.cloudflare.com/kitesurf) ⭐5 · 2026-08-06 — Agent 浏览器正在从复用 Chromium 转向以隔离成本和机器可读输出为中心的新运行时
- [Introducing Agent Plugins](https://vercel.com/blog/introducing-agent-plugins) ⭐5 · 2026-08-06 — Agent Plugins 把 Skills 和 MCP 的可移植部分收敛到一个最小包格式
- [The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping](https://arxiv.org/abs/2608.06361) ⭐5 · 2026-08-06 — VLM evaluation needs timestamp-level event traces because final counts can improve without faithful temporal understanding.
- [AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Inform...](https://arxiv.org/abs/2608.06362) ⭐5 · 2026-08-06 — Agent evaluation should optimize for auditable early stopping, not only fixed-budget aggregate win rates.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 252 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 225 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 123 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 42 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 61 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 46 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1718
- 公开展示卡片: 899
- 有全文内容: 812
- 最近 7 天信号: 127
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `evaluation`, `openai`, `arxiv`, `attention`, `anthropic`, `google`, `coding-agents`, `optimization`, `agent-security`, `claude-code`, `security`, `coding-agent`, `2026`, `agent-memory`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
