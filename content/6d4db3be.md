# AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models

- **ID**: 6d4db3be
- **原文链接**: https://arxiv.org/abs/2611.14515
- **PDF**: https://arxiv.org/pdf/2611.14515
- **作者**: Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- **日期**: 2026-11-10
- **更新**: 2026-11-10
- **分类**: models
- **来源类型**: paper
- **标签**: rlvr, scaffolding, llm-training, teacher-student
- **质量评分**: 4/5
- **抓取时间**: 2026-11-12T04:22:28Z

---

## 中文导读

RLVR 把每次尝试压成一个结果数字，训练中产生的大量过程信息被浪费；训练期脚手架（写进 prompt 的策略/提示）的设计与调整又主要靠人按领域手工做。AutoScaffold 是一个 AI-for-AI 框架：冻结的 teacher 周期性检查学生的训练经历，诊断瓶颈后生成两类脚手架——跨任务共享策略与针对个别难题的提示——并随学生进步调整支持的内容与数量，评测时脚手架全部移除。同一框架零改动跑 ALFWorld、搜索式 QA、数学推理、GPU kernel 生成四个域，去脚手架评测全部超过对应 RL 基线：ALFWorld 成功率 +7.2、QA 平均精确匹配 +4.0、GPU kernel 超过 PyTorch 参考实现的任务比例最多 +5.0；数学上用约三分之一的学生训练步数超过 QuestA 报告精度。分析显示 teacher 会在每个任务类里识别不同失败，并随学生成长把脚手架从逐步流程教学转向针对性修补。

## 为什么值得关注

把 RL 训练里被丢弃的过程信息变成自适应课程，而且不碰奖励函数。

teacher 诊断的对象不是模型权重，而是学生的训练经历；产出是可移植的 prompt 脚手架，领域特定信息要求被压到最低，训练全程无人工介入。两个细节值得注意：评测时脚手架全部移除，收益是真实能力而非测试时辅助；修订过的脚手架比保留旧版或完全无脚手架更能帮助学生。对跑 RLVR 训练管线的团队，这是一个不改奖励、不改数据的提分杠杆，且同一框架跨四个域验证过。

## 关键信息

- 论文标题：AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
- 作者：Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- arXiv：https://arxiv.org/abs/2611.14515
- 发布时间：2026-11-10
- arXiv 分类：cs.LG; cs.CL
- 关联标签：rlvr, scaffolding, llm-training, teacher-student
- 备注：评测时移除脚手架；四域（ALFWorld/搜索式 QA/数学/GPU kernel）同一框架零改动复用

## English Abstract

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines this experience, diagnoses bottlenecks, and designs scaffolds in two forms: (i) strategies shared across a class of tasks and (ii) hints for individual hard tasks, adjusting the content and amount of support as the student learns. The scaffolds are removed at evaluation. We apply the same framework to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation. When evaluated without scaffolds, students trained with AutoScaffold outperform those trained with the corresponding RL baselines in all four domains, with gains of 7.2 points in ALFWorld success and 4.0 points in average QA exact match. On GPU kernel generation, AutoScaffold increases the fraction of tasks with a correct kernel that runs faster than the PyTorch reference by up to 5.0 points. On math, our student surpasses QuestA's reported accuracy using approximately one-third as many student training steps. Analyses show that the teacher identifies a different failure in each task class and shifts its scaffolds from step-by-step workflows to targeted fixes as the student improves, and that its revised scaffolds help the student learn more than keeping the previous scaffold or using no scaffold.

## English Summary

RLVR reduces each attempt to a single outcome number, and training-time scaffolds - strategies or hints injected into prompts - are still designed by humans per domain. AutoScaffold is an AI-for-AI framework where a frozen teacher periodically examines the student's training experience, diagnoses bottlenecks, and designs two scaffold forms - cross-task strategies and hints for individual hard tasks - adapting support as the student improves; scaffolds come off at evaluation. Applied unchanged to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation, students beat corresponding RL baselines evaluated scaffold-free in all four domains: +7.2 ALFWorld success, +4.0 QA exact match, up to +5.0 points on GPU kernels faster than the PyTorch reference, and math accuracy above QuestA with roughly one-third the student training steps.

## Obsidian Notes

- 内容获取路径：`opencli arxiv paper 2611.14515 -f json` 一次成功，以元数据+摘要回填。
- 中文导读与价值判断均锚定在论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 现代站点生成器按 `content/6d4db3be.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
