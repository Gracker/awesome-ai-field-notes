# 浏览器Agent

Browser Agents — 4 条活跃资源

### [Scrapling: 自适应 Web 抓取框架](https://github.com/D4Vinci/Scrapling) 
by @D (2026-02-27) | ⭐⭐⭐⭐ 4/5 | 🌐

**自适应网页抓取框架，自带反反爬和 MCP 支持**

自适应网页抓取框架，从单次请求到全量并发爬取。解析器能在页面结构变化后重新定位元素，抓取器提供反反爬能力（如 Cloudflare 绕过）。Spider 系统支持并发、多会话路由、断点续跑、代理轮换和流式输出。适合生产级数据流水线。支持 MCP 集成。
 `scraping` `anti-bot` `cloudflare-bypass` `spider` `mcp`

---
### [一句话让 Agent 接入全网语义搜索与多平台读取](https://github.com/Panniantong/Agent-Reach) 
by @Neo Reid (2026-02-25) | ⭐⭐⭐ 3/5 | 🇨🇳

**一键给 Agent 接入多平台数据源，免费且模块可替换**

Agent Reach：一句安装指令快速获得 Web、Twitter/X、YouTube、Reddit、B站、RSS 等读取与搜索能力。免费优先、可替换渠道实现、带 doctor 诊断命令。每个平台独立模块，便于后续替换底层工具。降低 Agent 联网能力搭建门槛。
 `agent-reach` `multi-platform` `search` `mcp` `data-access`

---
### [Browser Use CLI 2.0 - AI 操作浏览器调研报告](#) 
by @高爷 (2026-03-23) | ⭐⭐⭐ 3/5 | 🇨🇳

**为AI agent设计的浏览器自动化工具，零成本复用Chrome登录态，语义理解替代脆弱的CSS selectors**

Browser Use CLI 2.0调研报告——一个为AI agents设计的浏览器自动化工具。核心特点：AI-First设计（语义理解替代CSS selectors）、自然语言驱动、持久化Daemon（50ms延迟）、支持复用本地Chrome登录态。与Playwright/Selenium对比，在AI集成和登录态复用上有显著优势。支持OpenAI/Anthropic/Google/本地模型。工作流集成潜力：SaaS控制台自动化、电商后台、招聘网站、财务录入等场景。
 `browser-use` `浏览器自动化` `AI-Agent` `Playwright` `CLI` `Selenium`

---
### [Browser Use 在 OpenClaw 环境的集成分析](#) 
by @高爷 (2026-03-23) | ⭐⭐⭐ 3/5 | 🇨🇳

**Browser Use集成OpenClaw的可行性分析，定位登录态复用和多步骤浏览器操作两大高价值场景**

分析Browser Use在OpenClaw环境中的集成可行性。盘点现有浏览器相关工具（OpenCLI、web_fetch、r.jina.ai）及其限制。Browser Use的核心优势场景：需要登录的网站数据抓取（知乎/掘金/即刻/星球）、复杂表单填写、多步骤浏览器操作（Perfetto分析流程）、需保持会话状态的任务。技术限制包括需要Python环境和LLM API。
 `browser-use` `OpenClaw` `浏览器自动化` `工具集成` `OpenCLI`

---