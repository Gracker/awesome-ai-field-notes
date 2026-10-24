# Meta Muse exposes users' personal and business secrets when they share conversations

- **ID**: add383da
- **原文链接**: https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations
- **作者**: Dan Goodin (Ars Technica, Senior Security Editor)
- **日期**: 2026-10 (from URL slug /2026/10/; article says researchers reported Monday; exact page timestamp not exposed in fetch)
- **分类**: industry
- **来源类型**: article
- **标签**: privacy, ai-agents, meta, security, sharing
- **质量评分**: 4/5
- **抓取时间**: 2026-10-23 20:22 UTC

---

## 中文导读

Claroc 研究者用一次被动 DNS 查询就枚举出 6800 个 Meta Muse 分享链接：分享页挂在 cf.metaaiusercontent.com，且把对话标题直接放进子域名（例如 loan-application-draft-a4c9e2.cf.metaaiusercontent.com），公共 DNS 记录让任何人都搜得到这些从未拿到手的链接，研究方称之为 GhostShares抽样页面包括：某候选人为前沿 AI 实验室高管面试准备的笔记（含内部联系人与会议时间）标注给 CEO 的公司营收复盘小微企业贷款申请带部分账号的银行欺诈提醒全年员工休假表等Muse 上线时宣称从底层为隐私与安全打造，Meta 现已暂停分享功能；该报告 10 月 8 日经漏洞赏金提交后一直无人回复对 agent 产品的直接教训：隐私设计必须覆盖 URL 与 DNS 这类元数据面

## 为什么值得关注

Meta Muse 把对话标题写进分享链接子域名，被动 DNS 一查即中：6800 个 GhostShares 泄露面试笔记与财务数据 Relevance for field notes: a concrete, verified privacy-design failure mode for AI agents - conversation titles leaked into public DNS via share-page subdomains - meaning agent products must treat URL/DNS metadata as part of the threat surface, not just page content.

## 关键信息

- 文章标题: Meta Muse exposes users' personal and business secrets when they share conversations
- 作者: Dan Goodin
- 来源: Ars Technica (security)
- 发布时间: 2026-10
- 关联标签: privacy, ai-agents, meta, security, sharing

## What the article reports (grounded facts)

- Claroc researchers enumerated 6,800 Muse share links with a single passive-DNS query. Share pages live on cf.metaaiusercontent.com with the conversation title placed in the subdomain (e.g. loan-application-draft-a4c9e2.cf.metaaiusercontent.com), so public DNS records make links discoverable without ever being handed them. The firm calls these GhostShares.
- Sampled exposures included: a candidate's notes for a confidential executive-search call with a frontier AI lab (naming the lab's internal contact and meeting time); a national marketing company's internal revenue review marked for its CEO; a small-business owner's loan application with the amount requested; a to-do list with a bank fraud alert, partial account number, transaction amount and time; a real-estate investor's internal performance report with two property addresses and exact return/income/mortgage figures; a full-year staff vacation calendar listing dozens of employees.
- Researcher quote: "If you had asked us beforehand, we would have guessed that gathering these would take real effort. It took one query."
- Meta statement: sharing creates pages accessible to those with the link, and Meta has paused the functionality while reviewing the report and how links can be discovered. Claroc CTO Asaf Aprozper reported the findings through the Muse bug bounty program on October 8 and got no reply (LinkedIn outreach also unanswered).
- Context: Muse is Meta's general-purpose agent that autonomously fills forms, books appointments and makes purchases, requiring broad account access; Zuckerberg pitched it as "built from the ground up for privacy and security". Three weeks after launch, Patrick Wardle found a zero-day letting any same-device app take over a Muse account, which Meta downplayed.

## English Summary

Claroc researchers enumerated 6,800 Meta Muse share links with a single passive-DNS query: share pages live on cf.metaaiusercontent.com with the conversation title placed in the subdomain (for example loan-application-draft-a4c9e2.cf.metaaiusercontent.com), so public DNS records make links discoverable without ever being handed them - the firm calls these GhostShares. Sampled pages exposed an executive-search prep note naming a frontier AI lab contact and meeting time, a company revenue review marked for its CEO, a small-business loan application, a fraud alert with a partial account number, and more. Muse was pitched as built from the ground up for privacy and security; Meta has paused the sharing feature while reviewing, and the report had sat unanswered in its bug bounty program since October 8....

## 证据

- Fetched 2026-10-23 20:22 UTC via `opencli web read --download-images false -f md`; full article body present in the returned markdown (ad/video chrome skipped).
- Original: https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations
- Researcher write-up: https://blog.claroc.io/ghostshares-muse-passive-dns/
- All facts above are quoted or paraphrased from the fetched article body; no outside details added.
