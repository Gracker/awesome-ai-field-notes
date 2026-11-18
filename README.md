# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [生产级 Agent 记忆系统现状：分层结构趋同，混合检索成为默认](https://godofgpt.com/entry/4facd1df/) ⭐4 · 2026-11-18 — 本机 Agent 实践笔记综述生产级记忆系统：Mem0State of AI Agent Memory 2026判断注意力在长跨度衰减，2026 年生产系统普遍把记忆做成独立组件，检索栈并行语义/关键词/实体三路融合；arXiv 2511.
- [Pluralistic: Enshittifiers groom us for scammers](https://pluralistic.net/2026/11/18/malice-v-incompetence) ⭐3 · 2026-11-18 — Cory Doctorow 论证平台溃败与诈骗产业是同一件事：官方系统越混乱越不给正常办事路径，骗局每一步就越像正常系统接下来会做的事时间线从 2009 年 Ben Laurie 抱怨 Verified by Visa 开始...
- [My Empire of Sunshine and Roses](https://geohot.github.io//blog/jekyll/update/2026/11/18/my-empire-of-sunshine-and-roses.html) ⭐3 · 2026-11-18 — George Hotz 以反事实差分历史开题：改变世界不是攒一堆署名成果，而是问如果你不存在历史会怎样不同他把 AI 的走向视为已被更高阶系数决定的量，随后给出两个具体怀疑：OpenAI 的广告画的是办公室的形状，真正的活都在几千公里外的机房完成，办公室没有理由继续存在.
- [External sandboxes for coding agents](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents) ⭐5 · 2026-11-17 — Simon Willison 与 Prime Radiant 发布external sandbox模式：agent 本体在沙箱外，执行的代码跑在专用沙箱里.
- [Arize Phoenix format-string injection (CVE-2026-53998, CVSS 10.0) exposes stored LLM secrets](https://github.com/Arize-ai/phoenix/security/advisories/GHSA-gfv3-m769-5xm3) ⭐4 · 2026-11-17 — LLM 观测平台 Arize Phoenix 的 applyChatTemplate GraphQL 端点存在格式串注入（CVE-2026-53998，CVSS 10.
- [Jensen Huang's first public statement since leaving NVIDIA](https://x.com/JensenHuang/status/2122726005219737649) ⭐4 · 2026-11-17 — NVIDIA 创始人黄仁勋 11 月 17 日发去职后首份公开声明：承认个人生活犯下严重错误给董事会制造了麻烦，将配合独立调查.
- [Introducing GPT-6.2 Astra and Sol (OpenAI announcement)](https://openai.com/index/introducing-gpt-6-2-astra-sol) ⭐4 · 2026-11-17 — Introducing GPT-6.2 Astra and Sol (OpenAI announcement)
- [Introducing FrontierHarness Eval v1.1: 22 harnesses x 5 models, the best harness differs per mod...](https://runta.com/blog/introducing-frontierharness-eval-v1-1) ⭐4 · 2026-11-17 — Runta 与 Baseten 的最大规模 harness 榜单：83B token27,280 次 agent 运行，22 harness x 5 模型 x 62 任务 x 4 尝试.
- [GPT6.2 Astra and GPT6.2 Sol (Willison review)](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol) ⭐4 · 2026-11-17 — Simon Willison 实测 OpenAI 新发的 GPT-6.
- [microsoft/onnxruntime and related repos vanish from GitHub; PyPI/NuGet binaries still installabl...](https://github.com/microsoft/onnxruntime) ⭐3 · 2026-11-17 — 22,328 star 的 microsoft/onnxruntime 11-17 从 GitHub 消失：main 连同 onnxruntime-genai-training-inference-examples-extensions 等（报道称至少七个仓库）全部 404.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 547 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 739 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 397 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 236 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 293 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 152 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3384
- 公开展示卡片: 2608
- 有全文内容: 2487
- 最近 7 天信号: 190
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agents`, `coding-agents`, `agent-security`, `security`, `agent-memory`, `kv-cache`, `mcp`, `coding-agent`, `prompt-injection`, `codex`, `open-weights`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
