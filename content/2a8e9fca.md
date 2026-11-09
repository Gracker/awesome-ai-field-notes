# LLMs are terrible at designing AI systems

- **ID**: 2a8e9fca
- **来源**: https://seangoedecke.com/llms-are-terrible-at-designing-ai-systems/
- **作者**: Sean Goedecke
- **发表**: 2026-11-08
- **证据**: AK-RSS Digest 2026-11-09（source/ 全文抓取，2026-11-09 20:16 Asia/Shanghai）

## 原文全文

# LLMs are terrible at designing AI systems
> 原文链接: https://seangoedecke.com/llms-are-terrible-at-designing-ai-systems/

---

LLMs don’t know how to design software that uses LLMs. They’re comfortable writing normal programs, but if you throw an AI-shaped problem at them, they will usually screw it up. Why is that?

### Going down the symbolic rabbit hole[](#going-down-the-symbolic-rabbit-hole)

For example, [this post](https://arbustoemchamas.substack.com/p/i-naively-tried-vibe-coding-a-memory) describes an attempt to vibe-code a memory tool that would flag when one memory contradicted another[1](#fn-1). This is a great instance of a task that was [virtually impossible](https://xkcd.com/1425/) five years ago but is now relatively trivial due to LLMs. You can simply task a LLM with scanning for contradictions, either in a big batch or pairwise[2](#fn-2).

However, when asked for the “state of the art” approach[3](#fn-3), the AI agent in this case did not recommend LLMs. It started building a bewilderingly complex symbolic system to convert the memory items into [structured logical atoms](https://en.wikipedia.org/wiki/Answer_set_programming), then mechanically compare them with a solver. This, of course, did not and could not work, because there is no analytic way of determining whether any two natural-language sentences express the same proposition.

The LLM knew this was impossible! When the user eventually lost patience and said “hey, why isn’t this working”, Claude immediately explained that this was a known 130-year-old problem with no solution. And yet it happily went around and around for weeks iterating on a dead end.

I’ve run into this myself. When I was building [Autodeck](https://www.seangoedecke.com/autodeck/) (AI-generated spaced repetition cards) my agents would routinely try to categorize cards by regex or keyword search instead of just making another LLM call.

### Why can’t LLMs use LLMs correctly?[](#why-cant-llms-use-llms-correctly)

Why would this be happening? I have two obvious explanations and one deeper one.

The first obvious explanation is that **most training code is pre-LLMs**. Assuming the labs aren’t feeding the current avalance of slop repositories directly into the models[4](#fn-4), the vast majority of the code that models learn from was written before LLMs were an option. So it would make sense that they’d reach for non-LLM approaches, in the same way that they’d reach for jQuery over modern vanilla JS, or Backbone.js over React, right? Wrong, actually! LLMs don’t choose jQuery and Backbone. Whatever part of the training process pushes them towards up-to-date knowledge in other areas isn’t successfully pushing them towards LLMs, so this can’t be the whole story.

The second obvious explanation is that **RLVR is not a good environment to write code that calls LLMs**. Much of the time LLMs spend training is spent in reinforcement learning environments where an automatic grader determines their performance (for instance, by running some code they wrote and checking the outputs). I don’t know this for a fact, but I would be surprised if these environments contained the credentials and API access for a LLM to call other LLMs[5](#fn-5). So even if the pretrained LLM was comfortable writing that kind of code, the reinforcement learning process might discourage[6](#fn-6) it from doing so.

The third explanation, which I like the most, is that **current AI agents are just not very good at software design**. On this explanation, picking a doomed symbolic approach instead of simply calling a LLM is not a weird aberration but a normal instance of AI agents picking the wrong tool for the job. I’ve seen this behavior from LLMs in other contexts too: trying to build complex (and doomed) consensus algorithms instead of tolerating stale data, introducing synchronous checks in event-driven systems, and so on. In the past I’ve [chalked these](https://www.seangoedecke.com/human-ai-partnerships-are-for-alignment-not-capability/) [up to](https://www.seangoedecke.com/how-to-read-code/) _alignment_, but I’m open to the idea that they’re just ordinary errors of software design.

### Conclusion[](#conclusion)

One lesson I learn over and over again is that I can’t judge a LLM by the standards of a human. Any human programmer who was capable of implementing a sophisticated symbolic solver would know that it wouldn’t work, and so if they suggested that approach I’d assume[7](#fn-7) they had a good reason. Only a LLM could be both smart enough and dumb enough to make this mistake.

I write a lot about the [skills](https://www.seangoedecke.com/getting-good-at-ai-takes-time-and-practice/) [that](https://www.seangoedecke.com/you-can-just-ask-ai-to-do-things/) [are](https://www.seangoedecke.com/tell-agents-the-why/) [involved](https://www.seangoedecke.com/prompts-are-technical-debt-too/) in working effectively with LLMs. I still stand by what I wrote in [February 2025](https://www.seangoedecke.com/beyond-prompting/):

> Using LLMs well involves extracting value from what they’re good at and avoiding wasting time at what they’re bad at.

This is surprisingly hard, because of the point above. LLMs are good and bad seemingly at random: they will work hard for hours but sometimes be [shockingly low-effort](https://www.lesswrong.com/posts/WewsByywWNhX9rtwi/current-ais-seem-pretty-misaligned-to-me), they will draw on inhumanly broad expertise but fail to apply the most basic common-sense, they can successfully [rewrite](https://bun.com/blog/bun-in-rust) enormously complex programs but will often make very silly [errors](https://www.seangoedecke.com/how-to-read-code/#cant-ai-just-do-it-for-you) in design.

If you can predict where they will do well or badly ahead of time, you can get _enormous_ value from LLMs; if you can’t, you will likely waste a lot of time and tokens going down hopeless approaches.

* * *

1.  [Here’s](https://news.ycombinator.com/item?id=50381522) another example where the user “implied” that Opus 5.5 should use a judge model and it instead constructed a series of regex checks.

    [↩](#fnref-1)
2.  Here I’d probably reach for a [decision model](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/).

    [↩](#fnref-2)
3.  In hindsight, this was probably the key mistake, though I don’t know how you’d turn that into advice for non-technical vibe-coders. Never asking the agent about the state of the field is a mistake too. Put one more notch on the [LLMs reward expertise](https://www.seangoedecke.com/llms-reward-expertise/) belt.

    [↩](#fnref-3)
4.  A fair assumption, I think: even though training on low-quality synthetic data clearly isn’t catastrophic for LLMs, it can’t be _great_.

    [↩](#fnref-4)
5.  It would be expensive, slow, and risky.

    [↩](#fnref-5)
6.  This theory also explains why LLMs are great at _prompting_ other LLMs as subagents, or on training LLMs from scratch: they’re likely directly RL-ed and evaluated on that, unlike on writing code that calls LLMs.

    [↩](#fnref-6)
7.  Well, okay, I wouldn’t — I’m arrogant enough to ask anyway — but I’d at least _expect_ a good reason.

    [↩](#fnref-7)

* * *

If you liked this post, consider [subscribing](https://buttondown.com/seangoedecke) to email updates about my new posts, or [sharing it on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fwww.seangoedecke.com%2Fllms-are-terrible-at-designing-ai-systems%2F&t=LLMs%20are%20terrible%20at%20designing%20AI%20systems).

Here's a preview of a related post that shares tags with this one.

> What requirements don't you have?
>
> When designing software, the requirements you don’t have are as important as the requirements you do. Identifying what you can compromise on — what can be slow, or stale, or inflexible — is usually the key to an elegant design.
>
> For instance, take preforking web servers like [Unicorn](https://github.com/defunkt/unicorn/). Because they lack the feature of shared mutable state between server instances, they can run each server in its own process, which provides isolation for free. Because Unicorn specifically ignores the problem of slow client handling, it can queue requests directly on Unix sockets, drastically simplifying the implementation.
> [Continue reading...](https://www.seangoedecke.com/what-requirements-dont-you-have/)

* * *

## 中文要点

Sean Goedecke 用实例说明 LLM 在「AI 形状的问题」上系统性地选错工具：有人 vibe code 记忆工具时，agent 放弃直接调 LLM 比对矛盾记忆，转头去造答案集编程式符号求解器——而判断两句自然语言是否同义本就没有解析解，Claude 自己也承认这是 130 年无解的老问题，却仍在这条死路上迭代数周。作者给三种解释：训练语料以前 LLM 时代代码为主（不成立，模型在别处会追新）、RLVR 环境缺凭证调不了其他 LLM、以及他最认同的——当前 agent 软件设计能力本身就弱，属于普通设计错误而非 alignment 问题。结论：评价 LLM 不能套人的标准，用好它要先知道它会栽在哪类问题上。

## Field Notes

- 来源证据：AK-RSS Digest 2026-11-09（source/ 全文抓取，2026-11-09 20:16 Asia/Shanghai）
- 入库批次：daily-intake-evening 2026-11-09
