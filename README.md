# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Pluralistic: How an AI moratorium can save AI bosses](https://pluralistic.net/2026/09/16/beggar-thy-neighbor) ⭐4 · 2026-09-16 — Doctorow 把 AI lab 联名呼吁 moratorium 重读成反垄断问题：hyperscaler 单位经济为负靠很快就好融资互相抄袭导致用户用脚投票...
- [Jev means structured output is interesting again](https://seangoedecke.com/jev-means-structured-output-is-interesting-again) ⭐4 · 2026-09-16 — Typesafe 发布的System One模型 Jev 只做结构化输出：最快约 70ms最慢 500ms，单次前向并行给出答案，甚至能实时打 Doom作者承认这个 latency 区间是产品分水岭（fast software 解锁新任务而不只是把旧任务做快）.
- [Mistral x Mozilla: Private, Multilingual AI Browsing](https://mistral.ai/news/mistral-x-mozilla) ⭐4 · 2026-09-16 — Mistral 与 Mozilla 宣布合作：Firefox 的 AI 浏览助手 Smart Window（beta）改用 Mistral 模型驱动，先落地法国和北美，年内扩展到英德四个要点：开源技术需要开源分发渠道；模型针对区域语言方言和文化语境训练...
- [Shadowing the Standard Library: Coding Agents vs Python Module Search Path](https://nesbitt.io/2026/09/15/shadowing-the-standard-library.html) ⭐5 · 2026-09-15 — Andrew Nesbitt 2026-09-15 的工程文：coding agent 解 zip 写一个 Python 解码脚本 触发 import struct，攻击者在同目录放一个 struct.
- [Tell Agents the Why, Not Just the How](https://seangoedecke.com/tell-agents-the-why) ⭐4 · 2026-09-15 — Sean Goedecke 2026-09-15 工程短文：把 spec 换成目标 + 优先级现代模型错的时候不是看不懂，是猜错了用户的优先级.
- [Learning to Solve Hard Problems in RL for LLMs by Never Giving Up](https://mnoukhov.github.io/posts/ngu) ⭐4 · 2026-09-15 — Noukhovitch（Ai2）博客解读论文：发现 LLM-RL 中的Matthew EffectRL 增益与模型初始能力成正比，简单题大幅提升初始 pass@32=0 的难题几乎不动在 Qwen 2.
- [Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking) ⭐4 · 2026-09-15 — Google 发布 Gemini 3.
- [When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control](https://arxiv.org/abs/2609.17516) ⭐4 · 2026-09-15 — CoSQ（Chain-of-Self-Questioning）：纯 prompt 框架，让 LLM 把作答变成条件决策先显式评估回答该问题所需信息是否充分.
- [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523) ⭐4 · 2026-09-15 — ScienceBuddy：把持续进化的科研 agent 塞进研究者日常工作流的交互式科研 workspace...
- [Agentic Societies Need a Social Harness](https://arxiv.org/abs/2609.17527) ⭐4 · 2026-09-15 — Washington 大学等团队提出社会 harness：agentic society 里代理代表不同 principal 跨信任边界自主协作，目标只部分对齐实验显示即使诚实且能干的代理，用现有 harness 和消息原语也常无法达成满意结果.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 320 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 410 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 233 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 115 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 148 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 101 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2341
- 公开展示卡片: 1465
- 有全文内容: 1368
- 最近 7 天信号: 117
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `claude-code`, `agent-security`, `multi-agent`, `security`, `coding-agent`, `agent-memory`, `agents`, `field-note`, `open-source`, `coding-agents`, `google`, `agent`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
