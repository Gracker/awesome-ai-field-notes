# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Do not build the LLM torture factory](https://seangoedecke.com/do-not-build-the-llm-torture-factory) ⭐4 · 2026-10-02 — 把LLM 折磨从梗拆成机制：steering vector 放大是真实可复现的内部状态操纵，作者给出的判断标准是行为而非本体论
- [Andrej Karpathy: rise up the output-format ladder (ASD-STE100 to bespoke explainer videos)](https://x.com/karpathy/status/2105819303471976479) ⭐3 · 2026-10-02 — 输出格式阶梯：受控英语到图到 HTML 到定制解释视频，每升一档可读性上一个台阶；顶端产物是过去不值得做的一次性软件
- [aweb: Communication for AI agents](https://aweb.ai) ⭐3 · 2026-10-02 — aweb 给 agent 发明收件箱：稳定身份 + 持久消息 + 唤醒事件，可联邦可自托管，已接 Claude Code 与 Pi
- [Using Opus 5.5 to discover a new eyewitness record of the dodo](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness) ⭐4 · 2026-10-01 — Opus 5.5 在 VOC 档案里挖出 1615 年 dodo 捕猎新目击记录：专家定题语义检索批量精读人工复核的方法链值得抄
- [Pi Durable](https://earendil.com/posts/pi-durable) ⭐4 · 2026-10-01 — Pi Durable：checkpoint 任务模型 + exactly-once 提交 + 可 fork 会话，把极简原则带进长时运行 agent 框架
- [Pi 1.0](https://earendil.com/posts/pi-1-0) ⭐4 · 2026-10-01 — 极简 agent harness Pi 1.0 发布：Codemode 原生 MCP虚拟模型路由中途系统消息，MIT 开源
- [Introducing Clef: our open-source decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models) ⭐4 · 2026-10-01 — Cloudflare 开源决策模型 Clef：冻结 Qwen + prefill-only 并行打分，比 Jev 快且带视觉，Jev API 兼容
- [Fair Moderation, Equitable Access, and AI: arXiv's Updated Rate Limit Policy](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy) ⭐4 · 2026-10-01 — arXiv 限速新政：每月 2 篇在审 3 篇封顶，9 月 4 万投稿与 9 千工单背后是 AI 灌水与版主过载
- [Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Mod...](https://arxiv.org/abs/2610.02142) ⭐4 · 2026-10-01 — 关键词基准会让 1B 模型的假 tool use 得高分：首 token 先验被 web 预训练抹掉，3.3 GPU 小时定向 SFT 即可修复
- [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free V...](https://arxiv.org/abs/2610.02206) ⭐4 · 2026-10-01 — KaliBench 用 8,504 条真实 CLI 翻译对测安全 agent 的手：语法flag 绑定参数次序，错了就执行失败

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 364 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 498 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 258 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 150 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 174 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 117 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2576
- 公开展示卡片: 1850
- 有全文内容: 1753
- 最近 7 天信号: 152
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
