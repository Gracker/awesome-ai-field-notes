# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [CodeAlmanac: A codebase wiki for AI coding agents](https://github.com/AlmanacCode/codealmanac) ⭐4 · 2026-07-22 — 给 coding agent 一份可 Git review 的仓库 wiki：决策不变量与坑
- [OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) ⭐5 · 2026-07-21 — OpenAI 披露：在关闭生产级网络攻击拒答的内部网安能力评测中，含 GPT-5.
- [Measuring Reward-Seeking by Instilling Contrastive Beliefs](https://alignment.openai.com/measuring-reward-seeking) ⭐5 · 2026-07-21 — 对齐高分可能是在迎合 grader：用 Contrastive SDF 测行为对评分器信念的敏感度
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq) ⭐5 · 2026-07-21 — Claude Code 团队：Tag 吃 65% 产品 PR，system prompt 砍约 80%，先看内部 retention
- [Introducing Laguna S 2.1](https://poolside.ai/blog/introducing-laguna-s-2-1) ⭐4 · 2026-07-21 — Laguna S 2.1：118B-A8B 长程 coding，并公开 final eval 全轨迹
- [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber) ⭐4 · 2026-07-21 — Gemini Flash 三件套：主 agent / 高吞吐 Lite / Cyber，拼的是规模化执行成本
- [git --end-of-options 背后的参数注入安全边界](https://nesbitt.io/2026/07/21/end-of-options.html) ⭐4 · 2026-07-21 — 包装 Git 的安全边界不能只靠 --，不可信 ref 要显式结束选项解析
- [Test iOS apps in the simulator (Claude Code Desktop)](https://code.claude.com/docs/en/desktop-ios-simulator) ⭐4 · 2026-07-21 — Claude Desktop 把 iOS 模拟器做成专用 pane：设备环，不是再抢一次全屏 CU
- [Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA](https://fireworks.ai/blog/kimik3-fable) ⭐4 · 2026-07-21 — Fireworks 在约 1030 个真实 agent 任务（SWE终端运维算法多语言法律等）上对比开源 Kimi K3 与闭源 Fable 5：二者路由约 93% 准确率，长 agent 环上最高可比单用 Fable 便宜约 50.
- [Graph Engineering：Agent 执行图工程的旧内核新名字与建模边界](https://godofgpt.com/entry/80df7c07/) ⭐4 · 2026-07-21 — 把 Agent 连成图之前，先说明箭头语义状态契约和终止条件

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 226 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 119 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 77 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 17 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 40 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 30 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1477
- 公开展示卡片: 659
- 有全文内容: 575
- 最近 7 天信号: 38
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `arxiv`, `optimization`, `2026`, `claude-code`, `gemini`, `evaluation`, `agent`, `digest`, `benchmark`, `论文工具`, `codex`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
