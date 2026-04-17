---
title: 'SmartPerfetto AI Agent 的 Harness Engineering 实战分享'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# SmartPerfetto AI Agent 的 Harness Engineering 实战分享

> Android Perfetto trace 分析 AI Agent 完整工程实践，MCP+Skill 三层验证范本

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=MzIwNTQxMjM5MA==&mid=2247487518&idx=1&sn=ec49eac761ffd13acc02cd5e6cea7b94) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-03-30

`SmartPerfetto` `Perfetto` `Android` `性能优化` `MCP` `Agent` `Harness-Engineering`

---

# SmartPerfetto AI Agent 的 Harness Engineering 实战分享

> 公众号: Android Performance
> 发布时间: 1970-01-01 08:33:46
> 原文链接: https://mp.weixin.qq.com/s?__biz=MzIwNTQxMjM5MA==&mid=2247487518&idx=1&sn=ec49eac761ffd13acc02cd5e6cea7b94

---
> 这篇文章记录了 SmartPerfetto 从零到可用过程中的关键技术决策——为什么选这个方案而不是那个，哪些地方踩了坑，踩完之后怎么调整的。
>
> SmartPerfetto 项目目前还处于开发期，所以还没有上线，如果没有意外会在合适的时机选择开源，大家共建。

## 为什么做这个工具

我做了多年 Android 性能优化。日常工作中大量时间花在 Perfetto trace 分析上——Perfetto 是 Google 开源的系统级 trace 工具，采集帧渲染、线程调度、CPU 频率、Binder 通信等数据，几乎是 Android 性能分析的标准工具。它的 trace\_processor 引擎把 trace 加载到一个嵌入式 SQLite 数据库中，支持用 SQL 查询。

分析 trace 的过程是高度重复的：找到问题区间、查帧数据、看线程状态、追阻塞链、关联系统指标。每次做的事情类似，但每个 trace 的细节不同。这种「流程固定、细节变化」的工作特点很适合 AI Agent 来处理——把固定流程中的数据收集和初步归因自动化，人来做最后的判断和确认。

SmartPerfetto 就是这个尝试的产物。它在 Perfetto UI 上加了一个 AI 分析面板，用户用自然语言提问（如「分析滑动性能」），背后由 Claude Agent 通过 MCP（Model Context Protocol，Anthropic 提出的工具调用协议）调用 trace\_processor 执行 SQL，自主完成多轮数据收集和分析。

写这篇文章的目的，是把构建过程中的工程决策和教训记录下来。从最初的「直接调 API」到现在的最多 20 个 MCP 工具（9 常驻 + 11 条件注入）+ 158 个 YAML Skill + 三层验证体系，中间的每个设计选择都有具体的反例在推动——试过不行才换的方案。这些踩坑记录对做 AI Agent 应用或者做 Android 性能工具的工程师可以直接借鉴。

## 开篇：同一个 Trace，两条分析路径

一个滑动 trace，120Hz 设备，用户反馈列表滑动偶尔卡顿。打开 Perfetto 看到惯性滑动阶段有 18 帧掉帧，其中 3 帧 Full 级（~60ms，120Hz 设备的单帧预算是 8.33ms）。

**路径 A：手动分析**

```
1. 打开 Perfetto UI，拖动时间轴找到滑动区间2. 展开 frame_timeline track，逐帧检查哪些超过 VSync 周期3. 18 帧掉帧——逐帧点开，展开 thread_state 切片，查看主线程在做什么4. 帧 1：Sleeping，手动查 waker_utid → system_server（Android 系统核心进程，托管 AMS/WMS 等系统服务）Binder 回来慢   帧 2：Running，但在 Choreographer#doFrame 里卡了 → RecyclerView onBind 过重   帧 3：Sleeping + Running 交替 → dequeueBuffer 等 SurfaceFlinger 合成   ... (还有 15 帧需要逐一检查)5. 关联 CPU 频率 track，确认是否有热降频或 governor 升频延迟6. 检查是否有 GC pause、Lock contention、Binder 超时7. 汇总证据，组织结论
```

第 3-4 步是主要工作量——18 帧掉帧，每帧都需要展开 thread\_state、追踪阻塞原因、关联 CPU 调度。分析过程是逐帧串行的：每帧的下钻路径可能不同（Binder? 锁? GC? IO?），全部看完再汇总。

