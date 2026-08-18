# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Models Are Getting Dumber on Purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐4 · 2026-08-17 — 反共识归因：事实层正被设计成可选件训练贵迭代慢的知识让位给检索，小模型负责推理
- [Anthropics First Lady Took a Winding Road to the Top](https://www.theinformation.com/articles/anthropics-first-lady-took-winding-road-top) ⭐3 · 2026-08-17 — Anthropic 治理拼图里被忽略的一块：无正式 title 但绕不开的第一夫人侧写
- [Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things](https://simonwillison.net/2026/Aug/16/qwen-38-27b) ⭐4 · 2026-08-16 — 27B 本地模型的首发权威评测：默认 xhigh 推理严重过度思考，关掉后仍是当前最实用的本地模型之一
- [How I think about reducing AI costs](https://martinalderson.com/posts/how-i-think-about-reducing-ai-costs) ⭐4 · 2026-08-16 — AI 账单降本的工程化四层下钻：从拆账换模型到 agent 工具返回限长，每层都有实测数字
- [Anthropics Watermark Text Adulteration in Claude Is a Perversion of Writing](https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing) ⭐4 · 2026-08-16 — 水印反对派的最完整论述：牺牲表达质量换可识别性，且合规范围远超法律底线
- [AI text watermarking is not a big deal](https://seangoedecke.com/ai-text-watermarking-is-not-a-big-deal) ⭐4 · 2026-08-16 — 水印恐慌的工程拆解：采样分布不变输出质量无可测差异，2027 年前人人都会做
- [A Third World Embedded Engineer Responds to "RISC-V: They Should Have Known Better"](https://rvembedded.com/blog_post/12) ⭐3 · 2026-08-16 — 指令集辩论被略掉的一段：十美分与一美元芯片之间的真实边界是运费与可获得性
- [dots3-note-prev: 280B MoE 多模态长上下文 agent 底座（Apache-2.0）](https://huggingface.co/dots-studio/dots3-note-prev) ⭐4 · 2026-08-15 — 280B MoE/16B active/512K 上下文的开源多模态 agent 底座：工程字段已坐实，TEMPO 方法论还停在 X 宣布层
- [OpenSandbox: Secure, Fast, and Extensible Sandbox runtime for AI agents](https://github.com/opensandbox-group/OpenSandbox) ⭐4 · 2026-08-15 — 开源可自托管的 agent sandbox 平台：K8s 调度 + gVisor/Kata/Firecracker 分级隔离 + Credential Vault 不把真密钥给 workload
- [Working With AI Feels More Like Leadership Than Coding](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership) ⭐4 · 2026-08-15 — 上下文工程的一句话版本：给 AI 交代背景好结果的样子和边界带人的技能正在变成带 agent 的技能

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 286 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 266 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 140 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 61 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 78 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 54 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 139 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1860
- 公开展示卡片: 1024
- 有全文内容: 939
- 最近 7 天信号: 118
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `arxiv`, `benchmark`, `research`, `evaluation`, `openai`, `anthropic`, `attention`, `google`, `coding-agent`, `security`, `claude-code`, `multi-agent`, `agent-memory`, `agent-security`, `coding-agents`, `optimization`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
