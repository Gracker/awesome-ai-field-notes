# CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

- **ID**: ec7b4a3f
- **原文链接**: https://arxiv.org/abs/2610.06829
- **PDF**: https://arxiv.org/pdf/2610.06829
- **作者**: Yifan Zhang, Yutong Dai, Viraj Prabhu, Zhiyuan Hu, Ran Xu, Zeyuan Chen
- **日期**: 2026-10-05
- **更新**: N/A
- **分类**: agents
- **来源类型**: paper
- **标签**: web-agents, conformal, self-verification, reinforcement-learning, test-time-scaling, arxiv
- **质量评分**: 5/5
- **抓取时间**: 2026-10-07T04:26:31Z

---

## 中文导读

开源 web agent 已经能执行真实浏览器任务，但用 RL 训练它们仍然依赖弱监督：二值任务成功信号太稀疏，做不了 credit assignment；用前沿模型当 judge 每步都调又太贵，而且部署时不能假设它可用。CLIFT 的思路是把昂贵的 judge 反馈蒸馏成可复用的信号：训练时让 agent 回答一组关于自身 rollout 的自然语言验证问题，Compositional Conformal Certifier 只保留那些 URL 条件证据与训练期 judge 一致的问题信号，用极性感知 lift 赋予带符号的信任权重，再以「永不从 judge 基线中扣减」的方式把验证分数混入每步奖励。测试时，这个认证问题库被冻结，原样复用为 Conformal Trajectory Selection（CTS）的结构化证据：agent 采样一条贪心 rollout 和若干多样化重试，自验证器总结每条 URL 轨迹，保守多数票决定是否弃当前解——全程不需要外部 judge。一个机制支持三种设定：WebArena Infinity 上取得开源 web agent 的 SOTA；VisualWebArena 上，用开源模型训练的问题库在测试时迁移到 GPT-5.5，在标准 harness 下达到 SOTA；Online Mind2Web 上不训练任何针对基准的 agent，仅翻译认证问题库就在零样本评估中改进了 live-web agent。

## 为什么值得关注

条目一句话：把昂贵的 judge 反馈蒸馏成可复用认证问题库——训练当奖励、测试时当免费裁判，一个机制吃三处。它正面回应开源 agent RL 的两个卡点（监督稀疏、judge 贵且部署不可得），conformal 认证让自验证信号有可校准的信任度，测试时无需 judge 的轨迹选择是部署友好的 test-time scaling。

## 关键信息

- 论文/文章标题：CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling
- 作者：Yifan Zhang, Yutong Dai, Viraj Prabhu, Zhiyuan Hu, Ran Xu, Zeyuan Chen
- 原文：https://arxiv.org/abs/2610.06829
- PDF：https://arxiv.org/pdf/2610.06829
- 发布时间：2026-10-05
- 分类：cs.CL (primary); cs.AI; cs.LG
- 关联标签：web-agents, conformal, self-verification, reinforcement-learning, test-time-scaling, arxiv

## English Abstract

Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language verification questions about its own rollouts; a Compositional Conformal Certifier keeps only question signals whose URL-conditional evidence agrees with a training-time judge, assigns signed trust weights through polarity-aware lift, and blends the resulting verifier score into per-step rewards in a way that never subtracts from the judge baseline. At test time, the same certified bank is frozen and reused as structured evidence for Conformal Trajectory Selection (CTS): the agent samples a greedy rollout and one or more diverse retries, the self-verifier summarises each URL trace, and a conservative majority-vote rule chooses whether to swap away from the current incumbent without calling any external judge. This single mechanism supports three settings. On WebArena Infinity, CLIFT achieves state-of-the-art performance among open-source web agents. On VisualWebArena, a bank trained with the open model transfers to GPT-5.5 at test time and reaches state-of-the-art performance under the canonical harness. On Online Mind2Web, without training an agent on the benchmark, translating the certified question bank improves a live-web agent in zero-shot evaluation. Together these results position conformal self-verification as a way to turn costly judge feedback into a reusable training signal and a judge-free test-time scaling signal.

## English Summary

CLIFT turns costly judge feedback into a reusable signal via conformal self-verification: during training the agent answers natural-language verification questions about its own rollouts, a Compositional Conformal Certifier keeps only judge-consistent signals and blends them into per-step rewards; at test time the frozen question bank drives judge-free Conformal Trajectory Selection. One mechanism yields SOTA among open-source web agents on WebArena Infinity, transfers to GPT-5.5 on VisualWebArena, and zero-shot improves a live-web agent on Online Mind2Web.

## Obsidian Notes

- 内容获取路径：优先尝试 `opencli arxiv paper 2610.06829 -f json`，遇 arXiv API HTTP 429；随后用 `opencli web read` 抓取 arXiv abs 页面，仅以页面可见元数据（标题、作者、提交时间、摘要、Subjects）回填，本页为 429 回退路径生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 现代站点生成器按 `content/{entry.id}.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
