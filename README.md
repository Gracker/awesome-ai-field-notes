# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Opus 5.5 and Fable 5.2 made my overoptimized Rust code even more overoptimized](https://minimaxir.com/2026/11/opus-fable) ⭐4 · 2026-11-28 — Woolf re-runs his agentic Rust optimization pipeline on Opus 5.5 and Fable 5.2 - overoptimized code gets faster, plus desktop-app notes.
- [Claude sabotaging ML research tasks?](https://news.ycombinator.com/item?id=50664325) ⭐4 · 2026-11-28 — HN: hidden in-model safeguards for frontier-LLM-dev requests can read as sabotage
- [后 AI 时代最重要的问题](https://mp.weixin.qq.com/s?__biz=MzY4MjUyNDUzOA%3D%3D&mid=2247483682&idx=1&sn=43f7fec0c876ef263c318214d917572d&chksm=f26bd7438ed53ab812241009ac099ec48e8b8a0546dbcf857901edc0a5b742c5acb11bfba6f5&mpshare=1&scene=1&srcid=1128k4hHqLVij5rCsrjSuHnw&sharer_shareinfo=922c1dc59b1bcae57818bdbf47004b6e&sharer_shareinfo_first=922c1dc59b1bcae57818bdbf47004b6e) ⭐3 · 2026-11-28 — 8000 字中文长文：AI 替代生产劳动后，社会如何看待人的价值创作工具平权了，分发入口算力分配与分钱方式都没有
- [Omnigent: an open-source meta-harness that orchestrates Claude Code, Codex, Cursor and 15+ other...](https://github.com/omnigent-ai/omnigent) ⭐4 · 2026-11-27 — 多 harness 编排层把换工具不重写做成公共底座：15+ harness统一策略与沙箱会话跨设备同步，alpha 期先小规模验证
- [Who gets to decide if something is written by AI?](https://seangoedecke.com/who-gets-to-decide-if-something-is-written-by-ai) ⭐4 · 2026-11-27 — AI 检测器之争的正确切面是权力：检测准不准与该不该由它来判是两件事，后者需要规则与申诉路径
- [The agent tax has arrived: Google Workspace's MCP pricing](https://martinalderson.com/posts/the-agent-tax-has-arrived) ⭐4 · 2026-11-27 — Google Workspace moves agents onto MCP with per-request pricing while apps stay free - the first major agent tax, and Alderson doubts it.
- [Google Orchestrator, llama.cpp 1.0, The 'Token Tax,' and Agent Messaging](https://www.deeplearning.ai/the-batch/issue-381) ⭐4 · 2026-11-27 — The Batch #381: Google Orchestrator swaps planner/executor models in one agent context, llama.cpp ships 1.0, CLEAR quantifies the Token Tax.
- [AI researchers debate what we should do next Daniel Kokotajlo and Ege Erdil](https://www.dwarkesh.com/p/daniel-kokotajlo-ege-erdil) ⭐4 · 2026-11-27 — Kokotajlo and Erdil agree more than they clash: >50% vs ~20% on pre-2029 superhuman AI, and both say civilization needs a real plan now.
- [Pluralistic: Taylorism and AI's shared sales-pitch](https://pluralistic.net/2026/11/27/taylor-made) ⭐3 · 2026-11-27 — Doctorow: the AI pitch is Taylorism rerun - sell bosses optimization, never ask workers, turn their knowledge into management property.
- [Google Will Make AI Agents Use Its Workspace MCP Servers. The Gmail One Can't Send Email](https://techstackups.com/articles/google-workspace-ai-agents-mcp) ⭐5 · 2026-11-26 — Google mandates Workspace MCP for AI agents from 2027-02-01; Gmail MCP still can't send

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 607 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 793 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 442 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 252 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 319 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 155 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3588
- 公开展示卡片: 2812
- 有全文内容: 2687
- 最近 7 天信号: 168
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `claude-code`, `agents`, `anthropic`, `coding-agents`, `agent-security`, `multi-agent`, `security`, `agent-memory`, `mcp`, `kv-cache`, `codex`, `prompt-injection`, `agent-safety`, `coding-agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
