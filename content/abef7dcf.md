# Google Cogentic ships Lean-verified unconditional integer factorization papers

- **ID**: abef7dcf
- **原文链接：** https://github.com/google-research/google-research/tree/master/cogentic_research_papers
- **作者：** Google Research
- **日期：** 2026-11-25
- **更新：** N/A
- **分类：** industry
- **来源类型：** github
- **标签：** ai-math, lean, formal-verification, gemini
- **质量评分：** 4/5
- **抓取时间：** 2026-11-26T15:44:07Z

---

## 中文导读

google-research 仓库 11 月 25 日批次收录 Cogentic 产出：跑在 Gemini 4 上的 agentic 数学发现框架交出 6 篇数学论文头篇给出整数因子分解无条件结果：单台固定图灵机上零错误 Las Vegas 算法，最坏期望时间 L_N[1/3, 105]，不依赖未证数论假设，输出逐个用 AKS 与直接乘法验证，完整证明用 Mathlib-only Lean 4 形式化；同批另有 DLP 亚拟多项式等里程碑在去启发式假设加全机器验证：指数仍是亚指数级（GNFS 启发式常数约 1.9，此篇 105），RSA 现实路径未变，PQC 节奏不用动

## 为什么值得关注

Google Cogentic ships Lean-verified unconditional integer factorization at L[1/3,105] via agentic discovery on Gemini 4

DevRadar 2026-11-26 read the repo README (integer_factorization / discrete_logarithm entries) and Aaronson's blog directly; summary restricted to those direct-read claims, hearsay lab rumors excluded.

## 关键信息

- 标题： Google Cogentic ships Lean-verified unconditional integer factorization papers
- 作者： Google Research
- 链接： https://github.com/google-research/google-research/tree/master/cogentic_research_papers
- 发布时间： 2026-11-25
- 分类： industry
- 关联标签： ai-math, lean, formal-verification, gemini

## English Summary

Google Research's repository added a cogentic_research_papers batch (2026-11-25): six math papers from Cogentic, an agentic math-discovery framework (arXiv 2609.40324). Headline: unconditional integer factorization in time L_N[1/3, O(1)] - a zero-error Las Vegas algorithm on a single fixed Turing machine, worst-case expected time L_N[1/3, 105], no unproven number-theoretic assumptions, outputs verified individually via AKS and direct multiplication, full proof formalized in Mathlib-only Lean 4. The batch also includes a sub-quasi-polynomial discrete-log algorithm for small-characteristic finite fields and a 1/5-approximate Nash equilibrium. The milestone is removing heuristic assumptions plus full machine verification; the exponent remains subexponential (GNFS heuristic ~1.9 vs 105 here), so RSA's practical path and PQC timelines are unchanged.

## Source Excerpts

### DevRadar 2026-11-26 P1 (OpenClaw定时任务/DevRadar)

google-research 仓库 11-25 批次收录 6 篇。Cogentic——跑在 Gemini 4 上的 agentic 数学发现框架（arXiv 2609.40324）——产出《Unconditional Integer Factorization in Time L_N[1/3, O(1)]》：单台固定图灵机上的零错误 Las Vegas 算法，最坏期望时间 L_N[1/3, 105]，输出用 AKS 与直接乘法逐个验证，不依赖未证数论假设，完整证明已用 Mathlib-only Lean 4（v4.35.0）形式化；同批还有小特征有限域 DLP 亚拟多项式算法、1/5-近似纳什均衡等。判断：因子分解这篇是亚指数（GNFS 启发式约 1.9、这篇是 105），里程碑在去掉启发式假设加全机器验证；RSA 当下没有被更快分解的现实路径，PQC 迁移节奏不用动。

### Context (scottaaronson.blog, read 2026-11-26)

Aaronson 写到多个可靠信源指向实验室手里有能打破现有密码系统的成果，但细节未公开；带 Lean 证书的实验室成果按默认可信处理。
