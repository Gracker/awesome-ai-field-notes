# Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems

- **ID**: aeb4fec4
- **原文链接**: https://arxiv.org/abs/2611.05275
- **作者**: Pengfei Zhou et al.
- **日期**: 2026-11-03
- **分类**: models
- **来源类型**: paper
- **标签**: model-routing, orchestration, cost-efficiency, benchmarks, omni-modal, agents
- **质量评分**: 4/5
- **抓取时间**: 2026-11-05T23:54:07

---

## 中文导读

Route Anything 把模型与策略路由放进统一框架：覆盖语言、图像、视频、语音生成、编程与办公 agent、机器人操作的 25 个基准、452 种候选配置、374,401 次计分运行构成 omni-modal 轨迹矩阵，理论上刻画质量—成本权衡下的最优路由并证明路由器可得信息决定性能上限。逐输入 oracle 比最佳固定候选高 5.4 分；学习路由在 16 个基准上仅高 0.3 分，视频生成 +2.1、机器人操作 +1.1 且策略时间省 24%；相对参考模型平均效率提升 8.82 倍。「知道哪个候选最好」与「学会选它」之间的差距是本文最值得读的结论。

## 为什么值得关注

37 万次计分运行把路由研究拉回地面：oracle 与学习路由差 5 分，8.82 倍效率收益依赖参考模型与成本定义，不能当通用加速比

## English Summary

Route Anything studies model and policy routing as one problem: an omni-modal trajectory matrix spans 25 benchmarks (language, image, video, speech generation, coding and workplace agents, robot manipulation) with 374,401 scored runs from 452 candidate configurations, plus a theory of optimal routing under quality-cost trade-offs showing attainable performance is bounded by the information available to the router. Per-input oracle routing beats the best fixed candidate by 5.4 points; learned routers beat it by only 0.3 points across 16 benchmarks (+2.1 video generation, +1.1 robot manipulation with 24% less policy time). Routing raises efficiency 8.82x on average versus the reference model - an advantage that depends on the reference model and per-task cost definitions.

## 原文

- arXiv ID: 2611.05275 (cs.CV)
- Authors: Pengfei Zhou, Yixing Ma, Hexin Wang, Weidong Tang, Zhenglin Wan, Wangbo Zhao, Yang You
- Submitted: 2026-11-03 (updated 2026-11-03)
- PDF: https://arxiv.org/pdf/2611.05275v1

## Abstract (原文)

Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capability, a promising path toward AGI now is to orchestrate a heterogeneous ecosystem of specialized models, tools, and policies (candidates) into a unified AI system. At the heart of this vision lies a fundamental question: how can an AI system dynamically select and coordinate the most capable candidate for each task while balancing performance and computational cost? In this work, we present Route Anything, a unified framework for studying model and policy routing across general-purpose AI systems. We develop a unified theoretical foundation that characterizes optimal routing under quality--cost trade-offs and establishes how the information available to a router determines its attainable performance. To systematically investigate routing across diverse capabilities, we first construct an omni-modal trajectory matrix spanning 25 benchmarks across language understanding, image, video, and speech generation, coding and workplace agents, and robotic manipulation, comprising 374,401 scored runs from 452 candidate configurations. Building on this framework, we train and test different routers to investigate the potential of omni-modal model routing, the capabilities of learned routers, and the conditions under which routing improves efficiency. Our results reveal substantial opportunities for capability orchestration: per-input oracle routing outperforms the best fixed candidate by 5.4 points, and learned routers outperform it by 0.3 points across 16 benchmarks, by 2.1 points on video generation, and by 1.1 points on robot manipulation while using 24% less policy time. More importantly, routing raises efficiency by 8.82x on average compared with the reference model.

（抓取于 2026-11-05T23:54:07，来源见上方原文链接）
