# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [An open letter for a global surge in cyber defense](https://x.com/gdb/status/2093021551855812842) ⭐5 · 2026-08-27 — 100+ 家 AI 厂商与云厂商联名承认攻击窗口已开：防御方第一次由能力方自己按铃，含金量在签名名单而不在信本身
- [Why do OpenAI's GPT-2 weights beat mine? Part four: digging into dropout](https://www.gilesthomas.com/2026/08/why-do-openai-gpt2-weights-beat-mine-4-ift-dropout) ⭐4 · 2026-08-27 — IFT 显著劣化的一个隐藏旋钮找到了：预训练没 dropout 的权重在 fine-tune 强开 dropout 会崩（21.55.3），配方可迁移
- [US judge blocks Pentagon's Anthropic blacklisting](https://www.reuters.com/legal/government/us-judge-blocks-pentagons-anthropic-blacklisting-2026-08-28) ⭐4 · 2026-08-27 — 空洞援引国家安全不是空白支票：AI 厂商拒绝军用化的合同边界第一次拿到司法背书，行业政策面里程碑
- [Sandboxing coding agents](https://micahflee.com/sandboxing-coding-agents) ⭐4 · 2026-08-27 — agent 沙箱的最小可行实现：专用 signing key + 隔离 ssh-agent + sbx，能签 commit 却碰不到你其余仓库
- [Breaking Claude Code Opus 5 Auto Mode](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode) ⭐4 · 2026-08-27 — auto mode 被 80% 命中率打穿还拦下自救命令：分类器防御的天花板就在这，沙箱+最小权限才是底线配置
- [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/abs/2608.27454) ⭐4 · 2026-08-27 — WikiSkill：技能演化配持久知识库，小模型带技能可反超更大裸模型，技能跨模型家族可迁移
- [SWE-Prime: Fewer Trajectories, Better Performance](https://arxiv.org/abs/2608.27449) ⭐4 · 2026-08-27 — SWE-Prime：两段式轨迹+语义段筛选，10% 成功轨迹子集 SFT 反超全量数据，SWE-Bench Verified 相对增益 24.2%
- [RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution](https://arxiv.org/abs/2608.27439) ⭐4 · 2026-08-27 — RedEvoAgent：把攻击轨迹蒸馏成可读攻击技能的黑盒红队智能体，验证棘轮只留有效更新，可跨执行环境迁移
- [Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Au...](https://arxiv.org/abs/2608.27427) ⭐4 · 2026-08-27 — PES 架构模式：人格域与执行域分离+契约桥，让智能体人格自由漂移而执行保持被审计；附数字员工平台案例
- [GLM-5.3 is now open-weight](https://huggingface.co/zai-org/GLM-5.3) ⭐4 · 2026-08-27 — GLM-5.3 开放权重：同底座纯后训练，编程大幅提升，官方明示涌现网络攻防能力（ExploitBench 翻倍）

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 269 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 324 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 178 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 81 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 108 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 80 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2047
- 公开展示卡片: 1177
- 有全文内容: 1084
- 最近 7 天信号: 176
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `multi-agent`, `agents`, `security`, `agent-memory`, `claude-code`, `google`, `coding-agent`, `agent-security`, `open-source`, `coding-agents`, `llm`, `llm-agents`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
