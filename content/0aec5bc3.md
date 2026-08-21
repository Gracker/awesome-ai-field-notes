# Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems

- arXiv: [2608.19140](https://arxiv.org/abs/2608.19140)
- Authors: George Andrikopoulos
- Published: 2026-08-19; categories: cs.AI, cs.CY, cs.LG, cs.SE

## Abstract

Frontier language models are compared, marketed, and benchmarked on capability -- what their best or average output can achieve. I argue this measures the wrong axis. The models have saturated accuracy: their mean output lands on the target. What now separates one system from another in practice is precision: how tightly concentrated their outputs are around that target across repeated, identical requests. Borrowing the marksman's distinction, capability is where the average shot lands; reliability is the size of the group. I make three claims. First, precision, not capability, is the frontier differentiator between systems, and benchmark culture systematically fails to measure it, reporting central tendency rather than spread. Second, precision is measurable, cheaply and without circularity, by running a fixed suite of deterministically scored tasks many times at fixed temperature and computing the per-task consistency of outcomes -- no model-in-the-loop grader required. Third, the measurement is not merely descriptive but decision-guiding: it separates consistent failures (a tight group off-centre, correctable by the operating discipline of Paper 1 -- a sight adjustment) from scattered failures (a wide group, correctable only by changing the model or its sampling -- a rifle problem). I define a grouping metric, specify a harness, and show how tracking a human-AI pair's grouping over time yields the compounding signal that Paper 1's field study requires. A first real run, since replicated, illustrates both the method and its most important limit: one measured gap was closed completely by a single rule (0/5 -> 5/5), while a suite of tasks authored from the rules themselves found no value, because a frontier model already embodies explicit good practice -- establishing that a discipline's worth is found by measurement on real work, not constructed from its own rulebook.

## Why it matters (AAIF scan)

立场文章：前沿模型的准确率（平均输出命中目标）已饱和，真正拉开系统差距的是精度：相同请求重复执行的输出分散度——射击的弹群而非矄准。三个主张：精度而非能力是前沿差异化因素，而基准文化只报中央趋势不报离敦；精度可以不用模型评分器低成本测量（固定温度多次跑确定性任务算一致性）；指标能指导决策，区分规则可修的一致性失败与需换模型/采样的分散失败。给出 grouping 度量、测试 harness 与一次已复现的实测（一条规则把 0/5 修到 5/5，而由规则改写的任务对前沿模型无增益）。

> Source: https://arxiv.org/abs/2608.19140