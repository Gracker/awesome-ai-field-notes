# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [SWE-Touch: Benchmarking Coding Agents When Users Touch the Code](https://arxiv.org/abs/2608.02499) ⭐5 · 2026-08-03 — SWE-Touch benchmarks coding agents under user code edits in shared workspaces.
- [Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation](https://arxiv.org/abs/2608.02518) ⭐5 · 2026-08-03 — Magnet detects AI misuse assembled across otherwise benign agent sessions.
- [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM...](https://arxiv.org/abs/2608.02560) ⭐4 · 2026-08-03 — PRECOG injects precomputed SSM states to make edge RAG prefill O(1).
- [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via...](https://arxiv.org/abs/2608.02508) ⭐4 · 2026-08-03 — RoMeRL reduces reward contamination in self-evolving agent memory.
- [LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference](https://arxiv.org/abs/2608.02515) ⭐4 · 2026-08-03 — LiveMem frames long-running LLM inference as state continuity under context turnover.
- [AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies](https://arxiv.org/abs/2608.02569) ⭐4 · 2026-08-03 — AtumAI formalizes datacenter policy design for agentic search and refinement.
- [A Taxonomy of Cognitive Capability Gaps in Generative and Agentic AI](https://arxiv.org/abs/2608.02553) ⭐4 · 2026-08-03 — A taxonomy of capability gaps for long-horizon cognitive and agentic AI.
- [I'm (mostly) picking models on speed now, not intelligence](https://martinalderson.com/posts/speed-vs-intelligence) ⭐4 · 2026-08-02 — 当主流模型已足够聪明时，速度和等待成本开始决定日常模型选择，而不只是能力榜单
- [Prevent cognitive debt by manually retyping LLM-generated code](https://ankursethi.com/blog/prevent-cognitive-debt-by-manually-retyping-llm-generated-code) ⭐4 · 2026-08-02 — A developer workflow note on avoiding cognitive debt from LLM-generated code.
- [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678) ⭐5 · 2026-07-31 — TokTier shows tokenization can dominate TTFT once agent prompt-cache hit rates get high.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 249 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 201 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 113 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 36 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 60 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 40 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1668
- 公开展示卡片: 849
- 有全文内容: 756
- 最近 7 天信号: 111
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `openai`, `arxiv`, `evaluation`, `attention`, `anthropic`, `google`, `optimization`, `coding-agent`, `coding-agents`, `agent-security`, `claude-code`, `2026`, `security`, `gemini`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
