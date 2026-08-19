# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Two-Factor Authentication Across Package Registries](https://nesbitt.io/2026/08/18/two-factor-authentication-across-package-registries.html) ⭐5 · 2026-08-18 — 供应链 2FA 的分水岭不在口号，在 registry 账户身份这一层
- [Cumora: 开源人机同群 team chat，协调硬门可审计](https://github.com/yetone/cumora) ⭐5 · 2026-08-17 — 多 agent 同房的胜负手在 HELD/去重/并发 cap 这些代码门，不在人设 prompt
- [Help peer](https://seangoedecke.com/help-peer) ⭐5 · 2026-08-17 — 多 agent 协作的真实形状是工具性互惠，不是默认合作
- [Claude Code v2.1.234: usage-limit auto-continue + context diet](https://github.com/anthropics/claude-code/releases/tag/v2.1.234) ⭐4 · 2026-08-17 — 额度重置自动续跑是状态机补一格，不是上下文管理豁免
- [手写 200 行 agent loop：区分玩 AI与懂 Agent的分界线](https://x.com/Ryrenz/status/2089188971720896902) ⭐4 · 2026-08-17 — 判断有没有懂 agent，看能不能手写出带停机与工具门的 200 行 loop
- [Models Are Getting Dumber on Purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐4 · 2026-08-17 — 反共识归因：事实层正被设计成可选件训练贵迭代慢的知识让位给检索，小模型负责推理
- [AI Alignment as a Thought-Terminating Cliche](https://borretti.me/article/ai-alignment-as-thought-terminating-cliche) ⭐4 · 2026-08-17 — aligned ASI是能证明任何结论的不透明前提，不是技术路线
- [What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models](https://arxiv.org/abs/2608.16852) ⭐4 · 2026-08-17 — 合规检测器'规则盲视'审计：换掉规则判定不变，只有逐步推理能逃出该失效
- [VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience](https://arxiv.org/abs/2608.16544) ⭐4 · 2026-08-17 — 技能自演化新先验：蒸馏公开技能版本变更史，均值提升 3.2-5.0 分且跨模型迁移更强
- [Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning](https://arxiv.org/abs/2608.16831) ⭐4 · 2026-08-17 — 策略迭代+人类反馈：迭代版本化自然语言策略，GPT-5.4 罕见病 Recall@1 提升 32.7 个百分点

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 287 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 268 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 142 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 62 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 79 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 62 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1874
- 公开展示卡片: 1038
- 有全文内容: 950
- 最近 7 天信号: 123
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `arxiv`, `benchmark`, `research`, `evaluation`, `openai`, `anthropic`, `attention`, `google`, `multi-agent`, `security`, `coding-agent`, `claude-code`, `agent-memory`, `agent-security`, `coding-agents`, `optimization`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
