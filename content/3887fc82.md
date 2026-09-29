---
title: 万字总结：Harness Engineering 项目开发实践经验完整分享
source: 36氪
date: 2026-05-30
url: https://eu.36kr.com/zh/p/3749464991187458
id: 2kX8t9cK
---

# 万字总结：Harness Engineering 项目开发实践经验完整分享

## 中文版

## 什么是 Harness Engineering？

Harness Engineering（驾驭工程）是一套围绕大语言模型建立的、工业级的管理制度。其核心理念是：AI 智能体就像一辆汽车，模型是引擎，交互程序是车轮，而 Harness 就是变速箱、制动器、仪表盘——让汽车能真正上路的那套系统。

2026 年第一季度，LangChain 发布《The Anatomy of an Agent Harness》，指出同一个模型，换上更精巧的 Harness 架构后，在 Terminal Bench 2.0 上的通过率直接从 52.8% 拉升至 66.5%——底层模型一动没动，纯靠"壳"的优化。

---

## 第一层：让 AI 按要求干活

### 问题：上下文不够 + 不听话

2025年，Anthropic 发现即使给 Claude 配上外部记忆系统（即 Context Engineering，记事本方案），依然存在四种失败模式：

1. **提前交卷**：智能体做了三个功能就宣布"项目完成"
2. **环境盲区**：代码有 Bug，跑不起来，智能体自己不知道
3. **虚标完成**：清单标了 done，功能实际是坏的
4. **失忆实习生综合征**：每轮新运行都花大量 Token 重新摸索项目结构

### 解法：管理制度 + 物理锁

Anthropic 的应对：
- **JSON 物理锁**：功能清单用 JSON 格式，智能体只能改"通过/不通过"字段，不能删功能、改描述，必须实际测试通过后才能标 passing
- **三步唤醒仪式**：每次 Session 开头强制执行 `pwd`（确认目录）+ `git log`（查看改动）+ 读进度文件
- **Git 存档与回滚**：每次代码改动通过 Git 存档，陷入死胡同可直接 `git revert`
- **Context Reset**：上下文溢出时彻底清空，换一条新智能体，只给它一张交接单

OpenAI 的做法（Repo-as-truth）：
- Agent 在运行时无法访问的东西 = 不存在
- 关键规则变成可执行的自动化检查（custom linter），挂在 CI 流水线上，违反了就合并不进去
- Doc-gardening Agent 专职维护文档，检测文档与代码脱节就自动发起修改

---

## 第二层：大规模并发控制

单个智能体能跑长途了，下一步是同时派出成百上千个智能体。但真正让它们涌入同一个代码仓库时——惨烈的连环车祸发生了。

### Cursor 的教训
20 个智能体同时工作时，有效吞吐量下降到仅相当于两三个——锁机制成了瓶颈。更绝望的是，其余智能体发现核心代码被占用，就专门挑最简单、最无关紧要的代码去改。

**解法**：Planner（规划器）+ Worker（执行器）+ Judge（裁判）的三层架构，在 DAG 引擎的单行道里，Planner 节点没吐出排期表之前，Worker 节点被硬生生锁死。

### Anthropic 的 C 编译器实验
16 个 Claude 实例并行写 C 语言编译器。整体编译和链接阶段出现了全局错误，智能体疯狂消耗算力，互相覆盖代码。

**解法**："二分查找"调试法。用 GCC 编译出来的内核作为参照，把"整个编译器哪里错了"拆成"这3个文件中哪个编译错了"，调试难度断崖式下降。

结果：近 2000 个 Session，两周时间，两万美金 API 费用，Claude Code 生成了 10 万行编译器，能编译出可以正常启动的 Linux 操作系统。

---

## 第三层：戳破 AI 的盲目自信

Agent 跑完大喊"任务完毕"，人类接手的代码是屎山——能用但巨慢，UI 混乱。

Harness v1 只解决了"不让 AI 瞎标"，没解决 AI 验证能力不足的问题。AI 面对自己完成的工作，几乎总是"自信地赞美"。

### Anthropic 的解法：Evaluator 对抗循环
把做事的（Generator）和评判的（Evaluator）分开。评估者会亲自动手验货，打开浏览器、点击按钮、验证报错栈，像真实用户一样操作一遍。

最新 V2 版本还引入了 Sprint Contract（冲刺合同）：每轮迭代开工前，Generator 和 Evaluator 先协商"做完长什么样"。

### Cursor 的解法：8 通道并行盲审
对于同一个代码差异，拉起 8 个独立的 Bugbot，每个通道拿到的代码顺序被打乱——顺序不同，推理路径就不同，幻觉不容易同步。8 个通道各自独立发现 Bug，最后用多数投票合并。

---

## 第四层：做减法的艺术

故事没有停在"加法"上。

Opus 4.5 和 4.6 登场后，Anthropic 开始拆自己造的东西：