**路径 B：SmartPerfetto Agent**

用户输入 `"分析滑动性能"`，以下是 Agent 实际执行的操作（来自 session log `session_agent-1774679540422`）：

```
classifyScene("分析滑动性能") → scrolling  (<1ms, 关键词匹配)buildSystemPrompt() → 4500 tokens (scrolling.strategy.md 注入)submit_plan({  phases: ["p0: 架构+时间范围", "p1: 滑动概览+掉帧列表",           "p1_9: 根因深钻", "p3: 综合结论"],  successCriteria: "WHY 链 ≥2 级，可操作优化建议"})invoke_skill("scrolling_analysis", {process_name: "com.example..."})  → 18 帧掉帧全部提取，每帧附带:    - 耗时、jank_type、reason_code (App/SF/GPU)    - 主线程状态分布 (Running/Sleeping/IO)    - 阻塞函数 top-3  → ArtifactStore: art_1 (~440 tokens 引用)fetch_artifact("art_1", "rows", 0, 18)  → 获取全部 18 帧的结构化数据invoke_skill("frame_blocking_calls", {frame_ids: [3, 7, 12]})  → 3 帧代表帧的阻塞链: dequeueBuffer / Binder / GClookup_knowledge("rendering-pipeline")  → 加载渲染管线参考资料输出结论:  [HIGH] 惯性滑动阶段 18 帧卡顿，3 次 Full 级 ~60ms 掉帧  [MEDIUM] 14 帧 Buffer Stuffing (App 按时完成渲染，但 BufferQueue 满导致呈现延迟)  [MEDIUM] Vulkan Shader 首帧编译 + CPU 冷频 (18.66ms, 超预算 2.2×)
```

**Metrics 快照** (来自 `logs/metrics/`)：16 次工具调用，0 次失败，SQL 平均 652ms。

下图展示了一次完整分析的请求生命周期——从用户输入到最终结论的每一步：



两条路径的分析步骤相同——查帧数据 → 定位 jank → 追踪阻塞链 → 关联系统状态 → 归纳结论。

差异在于：手动分析逐帧串行，每帧需要手动展开和追踪；Agent 通过 `scrolling_analysis` Skill 用一条 SQL 批量获取全部 18 帧的结构化数据，再选代表帧深钻阻塞链。

Agent 的分析结果同时落地到 Perfetto UI 上：

•**Auto-Pin**：Agent 提到的关键帧和 Slice 自动标记在时间线上

•**点击跳转**：结论中的时间戳和帧 ID 支持点击跳转到 Perfetto 对应位置

•**数据表格**：18 帧的完整性能数据以结构化格式渲染为可排序、可筛选的表格

**运行截图：以 SmartPerfetto 前端以 Perfetto 插件的形式存在**



**运行截图：滑动分析的时候详细分析每一个掉帧的地方， 点击最左边那个剪头可以展开**



**运行截图：滑动分析结论**



**运行截图：滑动分析结论，代表帧分析**



**运行截图：滑动分析结论，代表帧分析**



**运行截图：每一轮分析都有单独的分析 report，内容与前端显示的一致（更详细一些）**





分析结论、数据表格和 Perfetto 时间线在同一个界面上。Agent 完成批量数据收集和初步归因后，工程师在 Perfetto UI 上确认关键发现。

> 需要说明的是，当前 Agent 在复杂边界情况下仍然需要人的判断（后文会具体讨论误诊问题）。这篇文章记录的是构建这个 Agent 背后的工程决策过程。

* * *

## 第一部分：为什么 LLM 不能直接分析 Trace？

在开始讨论架构之前，需要先回答一个根本问题：为什么不能直接把 trace 数据发给 LLM 让它分析？这个问题的答案决定了 SmartPerfetto 整个架构的出发点。

### 数据规模：trace 文件装不进上下文

一个实际的 Perfetto trace 的数据规模是这样的：

维度

典型值

Trace 文件大小

50MB - 500MB

事件数量

百万 ~ 千万级

序列化为文本后

数 GB

Claude 最大 context

~200K tokens（约 150KB 文本）

