# Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows

- **ID**: dfde62a9
- **原文链接**: https://arxiv.org/abs/2610.02122
- **PDF**: https://arxiv.org/pdf/2610.02122
- **作者**: Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing, Duke Gand, Joseph J Ma
- **日期**: 2026-10-01
- **更新**: 2026-10-01
- **分类**: agents
- **来源类型**: paper
- **标签**: data-agents, benchmark, enterprise, text-to-sql, simulation
- **质量评分**: 4/5
- **Fetch**: 2026-10-03T04:21:07Z

---

## 中文导读

Argo-Bench 用模拟世界评测企业级数据 agent：以公开数据同行评审行业文献与监管文件为底，模拟一个真实规模（2024 年 8,100 万订单）的纽约外卖平台，导出为建模自 Oracle E-Business Suite schema 的 235 张表75 亿行 ERP 仓库模拟器的 ground-truth 状态对 agent 不可见，任务要求先在仓库中导航重建事实再行动；评测超越 text-to-SQLagent 要封禁欺诈账号分配骑手激励预算补发工资，评分器按动作在模拟器中的后果打分210 个任务各带可执行参考解，回应了既有 text-to-SQL 基准答案键频出错误业务事件挤在单表里的局限

## 为什么值得关注

Argo-Bench 把数据 agent 扔进 75 亿行模拟 ERP：先导航重建事实，再为封号/预算/补薪等动作的后果负责

以上导读与价值判断锚定论文摘要与元数据，完整英文摘要见下文。

## 关键信息

- 论文标题：Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows
- 作者：Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing, Duke Gand, Joseph J Ma
- arXiv：https://arxiv.org/abs/2610.02122
- 发布时间：2026-10-01
- arXiv 分类：cs.CL, cs.AI, cs.DB
- 关联标签：data-agents, benchmark, enterprise, text-to-sql, simulation

## English Abstract

Real-world enterprise data science and analytics workflows require reasoning across dozens of tables, performing statistical analyses, and acting on the results. Established text-to-SQL benchmarks evaluate query generation alone, and audits have found their answer keys frequently wrong. Because real enterprise warehouses are too sensitive to release, these benchmarks are built on public datasets where a business event fits in a single table. We introduce Argo-Bench, an evaluation framework comprising 210 data science and analytics tasks. Drawing on public data, peer-reviewed industry literature, and regulatory filings, we simulate a food delivery platform in New York City at true scale, with 81 million orders in 2024, grounded economics, fraud patterns, and marketplace incentives. We export this world to an ERP warehouse of 235 tables and 7.5 billion rows, modeled on the Oracle E-Business Suite schema. The simulator's ground-truth state is withheld from the warehouse the agent sees, so tasks require reconstructing facts by navigating the warehouse before acting on them. Argo-Bench goes beyond text-to-SQL: the agent files actions such as banning fraudulent accounts, allocating courier incentive budgets, or issuing back pay, and the grader scores each by its consequences in the simulator. Every task has an executable reference solution that demonstrates solvability using only the warehouse. The strongest of 14 frontier and open-weight models scores 95 or higher on only 34.8% of tasks and averages 59.5 points. We hope Argo-Bench drives progress toward agents that understand, navigate, and act within real data environments.

## English Summary

Argo-Bench evaluates enterprise data agents against a simulated world: grounded in public data, peer-reviewed industry literature, and regulatory filings, it simulates a NYC food-delivery platform at true scale (81M orders in 2024) and exports it to an ERP warehouse of 235 tables and 7.5 billion rows modeled on the Oracle E-Business Suite schema. The simulator's ground-truth state is withheld from the agent's warehouse, so tasks require reconstructing facts by navigation before acting. Beyond text-to-SQL, agents file actions (banning fraudulent accounts, allocating courier incentives, issuing back pay) graded by their consequences in the simulator; all 210 tasks have executable reference solutions. Motivated by audits finding established text-to-SQL answer keys frequently wrong.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
