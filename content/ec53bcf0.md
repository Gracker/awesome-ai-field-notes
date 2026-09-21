# Don't Build Multi-Agents

- **ID**: ec53bcf0
- **原文链接**: https://cognition.ai/blog/dont-build-multi-agents
- **作者**: Walden Yan
- **日期**: 2025-06-12
- **分类**: agents
- **来源类型**: article
- **标签**: context-engineering, multi-agent, cognition, devin, walden-yan
- **质量评分**: 4/5
- **抓取时间**: 2026-09-21T23:30Z

---

## 中文摘要

Cognition 创始人 Walden Yan 2025 年 6 月 12 日发文核心论点：context engineering 是构建 agent 的首要工作，prompt engineering 解决把任务说清楚，context engineering 解决在动态多轮可能有工具调用的系统里自动把对的上下文递给模型两条原则：(1) 共享上下文共享完整 agent 轨迹而不是单条消息摘要；(2) 动作携带隐式决策子智能体写代码时的风格选择边界条件处理库函数偏好，很难在合并阶段还原Flappy Bird 案例：分两个子智能体并行画背景和鸟，最后合成常得到一个和游戏无关的鸟结论：未结构化的 swarm 网状多智能体今天基本是分心项，先看 workflow再考虑单线程线性 agent最后才是多智能体

## English Abstract

Walden Yan (Cognition) published this June 12, 2025 post arguing that context engineering not prompt engineering is the primary job of building agents. Prompt engineering solves 'state the task clearly'; context engineering solves 'in a dynamic, multi-turn, tool-using system, automatically hand the right context to the model.' Two principles follow: (1) Share context share full agent traces, not per-message summaries; (2) Actions carry implicit decisions sub-agents make style, edge-case, and library-preference calls during write actions that are very hard to recover at merge time....

## 为什么值得关注

Walden Yan: context engineering 是构建 agent 首要工作并行写动作隐式决策会失控先把工作流与单线程 agent 做对

## Obsidian 证据摘要

> 来源: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-09-21-AK-RSS-Digest（89源精选）.md + 对应 evidence-2026-09-21 文件