两者差了好几个数量级。即使是一个较小的 50MB trace，里面的 slice（函数调用记录）、counter（CPU 频率采样点）、thread\_state（线程调度状态）等数据序列化后也远超 LLM 的上下文容量。

这就意味着 LLM 不可能直接「看到」trace 数据。它必须通过工具按需查询——先用 SQL 找到需要的数据子集（比如某个时间范围内某个线程的状态分布），拿到查询结果后再做分析。这个约束从根本上决定了 SmartPerfetto 必须是一个 **工具驱动** 的 Agent 架构，而不是把数据喂进 prompt 的简单方案。

### 精确计算：LLM 不擅长处理数值

性能分析的日常工作围绕精确数值展开：帧耗时的 P50 / P90 / P99 分位数、VSync 周期检测（需要对 VSYNC-sf 间隔取中位数并吸附到标准刷新率）、CPU 利用率的百分比计算、各线程状态的时间占比。

LLM 处理这类数值计算时经常出错。一个实际例子：早期测试中，Claude 把 16.7ms 的帧耗时判断为「正常，未超过 VSync 周期」——它按 60Hz（16.67ms）的帧预算来算了。但这个 trace 采集自一台 120Hz 设备，单帧预算应该是 8.33ms，16.7ms 实际上超预算了一倍。这类错误看起来很小，但在性能分析中会导致完全相反的结论。

数值计算必须由工具完成——SQL 的 `AVG()`、`PERCENTILE()` 和 YAML Skill 中预定义的统计逻辑，保证每次计算结果一致且精确。

### 领域知识：LLM 知道但不会用

Android 的渲染管线复杂度是很多开发者没有预期到的。最常见的三种渲染路径是：标准 HWUI 管线（HWUI 是 Android 默认的硬件加速渲染引擎，应用的 View 绘制指令在主线程生成，由 RenderThread 提交给 GPU，最终经 SurfaceFlinger 合成到屏幕）、Flutter 的双线程模型（1.ui → 1.raster，不走 RenderThread）、以及 WebView 的 Chromium 管线（CrRendererMain 线程负责渲染）。除此之外还有 Jetpack Compose、游戏引擎、相机管线等。SmartPerfetto 的架构检测系统目前识别 24+ 种渲染管线，不同管线的 jank 分析需要查看不同的线程和指标——这也是为什么架构检测是分析的第一步。

卡顿的根因可能跨线程（主线程阻塞 → 原因在 RenderThread）、跨进程（App 等待 → system\_server 的 WindowManagerService 响应慢）、甚至跨硬件层（CPU 调度到小核 → 算力不足 → 帧超时）。

LLM 的训练数据中包含这些概念——它「知道」什么是 RenderThread，什么是 Binder，什么是 SurfaceFlinger。但面对一个具体的 trace，它缺乏将这些知识**按场景分阶段运用**的能力。比如分析滑动卡顿时，需要先检查帧级数据（哪些帧掉了、掉帧类型是什么），再针对占比最高的根因类型选择不同的深钻路径（App 侧阻塞走 blocking\_chain\_analysis，合成端延迟走 SurfaceFlinger 分析）。这种分步骤、有条件分支的分析流程，需要通过策略注入来引导。

### 可靠性：错误率在实际运行中偏高

即使解决了数据访问问题，直接让 LLM 产出性能分析结论仍然面临可靠性问题。在 SmartPerfetto 的实际运行中，我观察到几类典型的输出问题：

•**幻觉**：生成 trace 中不存在的数据或指标

•**遗漏**：漏掉关键检查项（比如分析启动性能时不检查 JIT 编译和类加载的影响）

•**浅层归因**：停在「主线程忙」的层面，不继续追踪是忙在 futex（锁竞争）、binder\_wait（跨进程等待）还是 GC pause

•**结论不一致**：同一份 trace 分析两次，得到不同的严重等级判定

后文第二部分会详细讨论这个问题——agentv3 上线 18 天后的质量审查显示，约 30% 的 Agent 结论包含不同程度的误判。

### SmartPerfetto 的分工设计

基于这四个问题，SmartPerfetto 的架构按以下方式分工：

