# CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators

- **ID**: bb45f4fd
- **原文链接**: https://arxiv.org/abs/2608.27406
- **PDF**: https://arxiv.org/pdf/2608.27406v1
- **作者**: Kechen Liu, Ola Shorinwa
- **日期**: 2026-08-27
- **更新**: 2026-08-27
- **分类**: models
- **来源类型**: paper
- **标签**: world-models, video-generation, robotics, cross-embodiment, zero-shot
- **质量评分**: 4/5
- **抓取时间**: 2026-08-31T12:36:54Z

---

## 中文导读

现有动作条件视频模型通常局限于单一机器人形态，无法利用互联网规模的跨形态异构视频学习可泛化物理CLAP 基于物理规律与执行者无关这一洞察，用末端执行器位姿语言指令与潜在动作调和不同动作空间，并给出课程式跨形态学习配方：先从未标注视频以潜在动作学习基础物理先验，再锚定到末端执行器动作空间，实现零样本部署到真实任务在 DROID 等高难环境中达到或超过单形态 SOTA 视频模型，少样本适配可进一步增益发布套件覆盖末端执行器语言潜在动作三类条件空间，以及跨形态DROIDBridge双臂 YAMG1 人形等形态，代码与模型全部开源

## 为什么值得关注

现有动作条件视频模型通常局限于单一机器人形态，无法利用互联网规模的跨形态异构视频学习可泛化物理CLAP 基于物理规律与执行者无关这一洞察，用末端执行器位姿语言指令与潜在动作调和不同动作空间，并给出课程式跨形态学习配方：先从未标注视频以潜在动作学习基础物理先验...

论文于 2026-08-27 提交至 arXiv（分类：c, s, ., R, O, ,,  , c, s, ., A, I, ,,  , c, s, ., C, V），arXiv 摘要页面：https://arxiv.org/abs/2608.27406。

## 关键信息

- 论文标题：CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators
- 作者：Kechen Liu, Ola Shorinwa
- arXiv：https://arxiv.org/abs/2608.27406
- 发布时间：2026-08-27
- arXiv 分类：c, s, ., R, O, ,,  , c, s, ., A, I, ,,  , c, s, ., C, V
- 关联标签：world-models, video-generation, robotics, cross-embodiment, zero-shot

## English Abstract

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical laws govern spatiotemporal dynamics regardless of the actor. However, cross-embodiment learning is non-trivial because action representations vary sharply across robot platforms and are typically absent in human videos. CLAP addresses this fundamental challenge through the following core contributions. First, CLAP reconciles disparate action spaces using end-effector poses, language instructions, and latent actions. Second, to resolve their individual limitations, CLAP introduces a curriculum-based cross-embodiment learning recipe that first learns foundational physical priors across unlabeled video data using latent actions and subsequently grounds them in end-effector action spaces for zero-shot deployment to real-world tasks. Crucially, CLAP approaches or surpasses state-of-the-art single-embodiment video models in challenging environments like DROID. These performance advantages compound via few-shot adaptation to establish a novel paradigm for training single-embodiment video world models. Ultimately, CLAP delivers the most comprehensive suite of action-conditioned video world models to date - spanning diverse action-conditioning spaces (end-effector, language, and latent) and robot morphologies (including cross-embodiment, DROID, Bridge, bimanual YAM robots, and G1 humanoids). We open-source all code and models. Project Website at https://omni-clap.github.io .

## English Summary

State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics. To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents. CLAP is grounded in the insight that universal physical laws govern spatiotemporal dynamics regardless of the actor. However, cross-embodiment learning is non-trivial because action representations vary sharply across robot platforms and are typically absent in human videos. CLAP addresses this fundamental challenge through the following core contributions. First, CLAP reconciles disparate action spaces using end-effector poses, language instructions, and latent actions. Second, to resolve their individual limitations, CLAP introduces a curriculum-based cross-embodiment learning recipe that first learns foundational physical priors across unlabeled video data using latent actions and subsequently grounds them in end-effector action spaces for zero-shot deployment to real-world tasks. Crucially, CLAP approaches or surpasses state-of-the-art single-embodiment video models in challenging environments like DROID. These performance advantages compound via few-shot adaptation to establish a novel paradigm for training single-embodiment video world models. Ultimately, CLAP delivers the most comprehensive suite of action-conditioned video world models to date - spanning diverse action-conditioning spaces (end-effector, language, and latent) and robot morphologies (including cross-embodiment, DROID, Bridge, bimanual YAM robots, and G1 humanoids). We open-source all code and models. Project Website at https://omni-clap.github.io .

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
