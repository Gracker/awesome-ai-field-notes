# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Training a 125M model to autocomplete piano on-device](https://simedw.com/2026/08/20/midi-autocomplete) ⭐4 · 2026-08-20 — 个人项目复盘：125M 参数 transformer 在 iPhone 15 上实时自动补全钢琴演奏（约108 音符/秒），MIDI 表示与数据清洗是关键收益
- [Ornith-1.5: From Self-Scaffolding to Self-Improvement](https://ornith.ai/ornith_1_5.html) ⭐4 · 2026-08-20 — 开源模型 Ornith-1.5：自脚手架升级为端到端自我改进循环，397B MoE 智能体与编码基准对标 Claude Opus 4.8
- [Huzzah: pseudocode prompts as a persistent alternative to coding-agent chats](https://www.danielvaughn.dev/posts/huzzah) ⭐4 · 2026-08-20 — Show HN 实验性编辑器：用持久化伪代码声明替代易失的命令式长文提示，重建人机意图的中心权威
- [Don't paste the AI, please](https://dontpastetheai.com/) ⭐4 · 2026-08-20 — 被广泛传播的社交礼仪站点：别把未读的 LLM 回答直接粘给提问的人，对方也有同样的工具
- [Cerebras CS-4: rack-scale wafer inference, up to 30x faster than GPUs](https://www.cerebras.ai/cs4) ⭐4 · 2026-08-20 — Cerebras 发布 CS-4：三片 WSE-3 Turbo 机柜级推理系统，宣称比 GPU 快至 30 倍每瓦 10T+ 参数模型 1000+ tokens/s
- [fx: Tiny, open, native coding agent](https://fx.sh) ⭐3 · 2026-08-20 — 6.39MiB10 微秒冷启动的 Zig 版 agent CLI：把 coding agent 做成可嵌入的 Unix 工具
- [Use the built-in GELU, don't roll your own!](https://www.gilesthomas.com/2026/08/built-in-gelu) ⭐3 · 2026-08-20 — 换掉手写 GELU 就白拿 20% 训练吞吐：from-scratch LLM 训练的低成本加速样本
- [Issues in the Repo](https://nesbitt.io/2026/08/20/issues-in-the-repo.html) ⭐3 · 2026-08-20 — GitHub 宕机时的 Plan B 清单：五类把 issue 数据塞回 git 自身的方案与实战命令
- [What is Missing from AI Post-Training AI: An Empirical Analysis](https://arxiv.org/abs/2608.19072) ⭐5 · 2026-08-19 — 实证分析公开 post-training 轨迹：agent 的训练策略在开头就锁定，缺的不是经验/指导/推理算力而是执行中重新审视策略的机制
- [SPADE: Self-Play in Adaptive Synthetic Executable Environments](https://arxiv.org/abs/2608.19197) ⭐5 · 2026-08-19 — 自博弈 RL 框架：单个 LLM 同时扮演环境设计者与推理 agent，用可执行代码生成训练环境，30B 规模下八项基准平均 +5.3

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 298 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 277 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 144 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 66 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 88 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 66 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1913
- 公开展示卡片: 1077
- 有全文内容: 997
- 最近 7 天信号: 153
- 输出目录: `dist/`

## 热门标签

`llm`, `arxiv`, `ai-tools`, `benchmark`, `research`, `evaluation`, `openai`, `anthropic`, `attention`, `google`, `coding-agent`, `security`, `multi-agent`, `claude-code`, `agent-memory`, `agent-security`, `open-source`, `coding-agents`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
