# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Introducing SWE-2: RL at multi-trillion-parameter scale, 50% FrontierCode at 64% less cost](https://cognition.com/blog/swe-2) ⭐4 · 2026-09-10 — Cognition SWE-2：首次把 RL 扩到万亿参数级（基座 Kimi K3 2.8T），单次运行同时训练所有 reasoning-effort 档位...
- [字节一天连发3篇自进化Agent，彻底杀疯了（Closed-Loop RSI 组合拳）](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA%3D%3D&mid=2247511340&idx=1&sn=0916e760ff2308781151f02311457d14) ⭐5 · 2026-09-09 — 字节 Seed 用 Aspire/S3Gym/HarnessDev 三连发证伪一个口号：训练闭环能跑通不等于能力闭环能闭环，自进化 Agent 还远没到 self-improvement 的临界点
- [Two dire warnings, one from Terence Tao, the other from someone who just quit Anthropic](https://garymarcus.substack.com/p/two-dire-warnings-one-from-terence) ⭐5 · 2026-09-09 — 陶哲轩从数学界和 Coxon 从内部各自给出 p(doom) 推断，前沿实验室的对外话术和内部认知已经严重错位
- [GPT-6 Astra, Looped Transformers, and Hidden Reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐4 · 2026-09-09 — Raschka 拆解 GPT-6 Astra：recurrent depth 传闻无官方确认OpenAI 首席科学家"计算图深度在 GPT-4 的 2 倍以内"两可；他的判断是成功主要靠训练配方和数据，环 transformer 被高估，也掩盖不了思维链
- [DeepSeek V4.1 Flash: Pro auto-routed to Flash, Flash series price cut 50%](https://news.ycombinator.com/item?id=49624603) ⭐4 · 2026-09-09 — DeepSeek 9-9 banner 把 V4.1 Flash 超过 V4 ProPro 自动路由到 FlashFlash 系列再砍价 50% 三件事压成同日发布;V4.1 Flash 权重未开源,HF 上 V4.1 零命中
- [Anthropic is building a predictive surveillance system to monitor activists](https://prospect.org/2026/09/09/anthropic-artificial-intelligence-surveillance-system-monitor-activists) ⭐4 · 2026-09-09 — Prospect 把 Anthropic GSOC podcast + WSJ + SF Standard + 招聘 JD 拼成同一张图:Anthropic 用 person-of-interest 流程 + Samdesk OSINT + 报警但不出示证据 + JD 把 act...
- [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiov...](https://arxiv.org/abs/2609.10355) ⭐4 · 2026-09-09 — VideoLLM 推理效率综述：按帧采样/模态编码/connector token 削减/prefill 解码四个流水线阶段组织方法，只收有具体削减数据的工作，附持续维护的 awesome 列表
- [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) ⭐4 · 2026-09-09 — VLM 控机器人的接口设计：语义动作单元给 VLM 推理，本体解释器确定性落地；闭源 frontier 模型零样本可用，小开源模型几个 GPU 小时微调即部署，GUMI 还免遥操作硬件
- [Retrofitting Code Using LLMs to Support Exceptional Behavior](https://arxiv.org/abs/2609.10397) ⭐4 · 2026-09-09 — 新任务：给存量代码按 EBT 测试"补装"异常处理；EXCODER 用静态+动态分析做 context engineering，Qwen 2.5 Coder 32b 上 pass@1 85.92%（+12.56pp），TDD 式补 ERC 的第一个自动化方案
- [MOONWALK: Mediating Operations with Intent-Evidence-Action Alignment Across Junior-Supervisor Re...](https://arxiv.org/abs/2609.10385) ⭐4 · 2026-09-09 — 动画/VFX 前期评审的结构化工作流：意图固化成共享记录判断锚定证据AI 只做行政协调不碰创作方向；实测比纯聊天界面对齐更强决策可追溯

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 303 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 381 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 210 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 106 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 130 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 96 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2238
- 公开展示卡片: 1364
- 有全文内容: 1263
- 最近 7 天信号: 122
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `agent-memory`, `agents`, `open-source`, `google`, `coding-agents`, `safety`, `llm`, `long-context`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
