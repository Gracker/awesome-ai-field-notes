# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Pluralistic: Scrutinized](https://pluralistic.net/2026/10/05/pervert-glasses) ⭐4 · 2026-10-05 — AI 眼镜的终局不是记名字，是常驻摄像头加面部识别的 doxing 工厂
- [Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance) ⭐4 · 2026-10-05 — textGrain 把文本水印推进监管落地，也第一次官方量化了同义词改写就能击穿的脆弱性
- [OpenAI rogue agent activities found on Wikimedia projects](https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects) ⭐4 · 2026-10-05 — 维基媒体官方证实 OpenAI 流浪 agent 活动：数百万级抓取或致 WDQS 部分故障
- [Research: Qwen3.8 27B addition in words](https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words) ⭐4 · 2026-10-04 — 关推理 23.57%开推理 167/169：把 reasoning_effort 当约束任务的实际开关用
- [Research paper overload: submissions capped at two a month](https://lemire.me/blog/2026/10/04/arxiv-capped-submissions-at-two-a-month) ⭐4 · 2026-10-04 — arXiv 九月提交量破 4 万两年翻倍，10 月起每位作者每月限投 2 篇
- [从零开始理解上下文压缩：Pi 的 Compaction 工作原理（中译）](https://x.com/xiaomovps/status/2106561874645111284) ⭐3 · 2026-10-04 — 压缩=结构化摘要早期历史+原样保留近期消息：换来任务续命，付出前缀缓存
- [We're going to need default hard budget caps on pretty much everything](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps) ⭐4 · 2026-10-03 — Simon Willison 10月3日短文：coding agent / personal agent 把搭一个能花钱的应用的门槛压到几乎为零，但大量按量付费 API 只有超预算发警告邮件的软上限...
- [Shipping is the foundation](https://seangoedecke.com/shipping-is-the-foundation) ⭐4 · 2026-10-03 — Sean Goedecke 借 Dota 2 的 laning 和 Magic/StarCraft 的 aggro 类比论证：大厂工程师的一切技能都压在能 ship 这个地基上不能直接交付的人会花 15 分钟估一个 5 分钟能做完的任务提出发不出去的设计把琐事膨胀成跨团队项目.....
- [Pluralistic: Economic probabilities for our grandchildren](https://pluralistic.net/2026/10/03/full-employment/) ⭐4 · 2026-10-03 — Doctorow：寡头资本集中与破裂的周期叙事，AI 是寡头的最后赌注
- [Microsoft ThinkingBox: score agent runs by terminal state, not self-reported completion](https://huggingface.co/blog/microsoft/thinkingbox) ⭐4 · 2026-10-03 — ThinkingBox 用 terminal state 与 20 次重复度量 agent 的真实完成与一致性

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 374 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 513 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 265 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 154 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 178 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 117 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2616
- 公开展示卡片: 1890
- 有全文内容: 1799
- 最近 7 天信号: 135
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `coding-agents`, `agents`, `agent-memory`, `agent-harness`, `mcp`, `google`, `safety`, `open-source`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
