# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Ornith-1.5: From Self-Scaffolding to Self-Improvement](https://ornith.ai/ornith_1_5.html) ⭐4 · 2026-08-20 — 开源模型 Ornith-1.5：自脚手架升级为端到端自我改进循环，397B MoE 智能体与编码基准对标 Claude Opus 4.8
- [fx: Tiny, open, native coding agent](https://fx.sh) ⭐3 · 2026-08-20 — 6.39MiB10 微秒冷启动的 Zig 版 agent CLI：把 coding agent 做成可嵌入的 Unix 工具
- [Use the built-in GELU, don't roll your own!](https://www.gilesthomas.com/2026/08/built-in-gelu) ⭐3 · 2026-08-20 — 换掉手写 GELU 就白拿 20% 训练吞吐：from-scratch LLM 训练的低成本加速样本
- [Issues in the Repo](https://nesbitt.io/2026/08/20/issues-in-the-repo.html) ⭐3 · 2026-08-20 — GitHub 宕机时的 Plan B 清单：五类把 issue 数据塞回 git 自身的方案与实战命令
- [What Is Reasoning](https://lucumr.pocoo.org/2026/8/19/what-is-reasoning) ⭐4 · 2026-08-19 — 把 reasoning 从营销概念降级为 channel-routing convention：训练出的输出习惯而非神秘能力
- [The ordinariness of evil](https://pluralistic.net/2026/08/19/banaility) ⭐4 · 2026-08-19 — criti-hype：最流行的 AI 批评其实是把 Altman 的营销复读一遍再加(这很糟)
- [OpenRouter is Joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe) ⭐4 · 2026-08-19 — 最大模型聚合网关 OpenRouter 官宣加入 Stripe：日处理 10T+ token400+ 模型1000 万+开发者
- [BREAKING: OpenAI's unraveling has begun](https://garymarcus.substack.com/p/breaking-openais-unraveling-has-begun) ⭐4 · 2026-08-19 — 一条推文一组 WSJ 数字一份 NVIDIA 兜底架构24 小时内看清 OpenAI 解线的三条线头
- [smolmachines / smolvm as a sandbox for untrusted Python & JavaScript](https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox) ⭐3 · 2026-08-19 — 硬件隔离 microVM 沙箱实测：50ms 热执行与完整资源限制，agent 执行环境的对比基线
- [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528) ⭐5 · 2026-08-18 — 把部署 harness 接进 RL 训练循环的轻量开源框架，6K 样本让 9B 模型 SWE-bench 提升 14.6 个点

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 295 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 274 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 143 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 65 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 87 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 66 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1904
- 公开展示卡片: 1068
- 有全文内容: 988
- 最近 7 天信号: 144
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
