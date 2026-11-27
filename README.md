# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Google Will Make AI Agents Use Its Workspace MCP Servers. The Gmail One Can't Send Email](https://techstackups.com/articles/google-workspace-ai-agents-mcp) ⭐5 · 2026-11-26 — Google mandates Workspace MCP for AI agents from 2027-02-01; Gmail MCP still can't send
- [Don't Ask Again writes plaintext keys into Claude Code settings.local.json](https://news.ycombinator.com/item?id=50407882) ⭐4 · 2026-11-26 — Claude Code's Don't Ask Again stores whole commands with plaintext keys in settings.local.json; ~1122 public copies have keys
- [Agentic Algorithm Engineering (AAE): optimize code with falsifiable hypotheses](https://chszlab.github.io/AgenticAlgorithmEngineering) ⭐4 · 2026-11-26 — Heidelberg's AAE skill makes Claude Code optimize C like an algorithm engineer: falsifiable hypothesis, one patch per win
- [OpenAI may be in cost control mode](https://micjm.com/blog/openai-is-in-cost-control-mode) ⭐4 · 2026-11-26 — Arena data: GPT-6.2 Astra/Sol tuned for cost; reasoning tokens down, p<=0.0064
- [AMD-specific fork of llama.cpp, and the vibe-coded inference engine wave](https://devnull.land/amd-specific-llama-cpp) ⭐4 · 2026-11-26 — Bespoke vibe-coded inference engine wave; AMD llama.cpp patchset lifts 35 to 55 tok/s
- [GPT-6.2 usage accounting corrected: Astra 40% / Sol 25% faster quota exhaustion](https://x.com/thsottiaux/status/2125784147889393806) ⭐3 · 2026-11-26 — OpenAI corrects GPT-6.2 usage accounting: quotas exhaust 40% (Astra) / 25% (Sol) sooner; banked reset compensation issued
- [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) ⭐3 · 2026-11-26 — AI agents working on Git-managed infra made self-hosting experimentation fun again
- [Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust) ⭐5 · 2026-11-25 — Anthropic's Rust migration needed production as oracle: 98% test-green matched only ~25% of production traffic
- [How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository...](https://arxiv.org/abs/2611.34875) ⭐5 · 2026-11-25 — Coding agents' extra edits are mostly tests/docs; code necessity rivals human patches
- [Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934) ⭐5 · 2026-11-25 — Monitor evals mislead: false-negative rates swing 0.5%-23% with attack-policy choice

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 595 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 784 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 435 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 252 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 307 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 155 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3548
- 公开展示卡片: 2772
- 有全文内容: 2638
- 最近 7 天信号: 179
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `agents`, `anthropic`, `coding-agents`, `multi-agent`, `agent-security`, `security`, `agent-memory`, `mcp`, `kv-cache`, `codex`, `prompt-injection`, `agent-safety`, `coding-agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
