# Scrapling — 自适应 Web 爬虫框架

## English原文

Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl. Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers bypass anti-bot systems like Cloudflare Turnstile out of the box. And its spider framework lets you scale up to concurrent, multi-session crawls with pause/resume and automatic proxy rotation — all in a few lines of Python.

## 核心特点

Scrapling 是一个自适应网页爬虫框架，从单次请求到大规模爬取都能处理。其解析器能从网站变化中学习，当页面更新时自动重新定位目标元素。其 fetcher 内置绕过反爬虫系统（如 Cloudflare Turnstile）的能力。Spider 框架支持并发、多会话爬取，支持暂停/恢复和自动代理轮换——全部用少量 Python 代码实现。

### 主要特性

- **🕷️ 类 Scrapy 的 Spider API**：通过 start_urls、async parse callbacks 和 Request/Response 对象定义爬虫
- **⚡ 并发爬取**：可配置的并发限制、per-domain 节流和下载延迟
- **🔄 多会话支持**：统一接口处理 HTTP 请求和隐身浏览器
- **💾 暂停与恢复**：基于检查点的爬取持久化，Ctrl+C 优雅关闭
- **📡 流式模式**：通过 `async for item in spider.stream()` 实时流式处理数据
- **🛡️ 请求拦截检测**：自动检测和重试被拦截的请求
- **🤖 Robots.txt 合规**：可选的 robots_txt_obey 标志
- **🧪 开发模式**：首次运行缓存响应到磁盘，后续运行回放，无需重新请求目标服务器
- **📦 内置导出**：JSON/JSONL 格式导出

### 反爬虫绕过

- **隐身 HTTP 请求**：模拟浏览器 TLS 指纹、headers，支持 HTTP/3
- **动态加载**：通过 Playwright 的 Chromium 和 Chrome 的完整浏览器自动化
- **高级隐身模式**：StealthyFetcher 和指纹伪造，可绕过 Cloudflare Turnstile 等各种反爬机制
- **会话管理**：FetchesSession、StealthySession、DynamicSession 类的持久化会话支持
- **代理轮换**：内置 ProxyRotator 支持循环或自定义轮换策略
- **DNS 防泄露**：可选的 DNS-over-HTTPS 支持

### 智能选择器

- **🔄 智能元素追踪**：使用智能相似度算法在网站变化后重新定位元素
- **🎯 灵活选择**：CSS 选择器、XPath 选择器、过滤器搜索、文本搜索、正则搜索
- **🔍 查找相似元素**：自动定位与已找到元素相似的其他元素
- **🤖 MCP Server**：内置 MCP 服务器，支持 AI 辅助网页爬取和数据提取

### 性能

- **🚀 极速**：优化的性能超越大多数 Python 爬虫库
- **🔋 内存高效**：优化的数据结构和惰性加载
- **⚡ 快速 JSON 序列化**：比标准库快 10 倍
- **🏗️ 实战验证**：92% 测试覆盖率，完整类型提示

## 快速上手

### HTTP 请求

```python
from scrapling.fetchers import Fetcher, FetcherSession

with FetcherSession(impersonate='chrome') as session:
    page = session.get('https://quotes.toscrape.com/', stealthy_headers=True)
    quotes = page.css('.quote .text::text').getall()
```

### 高级隐身模式

```python
from scrapling.fetchers import StealthyFetcher, StealthySession

with StealthySession(headless=True, solve_cloudflare=True) as session:
    page = session.fetch('https://nopecha.com/demo/cloudflare', google_search=False)
    data = page.css('#padded_content a').getall()
```

### 构建完整爬虫

```python
from scrapling.spiders import Spider, Request, Response

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    concurrent_requests = 10

    async def parse(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                "text": quote.css('.text::text').get(),
                "author": quote.css('.author::text').get(),
            }

        next_page = response.css('.next a')
        if next_page:
            yield response.follow(next_page[0].attrib['href'])

result = QuotesSpider().start()
result.items.to_json("quotes.json")
```

## 相关链接

- 文档：https://scrapling.readthedocs.io
- GitHub：https://github.com/D4Vinci/Scrapling
- PyPI：https://pypi.org/project/scrapling/

---

来源：[D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
