# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [即将到来的 Loop: coding agent 之上的 harness loop 正在成为第二层接口](https://x.com/yibie/status/2075435834581668088) ⭐5 · 2026-07-27 — harness loop 正在改变 coding agent 的工作方式：人写 loop，loop 驱动模型
- [The Reverse Information Paradox: AI 时代的企业 IP 风险从卖方泄密反过来了](https://x.com/satyanadella/status/2076323181154230284) ⭐5 · 2026-07-27 — AI 时代的信息悖论反转：买方在付费使用的同时，还付出了更宝贵的专有知识
- [Own the Outer Loop: Agent 工程的 Quality / Verdict / Answerability 框架](https://x.com/addyosmani/status/2074927530482835916) ⭐5 · 2026-07-27 — Agent 工程三支柱：Quality（质量证据）Verdict（裁决）Answerability（可解释性）
- [睡眠计算: Agent 运行痕迹的离线记忆巩固模式](https://x.com/yibie/status/2075457839481708960) ⭐4 · 2026-07-27 — Agent 记忆新模式：热路径只记录，离线 GeneratorReflectorCurator 提炼经验
- [入职第一周写 9 个 skill 把 onboarding 变成个人 Agent 工作系统](https://x.com/chenchengpro/status/2080883181683605538) ⭐4 · 2026-07-27 — 把 onboarding 从读文档变成写 skill：9 个个人 Agent skill 覆盖入职全流程
- [Qwen 3.6 35B MoE on RTX 3090: 本地 MoE 推理的 VRAM 和后端取舍](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090) ⭐4 · 2026-07-27 — RTX 3090 跑 Qwen 3.6 35B MoE 实测：Vulkan vs CUDA 后端的 VRAM/速度/上下文长度三角取舍
- [AI 落地不要只盯提效，要接到赚钱和信任](https://x.com/kaitoxhacker/status/2077782013558296630) ⭐4 · 2026-07-27 — To B 的 AI 落地最大阻碍不是技术，而是信任和业务理解
- [Being Linux Torvalds: AI 编程时代，工程师更像项目 maintainer](http://antirez.com/news/171) ⭐5 · 2026-07-26 — AI 编程的专家价值不在写 prompt，而在像 maintainer 一样做方向判断和设计审查
- [当我们聊 Agent OS 时，我们聊些什么](https://mp.weixin.qq.com/s?__biz=MzkzNTk2MDUxMg%3D%3D&mid=2247484348&idx=1&sn=cbf6bd580b44738c6f501f9ffd6383bb&chksm=c3f5eb56a9d66370fc52075887c47735629523dabdbc4cac41a5b90fe09da491d20fd3c16c15) ⭐4 · 2026-07-26 — Agent OS 的核心不是更强聊天框，而是围绕记忆技能权限和数据编织的系统层
- [LLM token relay market: 便宜 token 转售已经变成可套利攻击面](https://simonwillison.net/2026/Jul/26/relay-market) ⭐4 · 2026-07-26 — LLM token 转售黑灰产已成形：API key 池免费试用滥用和盗卡组成了完整套利链

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 230 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 148 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 88 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 25 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 48 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 34 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1541
- 公开展示卡片: 723
- 有全文内容: 639
- 最近 7 天信号: 75
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `arxiv`, `google`, `anthropic`, `benchmark`, `evaluation`, `optimization`, `2026`, `claude-code`, `gemini`, `coding-agent`, `workflow`, `agent`, `digest`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
