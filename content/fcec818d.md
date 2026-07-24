# Beyond Fail-to-Pass: Iterative Hardening of Co-Generated Bug Reproduction Tests and Fixes

- **ID**: fcec818d
- **原文链接**: https://arxiv.org/abs/2607.19843
- **PDF**: https://arxiv.org/pdf/2607.19843
- **作者**: Yuhao Tan, Zhibang Yang, Fangkai Yang, Yuan Yao, Yu Kang, Lu Wang, Pu Zhao, Xin Zhang, Xiaoxing Ma, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **日期**: 2026-07-22
- **分类**: cs.SE, cs.AI
- **标签**: automated-program-repair, swe-bench, bug-reproduction-tests, coding-agents, evaluation
- **质量评分**: 5/5
- **抓取时间**: 2026-07-24T12:19:08+08:00

---

## 中文解读

这篇论文直接挑战 coding agent/APR 评测里常用的 fail-to-pass 标准：一个 BRT 即使能在 buggy 版本失败golden fix 通过，也可能过于宽松，仍放行错误补丁作者区分 rigorous/lax BRT，指出共生成测试和修复时会出现 test-fix error coupling，并提出 CoHarden：先生成测试，再用幸存 mutation patch 反复硬化测试和修复摘要报告在 SWE-bench Verified 上达到 69.4% Resolved78.9% FP

## 为什么值得关注

- 指出 coding agent / 自动修复评测中“测试从失败到通过”并不等价于高质量修复，为更严格的 bug reproduction tests 提供了方法。

## English Summary

The paper argues that fail-to-pass is not enough for bug reproduction tests in automated program repair: some tests fail on buggy code and pass on the golden fix but are lax enough to admit plausible wrong patches. It separates rigorous and lax BRTs, identifies testfix error coupling in co-generation, and proposes CoHarden, which iteratively hardens tests and fixes against surviving mutation patches. The abstract reports 69.4% Resolved and 78.9% FP on SWE-bench Verified.

## Abstract

Large language models (LLMs) have made automated program repair (APR) increasingly practical for real-world bugs, but repairing directly from bug reports remains underconstrained. Bug reproduction tests (BRTs) help close this gap by turning a bug report into an executable, bug-specific signal that can guide repair and validate candidate patches. Existing work has therefore studied BRT generation as a core subproblem in APR and mainly evaluates a generated BRT using the fail-to-pass (F->P) criterion, which requires the test to fail on the buggy code but pass on the golden fix. We show that F->P alone is insufficient when the goal of a BRT is to improve downstream repair. In particular, some F->P BRTs are lax, reproducing the observed symptom yet still admitting plausible-but-incorrect patches. We formalize this missing quality dimension by separating F->P BRTs into rigorous and lax ones, and show empirically that only the former consistently improve repair success. We further find that co-generation introduces test--fix error coupling, where the in-trajectory fail-to-pass (F->P) check can pass even when both the generated patch and generated test are wrong. Based on these findings, we propose CoHarden, a co-generation framework that uses the Lax signal as an in-loop convergence criterion. CoHarden first generates a test before any fix, then iteratively hardens the test and fix against surviving mutation patches until the generated test no longer admits Lax regressions. Experiments show that CoHarden reaches 69.4% Resolved and 78.9% F->P on SWE-bench Verified, outperforming the strongest fix-only and cogeneration baselines by +9.6 and +7.9 percentage points in Resolved, respectively, with consistent gains across LLM backbones and benchmarks.

## Metadata

- arXiv ID: 2607.19843
- Primary category: cs.SE
- Categories: cs.SE, cs.AI
- Source: OpenCLI arXiv metadata
