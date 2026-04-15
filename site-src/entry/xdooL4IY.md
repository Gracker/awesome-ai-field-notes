---
title: '新一代 Agentic AI 智能体，助力 Android 开发 | Google I/O你好，我是朱涛。今天我们来聊聊 - 掘金'
sidebar: false
---

::: info
[← 返回模型](/models)
:::

# 新一代 Agentic AI 智能体，助力 Android 开发 | Google I/O你好，我是朱涛。今天我们来聊聊 - 掘金

> Cubox 收藏 — 新一代 Agentic AI 智能体，助力 Android 开发 | Google I/O你好，我是

🔗 [原文链接](https://juejin.cn/post/7529430220152897562) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2025-07-27

---

# 新一代 Agentic AI 智能体，助力 Android 开发 | Google I/O

往期文章：

《00. 文章合集目录》

《Google Gemini 如何加速 Android 开发？》

《深入理解 Android Jetpack Lifecycle（用法篇）》

《深入理解 Jetpack Lifecycle（原理篇）》

你好，我是朱涛。今天我们来聊聊 AI 和 Android 开发的话题。

往年的 Google I/O 大会，Android 几乎每年都是主角。但是，从近两年开始，AI 在 I/O 大会的重要性逐渐提升，而今年 Google I/O 大会上，AI 已经成为了万众瞩目的主角。

这几年，以 ChatGPT 为代表的生成式 AI 发展迅猛，各个科技巨头都开发出了各自的AI。比如：OpenAI 的 ChatGPT，Google 的 Gemini，Meta 的 Llama。而对我们开发者影响最大的，应该要属 Cursor，因为它开创了 AI 编程的先河。不过，可惜的是，Cursor 在 Android 开发领域的表现一直不太突出。

而今年 Google I/O 上，Android 团队宣布对 Android Studio 做了一系列的增强。

如果你想要体验最新的 Android AI 编程工具，则需要升级到最新的 Android Studio Preview，它的版本名称叫做 Narwhal，中文意思是一角鲸。

对比几个月前的 Android Studio Meerkat 版本，一角鲸版本在 AI 功能方面做了许多增强。从某种意义上来说，确实在往 Agentic AI 的方向进化。

如果你看过我之前写的文章 《Google Gemini 如何加速 Android 开发？》，你会知道，之前版本的 Android Studio 只能简单的问答。但这次升级到 Narwhal 版本，你会看到一系列 AI 相关的介绍。

上面引导内容的大概意思就是，Android Studio 现在支持 AI Agent 模式了。接下来，我们来看看如何配置和使用吧。

首先，我们当然需要关闭 Android Studio 自带的 Assist 引导，然后点击右侧的 Gemini 图标。

点击这个图标后，就会出现 Gemini 聊天的界面了。

很明显，普通模式，就是像 ChatGPT 那样可以跟 AI 聊天。这个功能我在上一篇博客里介绍过了。今天我们重点来看看 Agent 模式。

Agent 模式下的关键配置，我已经在图片里标注了。我们从上往下一一介绍：

Agent Tab：点击这个 Tab 就可以帮助我们切换到 Agent 模式下了。那么，Agent 模式和普通模式到底有什么区别呢？用一句话概括：普通模式下，Gemini 只能和我们聊天，Agent 模式下，Gemini 一定程度接管 IDE 进行简单的操作。

API Key：Google 官方给所有 Android 开发者提供了免费使用 Gemini 的额度，但仅限于相对便宜的默认模型，如果希望使用 Gemini 的最强模型，则需要使用自己的 API Key。

选择上下文：当我们向 AI 提问的时候，大部分情况下，是会和当前工程的某些代码相关的。这里就需要我们明确指定提问的上下文信息。

选择 AI 模型：前面提到过，Google 提供的是免费默认模型，在遇到一些复杂问题的时候，AI 可能力不从心。这时候，如果你想要使用 Gemini 的最强模型，就需要你自己的 API Key 了。

更多设置：这里当前的设置非常简单，只有一个选项，是否自动允许 Agent 的操作。前面我提到过，Agent 模式下，AI 可以接管 IDE 对代码工程进行简单的操作。一般来说，我们刚开始使用 Agent 模式的时候，建议暂时不要开启，等熟悉了以后，再根据情况考虑是否要开启。目前我自己平时是不开启的。

Agent 模式具体该怎么用？其实就跟 ChatGPT 聊天差不多。只是从前我们需要自己拷贝代码，然后修改代码，然后手动运行程序查看效果，现在这些都可以交给 AI 自动完成了。

下面这个是 Google 官方提供的案例：

问题：APP 界面默认是明亮主题，希望改成默认黑暗主题。

具体该怎么做呢？其实我们只需要发一条消息给 AI：我希望把默认主题模式，改为黑暗主题。（Make dark mode the default in user preferences）

其他的，你就不用管了。 AI 会自动查找工程里的源代码，找到相关的配置文件，自动修改代码的内容，然后重新部署代码让它生效。

真香！

我在上一篇博客里，曾经用过这个例子来考验 Gemini，当时它回答的并不好。

这次我直接在 Android Studio 里创建了一个类，然后把问题丢给 Agent。

Gemini 直接在编辑器里帮我把代码改好了，然后告诉了我修复的思路：

并且，Gemini 也敏锐的发现了代码仍然有进一步优化的空间，主动提出了可以使用 Data Class 优化。

这时候我只需要动动嘴，告诉 Gemini 继续优化。

但是，Gemini 这次的修改仍然没有达到我的期望，我又继续发问了。

这次 Gemini 给出的修复已经非常不错了，并且，在后面它还贴心的附带了使用介绍。

这次实验，我使用自己的 API Key，使用的模型是 Google 最强的模型 Gemini 2.5 Pro，所以它总体的表现也非常令人满意。唯一的遗憾是，Gemini 没有一步到位帮我优化好代码，中间让我介入了两次。不过，这些其实可以通过一些通用配置来解决，我们可以通过为工程配置一些全局规则，让 Agent 更智能化的帮我们判断。理论上也可以实现一步到位的优化。

关于配置的部分，我们以后有机会再讲吧。

在使用自己的 API Key 的情况下，一定要注意使用量，还有上下文长度。在某些极端情况下，AI 烧钱速度也是会很快的，我曾经遇到过一晚上烧200美金的情况，触发 Gemini 单日消费上限后才停下来。

这里我附上 Gemini 各个模型 token 的价格，给大家参考：

看完上面的价格后，你也许会发现，Gemini 的 API Key 分为两个等级。

所以，如果你是在做一些无关紧要的业余项目，那就可以考虑使用免费的 API Key。如果是重要的项目，则最好老实付费。

说实话，对比 Cursor，当前 Android Studio 的 Agent 体验其实还差点意思。但由于 Cursor 本身对 Android 开发不太友好，这就意味着，对于我们 Android 程序员来说，Android Studio + Gemini 成为了最佳选择。

AI 编程工具可以大幅提升我们的开发效率，但 AI 也是一把双刃剑，用的不好的话，有时候会适得其反。AI 编程本身是个非常大的话题，本文的作用是为大家科普，其背后还有许多知识点需要学习。大家如果感兴趣，可以去找一些大模型相关的知识了解一些，尤其是 Prompt，它是我们驾驭 AI 的关键。

好了，今天的内容就到这。感谢你的时间，我们下次见。
