# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [NVIDIA Nemotron 3.5 Super VL: open-weight 120B/12B MoE, AA Intelligence Index 26](https://artificialanalysis.ai/models/nemotron-3-5-super-vl) ⭐4 · 2026-10-15 — 120B/12B 开源 MoE 加 1M 上下文，同级开源里智力靠前且吞吐高，适合做本地/API 推理对照实测
- [Muse Spark Open (Xhigh): Meta open-weight 816B/42B, AA Intelligence Index 39](https://artificialanalysis.ai/models/muse-spark-open) ⭐4 · 2026-10-15 — AA 指数 39 的开源权重变体智力领先档但偏贵：Meta 把闭源产品线下放开源的信号值得跟踪
- [Hermes Agent v0.22.2: gateway-after-reboot fix after wrong-commit 0.22.1](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.2) ⭐4 · 2026-10-15 — 官方承认 0.22.1 打错 commit 并修复重启后 gateway 不拉起：升级前先看 0.22.1 会话无法删除的已知限制
- [Codex 0.163.0: mid-turn steering, searchable /config, parallel read-only tools](https://github.com/openai/codex/releases/tag/rust-v0.163.0) ⭐4 · 2026-10-15 — 0.163 把打断语义和配置发现一次修到位：中途 steer 与并行只读工具是日常手感的实质变化，不只是版本号
- [Claude Code v2.1.301: unattended retry watchdog usage-limit cap](https://github.com/anthropics/claude-code/releases/tag/v2.1.301) ⭐4 · 2026-10-15 — 无人值守重试终于有了熔断阈值，配合分类器决策进 OTEL 事件，长跑 agent 的费用与可观测性边界更清晰
- [Claude Code issue 102597: background agents re-send full context on every macOS DarkWake overnig...](https://github.com/anthropics/claude-code/issues/102597) ⭐4 · 2026-10-15 — 合盖一晚烧掉 81 次全量重发请求：后台 agent 与 macOS 睡眠机制的适配空洞，跑长任务前值得自查电源设置
- [SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm](https://arxiv.org/abs/2610.20431) ⭐4 · 2026-10-14 — 差结果也能喂进进化回路，是 RSI 从单 agent 走向 swarm 编排的关键一步，可复现性仍待第三方验证
- [RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios](https://arxiv.org/abs/2610.19698) ⭐4 · 2026-10-14 — 把规则从单句事实搬进多文件工作区后，前沿模型端到端规则推理最高不过 55%，暴露了 agent 规程执行的真实短板
- [Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](https://arxiv.org/abs/2610.20344) ⭐4 · 2026-10-14 — 首个测 harness 工程本身的确定性基准：GPT-6 Astra 也只过 53%，模型之外的能力差距被长期低估
- [Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control) ⭐5 · 2026-10-13 — Anthropic 工程博客：2026 年 5 月其 monorepo 日均合并约 2500 次代码变更，9 月已超 3 万次/日...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 400 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 552 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 288 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 166 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 199 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 129 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2751
- 公开展示卡片: 2023
- 有全文内容: 1918
- 最近 7 天信号: 123
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `agent-safety`, `mcp`, `agent-harness`, `open-source`, `kv-cache`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
