---
title: 'Scrapling: 自适应 Web 抓取框架'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# Scrapling: 自适应 Web 抓取框架

> 自适应网页抓取框架，自带反反爬和 MCP 支持

🔗 [原文链接](https://github.com/D4Vinci/Scrapling) | @D | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`scraping` `anti-bot` `cloudflare-bypass` `spider` `mcp`

---

# Scrapling: 自适应 Web 抓取框架

## English

# Scrapling: 自适应Web抓取框架

## 中文

# Scrapling: 自适应Web抓取框架

🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

## 核心特性

### 智能解析
- **自适应学习**: 从网站变化中学习，自动重新定位元素
- **灵活选择**: CSS选择器、XPath选择器、基于过滤器的搜索
- **相似元素查找**: 自动定位与找到元素相似的元素

### 强大的抓取器
- **HTTP请求**: 快速且隐蔽的HTTP请求
- **动态加载**: 支持完整浏览器自动化
- **反机器人绕过**: 高级隐蔽功能和指纹欺骗

### 爬虫框架
- **并发爬取**: 可配置的并发限制
- **多会话支持**: 统一接口，支持HTTP请求和隐蔽无头浏览器
- **暂停/恢复**: 基于检查点的爬取持久性

## 主要功能

### 🔍 智能元素跟踪
使用智能相似算法在网站更改后重新定位元素。

### 🛡️ 反机器人系统绕过
- **Cloudflare Turnstile**: 自动绕过所有类型的Cloudflare
- **指纹欺骗**: 伪装浏览器TLS指纹、头部
- **会话管理**: 持久会话支持，跨请求管理和状态维护

### 🚀 性能优化
- **闪电般快速**: 优化性能，超越大多数Python抓取库
- **内存高效**: 优化的数据结构和延迟加载
- **快速JSON序列化**: 比标准库快10倍

## 企业集成

### 专业反机器人解决方案
企业级保护，支持Akamai、DataDome、Kasada和Incapsula的有效 antibot令牌生成。

### 代理服务
- **住宅代理**: 快速住宅和ISP代理，195+位置
- **代理轮换**: 内置代理轮换器，支持循环或自定义轮换策略
- **域名阻塞**: 阻止对特定域名的请求

## MCP服务器集成

内置MCP服务器，支持AI辅助Web抓取和数据提取：
- 功能强大的自定义功能
- 利用Scrapling提取目标内容
- 传递给AI，加速操作并减少令牌使用

## 使用示例

### 基本HTTP请求
```python
from scrapling.fetchers import Fetcher
page = Fetcher.get('https://example.com')
data = page.css('.product').getall()
```

### 高级隐蔽模式
```python
from scrapling.fetchers import StealthyFetcher
page = StealthyFetcher.fetch('https://example.com', headless=True, network_idle=True)
```

### 完整爬虫
```python
from scrapling.spiders import Spider
class MySpider(Spider):
    name = "demo"
    start_urls = ["https://example.com/"]
    async def parse(self, response):
        for item in response.css('.product'):
            yield {"title": item.css('h2::text').get()}
MySpider().start()
```

## 生态系统

### 代理服务商
- BirdProxies: 195+位置，公平定价
- Hyper Solutions: 企业级反机器人解决方案
- TikHub.io: 900+稳定API，16+平台

### 开发者工具
- **交互式Web抓取Shell**: 内置IPython shell
- **自动选择器生成**: 为任何元素生成强大的CSS/XPath选择器
- **类型覆盖**: 完整的类型提示支持

## 现状
- **GitHub趋势**: 在GitHub Trending上表现优异
- **测试覆盖**: 92%测试覆盖率
- **活跃使用**: 过去一年被数百个网页抓取者日常使用
- **社区支持**: 活跃的开发社区和完整的文档支持
