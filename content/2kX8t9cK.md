---
title: "万字总结：我的 Harness Engineering 项目开发实践经验完整分享（上）"
source: "mp.weixin.qq.com"
category: "agents/frameworks"
tags: ["harness-engineering", "codex", "claude-code", "planner-evaluator-generator", "ai-coding"]
publish_date: "2026-04"
quality_score: 5
url: "https://mp.weixin.qq.com/s?__biz=MzIxMjk2NDE1NA==&mid=2247483752&idx=1&sn=4c49ba63e425aae3c3ea1b96ca138587"
---

# 万字总结：我的 Harness Engineering 项目开发实践经验完整分享（上）
# Harness Engineering: 15万行代码实践总结（Part 1）

## 中文原文 / Chinese Original

作者分享无手写代码前提下项目累计生成 **15 万行代码**的实践经验。

### 核心设计架构

**角色分工：Planner-Evaluator-Generator**

- **Planner（规划者）**：Codex（GPT 模型）负责规划、验收、需求拆解
- **Evaluator（验收者）**：独立角色负责验证实现是否符合要求
- **Generator（执行者）**：Claude Code（国产开源模型）负责代码生成

### 关键机制

1. **阶段计划**：每个任务分解为多个阶段，每阶段有明确验收标准
2. **结构化 Prompt**：用结构化方式描述需求，减少歧义
3. **零信任验收**：假设每次生成都有问题，强制执行验收流程
4. **长期记忆**：验收发现的问题（生产路径未验证、异常无日志）自动沉淀到记忆文件，下次自动检查

### 核心原则验证

文章验证了几个 Harness Engineering 的核心原则：

1. **规划与执行不能混** — Planner 如果同时执行，会失去客观判断能力
2. **验收与实现不能同角色** — 自己写代码自己验收，永远发现不了问题
3. **记忆要持久化** — 每次失败都要变成下次的防御能力

### 工程效果

在无手写代码的情况下：
- 累计生成 15 万行代码
- 单次任务平均执行 50+ 步骤
- 验收问题发现率 > 60%（大部分问题在验收阶段被发现）

---

## English Translation

Author shares practical experience of generating **150,000 lines of code** without hand-coding.

### Core Architecture

**Role Separation: Planner-Evaluator-Generator**

- **Planner**: Codex (GPT model) handles planning, acceptance, requirement breakdown
- **Evaluator**: Independent role verifies implementation against requirements
- **Generator**: Claude Code (domestic open-source model) handles code generation

### Key Mechanisms

1. **Phase Planning**: Each task divided into phases with clear acceptance criteria
2. **Structured Prompt**: Describe requirements structurally to reduce ambiguity
3. **Zero-Trust Acceptance**: Assume every generation has problems, enforce verification process
4. **Long-term Memory**: Issues found in acceptance (unverified production paths, no error logs) automatically沉淀 to memory files, checked automatically next time

### Core Principles Validated

Several Harness Engineering principles validated:

1. **Planning and execution must be separate** — if Planner also executes, it loses objective judgment
2. **Verification and implementation must not be the same role** — if you write code and verify it yourself, you'll never find problems
3. **Memory must be persistent** — every failure becomes next time's defense capability

### Engineering Results

Without hand-coding:
- 150,000 lines of code generated cumulatively
- Average 50+ steps per task execution
- 60%+ issue detection rate (most issues caught at verification stage)

> Source: [WeChat Article](https://mp.weixin.qq.com/s?__biz=MzIxMjk2NDE1NA==&mid=2247483752&idx=1&sn=4c49ba63e425aae3c3ea1b96ca138587)
