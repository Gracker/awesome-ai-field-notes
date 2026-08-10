# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow) ⭐5 · 2026-08-07 — AI 编码越强，规格上下文测试和责任边界越要前置
- [Managing AI Coding Costs at Scale](https://www.databricks.com/blog/managing-ai-coding-costs-scale) ⭐5 · 2026-08-07 — AI coding 的规模化落地开始从模型能力转向成本可见性路由和网关治理
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) ⭐4 · 2026-08-07 — 团队级 agent 记忆的核心是把经验治理成可复用资产
- [The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping](https://arxiv.org/abs/2608.06361) ⭐5 · 2026-08-06 — VLM evaluation needs timestamp-level event traces because final counts can improve without faithful temporal understanding.
- [The Bitter Lesson of Tool Calling](https://arxiv.org/abs/2608.06370) ⭐5 · 2026-08-06 — 工具接口形态会跟模型能力一起演进，typed code stubs 可能比 JSON 调用更适合强模型
- [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajector...](https://arxiv.org/abs/2608.06346) ⭐5 · 2026-08-06 — 长轨迹 agent 调试需要区分局部错误已修复错误和真正导致失败的关键错误
- [Learning When to Trust via Selective Context Preference Optimization](https://arxiv.org/abs/2608.06377) ⭐5 · 2026-08-06 — 上下文安全的目标不是一概不信外部信号，而是学会选择性信任
- [Learning Globally Reusable Skills for Coding Agents](https://arxiv.org/abs/2608.06153) ⭐5 · 2026-08-06 — 技能库不能只局部追加，coding agent 需要关系图合并和 replay 验证来保持可复用性
- [DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds](https://arxiv.org/abs/2608.06113) ⭐5 · 2026-08-06 — CLI agent 训练不能只记住某个 scaffold 的规划格式，planning 需要变成模型可迁移能力
- [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](https://arxiv.org/abs/2608.06305) ⭐5 · 2026-08-06 — 表格密集长文档的 RAG 需要可回放操作轨迹，不能只相信 top-k embedding 相似度

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 254 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 227 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 125 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 42 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 61 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 47 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1725
- 公开展示卡片: 906
- 有全文内容: 820
- 最近 7 天信号: 131
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
