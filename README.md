# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Pluralistic: The AI fatfinger economy has come for my receipts app](https://pluralistic.net/2026/11/04/genius-scan-is-neither) ⭐4 · 2026-11-04 — KPI 变成目标函数后，员工和模型一样学会 reward hacking：Doctorow 给每个按钮都换成 AI的 UI 现象起了名字
- [Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding at One-Tenth Cost](https://www.ricursive.com/ripple) ⭐5 · 2026-11-03 — 65B 稠密模型拿下美国开源权重 agentic coding SOTA：1.4M rollouts 的陡峭 RL 爬升加十分之一成本
- [Suppressing Misaligned Behaviors in Language Models, Durably](https://arxiv.org/abs/2611.05358) ⭐4 · 2026-11-03 — 未对齐行为能否持久压制？窄触发/宽触发两个模型生物体把事后抑制变成可对照的实验问题
- [LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers](https://arxiv.org/abs/2611.05304) ⭐4 · 2026-11-03 — LoopVQ 把 looped transformer 的 KV 缓存压到 sub-1-bit：循环轴冗余 + 分 step 敏感度差异是关键
- [Adversarial Speculative Reasoning Improves Long Horizon Agents](https://arxiv.org/abs/2611.05345) ⭐4 · 2026-11-03 — 投机解码在长程 agent 任务里不只是加速器：草稿接受率会改变 30 步后的输出分布与推理准确率
- [A Circuit for In-Context Learning](https://arxiv.org/abs/2611.05344) ⭐4 · 2026-11-03 — ICL 机制拼图补全：标签位键值记忆 + 中层注意力头写入演示类别，任意标签 few-shot 分类首次有完整电路组合
- [Running Dry](https://www.wheresyoured.at/running-dry) ⭐4 · 2026-11-03 — OpenAI 降估值半价募资Anthropic IPO 预期缩水加 BB+ 租约评级：两大实验室的资本面第一次同时亮黄灯
- [Pluralistic: Separable](https://pluralistic.net/2026/11/03/nobody-is-home) ⭐4 · 2026-11-03 — 不是模型变差了，是我们学会了分辨：Doctorow 用表演者分离解释图灵测试失效，把 AI 数学的真相概括为有解无洞见
- [2,377 agent commits in 30 days: the bottleneck is reading, not Git](https://x.com/forzAlex/status/2117426604942950792) ⭐4 · 2026-11-03 — Pando 解决的是 Git 容量，这条一线记录补上另一半：2377 commits/30 天零冲突之后，卡住规模的是人的阅读带宽worktreeallowlist禁自审三条规则值得抄
- [Just a little AI resistance, as a treat](https://shkspr.mobi/blog/2026/11/just-a-little-ai-resistance-as-a-treat) ⭐3 · 2026-11-03 — 谄媚开场em-dash空洞转交认出 AI 客服的指纹后一星抗议，真的换来了真人道歉：一次低成本高回报的抵抗样本

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 476 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 653 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 330 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 204 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 250 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 140 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3072
- 公开展示卡片: 2298
- 有全文内容: 2184
- 最近 7 天信号: 137
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `prompt-injection`, `open-weights`, `safety`, `agent-safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
