# GRH for Dirichlet L-functions, in Lean 4 (shorter Anthropic-collaboration edition)

- **ID**: f63f4cad
- **原文链接**: https://github.com/lsernau/grh-lean
- **PDF**: N/A
- **作者**: lsernau（与 Anthropic 同事及 Claude 合作）
- **日期**: README 无日期；条目 added 2026-11-27
- **更新**: N/A
- **分类**: industry
- **来源类型**: github
- **标签**: lean, mathematics, anthropic, formal-verification
- **质量评分**: 4/5
- **抓取时间**: 2026-11-27T12:21:42+00:00

---

## 中文导读

lsernau 与 Anthropic 同事及 Claude 合作发布的 Lean 4 研究工件：基于 Levent Alpöge 的证明（alpo.ge/remark.pdf），形式化黎曼假设与 Dirichlet L 函数上的广义黎曼假设，构建于 Mathlib，只依赖 propext、Classical.choice、Quot.sound 三个公理。两个版本：grh/ 可读版约 30 万行（从 grh/GUIDE.md 读起），grh-compact/ 同一组五个定理约 7.6 万行，各自是独立 Lake 项目。构建需 Lean v4.35.0 与 Mathlib commit 56a00585，12 核 24 GB 内存约一至两小时。状态声明克制：仅通过机器检查、无数学家通读、不附论文；仓库不维护、不收贡献。Apache 2.0，版权归 Anthropic PBC。

## 为什么值得关注

**一句话**: Anthropic-collab Lean 4 proof of GRH: 76k-line compact edition, machine-checked only

这是 2026-11 AI 辅助数学证明浪潮的又一数据点：机器检查保证了证明「存在」，但可读版 30 万行、紧凑版 7.6 万行的体量说明人类通读与同行评议仍是缺口。其工程形态——Mathlib 底座、公理白名单、双版本组织——对 AI 形式化证明项目是现成模板。

## 关键信息

- 证明对象：黎曼假设 + Dirichlet L 函数广义黎曼假设（同一组五个定理）
- 基础：Levent Alpöge 的证明；与 Anthropic 同事及 Claude 合作产出
- 公理：propext / Classical.choice / Quot.sound
- 版本：可读版约 300,000 行；紧凑版约 76,000 行
- 构建：Lean v4.35.0 + Mathlib@56a00585；12 核 24 GB 约一至两小时
- 状态：仅机器检查通过，无数学家通读，无论文；不维护不收贡献
- 许可：Apache 2.0，Copyright 2026 Anthropic, PBC

## English README Notes

A Lean 4 proof of the Riemann Hypothesis and of the Generalized Riemann Hypothesis for Dirichlet L-functions, built on Mathlib and using only the axioms propext, Classical.choice and Quot.sound. The proof is based on Levent Alpoge's, with Claude. This repository is a shorter version, produced in collaboration with colleagues at Anthropic, and Claude. Two editions: grh/ (readable edition, about 300,000 lines) and grh-compact/ (the same five theorems, about 76,000 lines). Build needs Lean v4.35.0 and Mathlib at commit 56a00585. Status: the proof has passed machine checks only; no mathematician has read it through, and no paper comes with it. License: Apache 2.0, Copyright 2026 Anthropic, PBC.

### Entry Summary (from entries.json)

lsernau, in collaboration with colleagues at Anthropic and Claude, released a Lean 4 research artifact proving the Riemann Hypothesis and the Generalized Riemann Hypothesis for Dirichlet L-functions, based on Levent Alpoge's proof, built on Mathlib and using only the axioms propext, Classical.choice, and Quot.sound. Two editions: a readable ~300,000-line version and a compact ~76,000-line version proving the same five theorems. Build needs Lean v4.35.0 plus Mathlib at 56a00585; one to two hours on 12 cores / 24 GB. The status note is deliberately restrained: machine-checked only, no mathematician has read it through, no paper accompanies it, unmaintained and not accepting contributions. Apache 2.0, Copyright 2026 Anthropic, PBC. Part of the same November 2026 wave of AI-assisted proofs as OpenAI's math repository.

## Obsidian Notes

- `opencli web read` 被目标站点拒绝（Navigation rejected），README 改经 raw.githubusercontent.com 直取（2026-11-27 UTC）。内容锚定仓库 README 与条目既有摘要。
- 本文件由 aaif-intake-pipeline `content-fetcher` 模式生成；entries.json 未改动，仅回填内容页。
