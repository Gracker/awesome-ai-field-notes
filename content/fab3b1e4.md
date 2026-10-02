# The AI Race Just Got Awkward

- **ID**: fab3b1e4
- **原文链接**: https://insufferable.dev/posts/the-ai-race-just-got-awkward/
- **作者**: insufferable.dev
- **日期**: 2026-09-29
- **分类**: models
- **来源类型**: article
- **标签**: deepseek、kv-cache、pricing、inference
- **质量评分**: 4/5
- **抓取时间**: 2026-10-02 (daily-intake-evening, opencli/web fetch)

---

## 中文导读

insufferable.dev 把 Opus 5.5 与 GPT-6.1 Sol 的 cache read 降价直接归因到 DeepSeek 公开的 KV cache 优化：MLA 先压缩约 15 倍，随后 CSA、Heavily Compressed Attention，到 V4.1-Flash 用 CSA2、跨层缓存复用、causal encoder-decoder 与 FP4 caching 把全局 KV cache 压到每 token 890 字节，长会话场景相对 V1 约 437 倍。直接后果是西方定价：Opus 5.5 cache read 对 Opus 5 降 60%，GPT-6.1 Sol 对 GPT-5.6 Sol 7 月末定价降 80%，两家都几乎不提技术出处、悄悄发布。作者的措辞是 adoption 而非 stealing——中国厂商把配方公开送出去，受 GPU 限制被迫把性能优化做成第一目标的路线现在反过来给亏损的西方实验室续命。

## 为什么值得关注

cache read 降价就是采用 DeepSeek 成果的价格指纹：437 倍压缩对应 Opus -60%、Sol -80%，措辞用 adoption 不用 stealing。

## English Summary

insufferable.dev attributes the cache-read price cuts of Opus 5.5 and GPT-6.1 Sol directly to DeepSeek's openly published KV-cache optimizations: MLA compressed ~15x, then CSA and Heavily Compressed Attention, with V4.1-Flash's CSA2, cross-layer cache reuse, causal encoder-decoder architecture and FP4 caching bringing the global KV cache to 890 bytes per token - roughly 437x versus V1 for long-session workloads. The consequence is Western pricing: Opus 5.5 cut cache-read 60% versus Opus 5, GPT-6.1 Sol cut 80% versus GPT-5.6 Sol's late-July pricing, both shipped quietly with little credit. The author insists on 'adoption' over 'stealing': Chinese labs gave the recipes away, and GPU-constrained performance-first engineering is now keeping loss-making Western labs afloat.

## Obsidian 原文摘录（抓取正文头部）

```
If you read the news headlines these days, you would be forgiven for thinking that the Western labs are getting spawn-camped by Chinese labs en masse. The Distillation Drama Not a week goes by when Anthropic doesn’t release another article on how the Chinese are distilling their models , becoming a danger to humanity itself , etc. It’s beneficial for them to say that because it sets the ground for these models to be restrained legally and regulatorily later on . But it’s clear that the days of mindless distilling are over. Not just over. The new game in town is adopting Chinese labs’ advances. Note how I call this adoption instead of the more vitriol-infused “stealing” that Anthropic tends to use. That’s because, unlike the Western companies, the Chinese are pretty much giving away their recipes. A Different Game The latest one shamelessly copied without acknowledgement is the breakthrough in KV cache optimizations that DeepSeek has generously shared with the world. It is a mind-blowing optimization that basically dropped the KV cache footprint for certain use cases that use a long session context, like coding, by a factor of roughly 437x compared with DeepSeek-V1. They were the first ones to release the MLA architecture, which compressed the cache by roughly 15x, and then followed it up with ‘Compressed Sparse Attention’ and ‘Heavily Compressed Attention.’ The latest DeepSeek-V4.1-Flash pushes it even further with CSA2, cross-layer cache reuse, a causal encoder-decoder architecture, and FP4 caching, bringing the global KV cache down to 890 bytes per token. Why do these things matter? Because for serving long-context models, one of the largest costs is the VRAM needed to hold this cache in GPU memory. Below is the graph showing just how crazy this whole thing is: Follow the Cache Money Compare that with what the same tier cost roughly two months ago. All prices below are per 1 million tokens: A Very Quiet Thank-You All this must mean the Western AI companies are now extremely inference-margin positive. The constraints on access to advanced GPUs forced Chinese labs to make performance optimization a number one goal, and it shows in the results. Now I don’t know why they would freely give away such a breakthrough, but they just did, and for once both Anthropic and OpenAI released models that are basically top-tier and are using these optimizations. They do seem to be a little embarrassed by the copying. Hence the silent releases without much pre-announcement for both Claude Opus 5.5 and GPT-6.1 Sol. The user reviews have been stellar w.r.t. usage, and the quality doesn’t seem to be that far off compared to their flagship models (Claude Fable 5.1 and GPT-6 Astra). The cache read costs are the proof of the adoption. They dropped sharply: Opus 5.5 cut cache-read pricing by 60% versus Opus 5, while GPT-6.1 Sol cut it by 80% versus GPT-5.6 Sol’s late-July pricing. So the Chinese labs have thrown a lifeline to the Western loss-making labs, and I just have no clue as to why.
```

## Notes

- Content grounded in a same-day fetch (opencli web read / twitter thread / direct HTTP) during daily-intake-evening.
- 中文导读 block is the entry's summary_zh (verbatim); 为什么值得关注 is the entry's one_liner; no claims beyond the fetched source text were added.
- Source file cached at /tmp/aaif-evening/insufferable.md during the run.
