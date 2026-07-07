# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Context graphs: how AI agents can store and use past decisions](https://nanonets.com/blog/what-is-a-context-graph) ⭐3 · 2026-07-05 — context graph 把 Agent 记忆从相似段落堆升级为带类型的实体-关系图，并把每次决策沉淀为 trace
- [转发一下 B 站博主的锐评 PPT skills：](https://godofgpt.com/entry/4932ce54/) ⭐3 · 2026-07-04 — 注意：有些 skill 不是专门做 PPT 的，所以评分会有点低，只是需求不同，想专门做 PPT 的看最前面的 1.
- [最近这几个月分享了太多关于Codex的玩法了，横跨了赚钱自媒体视频记忆系统APP开发上架教程等多个领域，大家进行系统学习的时候，可以把这篇推文发给Codex，让它给你推荐阅读路径](https://godofgpt.com/entry/87587bbf/) ⭐3 · 2026-07-04 — 最近这几个月分享了太多关于Codex的玩法了，横跨了赚钱自媒体视频记忆系统APP开发上架教程等多个领域，大家进行系统学习的时候，可以把这篇推文发给Codex，让它给你推荐阅读路径
- [摁头推荐，Codex必安的一个插件！](https://godofgpt.com/entry/f7c494dc/) ⭐3 · 2026-07-04 — Codex我用下来有个很大的问题，就是哪怕是一个非常复杂的任务，它都不会主动地去调用Agents Team相较而言， claude code就非常的主动 作者: zjp1997720 (智见AI-大鹏) 链接:
- [吴恩达三言两语，就把 Loop Engineering 说清楚了](https://godofgpt.com/entry/4ea0241d/) ⭐3 · 2026-07-04 — 吴恩达果然厉害前两天在他的 Newsletter 中，短短几句话就把 Loop Engineerring 这个新词的本质说清楚了 作者: xiaogaifun (小盖) 链接:
- [Prompt engineering & loop engineering, clearly explained!](https://godofgpt.com/entry/c354ef57/) ⭐3 · 2026-07-04 — At its core, an agent is a while loop: ReAct described this form of loop back in 2022-23, and almost every agent/framework runs a similar im...
- [Loop Engineering 这个词最近火起来了，但它真正重要的地方不是 cronworktree并行开几个 agent 这些技巧](https://godofgpt.com/entry/3b14fe3e/) ⭐3 · 2026-07-04 — 这些东西有用，但只是实现层 更本质的变化是：我们正在把 AI Manager 做的二阶管理动作写进系统 以前你用 AI，核心动作是自己拆任务补背景看中间结果判断下一步现代 coding agent 已经能自己写代码运行验证看报错debug真正卡住人的地方...
- [AI半导体终局推演2026(II)](https://godofgpt.com/entry/4f3a21e4/) ⭐3 · 2026-07-04 — 当半导体结构性演进到AI推理主线，内存和存储成为了最大瓶颈，市场对内存和存储最大的怀疑就是： HBM/DRAM/SSD会不会摆脱传统周期性？
- [What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in...](https://arxiv.org/abs/2607.02507) ⭐4 · 2026-07-03 — 无显式目标下多 Agent 公开与 OTR 表达发散 ~40%，提示 Agent 评估需要补一块涌现目标检测
- [UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development](https://arxiv.org/abs/2607.02186) ⭐4 · 2026-07-03 — 软件开发需要多角色 Agent 协作，现有 LLM 多 Agent 框架（ChatDev 等）默认中间结果同等可信，但实际上不同角色产出可靠性差异很大。

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 227 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 117 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 73 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 18 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 44 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 31 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 139 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1125
- 公开展示卡片: 649
- 有全文内容: 571
- 最近 7 天信号: 60
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
