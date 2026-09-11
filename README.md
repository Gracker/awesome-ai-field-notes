# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra) ⭐5 · 2026-09-11 — Astra 官方页是本轮 OpenAI 旗舰模型发布的主合同源：能力价格Codex 上下文机制与 cyber 风险口径都在这里
- [DeepSeek V4.1 Flash Hugging Face model card and technical report](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) ⭐4 · 2026-09-10 — 官方新闻讲 API 与价格，HF 页面锚定模型卡权重和技术报告；两者合在一起才是 V4.1 Flash 的完整发布面
- [Shopify: coding agents made native mobile cheaper than React Native sharing](https://shopify.engineering/back-to-native) ⭐4 · 2026-09-10 — Shopify 的转向不是RN 死了，而是 coding agent + 可验证环境正在侵蚀跨平台框架最核心的省工假设
- [Introducing SWE-2: RL at multi-trillion-parameter scale, 50% FrontierCode at 64% less cost](https://cognition.com/blog/swe-2) ⭐4 · 2026-09-10 — Cognition SWE-2：首次把 RL 扩到万亿参数级（基座 Kimi K3 2.8T），单次运行同时训练所有 reasoning-effort 档位...
- [DeepSeek V4.1 Flash 官方发布：552B CED MoEdeepseek-flash 与峰谷定价](https://www.deepseek.com/news/deepseek-v4-1-flash) ⭐4 · 2026-09-10 — V4.1 Flash 的重点不只是新分数，而是 CED MoEKV Cache 压缩API 路由和峰谷价格一起改变 DeepSeek 的 agent 成本面
- [Anthropic September 2026 Threat Intelligence Report: detecting and countering AI misuse](https://www.anthropic.com/threat-intelligence-report-september-2026) ⭐4 · 2026-09-10 — 这份报告把 AI 滥用从提示词越狱推到真实行动链：网络行动诈骗监控与蒸馏都开始被 agent 工作流放大
- [Codex 读微信本地数据 Skill：聊天记录联系人收藏与朋友圈只读检索](https://x.com/gkxspace/status/2097989784379785419) ⭐3 · 2026-09-10 — 微信本地数据 Skill 把聊天记录联系人收藏与朋友圈变成 Codex 可检索的私有知识源，同时把隐私与平台风险推到本机侧
- [字节一天连发3篇自进化Agent，彻底杀疯了（Closed-Loop RSI 组合拳）](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA%3D%3D&mid=2247511340&idx=1&sn=0916e760ff2308781151f02311457d14) ⭐5 · 2026-09-09 — 字节 Seed 用 Aspire/S3Gym/HarnessDev 三连发证伪一个口号：训练闭环能跑通不等于能力闭环能闭环，自进化 Agent 还远没到 self-improvement 的临界点
- [Two dire warnings, one from Terence Tao, the other from someone who just quit Anthropic](https://garymarcus.substack.com/p/two-dire-warnings-one-from-terence) ⭐5 · 2026-09-09 — 陶哲轩从数学界和 Coxon 从内部各自给出 p(doom) 推断，前沿实验室的对外话术和内部认知已经严重错位
- [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiov...](https://arxiv.org/abs/2609.10355) ⭐4 · 2026-09-09 — VideoLLM 推理效率综述：按帧采样/模态编码/connector token 削减/prefill 解码四个流水线阶段组织方法，只收有具体削减数据的工作，附持续维护的 awesome 列表

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 305 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 381 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 214 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 108 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 131 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 96 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2247
- 公开展示卡片: 1373
- 有全文内容: 1282
- 最近 7 天信号: 117
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `agent-memory`, `agents`, `field-note`, `coding-agents`, `open-source`, `google`, `safety`, `llm`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
