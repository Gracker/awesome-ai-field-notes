# What GLM-5.3 Flash running on Chinese hardware actually means

- **ID**: e6cc5ca4
- **原文链接**: https://martinalderson.com/posts/glm-5-3-flash-chinese-hardware/
- **作者**: Martin Alderson
- **日期**: 2026-08-29
- **分类**: infra
- **来源类型**: article
- **标签**: ai-hardware, china-semiconductors, glm-5.3, inference-cost, euv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-29T23:47:00+08:00

---

## 中文导读

Martin Alderson 拆解 Z.AI "GLM-5.3 Flash 端到端跑在国产芯片上"的声明：Z.AI 未点名芯片厂、未给吞吐/功耗数据（无人独立验证），他默认华为海思 910c 一档——96GB HBM2e 双计算 die、INT8 约 1.6 PFLOP/s、约 3TB/s、600W，约为四年前 H100 的 60%，且无原生 FP8。950 系算力不涨，拆 prefill（950PR，配慢的 HiBL）与 decode（950DT，配 HiZQ）两种 SKU 分摊国产 HBM 产能。真正的墙是 EUV：深圳逆向样机尚未产出可用芯片，业界预计规模量产不早于 2030（ASML 走了 25 年）；过不了 EUV 就压不下 7nm 以下的功耗墙。功耗账：纸面每瓦只差 2-3 倍（600W vs Rubin 约 2000W），但 96GB 限 KV cache 压小 batch，decode 每瓦吞吐再打折，每 token 每瓦落后约 5 倍还是宽容估计——电费从集群成本 10-20% 跳到近一半。判断：这是工程能力展示而非战略突破，中美算力差距可能继续拉大

## 原文摘录（节选）

> 摘录来源：opencli web read 全文抓取

```markdown
# What GLM-5.3 Flash running on Chinese hardware actually means
> 作者: Martin Alderson
> 发布时间: 2026-08-29T00:00:00.000Z
> 原文链接: https://martinalderson.com/posts/glm-5-3-flash-chinese-hardware/

---

Z.AI [confirmed](https://z.ai/blog/glm-5.3-flash) that their most recent model release was running all inference on Chinese manufactured hardware. While no doubt an impressive feat, Western companies still have a huge advantage that I can't see changing quickly.

## Where is Chinese AI hardware at?

To start with, it's worth looking into _where_ Chinese AI hardware is. I'm focusing entirely on the HiSilicon parts - the most competitive parts from Huawei. There are (many, actually) other manufacturers building AI hardware, but it's widely believed that they are no further ahead than HiSilicon, so I think that for brevity it's a fair starting point.

One caveat before I go further: Z.AI didn't actually name a chipmaker, and didn't publish throughput or power numbers either. Nobody has independently verified the claim. So I'm assuming HiSilicon here because it's the only plausible candidate at that scale, not because anyone has confirmed it.

It's also worth mentioning that the US export restrictions ([CSIS has a good overview](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls)) of high end AI hardware have made this an enormous priority, understandably, for the Chinese. And it's definitely worth mentioning that finding accurate sources for many of the numbers I'll cite are difficult to be confident in, so take the exact numbers with a pinch of salt.

The current 'scale-up' series of HiSilicon chip, the 910c series, pairs 96GB of HBM 2e memory with two compute dies, probably achieving something like 1.6PFLOP/s of INT8 compute with ~3TB/sec of memory bandwidth, at around 600W.

In essence, this is substantially behind even the H100 from Nvidia, which is now 4 years old. These are [around 60%](https://x.com/Yuchenj_UW/status/1884296403771617351) as fast as the H100, and has various other footguns (no native FP8 support for example), which probably restrict efficiency further for many use cases.

The next generation 950-series doesn't meaningfully increase compute as far as I can see, but does use domestically produced HiZQ/HiBL HBM memory. Interestingly the cards are configured in two variants - the 950PR and 950DT, with the former focusing on prefill and the latter on decode. In reality, the two products are very similar, but the prefill variant using slower HiBL memory vs the decode HiZQ memory. It does however support more quantisation types, like FP8.

## The constraints

I think this shows the limitations of what Chinese hardware can do - at least for the near future.

Yes, they can run inference, but so can _many_ sets of hardware now - AMD, Google and Amazon all have competitive solutions, and OpenAI are making significant progress on their [Jalapeño inference chip](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/), which in the [first published benchmarks](https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/) did 1.5-1.9x the work per watt of Nvidia's GB300. Inference hardware while no doubt complex, is a pretty _solved_ problem right now with a lot of competition - and that's before you bring in the Cerebras and Groq approach chips.

The wall that these Chinese hardware manufacturers are hitting is the lack of viable EUV (extreme ultraviolet) fabrication. This is the next generation silicon manufacturing process from ASML and it is _extremely hard_. I'd really, _really_ recommend reading [Chip War](https://www.christophermiller.net/semiconductors) by Chris Miller for the full story, but regardless until there is significant progress on this - and by significant progress, I don't mean the [reverse engineered prototype](https://www.techspot.com/news/110649-china-has-reverse-engineered-euv-machine-marking-major.html) in a Shenzhen lab. I mean reliable, _scale_ production.

The industry would be astonished if they got this to scale production before 2030. Bear in mind the Shenzhen prototype hasn't produced a working chip yet, and the more optimistic forecasts have them doing that around 2030 - volume production is a further step beyond it. It took ASML 25 years to figure out this technology - and a good 5+ years of this was scaling it up from the lab to "real" production lines. While China no doubt has incredible engineering talent _and_ the ability to reverse engineer some of ASML's work, it's still a daunting challenge.

Without EUV it is not possible to go (much) below the "7nm" fabrication size. Without being able to go below that size, you quickly hit a wall in thermal efficiency, and you reach a point where you simply cannot make the chip(s) any bigger or faster because you cannot expel the heat quickly enough.

Added to that, the additional export restrictions on HBM memory to China are clearly causing significant issues, hence the strange use of two different home grown memory technologies in the 950-series - no doubt because they can't produce enough fast (which is still comparatively _slow_) memory.

These are really the same base constraint - without EUV manufacturing technology you can't produce the latest generations of very fast HBM memory either.

## But maybe this doesn't matter?

Clearly the approach China is taking is instead of really looking for solid incremental leaps in compute and memory from better manufacturing techniques, the idea is to build _a lot_ of them. Even if your fastest chips are at best 5 years behind the latest Nvidia GPUs, you can just build 10 times as many for the same overall inference capacity. And it really is roughly 10x - not against the H100 I was comparing to above, but against what Nvidia actually ships today. A Rubin VR200 is somewhere around 35PFLOP/s of dense FP4 with 22TB/sec of HBM4 bandwidth. The 910c is 60% of a four year old 
```

---

> 本文由 daily-intake-evening 流水线于 2026-08-29 归档；摘录为原文节选，全文见原文链接。
