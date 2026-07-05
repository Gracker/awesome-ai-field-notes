# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514) ⭐4 · 2026-07-02 — 持久化代码库下的分布式 AI 攻击首次被系统量化，提示当前 Monitor 策略同时挡不住 gradual 与 non-gradual 两类注入
- [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509) ⭐3 · 2026-07-02 — 无需训练的 RECONTEXT 把长上下文重新组织为可重放的证据池，给当前大模型补上一块会用上下文的能力
- [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440) ⭐3 · 2026-07-02 — EvoPolicyGym 把自主改进策略从最终分数拆解为预算分配与反馈转化诊断，为 Agent 评测补一块短板
- [Kimi K2.7 Code is generally available in GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot) ⭐4 · 2026-07-01 — Copilot 模型选择器首次引入开源权重模型，Kimi K2.7 Code 正式 GA，重塑开发者对模型成本与可控性的选择空间
- [From brain waves to words: a new path to communication without surgery](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication) ⭐5 · 2026-06-30 — Meta Brain2Qwerty：非侵入式脑信号直接转文字，为瘫痪患者打开免手术沟通路径
- [Introducing GeneBench-Pro](https://openai.com/index/introducing-genebench-pro) ⭐4 · 2026-06-30 — GeneBench-Pro：首个面向真实基因组学工作流的 AI 评测基准
- [Hugging Face 发布新型嵌入模型：性能提升50%，支持128K上下文](https://huggingface.co/blog/new-embedding-models-june-2026) ⭐4 · 2026-06-30 — Hugging Face 发布最新一代嵌入模型，在语义理解能力上提升50%，支持128K超长上下文，适用于大规模文档检索和语义相似性计算
- [Core dump epidemiology: fixing an 18-year-old bug](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐4 · 2026-06-30 — OpenAI 用 core dump 流行病学定位 18 年老 bug，AI 时代工程调试范式新案例
- [Anthropic launches AI drug discovery program](https://www.cnbc.com/2026/06/30/anthropic-launches-ai-drug-discovery-program-claude-science) ⭐4 · 2026-06-30 — Anthropic 启动 Claude for Science 药物发现项目：进军 AI for Biotech
- [How ChatGPT adoption has expanded](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐3 · 2026-06-30 — ChatGPT 全球扩张进入深度使用阶段，新兴市场在低资源语言上增长最快

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 226 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 108 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 69 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 17 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 43 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 28 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 152 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1461
- 公开展示卡片: 643
- 有全文内容: 554
- 最近 7 天信号: 400
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `2026`, `gemini`, `benchmark`, `agent`, `digest`, `论文工具`, `open-source`, `claude-code`, `enterprise`, `codex`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
