# Loopjacking in A2A Implementations: Hijacking Human-in-the-Loop Approvals

> Source: <https://adithyanak.com/loopjacking-in-a2a-implementations/>
> Author: Adithyan Arun Kumar (FN-10 / Agentic Security Research)
> Published: 2026-09-21 · Evidence archive: <https://github.com/adithyan-ak/loopjacking/blob/main/EVIDENCE.md>

## 摘要（基于原文）

**Loopjacking**：实现只校验"这个 A2A Task 被批准过"，而不校验"被批准的到底是哪个操作"，导致一个针对操作 A 的人类批准决定被挪用去放行实质不同的操作 B。

受控实验（LangGraph Agent Server）：审批角色收到 `mock_wire_transfer(20, approved-vendor)` 的人类在环路（human-in-the-loop）中断请求；另一个 maker 角色能更新挂起的线程但无法批准或执行受保护转账。maker 通过服务器的 A2A 路由再发一条消息，把挂起调用替换成 `mock_wire_transfer(2000, attacker-sink)`。审批角色提交的还是"转 20"的决定，模拟账本里落账的却是"以审批者权限转出 2000"。

作者把根因拆到 A2A 的任务模型层：Task ID 回答的是"这条消息关于哪份工作"，不回答"人类到底批准了哪个具体工具调用"。任务承载的操作 A 展示给审批者、记下决定 `D_A` 之后，后续消息可以在 Task ID 不变的前提下把挂起操作换成 B。只查"Task 被批准"的实现会把 `D_A` 花在 B 上；只有"对比当前可执行操作与 `D_A` 绑定的那个操作"的实现才会拒绝或重新询问。这里存在两个独立记录：协调记录（Task）和批准绑定记录（被授权的精确操作）——把两者混用就是漏洞。文中还沿 A2A 的任务模型、授权指引和已发布的 Agent Server 代码路径做了系统分析。

**实验边界**（作者明示）：审批角色是脚本化的，测的是产品的"批准绑定"而非真人是否会在 UI 里注意到变化；用内存服务器、合成身份、确定性本地模型、无害账本；请求、决定、控制项和被测版本都留有公开证据存档。

## Field note

对任何实现 human-in-the-loop 审批的 agent 框架（不限于 A2A）都是通用教训：审批对象必须是"操作的完整语义表示"（工具名+参数+目标资源）并与之绑定到执行点，而不是一个可变会话对象的 ID。落地检查项：批准后执行前重新比对操作哈希；收到会更新挂起操作的新消息时使旧批准失效；审批 UI 与执行审计用同一份操作表示。与本周监控/轨迹类论文（EvasionBench、trace tampering）互补：那两篇讲 agent 主动绕过，这篇讲审批机制的绑定缺陷——防线两侧都要补。
