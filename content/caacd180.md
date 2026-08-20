# TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation

- **ID**: caacd180
- **原文链接**: https://arxiv.org/abs/2608.17588
- **PDF**: https://arxiv.org/pdf/2608.17588
- **作者**: Zhibo Zhang, Zhen Ouyang, Ling Shi, Kailong Wang
- **日期**: 2026-08-18
- **更新**: 2026-08-18
- **分类**: cs.AI, cs.SE
- **来源类型**: arxiv
- **标签**: agent-skills, security, safety, arxiv, paper
- **质量评分**: 4/5
- **抓取时间**: 2026-08-20T15:44:49Z

---

## 中文导读

自动生成 Agent Skill 的难点在于，仅凭产物或最终任务结果无法确定 agent 会执行哪些动作、产生哪些副作用。TRUSS 用证据引导生成：先对照源码与领域证据检查功能声明，按九条预定义安全属性评估完整产物；通过静态门的候选再由受控执行环境中的影子 agent 加载，工具经 broker 暴露给策略执行并记录带溯源的执行轨迹，功能失败与属性违规会回链到责任 Skill 内容驱动迭代修复。在 168 个 SkillInject 产物、155 个 SkillSafetyBench 案例和 187 个 SkillGenBench 任务上评估：漏洞检测精确率与召回率均达 100%；修复使攻击成功率从 38.71% 降至 19.35%（GPT 5.5）、从 46.45% 降至 29.68%（GPT 5.4），零攻击回归；任务有效性从 17.11% 提升到 52.94%。

## 为什么值得关注

证据引导的 Agent Skill 自动生成安全框架：静态门加影子 agent 执行溯源，攻击成功率减半且任务有效性翻三倍

## English Abstract

Agent Skills package reusable natural language procedures with executable resources, enabling software agents to acquire task specific capabilities without model adaptation. Automatically generating such Skills can improve task performance, yet evaluating a candidate solely from its artifact or final task outcome leaves unresolved which actions the equipped agent will perform and which side effects those actions will produce. We present TRUSS, an evidence guided framework for generating functionally effective and safety reliable Agent Skills. TRUSS first inspects functional claims against source and domain evidence while evaluating the complete artifact under nine predefined safety properties. Candidates admitted by this static gate are loaded by a shadow agent inside a Controllable Execution Environment, where brokered tools expose requested actions to policy enforcement and record their results as provenance preserving execution traces. Functional failures and property violations are linked back to the responsible Skill content and used to guide iterative refinement. We evaluate TRUSS on 168 SkillInject artifacts, 155 SkillSafetyBench cases, and all 187 tasks in SkillGenBench. TRUSS achieves 100.00\% precision and recall in vulnerability detection. Repair reduces attack success from 38.71\% to 19.35\% with GPT 5.5 and from 46.45\% to 29.68\% with GPT 5.4, with zero attack regression. For Skill generation, TRUSS raises task effectiveness from 17.11\% without Skills to 52.94\%, while increasing the benchmark Security rate from 50.80\% to 100.00\%. These results show that execution evidence can expose behavioral failures missed by artifact inspection and can guide Skill generation toward jointly verified functional and safety outcomes.

## Obsidian 证据

- 来源 digest: 论文流水线 2026-08-20（评分 8.2）。
- 元数据与摘要经 opencli arxiv paper 核对；中文导读锚定摘要陈述的事实与数字。
