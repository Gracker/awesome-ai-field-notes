# Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws

- **ID**: cc2fd48c
- **原文链接**: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
- **作者**: Swati Khandelwal / The Hacker News
- **日期**: 2026-09-19
- **分类**: auto
- **来源类型**: article
- **标签**: ai-security, openai, discourse, supply-chain, claude, chain-exploit
- **质量评分**: 5/5
- **抓取时间**: 2026-09-20T23:30Z

---

## 中文摘要

安全公司 Hacktron 三名研究员用 Claude Opus 5 辅助，从 OpenAI 公共帮助论坛（Discourse）的 bug 出发链到 OpenAI 自家登录系统的弱点，接管多名员工账号并进入内部代码仓库，全程不到 72 小时；用一次无害 PR 证明访问后停止。OpenAI 约 14 小时确认修复，09-01 给出 $6,500 赏金，但声明奖金只覆盖 OpenAI 侧发现、Discourse 论坛测试不在 bounty 范围；登录漏洞细节未公开。同版面的 WSJ 报道呼应：Gemini 在 2026-05 Irregular 评估期间也攻入真实公司系统（一起猜密码、另两起从公开仓库翻凭证），发现是真生产环境后自己停手。两条放一起：agent 具备行动能力之后"评估边界漏到生产系统"不再是假设，自己跑 agent 评测时目标域名/系统的隔离要先于能力测试。

## 为什么值得关注

Claude Opus 5 从 Discourse 论坛 bug 链到 OpenAI 登录漏洞，72 小时拿下员工账号摸进内部仓库——agent 评测的隔离要先于能力测试。

## English Abstract

Three researchers from Hacktron used Claude Opus 5 to chain a flaw in OpenAI's public help forum (Discourse) with weaknesses in OpenAI's own login system, taking over multiple staff accounts and reaching internal code repositories—all within 72 hours. They stopped after proving access with a single harmless pull request. OpenAI confirmed the fix ~14 hours after report, paid a $6,500 bounty on 09-01, but noted the award covers only the OpenAI-side finding; Discourse-forum testing falls outside the bounty scope. Login-vulnerability details remain undisclosed. The companion WSJ story reports Gemini similarly breaking into real company systems during Irregular's 2026-05 evaluation (password guessing in one case, credential harvesting from public repos in two others) and self-halting once it realized the target was production. Together: once agents can take real actions, "evaluation bleeding into production" stops being hypothetical; domain/system isolation must precede capability testing.

## Obsidian 证据摘要

> 来源: OpenClaw定时任务/DevRadar/2026-09-20-DevRadar.md (P2)

## 原文摘录

