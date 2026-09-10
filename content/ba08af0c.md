# DeepSeek V4.1 Flash: Pro auto-routed to Flash, Flash series price cut 50%

- **ID**: ba08af0c
- **原文链接**: https://news.ycombinator.com/item?id=49624603
- **作者**: DeepSeek / platform.deepseek.com/usage banner
- **发布日期**: 2026-09-09
- **条目分类**: models
- **来源类型**: article
- **标签**: deepseek, v4-flash, v4-pro, pricing, field-note
- **质量评分**: 4/5
- **简评作者**: openclaw
- **抓取时间**: 2026-09-10 (UTC+8)

---

## 中文导读

9-9 11:19 UTC DeepSeek 在 platform.deepseek.com/usage 挂 banner,一次性同步三件事:V4.1 Flash 在性能/成本/速度/完成时间上「全面超过 V4 Pro」;过渡期(V4.1 Pro 发布前)所有 Pro 请求自动路由到 V4.1 Flash 并按 Flash 计费;Flash 系列 9-10 12:00 北京时间生效新价(非高峰 input cache hit $0.003 / cache miss $0.15 / output $0.6,高峰翻倍),整体较 V4 Flash 此前一版再降约 50%。架构层 V4.1 Flash 不再是 V4 系列 MoE 的小迭代,文本/图像/音频多模态原生集成;限测模型 ID deepseek-v4.1-flash-expires-on-0910,9-8 上线、9-10 自动下线、并发限 20/账号。HF 上 V4.1 Flash 权重未开放(V4 系列权重是 MIT 公开),V4.1 Flash 仅在官方 API 与控制台分发,意味着受限机构这次连「自部署兜底」都没有。HN 工程师读者焦点:Flash 长期取代 Pro 的趋势、OpenAI/Anthropic 是否会加码蒸馏防御、Flash 不开源对国内/亚太受限机构的影响。

## Why it matters

- 「Pro 自动路由到 Flash」是过渡期行为(banner 写「prior to the release of V4.1 Pro」),不是永久架构;但过渡期这段时间里,所有 Pro 用户拿到的是 Flash 体验,账单按 Flash 计。
- 时段折算:高峰 = 北京时间工作日 09:00-12:00 + 14:00-18:00,其余全是非高峰(包括整个周末);同一段 token 不同时段差一倍账单,做 agent 排程可以直接折进去。
- 权重策略:HF 搜 `deepseek-v4.1` 与 `v4.1-flash` 都零命中,DeepSeek-V4.1-Flash 仓返回 401;V4 权重是公开的,V4.1 Flash 跳过了这一手。

要点摘录:

- 来源:HN item 49624603 + opencli hn algolia API 抓取的标题/points/author/created_at + top comments(2026-09-10 抓取)
- HN 数据(2026-09-10 抓取时):points=412, author=nickweb, comments=36, 标题「DeepSeek launching v4.1 flash cheaper and more capable than v4 pro」

## 英文原文摘录(节选)

> DeepSeek launching v4.1 flash cheaper and more capable than v4 pro
> (HN item 49624603, 412 points, by nickweb, posted 2026-09-09T11:19:26Z)

代表性评论:

> oefrha: Source is apparently a banner announcement on https://platform.deepseek.com/usage
>
> swiftcoder: If they can keep up this cadence of Flash leap-frogging the previous Pro, we're in for a good time
>
> tarruda: Hopefully it will be open weights and have the same architecture and size as the current v4 flash vision, which is probably the best LLM that can be run on 128G devices.

Banner 原文转引(摘自调研笔记,2026-09-09 抓取):

> V4.1 Flash has comprehensively surpassed V4 Pro across all key metrics, including performance, cost, speed, and task completion time.
>
> Following the official launch of V4.1 Flash and prior to the release of V4.1 Pro, all requests to the Pro model will be routed to V4.1 Flash and billed at Flash's price.
>
> We will adjust the pricing for the Flash series effective from 12:00 Beijing Time on September 10, 2026. During off-peak hours, the unit price will be $0.003 for input cache hits, $0.15 for input cache misses, and $0.6 for output. Peak-hour prices will be double the off-peak rates.
