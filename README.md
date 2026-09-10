# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [字节一天连发3篇自进化Agent，彻底杀疯了（Closed-Loop RSI 组合拳）](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA%3D%3D&mid=2247511340&idx=1&sn=0916e760ff2308781151f02311457d14) ⭐5 · 2026-09-09 — 字节 Seed 用 Aspire/S3Gym/HarnessDev 三连发证伪一个口号：训练闭环能跑通不等于能力闭环能闭环，自进化 Agent 还远没到 self-improvement 的临界点
- [Two dire warnings, one from Terence Tao, the other from someone who just quit Anthropic](https://garymarcus.substack.com/p/two-dire-warnings-one-from-terence) ⭐5 · 2026-09-09 — 陶哲轩从数学界和 Coxon 从内部各自给出 p(doom) 推断，前沿实验室的对外话术和内部认知已经严重错位
- [DeepSeek V4.1 Flash: Pro auto-routed to Flash, Flash series price cut 50%](https://news.ycombinator.com/item?id=49624603) ⭐4 · 2026-09-09 — DeepSeek 9-9 banner 把 V4.1 Flash 超过 V4 ProPro 自动路由到 FlashFlash 系列再砍价 50% 三件事压成同日发布;V4.1 Flash 权重未开源,HF 上 V4.1 零命中
- [Anthropic is building a predictive surveillance system to monitor activists](https://prospect.org/2026/09/09/anthropic-artificial-intelligence-surveillance-system-monitor-activists) ⭐4 · 2026-09-09 — Prospect 把 Anthropic GSOC podcast + WSJ + SF Standard + 招聘 JD 拼成同一张图:Anthropic 用 person-of-interest 流程 + Samdesk OSINT + 报警但不出示证据 + JD 把 act...
- [How banked Codex resets work](https://help.openai.com/articles/20001498-how-banked-codex-resets-work) ⭐3 · 2026-09-09 — OpenAI 官方说明 banked Codex resets 的发放窗口(9-3 / 9-4 / 9-7 三轮)与消耗规则:未触发窗口重置不消耗9-7 那轮是常规重置不可留存
- [Codex & ChatGPT team: banked resets not fully applying in Work/Codex](https://x.com/thsottiaux/status/2097752790177370535) ⭐3 · 2026-09-09 — Codex/ChatGPT 团队 Sottiaux 9-9 公开承认 banked reset 点用未完整生效,承诺补发;用户跟帖补到周限额未刷新账户报错9-7 全球 reset 部分账号未到账
- [Concentration Risk](https://www.wheresyoured.at/concentration-risk) ⭐5 · 2026-09-08 — AI 不是炒作，金融工程结构要塌：头部 lab 80% 收入来自 1% 客户，2027 take-or-pay 重置期一过，云厂的账面跟着炸
- [The Education of a Doomer](https://borretti.me/article/the-education-of-a-doomer) ⭐4 · 2026-09-08 — Borretti 把 doomer 论证推到一个不舒服的位置：disempowerment 不靠超级智能降临，靠囚徒博弈和人类主动交权，现在已经发生
- [OpenAI claims NavierStokes existence-and-smoothness result, with Lean formalisation](https://openai.com/index/navier-stokes-solution) ⭐4 · 2026-09-08 — OpenAI 公布 3D 不可压缩 NavierStokes 方程有限时间奇点的证明草稿以及 Lean 定理化，回应了七大千科贩奖之一它们说明证明由一个内部体系完成，能力显著高于 GPT-6 AstraLean 项目已公开于 github.
- [i-have-adhd: a skill that keeps coding agents action-first](https://github.com/ayghri/i-have-adhd) ⭐3 · 2026-09-08 — 一个面向 AI 代码助手的轻量插件/技能包，安装后能让Claude CodeCodex 类工具在帮助开发者时先给动作再讲步骤，避免Hope this helps!

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 301 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 377 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 207 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 104 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 130 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 95 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2226
- 公开展示卡片: 1352
- 有全文内容: 1261
- 最近 7 天信号: 114
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `agent-memory`, `agents`, `open-source`, `google`, `coding-agents`, `safety`, `reasoning`, `long-context`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
