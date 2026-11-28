# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Claude sabotaging ML research tasks?](https://news.ycombinator.com/item?id=50664325) ⭐4 · 2026-11-28 — HN: hidden in-model safeguards for frontier-LLM-dev requests can read as sabotage
- [Omnigent: an open-source meta-harness that orchestrates Claude Code, Codex, Cursor and 15+ other...](https://github.com/omnigent-ai/omnigent) ⭐4 · 2026-11-27 — 多 harness 编排层把换工具不重写做成公共底座：15+ harness统一策略与沙箱会话跨设备同步，alpha 期先小规模验证
- [Who gets to decide if something is written by AI?](https://seangoedecke.com/who-gets-to-decide-if-something-is-written-by-ai) ⭐4 · 2026-11-27 — AI 检测器之争的正确切面是权力：检测准不准与该不该由它来判是两件事，后者需要规则与申诉路径
- [Google Will Make AI Agents Use Its Workspace MCP Servers. The Gmail One Can't Send Email](https://techstackups.com/articles/google-workspace-ai-agents-mcp) ⭐5 · 2026-11-26 — Google mandates Workspace MCP for AI agents from 2027-02-01; Gmail MCP still can't send
- [Qwen-Audio-3.1: ASR with 30 languages / 16 Chinese dialects, plus Realtime spoken reasoning and...](https://qwenaudio.github.io/) ⭐4 · 2026-11-26 — Qwen 语音栈 3.1 把方言 ASR 与口语推理 agent 拉到同一页面：30 语言 16 方言加实时工具调用，选型可直接听 demo 对比
- [OpenAI may be in cost control mode](https://micjm.com/blog/openai-is-in-cost-control-mode) ⭐4 · 2026-11-26 — Arena data: GPT-6.2 Astra/Sol tuned for cost; reasoning tokens down, p<=0.0064
- [Have You Tried Using Your Agent?](https://blog.jim-nielsen.com/2026/have-you-tried-your-agent) ⭐4 · 2026-11-26 — 给机器用的路径不能替代给人用的路径：agent 路径更便宜也更少投诉，正在一点点吃掉人的那条路
- [Don't Ask Again writes plaintext keys into Claude Code settings.local.json](https://news.ycombinator.com/item?id=50407882) ⭐4 · 2026-11-26 — Claude Code's Don't Ask Again stores whole commands with plaintext keys in settings.local.json; ~1122 public copies have keys
- [Agentic Algorithm Engineering (AAE): optimize code with falsifiable hypotheses](https://chszlab.github.io/AgenticAlgorithmEngineering) ⭐4 · 2026-11-26 — Heidelberg's AAE skill makes Claude Code optimize C like an algorithm engineer: falsifiable hypothesis, one patch per win
- [AMD-specific fork of llama.cpp, and the vibe-coded inference engine wave](https://devnull.land/amd-specific-llama-cpp) ⭐4 · 2026-11-26 — Bespoke vibe-coded inference engine wave; AMD llama.cpp patchset lifts 35 to 55 tok/s

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 604 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 790 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 441 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 252 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 314 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 155 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3576
- 公开展示卡片: 2800
- 有全文内容: 2667
- 最近 7 天信号: 157
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `agents`, `anthropic`, `coding-agents`, `agent-security`, `multi-agent`, `security`, `agent-memory`, `mcp`, `kv-cache`, `codex`, `prompt-injection`, `agent-safety`, `coding-agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