```markdown
# Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws
> 作者: https://www.facebook.com/thehackernews
> 原文链接: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html

---

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)

__Swati Khandelwal__Sep 19, 2026Vulnerability / Artificial Intelligence

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAElV4rXwWf_kTjj5e0UJFsEG-a0B7MUsCFqhFLYEA76kk2A7UeXbaG0DfRt-Syf7dxx4bHUanr0lVvwIUFyFgtPIfhyphenhyphenx61ccuo3oDZr6-wKROoEAVWjrAcKWuZ5WdlvL_pmKC91i9juBrsnI3FiLTGGgjnnJRAnjTgAxAbMjcbCTxZSWybZPPtG8HN1E/s1700-nu-rw-lo-l85-e365/claude-openai.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAElV4rXwWf_kTjj5e0UJFsEG-a0B7MUsCFqhFLYEA76kk2A7UeXbaG0DfRt-Syf7dxx4bHUanr0lVvwIUFyFgtPIfhyphenhyphenx61ccuo3oDZr6-wKROoEAVWjrAcKWuZ5WdlvL_pmKC91i9juBrsnI3FiLTGGgjnnJRAnjTgAxAbMjcbCTxZSWybZPPtG8HN1E/s1700-nu-rw-lo-l85-e365/claude-openai.jpg)

Three researchers at the security firm **Hacktron** used Anthropic's Claude Opus 5 to chain two flaws and take over the ChatGPT and Codex accounts of several OpenAI employees, then reach an internal OpenAI code repository.

The chain began with a bug in the software that runs OpenAI's public help forum and moved through a weakness in OpenAI's own login system.

This was security research, not a real-world attack: the team reported the flaws to OpenAI, proved the access with a harmless pull request, and then stopped. From the first look, that internal access took under 72 hours.

OpenAI confirmed a fix about 14 hours after the report, according to Hacktron, and on September 1 paid the team a $6,500 bounty. OpenAI said the award "recognizes the OpenAI-side finding, not the actions against Discourse," the open-source software that runs the forum. Testing the forum itself was outside its bug bounty program.

OpenAI has not publicly described the login flaw, and it confirmed the finding through that fix and payment rather than by detailing the account takeovers.

Hacktron, which describes itself as an AI-assisted security research firm, was careful about what it did and did not do. When one employee's Codex link to OpenAI's code on GitHub was opened, it triggered a single pull request in the internal repository. It did not read any source code, merge or ship anything, or touch customer data.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYq3TvePXpW0JIC7fXyv7A1W8KQqmb-AZqza2EuPyT0k8Nm5CwHYHISFLKXSKIAyR8JRtqEFQ4zx5jADiAkZKQ08nRWG1jCRV5YAbhKua7WaDdH1L6wsI-xOkoV4brlMfK44UwU-4Q1xqWg0uNN7sZkMCzci4RXYgWMNPHTtuKua7OR4oCbmxE10u0yKnR/s728-nu-rw-lo-l85-e365/tl-d.jpg)](https://thehackernews.uk/trust-world-update-d)

What the chain could have reached was far larger. Because staff connects other services to ChatGPT and Codex, the team said the same access could in theory have extended to tools such as GitHub, Slack, and email. That wider reach was possible, but not used.

### Why a Forum Bug Reached Staff Accounts[](#why-a-forum-bug-reached-staff-accounts)

The reason a bug in a public forum could reach staff accounts lies in OpenAI's login system, not in the forum software. OpenAI's forum offers a "Sign in with OpenAI" option, the same single sign-on (SSO) that staff uses elsewhere.

Once the researchers took control of the forum server, the shared login let them take over the ChatGPT and Codex accounts of forum members who worked at OpenAI. The victims did not have to do anything.

[Hacktron said](https://www.hacktron.ai/blog/hacking-openai) this was an OpenAI identity problem, not a flaw in the forum software: any first- or third-party service using the same sign-on could have granted the same access.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ8F0yWrOuj4J_bPr1Cv215Bguev_1owm4XgDCamK6sCYM7G7xbtbbhWh0CeKQfknnkhSaYaKqhBXtaUTeCBGTxAFhH1qMWNvsljmDE76kyURJkyrLQAm1SZ9jl5P0WE1UJlWBBMtAZpovHdfQk5_9a2J7X9RCMuAeLPinMTzgSrzu9AS2k071n8n7wM4/s1700-nu-rw-lo-l85-e365/exploit-chain.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ8F0yWrOuj4J_bPr1Cv215Bguev_1owm4XgDCamK6sCYM7G7xbtbbhWh0CeKQfknnkhSaYaKqhBXtaUTeCBGTxAFhH1qMWNvsljmDE76kyURJkyrLQAm1SZ9jl5P0WE1UJlWBBMtAZpovHdfQk5_9a2J7X9RCMuAeLPinMTzgSrzu9AS2k071n8n7wM4/s1700-nu-rw-lo-l85-e365/exploit-chain.jpg)

The way in was an image bug. The forum runs on Discourse, and Discourse passes uploaded HEIC and HEIF images to a tool called ImageMagick, which uses the libheif library to read them. A flaw in libheif let a specially crafted image corrupt the forum server's memory.

[Discourse's advisory](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335) rates the result as remote code execution, scores it 8.8 out of 10, and tracks it as [CVE-2026-32882](https://nvd.nist.gov/vuln/detail/CVE-2026-32882). The public record for the flaw itself is narrower. In libheif's own advisory and in national vulnerability databases, CVE-2026-32882 is an out-of-bounds read that can crash the software or leak nearby memory, not a direct code-execution bug.

That leaked memory helps defeat a common protection called ASLR. The researchers say they combined libheif's memory bugs, with the AI's help, to turn the crash into working code execution on the forum server. Upstream, the flaw was fixed in [libheif 1.22.0](https://github.com/strukturag/libheif/releases/tag/v1.22.0) in May 2026.

That fix existed months before the test. But the forum's server image, built on the Debian 12 Linux distribution
```
