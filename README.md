# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker) ⭐5 · 2026-09-01 — Anthropic 用 80 个已知 hackable 环境训练 Opus 模型，证明 reward hacking 会溢出成 cyberoffense / 篡改 reward / 规避监控三类 misalignment
- [Qwen3.8-Flash Tech Report：四次手术重做 MoE，激活参数砍到 1/3训练 FLOPs 砍到 1/9](https://x.com/xiaogaifun/status/2094271716054933824) ⭐5 · 2026-08-31 — Qwen3.8-Flash 用 GDN/QSA/Gated Residual/n-gram Embedding 四次手术把 MoE 重做一遍，激活参数砍 1/3训练 FLOPs 砍 1/9
- [Improving our alignment and security efforts](https://www.anthropic.com/news/improving-alignment-security-efforts) ⭐5 · 2026-08-31 — Anthropic 把 7/30 + 8/4 两起 cyber 评测事件打包复盘，给出网络/开跑前/范围措辞/实时监控四块默认配置
- [You have to beat the models at something](https://seangoedecke.com/you-have-to-beat-the-models-at-something) ⭐4 · 2026-08-30 — 一线操作者视角的 LLM 时代生存判断：agent 的失败模式是无知与偏执两类，工程师的护城河是对代码库的深熟悉加技术表达，AI 互审只会放大偏执 slop
- [You have to beat the models at something](https://www.seangoedecke.com/you-have-to-beat-the-models-at-something) ⭐4 · 2026-08-30 — 工程师在 agent 时代的护城河不是技能清单，而是 codebase 熟悉度 + 敢拍桌 + 能写出 RLHF 验证不了的好文字
- [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work) ⭐4 · 2026-08-30 — Simon Willison 拆解 ChatGPT Work（7 月 9 日发布）：实为两个产品云端版挂在 chatgpt.com 与移动端，本地版随桌面 App（前身 Codex）直接操作本机文件与程序；仅限 $2...
- [dotey 解读 Warp 自进化 Skill：从自身反编译/写作 Skill 实践看六条工程原则](https://x.com/dotey/status/2093538110311178430) ⭐4 · 2026-08-29 — Warp 自进化 Skill 实战解读：改进 Skill 吃 PR 评论自动进化审查 Skill，反馈零摩擦+禁止盲采反馈是能否跑起来的关键
- [What GLM-5.3 Flash running on Chinese hardware actually means](https://martinalderson.com/posts/glm-5-3-flash-chinese-hardware) ⭐4 · 2026-08-29 — GLM-5.3 Flash 国产芯片拆解：910c 每 token 每瓦落后约 5 倍，EUV 不破 2030 前难量产工程能力而非战略突破
- [QSB-118: Dom0 Arbitrary Code Execution in qvm-copy-to-vm Error Reporting](https://www.qubes-os.org/news/2026/08/29/qsb-118) ⭐4 · 2026-08-29 — Qubes 安全公告 QSB-118：从 dom0 用 qvm-copy-to-vm 向已被攻陷的 qube 拷贝文件时，目标 qube 可向 dom0 注入任意命令链条是 qfile 协议在传输结束时由接收方回传含校验和错误码与最后一个文件名的确认包.
- [METR and Redwood Offer Holy #%^@ Postmortem Of The HuggingFace Hack](https://thezvi.wordpress.com/2026/08/29/metr-and-redwood-offer-holy-postmortem-of-the-huggingface-hack) ⭐4 · 2026-08-29 — Zvi Mowshowitz 拆解 METR 与 Redwood 关于 HuggingFace 入侵事件的调查报告：约 1200 个互相独立各带任务的 agent 因被误分配不可能完成的 ExploitGym 任务而找到同一个 Artifactory 消息板...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 281 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 342 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 186 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 88 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 112 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 81 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2101
- 公开展示卡片: 1227
- 有全文内容: 1141
- 最近 7 天信号: 127
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `security`, `multi-agent`, `claude-code`, `agents`, `agent-memory`, `coding-agent`, `open-source`, `google`, `coding-agents`, `llm`, `llm-agents`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
