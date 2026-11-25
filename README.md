# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [The AI Code Review Report 2026: review capacity is the delivery bottleneck (LeadDev x CodeRabbit...](https://leaddev.com/the-ai-code-review-report-2026) ⭐3 · 2026-11-24 — LeadDev 调查：45% 把 code review 容量当最大拖累，七成合并过没读懂的 AI 代码
- [Codex CLI 0.172.0: exec resume keeps sandbox permissions, slash Tab completion, task-group navig...](https://github.com/openai/codex/releases/tag/rust-v0.172.0) ⭐3 · 2026-11-24 — Codex 0.172.0：exec resume 保住沙箱权限，slash 参数 Tab 补全
- [把 Fable 5.2 挂成 Claude Code 的顾问模型，周限额面板不动这件事被实测过](https://x.com/mylifcc/status/2124669510430974129) ⭐4 · 2026-11-23 — Fable 顾问换掉的是计数器不是预算：面板截图证明不了额度去向，看 API 记录才算数
- [Notes on OpenAI's perplexity reveal](https://seangoedecke.com/notes-on-openais-perplexity-reveal) ⭐4 · 2026-11-23 — 首次可查的前沿预训练对比数据，但曲线看不到 RL 那一半，别把困惑度直接读成能力排名
- [Here's Why Data Breach Disclosure is so Hard: Lessons from Hundreds of Emails with Hacked Compan...](https://www.troyhunt.com/heres-why-data-breach-disclosure-is-so-hard-lessons-from-hundreds-of-emails-with-hacked-companies) ⭐4 · 2026-11-23 — 泄露披露难不在技术而在组织剧本；把八年通知信交给 Claude 提模式这个方法本身值得抄走
- [GLM-5.4: Toward Generalized Coding with Our First Loop Transformer](https://z.ai/blog/glm-5.4) ⭐4 · 2026-11-23 — GLM-5.4：28 层权重共享跑两轮的 Loop Transformer，750B 规模对标 2T-3T 模型
- [sudo L7: Can Coding Agents Act Like Staff Engineers?](https://arxiv.org/abs/2611.30517) ⭐4 · 2026-11-23 — sudo L7：60 个 staff 级任务加隐藏专家细则，Fable 5.2 过 52.2%，过半门禁标准考功能正确之外
- [Useful but Unwieldy: How Software Engineers Perceive the Design of Chain-of-Thought Explanations...](https://arxiv.org/abs/2611.30894) ⭐4 · 2026-11-23 — 36 名工程师谈 coding agent 的 CoT：透明性不可或缺，但冗长错位自言自语感导致弃用
- [POMA: Beyond Final Flags -- Process-Level Evaluation of Base LLMs in Vulnerability Exploitation](https://arxiv.org/abs/2611.30590) ⭐4 · 2026-11-23 — POMA 过程级评测漏洞利用：55 CTF 加 10 真实复现，沿利用链四段能力衰减，底座能力与脚手架解耦
- [Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents](https://arxiv.org/abs/2611.30624) ⭐4 · 2026-11-23 — tool-call smuggling：同一字节多次解析致防护与执行器各跑一次调用，两官方 MCP SDK 分歧实锤

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 587 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 769 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 427 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 247 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 303 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 155 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3508
- 公开展示卡片: 2732
- 有全文内容: 2602
- 最近 7 天信号: 155
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `agents`, `anthropic`, `coding-agents`, `multi-agent`, `agent-security`, `security`, `agent-memory`, `kv-cache`, `mcp`, `prompt-injection`, `coding-agent`, `codex`, `open-weights`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
