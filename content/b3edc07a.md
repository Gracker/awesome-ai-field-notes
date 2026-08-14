# DecryptAds：把广告供应链拆开给你看（ads.txt/sellers.json 交叉透视）

- **ID**: b3edc07a
- **原文链接**: https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out/
- **作者**: Brian Krebs
- **日期**: 2026-08-14
- **分类**: industry
- **来源类型**: article
- **标签**: adtech, privacy, security, supply-chain, transparency
- **质量评分**: 4/5
- **抓取时间**: 2026-08-14T15:38:57Z
- **Obsidian 证据**: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-08-14-AK-RSS-Digest（89源精选）.md（评分 8.4/10，正文 17k 字符已落盘）

---

## 中文导读

Krebs 介绍免费服务 DecryptAds：抓取 ads.txt / app-ads.txt / sellers.json / buyers.json 四类公开文件做交叉引用，把任意站点的广告供应链可视化。具体数据：ESPN 背后 143 家广告方中 4 家总部在俄/中/阿联酋；armytimes.com 等 6 个美军新闻网站允许俄罗斯 Between Digital 投放；Opera 母公司 Kunlun 被识别为中方实体。文章同时把 H96 TV stick 租用户带宽伪装手机点击给 AI 农场广告的事件补上 Fengwo Group 与 Yandex seller ID 的关联。

## 为什么值得关注

不是再讲一遍「广告在追踪你」，而是给出一个能立刻查任何站点的工具 + 一组可复述的供应链安全事实，做反 malvertising / 供应链安全的工程师可直接上手。

---

## 正文存档

# Who’s Tracking You? Use This New Service to Find Out
> 原文链接: https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out/

---

It can be daunting to determine who’s responsible for showing ads on the websites we visit, or who’s harvesting data from the mobile apps we use every day. That information is already semi-public, but it is not easily parsed and traditionally much of it has remained walled away in the hands of large advertising platforms. Not anymore: A powerful and free new service called **DecryptAds** scrapes and correlates this adtech data and makes it simple to quickly learn a great deal about the entities that are tracking you.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/08/decryptads-ESPN.png)](https://krebsonsecurity.com/wp-content/uploads/2026/08/decryptads-ESPN.png)

A Decryptads summary of the advertising partnerships declared by espn.com.

The [newly launched](https://decryptads.com/blog/posts/ad-tech-transparency-launch.html) **decryptads.com** says it is constantly scraping the files that websites and apps make publicly available to disclose the companies that are permitted to run ads or collect user data. These files include:

–**ads.txt**: all of the adtech companies and data brokers that may run ads or harvest data from the site;
–**app-ads.txt**: entities that can harvest data from or display ads on mobile and smart TV apps;
–**buyers.json/sellers.json**: the entities buying, selling or reselling ad inventory for a given site or app.

**Zach Edwards** is chief research officer for DecryptAds and a threat researcher at the security company **Infoblox**. Edwards said he and two other founders decided the service was needed because the adtech data in these files is generally only useful when it can be cross-referenced to build a more complete picture of the advertising ecosystem for each website or app.

“It’s an adtech tool but we’re trying to approach adtech from a security perspective,” Edwards said. “It’s really built for a lot of privacy and security use cases that have been dramatically underserved.”

Those use cases, he said, include tracking down the source of malicious ads that try to foist malware on targeted users, identifying ad networks located in adversarial nations, and detecting the fast growing swarms of AI-generated slop websites and apps. And as decryptads.com demonstrates, these potential security and privacy threats are near impossible to detect just by viewing a single apps.txt or app-ads.txt file.

“Supply-chain integrity issues rarely live in a single file,” the site [explains](https://decryptads.com/blog/posts/analytical-features.html). “They show up as broken cross-references between ads.txt, app-ads.txt, and sellers.json files; as cloned declaration sets across unrelated domains; as seller removals that only make sense when viewed across exchanges; and even as supply paths in bid logs that never actually appear in any given publisher’s authorized-seller list.”

A search in DecryptAds for the hugely popular sports network **espn.com** reveals 143 ad partners and 19 registered data broker domains are listed within its [ads.txt](https://www.espn.com/ads.txt) and [app-ads.txt](https://www.espn.com/app-ads.txt) files. That data broker information is gradually becoming available because four states — California, Oregon, Texas and Vermont — have recently passed laws requiring data brokers to register if they buy or sell data on consumers from those states. DecryptAds reports that almost half of those data brokers are collecting geolocation data from espn.com visitors who aren’t blocking ads, while another three disclose that they collect device fingerprints and sensitive personal information.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/08/espn-supplychain.png)](https://krebsonsecurity.com/wp-content/uploads/2026/08/espn-supplychain.png)

A visual representation of the complex ad supply chain declared by espn.com. Image: decryptads.com.

## HIGH-RISK AD PARTNERS

DecryptAds also makes it easy to learn the beneficiaries and national origins of the advertising firms lurking in apps and websites, displaying a conspicuous warning when adtech partners of an app or website are based in [“geo-risk”](https://decryptads.com/geo_risk) areas like China and Russia, or in countries with strong financial and political ties to both — such as Cyprus and the United Arab Emirates (UAE).

According to DecryptAds, espn.com works with four different advertising entities that are based in either Russia, China or the UAE, including the adtech firm **Between Digital**, which lists a New York address. However, the [dossier on Between Digital](https://decryptads.com/ad_system/betweendigital.com) flags them as a Russian firm, showing that [their publisher offers](https://cp.betweendigital.com/files/PublisherOffer.pdf) (PDF) are processed through **Alfa Bank**, Russia’s largest private commercial bank and one of several financial institutions placed under U.S. sanctions in 2022 after Russia invaded Ukraine. KrebsOnSecurity sought comment from both Between Digital and the company’s founder, and will update this story in the event that either replies.

A search for several top U.S. military news websites — including [armytimes.com](https://decryptads.com/search/publisher/armytimes.com), [airforcetimes.com](https://decryptads.com/publisher/airforcetimes.com), [defensenews.com](https://decryptads.com/publisher/defensenews.com), [navytimes.com](https://decryptads.com/publisher/navytimes.com), [marinecorpstimes.com](https://decryptads.com/publisher/marinecorpstimes.com) and [federaltimes.com](https://decryptads.com/publisher/federaltimes.com) — shows they all allow Between Digital to serve ads and track users, as well as two entities in the UAE and another in the ownership secrecy haven of Panama. DecryptAds reports that Between Digital is collecting ad data on approximately 55,000 partner websites.

[![](https://krebsonse

> …（正文截断，全文见原文链接）