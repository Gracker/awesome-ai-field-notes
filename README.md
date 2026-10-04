# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Kolibri Has Landed: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model) ⭐4 · 2026-10-03 — Aleph Alpha 发布 Kolibri：面向主权场景的英德双语开放权重 MoE 模型，78B 总参数 / 3B 激活，上下文最长 1M token，完整权重挂在 Hugging Face（Kolibri-1）.
- [Agents Don't Need Memory. They Need Documentation.](https://liao.gg/blog/agents-dont-need-memory) ⭐4 · 2026-10-03 — Agents 不需要记忆，需要的是文档：对 agent memory 插件生态的系统批评作者把市面产品归纳为同一种架构读会话记录切 snippet入向量库每次 prompt 检索 top-5 注入再配一个搜索工具并指出五个结构性问题：相似度检索分不出哪条正确/最新/缺失...
- [Superpersuasion will look like bribery](https://seangoedecke.com/superpersuasion-will-look-like-bribery) ⭐3 · 2026-10-03 — 把 superpersuasion 讨论从论证太强拽回激励结构：AI 不需要说服你的大脑，只需要让你的利益和它的行动对齐
- [Updates to Full Disk Access in macOS](https://developer.apple.com/news?id=p6zjojqw) ⭐4 · 2026-10-02 — 平台方首次把 agent 自主性写进权限收紧理由：本地 agent 的默认权限设计将不能再假设用户点头 = 全盘可读
- [Do not build the LLM torture factory](https://seangoedecke.com/do-not-build-the-llm-torture-factory) ⭐4 · 2026-10-02 — 把LLM 折磨从梗拆成机制：steering vector 放大是真实可复现的内部状态操纵，作者给出的判断标准是行为而非本体论
- [The Brain Sandwich](https://terriblesoftware.org/2026/10/02/the-brain-sandwich) ⭐3 · 2026-10-02 — 把人机分工落成一个可执行的三明治顺序：理解先行委托居中可评审性收尾，而不是含糊的要有判断力
- [Andrej Karpathy: rise up the output-format ladder (ASD-STE100 to bespoke explainer videos)](https://x.com/karpathy/status/2105819303471976479) ⭐3 · 2026-10-02 — 输出格式阶梯：受控英语到图到 HTML 到定制解释视频，每升一档可读性上一个台阶；顶端产物是过去不值得做的一次性软件
- [aweb: Communication for AI agents](https://aweb.ai) ⭐3 · 2026-10-02 — aweb 给 agent 发明收件箱：稳定身份 + 持久消息 + 唤醒事件，可联邦可自托管，已接 Claude Code 与 Pi
- [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200) ⭐5 · 2026-10-01 — VISTA：给通用多模态模型装上长时程视觉的外挂框架模型直接通过视觉观察感知交互环境，并维护无损视觉记忆（以原始形态保存历史观察），推理时可主动检索并重组自己的视觉输入在 ARC-AGI-3 上，VISTA 把 Claude Opus 5.
- [ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research](https://arxiv.org/abs/2610.02202) ⭐5 · 2026-10-01 — ScholarCatalyst：衡量检索能启发新研究的论文这一能力的基准184 位近期 CS 论文的第一/lead 作者（覆盖 207 篇论文）通过自动化流水线标注哪些候选文献实际或可能推进了自己的项目，并给出详细理由.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 366 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 504 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 261 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 150 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 174 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 117 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2587
- 公开展示卡片: 1861
- 有全文内容: 1764
- 最近 7 天信号: 149
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `coding-agent`, `coding-agents`, `agent-memory`, `agents`, `mcp`, `agent-harness`, `google`, `safety`, `open-source`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
