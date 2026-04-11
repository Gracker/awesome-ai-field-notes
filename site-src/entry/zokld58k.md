---
title: 'Google Gemma-4-31B 模型被彻底破解'
sidebar: false
---

::: info
[← 返回模型](/models)
:::

# Google Gemma-4-31B 模型被彻底破解

> Gemma-4-31B 越狱版本出炉，HarmBench 93.7%，本地无审查新选择

🔗 [原文链接](https://x.com/Lonely__MH/status/2040832951206961413) | @Lonely__MH | 🇨🇳 | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-04-10

`gemma` `jailbreak` `open-source` `harmbench` `safety`

---

## English

https://scrapling.readthedocs.io

Effortless Web Scraping for the Modern Web

Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl.

Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers bypass anti-bot systems like Cloudflare Turnstile out of the box. And its spider framework lets you scale up to concurrent, multi-session crawls with pause/resume and automatic proxy rotation - all in a few lines of Python. One library, zero compromises.

Blazing fast crawls with real-time stats and streaming. Built by Web Scrapers for Web Scrapers and regular users, there's something for everyone.

from scrapling.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher
StealthyFetcher.adaptive = True
p = StealthyFetcher.fetch('https://example.com', headless=True, network_idle=True) # Fetch website under the radar!
products = p.css('.product', auto_save=True) # Scrape data that survives website design changes!
products = p.css('.product', adaptive=True) # Later, if the website structure changes, pass adaptive=True to find them!

Or scale up to full crawls

from scrapling.spiders import Spider, Response

class MySpider(Spider):
 name = "demo"
 start_urls = ["https://example.com/"]

 async def parse(self, response: Response):
 for item in response.css('.product'):
 yield {"title": item.css('h2::text').get()}

MySpider().start()

## 中文

https://scrapling.readthedocs.io

现代网络爬虫的轻松解决方案

Scrapling 是一个自适应的网络爬虫框架，可以处理从单个请求到大规模爬取的各种任务。

其解析器能够从网站变化中学习，并在页面更新时自动重新定位元素。其查找器可以绕过 Cloudflare Turnstile 等反机器人系统。而其爬虫框架让您可以用几行 Python 代码扩展到并发、多会话的爬取，支持暂停/恢复和自动代理轮换——一个库，零妥协。

 blazing fast 的爬取速度，带有实时统计和流式处理。由网络爬虫开发者为网络爬虫开发者和普通用户而建，人人都能使用。

from scrapling.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher
StealthyFetcher.adaptive = True
p = StealthyFetcher.fetch('https://example.com', headless=True, network_idle=True) # 在雷达下抓取网站！
products = p.css('.product', auto_save=True) # 抓取能够 survive 网站设计变化的数据！
products = p.css('.product', adaptive=True) # 后来，如果网站结构发生变化，传入 adaptive=True 来找到它们！

或者扩展到完整的爬取

from scrapling.spiders import Spider, Response

class MySpider(Spider):
 name = "demo"
 start_urls = ["https://example.com/"]

 async def parse(self, response: Response):
 for item in response.css('.product'):
 yield {"title": item.css('h2::text').get()}

MySpider().start()

## 核心特性
- 🕷️ Scrapy 风格 Spider API：使用 start_urls、异步 parse 回调和 Request/Response 对象定义爬虫。
- ⚡ 并发爬取：可配置的并发限制、按域名限流和下载延迟。
- 🔄 多会话支持：HTTP 请求和隐形无头浏览器的统一接口——通过 ID 将请求路由到不同会话。
- 💾 暂停与恢复：基于检查点的爬取持久化。按 Ctrl+C 优雅关闭；重启时从停止的地方继续。
- 📡 流式模式：通过 async for item in spider.stream() 流式传输抓取的项目，带有实时统计——适合 UI、管道和长时间运行的爬取。
- 🛡️ 阻塞请求检测：自动检测和重试阻塞的请求，可自定义逻辑。
- 🤖 Robots.txt 兼容性：可选的 robots_txt_obey 标志，尊重 Disallow、Crawl-delay 和 Request-rate 指令，支持按域名缓存。
- 🧪 开发模式：首次运行时将响应缓存到磁盘，后续运行时重播——无需重新命中目标服务器即可迭代 parse() 逻辑。

## 查找器功能
- HTTP 请求：使用 Fetcher 类进行快速隐形的 HTTP 请求。可以模拟浏览器的 TLS 指纹、头部信息，并使用 HTTP/3。
- 动态加载：通过支持 Playwright Chromium 和 Google Chrome 的 DynamicFetcher 类进行完整的浏览器自动化，抓取动态网站。
- 反机器人绕过：使用 StealthyFetcher 和指纹欺骗的高级隐形功能。可以轻松绕过所有类型的 Cloudflare Turnstile/Interstitial 自动化检测。
- 会话管理：使用 FetcherSession、StealthySession 和 DynamicSession 类进行持久会话支持，跨请求管理 cookie 和状态。
- 代理轮换：内置 ProxyRotator，支持所有会话类型的循环或自定义轮换策略，以及每个请求的代理覆盖。

## 解析器功能
- 🔄 智能元素跟踪：使用智能相似度算法在网站变化后重新定位元素。
- 🎯 智能灵活选择：CSS 选择器、XPath 选择器、基于过滤器的搜索、文本搜索、正则搜索等。
- 🔍 查找相似元素：自动定位与找到的元素相似的元素。
- 🤖 AI 使用的 MCP 服务器：内置用于 AI 辅助网络爬虫和数据提取的 MCP 服务器。

## 性能优势
- 🚀 闪电般快速：优化的性能，超越大多数 Python 爬虫库。
- 🔋 内存高效：优化的数据结构和延迟加载，占用最少的内存。
- ⚡ 快速 JSON 序列化：比标准库快 10 倍。
- 🏗️ 经过实战检验：Scrapling 不仅具有 92% 的测试覆盖率和完整的类型提示覆盖率，而且在过去一年中已被数百个网络爬虫开发者日常使用。
