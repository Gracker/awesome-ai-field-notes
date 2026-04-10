# 单Agent框架

Single-Agent — 2 条活跃资源

### [Hermes 从 0 到 1 教程](https://x.com/Pluvio9yte/status/2041571378021986486) 
by @Pluvio9yte (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Nous Research 开源自改进 Agent 框架，内置持久记忆与 Skill 进化**

介绍 Nous Research 开源的自改进 AI Agent 框架 Hermes。核心特点：内置学习循环，每次完成任务后自动提炼可复用 Skill 存入持久记忆。多层记忆系统（短期+长时+Skills），支持 40+ 工具。与 OpenClaw 对比：Hermes 重单个 Agent 深度自我成长，OpenClaw 强在多平台覆盖和复杂工作流。内置 hermes claw migrate 迁移命令。
 `hermes` `nous-research` `self-improving` `agent` `memory` `openclaw`

---
### [Trace2Skill](https://arxiv.org/abs/2603.25158) 
 (2026-04-07) | ⭐⭐⭐ 3/5 | 🇨🇳

**LLM 推理能力增强的新方法**

LLM Agent 需要领域特定技能（skills）才能高效处理复杂任务。但技能创建面临三重困境：

1. 人工编写不可扩展：每个领域都需要专家花大量时间写详细的操作指南，随着 Agent 应用场景扩展，这个瓶颈越来越严重
2. 纯 LLM 生成效果差：直接让 LLM 凭参数化知识写技能，缺乏对目标领域具体操作和常见陷阱的了解，收益有限
3. 在线顺序更新导致碎片化：现有在线范式（如 ExpeL、Skill-Gen）按顺序处理每条轨迹，一条轨迹学一个教训就更新一次技能，导致技能碎片化且容易过拟合
 `obsidian` `fine-tuning` `agent` `llm` `paper` `reasoning` `memory` `ai`

---