```
LLM (Claude) 负责:              工具系统负责:├─ 理解用户意图                  ├─ SQL 精确查询 (trace_processor)├─ 制定分析计划                  ├─ 数值计算与统计 (Skill 内置)├─ 推理因果关系                  ├─ 渲染架构检测 (24+ 管线)├─ 跨领域关联分析                ├─ 分层数据提取 (L1-L4)├─ 生成结构化结论                ├─ Perfetto stdlib 查询└─ 自然语言交互                  └─ 数据摘要与压缩 (Artifact Store)连接层: MCP Protocol — 最多 20 个工具 (9 常驻 + 11 条件)策略层: 12 套场景策略 (.strategy.md)质量层: 3 层验证 + SQL 纠错学习
```

LLM 做推理和表达，工具做查询和计算。连接两者的是 MCP（Model Context Protocol，Anthropic 提出的工具调用协议）——Claude 通过标准 MCP 接口调用 trace\_processor 执行 SQL、调用 YAML Skill 做结构化分析、查询 Perfetto stdlib 模块。分析结果通过 SSE（Server-Sent Events）实时推送到 Perfetto UI 前端。

支撑这个分工的工程基础设施包括：场景路由（根据用户问题注入不同的分析策略）、数据压缩（控制返回给 LLM 的数据量）、质量验证（拦截 LLM 的领域误判）。后面几个部分展开讨论每个部分的设计过程。

下图是完整的系统架构，展示了从用户请求到分析结论的 4 个阶段：



* * *

## 第二部分：从 Workflow 到 Agent

### Workflow 和 Agent 的区别

Anthropic 在 2024 年 12 月发表的《Building Effective Agents》\[1\]（作者 Erik Schluntz、Barry Zhang）中，将 AI 系统分为两类：

•**Workflow（工作流）**：LLM 和工具通过预定义的代码路径进行编排。每一步做什么、下一步走哪里，都由开发者事先定义好。

•**Agent（智能体）**：LLM 动态主导自身流程和工具使用，自主决定如何完成任务。

这个区分的实际意义在于灵活性和可控性的权衡。Workflow 提供可预测性，适合步骤固定的任务；Agent 提供灵活性，适合需要根据中间数据调整方向的开放式问题。Andrew Ng 的描述很准确：不需要二元地判断一个系统是不是 Agent，而是把它看作不同程度的 Agent 化。SmartPerfetto 的 agentv2 和 agentv3 分别对应这个光谱的两端。

### 为什么性能分析需要 Agent 而不是 Pipeline

性能分析不是一个「给输入得输出」的固定流程，它是一个探索性的推理过程。以一个实际的滑动分析为例：

```
1. 先看总览 → 发现 47 帧卡顿，P90 = 23.5ms2. 根据总览决定方向 → 40% 卡在 APP 阶段，优先看 APP 侧3. 选代表帧深钻 → Frame #234 的 RenderThread 被 Binder 阻塞 23ms4. 形成假设 → "可能是 system_server 的 Binder 响应慢"5. 验证假设 → 查 Binder 对端的 thread_state，发现 system_server CPU 调度延迟6. 假设如果不成立 → 回退，换方向（比如改查 GPU 或 GC）7. 综合所有发现，形成结论
```

每一步决策都依赖前一步的结果——无法在分析开始前就确定所有步骤。Pipeline 无法处理「这个 trace 的问题可能在 GPU，也可能在 GC，需要根据中间数据动态选择下钻方向」这种需求。

SmartPerfetto 的设计是确定性和灵活性的混合：已知场景（滑动、启动、ANR 等）用 Strategy 文件约束必检项，保证不遗漏；但每个阶段内的具体查询和深钻方向由 Claude 自主决定。未匹配的场景则完全交给 Claude 自主探索。

### agentv2：一个典型的 Workflow

agentv2 使用 DeepSeek 作为后端，采用 Governance Pipeline 架构——通过 planner / executor / synthesizer 三阶段编排，本质上是预定义的多步骤工作流（历史 commit `6d80aefb`: "Replace the 13-step agentv2 governance pipeline with Claude-as-orchestrator"）。

这个架构在标准 Android 应用的滑动分析上工作得不错，但遇到非标准情况就出问题了。比如 Flutter 应用的 trace 里没有标准的 frame\_timeline 数据，管线拿到空结果后继续执行后续步骤，最终输出基于空数据的结论。

