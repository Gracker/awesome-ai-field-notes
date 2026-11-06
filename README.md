# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Pluralistic: Without CDA 230, Facebook will own the internet forever](https://pluralistic.net/2026/11/05/see-you-in-court) ⭐4 · 2026-11-05 — 反直觉但论证扎实：废 230 利好 Meta 不利好用户；禁抓取与AI 审核两个议程都被点名为大科技的护城河
- [Jepsen: ParticleDB 1.1.4](https://jepsen.io/analyses/particledb-1.1.4) ⭐4 · 2026-11-05 — Jepsen 把LLM 写的数据库钉在案板上：产出速度换来解释并修掉问题能力的退化，而文档这个替代品也由模型生成
- [Claude Code sends your email address to websites via User-Agent header](https://github.com/anthropics/claude-code/issues/107757) ⭐4 · 2026-11-05 — 一份针对 claude-code v2.
- [A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root) ⭐5 · 2026-11-04 — 948 个 LPE约 $1,279/个的单价表把 agent 攻防从演示推进到流水线经济学；低权限root是未打补丁系统的新默认假设
- [Pluralistic: The AI fatfinger economy has come for my receipts app](https://pluralistic.net/2026/11/04/genius-scan-is-neither) ⭐4 · 2026-11-04 — KPI 变成目标函数后，员工和模型一样学会 reward hacking：Doctorow 给每个按钮都换成 AI的 UI 现象起了名字
- [OpenAI to acquire Pierre Computer Company, Inc.](https://openai.com/index/openai-to-acquire-pierre) ⭐4 · 2026-11-04 — 收购 Pierre 加自研 Pando 组成 agent 时代源码平面的一套动作：审阅层与存储层都收进 Codex 版图，开源承诺待观察
- [Background subagents in Claude Code now use less of your usage limit](https://x.com/ClaudeDevs/status/2118063143167693011) ⭐4 · 2026-11-04 — 心跳路径换小模型是账单小幅改善而非砍 99% 会话开销；HN 16.4% 与官方 26% 是不同总体，两边都要看
- [SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative V...](https://arxiv.org/abs/2611.06876) ⭐4 · 2026-11-04 — 针对智能体上下文压缩的时延问题：用大模型摘要长交互历史会引入明显延迟，信息保留与延迟需要权衡SpecCompact 基于结构化摘要槽位可独立生成且不丢信息的观察，用槽位并行语义推测加速压缩微调小模型起草器并行生成槽位，目标模型逐行验证并修复被拒内容，后续起草使用更新后的槽位前缀.
- [ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841) ⭐4 · 2026-11-04 — ServerBench 让编码智能体为自身运行设计完整的专用 LLM serving 系统，统一目标为dollars per dollar：每美元 GPU 成本产出的达时延门槛 token 价值.
- [On Turn-Level Best-of-N Sampling for Scaling LLM Agents](https://arxiv.org/abs/2611.06868) ⭐4 · 2026-11-04 — 在长程智能体任务上评估回合级 best-of-N 采样这一简单的推理时扩展方法：每回合由生成器模型给出 N 个候选动作，选择器模型挑一个交给环境执行...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 485 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 660 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 335 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 205 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 253 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 140 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3097
- 公开展示卡片: 2323
- 有全文内容: 2200
- 最近 7 天信号: 154
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `coding-agents`, `security`, `agents`, `agent-memory`, `agent-harness`, `coding-agent`, `open-weights`, `prompt-injection`, `safety`, `agent-safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
