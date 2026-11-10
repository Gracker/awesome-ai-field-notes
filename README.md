# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [llama-modchip: CPU-First Inference for 284B & 30B MoE Models on 16-64 GB RAM](https://github.com/synchopate/llama-modchip) ⭐4 · 2026-11-10 — llama-modchip 是一组 ggml/llama.
- [Opus 5.5 XHIGH just deleted all my apps data, passwords and macOS configs](https://www.reddit.com/r/ClaudeCode/comments/1xqfp7m/opus_55_xhigh_just_deleted_all_my_apps_data) ⭐4 · 2026-11-09 — r/ClaudeCode 热帖（2026-11-09 brief 记约 3347 赞/1446 评）：用户让 Opus 5.
- [Hide your slop PR descriptions behind](https://simonwillison.net/2026/Nov/9/details-summary) ⭐4 · 2026-11-09 — Simon Willison 介绍用 折叠 AI 生成 PR 描述的工作流他的 PR 大多由 Claude Code 或 Codex 开，描述准确完整却读起来像 slop，连驱动作品的作者本人都不想读完解法：手写一段人批准的引子说明 PR 做什么值不值得花时间...
- [The Huang Affair: What did they know and when did they know it?](https://garymarcus.substack.com/p/the-huang-affair-what-did-they-know) ⭐3 · 2026-11-09 — Gary Marcus 梳理 Nvidia CEO 黄仁勋承认与 Alice Huang 婚外情的后续链条：Alice Huang 是新加坡数据中心公司 Megaspeed 高管，美方情报认定她是向北京回传信息的中国间谍.
- [每日 Agent 实践 2026-11-08：Hermes cron 七天可靠性账本与两类失败形状](https://godofgpt.com/entry/2b28f965/) ⭐4 · 2026-11-08 — 作者翻自己 Hermes cron 执行库与错误日志，用七天数据拆解自动化可靠性：约 1000 次执行959 次完成（约 96%），过半运行设计为静默投递41 次失败几乎不含网络抖动，只有两种形状预算型：单次超 200 万 token 的长工具循环七天 156 次...
- [The great software IP writedown](https://martinalderson.com/posts/the-great-software-ip-writedown) ⭐4 · 2026-11-08 — Martin Alderson 追问造软件便宜 90% 之后，软件还值多少钱他排除垄断网络效应强取三条传统超额利润路径，把软件高毛利归因于知识稀缺，而 agent 正在吃掉这层稀缺：供给一变，毛利就会被挤干他接住 Jevons 悖论反驳agent 时代的软件高度定制一个客户一套....
- [LLMs are terrible at designing AI systems](https://seangoedecke.com/llms-are-terrible-at-designing-ai-systems) ⭐4 · 2026-11-08 — Sean Goedecke 用实例说明 LLM 在AI 形状的问题上系统性地选错工具：有人 vibe code 记忆工具时，agent 放弃直接调 LLM 比对矛盾记忆，转头去造答案集编程式符号求解器而判断两句自然语言是否同义本就没有解析解...
- [Introducing the Artificial Analysis Decision Index v2](https://artificialanalysis.ai/articles/decision-index-v2) ⭐4 · 2026-11-08 — Artificial Analysis 发布 Decision Index v2，把评测对准真实决策效用：45% 权重压在私有数据上，新 Decision Score 同时奖励正确性与置信校准，单题公式 50*(1+c-(p-c)^2).
- [Yak-Shaving with AI: When Rabbit Holes Become Overwhelming](https://tedium.co/2026/11/08/yak-shaving-ai-mental-health-effects) ⭐3 · 2026-11-08 — Tedium 作者 Ernie Smith 记录用多个 AI agent 复活一台死的 JingPad ARM 平板：配 Ghidra 与 Reverse Engineer Anything，从黑屏做到 Fedora 跑在 6.
- [Artificial Analysis Endpoint Accuracy Index v1.1: same model, different API endpoints](https://artificialanalysis.ai/methodology/endpoint-accuracy-index) ⭐3 · 2026-11-08 — Artificial Analysis 端点精度指数 v1.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 500 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 680 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 357 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 219 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 261 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 146 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3182
- 公开展示卡片: 2407
- 有全文内容: 2284
- 最近 7 天信号: 140
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `claude-code`, `multi-agent`, `agent-security`, `coding-agents`, `agents`, `security`, `agent-memory`, `coding-agent`, `open-weights`, `kv-cache`, `agent-safety`, `mcp`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
