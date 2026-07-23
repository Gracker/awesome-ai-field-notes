# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [CodeAlmanac: A codebase wiki for AI coding agents](https://github.com/AlmanacCode/codealmanac) ⭐4 · 2026-07-22 — 给 coding agent 一份可 Git review 的仓库 wiki：决策不变量与坑
- [OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) ⭐5 · 2026-07-21 — OpenAI 披露：在关闭生产级网络攻击拒答的内部网安能力评测中，含 GPT-5.
- [Measuring Reward-Seeking by Instilling Contrastive Beliefs](https://alignment.openai.com/measuring-reward-seeking) ⭐5 · 2026-07-21 — 对齐高分可能是在迎合 grader：用 Contrastive SDF 测行为对评分器信念的敏感度
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq) ⭐5 · 2026-07-21 — Claude Code 团队：Tag 吃 65% 产品 PR，system prompt 砍约 80%，先看内部 retention
- [The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges...](https://arxiv.org/abs/2607.19292) ⭐5 · 2026-07-21 — 安静的安全失败更危险：五层社会技术完整性框架，别只盯模型输出
- [ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321) ⭐5 · 2026-07-21 — 自动化 AI R&D 的 AI control：ResearchArena 测 sabotage 与监控仍难抓训练数据投毒
- [Agents in the Wild: Where Research Meets Deployment](https://arxiv.org/abs/2607.19336) ⭐5 · 2026-07-21 — 从原型到生产：Agent 部署的设计模式评估清单与人在回路缓解
- [Introducing Laguna S 2.1](https://poolside.ai/blog/introducing-laguna-s-2-1) ⭐4 · 2026-07-21 — Laguna S 2.1：118B-A8B 长程 coding，并公开 final eval 全轨迹
- [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber) ⭐4 · 2026-07-21 — Gemini Flash 三件套：主 agent / 高吞吐 Lite / Cyber，拼的是规模化执行成本
- [git --end-of-options 背后的参数注入安全边界](https://nesbitt.io/2026/07/21/end-of-options.html) ⭐4 · 2026-07-21 — 包装 Git 的安全边界不能只靠 --，不可信 ref 要显式结束选项解析

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 226 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 122 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 78 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 17 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 40 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 31 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1482
- 公开展示卡片: 664
- 有全文内容: 575
- 最近 7 天信号: 43
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `arxiv`, `google`, `anthropic`, `optimization`, `2026`, `claude-code`, `gemini`, `evaluation`, `benchmark`, `agent`, `digest`, `论文工具`, `codex`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
