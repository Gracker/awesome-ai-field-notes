# Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance

- **ID**: c1dcf2e2
- **原文链接**: https://arxiv.org/abs/2611.23142
- **PDF**: https://arxiv.org/pdf/2611.23142v1
- **作者**: Lorenzo Masoero
- **日期**: 2026-11-17
- **更新**: 2026-11-17
- **分类**: agents
- **来源类型**: paper
- **标签**: multi-agent, documentation, deployment, support-triage, field-report
- **质量评分**: 4/5
- **抓取时间**: 2026-11-19T04:20:42Z

---

## 中文导读

已部署多 agent 系统实战：代码迭代快于客户文档，而 LLM agent 又把文档当主接口，陈旧内容被当成权威传播；TriAgent 持续抽取两类信号（已解决支持工单暴露的文档缺口，自动化回路发现的代码与文档偏差）并修复漂移；43 天影子模式运行 triage 499 张工单，找出 92 处缺口；来自独立模型家族的 LLM 评审团判定其可验证断言 81.1% 正确（人工有结论的 302 条中 245 条，三评审多数）；IAAI-27 录用

## 为什么值得关注

已部署多 agent 系统实战：代码迭代快于客户文档，而 LLM agent 又把文档当主接口，陈旧内容被当成权威传播；TriAgent 持续抽取两类信号（已解决支持工单暴露的文档缺口，自动化回路发现的代码与文档偏差）并修复漂移...

arXiv 2026-11 新一批 agent 安全与能力研究：覆盖自我改进自主性、跨组织信任基础设施、文档维护多 agent 实战、跨屏组合危害评测、长程漏洞利用能力激发，均为 agent 能力边界与安全机制的直接证据。

## 关键信息

- 论文标题：Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance
- 作者：Lorenzo Masoero
- arXiv: https://arxiv.org/abs/2611.23142
- 发布时间：2026-11-17
- arXiv 分类：cs.SE, cs.AI, cs.CL
- 关联标签：multi-agent, documentation, deployment, support-triage, field-report

## English Abstract

The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind already exist in abundance, both explicit (e.g., resolved support tickets revealing what documentation lacks) and implicit (e.g., code-documentation discrepancies detectable from automated loops). We deploy a multi-agent system, built around a triage agent we call "TriAgent," that continuously extracts these signals and repairs documentation drift. Over 43 days of shadow-mode operation, our system triaged 499 tickets and surfaced 92 gaps in the documentation. Using a panel of LLM judges from independent model families, 81.1% of TriAgent's verifiable assertions were correct (245 of the 302 assertions the human resolution addresses; majority of three judges); on length-comparable pairs the panel preferred TriAgent's response in 70.5% of pairs and the human engineer's in 23.2% (the rest had no judge majority). Importantly, agent- and human-sourced replies tended to be complementary, with the human often surfacing insights that were either buried within the existing documentation or missing from it entirely; our system turns each such insight into a documentation gap and, after human review, a fix. Repairing a gap measurably improved the agent's later answer: when the agent re-answered the same ticket after the repair, blinded judges preferred the post-repair answer over its own pre-repair answer 71.4% of the time (n=35). A blinded human audit confirms strong alignment on self-improvement.

## English Summary

Code now evolves faster than customer-facing documentation, and as users rely on LLM-based agents that consume documentation as their primary interface, stale information propagates and is treated as authoritative. This deployed multi-agent system, built around a triage agent called TriAgent, continuously extracts explicit signals (resolved support tickets revealing missing documentation) and implicit signals (code-documentation discrepancies detectable from automated loops), then repairs documentation drift. Over 43 days of shadow-mode operation it triaged 499 tickets and surfaced 92 documentation gaps. A panel of LLM judges from independent model families found 81.1% of TriAgent's verifiable assertions correct (245 of 302 assertions addressed by the human resolution, by majority of three judges).

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
