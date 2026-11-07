# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [please do not escape: A Dataset of Sandboxes for AI Coding Agents](https://pleasedonotescape.com/) ⭐3 · 2026-11-07 — please do not escape：给 AI coding agent 挑沙箱的数据集，每条记录锚定一手来源
- [Anthropic: The Components of Agent Memory salience, dreaming, and memory stores](https://www.anthropic.com/research/components-of-agent-memory) ⭐5 · 2026-11-06 — 记忆越记越多反而变钝：Anthropic 用 dreaming 在会话外整理 store，wiki 检索 13%48%
- [Cursor Voice Chat: realtime voice calls with coding agents](https://cursor.com/changelog/voice-chat) ⭐4 · 2026-11-06 — coding agent 的监督通道从文字搬进语音：Cursor 用 Grok Voice 让你边跑边问
- [Codex CLI 0.167.0: agent command center, backend switching with draft retention](https://github.com/openai/codex/releases/tag/rust-v0.167.0) ⭐4 · 2026-11-06 — Codex 正式版给终端加 agent 指挥台：多后端切换保草稿，多 agent 并行有了统一视图
- [Claude Code v2.1.319: MCP tasks go background by default, deny-instead-of-prompt permissions](https://github.com/anthropics/claude-code/releases/tag/v2.1.319) ⭐4 · 2026-11-06 — MCP 长任务默认后台化权限可改为拒绝续跑：cron/CI 里的 Claude Code 不再卡权限弹窗
- [中国LLM讨论纪要](https://mp.weixin.qq.com/s?__biz=Mzg3OTg3NTY1OA%3D%3D&mid=2247492486&idx=1&sn=871f27cecf739a57fc03f9369963f9d0) ⭐4 · 2026-11-06 — 一份把算力蒸馏成本格局与 AIDD 全串起来的买方纪要：国内追赶的时间窗正被反蒸馏压缩
- [OpenAI BioBasicsBench: 100 wet-lab tasks test how agents read raw experimental data](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science) ⭐4 · 2026-11-06 — 考科学 agent 读原始实验数据：BioBasicsBench 用 100 个湿实验任务拉开 Astra 与 5.6 Sol 23 分
- [GoLand's Profiler Now Works with AI Agents](https://blog.jetbrains.com/go/2026/11/06/we-gave-ai-agents-goland-s-profiler-they-found-the-same-bottlenecks-with-half-the-tokens) ⭐4 · 2026-11-06 — GoLand 2026.3 让 Claude Code/Codex/Junie 通过 skill+MCP 直接驱动 Go profiler，同一瓶颈只用一半 token
- [First self-hosted readings of Kimi K3.1 Pro pruned75 on dual DGX Station](https://x.com/SJRonanMD/status/2118566508939137043) ⭐4 · 2026-11-06 — 475.5GB 砍 75% 专家的试点读数说明 K3.1 Pro 自部署刚到能出 token阶段，质量复测才是下一关
- [Dwarkesh's Blood on the Clocktower eval: the benchmark where AIs have to lie to win](https://www.dwarkesh.com/p/clocktower) ⭐4 · 2026-11-06 — 386 局狼人杀式评测给 AI 排名：Astra 领先 Opus 4.6 约 430 Elo，差距主要在识破骗局的好人侧

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 491 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 669 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 348 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 207 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 255 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 144 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3133
- 公开展示卡片: 2359
- 有全文内容: 2240
- 最近 7 天信号: 147
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `claude-code`, `agent-security`, `coding-agents`, `security`, `agents`, `agent-memory`, `coding-agent`, `open-weights`, `agent-harness`, `mcp`, `agent-safety`, `prompt-injection`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
