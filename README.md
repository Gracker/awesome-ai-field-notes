# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Apple Intelligence may become mandatory in iOS and macOS 27](https://manualdousuario.net/en/apple-intelligence-mandatory-ios-macos-27) ⭐4 · 2026-10-09 — iOS/macOS 27 起 Apple Intelligence 无法整体关闭：35GB 占用逐项开关HN 770+ 分热议
- [Launching an opt-in vulnerability-finding service for open-source software](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source) ⭐5 · 2026-10-08 — OSS Scanner：模型直出无人工预审的免费开源扫洞，29k 候选漏洞抽检 88% 达 CVD 标准
- [From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Age...](https://arxiv.org/abs/2610.12463) ⭐5 · 2026-10-08 — 2026 年三大实验室的 agent 安全评估事故复盘
- [Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff](https://arxiv.org/abs/2610.12436) ⭐5 · 2026-10-08 — 生态学视角看失控风险：协作创造种群数量阈值
- [Ultrafast mode](https://developers.openai.com/api/docs/guides/ultrafast-mode) ⭐4 · 2026-10-08 — Ultrafast mode 文档落地：service_tier 一行开关，6 倍价买 token 间隔，agent 循环官方建议 WebSocket
- [OpenAI, the Partition Principle, and Mathematics](https://karagila.org/2026/openai-pp) ⭐4 · 2026-10-08 — 集合论学者评 OpenAI 分离原理预印本：desk rejection 水平，宣称即 DoS
- [Introducing the Anthropic Cyber Mission](https://www.anthropic.com/news/anthropic-cyber-mission) ⭐4 · 2026-10-08 — Anthropic Cyber Mission 启动：CIDP 11 家伙伴守 OT 关基，OSS Scanner 免费扫开源找洞
- [Searching for "Harmful Refusal": A Psychometric Audit of an AI Safety Benchmark](https://arxiv.org/abs/2610.12409) ⭐4 · 2026-10-08 — 有害拒答作为可测属性成立吗：HELM Safety 心理测量审计
- [Predicting Alignment Generalization with Value Representations](https://arxiv.org/abs/2610.12410) ⭐4 · 2026-10-08 — 用激活值表征预测对齐泛化：相关性 0.45 对 0.05
- [On the estimation and validity of AI time horizons---a statistical look at the METR plot](https://arxiv.org/abs/2610.12466) ⭐4 · 2026-10-08 — 用 METR 数据重算 50% 时间视野：样条 + 项目反应理论

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 391 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 538 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 272 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 163 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 193 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 120 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2692
- 公开展示卡片: 1966
- 有全文内容: 1864
- 最近 7 天信号: 155
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `agents`, `security`, `coding-agent`, `coding-agents`, `agent-memory`, `mcp`, `agent-harness`, `kv-cache`, `safety`, `open-source`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
