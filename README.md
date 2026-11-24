# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [The AI Code Review Report 2026: review capacity is the delivery bottleneck (LeadDev x CodeRabbit...](https://leaddev.com/the-ai-code-review-report-2026) ⭐3 · 2026-11-24 — LeadDev 调查：45% 把 code review 容量当最大拖累，七成合并过没读懂的 AI 代码
- [Codex CLI 0.172.0: exec resume keeps sandbox permissions, slash Tab completion, task-group navig...](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐3 · 2026-11-24 — Codex 0.172.0：exec resume 保住沙箱权限，slash 参数 Tab 补全
- [把 Fable 5.2 挂成 Claude Code 的顾问模型，周限额面板不动这件事被实测过](https://x.com/mylifcc/status/2124669510430974129) ⭐4 · 2026-11-23 — Fable 顾问换掉的是计数器不是预算：面板截图证明不了额度去向，看 API 记录才算数
- [Notes on OpenAI's perplexity reveal](https://seangoedecke.com/notes-on-openais-perplexity-reveal) ⭐4 · 2026-11-23 — 首次可查的前沿预训练对比数据，但曲线看不到 RL 那一半，别把困惑度直接读成能力排名
- [Here's Why Data Breach Disclosure is so Hard: Lessons from Hundreds of Emails with Hacked Compan...](https://www.troyhunt.com/heres-why-data-breach-disclosure-is-so-hard-lessons-from-hundreds-of-emails-with-hacked-companies) ⭐4 · 2026-11-23 — 泄露披露难不在技术而在组织剧本；把八年通知信交给 Claude 提模式这个方法本身值得抄走
- [GLM-5.4: Toward Generalized Coding with Our First Loop Transformer](https://z.ai/blog/glm-5.4) ⭐4 · 2026-11-23 — GLM-5.4：28 层权重共享跑两轮的 Loop Transformer，750B 规模对标 2T-3T 模型
- [When in doubt, flail about](https://seangoedecke.com/when-in-doubt-flail-about) ⭐3 · 2026-11-23 — 缺信息时乱试是对的，但安全绳是反馈敏感度不是乱试本身
- [Claude Code v2.1.331: cloud-terminal Code Mode, MCP hang fix, doctor API checks](https://github.com/anthropics/claude-code/releases/tag/v2.1.331) ⭐3 · 2026-11-23 — Claude Code v2.1.331：云端终端 Code Mode，修 MCP 畸形回复挂 30 分钟
- [To code well, avoid blunders](https://seangoedecke.com/to-code-well-avoid-blunders) ⭐4 · 2026-11-22 — 编码 agent 的短板是顺手加需求：审阅清单应问新增了什么要求而不是逐行找 bug
- [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence) ⭐4 · 2026-11-22 — OpenAI 公布内部困惑度标尺：GPT-3.5 0.99GPT-4 0.910.8 以下涌现网安数学能力，主张行业共享 pacing 指标

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 587 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 765 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 423 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 247 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 303 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 155 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3500
- 公开展示卡片: 2724
- 有全文内容: 2602
- 最近 7 天信号: 147
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `agents`, `anthropic`, `multi-agent`, `coding-agents`, `agent-security`, `security`, `agent-memory`, `kv-cache`, `mcp`, `coding-agent`, `codex`, `open-weights`, `agent-safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
