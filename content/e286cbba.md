# DEIA: Evidence-Grounded Crash Repair with Change-Aware Test Design for HarmonyOS ArkTS

- **ID**: e286cbba
- **原文链接**: https://arxiv.org/abs/2611.14064
- **作者**: Xuhui Lu, Zhihao Liu, Xiaoke Fang, Yuhuan Fan, Yanzhe Tang, Xiaohui Wan, Xiaoyu Wu, Zheng Zheng
- **日期**: 2026-11-10
- **更新**: N/A
- **分类**: coding
- **来源类型**: paper
- **标签**: arxiv, crash-repair, harmonyos, llm, testing, mobile
- **质量评分**: 4/5
- **抓取时间**: 2026-11-13T15:45:09+00:00

---

## 中文导读

DEIA 面向 HarmonyOS ArkTS 应用 crash 自动修复，难点定位为证明改动与上报失败相关、改完可构建可运行且不破坏既有行为。流程：有界源码证据包→LLM 提出带内容锚点的修改→确定性 writer 落补丁并验证；F2P 义务从上报故障推导，P2P 从补丁影响面推导，ledger 记录补丁、义务与开销。30 任务对比 OpenHands：首增行命中 25/29（86.2%）对 19/29（65.5%），token −81.5%、调用 −60.8%、候选生成时间 −34.9%；作者自曝 58 条 P2P 义务只真执行 2 条，行为保持尚未证明。代码与数据集公开。

## 为什么值得关注

移动端 crash 自动修复的结构化答案：证据包+锚点编辑+确定性写入省八成 token，Android 侧还没有对标的公开工作，结构可直接移植。

中文导读与价值判断锚定在条目已有摘要与抓取到的原文/摘要、作者、日期与分类信息上；未补充源材料之外的实验细节。

## 关键信息

- 标题：DEIA: Evidence-Grounded Crash Repair with Change-Aware Test Design for HarmonyOS ArkTS
- 作者：Xuhui Lu, Zhihao Liu, Xiaoke Fang, Yuhuan Fan, Yanzhe Tang, Xiaohui Wan, Xiaoyu Wu, Zheng Zheng
- 链接：https://arxiv.org/abs/2611.14064
- 发布时间：2026-11-10
- 关联标签：arxiv, crash-repair, harmonyos, llm, testing, mobile

## English Summary

DEIA is an evidence-grounded workflow for HarmonyOS crash repair: it builds a bounded source-evidence package, uses an LLM to propose content-anchored edits, and relies on a deterministic writer to materialize and check the patch. Fail-to-pass obligations derive from the reported fault, pass-to-pass obligations from the patch's potential impact, and a stage-level ledger links patches, obligations, runtime observations and generation cost. On 30 repair tasks from 24 apps vs an OpenHands workflow (29 matched), first-added-line location hits 25/29 (86.2%) vs 19/29 (65.5%), with 81.5% fewer tokens, 60.8% fewer model calls, 34.9% less generation time; only 2 of 58 P2P obligations were executed, so behavior preservation remains unestablished. Code and dataset are public.

## 原文摘录 / Evidence Excerpts

Mobile crash repair requires more than identifying a source edit. Developers must establish how the edit relates to the reported failure and whether the modified application can be built, launched, and exercised without disrupting valid behavior. ... DEIA constructs a bounded source-evidence package, uses a large language model to propose content-anchored edits, and relies on a deterministic writer to materialize and check the patch.

We evaluate DEIA on 30 repair tasks from 24 HarmonyOS applications and compare it with an OpenHands-based workflow on 29 matched tasks. DEIA's first-added-line location exactly matches the curated reference in 25/29 tasks (86.2%), compared with 19/29 (65.5%) for OpenHands ... DEIA also uses 81.5% fewer tokens, makes 60.8% fewer model calls, and takes 34.9% less candidate-generation time on average. Only two of the 58 behavior-specific P2P obligations were executed ... comprehensive behavior preservation therefore remains unestablished.

Comments: Code and dataset: https://gitcode.com/harmony-dfx-detection/answer_B/tree/DEIA

---

## 证据来源

opencli arxiv paper 2611.14064 -f json 直接抓取元数据与摘要（2026-11-13）；cs.SE，2026-11-10 提交。数字逐条对照摘要原文断言命中（论文流水线 2026-11-13 记录）。
