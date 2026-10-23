# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Claude Duet: proactive agent research preview powered by Opus 5.5](https://claude.com/product/claude-duet) ⭐4 · 2026-10-23 — Claude Duet 研究预览：早晨简报加消息派活，云端自己持续干活，敏感操作先审批，Opus 5.5 驱动
- [智能体手机加速爆发？换机困境端侧AI与下一代入口之争](https://mp.weixin.qq.com/s?__biz=MzA4NjUwNTI0OA%3D%3D&mid=2247500542&idx=1&sn=e8e3fde608787b50549a4985e457c186) ⭐3 · 2026-10-22 — 换机周期 4348 个月才是厂商押注智能体手机的真正推力，Agent 是下一轮换机的新故事
- [md2wechat: 面向 AI Agent 的公众号创作发布 CLI（BSL 1.1 许可）](https://github.com/geekjourneyx/md2wechat-skill) ⭐3 · 2026-10-22 — 副作用必须显式加参数的 Agent CLI 接口设计值得抄，但 BSL 1.1 是源码可用不是开源
- [What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion](https://arxiv.org/abs/2610.30026) ⭐5 · 2026-10-21 — 企业 Agent 的可靠性输在文档摄取层：主流转换器全都丢掉高亮与颜色线索，需求识别 F1 从 0.690 跌到 0.150
- [PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet](https://www.wiz.io/blog/php2shell-php-rce) ⭐5 · 2026-10-21 — Wiz 披露 PHP2Shell：存在几十年的内存缺陷被前沿 AI 数小时内变成可用 exploit，CVSS 9.2 影响大半个互联网
- [Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor) ⭐5 · 2026-10-21 — LiteLLM 1.107.0 在 PyPI 被投毒：一行 maturin 配置带进窃密器与后门，任意 Python 进程启动即触发外传
- [Widespread PHP Flaw May Cause Many Site Outages Today](https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today) ⭐4 · 2026-10-21 — 潜伏几十年的 PHP RCE 把欧洲政府网站打到主动下线，前沿 AI 把 exploit 开发门槛显著拉低
- [Pluralistic: Adversarial interoperability is a team sport](https://pluralistic.net/2026/10/21/brittle-individualism) ⭐4 · 2026-10-21 — vibe coding 站进了 Canonical 当年的位置：LLM 把对抗性互操作从极客技能变成团队运动
- [VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage](https://arxiv.org/abs/2610.30090) ⭐4 · 2026-10-21 — 类型化决策头做边界 triage：CPU 毫秒级能抓全新攻击族，但时间漂移下所有方法校准崩塌（ECE 0.04 到 0.40）
- [ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination](https://arxiv.org/abs/2610.29934) ⭐4 · 2026-10-21 — ToM2Vec 用连续推理 token 在隐空间做心智理论，五个多智能体环境稳定涨分，还能泛化到没见过的对手模型族

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 428 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 577 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 306 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 178 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 217 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 133 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2856
- 公开展示卡片: 2128
- 有全文内容: 2011
- 最近 7 天信号: 107
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `agents`, `coding-agents`, `agent-memory`, `coding-agent`, `agent-harness`, `safety`, `kv-cache`, `prompt-injection`, `agent-safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
