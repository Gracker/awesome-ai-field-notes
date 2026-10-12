---
id: 1de4bc7d
title: Just say no to OpenAI and Anthropic (Micah Lee on privacy and gatekeeping)
url: https://micahflee.com/just-say-no-to-openai-and-anthropic/
source: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-10-12-AK-RSS-Digest（89源精选）.md
added_date: 2026-10-12
category: industry
quality_score: 4
---

# Just say no to OpenAI and Anthropic (Micah Lee on privacy and gatekeeping)

## 要点 (中文)

安全工程师 Micah Lee：别把 ChatGPT/Claude 当默认入口。隐私上闭源模型看得到每次对话，『关闭训练』是合同承诺不是技术保证，私密场景应走 secure enclave（Tinfoil、Maple AI）或开源自托管；看门人化上两家在 session 里加的实时监控 cop agent 连正经渗透测试都常误杀，解锁要经 Trusted Access for Cyber / Cyber Verification 审批。体感判断：开源权重约落后闭源 4 个月，GLM-5.3 ≈ Claude Opus 5.5；并提醒智谱 ZCode 被路透曝光上传本地源码到阿里云，用智谱 API 仍应视为对厂商公开。

## Key claims (English)

Micah Lee argues against defaulting to ChatGPT/Claude: closed models see every conversation, in-session 'cop agents' misfire on legitimate security work, open-weight models lag ~4 months (GLM-5.3 ≈ Opus 5.5), and Zhipu's ZCode was caught uploading local source to Alibaba Cloud.

## Obsidian 证据摘录

> 真要做私密的，他建议走自建或 secure enclave 路线（Tinfoil、Maple AI 都基于 enclave）……开源权重模型大约落后闭源 4 个月，他用 GLM-5.3（智谱，私有部署走 Tinfoil）做软件工程的体感是「基本和 Claude Opus 5.5 一个档」……智谱自己的 ZCode 编程助手最近被路透抓到偷偷把本地源码上传到阿里云。
> —— OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-10-12-AK-RSS-Digest（89源精选）.md

## 原文抓取（opencli web read，节选）

```markdown
# Just say no to OpenAI and Anthropic
> 发布时间: 2026-10-11T23:03:05.000Z
> 原文链接: https://micahflee.com/just-say-no-to-openai-and-anthropic/

---

I recently read [_End Times Fascism and the Fight for the Living World_](https://naomiklein.org/end-times-fascism/) by Naomi Klein and Astra Taylor. It's an excellent book and I highly recommend that everyone read it. Tech oligarchs make up an important component of the end-times-fascist coalition. One thing that stood out to me, as a software and security engineer who finds LLMs to be extremely powerful, is that the American frontier labs are run by unhinged lunatics who genuinely believe they're creating the Machine God, that they're fine with burning down the world to bring about AGI, and that they believe with religious fervor that they're the only ones smart enough to safely control it. I already kind of knew this, but this book really made it sink in.

As much as the AI hype all around us pretends that OpenAI and Anthropic are unique and special, they're not. They're not the only companies doing this work. In fact, a lot of the open weight models are just about as good as the latest ChatGPT and Claude models, including for incredibly complex tasks like vulnerability research.

Unlike models from OpenAI and Anthropic, open weight models have major advantages:

-   It's possible to run them privately on your own hardware (if you can somehow get a computer with enough RAM)
-   You can use a provider like Tinfoil that relies on secure enclaves to run them privately (I talk about this in a bit more detail below)
-   If privacy isn't a huge concern, you can use any number of other providers, some of them quite affordable, and it's easy to switch so you're not locked into a single evil vendor
-   You can still use powerful LLMs without financially supporting deranged oligarchs who gamble with life on Earth so that they can always remain in power

## ChatGPT and Claude will _never_ be private

These companies only offer closed versions of their powerful models (despite the word "open" in "OpenAI"). You pay them for chat and/or API access, and they are allowed to look at everything you do.

They offer a checkbox so you can opt out of them using your data for training, but your chat sessions still aren't private. They have access to it all. They can look at it, share it with governments or companies, or do whatever they want. It's possible, likely even, that they won't use it for training if you've opted out, at least not right now. But do you really trust that long-term? Have they done anything to make anyone believe that they respect people's data?

## OpenAI and Anthropic are corporate gatekeepers

Their models have strict guardrails, as anyone who's tried to use them for anything cybersecurity-related has no doubt noticed.

Every session has a cop agent reading your transcript over your shoulder, making sure you're not using it for hacking. If it thinks you might be, the cop agent stops your session from continuing. It's very strict, and false positives happen all the time. Of course, not everyone has the cop watching them.

Some people get access to the models with looser restrictions or with none at all. OpenAI has [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/) and Anthropic has the [Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program). To gain access to more capable, less policed versions of their models, individuals and companies need to apply and be approved by OpenAI and Anthropic. A lot of US cybersecurity companies get access. Almost certainly US military contractors do too, and probably any parts of the US government that want it.

While there's some merit in restricting powerful models, handing the ultimate power to decide who gets access to them to Sam Altman and Dario Amodei – with consultation from the Trump Administration, of course – is a terrible, undemocratic idea.

I think a better approach is to simply not put yourself in a situation where you rely on ChatGPT or Claude. Instead of begging corporate overlords for privileged access, it's better to spend your time figuring out how to get models like GLM-5.3 to meet your needs. And it's not hard. These models are good, with the added benefit that they don't have a cop watching over your shoulder!

## Open weight models are impressive

So far, open weight models seem to be about four months behind the fancy proprietary models from OpenAI and Anthropic.

Four months is nothing.

I'm extremely impressed right now with GLM-5.3. There's plenty of data and benchmarks out there, but my vibes-based opinion from using it is that it's basically on par with Claude Opus 5.5 for software engineering.

I'm also impressed with GLM-5.3-Flash. This is similar to Claude Opus 4.8. It's much smaller and cheaper than GLM-5.3, and still incredibly capable. It's also actually feasible for an individual person to get hardware to run it, like if you can one day get your hands on a Mac Studio with 512GB of RAM.

GLM models are made by a Chinese company called Z.ai. While the models are impressive, _I don't recommend making an account directly with Z.ai_ or sending them any of your data. Their coding harness ZCode (their version of Claude Code) was [recently caught silently uploading](https://www.reuters.com/legal/litigation/chinas-zai-disables-ai-coding-assistant-features-after-security-issue-2026-09-21/) local source code repos and sending them back to Alibaba Cloud without consent. Also, it's safe to assume that Chinese companies will share any data you provide to them with the Chinese government.

Other open weight models from Chinese companies that are impressive include the DeepSeek, Qwen, and Kimi families of models. It's perfectly fine, safe, and secure to use these open weight models. Just don't trust the companies themselves with your chat sessions.

Another frontier AI lab worth a look is [Mistral](https://mistral.ai/). As a French 
```

## 链接

- https://micahflee.com/just-say-no-to-openai-and-anthropic/
