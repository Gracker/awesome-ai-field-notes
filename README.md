# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐4 · 2026-10-16 — Claude 半小时破解 NIST 曲线种子 25 年悬案：五个种子全是 Unix 时间戳播种的 lrand48 输出，传闻的口令哈希并不存在
- [NVIDIA Nemotron 3.5 Super VL: open-weight 120B/12B MoE, AA Intelligence Index 26](https://artificialanalysis.ai/models/nemotron-3-5-super-vl) ⭐4 · 2026-10-15 — 120B/12B 开源 MoE 加 1M 上下文，同级开源里智力靠前且吞吐高，适合做本地/API 推理对照实测
- [Muse Spark Open (Xhigh): Meta open-weight 816B/42B, AA Intelligence Index 39](https://artificialanalysis.ai/models/muse-spark-open) ⭐4 · 2026-10-15 — AA 指数 39 的开源权重变体智力领先档但偏贵：Meta 把闭源产品线下放开源的信号值得跟踪
- [MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](https://arxiv.org/abs/2610.22344) ⭐4 · 2026-10-15 — 35B MoE 用窗口化结果奖励的 RL 学会长周期 ML 工程调优，MLE-Bench Lite 获奖率 37.9% 到 72.7%，追平更大前沿模型
- [Hermes Agent v0.22.2: gateway-after-reboot fix after wrong-commit 0.22.1](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.2) ⭐4 · 2026-10-15 — 官方承认 0.22.1 打错 commit 并修复重启后 gateway 不拉起：升级前先看 0.22.1 会话无法删除的已知限制
- [FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350) ⭐4 · 2026-10-15 — 把 agent 评测从规格明确的工单搬进真实客户交付：最强配置只完整解决 14/95，未言明约束发现是最大瓶颈
- [Discovering state-of-the-art quantum circuits with large language models](https://arxiv.org/abs/2610.22367) ⭐4 · 2026-10-15 — LLM 提案加独立评估器打分的进化搜索，在 8 个量子线路任务里 7 个刷新 SOTA，还找到新的素域模逆可逆架构
- [Codex 0.163.0: mid-turn steering, searchable /config, parallel read-only tools](https://github.com/openai/codex/releases/tag/rust-v0.163.0) ⭐4 · 2026-10-15 — 0.163 把打断语义和配置发现一次修到位：中途 steer 与并行只读工具是日常手感的实质变化，不只是版本号
- [Claude Code v2.1.301: unattended retry watchdog usage-limit cap](https://github.com/anthropics/claude-code/releases/tag/v2.1.301) ⭐4 · 2026-10-15 — 无人值守重试终于有了熔断阈值，配合分类器决策进 OTEL 事件，长跑 agent 的费用与可观测性边界更清晰
- [Claude Code issue 102597: background agents re-send full context on every macOS DarkWake overnig...](https://github.com/anthropics/claude-code/issues/102597) ⭐4 · 2026-10-15 — 合盖一晚烧掉 81 次全量重发请求：后台 agent 与 macOS 睡眠机制的适配空洞，跑长任务前值得自查电源设置

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 402 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 554 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 289 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 166 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 199 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 130 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2757
- 公开展示卡片: 2029
- 有全文内容: 1929
- 最近 7 天信号: 118
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
