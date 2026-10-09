# Decoupling Exploration from Optimization in RLVR

- **ID**: dfb77cd2
- **原文链接**: https://arxiv.org/abs/2610.10536
- **PDF**: https://arxiv.org/pdf/2610.10536
- **作者**: Saif Punjwani, Micah Goldblum
- **日期**: 7 Oct 2026
- **更新**: N/A
- **分类**: models
- **来源类型**: paper
- **标签**: rlvr, exploration, distillation, reasoning, dapo
- **质量评分**: 4/5
- **抓取时间**: 2026-10-09T04:29:21Z
- **元数据来源**: arXiv abs 页面（HTTP 429 回退）

---

## 中文导读

RLVR 的核心卖点是发现新推理策略，但实践里给 RLVR 加强新颖性激励收效有限还会掉模型质量，而 verifiable reward 只监督模型知识和行为的一小段，一旦掉下去很难恢复ExpDis（Exploration-Distillation）把探索与优化解耦：先训一个或多个 reward 里带 novelty bonus 的 explorer 策略，按正确性与质量过滤其轨迹，再蒸馏进独立的学生策略，学生训练不带 novelty bonus，多轮交替探索与优化七个数学推理基准两个模型族上，ExpDis 在相同 wall-clock 预算下超过 DAPO，且 pass@k scaling 更好，说明学生策略能生成更多样化的正确解

## 为什么值得关注

条目一句话：RLVR 探索别和优化搅在一起：explorer 带奖探索蒸馏给学生，同预算超 DAPO

RLVR 的新颖性激励直接加在优化目标上容易掉模型质量，且 verifiable reward 只监督模型行为的一小段，掉了很难恢复。ExpDis 把探索拆给带 novelty bonus 的 explorer，轨迹按正确性与质量过滤后蒸馏进独立 student，同预算下超过 DAPO 等强基线。

## 关键信息

- 论文标题：Decoupling Exploration from Optimization in RLVR
- 作者：Saif Punjwani, Micah Goldblum
- arXiv：https://arxiv.org/abs/2610.10536
- 发布时间：7 Oct 2026
- arXiv 分类：Machine Learning (cs.LG) ; Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- 关联标签：rlvr, exploration, distillation, reasoning, dapo

## English Abstract

Modern language models undergo reinforcement learning with verifiable rewards (RLVR) on top of already-trained checkpoints. A key promise of RLVR is the discovery of new reasoning strategies. In principle, a model can sample novel ideas absent from its prior training data. In practice, however, augmenting RLVR with strong novelty incentives has seen limited success and can degrade model quality. Because verifiable rewards supervise only a narrow slice of the model's knowledge and behavior, such degradations are difficult to recover from. Instead, we decouple exploration from optimization in a framework we call Exploration-Distillation (ExpDis). We train one or more explorer policies with a novelty bonus in the reward, filter their trajectories for correctness and quality, and distill them into a separate student policy. The student policy is then trained without a novelty bonus. We repeat the above procedure for several rounds, alternating between exploration and optimization. This decoupling allows us to aggressively scale exploration without degrading the student policy. Across seven mathematical reasoning benchmarks and two model families, ExpDis outperforms DAPO at the same wall-clock budget. Moreover, we observe improved pass@k scaling, indicating that ExpDis produces models that generate more diverse correct solutions.

## English Summary

A key promise of RLVR is discovering new reasoning strategies, but in practice adding strong novelty incentives sees limited success and can degrade model quality, and because verifiable rewards supervise only a narrow slice of knowledge and behavior, such degradation is hard to recover from. Exploration-Distillation (ExpDis) decouples the two: train one or more explorer policies with a novelty bonus in the reward, filter their trajectories for correctness and quality, distill them into a separate student policy trained without the bonus, and repeat in alternating rounds. Across seven mathematical reasoning benchmarks and two model families, ExpDis outperforms DAPO at the same wall-clock budget, with improved pass@k scaling indicating the student generates more diverse correct solutions.

## Obsidian Notes

- 内容获取路径：优先尝试 `opencli arxiv paper 2610.10536 -f json`；如遇 arXiv API HTTP 429，则改由 arXiv abs 页面元数据与摘要回填。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 本文件写入 canonical content 目录（content/{id}.md），而非 openclaw/content/（project_root symlink 陷阱）。
