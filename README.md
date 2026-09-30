# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Anthropic IPO Prospectus Puts Model Risk and Locked Compute on the Same Page](https://www.theguardian.com/technology/2026/sep/29/anthropic-warns-existential-ai-risks-humanity-ipo-document-claude) ⭐5 · 2026-09-29 — Anthropic 招股书未公开,但 Guardian/Reuters/FT 转述已确认两个相邻段落:风险因素约 80/261 页业务描述约 48 页,未来十年 AI 基础设施承诺至少 5180 亿美元,其中约 80% 不可取消或无论使用多少都要付款风险页直接列出 advance...
- [The AI margin collapse is gathering pace](https://martinalderson.com/posts/ai-margin-collapse-gathering-pace) ⭐4 · 2026-09-29 — 把 60 天内各家降价拼成一张账单表：agent 的真实成本在 cache read 而非 input/output 单价，比价口径该换了
- [GLM-5.3 and the spread of advanced cyber capabilities](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) ⭐4 · 2026-09-29 — Anthropic 实测确认开源模型已具备端到端漏洞利用能力且护栏可被简单绕过，发布政策的争论焦点正从能力转向权重可及性
- [Dead Money](https://www.wheresyoured.at/dead-money) ⭐4 · 2026-09-29 — 把 hyperscalerNVIDIA 与 OpenAI/Anthropic 的内部循环和 $570B 债务摆在一张桌上：需求故事现在押在两家互为兜底的客户身上
- [BREAKING: Florida seeks injunction against OpenAI](https://garymarcus.substack.com/p/breaking-florida-seeks-injunction) ⭐3 · 2026-09-29 — 同一天的两件事被并成一条监管曲线：厂商自建 agent 安全平台，州政府直接申请禁令，自愿承诺的效力正在被重新定价
- [TokenCast: Forecasting Token Consumption During LLM Agent Execution](https://arxiv.org/abs/2609.35760) ⭐4 · 2026-09-28 — 同一任务在 LLM 智能体多次执行间 token 消耗可差一个数量级，且总消耗在执行前难以预测TokenCast 为每个执行段学习可组合的成本表示（自身消耗+带来的上下文增长），相邻段复合成累计估计，把前段上下文被后继每次调用重读的隐性成本纳入预测.
- [Shockingly Simple Self-retrospection Improves Agentic Models Without RL](https://arxiv.org/abs/2609.35741) ⭐4 · 2026-09-28 — 提出 Retrospection-Only Fine-Tuning（ROFT）：智能体完成任务后，仅对自己的复盘解释做 next-token 微调，不用外部教师不用奖励策略更新在 Qwen3.
- [KV-streams for Efficient Compaction in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35750) ⭐4 · 2026-09-28 — 拉长智能体 RL 的任务时程被 GPU 显存中的长轨迹上下文卡住，主流上下文压缩策略每次压缩都要反复 prefill，拖垮训练吞吐KV-streams 提出流式前传 KV cache 而非压缩后冲刷，与任意压缩策略即插即用：在三种压缩策略上取得 2.
- [Jeff: Jev-compatible 0.8B decision models, trained at home, ~30 ms](https://github.com/firelex/jeff) ⭐4 · 2026-09-28 — Jeff: Jev-compatible 0.8B decision models, trained at home, ~30 ms
- [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) ⭐4 · 2026-09-28 — Anthropic 发布 Claude 5.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 350 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 477 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 257 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 139 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 168 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 113 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2519
- 公开展示卡片: 1793
- 有全文内容: 1706
- 最近 7 天信号: 122
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `agent-memory`, `coding-agents`, `agents`, `google`, `mcp`, `agent`, `open-source`, `paper`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
