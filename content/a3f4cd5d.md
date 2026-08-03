# HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks

- **ID**: a3f4cd5d
- **Source**: arXiv
- **Original URL**: https://arxiv.org/abs/2604.09937
- **PDF**: https://arxiv.org/pdf/2604.09937v1
- **Authors**: Suhana Bedi, Ryan Welch, Ethan Steinberg, Michael Wornow, Taeil Matthew Kim, Haroun Ahmed, Peter Sterling, Bravim Purohit, Qurat Akram, Angelic Acosta, Esther Nubla, Pritika Sharma, Michael A. Pfeffer, Sanmi Koyejo, Nigam H. Shah
- **Published**: 2026-04-10
- **Categories**: cs.AI
- **Comments**: 24 pages, 5 figures, 5 tables. Benchmark paper introducing 4 simulated environments, 135 tasks, and 1,698 evaluation points for healthcare administrative computer-use agents
- **AAIF category**: agents
- **Tags**: computer-use-agents, benchmark, healthcare, evaluation, arxiv, cs.ai
- **Quality score**: 4/5
- **Fetched at**: 2026-08-03T12:20:39+08:00

---

## One-liner

医疗行政 CUA 基准显示：子任务能力不等于端到端可靠自动化

## Chinese summary

HealthAdminBench 针对医疗行政工作流构建了 4 个 GUI 环境135 个专家任务和 1,698 个可验证子任务，用来评估 computer-use agents摘要报告最强端到端成功率仅 36.3%，而最高子任务成功率为 82.8%，说明医疗行政自动化的真实可靠性瓶颈仍在长链路任务完成

## English summary

Healthcare administration accounts for over $1 trillion in annual spending, making it a promising target for LLM-based computer-use agents (CUAs). While clinical applications of LLMs have received significant attention, no benchmark exists for evaluating CUAs on end-to-end administrative workflows. To address this gap, we introduce HealthAdminBench, a benchmark comprising four realistic GUI environments: an EHR, two payer portals, and a fax system, and 135 expert-defined tasks spanning three administrative task types: Prior Authorization, Appeals and Denials Management, and Durable Medical Equipment (DME) Order Processing. Each task is decomposed into fine-grained, verifiable subtasks, yielding 1,698 evaluation points....

## arXiv abstract

Healthcare administration accounts for over $1 trillion in annual spending, making it a promising target for LLM-based computer-use agents (CUAs). While clinical applications of LLMs have received significant attention, no benchmark exists for evaluating CUAs on end-to-end administrative workflows. To address this gap, we introduce HealthAdminBench, a benchmark comprising four realistic GUI environments: an EHR, two payer portals, and a fax system, and 135 expert-defined tasks spanning three administrative task types: Prior Authorization, Appeals and Denials Management, and Durable Medical Equipment (DME) Order Processing. Each task is decomposed into fine-grained, verifiable subtasks, yielding 1,698 evaluation points. We evaluate seven agent configurations under multiple prompting and observation settings and find that, despite strong subtask performance, end-to-end reliability remains low: the best-performing agent (Claude Opus 4.6 CUA) achieves only 36.3 percent task success, while GPT-5.4 CUA attains the highest subtask success rate (82.8 percent). These results reveal a substantial gap between current agent capabilities and the demands of real-world administrative workflows. HealthAdminBench provides a rigorous foundation for evaluating progress toward safe and reliable automation of healthcare administrative workflows.

## Why it matters for AAIF

- Grounded from arXiv metadata fetched with `opencli arxiv paper` and the existing AAIF entry summary.
- This backfill turns an entry-only card into a readable local content page without changing `entries.json`.
