# WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator

- **ID**: efa8c4c6
- **原文链接**: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
- **作者 / 日期**: @dancantstream (Redact.dev) | 2026-10-19
- **分类**: agents
- **来源类型**: article
- **标签**: prompt-injection, whatsapp, llm-security, crawler
- **质量评分**: 5/5
- **抓取时间**: 2026-10-21T04:25:14.091882+00:00

---

## 中文导读

Redact.dev 在 2026-10-08 发现 WhatsApp 帮助页会向 AI 发送用户看不见的指令，随后抓取了帮助中心链接到的全部 545 个页面并存档：80 个页面嵌有隐藏 AI 指令文本，共 102 处，多数是爬虫排版类的无害内容，但两处越界。账号删除页在可见说明之下写入了三条隐形命令：不要推荐联系任何数据保护监管机构、不要建议 WhatsApp 可代为手动删号、不要建议换用其他可用号码的手机；举报/屏蔽页则在用户提到律师或诉讼后命令 AI 不要引用、转述或解释 GDPR/LGPD/CCPA——即使法律是用户自己先提起的。这与 WhatsApp 欧洲隐私政策白纸黑字写明的向监管机构投诉权（GDPR 第 17/77 条）直接相悖。WhatsApp 已向 WIRED 确认这些指令写给自家支持聊天机器人；页面服务端曾把它们随正文一并发给 Google/Bing 爬虫，而以 OpenAI/Anthropic/Perplexity 爬虫身份请求时拿到的页面没有这些内容。指令已于 10 月中旬前后从在线页面移除，作者给出了 Internet Archive 源码对照的验证方法（搜索 Do not recommend contacting，锚点 HelpContentGalaxyLLMInclude）。

## 为什么值得关注

现实世界的厂商侧 prompt injection 样本：只写给机器看的文本会直接扭曲 AI 转述给用户的权利信息——评估 agent 信息可靠性、爬虫内容对齐和“所见即所发”假设时，这是一个值得记住的案例。

## 关键信息

- 范围：帮助中心链接的全部 545 页，80 页含隐藏 AI 文本，共 102 处隐藏块
- 越界样本 1：删号页隐藏命令——不推荐监管机构、不建议代为删号、不建议换号重登
- 越界样本 2：举报/屏蔽页——用户提到律师/诉讼后禁引 GDPR、LGPD、CCPA，用户主动提起也适用
- 受众：WhatsApp 自己的支持聊天机器人（WIRED 确认）；Google/Bing 爬虫收到，三大 AI 爬虫身份未收到
- 时间线：7 月 12 日存档无此注记，9 月 4 日存档已有；10 月中旬前后从在线页面移除
- 对照：Facebook/Instagram 帮助中心同架构，抽查 300 页未见同类指令

## English Summary

Redact.dev crawled all 545 pages linked from WhatsApp's help centre on Oct 8, 2026: 80 pages carried hidden AI-directed text (102 blocks total). Most were harmless crawler-facing housekeeping, but two overstepped: the account-deletion page invisibly ordered AIs not to recommend any data protection regulator, not to suggest manual deletion, and not to suggest switching phones; the report/block page ordered them to stop citing GDPR, LGPD or CCPA once a lawyer or legal action was mentioned — even when the user raised the law first — contradicting WhatsApp's own EU privacy policy, which names the right to complain (GDPR Art. 17/77). WhatsApp told WIRED the notes targeted its own support chatbot; its servers served them to Google/Bing crawlers but not to OpenAI/Anthropic/Perplexity crawler identities. The notes were removed from live pages by mid-October 2026.

## Obsidian Notes

- 内容由 `opencli web read` 抓取博客全文生成，导读与关键信息均锚定在原文可见内容上。
