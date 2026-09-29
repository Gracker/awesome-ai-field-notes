# Jev-Mobile: Jev as an Executor for Mobile GUI Agents

> 原文链接: https://arxiv.org/abs/2609.30186
> 作者: Linghua Zhang
> 发布时间: 2026-09-24
> 源: arxiv

---

## 摘要

Jev-Mobile(arXiv 2609.30186)改写 mobile GUI agent 的范式:把 VLM 的角色压到「低频规划」,动作落地交给高频轻量执行器。具体:VLM 指定 local goals,accessibility tree 定义结构化可执行动作空间,一个叫 Jev 的快 typed decision model 在这个空间内反复选动作——一次 VLM 决策可以支撑多步 GUI 动作,降低昂贵 VLM 推理同时保留自适应交互。AndroidWorld 全套任务:成功率 79%(SeeAct-V 78%、Step-wise VLM 84%),成功轨迹端到端时间 -32.7%,API 成本 -73.4%。

## English Summary

Jev-Mobile (arXiv 2609.30186) rewrites the mobile GUI agent paradigm by downshifting the VLM to 'low-frequency planning' and handing action grounding to a high-frequency lightweight executor. Concretely, the VLM specifies local goals, the accessibility tree defines a structured executable action space, and Jev — a fast typed decision model — repeatedly selects actions within that space, so a single VLM decision grounds multiple GUI actions while preserving adaptive interaction. On the full AndroidWorld suite the system hits 79% task success (versus 78% for SeeAct-V and 84% for a step-wise VLM baseline) and, among successful trajectories, cuts end-to-end time by 32.7% and API cost by 73.4%.

## 为什么值得关注

主题线扩展 AAIF `mobile-gui-agent/vlm/accessibility-tree/androidworld` 等主题。

## 信息源

- https://arxiv.org/abs/2609.30186
