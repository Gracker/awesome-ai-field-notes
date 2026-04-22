# 深度解析 Claude Code 在 Prompt / Context / Harness 的设计与实践

来源: https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247559627
作者: 阿里妹（技术实践与独立思考）

## 文章概述

本文从 Prompt Engineering（提示词工程）、Context Engineering（上下文工程）和 Harness Engineering（驾驭工程）三个维度，系统解析 Claude Code 的内部设计，提炼可复用的 Agent 系统方法论。

## Prompt Engineering：静态与动态信息的组装

Claude Code 的 System Prompt 是一个多层级、动态组装的过程，通过以下六步实现：

1. **QueryEngine 发起请求**：`ask()` → `fetchSystemPromptParts()` → `buildEffectiveSystemPrompt()` → `query()`
2. **并行获取三大组件**：defaultSystemPrompt + systemContext + userContext
3. **组装默认 System Prompt**：分为静态部分（身份介绍、系统行为规则、任务执行指南、操作安全守则、工具使用指南、语气风格、输出效率）和动态部分（会话特定指导、自动记忆、环境信息、语言偏好、输出风格、MCP 指令等）
4. **优先级决策**：overrideSystemPrompt > Coordinator prompt > Agent prompt > customSystemPrompt > defaultSystemPrompt
5. **注入上下文**：appendSystemContext() 追加 Git 状态，prependUserContext() 注入 CLAUDE.md 内容
6. **缓存分块**：splitSysPromptPrefix() 将 Prompt 数组拆分为 cacheScope='org'、'global' 和 null 三个层级

## Context Engineering：三层渐进式压缩体系

### Layer 1: MicroCompact（微压缩）
纯规则驱动，无 LLM 调用。对超过时间阈值的旧消息工具输出进行截断，或在 KV Cache 边界外执行压缩。

### Layer 2: Session Memory Compact（会话记忆压缩）
直接复用已有会话记忆摘要替换冗长历史消息。触发门槛：Token ≥ 10,000 且文本消息条数 ≥ 5 条。

### Layer 3: Full LLM Compact（完全压缩）
调用 LLM 生成结构化摘要，遵循严格 9 段式模板（Primary Request、Key Technical Concepts、Files/Code、Errors/fixes、Problem Solving、User messages、Pending Tasks、Current Work、Optional Next Step）。

引入**隐式思维链（Implicit CoT）**：要求模型在 `<analysis>` 标签内推演，再在 `<summary>` 输出，防止幻觉。

## Memdir 结构化记忆系统

四种记忆类型：
- **User（用户级）**：个人偏好、操作习惯
- **Feedback（反馈级）**：模型修正记录、避坑指南
- **Project（项目级）**：技术选型、架构决策
- **Reference（参考级）**：文档片段、代码模式

引入 LLM-in-the-loop 检索：使用 Sonnet 模型做语义驱动检索，最多返回 5 条最相关记忆。

## Harness Engineering：六大系统内置 Agent

| Agent | 功能 | 特点 |
|-------|------|------|
| General-Purpose Agent | 万能打工人 | tools=['*']，默认模型 |
| Explore Agent | 代码库侦察兵 | 严格只读，Haiku 模型 |
| Plan Agent | 软件架构师 | 只读，继承父模型，结构化输出 |
| Verification Agent | 质量检验官 | 红蓝对抗思维，严格权限控制，按变更类型分类验证策略 |
| Claude Code Guide Agent | 自我说明书 | Haiku 模型 |
| Statusline Setup Agent | 状态栏安装 | 仅 Read+Edit |

### Verification Agent 设计哲学
1. **红蓝对抗**：不是确认代码能跑，而是想办法把它搞崩
2. **反偷懒话术**：代码看起来对 ≠ 运行过了，实现者测试通过 ≠ 独立验证过
3. **严格权限**：验证专用，禁止修改文件
4. **分类验证策略**：前端/后端/CLI/基础设施/Bug修复/数据库迁移各有不同策略

## 安全体系

- **Permission Engine**：Allow/Ask/Deny 三行为模型，多源规则配置，优先级覆盖机制
- **Sandbox Isolation**：基于 bubblewrap 的 Linux 沙箱，文件系统只读挂载、Network/PID 命名空间隔离、以非 root 用户运行
- **异步生成器驱动主循环**：流式处理、协作式控制、优雅取消、有状态上下文维持

## 有趣彩蛋

- **Caffeinate**：阻止 Mac 休眠，Claude Code 干活时保护电脑不睡着
- **Anti-Distillation**：注入假工具定义防止蒸馏
- **Undercover Mode**：卧底模式，隐藏 AI 身份
- **Buddy System**：电子宠物系统（ASCII 艺术精灵）
- **荒诞加载动词**：一百多个随机动词如 Hullaballooing、Discombobulating、Clauding

## 结论

Claude Code 在 Prompt/Context/Harness 三个维度的设计为 Agent 系统构建树立了极佳的技术标杆。其工程化思路（分层压缩、Memdir 语义记忆、Verification Agent 红蓝对抗、沙箱隔离、异步生成器主循环）可直接复用。
