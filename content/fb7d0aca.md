# Sol Advisor: Codex-native architect orchestration with Luna and Terra implementation lanes

- **ID**: fb7d0aca
- **原文链接**: https://github.com/DannyMac180/sol-advisor
- **作者**: DannyMac180 (GitHub)
- **日期**: 2026-08-01
- **分类**: agents
- **来源类型**: github
- **标签**: codex, agents, orchestration, multi-agent, plugin, code-review
- **质量评分**: 4/5
- **抓取时间**: 2026-08-23T15:45:00Z

---

## 中文导读

Codex-only 的工作流插件，把“能力路由”写进交付流程：主会话 Sol（GPT-5.6 Sol/High）拥有架构、任务拆解、路由选择、验证与验收；solo 是默认路由，只在确实改善交付时才启用一个辅助角色——delegate（完整规格交给单一实现者：Luna/Max 做有界工作，Terra/High 做判断密集或高风险工作）、audit（root 自己实现，由全新只读 Sol/High 复审）、full（显式高风险例外：一个实现者 + root 验证 + 全新 Sol 复审）。Sol 必须在第一个 task 工具调用前声明 SELECTIVE ROUTE 与风险理由，只能因新观察到的风险升级、绝不静默降级；root 检查完整 diff、重跑检查；复审结论只有 ship/fix-first/rethink，任何 fix 都要重新过审。

## 为什么值得关注

把多模型协作里最容易糊掉的责任边界写成硬约束：路由必须先声明理由、验收权永远在主会话、辅助工作只替代不复制 root 工作；对照“agent 套 agent 互相扯皮”的常见失败模式，这份设计（默认 solo + 至多一个辅助 + 强制复审）是可直接抄的模板。

## 关键信息

- 仓库：DannyMac180/sol-advisor（2026-08-01 创建，2315 stars @2026-08-23 实测）
- 依赖：Codex CLI / ChatGPT 桌面端（插件启用）、GPT-5.6 Sol/High；Luna/Max 或 Terra/High 仅在所选路由委派时需要
- 四路由：solo（默认）/ delegate / audit / full（显式例外）
- SELECTIVE ROUTE：首个 task 工具调用前声明模式与风险理由；只升不降
- 复审结论：ship / fix-first / rethink；任何 fix 必须重新过审
- 安装：codex plugin marketplace add DannyMac180/sol-advisor；安装器 fail-closed

## English Summary

A Codex-only plugin for capability-routed delivery: the Sol/High primary session owns planning, routing, verification and acceptance. Solo is the default; one auxiliary at most — delegate (Luna/Max bounded work, Terra/High judgment-heavy), audit (fresh read-only Sol review), full (explicit exception with implementer + root verification + fresh review). A SELECTIVE ROUTE declaration with risk rationale is required before the first task tool call; escalation only on newly observed risk, never silent downgrade. Reviews return ship/fix-first/rethink; any fix requires re-review. Fail-closed installer.

## 原文要点摘录

> Sol Advisor is a Codex-only workflow for capability-routed software delivery. You bring the goal and constraints; Sol owns the plan, implementation or delegation, verification, and acceptance.

> Solo is the default. One auxiliary is the default maximum; full is the explicit exception.

> a fresh Sol / High reviewer returns ship, fix-first, or rethink; any fix requires a new review.

## Obsidian Notes

- 内容由 opencli web read 抓取 GitHub README 生成（2026-08-23）。
- 候选来源：X 书签消化 2026-08-23（@Xudong07452910 推荐，评分 8.0）；路由表、SELECTIVE ROUTE、复审规则均锚定 README 原文，stars 数为 GitHub API 当日实测。
