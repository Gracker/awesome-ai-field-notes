# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [中国LLM讨论纪要](https://mp.weixin.qq.com/s?__biz=Mzg3OTg3NTY1OA%3D%3D&mid=2247492486&idx=1&sn=871f27cecf739a57fc03f9369963f9d0) ⭐4 · 2026-11-06 — 一份把算力蒸馏成本格局与 AIDD 全串起来的买方纪要：国内追赶的时间窗正被反蒸馏压缩
- [First self-hosted readings of Kimi K3.1 Pro pruned75 on dual DGX Station](https://x.com/SJRonanMD/status/2118566508939137043) ⭐4 · 2026-11-06 — 475.5GB 砍 75% 专家的试点读数说明 K3.1 Pro 自部署刚到能出 token阶段，质量复测才是下一关
- [Revolut swaps Claude Code for a Chinese open-weight model, cutting its AI coding costs](https://dealroom.co/news/169124-revolut-swaps-claude-code-for-a-chinese-open-weight-model-cutting-its-ai) ⭐3 · 2026-11-06 — 约两千赞的社区热度背后是真实账本：coding 场景的单位 token 成本已经让自建开源权重赢过订阅
- [GPT-6 Cyber: Advancing the frontier of aligned cybersecurity agents](https://openai.com/index/introducing-gpt-6-cyber) ⭐5 · 2026-11-05 — 首个 Critical 级网络安全模型：能力大涨的同时把越界率压到 0.07%，调用权锁在 Daybreak Red 门后
- [Hermes Agent v0.23.0 - The Hearth Release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0) ⭐4 · 2026-11-05 — 单 gateway 拥有会话加浏览器端完整 Desktop，是 Hermes 从单机工具走向常驻基础设施的一步
- [Claude Code sends your email address to websites via User-Agent header](https://github.com/anthropics/claude-code/issues/107757) ⭐4 · 2026-11-05 — 一份针对 claude-code v2.
- [Build Live Apps in Cursor](https://cursor.com/changelog/build-live-apps) ⭐4 · 2026-11-05 — 把写完就死在 localhost的内部工具直接变成可分享应用，四项发布硬检查是同类平台值得抄的作业
- [Pluralistic: Without CDA 230, Facebook will own the internet forever](https://pluralistic.net/2026/11/05/see-you-in-court) ⭐4 · 2026-11-05 — 反直觉但论证扎实：废 230 利好 Meta 不利好用户；禁抓取与AI 审核两个议程都被点名为大科技的护城河
- [Jepsen: ParticleDB 1.1.4](https://jepsen.io/analyses/particledb-1.1.4) ⭐4 · 2026-11-05 — Jepsen 把LLM 写的数据库钉在案板上：产出速度换来解释并修掉问题能力的退化，而文档这个替代品也由模型生成
- [Introducing Personal Finance in Claude](https://claude.com/resources/articles/introducing-personal-finance-in-claude) ⭐3 · 2026-11-05 — 只读权限加无自营产品的金融问答是克制的好设计，剩下的问题只是账户授权面能否过合规

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 489 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 662 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 339 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 206 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 254 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 140 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3109
- 公开展示卡片: 2335
- 有全文内容: 2220
- 最近 7 天信号: 143
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `claude-code`, `agent-security`, `coding-agents`, `security`, `agents`, `agent-memory`, `open-weights`, `agent-harness`, `coding-agent`, `agent-safety`, `prompt-injection`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