### agentv3：迁移到 Agent 架构

2026 年 3 月 2 日（commit `6d80aefb`），我切换到 Claude Agent SDK。Claude 接收工具定义和策略后，自主决定调用什么工具、按什么顺序、查什么数据。

一个 AI Agent 通常具备以下特征，agentv3 的实现对照如下：

特征

SmartPerfetto 中的实现

代码位置

自主性

Agent 自主决定调用哪个工具、按什么顺序

`claudeRuntime.ts`

推理能力

每次工具调用后追加 REASONING\_NUDGE 触发显式反思

`claudeMcpServer.ts:84`

工具使用

最多 20 个 MCP 工具调用 trace\_processor

9 常驻 + 11 条件

规划能力

submit\_plan + requirePlan() 门控

轻量模式关闭

反思能力

3 层 Verifier + Correction Prompt (max 2 轮)

`claudeVerifier.ts`

错误恢复

SQL 纠错学习 + 跨会话误判模式学习

跨文件

记忆

短期: Analysis Notes / Artifact Store；长期: Pattern Memory / SQL Fix Pairs

7 层记忆

```
agentv2 (Workflow): 固定管线 → 每步预定义 → 意外数据 = 错误结论agentv3 (Agent):    动态计划 → 自主调用工具 → 意外数据 = 调整计划
```

### 迁移后的 9 轮审查

从 3 月 2 日到 3 月 20 日，经历了 9 轮架构审查。其中影响最大的几轮：

轮次

日期

主要发现

Round 1

3/2

初始 SDK 集成后 12 个修复——SQL 知识库没接入 System Prompt，jank\_frame\_detail 中 CPU 核数硬编码为 4

Round 3

3/12

架构接线审计——12 处「实现了但没接上」的断连，比如验证管线在 0 findings 时被跳过

Round 7

3/15

Perfetto Stdlib 集成——预加载模块 4→22，Schema Index 708→761

Round 9

3/20

18 天真实 trace 后的生产质量审查——3 P0 + 4 P1 + 5 P2，催生了三层验证系统

### 冷启动 4 层联动 Bug

2026 年 3 月 19 日（commit `d5a1d7b3`），发现冷启动被错误分类为热启动。追踪后发现这是一个跨 4 层的联动问题：

```
Layer A (Perfetto Stdlib): bindApplication 的 ts 比 launchingActivity 早 ~98ms → 被过滤器排除Layer B (Skill 逻辑):      startup_events_in_range 的时间过滤与 Layer A 不兼容Layer C (10 个下游 Skill):  冗余的 startup_type 过滤条件 → 重分类后返回 0 行Layer D (质量门禁):         startup_analysis 的过滤规则和重分类逻辑不同步
```

修复规模：重写 10 个下游 Skill，新增 4 个启动分析 Skill。这个问题说明在 Skill 依赖链中，上游的一个字段语义错误会逐层放大。

* * *

## 第三部分：三个关键的工程决策

### 决策 1：Scene Classification — 从全量注入到按需加载

一开始我把 12 个场景（scrolling / startup / ANR / interaction / pipeline / game / memory 等）的分析策略全部塞进 System Prompt，总计 15000+ tokens。逻辑是：Claude 应该知道所有场景的分析方法，这样不管用户问什么都能应对。

实际运行后发现 Claude 会混淆不同场景的术语——在分析滑动时引用了启动阶段的指标，把 VSync 间隔（帧间时序）和 bindApplication（进程初始化）搞混。根本原因是不同场景的术语存在大量重叠，「帧」在滑动场景里是渲染帧，在启动场景里是首帧显示，12 套策略同时出现时 LLM 无法区分上下文。

解决方式是做场景分类，每次只注入一套策略：

```
// sceneClassifier.ts — 12 场景, <1ms 执行export function classifyScene(query: string): SceneType {  const scenes = getRegisteredScenes(); // 从 .strategy.md frontmatter 加载  const sorted = scenes    .filter(s => s.scene !== 'general')    .sort((a, b) => a.priority - b.priority); // ANR(1) → startup(2) → scrolling(3)  for (const scene of sorted) {    if (scene.compound_patterns.some(p => p.test(query))) return scene.scene;    if (scene.keywords.some(k => lower.includes(k))) return scene.scene;  }  return 'general';}
```

