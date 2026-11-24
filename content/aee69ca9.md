# AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering

- **ID**: aee69ca9
- **原文链接**: https://arxiv.org/abs/2611.27734
- **PDF**: https://arxiv.org/pdf/2611.27734v1
- **作者**: Minye Shao, Chenghao Xiao, Xingyue Zhao, Yang Long
- **日期**: 2026-11-20
- **更新**: 2026-11-20
- **分类**: agents
- **来源类型**: paper
- **标签**: agents, benchmark, knowledge-graph, ontology
- **质量评分**: 4/5
- **抓取时间**: 2026-11-24T04:20:39Z

---

## 中文导读

AutoOntologyBench 把 agent 能否自建可用知识变成可测的题：19947 个经审计任务，覆盖 7 个领域 18 个真实知识源，带源生校验，在统一知识表示下对比 9 个前沿模型 agent检索之上叠加 agent 自建本体可加 6.1 分任务成功率，但比专家本体仍差 13 分，说明自主知识获取才是科研 agent 规模化的瓶颈做 agent 知识层或记忆系统的人，值得把这 13 分差距当成自己的标尺

## 为什么值得关注

AutoOntologyBench：agent 自建本体加 6.1 分但落后专家本体 13 分，知识获取成科研 agent 瓶颈

做 agent 知识层或科研自动化时，agent 自建本体在检索之上加 6.1 分任务成功率、仍落后专家本体 13 分，这组数字可以直接当自主知识获取能力的标尺。

## 关键信息

- 论文标题：AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering
- 作者：Minye Shao, Chenghao Xiao, Xingyue Zhao, Yang Long
- arXiv：https://arxiv.org/abs/2611.27734
- 发布时间：2026-11-20
- arXiv 分类：cs.CL
- 关联标签：agents, benchmark, knowledge-graph, ontology

## English Abstract

Foundation-model agents are increasingly extending beyond software engineering (SWE) into autonomous scientific research, where acquiring and integrating domain knowledge remains a critical challenge. Recent industrial advances have increasingly adopted knowledge graphs and ontology-based semantic layers to organize heterogeneous knowledge into reusable representations. We ask: Can autonomous agents construct ontologies that help them solve real tasks, and do they offer measurable benefits over alternative knowledge representations? Existing benchmarks evaluate ontology correctness or agent task success in isolation, leaving the value of autonomously acquired knowledge unresolved. We therefore introduce AutoOntologyBench, a task-grounded benchmark comprising 19,947 audited tasks grounded in 18 real-world knowledge sources across 7 domains, with source-native verification. Spanning Application, Repair, Organization, and Construction, AutoOntologyBench compares nine frontier-model agents under matched knowledge representations. Layered on retrieval, agent-built ontologies add 6.1 points of task success, yet trail an expert-derived reference by 13.0, identifying autonomous knowledge acquisition as the bottleneck to scalable scientific research. Code and resources are available at https://github.com/VinyehShaw/AutoOntologyBench.

## English Summary

AutoOntologyBench asks whether autonomous agents can construct ontologies that measurably help them solve real tasks, and whether they beat alternative knowledge representations. The benchmark contains 19,947 audited tasks grounded in 18 real-world knowledge sources across 7 domains, with source-native verification, comparing nine frontier-model agents under matched knowledge representations. Layered on retrieval, agent-built ontologies add 6.1 points of task success, yet trail an expert-derived reference by 13.0 points, identifying autonomous knowledge acquisition as the bottleneck for scalable autonomous scientific research. Code and resources are available on GitHub.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
