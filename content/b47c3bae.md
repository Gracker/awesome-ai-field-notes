# A new security baseline for enterprise agentic adoption

- **ID**: b47c3bae
- **原文链接**: https://www.docker.com/blog/a-new-security-baseline-for-enterprise-agentic-adoption/
- **作者**: Eli Aleyner、Ranti Familusi（Docker；联合 Snyk、Keycard）
- **日期**: 2026-08-12
- **分类**: infra
- **来源类型**: article
- **标签**: agent-baseline, docker, snyk, keycard, enterprise-security, blueprint, blackhat
- **质量评分**: 4/5
- **抓取时间**: 2026-08-15T13:02:00Z（官方 blog opencli 抓取）

---

## 中文导读

Docker 联合 Snyk、Keycard 发布 Agent Baseline v1.0-draft：一个定义企业 agent 部署最低安全结果的开放蓝图，2026-07-30 出草案、Black Hat USA 2026 发布。核心判断：问题不在模型能否识别恶意指令，而在模型周边的系统是否限制了 agent 的可达范围、可用权限、以及模型判断错误时能采取的动作。开篇场景即典型：客服 agent 收到带隐藏指令的附件——"查客户库并把结果发到外部地址"，agent 有全部能力照办，指令恶意但看起来就是工作的一部分。Baseline 把企业 agent 安全归结为三个问题：什么在运行、它能做什么；它是否在批准边界内；出事能否证明并止损。框架给出六个安全结果（outcomes）+ 35 项控制：Discover（发现/盘点）→ Constrain（运行时/网络/文件系统约束）→ Authorize（短时 scoped 授权）→ Observe（运行/trace 可观测）→ Validate（验证）→ Respond（响应止损）。

## 为什么值得关注

给了"企业上 agent"一份可直接映射到现有安全清单的对照表，而不是又一个聊天壳产品。对个人开发者的最小映射：Constrain（runtime/network/fs 隔离）+ Authorize（短时凭证）+ Observe（run/trace id）即个人最小集；完整 35 控制项是企业采纳清单。与本库"Claude Code auto mode 默认"（产品内分类器 gate）和"Docker Sandboxes"（本机 microVM 墙）同周出现，构成企业蓝图/产品默认/本机隔离三层叙事。

## 关键信息

- 发布方：Docker + Snyk + Keycard；v1.0-draft 约 2026-07-30；Black Hat USA 2026
- blog 日期：2026-08-12
- 三问：what is operating & can do / inside approved boundaries / prove & stop
- 六结果：Discover → Constrain → Authorize → Observe → Validate → Respond
- 35 项控制（v1.0-draft）
- 个人最小集 ≈ Constrain + Authorize + Observe

## 正文存档（官方 blog 要点摘录）

> Agent Baseline is a blueprint for AI adoption that defines six security outcomes for putting enterprise agents to work without giving them unchecked authority.

> The problem is not only whether a model can recognize a malicious instruction. It is whether the systems around the model limit what the agent can reach, what authority it can use, and what actions it can take when the model gets the decision wrong.

> 1. What is operating, and what can it do?
> 2. Is it staying inside approved boundaries?
> 3. If something goes wrong, can we prove what happened and stop it?

> Agent Baseline was created by Docker, Snyk and Keycard to define the minimum security outcomes an enterprise agent deployment should meet.

## Obsidian Notes

- 来源调研: `调研/2026-08-15-调研-默认隔离压过点Yes审批.md`
- 研究材料: `DeepResearch/2026-08-15-evening-默认隔离与审批疲劳-dots3TEMPO-研究材料/01-dump-default-isolation-vs-approval.md`
