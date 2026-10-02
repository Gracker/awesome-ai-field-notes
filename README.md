# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [aweb: Communication for AI agents](https://aweb.ai) ⭐3 · 2026-10-02 — aweb 给 agent 发明收件箱：稳定身份 + 持久消息 + 唤醒事件，可联邦可自托管，已接 Claude Code 与 Pi
- [Using Opus 5.5 to discover a new eyewitness record of the dodo](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness) ⭐4 · 2026-10-01 — Opus 5.5 在 VOC 档案里挖出 1615 年 dodo 捕猎新目击记录：专家定题语义检索批量精读人工复核的方法链值得抄
- [Pi Durable](https://earendil.com/posts/pi-durable) ⭐4 · 2026-10-01 — Pi Durable：checkpoint 任务模型 + exactly-once 提交 + 可 fork 会话，把极简原则带进长时运行 agent 框架
- [Pi 1.0](https://earendil.com/posts/pi-1-0) ⭐4 · 2026-10-01 — 极简 agent harness Pi 1.0 发布：Codemode 原生 MCP虚拟模型路由中途系统消息，MIT 开源
- [Introducing Clef: our open-source decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models) ⭐4 · 2026-10-01 — Cloudflare 开源决策模型 Clef：冻结 Qwen + prefill-only 并行打分，比 Jev 快且带视觉，Jev API 兼容
- [Fair Moderation, Equitable Access, and AI: arXiv's Updated Rate Limit Policy](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy) ⭐4 · 2026-10-01 — arXiv 限速新政：每月 2 篇在审 3 篇封顶，9 月 4 万投稿与 9 千工单背后是 AI 灌水与版主过载
- [Software Heritage Identifiers](https://nesbitt.io/2026/10/01/software-heritage-identifiers.html) ⭐3 · 2026-10-01 — SWHID 成为 ISO 标准后与 purl 的互补关系首次被完整工程化：swh-git/swhid-go 让按内容寻址克隆归档源码可用
- [Gemini 4 Argon: our next era of frontier intelligence](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon) ⭐5 · 2026-09-30 — Gemini 4 Argon：1M token 输出上限800K 行内核 C/C++Rust 迁移与自主漏洞修复，首批向网络防御者开放
- [How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) ⭐5 · 2026-09-30 — 同等时间预算同 backbone 下，精密 MLE harness 打不过单会话极简 coding agent，收益主要来自模型本身
- [How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text](https://arxiv.org/abs/2609.40295) ⭐5 · 2026-09-30 — 800 个预训练实验证明野生 AI 生成文本对预训练的收益可变号：数据饥饿时先甜后毒，高预算时几乎只有害

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 360 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 490 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 257 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 149 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 172 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 116 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2559
- 公开展示卡片: 1833
- 有全文内容: 1732
- 最近 7 天信号: 136
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `agent-memory`, `coding-agents`, `agents`, `mcp`, `agent-harness`, `google`, `open-source`, `agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
