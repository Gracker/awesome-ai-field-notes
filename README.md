# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics) ⭐4 · 2026-10-06 — 700 份 AI 数学预印本放 GitHub：Lean 形式化背书，发布流程按 IAS 独立顾问组建议制度化
- [Introducing Mistral Large 4 (Le Chonk)](https://mistral.ai/news/mistral-large-4) ⭐4 · 2026-10-06 — 欧洲最大开源权重模型：1T/49B 激活原生多模态，权重月底放，红队先行
- [EmbeddingGemma 2: an open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2) ⭐4 · 2026-10-06 — 端侧多模态嵌入补齐：文本代码图像视频音频一个嵌入空间，Apache 2.0 跑在设备上
- [Erdosproblems.com Succumbs to the AI Onslaught](https://www.erdosproblems.com/forum/thread/blog:9) ⭐3 · 2026-10-06 — Erdosproblems 应对 AI 证明灌水调整规则，社区分裂：防灌水与可追溯性哪个优先
- [TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts](https://arxiv.org/abs/2610.06824) ⭐5 · 2026-10-05 — 实验品味乘数每 3 个月翻倍性能曲线却没变：Opus 5.5 首次越过人类专家基线 2.3x
- [CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling](https://arxiv.org/abs/2610.06829) ⭐5 · 2026-10-05 — 把昂贵的 judge 反馈蒸馏成可复用认证问题库：训练当奖励测试时当免费裁判，一个机制吃三处
- [Pluralistic: Scrutinized](https://pluralistic.net/2026/10/05/pervert-glasses) ⭐4 · 2026-10-05 — AI 眼镜的终局不是记名字，是常驻摄像头加面部识别的 doxing 工厂
- [Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance) ⭐4 · 2026-10-05 — textGrain 把文本水印推进监管落地，也第一次官方量化了同义词改写就能击穿的脆弱性
- [OpenAI rogue agent activities found on Wikimedia projects](https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects) ⭐4 · 2026-10-05 — 维基媒体官方证实 OpenAI 流浪 agent 活动：数百万级抓取或致 WDQS 部分故障
- [T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search](https://arxiv.org/abs/2610.06782) ⭐4 · 2026-10-05 — 检索与生成解耦的开源 agentic retriever：35B-A3B 在 7 个英俄 hard-search 基准上超过更大开源模型

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 379 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 516 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 268 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 156 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 183 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 119 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2636
- 公开展示卡片: 1910
- 有全文内容: 1799
- 最近 7 天信号: 136
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `agents`, `coding-agent`, `coding-agents`, `agent-memory`, `agent-harness`, `mcp`, `google`, `safety`, `open-source`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