关键词和优先级声明在每个 `.strategy.md` 的 YAML frontmatter 中，不硬编码在代码里：

```
# scrolling.strategy.md---scene: scrollingpriority: 3keywords: [滑动, 掉帧, jank, scroll, fps, 帧率, 卡顿]compound_patterns:  - "(?:分析|看看|检查).*(?:滑动|滚动|列表)"---
```

添加新场景只需新建一个 `.strategy.md` 文件。DEV 模式下支持热加载，修改后刷新浏览器即可生效。

调整之后 System Prompt 从 ~15000 tokens 降到 ~4500 tokens，策略混淆的问题没有再出现。新增场景也从改代码变成了新建一个 `.md` 文件。

当多轮对话积累了较多上下文（分析笔记、历史计划、模式记忆等），System Prompt 可能重新超过 4500 token 预算。这时按优先级逐个丢弃低价值段落：SQL 知识库参考（Claude 可以用 `lookup_sql_schema` 工具按需查询）→ 历史分析经验 → 历史踩坑记录 → SQL 纠错对 → 子代理协作指引 → 历史分析计划。核心段落（角色、方法论、场景策略、输出格式）不会被丢弃。

### 决策 2：Artifact Store — 控制返回给 LLM 的数据量

决策 1 解决了 System Prompt 的膨胀问题。但即使场景策略只注入了一套，Agent 在执行过程中每次调用 Skill 仍然会产生大量数据（200+ 行帧数据），这些数据全部放进上下文带来新的问题。

早期版本把 Skill 执行结果（比如 200 行帧数据、487 行阻塞分析）完整返回给 Claude。每个 Skill 结果约 3000 tokens，一次分析调用 5-8 个 Skill，仅 Skill 数据就占 15000-24000 tokens。

token 成本是一方面，更意外的发现是：数据越多，Claude 的输出质量反而越差。面对 200 行帧数据时，它倾向于逐行描述（「帧 1 耗时 12.3ms，帧 2 耗时 15.7ms...」）而不是做模式归纳。我猜测原因是上下文中充斥大量数字后，LLM 的注意力被分散了。

解决方式是把 Skill 结果存入 ArtifactStore，返回给 Claude 的只有紧凑引用（~440 tokens）——行数、列名和摘要信息。需要详情时，Claude 通过 `fetch_artifact` 按需分页获取。完整数据通过独立的 SSE（Server-Sent Events）通道发送给前端渲染，不经过 LLM。

```
invoke_skill("scrolling_analysis") 执行结果:  ├── 前端: 全量 DataEnvelope (200 行) → SSE → UI 表格渲染  │         (DataEnvelope: 自描述的数据合约，包含列名、类型、交互动作，  │          前端根据 schema 自动渲染表格/图表，不需要针对每个 Skill 写代码)  └── Claude: 紧凑引用 (~440 tokens)              "scrolling_analysis 完成. 概要: 347 帧, jank 率 10.6%               art_1 (详情: fetch_artifact('art_1', 'rows', 0, 20))"
```

**fetch\_artifact 的三个粒度：**

级别

返回内容

约 tokens

`summary`

行数 + 列名 + 首行样本

~50

`rows`

分页数据 (offset/limit)

~200-500

`full`

完整原始数据

~3000

调整后每个 Skill 的 token 成本从 ~3000 降到 ~440，8 个 Skill 从 ~24000 降到 ~3520 tokens。Claude 的输出从逐行描述变成了模式归纳，前端仍然能拿到完整数据做表格渲染。

### 决策 3：三层验证 — 从真实误判中学到的

agentv3 上线 18 天后，我做了一次系统性的质量审查（2026 年 3 月 20 日，commit `da63eaf9`）。统计结果让我意外：约 30% 的 Agent 结论包含不同程度的误判。

以下是实际遇到的误判案例：