- **Context Reset 拆了**：Opus 4.6 的上下文管理能力已强到不需要那块干净石板
- **Sprint Contract 拆了**：新模型已能自己把控节奏，不再需要每轮开工前先谈合同
- **Evaluator 从每轮对抗改成了最后一轮做 QA**：不是不需要了，是需要的方式变了

**核心洞察**：Harness 的每一个组件，都编码了一条"关于模型做不到什么的假设"。当假设不再成立，组件就该走了。

---

## 真正的护城河是什么？

Harness 的价值不是绝对的，而是相对于模型能力的。补偿面在迁移：

> 模型每强一分，Harness 的重心就移一寸。每一次加组件，都是在补偿模型当前做不到的事；每一次去组件，都是因为模型进步让某个补偿变成了多余的累赘。

真正有价值的不是补偿的厚度，而是**追踪补偿面迁移的能力**——知道下一寸该加什么，上一寸该拆什么。

护城河不在 Harness 的厚度，在迁移的速度。


---

## English Version

## What is Harness Engineering?

Harness Engineering is a pure industrial-grade management system built around large language models. The core idea: AI agents are like cars — the model is the engine, the interaction program is the wheels, and the Harness is the transmission, brakes, and dashboard that actually make the car drivable.

In Q1 2026, LangChain published "The Anatomy of an Agent Harness," showing that swapping in a better Harness architecture raised a model's Terminal Bench 2.0 pass rate from 52.8% to 66.5% — with zero changes to the underlying model.

---

## Layer 1: Making AI Follow Instructions

### The Problem: Context Overload + Non-compliance

Anthropic discovered that even with external memory systems (Context Engineering), four failure modes persisted:

1. **Early finish**: Agent did three features and declared "project complete"
2. **Environment blind spots**: Code has bugs that make it fail, agent doesn't know
3. **False positives**: Checklist says "done" but the feature is broken
4. **Amnesiac intern syndrome**: Every new session wastes massive tokens re-exploring the project

### Anthropic's Solution: Management System + Physical Locks
- **JSON physical lock**: Feature lists use JSON; agent can only toggle pass/fail, cannot delete features or alter descriptions
- **Three-step wake-up ritual**: `pwd` + `git log` + read progress file at session start
- **Git archiving and rollback**: Every code change archived in Git; `git revert` available
- **Context Reset**: When context overflows, clear everything and hand a fresh agent a handover document

### OpenAI's Approach: Repo-as-truth
- Whatever an Agent can't access at runtime = doesn't exist
- Key rules turned into automated checks (custom linters) on CI pipeline
- Doc-gardening Agent maintains docs, flags drift between docs and code

---

## Layer 2: Large-scale Concurrency Control

Once a single car runs reliably, the next step is sending hundreds at once. The result: catastrophic collisions.

### Cursor's Lesson
20 agents working simultaneously → effective throughput dropped to 2-3 agents. Agents found core code locked, so they started修改注释和缩进——pure chaos.

**Solution**: Planner → Worker → Judge three-layer hierarchy with DAG engine. Workers are physically locked until Planner approves the schedule.

### Anthropic's C Compiler Experiment
16 Claude instances writing a C compiler in parallel → global linking errors → agents burned compute and overwrote each other's code.

**Solution**: Binary search debugging. Use GCC's output as reference, narrow down which 3 files contain the bug. Result: ~2000 sessions, 2 weeks, $20K API costs, 100K-line compiler that boots Linux.

---

## Layer 3: Piercing AI's Overconfidence

Agent finishes, yells "task complete" — human接手发现代码是屎山.

Harness v1 solved "preventing AI from cheating on self-assessment" but not "AI can't objectively evaluate itself."

### Anthropic's Generator-Evaluator Loop
Separate the generator from the evaluator. The evaluator actually tests — opens browser, clicks buttons, reads error stacks. Pure end-to-end adversarial loop.

V2 introduced Sprint Contracts: before each iteration, Generator and Evaluator negotiate what "done" looks like.

### Cursor's 8-Channel Parallel Blind Review
For the same code diff, spin up 8 independent Bugbots with scrambled ordering. Each channel reasons differently, hallucinations don't sync. Majority voting merges results. Each bug must appear in multiple channels to pass.

---

## Layer 4: The Art of Subtraction

Opus 4.5/4.6 released — Anthropic started tearing out what they built:

- **Context Reset removed**: Opus 4.6's context management makes it unnecessary
- **Sprint Contract removed**: New model self-regulates without pre-round contracts
- **Evaluator reduced to final-round QA only**: Needs changed, not eliminated

**Core insight**: Every Harness component encodes an assumption about what the model can't do. When the assumption no longer holds, the component should go.

---

## What Is the Real Moat?

Harness value is relative to model capability. The compensation surface migrates:

> Every time the model gets stronger, the Harness重心 shifts one inch. Every addition compensates for what the model currently can't do; every removal is because model progress made a compensation become overhead.

The real value isn't the thickness of compensation — it's the **ability to track where the compensation surface is migrating**.

