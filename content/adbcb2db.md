# FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents

- **ID**: adbcb2db
- **原文链接**: https://arxiv.org/abs/2609.35744
- **PDF**: https://arxiv.org/pdf/2609.35744v1
- **作者**: Hoyoung Lee, Suyeol Yun, Jack Haverty, Yunju Cho, Meesong Kim, Daekyung Park, Sumin Kim, Jihoon Kwon, Jasmine Jia Geng, Andrew Chin, Yin Luo, Edward Tong, Yu Yu, Zach Golkhou, Minkyu Kim, Igor Halperin, Young Cha, Alejandro Lopez-Lira, Chanyeol Choi, Yongjae Lee
- **日期**: 2026-09-28
- **更新**: 2026-09-28
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-evaluation, rubric, finance, benchmark
- **质量评分**: 4/5
- **抓取时间**: 2026-09-30T12:24:18Z

---

## 中文导读

评估金融研究智能体需要体现专家标准且按信息截止日固定数值的评分规则（rubric）FinAutoRubric 让专家只提供可复用的评估指引，由智能体与代码执行具体任务的 rubric 生成复核与校验：指引同时作为提示词与代码强制规则，可复用标准库（Task Bank）跨任务传递；长循环中 writer 智能体逐一研究预期值reviewer 智能体核验，失败升级到人在三个专家撰写的金融基准上，其 rubric 与最强生成器同样贴合专家打分与人工评分一致，且在盲评中被内部分析师更偏好随论文发布 100 查询的 FinAutoRubric Benchmark（78 个任务八类资产），并显示上一代模型生成的 rubric 对新一代模型仍有区分度/余量

## 为什么值得关注

评估金融研究智能体需要体现专家标准且按信息截止日固定数值的评分规则（rubric）FinAutoRubric 让专家只提供可复用的评估指引，由智能体与代码执行具体任务的 rubric 生成复核与校验：指引同时作为提示词与代码强制规则，可复用标准库（Task Bank）跨任务传递.

- arXiv categories: c, s, ., A, I, ,,  , q, -, f, i, n, ., C, P
- published 2026-09-28, updated 2026-09-28; 20 authors
- fit: entry category `agents`, tags agent-evaluation, rubric, finance, benchmark

## 关键信息

- 论文标题: FinAutoRubric: Expert-Guided Automatic Rubric Generation for Evaluating Financial Research Agents
- 作者: Hoyoung Lee, Suyeol Yun, Jack Haverty, Yunju Cho, Meesong Kim, Daekyung Park, Sumin Kim, Jihoon Kwon, Jasmine Jia Geng, Andrew Chin, Yin Luo, Edward Tong, Yu Yu, Zach Golkhou, Minkyu Kim, Igor Halperin, Young Cha, Alejandro Lopez-Lira, Chanyeol Choi, Yongjae Lee
- arXiv: https://arxiv.org/abs/2609.35744
- 发布时间: 2026-09-28
- arXiv 分类: c, s, ., A, I, ,,  , q, -, f, i, n, ., C, P
- 关联标签: agent-evaluation, rubric, finance, benchmark

## English Abstract

Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expert-reviewed finance benchmarks rely on fixed, per-item rubrics, which are costly to extend and cannot encode each institution's own standard. In FinAutoRubric, experts specify reusable evaluation guidance, while agents and code carry out query-specific rubric generation, review, and validation. This expert guidance governs every agent, as prompts and as rules that code enforces, and a Task Bank of reusable criteria carries it across tasks. In long-horizon loops that follow the expert guidance, a writer agent researches every expected value and a reviewer agent verifies it, and failures escalate to a human. On three expert-authored finance benchmarks, its rubrics track expert scoring as closely as the strongest evaluated generator while stating the expert rubric's expected value for more criteria, their scores agree with human grading, and in-house analysts prefer them in a blind review. The released 100-query FinAutoRubric Benchmark, built from in-house analysts' key questions across 78 tasks and eight asset classes, shows that rubrics from an earlier model generation still leave headroom for a later one.

## English Summary

Evaluating finance research agents requires rubrics that reflect expert standards and fix the values correct as of an information cutoff. Expert-reviewed finance benchmarks rely on fixed, per-item rubrics, which are costly to extend and cannot encode each institution's own standard. In FinAutoRubric, experts specify reusable evaluation guidance, while agents and code carry out query-specific rubric generation, review, and validation. This expert guidance governs every agent, as prompts and as rules that code enforces, and a Task Bank of reusable criteria carries it across tasks. In long-horizon loops that follow the expert guidance, a writer agent researches every expected value and a reviewer agent verifies it, and failures escalate to a human....

## Obsidian Notes

- 内容由 opencli arxiv paper 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断锚定在条目摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
