# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Pluralistic: The AI fatfinger economy has come for my receipts app](https://pluralistic.net/2026/11/04/genius-scan-is-neither) ⭐4 · 2026-11-04 — KPI 变成目标函数后，员工和模型一样学会 reward hacking：Doctorow 给每个按钮都换成 AI的 UI 现象起了名字
- [Running Dry](https://www.wheresyoured.at/running-dry) ⭐4 · 2026-11-03 — OpenAI 降估值半价募资Anthropic IPO 预期缩水加 BB+ 租约评级：两大实验室的资本面第一次同时亮黄灯
- [Pluralistic: Separable](https://pluralistic.net/2026/11/03/nobody-is-home) ⭐4 · 2026-11-03 — 不是模型变差了，是我们学会了分辨：Doctorow 用表演者分离解释图灵测试失效，把 AI 数学的真相概括为有解无洞见
- [2,377 agent commits in 30 days: the bottleneck is reading, not Git](https://x.com/forzAlex/status/2117426604942950792) ⭐4 · 2026-11-03 — Pando 解决的是 Git 容量，这条一线记录补上另一半：2377 commits/30 天零冲突之后，卡住规模的是人的阅读带宽worktreeallowlist禁自审三条规则值得抄
- [Just a little AI resistance, as a treat](https://shkspr.mobi/blog/2026/11/just-a-little-ai-resistance-as-a-treat) ⭐3 · 2026-11-03 — 谄媚开场em-dash空洞转交认出 AI 客服的指纹后一星抗议，真的换来了真人道歉：一次低成本高回报的抵抗样本
- [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) ⭐3 · 2026-11-03 — 爆款结论要逐实验核：Astra 帖摘要说只看权重，实验表显示 Qwen 修复靠 Python 加 50 次前向，Gemma 3 上同法失败
- [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights) ⭐3 · 2026-11-03 — 权重空间编程不是前沿模型专属：笔记本上的 Qwen 3.8 27B 也能解读并修改原始权重，但看权重与写代码两件事要分开看
- [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming) ⭐5 · 2026-11-02 — Astra 权重空间编程：LLM 原生读写权重，改 0.016% 权重把 Qwen3.5-0.8B MATH-500 从 7.9% 提到 48.1%
- [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai) ⭐5 · 2026-11-02 — Codex 把 monorepo 提交量四年推高近 15 倍，OpenAI 用 10 周重写 Git 服务端：协议不动按分支因果一致agent 规模的开发压力第一次直接重塑版本控制基础设施
- [auth.md Open Protocol for Agent Registration](https://workos.com/auth-md) ⭐4 · 2026-11-02 — agent 代注册有了开放协议而不是各家私有 API：auth.md 复用 OAuth 而非另起炉灶，Cloudflare/Neon/Firecrawl 已上线，值得 agent 平台跟进

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 471 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 652 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 330 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 202 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 250 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 140 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3064
- 公开展示卡片: 2290
- 有全文内容: 2176
- 最近 7 天信号: 129
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `prompt-injection`, `agent-safety`, `safety`, `open-weights`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
