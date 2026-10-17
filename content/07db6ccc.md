---
id: 07db6ccc
title: AI is driving a boom in modestly successful software projects
url: https://seangoedecke.com/ai-is-driving-a-boom-in-modestly-successful-software/
source: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-10-17-AK-RSS-Digest.md
added_date: 2026-10-17
category: industry
quality_score: 4
---

# AI is driving a boom in modestly successful software projects

> 原文链接: https://seangoedecke.com/ai-is-driving-a-boom-in-modestly-successful-software/
> Content fetched: 2026-10-17 — opencli web read (markdown)

## 要点 (中文)

Sean Goedecke 用约 20 个暴露安装量的市场（NVDA 辅助功能插件、HACS、Steam、浏览器插件、Nexus 模组、Blender 扩展等）对比 2022-24 与 2025-26 两个窗口：新软件总量视场景约 2-20 倍增长，头部明星项目没有同等级爆发，而“有用但不大”的中间层项目约翻倍——NVDA 千次下载级新插件翻倍、万次以上原地不动，Steam 百评级新游戏比 2024 年前多 60%。他解释为何看插件/模组市场而非大公司（大公司被现有代码量卡住、小项目想到就做），以及为何“AI 生成”自愿披露率不可靠，结论是 AI 把“几百到几千人需要的小项目”结构性翻倍，但产品构想本身仍是稀缺资源。

## Key claims (English)

Using ~20 marketplaces that expose install counts (NVDA plugins, HACS, Steam, browser extensions, Nexus mods, Blender addons), Sean Goedecke compares 2022-24 vs 2025-26: total new software grew 2-20x depending on the venue, with roughly 2x growth in modestly successful projects but no comparable boom in megahits — thousand-download NVDA plugins doubled while 10k+ stayed flat, and Steam's 100-review new games are up 60% vs pre-2024. He argues AI structurally doubles the layer of small useful projects, while product ideas remain the scarce resource.

## Obsidian 证据摘录

> 在 20 多个暴露安装量的市场上把 2022-2024 与 2025-2026 两个窗口做了对比,看到的是中间那层“有用但不大”的项目几乎翻倍,头部明星应用没有同等级别的爆发……AI 这一波把“几百到几千人需要的小项目”翻了一倍,这是结构性的好事,但产品构想本身就是稀缺资源
> —— OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-10-17-AK-RSS-Digest.md

## 原文抓取


If AI is so great, why aren’t we seeing an explosion of new, amazing software products? If anyone can turn their idea into working software with coding agents, [where is all that software](https://www.natemeyvis.com/where-is-all-the-new-good-software/)? People have been [asking](https://mikelovesrobots.substack.com/p/wheres-the-shovelware-why-ai-coding) [this question](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html) for years. As far as I can tell, the answer is that it’s spread out over a lot of modestly successful projects:

-   Somewhere between 2x and 20x new software is being created, depending on where you look
-   There’s no real growth in massively successful software projects (not counting AI tools)
-   There is around 2x growth in modestly successful software projects

### Where all the new software is[](#where-all-the-new-software-is)

I picked[1](#fn-1) around twenty separate sources — software marketplaces, plugin registries, modding platforms, etc — which [expose](https://github.com/sgoedecke/where-is-the-software/blob/main/WRITEUP.md) installation counts. I then compared the number[2](#fn-2) of successful software projects between 2022-24 and 2025-26: i.e. before and after agentic coding hit the mainstream in mid-2025.

There’s a clear jump in _modestly_ (not wildly) successful projects. For instance, the NVDA screen-reader [addons directory](https://nvda-addons.org/) had a bit over twice as many new addons with more than a thousand downloads (though no change in addons with more than ten thousand). The HACS open-source home automation [community plugins store](https://www.hacs.xyz/) likewise saw twice as many new addons with over a hundred installs but no change in ones with over a thousand. New Steam games with over a hundred reviews are about 60% more common now than pre-2024. Obsidian plugins, Firefox and Chrome extensions, Nexus game mods, and Blender extensions had the same pattern. The Google Play store, WordPress plugins, and a few others didn’t show this pattern, but I think it’s still enough to conclude that AI is indeed driving a boom in hobbyist software.

[![data](https://www.seangoedecke.com/static/4f91bc34d50bc74f627d5c0b46f4889c/fcda8/data.png "data")](https://www.seangoedecke.com/static/4f91bc34d50bc74f627d5c0b46f4889c/0c1c2/data.png)

### Why addons and plugins?[](#why-addons-and-plugins)

I think examining addons, mods, and plugins is useful for a few reasons. First, it’s usually pretty easy to tell how many people are using them, or at least have installed them. Obviously AI is letting people 