```
[案例 1] Agent 将 VSync 对齐偏移标记为 CRITICAL实际情况: 现代高刷设备（90Hz/120Hz/144Hz）的 VSync 间隔本身就不是完全固定的，存在正常的微小偏移（±0.5ms 量级）。Agent 把这种正常偏移当成了异常[案例 2] Agent 将 Buffer Stuffing 帧计入掉帧统计实际情况: Buffer Stuffing 表示 App 按时完成了渲染，但 BufferQueue 队列满导致生产侧背压。这不是 App 逻辑问题，不应直接算作 App 侧掉帧。SmartPerfetto 通过双信号检测处理：默认排除，但如果实际呈现间隔 > 1.5x VSync则仍计入感知掉帧[案例 3] Agent 将单帧耗时异常标记为 CRITICAL实际情况: 孤立的单帧异常不构成模式，需要确认是否重复出现[案例 4] Agent 将主线程 Sleeping 占 35% (469ms) 标记为 MEDIUM实际情况: 在启动总时长中，469ms 的主线程睡眠占比已经很高，应标记为 HIGH
```

这些误判有一个共同特点：它们不是逻辑错误，而是 **领域经验的缺失**。高刷设备上 VSync 微小偏移是正常的、Buffer Stuffing 的延迟发生在管线队列层面而非 App 逻辑、单帧异常不构成模式——这些判断依赖对 Android 图形栈的深入理解，Claude 的训练数据对这些细节覆盖不足。

认识到这一点后，我建立了三层递进验证：

```
Layer 1: 启发式检查 (无 LLM 调用)  — 正则匹配已知误判模式（VSync 偏移标 CRITICAL、Buffer Stuffing 算掉帧、单帧标 CRITICAL）Layer 2: Plan 遵从检查 (无 LLM 调用)  — 对照 submit_plan 的步骤，检查结论是否覆盖了所有计划阶段Layer 3: 独立模型审查 (使用 Haiku)  — 用不同模型检查每个发现是否有数据证据支持，因果链是否完整
```

验证发现严重问题时，生成 Correction Prompt 让 Claude 修正结论（最多 2 轮）。

**跨会话学习：** 确认的误判模式被持久化到 `logs/learned_misdiagnosis_patterns.json`，下次分析时自动注入 System Prompt。例如系统学到了：

```
{  "keywords": ["R008", "TTID", "超出", "LOW"],  "message": "TTID 超出标记为 LOW，但 TTID(1912ms) 超出 dur_ms(1338ms) 43%，              应标记为 MEDIUM 或更高",  "occurrences": 1}
```

> 注：学习到的误判模式不会立即生效。代码中要求 `occurrences >= 2` 才会进入有效模式集——首次记录只是标记，同一模式第二次出现时才会注入到后续分析的 System Prompt 中，避免孤立事件造成过度矫正。

* * *

## 第四部分：为什么不用标准的 Skill 系统？

### 从 SOP 到 YAML Skill 的设计选择

做性能分析的团队一般都有自己的 SOP（标准操作流程）：滑动卡顿怎么查、启动慢怎么分析、ANR 怎么定位。SOP 通常是一份文档或检查清单，有经验的工程师照着做，新人跟着学。

Anthropic 的 Claude Code 有一套 Skills 系统，本质上是参数化的 Prompt 模板——注入上下文后提交给 Agent 执行。一个自然的想法是把性能分析 SOP 写成这种 Prompt 模板，让 Claude 按 SOP 执行。

我一开始也走了这条路。给 Claude 的 Prompt 是：「查询 frame\_timeline 表，找出 jank 帧，分析主线程在 jank 帧期间的状态分布。」

Claude 理解意图没问题，但每次生成的 SQL 不一样。有时候 JOIN 路径写对了（`slice → thread_track → thread`），有时候直接写 `slice.utid`——这个列不存在。查出来的结果格式也不固定，有时候 3 列有时候 5 列，前端渲染没法做。

原因很简单：SOP 是给人看的，工程师看到「查 frame\_timeline」知道具体该写什么 SQL。LLM 对 Perfetto 的 SQL schema 理解不完整（这些 schema 在训练数据中覆盖有限），每次从 SOP 文本到 SQL 的翻译过程都会引入方差。

SmartPerfetto 的 YAML Skill 采用了不同的思路——不是 Prompt 模板，而是声明式的 SQL 执行单元：

> [内容过长，已截断]
