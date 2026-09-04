# Comparing Human Oversight Strategies for Computer-Use Agents (arXiv 2604.04918)

- **ID**: 67fedfa3
- **原文链接**: https://arxiv.org/abs/2604.04918
- **PDF**: https://arxiv.org/pdf/2604.04918
- **作者**: Chaoran Chen, Zhiping Zhang, Zeya Chen, Eryue Xu, Yinuo Yang, Ibrahim Khalilov, Simret A Gebreegziabher, Yanfang Ye, Ziang Xiao, Yaxing Yao, Tianshi Li, Toby Jia-Jun Li
- **日期**: 2026-04-06
- **分类**: agents
- **来源类型**: paper
- **标签**: computer-use, oversight, human-in-the-loop, cua, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-09-04T08:00:00Z

---

## 中文导读

论文把 CUA 监督拆成决策权归属（agent-led vs human-controlled）与人类介入层级（step-level vs plan-level）两个轴，对应 Action Confirmation、Risk Gated、Supervisory Co-Execution、Structurally Enriched 四种策略，用 48 名参与者在活网环境下做对照实验并埋入隐私泄露、prompt injection、dark pattern。结论：策略更多塑造风险是否浮到台面，而非人在关键时刻的拦截能力——plan-based 两种策略把问题动作发生率压到 60.4% 与 74.5%，step-level 两种是 88.5% 与 90.1%；但 Risk Gated 在干预成功率上以 26.4% 排第一，Supervisory Co-Execution 仅 9.2%，最终攻击成功率四组都在 54.8%-67.3% 之间。作者据此提出 oversight 取决于能否让决策关键节点在执行中可识别并及时介入，而非最大化人类参与。论文 2026-04-06 提交 cs.HC，今天在 Agent 实践笔记中与 Anthropic 自主度报告、EU AI Act 第 14 条 'interrupt operation' 并读。

## 为什么值得关注

研究用对照实验证实了一个长期被反复提起的论点：人不是更警觉了，而是更顺手了。Bainbridge 1983 的 automation bias 描述 'exposure rather than correction'，跟论文结论几乎一致。论文给出的策略差值（plan-based 60.4% / 74.5% vs step-level 88.5% / 90.1%）对设计人类监督 UI 的人来说是一个可量化锚点。

## 关键信息

- 论文标题：Comparing Human Oversight Strategies for Computer-Use Agents
- 作者：Chaoran Chen, Zhiping Zhang, Zeya Chen, Eryue Xu, Yinuo Yang, Ibrahim Khalilov, Simret A Gebreegziabher, Yanfang Ye, Ziang Xiao, Yaxing Yao, Tianshi Li, Toby Jia-Jun Li
- arXiv：https://arxiv.org/abs/2604.04918
- 提交时间：2026-04-06
- arXiv 分类：cs.HC
- 关联标签：computer-use, oversight, human-in-the-loop, cua, arxiv

## English Abstract

LLM-powered computer-use agents (CUAs) are shifting users from direct manipulation to supervisory coordination. Existing oversight mechanisms, however, have largely been studied as isolated interface features, making broader oversight strategies difficult to compare. We conceptualize CUA oversight as a structural coordination problem defined by delegation structure and engagement level, and use this lens to compare four oversight strategies in a mixed-methods study with 48 participants in a live web environment. Our results show that oversight strategy more reliably shaped users' exposure to problematic actions than their ability to correct them once visible. Plan-based strategies were associated with lower rates of agent problematic-action occurrence, but not equally strong gains in runtime intervention success once such actions became visible. On subjective measures, no single strategy was uniformly best, and the clearest context-sensitive differences appeared in trust. Qualitative findings further suggest that intervention depended not only on what controls users retained, but on whether risky moments became legible as requiring judgment during execution. These findings suggest that effective CUA oversight is not achieved by maximizing human involvement alone. Instead, it depends on how supervision is structured to surface decision-critical moments and support their recognition in time for meaningful intervention.

## English Summary

The paper frames CUA oversight as a structural coordination problem along two axes — delegation structure (agent-led vs human-controlled) and engagement level (step-level vs plan-level) — yielding four strategies (Action Confirmation, Risk Gated, Supervisory Co-Execution, Structurally Enriched). A mixed-methods study with 48 participants in a live web environment planted privacy leaks, prompt injection and dark patterns. Oversight strategy more reliably shaped users' exposure to problematic actions than their ability to correct them once visible. Plan-based strategies were associated with 60.4% and 74.5% problematic-action rates versus 88.5% and 90.1% for the step-level pair; yet Risk Gated led intervention success at 26.4% versus 9.2% for Supervisory Co-Execution, with all four final attack-success rates clustered in 54.8%-67.3%. Effective CUA oversight therefore depends on whether decision-critical moments become legible during execution, not on maximizing human involvement.

## Obsidian Notes

- 来源 abstract 通过 `opencli arxiv paper 2604.04918 -f json` 抓取；arXiv 提交日期 2026-04-06 (cs.HC)。
- 中文导读与英文摘要均锚定在论文摘要原文，未补充摘要之外的实验细节。
- 今日由 Agent 实践探索笔记 `OpenClaw定时任务/Agent实践探索/2026-09-04-Agent实践探索.md` 重新提起，因此视为今日入库候选。
