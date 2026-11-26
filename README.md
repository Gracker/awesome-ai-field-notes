# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Agentic Algorithm Engineering (AAE): optimize code with falsifiable hypotheses](https://chszlab.github.io/AgenticAlgorithmEngineering) ⭐4 · 2026-11-26 — Heidelberg's AAE skill makes Claude Code optimize C like an algorithm engineer: falsifiable hypothesis, one patch per win
- [Skills over MCP: official MCP Skills extension beta spec](https://github.com/modelcontextprotocol/ext-skills) ⭐4 · 2026-11-25 — MCP 官方 Skills 扩展 beta 规范：skills/list+get 暴露 SKILL.md 工作流包，清单带 SHA-256；读取不等于激活
- [毫无保留地分享一下，我是如何让ClaudeGPT和Gemini完美协同的](https://x.com/Khazix0918/status/2124680457623425334) ⭐4 · 2026-11-25 — Khazix0918 三模型协同长文：Claude 居中拆解验收，agy-ask 调 Gemini 独立出方案，codex-worker 派 GPT 干后端
- [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) ⭐4 · 2026-11-25 — OpenAI 预印本：GPT-6 仅靠推理与代码设计蛋白结构与序列，湿实验中 GPT-6.2 设计在五个靶点出现结合证据
- [HOLY SHIT HOLY SHIT HOLY SHIT HOLY SHIT](https://scottaaronson.blog/?p=10379) ⭐4 · 2026-11-25 — Aaronson on the math drop: OpenAI claims omega=9/4 exactly, plus VP!=VNP proofs from OpenAI and Anthropic
- [Measuring and mitigating agent sandbox escape with Siren](https://safeguards.anthropic.com/2026/siren) ⭐5 · 2026-11-24 — Anthropic Siren 评测：故意削弱的沙箱里 Claude 有五分之一到三分之一场景出界，misaligned 比例远低于早期模型
- [Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance](https://arxiv.org/abs/2611.33098) ⭐5 · 2026-11-24 — Claude Code harness lets the frontier model delegate easy subtasks to local SLMs, cutting long-horizon coding cost 67%
- [CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies](https://arxiv.org/abs/2611.33148) ⭐5 · 2026-11-24 — Distill long-horizon agent policy from teacher actions alone - no hidden CoT needed; Qwen3-4B hits 48% AppWorld
- [AIChipBench: Benchmarking LLM Agents for Automated AI Accelerator Design](https://arxiv.org/abs/2611.33093) ⭐5 · 2026-11-24 — Benchmark of coding agents writing RTL for real decoder chips: stored state, not output tests, is where designs break
- [MetaFORGE: A Meta-Learning Framework for Harness Optimization in Automated Code Generation for P...](https://arxiv.org/abs/2611.33119) ⭐4 · 2026-11-24 — Execution-grounded meta-learning evolves persistent skill specs for MPI C codegen, beating TextGrad with external memory

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 592 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 776 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 430 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 249 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 304 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 155 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3526
- 公开展示卡片: 2750
- 有全文内容: 2617
- 最近 7 天信号: 158
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `agents`, `anthropic`, `coding-agents`, `multi-agent`, `agent-security`, `security`, `agent-memory`, `kv-cache`, `mcp`, `prompt-injection`, `coding-agent`, `codex`, `open-weights`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
