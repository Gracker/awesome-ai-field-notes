# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Claude Code Projects: coordinator goes proactive across parallel threads](https://x.com/ClaudeDevs/status/2121375309287301360) ⭐4 · 2026-11-15 — Anthropic 大改 Claude Code 的 Projects：项目内由协调器跨并行线程调度任务，协调器更主动在项目聊天里答问主动汇报各线程状态（官帖 18k likes）核对口径：/btw 开旁路提问/fork 分支线程...
- [Terminal-Bench 4.1: verifier hardening against reward hacking, $0 artifact regrade](https://www.tbench.ai/news/terminal-bench-4-1) ⭐4 · 2026-11-14 — 基准方防 reward hacking 的可抄作业：Worker 隔离加产物消毒加存工件 0 成本重评
- [Artificial Analysis Coding Agent Index v2.1: three-way tie at 58, 30x per-task cost spread](https://artificialanalysis.ai/agents/coding-agents) ⭐4 · 2026-11-14 — 读榜纪律：测的是模型+harness+effort 组合，榜首并列 58 但单任务成本差 30 倍，先看 Pareto 再看名次
- [Taking AI Seriously](https://borretti.me/article/taking-ai-seriously) ⭐3 · 2026-11-14 — Borretti 11 月 14 日正面处理认真对待 AI到底指什么他把程序员建议的时间线从补全有用但你要懂仓库一路排到cron job 每天把 spec 编译成 x86 汇编，判断这条曲线像正在输掉战争国家的战报.
- [Ops needs friction](https://www.jeffgeerling.com/blog/2026/ops-needs-friction) ⭐3 · 2026-11-14 — Geerling 11 月 14 日从微软连续宕机与 FAA 全国地面停飞讲起：运维思维与开发项目管理思维根本不同，核心是系统出问题时保持镇定，在没准备过的条件下调试别人写的代码案例：某团队为生产环境用真实数据调试长期开 debug 级日志...
- [Of Course People Hate Data Centres](https://hugotunius.se/2026/11/14/of-course-people-hate-data-centres.html) ⭐3 · 2026-11-14 — Tunius 11 月 14 日解释 2026 年最激烈的政治议题为何是钢筋水泥的数据中心：人们恨的其实是 AI 及其鼓吹者，数据中心只是敌意落地最显眼的石头数字很硬：美国中期选举 44 项数据中心投票仅 1 项对开发商有利，出口民调 76% 反对本地建设...
- [How to find meaning in large tech companies](https://seangoedecke.com/how-to-find-meaning-in-large-tech-companies) ⭐3 · 2026-11-14 — 大厂意义的具体化：不辩解不劝退，把修一个 bug 省下的用户月当有量级之事来算
- [The avalanche that hit math is coming for AI development](https://www.dwarkesh.com/p/rsi) ⭐4 · 2026-11-13 — 判断可以改口，但这次给了三个可查锚点：组织内占比人均日花费进展速度翻倍
- [The Hater's Guide to Megaspeed](https://www.wheresyoured.at/hg-megaspeed) ⭐4 · 2026-11-13 — 关键不是八卦是口径：若走私占 Nvidia 年收入两成，出口管制下的需求要重新对账
- [Securing persistent agents like OpenClaw at OpenAI](https://developers.openai.com/blog/securing-persistent-agents-like-openclaw-at-openai) ⭐4 · 2026-11-13 — 500+ 生产持久 agent 的控制面清单：控制面分离schema 化 allowlist凭证代理LLM 二审独立身份

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 533 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 723 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 388 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 231 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 284 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 151 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3329
- 公开展示卡片: 2554
- 有全文内容: 2435
- 最近 7 天信号: 197
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agent-security`, `coding-agents`, `agents`, `security`, `agent-memory`, `coding-agent`, `kv-cache`, `mcp`, `codex`, `open-weights`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
