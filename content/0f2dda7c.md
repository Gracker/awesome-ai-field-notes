# Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing

- **ID**: 0f2dda7c
- **原文链接**: https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing
- **作者**: John Gruber
- **日期**: 2026-08-16
- **分类**: industry
- **来源类型**: article
- **标签**: anthropic, watermark, eu-ai-act, regulation, claude, writing
- **质量评分**: 4/5
- **抓取时间**: 2026-08-17T23:51:34+08:00

---

## 中文导读

Gruber 对 Anthropic 为符合 EU AI Act 50(2) 而在全量 Claude 文本嵌入水印的逐层反驳：机制是 token 采样按 green/red list 加偏、事后可用密钥识别，但这不是“不可感知”的隐写——它会改变词选择；法规只要求 provider 端标记，把范围拉到模型级全量是 Anthropic 自己的选择；有动机的作弊者重写一遍即可绕过，先被怀疑的反而是无辜的辅助写作用户。EU 条款的宽立法与厂商的宽执行叠加，代价由写作者承担。

## 为什么值得关注

水印反对派的最完整论述：牺牲表达质量换可识别性，且合规范围远超法律底线。

**收录理由**：把水印的技术原理、监管来源与对作者的实际伤害一次讲透，立场对内容工作者有代表性

## 关键信息

- AK RSS Digest 评分：AK RSS Digest 评分：8.6/10
- 来源：AK RSS Digest（2026-08-17 期）
- Obsidian 证据：`OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-08-17-AK-RSS-Digest（89源精选）.md`

## 原文快照

# Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing

---

# Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing

###### Sunday, 16 August 2026

When I [wrote this week](https://daringfireball.net/linked/2026/08/11/anthropic-claude-watermarks) about Anthropic’s announcement that all Claude models, worldwide, would soon begin “watermarking” everything they generate, including text, to comply with [this EU regulation](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content), we were left to speculate _how_ this was going to work, because Anthropic offered not even a vague description of how it would work — despite the fact that the title of the announcement was, absurdly and insultingly, “[How Claude Marks AI-Generated Content](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)”.

My initial speculation was that maybe they’d hide invisible non-printing Unicode characters in the text. Just spitballing. Turns out that’s not what they’re going to do. What they’re going to do is apply a form of steganography, where the choice of words (or other token output) at inference time will leave fingerprints that can later, maybe, be detected probabilistically.

I initially guessed “invisible characters” not because I didn’t think of the semantic word-choice technique, but because I was a fool who took Anthropic at its word in their description of what they would do. Their original support document claims:

They say “imperceptible” and “doesn’t change the meaning, quality, or readability”. Their words. Not _almost_ imperceptible. Not _slightly_ changes the meaning, quality, or readability. That made sense to me, because that’s absolutely what I want — nay, demand — from any tools I use personally. It’s unacceptable for a tool to sacrifice an iota of clarity, coherence, meaning, quality, etc. for the purpose of embedding hidden clues within the text to suggest its provenance. That’s what I would and will demand. And Anthropic’s (original) support document unambiguously claims that’s what their system will enable. So if that were true, I couldn’t see what was left other than hiding invisible characters within the text.

My error was believing Anthropic that their system wouldn’t adulterate and corrupt the semantics of the text their models generate. _That_ is in fact exactly what they plan to do. I should have my head examined for believing a single word of a document titled “How Claude Marks AI-Generated Content” that doesn’t explain, at all, how Claude marks (or will mark) AI-generated content.

## How It’s _Actually_ Going to Work

Yesterday, on an entirely different website than [the original](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) “How Claude marks AI-generated content” article (the one that didn’t explain anything at all about how it works), Anthropic published “[How Claude’s Text Watermark W

> 抓取方式：opencli web read（2026-08-17）。完整原文见上方链接。
