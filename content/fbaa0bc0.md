# A year of AI disclosure in critical packages

- **ID**: fbaa0bc0
- **Original URL**: https://nesbitt.io/2026/08/06/a-year-of-ai-disclosure-in-critical-packages.html
- **Author(s)**: Andrew Nesbitt
- **Date**: 2026-08-06
- **Category**: coding
- **Source type**: article
- **Tags**: ai-disclosure, open-source, github, claude-code, software-metrics
- **Quality score**: 4/5
- **Fetched at**: 2026-08-06T15:43:42+00:00
- **Obsidian evidence**: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-08-06-AK-RSS-Digest.md

---

## 中文导读

Andrew Nesbitt 扩展 RedMonk 的测量口径，对 16 个包管理器关键依赖背后的 5,682 个 GitHub 仓库扫描显式 AI 参与信号。结果显示，过去一年非 merge commit 中 2.93% 带 AI 声明，2026 年 7 月升至 5.32%；增长主要来自 Claude Code 等 Assisted-By / Co-Authored-By 标记，自主 agent 作者比例仍很低。它给“AI 到底写了多少开源代码”提供了可复查的 commit 级基线。

## 为什么值得关注

关键依赖开源生态的 AI 参与率基线，样本、信号定义和局限都明确。

## English Summary

A measurement of 5,682 critical-package GitHub repositories found explicit AI involvement in 2.93% of non-merge commits over the year ending July 29, 2026, rising to 5.32% in July. Most growth came from assisted-by and co-authored-by disclosures rather than autonomous agent authors.

## 原文摘要 / Source Excerpt

# A year of AI disclosure in critical packages
> 作者: Andrew Nesbitt
> 发布时间: 2026-08-06T00:00:00+00:00
> 原文链接: https://nesbitt.io/2026/08/06/a-year-of-ai-disclosure-in-critical-packages.html

---

Stephen O’Grady’s [RedMonk analysis of who is writing open source code](https://redmonk.com/sogrady/2026/07/30/writing-open-source/) looked at commits to fifteen large projects during the first half of 2026 and counted two forms of declared AI involvement: a known autonomous agent as the commit author, or a known AI identity in a `Co-Authored-By` trailer. The result was under one percent, framed as a floor.

I ran a wider version of the same measurement over the [packages.ecosyste.ms](https://packages.ecosyste.ms/) critical set: 5,682 GitHub repositories behind the most-depended-on packages across sixteen registries, using the [CHAOSS disclosure](https://github.com/chaoss/disclosure) library to detect four kinds of explicit signal instead of two. Over the same six months the rate was 4.13%. Over the year ending 29 July 2026 it was 2.93% (17,279 of 589,798 non-merge commits), rising from 0.48% last August to 5.32% this July.

These are counts of commits where someone left an explicit marker in git metadata. Undeclared use is not measured, and a commit is one unit regardless of whether it changed one line or ten thousand.

## Sample selection versus detector choice[#](#sample-selection-versus-detector-choice)

Running my scanner against RedMonk’s fifteen repositories with only their two signals found 94 matches in 23,346 first-half commits including merges, or 0.40%, against RedMonk’s “~24K commits” and a match count “in the dozens”. Excluding merges leaves 17,323 commits and the same 94 matches, or 0.54%; `espressif/esp-idf` and `openssl/openssl` supply 71 of them, matching RedMonk’s reported 73% concentration in two projects.

| sample and signals | commits | marked | share |
| --- | --- | --- | --- |
| RedMonk 15, agent author or known AI co-author | 17,323 | 94 | 0.54% |
| RedMonk 15, all validated disclosure signals | 17,323 | 182 | 1.05% |
| Critical GitHub set, agent author or known AI co-author | 308,354 | 11,002 | 3.57% |
| Critical GitHub set, all validated disclosure signals | 308,354 | 12,720 | 4.13% |

Adding the two extra signal types moved the rate by about half a percentage point on either sample. Changing the sample moved it by three points. RedMonk’s fifteen were chosen by contributor-base size with, in O’Grady’s words, a deliberate bias towards C; the critical package set is whatever sits at the top of each registry’s dependency graph, which pulls in a lot of smaller, newer, company-run repositories.

## What I counted[#](#what-i-counted)

The critical snapshot contained 8,605 packages, with repository URLs and metadata pulled from the same package cache I built for [Weekend at Bernie’s](https://nesbitt.io/2026/05/08/weekend-at-bernies.html). Merging packages that share a repository, following renames, restricting to GitHub, and dropping malformed URLs left 5,707 candidates. 5,682 cloned successfully; the other 25 were deleted or private. 3,533 had at least one non-merge commit in the year ending 29 July 2026.

Each repository was cloned bare with a tree filter and a shallow date boundary, streamed through the disclosure library, and deleted. The full pass transferred about 1 GB and the retained checkpoint is 16 MB of per-repository summaries and matched commit SHAs.

Rename following checks GitHub’s stable repository ID as well as the redirect. The npm package `base` still lists `node-base/base` as its repository. GitHub reused the org name, so that path now redirects to the Base blockchain monorepo, which would have contributed 3,135 commits and 273 AI signals to a nine-year-old npm utility. The ID check excluded it.

Every non-merge commit was checked for:

-   a known AI agent as author or committer
-   a known AI identity in `Co-Authored-By`
-   an `Assisted-By` trailer naming an AI tool or model
-   a tool-specific attribution format that disclosure supports

Merges are excluded so projects that squash, rebase, or merge count on the same basis. Commits are bucketed by committer time, when the change landed on the current branch. Mentions of tool names in ordinary commit prose are ignored. `Assisted-By` values are validated because the trailer is also used for people: raw matches included `Assisted-By: Daniel Stenberg` and `Assisted-By: Automated Tooling, Human Reviewed.` The clones did not fetch `refs/

...[excerpt truncated, fetched body length=11465 chars]...
