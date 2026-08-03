# SWE-bench Goes Live!

- **ID**: 8baf5fa7
- **Source**: arXiv
- **Original URL**: https://arxiv.org/abs/2505.23419
- **PDF**: https://arxiv.org/pdf/2505.23419v2
- **Authors**: Linghao Zhang, Shilin He, Chaoyun Zhang, Yu Kang, Bowen Li, Chengxing Xie, Junhao Wang, Maoquan Wang, Yufan Huang, Shengyu Fu, Elsie Nallipogu, Qingwei Lin, Yingnong Dang, Saravan Rajmohan, Dongmei Zhang
- **Published**: 2025-05-29
- **Updated**: 2025-06-01
- **Categories**: cs.SE, cs.AI, cs.CL
- **Comments**: Homepage: \url{https://swe-bench-live.github.io/}, Code: \url{https://github.com/SWE-bench-Live}, Dataset: \url{https://huggingface.co/SWE-bench-Live}
- **AAIF category**: coding
- **Tags**: coding-agents, swe-bench, benchmark, data-contamination, arxiv, cs.se
- **Quality score**: 5/5
- **Fetched at**: 2026-08-03T12:20:36+08:00

---

## One-liner

SWE-bench-Live 用持续更新的真实 GitHub issue 降低编码智能体评测污染风险

## Chinese summary

SWE-bench-Live 通过自动化实例创建和环境设置，发布 1,319 个来自 2024 年后 GitHub issue 的任务，覆盖 93 个仓库，并为每个任务配套 Docker 镜像论文报告相比静态 SWE-bench，现有 agent 和模型在 live-updatable抗污染的任务上仍有明显性能差距

## English summary

The issue-resolving task, where a model generates patches to fix real-world bugs, has emerged as a critical benchmark for evaluating the capabilities of large language models (LLMs). While SWE-bench and its variants have become standard in this domain, they suffer from key limitations: they have not been updated since their initial releases, cover a narrow set of repositories, and depend heavily on manual effort for instance construction and environment setup. These factors hinder scalability and introduce risks of overfitting and data contamination. In this work, we present SWE-bench-Live, a live-updatable benchmark designed to overcome these challenges. Our initial release consists of 1,319 tasks derived from real GitHub issues created since 2024, spanning 93 repositories. Each task is accompanied by a dedicated Docker image to ensure reproducible execution....

## arXiv abstract

The issue-resolving task, where a model generates patches to fix real-world bugs, has emerged as a critical benchmark for evaluating the capabilities of large language models (LLMs). While SWE-bench and its variants have become standard in this domain, they suffer from key limitations: they have not been updated since their initial releases, cover a narrow set of repositories, and depend heavily on manual effort for instance construction and environment setup. These factors hinder scalability and introduce risks of overfitting and data contamination. In this work, we present SWE-bench-Live, a live-updatable benchmark designed to overcome these challenges. Our initial release consists of 1,319 tasks derived from real GitHub issues created since 2024, spanning 93 repositories. Each task is accompanied by a dedicated Docker image to ensure reproducible execution. Central to our benchmark is \method, an automated curation pipeline that streamlines the entire process from instance creation to environment setup, removing manual bottlenecks and enabling scalability and continuous updates. We evaluate a range of state-of-the-art agent frameworks and LLMs on SWE-bench-Live, revealing a substantial performance gap compared to static benchmarks like SWE-bench, even under controlled evaluation conditions. To better understand this discrepancy, we perform detailed analyses across repository origin, issue recency, and task difficulty. By providing a fresh, diverse, and executable benchmark grounded in live repository activity, SWE-bench-Live facilitates rigorous, contamination-resistant evaluation of LLMs and agents in dynamic, real-world software development settings.

## Why it matters for AAIF

- Grounded from arXiv metadata fetched with `opencli arxiv paper` and the existing AAIF entry summary.
- This backfill turns an entry-only card into a readable local content page without changing `entries.json`.
