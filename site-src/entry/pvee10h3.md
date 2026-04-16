---
title: '或'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# 或

> AI 实践：或

🔗 [原文链接](https://x.com/Wuming_Mr_/status/2028419040847249428) | @WumingMr |  | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-03-03

`openclaw` `agent` `obsidian` `skill` `github`

---

# 我在 ClawHub 折腾一周后，留下这 10 个真香技能

## 先说结论
**#ClawHub 真的能把 #OpenClaw 从"会聊天的工具"升级成"能干活的员工"。**

但前提是——别乱装。

现在生态已经野蛮生长，上万个 Skills 里确实有宝藏，也有雷。踩过两个坑（一个权限乱读文件，一个 prompt 写得离谱），所以这篇是纯个人实战后的筛选清单，不是搬运榜单。

**时间**：2026年3月

**结论**：新手按这个顺序装，基本不会翻车。

---

## ✅ 第一优先级：保命四件套（先装这 4 个）

### 1️⃣ Skill Vetter（安全审计）
这玩意必须第一个装。安装新 skill 前自动扫描风险指令，相当于给 Agent 装个"防毒软件"。ClawHub 现在下载量≠安全，别太天真。

### 2️⃣ Tavily / SerpAPI（联网搜索）
没联网的 Agent，本质是信息孤岛。装完之后才真正"活过来"。查实时资讯、验证信息、抓最新数据，全靠它。

### 3️⃣ Browser / Playwright（浏览器自动化）
能自己开网页、点按钮、填表单、截图。现在很多重复性网页操作都丢给它，效率翻倍。做爬取、自动提交、监控页面变化都很好用。

### 4️⃣ Code Interpreter（Python 执行）
这是核心生产力引擎。数据分析、画图、处理文件、跑脚本，没有它很多复杂任务根本落不了地。

👉 **这四个装完，OpenClaw 才算"能干活"。**

---

## ⚙️ 第二阶段：让它真正参与工作流

### 5️⃣ File Manager（文件管理）
读写本地文件、批量改名、处理 PDF。不装它，Agent 只能"想办法"，不能"动文件"。

### 6️⃣ GitHub Assistant（Git 操作）
commit、PR、issue、review 一条龙。对开发者来说，它就是一个不摸鱼的实习生。

### 7️⃣ Notion / Obsidian 连接器（知识库）
自动建笔记、更新文档、查询知识库。装完后开始真的把它当"第二大脑"。

---

## 🚀 第三阶段：从工具到"主动员工"

### 8️⃣ Cron / Scheduler（定时任务）
每天自动跑日报、周报、数据监控。这一步是质变——它开始主动工作。

### 9️⃣ Self-Improving / Evolver（自我优化）
分析失败记录，优化 prompt。不算必需，但长期用下来会明显变聪明。

### 🔟 Daily Digest（主动日报）
每天自动整理工作总结、待办事项、行业动态。这个真的很"有陪伴感"。

---

## 🧭 安装顺序建议

**安全 → 联网 → 浏览器 → 代码**（这 4 个是基础）

然后按需求补：文件 → Git → 知识库 → 定时 → 自我进化 → 主动日报

> 别一口气全装。装一个，用两天，确认稳定再继续。

---

## 🛠 安装方式

确保先装 CLI：
```bash
npm i -g clawhub
# 或
npx clawhub@latest
```

然后按顺序装：
```bash
clawhub install skill-vetter
clawhub install tavily-search
clawhub install playwright-browser
clawhub install code-interpreter
clawhub install file-manager
clawhub install github-assistant
clawhub install notion-connector
clawhub install cron-scheduler
clawhub install self-improving
clawhub install daily-digest
```

> 装完一定要重启 OpenClaw 会话，不然很多人会以为"没生效"。

---

## 最后一点真实建议

- 别看介绍写得酷就装
- 多看评论区真实反馈
- 下载量+更新频率一起看
- 能开沙盒就别直接给全权限

现在 ClawHub 很像早期插件市场阶段——机会巨大，风险也真实存在。如果你刚入坑 OpenClaw，照这个顺序走，基本能少走很多弯路。

等你把前四件套跑顺了，再来聊怎么把 Agent 训练成真正的"数字合伙人"。

---

*本指南来自 @Wuming_Mr_ 的 X 推文*
