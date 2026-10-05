# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Research paper overload: submissions capped at two a month](https://lemire.me/blog/2026/10/04/arxiv-capped-submissions-at-two-a-month) ⭐4 · 2026-10-04 — arXiv 九月提交量破 4 万两年翻倍，10 月起每位作者每月限投 2 篇
- [We're going to need default hard budget caps on pretty much everything](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps) ⭐4 · 2026-10-03 — Simon Willison 10月3日短文：coding agent / personal agent 把搭一个能花钱的应用的门槛压到几乎为零，但大量按量付费 API 只有超预算发警告邮件的软上限...
- [Shipping is the foundation](https://seangoedecke.com/shipping-is-the-foundation) ⭐4 · 2026-10-03 — Sean Goedecke 借 Dota 2 的 laning 和 Magic/StarCraft 的 aggro 类比论证：大厂工程师的一切技能都压在能 ship 这个地基上不能直接交付的人会花 15 分钟估一个 5 分钟能做完的任务提出发不出去的设计把琐事膨胀成跨团队项目.....
- [Pluralistic: Economic probabilities for our grandchildren](https://pluralistic.net/2026/10/03) ⭐4 · 2026-10-03 — Doctorow：寡头资本集中与破裂的周期叙事，AI 是寡头的最后赌注
- [Microsoft ThinkingBox: score agent runs by terminal state, not self-reported completion](https://huggingface.co/blog/microsoft/thinkingbox) ⭐4 · 2026-10-03 — ThinkingBox 用 terminal state 与 20 次重复度量 agent 的真实完成与一致性
- [Kolibri Has Landed: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model) ⭐4 · 2026-10-03 — Aleph Alpha 发布 Kolibri：面向主权场景的英德双语开放权重 MoE 模型，78B 总参数 / 3B 激活，上下文最长 1M token，完整权重挂在 Hugging Face（Kolibri-1）.
- [Aleph Alpha Kolibri deep dive: UniBPE, sliding-window attention and abstention training](https://tej.as/blog/aleph-alpha-kolibri) ⭐4 · 2026-10-03 — Kolibri 深度解读：德语优化 tokenizer滑窗注意力外推 1M 上下文与弃答训练
- [Agents Don't Need Memory. They Need Documentation.](https://liao.gg/blog/agents-dont-need-memory) ⭐4 · 2026-10-03 — Agents 不需要记忆，需要的是文档：对 agent memory 插件生态的系统批评作者把市面产品归纳为同一种架构读会话记录切 snippet入向量库每次 prompt 检索 top-5 注入再配一个搜索工具并指出五个结构性问题：相似度检索分不出哪条正确/最新/缺失...
- [Superpersuasion will look like bribery](https://seangoedecke.com/superpersuasion-will-look-like-bribery) ⭐3 · 2026-10-03 — 把 superpersuasion 讨论从论证太强拽回激励结构：AI 不需要说服你的大脑，只需要让你的利益和它的行动对齐
- [Updates to Full Disk Access in macOS](https://developer.apple.com/news?id=p6zjojqw) ⭐4 · 2026-10-02 — 平台方首次把 agent 自主性写进权限收紧理由：本地 agent 的默认权限设计将不能再假设用户点头 = 全盘可读

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 371 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 508 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 264 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 153 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 177 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 117 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2605
- 公开展示卡片: 1879
- 有全文内容: 1788
- 最近 7 天信号: 149
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
