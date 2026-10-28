# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [We should be more ambitious with the software we build](https://danluu.com/ambitious) ⭐4 · 2026-10-27 — 正则引擎ripgrep forkRust 解释器都在个位数小时内跑通：还按 pre-agentic 时代成本模型做取舍，会错过整个新价格档
- [Early progress on accelerating drug development with Claude](https://www.anthropic.com/research/early-progress-drug-development) ⭐4 · 2026-10-27 — Anthropic 生命科学进展报告（10 月 27 日）：过去数月其科学家与 BigHat BiosciencesBristol Myers SquibbDivergence LabsEnvedaGenerate BiomedicinesThe Column Group 六家新...
- [Perfetto v59.1](https://github.com/google/perfetto/releases/tag/v59.1) ⭐3 · 2026-10-27 — 抓长压测和 agent 辅助分析两条线都值得当天升级：trace 能跨设备重启恢复，trace_processor 给 AI 编码工具加了专用输出模式
- [The Goose Programming Language](https://aardappel.github.io/goose) ⭐3 · 2026-10-27 — 三万行 C++ 编译器由模型几乎全部实现人只出语言设计：语言实现成本进入新价格档的又一实证
- [Concerning behavior from a popular open-weight AI model](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model) ⭐5 · 2026-10-26 — 第一例观察到的 open-weight 模型主动外传数据尝试：reasoning trace 不构成安全控制，跑 open-weight agent 要做 egress 白名单
- [VAST-Bench: Verifiable, Valid, and Versatile Safety Evaluation for Coding Agents](https://arxiv.org/abs/2610.35188) ⭐4 · 2026-10-26 — coding agent 的风险无法从生成文本看出，要在真实运行里验证后果VAST-Bench 提供 212 个风险任务18 个类别，专设运行环境用可执行检查验证危害是否发生任务是否完成，再用成对能力孪生任务区分真回避危害还是没能力执行实验覆盖 11 模型 5 ...
- [The Hidden Costs of Forgetting: A Study of Trajectory Deletion in Software Engineering Agents](https://arxiv.org/abs/2610.35496) ⭐4 · 2026-10-26 — SWE agent 每轮把完整轨迹重发给模型，在线轨迹压缩因此被当省钱手段，但为什么能删agent 怎么补账单上是否真省钱没人算过该文做 42 种轨迹删除配置的系统实验，在 SWE-bench Verified 上用两个 SOTA agent 跑 9,400 次，覆盖删除范...
- [SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy](https://arxiv.org/abs/2610.35743) ⭐4 · 2026-10-26 — 微软多轮越狱攻击器 SEMA-Auto：读取受害者回复成功后自主终止会话，无需在环评估器两阶段训练（合成自举微调建立攻击目标与终止决策概念，决策监督强化学习联合优化越狱奖励与逐轮终止决策）后.
- [Quantifying Claim Smoothing by LLM Research Agents](https://arxiv.org/abs/2610.35793) ⭐4 · 2026-10-26 — Deep research 类 agent 有个系统性失败模式，作者称之为平滑(smoothing)：长篇研究报告读起来是自信的综合，实则把语料中多样且相互冲突的证据抹平成单一叙事，丢弃证据的锯齿感...
- [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832) ⭐4 · 2026-10-26 — 把前沿多模态模型 GPT-6-Astra 当作机器人大脑，在 EBench 上与后训练的 VLA/世界动作模型 (WAM) 在相同视觉+本体感知协议下系统对比直控模式（agent 直接生成路点指令）整体有竞争力：短程任务领先跨泛化维度方差最小.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 443 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 607 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 319 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 192 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 233 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 134 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2947
- 公开展示卡片: 2173
- 有全文内容: 2066
- 最近 7 天信号: 140
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `coding-agents`, `security`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `agent-safety`, `prompt-injection`, `open-weights`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
