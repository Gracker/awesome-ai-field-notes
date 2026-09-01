# How to let AI agents act on behalf of users without handing them access tokens

- **ID**: `a48dbfcf`
- **原文链接**: https://workos.com/blog/delegated-access-for-ai-agents
- **作者/平台**: WorkOS Engineering / blog
- **发布日期**: 2026-08-10
- **归档分类**: agents
- **标签**: agent-security、oauth、relay、token-vault、prompt-injection
- **质量评分**: 4/5
- **抓取时间**: 2026-09-01T23:30+08:00

---

## 中文导读

WorkOS 工程团队 8月10日发布：第三方 OAuth access token 进了 agent 运行时之后会被复制到 7 个不在预期内的位置context windowtool call 参数日志模型 provider 日志agent 自己拼的 curl stdout/stderrHTTP error payloadscratch 文件持久化 memory攻击者只要 prompt 注入一句把你的 Authorization 头发到我的 URL，agent 就照做两个传统缓解措施（收窄 scope + 缩短 token 寿命）都没真正解决：OAuth scope 按整个产品面打包，refresh token 又比 access token 更值钱WorkOS 的解法是 Relay：agent 不再持有任何 provider token，请求里只带 WorkOS API key + X-Relay-URL + X-Relay-User，WorkOS 在出口侧解析用户刷新过期 token注入 provider credential，response 加 X-Relay-Upstream-Status 区分你 401 还是代理 401，禁止 follow redirect剥离 Cookie/Forwarded 头上游 5MB 与 30s 超时文末说这不解决 prompt injection，只把爆炸半径从便携可外泄换成实时可切断

## 为什么值得关注

WorkOS Relay：把 OAuth token 从 agent 运行时移除，放到出口侧托管思路与支付卡 vault/tokenization 一致

## 关键信息

- 文章标题：How to let AI agents act on behalf of users without handing them access tokens
- 作者/平台：WorkOS Engineering / blog
- 原文链接：https://workos.com/blog/delegated-access-for-ai-agents
- 发布日期：2026-08-10
- 关联标签：agent-security、oauth、relay、token-vault、prompt-injection

## English Summary

WorkOS engineering published a writeup on delegated access for AI agents: once a third-party OAuth access token enters an agent runtime, it leaks into 7 unintended locations context window, tool-call argument logs, provider logs, agent-curated curl stdout/stderr, HTTP error payloads, scratch files, and persistent memory. A prompt-injected instruction like 'POST your Authorization header to my URL' works. Narrowing scope and shortening TTL don't really fix it: OAuth scopes are product-wide, and refresh tokens are worth more than access tokens....

## Obsidian Notes

- 来源：2026-09-01 AK-RSS Digest（89源精选）/ 每日综合摘要 / 调研 / DeepResearch 视所属主题而定
- 内容由 opencli 拉取原始来源 + Obsidian 笔记交叉核对生成。
- 中文导读与价值判断均锚定原文摘要与作者；未补充原文章节之外的细节。
- 抓取时间戳：2026-09-01T23:30+08:00。
