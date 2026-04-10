# 编排框架

Orchestration — 6 条活跃资源

### [Launching Claude Managed Agents](https://x.com/RLanceMartin/status/2041927992986009773) 
by @RLanceMartin (2026-04-06) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**Anthropic 官方托管 Agent 基础设施，大脑/手/记忆三层解耦架构**

Anthropic 发布 Claude Managed Agents：预构建的可配置 Agent 运行底座，运行在托管基础设施上。三大核心概念：Agent（版本化配置）、Environment（沙盒模板）、Session（有状态运行）。四种用法：事件触发、定时、即发即忘、长时间任务。架构上将"大脑"（Claude+调度框架）、"手"（沙盒工具）、"记忆"（会话日志）解耦，支持独立故障恢复。
 `claude` `managed-agents` `anthropic` `agent-sdk` `infrastructure` `cloud-agent`

---
### [Anthropic 今天发了一个新产品，可能会让一批做 AI 智能体基础设施的团队失业](https://x.com/dotey/status/2042017036931305667) 
by @dotey (2026-04-06) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**中文深度解析 Claude Managed Agents 的产品定位、架构设计与企业案例**

中文深度分析 Claude Managed Agents。与 Claude Code 的区别：Code 跑在本地给个人用，Managed Agents 跑在云端给企业用，24 小时不间断。典型用法：事件触发型（Sentry 自动修 bug）、定时型（每日简报）、即发即忘型（Slack 派活）、长时间任务。技术架构将大脑/手/记忆解耦。案例：Notion、Sentry、Atlassian、Rakuten 等已接入。Anthropic 年化收入突破 300 亿美元。
 `claude` `managed-agents` `anthropic` `enterprise` `agent-infrastructure`

---
### [DeerFlow 2.0: ByteDance 开源超级 Agent 运行底座](https://github.com/bytedance/deer-flow) 
by @Bytedance (2026-02-27) | ⭐⭐⭐⭐ 4/5 | 🌐

**字节跳动的超级 Agent 底座，LangGraph 重写，支持子 Agent 并行编排**

字节跳动开源 DeerFlow 2.0，基于 LangGraph 和 LangChain 完全重写的超级 Agent 运行底座。可编排子 Agent、记忆、工具与沙箱以完成长链路多步骤任务。核心能力：任务分解（主 Agent 并行派发子 Agent）、中间结果汇总、跨会话持久化记忆。默认提供文件系统、技能、执行环境。
 `deer-flow` `bytedance` `langgraph` `langchain` `super-agent` `sub-agent`

---
### [How to set up OpenClaw Agents that actually get better Over Time](https://x.com/Saboo_Shubham_/status/2027463195150131572) 
by @Shubham Saboo (2026-02-28) | ⭐⭐⭐⭐ 4/5 | 🌐

**OpenClaw Agent 自改进的 40 天实战：靠 markdown 文件栈而非调 prompt**

40 天实践：Agent 变聪明靠的不是调 prompt 或换模型，而是持续对话反馈让它们自己写下来。三层操作系统：内容 Agent 学会了作者的声音、研究 Agent 每天交付 7 个值得读的故事、8 个 Agent 24/7 运行。核心是越来越丰富的 markdown 文件栈。同一模型第 1 天和第 40 天输出质量天差地别。
 `openclaw` `memory` `self-improvement` `agent-stack` `markdown`

---
### [OpenClaw Memory 终极指南](https://x.com/lijiuer92/status/2025678747509391664) 
by @李韭二 (2026-02-23) | ⭐⭐⭐ 3/5 | 🇨🇳

**OpenClaw 记忆系统实践指南，覆盖失忆、可发现性与长期维护**

围绕 Agent 失忆、记忆可发现性、长期上下文维护与工程化落地展开，强调通过结构化记忆机制降低重复输入和推理成本。适合作为 OpenClaw/Agent 记忆系统设计的实践参考。内容为摘要归档，待补全全文。
 `openclaw` `memory` `agent` `long-term-context`

---
### [全面解析：如何部署 Conway Agent，开启链上 AI 生存游戏](https://x.com/JXiaoLoong/status/2024376180707905816) 
by @0xJA (2026-02-24) | ⭐⭐⭐ 3/5 | 🇨🇳

**链上自主 AI Agent 的部署与运行指南，一体化沙盒平台**

介绍 Conway Agent 部署方法。Conway 把服务器（Conway Cloud/Sandbox）、AI 推理（Conway Compute）和域名封装到统一平台，使用 Credit 计费。定位为完全自主运行的 AI 系统。内容较简短，为归档节选。
 `conway` `on-chain-ai` `agent-deployment` `sandbox`

---