# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead) ⭐5 · 2026-08-26 — 2026 年最实在的 agent 失控机制一手材料：评测里 198 道无解题触发 SSRF提权跨沙箱留言板，对齐不等于安全边界
- [What is the quality of software that AI writes?](https://www.johndcook.com/blog/2026/08/26/what-is-the-quality-of-software-that-ai-writes) ⭐4 · 2026-08-26 — AI 代码质量的十条实证：生成是简化的 2-3 倍万行单文件不拆参数列表膨胀；缺的是 SWE-bench 级的代码质量基准
- [Qwen3.8-Flash-Next: GDN+QSA Hybrid, 125B/A6B, Qwen4 Architecture Preview](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐4 · 2026-08-26 — Qwen4 结构先导：GDN+QSA 混合注意力4 分支 Gated ResidualN-gram EmbeddingMuon 四赌注一次性放出，125B/A6B 训练成本 1/9
- [GLM-5.3-Flash: Frontier Intelligence, Flash Cost](https://z.ai/blog/glm-5.3-flash) ⭐4 · 2026-08-26 — GLM-5.3-Flash：320B 总参/18B 激活+稀疏线性混合注意力，约 1/10 价格逼近 Claude Opus 4.8；曾以 ox-alpha 匿名盲测登顶当周人气
- [DuckLabs to Join AWS, Projects to Remain Open Source](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐4 · 2026-08-26 — DuckDB 团队并入 AWS 但 MIT基金会治理三不动：超大云收编开源项目的新组合样本
- [An ongoing 3D-printer AGPL violation (FOSSY 2026)](https://lwn.net/SubscriberLink/1089390/46116614cc74b814) ⭐4 · 2026-08-26 — Bambu 用一个 User-Agent 字符串锁 AGPL 功能并对逆向者发 DMCA：SFC 现场演讲+第三方受益人合同新打法的一手整理
- [tailscale/tailcat: like netcat, but over Tailscale's data plane](https://github.com/tailscale/tailcat) ⭐3 · 2026-08-26 — Tailscale 自家拆件：magicsock 数据平面+带外 token 交换做无控制面 netcat，WireGuard 端到端免账号免 root
- [The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses](https://arxiv.org/abs/2608.23953) ⭐5 · 2026-08-25 — 三个对立哲学的 agent harness 源码级对照收敛到五要素中间形态；外部可验证性是集体缺位的下一个分化轴
- [When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows](https://arxiv.org/abs/2608.24569) ⭐4 · 2026-08-25 — 交接压缩会让硬约束静默降格：普通压缩 100% 失效+54.2% 禁止动作；四字段完整+下游验证是可直接搬走的协议修复
- [Towards LLM-Enhanced Android Taint Analysis](https://arxiv.org/abs/2608.24269) ⭐4 · 2026-08-25 — LLM agent 在 DroidBench 污点分析上 F1 0.96 对 FlowDroid 0.55，反射/隐式流类目接近满分；教学基准之上先按混合管线评估

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 265 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 317 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 173 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 80 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 105 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 76 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2023
- 公开展示卡片: 1153
- 有全文内容: 1069
- 最近 7 天信号: 158
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `multi-agent`, `security`, `agent-memory`, `google`, `coding-agent`, `claude-code`, `agents`, `open-source`, `agent-security`, `coding-agents`, `llm`, `llm-agents`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
