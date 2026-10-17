# (When) Should a Software Factory be Lights-off? CRBugBench：代码评审代理抓 bug 能力基准

> Source: https://arxiv.org/abs/2610.13668
> Content fetched: 2026-10-17T12:25:00+08:00
> Grounding: opencli arxiv paper (HTTP 429) -> arxiv.org/abs page via opencli web read

## 一句话
CRBugBench 用 1800 个人工核验的 bug 评测评审代理：最强组合在 top-5 评论中命中 71.9%，五个月内从 47.7% 大幅提升，但私有仓库和需要非局部推理的 bug 仍是短板

## 关键信息
- arXiv ID: 2610.13668
- English title: (When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection
- Authors: Chenyang Yang, Hao He, Ti-Chung Cheng, Jenna Butler, Emerson Murphy-Hill, Carmen Badea, Christian Bird
- Submitted/Published: 2026-10-09
- Subjects: cs.SE
- PDF: https://arxiv.org/pdf/2610.13668v1
- Tags: code-review, coding-agents, benchmark, bug-detection
- Quality score: 4

## 中文摘要
为检验「无人值守软件工厂」的可行性，作者构建 CRBugBench：从 98 个开源仓库的提交历史挖掘人工核验过的 bug，并配对其引入 PR，形成 1000 个开源评审任务，另有 800 个来自某大型企业私有仓库的任务。SOTA 评审代理表现不差：claude-opus-5 + copilot-cli 在 top-5 评论中命中 71.9% 的 bug，比五个月前 opus-4.6 的 47.7% 明显提升；但在复杂变更、需要跨文件非局部推理的 bug 以及缺乏项目上下文的私有仓库上性能骤降。提示词层面的探索引导可再加约 5.8%（成本 +10%）。论文据此给出落地建议：按 PR 复杂度分配评审力度、按项目优先级引导代理、补充仓库知识、按 PR 特征分派模型，并随模型演进持续监控质量。

## English Summary
As coding agents accelerate code generation, the authors ask how close we are to a 'lights-off' software factory with little human supervision. They build CRBugBench: a data pipeline mines human-verified bugs from repository history and pairs each bug with its introducing PR, yielding 1,000 review tasks across 98 open-source GitHub repositories plus 800 tasks from proprietary industry repositories at one large company. The best agent (claude-opus-5 with copilot-cli) catches 71.9% of bugs within its top-5 comments, up from 47.7% for opus-4.6 five months earlier. Agents remain weaker on complex changes and bugs requiring non-local reasoning, with sharp drops on proprietary repositories where project context matters. Scaling compute helps most through prompt changes: exploration-nudging prompts gain up to 5.8% at 10% higher cost. The paper derives concrete adoption guidance: scale review effort to PR complexity, steer agents by project priorities, supply repository knowledge, dispatch models by PR characteristics, and monitor quality as models evolve.

## Why it matters
它把「评审代理能不能替代人」从直觉问题变成可复现的基准：开源与私有双分布、bug 与引入 PR 配对成真实评审任务。结果显示模型迭代很快但项目上下文是硬瓶颈，对 agent 代码工作流的选型、预算分配和人机分工边界都有直接参考价值。

## arXiv Abstract
With the advances of coding agents, software developers are spending more time reviewing code than writing code. As human review velocity falls behind agentic code generation, it is tempting to build automated review agents towards a future of "lights-off" software factory with little to no human supervision. To assess the practicality of such a fully autonomous software factory, we construct CRBugBench, a new benchmark that evaluates whether review agents detect human-verified bugs. We build a data pipeline that mines bugs from repository history, and pair each bug with its introducing PR to form a review task. CRBugBench consists of 1,000 review tasks across 98 open-source GitHub repositories, and 800 additional tasks from proprietary industry repositories at one large company. We then use the benchmark to study agent review quality: We found that SOTA review agents do well: the best (claude-opus-5 with copilot-cli) catches 71.9% of bugs within its top-5 comments, up from 47.7% (opus-4.6) in five months of model evolution. Yet agents remain less effective on complex changes and bugs requiring non-local reasoning, with sharp performance drops on proprietary industry repositories where project context is more often needed. To improve bug detection, we found scaling compute helps most through prompt changes: exploration-nudging prompts gain up to 5.8% performance at 10% higher cost. From these findings, we derive concrete guidance for developers to adopt review agents - scaling review effort to PR complexity, steering agents by project priorities, supplying repository knowledge, dispatching models by PR characteristics, and monitoring quality as models evolve.

## Source Metadata
```json
{
  "id": "2610.13668",
  "title": "(When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection",
  "authors": "Chenyang Yang, Hao He, Ti-Chung Cheng, Jenna Butler, Emerson Murphy-Hill, Carmen Badea, Christian Bird",
  "abstract": "With the advances of coding agents, software developers are spending more time reviewing code than writing code. As human review velocity falls behind agentic code generation, it is tempting to build automated review agents towards a future of \"lights-off\" software factory with little to no human supervision. To assess the practicality of such a fully autonomous software factory, we construct CRBugBench, a new benchmark that evaluates whether review agents detect human-verified bugs. We build a data pipeline that mines bugs from repository history, and pair each bug with its introducing PR to form a review task. CRBugBench consists of 1,000 review tasks across 98 open-source GitHub repositories, and 800 additional tasks from proprietary industry repositories at one large company. We then use the benchmark to study agent review quality: We found that SOTA review agents do well: the best (claude-opus-5 with copilot-cli) catches 71.9% of bugs within its top-5 comments, up from 47.7% (opus-4.6) in five months of model evolution. Yet agents remain less effective on complex changes and bugs requiring non-local reasoning, with sharp performance drops on proprietary industry repositories where project context is more often needed. To improve bug detection, we found scaling compute helps most through prompt changes: exploration-nudging prompts gain up to 5.8% performance at 10% higher cost. From these findings, we derive concrete guidance for developers to adopt review agents - scaling review effort to PR complexity, steering agents by project priorities, supplying repository knowledge, dispatching models by PR characteristics, and monitoring quality as models evolve.",
  "published": "2026-10-09",
  "updated": "2026-10-09",
  "primary_category": "cs.SE",
  "categories": "cs.SE",
  "comment": "",
  "pdf": "https://arxiv.org/pdf/2610.13668v1",
  "url": "https://arxiv.org/abs/2610.13668"
}
```
