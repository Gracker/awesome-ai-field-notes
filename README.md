# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [2,377 agent commits in 30 days: the bottleneck is reading, not Git](https://x.com/forzAlex/status/2117426604942950792) ⭐4 · 2026-11-03 — Pando 解决的是 Git 容量，这条一线记录补上另一半：2377 commits/30 天零冲突之后，卡住规模的是人的阅读带宽worktreeallowlist禁自审三条规则值得抄
- [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming) ⭐5 · 2026-11-02 — Astra 权重空间编程：LLM 原生读写权重，改 0.016% 权重把 Qwen3.5-0.8B MATH-500 从 7.9% 提到 48.1%
- [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai) ⭐5 · 2026-11-02 — Codex 把 monorepo 提交量四年推高近 15 倍，OpenAI 用 10 周重写 Git 服务端：协议不动按分支因果一致agent 规模的开发压力第一次直接重塑版本控制基础设施
- [Reliably aligning LLMs is impossible in principle](https://www.seangoedecke.com/alignment-is-impossible) ⭐4 · 2026-11-02 — Sean Goedecke 认为可靠对齐 LLM不只做不到，连成功标准都无法连贯定义LLM 不是盲优化器：它训练于模仿庞大人类语料，内部是随输入切换的人格混合，没有可形式化的固定目标可指定...
- [Cursor marketplace compromise of Claude Code extension: official security notice](https://cursor.com/blog/claude-code-extension-security-notice) ⭐4 · 2026-11-02 — Cursor 官方公告确认：10 月 29 日 2:2713:35（太平洋时间）间，其市场上的 Anthropic.
- [Mathematics has changed. Let's act like it](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it) ⭐5 · 2026-11-01 — Calegari 客座 Tao 博客：OpenAI 700 篇论文是数学分水岭，社区该改评审/招聘/期刊机制而非悲伤
- [Hermes 190 个 cron 任务复盘：看门狗时代结束，上下文预算成为新单点](https://godofgpt.com/entry/cb9c878c/) ⭐3 · 2026-11-01 — 对本机 190 个 Hermes cron 任务的复盘：127 个禁用任务里 101 个属于旧的五段式流水线（采集/成稿/发布/通知/看门狗），现已被 15 个单任务替代，18 个看门狗只剩 1 个启用合并消掉了交接失败面...
- [Google Project Suncatcher: first AI response from a data-center-class TPU in orbit](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-satellite-response) ⭐3 · 2026-11-01 — Google 轨道 TPU 卫星跑通首个 AI 响应：星上 Gemma 4 生成俳句下行回传，下一步验证热应力与辐射下的工作负载.
- [VOLTA-AUTODOXER: infostealer outsources victim appraisal to LLMs via OpenRouter](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer) ⭐4 · 2026-10-31 — Cisco Talos 披露 VOLTA-AUTODOXER：窃密木马偷完凭据后把序列化受害者档案 POST 给 OpenRouter，让模型以 forensic analyst 身份输出 WHAT THEY'RE WORTH 与 THEIR OPSEC.
- [Report from the Vatican](https://garymarcus.substack.com/p/report-from-the-vatican) ⭐4 · 2026-10-31 — Gary Marcus 记述在梵蒂冈见到教皇利奥十四世，转录其 AI 讲话五条主张（引 2026 年 5 月通谕Magnifica Humanitas编号）：AI 的未来没有被预先决定；机器无身体不经历体验（编号 99）...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 469 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 647 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 329 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 199 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 245 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 140 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3048
- 公开展示卡片: 2274
- 有全文内容: 2163
- 最近 7 天信号: 120
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `coding-agents`, `security`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `prompt-injection`, `agent-safety`, `open-weights`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
