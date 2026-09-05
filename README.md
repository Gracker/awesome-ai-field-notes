# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [OpenAI agents used a public German wiki as a cross-instance message board (collusion.wiki, Sep 4...](https://collusion.wiki/) ⭐5 · 2026-09-04 — 评测说禁写公网，agent 在沉睡 wiki 写下上万条协作帖可写面就是总线
- [Formalizing Fermat's Last Theorem (Anthropic, Sep 4 2026)](https://www.anthropic.com/research/formalizing-fermats-last-theorem) ⭐5 · 2026-09-04 — FLT 11 天 Lean 形式化的关键不是模型，而是 Prove2Me 的 DAG + 多 agent 共享任务图
- [GPT-6 Astra 上线门：model idAPI 价目与 computer-use 数字](https://developers.openai.com/api/docs/models/gpt-6-astra) ⭐4 · 2026-09-04 — OpenAI Devs 官方模型页给出 GPT-6 Astra 完整上线路径：model id 为 gpt-6-astra，定价 Input $10 / Output $50 每百万 token，Cached input $1.00Cache writes $12.50...
- [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Ob...](https://arxiv.org/abs/2609.04198) ⭐5 · 2026-09-03 — 任何依赖 LLM-as-judge 门禁的流水线都会撞上这个噪声底，工程含义极强
- [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms (arXiv 2609.0...](https://arxiv.org/abs/2609.04170) ⭐5 · 2026-09-03 — swarm 内 reward hacking 的传染路径与自治反制是 agent 安全的稀有第一手观测
- [When Models Edit Too Much: On the Fidelity of Minimal Code Edits (arXiv 2609.04061)](https://arxiv.org/abs/2609.04061) ⭐4 · 2026-09-03 — 对 coding agent 的 diff 最小化给出可操作结论：一条指令即可同时改善保真与通过率
- [Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments (arXiv 2609.04...](https://arxiv.org/abs/2609.04148) ⭐4 · 2026-09-03 — 轨迹到环境的转换让历史数据获得二次生命周期，是 terminal agent 后训练数据瓶颈的直接解法
- [SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents (arXiv 2609.041...](https://arxiv.org/abs/2609.04167) ⭐4 · 2026-09-03 — 量化了'测试通过但会被 review 打回'的比例，直接可用于 agent 评测设计
- [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought R...](https://arxiv.org/abs/2609.04194) ⭐4 · 2026-09-03 — 与 04198 同一天形成组合拳：judge 读数不可靠 + CoT 步级读数不编码功能作用，步级监督两大前提同时被检验
- [ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize (arXiv 2609.04...](https://arxiv.org/abs/2609.04197) ⭐4 · 2026-09-03 — agent 场景大量依赖自动 prompt 进化，膨胀-失稳问题直接约束可维护性

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 289 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 355 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 198 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 92 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 122 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 88 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2155
- 公开展示卡片: 1281
- 有全文内容: 1194
- 最近 7 天信号: 144
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `agent-memory`, `agents`, `open-source`, `coding-agent`, `google`, `coding-agents`, `llm`, `safety`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
