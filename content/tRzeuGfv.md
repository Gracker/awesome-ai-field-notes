# 解读 Anthropic 博文：适用于长期运行 Agents 的有效框架

> 公众号: kate人不错
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s/UgTbCsVMcG8N9VC3VRZbMg

---
# 长时间运行AI代理编码指南

> 基于 Anthropic 的 "Effective harnesses for long-running agents" 最佳实践

https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## 核心问题

![Image](images/img_001.png)

当AI代理执行复杂任务（需要数小时甚至数天）时，面临一个核心挑战：

> **每个新的上下文窗口开始时，代理对之前发生的事情毫无记忆。**

想象一个软件项目由轮班工程师负责，每个新工程师到达时都不记得上一班发生了什么。

### 主要失败模式

![Image](images/img_002.png)

1.  **一次性尝试完成所有事情** - 代理试图一口气完成整个应用，导致上下文耗尽，功能半途而废

2.  **过早宣布完成** - 看到一些进展后就声明任务完成

3.  **缺乏适当测试** - 标记功能完成但未进行端到端测试

4.  **环境状态混乱** - 留下有bug或未记录的代码


* * *

## 解决方案架构

![Image](images/img_003.png)

采用**双代理架构**来解决长时间运行问题：

![Image](images/img_004.png)

* * *

## 初始化代理

初始化代理在**第一次运行**时执行，负责搭建整个项目的基础架构。

### 核心职责

![Image](images/img_005.png)

### init.sh 示例

`#!/bin/bash # init.sh - 环境初始化脚本 # 安装依赖 npm install # 启动开发服务器 npm run dev & # 等待服务器启动 sleep 5 # 基础健康检查 curl -f http://localhost:3000 || exit 1 echo"✅ 开发环境已就绪" `

* * *

## 编码代理

编码代理在**每个后续会话**中运行，负责增量完成功能。

### 会话启动流程

![Image](images/img_006.png)

![Image](images/img_007.png)

### 增量开发原则

> ⚠️ **关键原则：每次只开发一个功能**

这是解决"一次性尝试完成所有事情"问题的核心策略。

* * *

## 关键文件结构

### 1\. feature\_list.json

功能列表文件，记录所有待实现的功能及其状态：

`{   "features": [     {       "id": "F001",       "category": "functional",       "description": "用户可以创建新对话",       "priority": 1,       "steps": [         "导航到主界面",         "点击'新对话'按钮",         "验证创建了新对话",         "检查聊天区域显示欢迎状态",         "验证对话出现在侧边栏"       ],       "passes": false     },     {       "id": "F002",       "category": "functional",       "description": "用户可以发送消息并收到AI回复",       "priority": 2,       "steps": [         "在输入框输入消息",         "点击发送按钮或按回车",         "验证消息显示在对话中",         "等待AI回复",         "验证AI回复正确显示"       ],       "passes": false     }   ] } `

> 🚫 **严格规则**：只能修改 `passes` 字段，不得删除或修改测试内容！

### 2\. claude-progress.txt

进度日志文件，记录每个会话的工作内容：

`# Claude 开发进度日志 ## 2025-12-05 会话 1 - ✅ 初始化项目结构 - ✅ 配置开发环境 - ✅ 实现基础路由 ## 2025-12-05 会话 2 - 🔧 修复了登录页面的样式问题 - ✅ 完成用户认证功能 (F001) - 📝 下一步：实现对话创建功能 (F002) ## 待解决问题 - [ ] 移动端响应式布局需要优化 - [ ] 消息发送需要添加加载状态 `

### 3\. 项目目录结构

![Image](images/img_008.png)

* * *

##

环境管理的三大支柱

![Image](images/img_009.png)

### 测试驱动开发

![Image](images/img_010.png)

* * *

## 常见问题与解决方案

### 问题对照表

问题

初始化代理行为

编码代理行为

过早宣布项目完成

创建详细的功能列表文件

开始时读取功能列表，选择单个功能开发

环境状态混乱

初始化Git仓库和进度文件

开始时读取进度文件和Git日志，运行基础测试捕获bug

功能标记完成太早

设置功能列表文件

自我验证所有功能，只在仔细测试后才标记为"通过"

不知道如何运行应用

编写init.sh脚本

开始时读取init.sh

### 状态恢复策略

![Image](images/img_011.png)

* * *

## 实践清单

### 初始化代理清单

-   \[ \] 分析用户需求，拆分为具体功能（建议100+个细粒度功能）

-   \[ \] 创建 `feature_list.json`，所有功能初始状态为 `"passes": false`

-   \[ \] 创建 `init.sh` 启动脚本

-   \[ \] 创建 `claude-progress.txt` 进度文件

-   \[ \] 初始化 Git 仓库并创建首次提交

-   \[ \] 记录项目结构和运行方式


### 编码代理清单（每次会话）

**开始时：**

-   \[ \] 运行 `pwd` 确认工作目录

-   \[ \] 读取 `claude-progress.txt` 了解最近进展

-   \[ \] 读取 `feature_list.json` 查看待完成功能

-   \[ \] 查看 `git log --oneline -20` 了解代码历史

-   \[ \] 运行 `init.sh` 启动开发环境

-   \[ \] 运行基础功能测试


**开发时：**

-   \[ \] 每次只选择**一个**功能开发

-   \[ \] 实现功能后进行端到端测试

-   \[ \] 使用浏览器自动化工具验证UI功能


**结束时：**

-   \[ \] 只有测试通过才将 `passes` 设为 `true`

-   \[ \] 更新 `claude-progress.txt`

-   \[ \] 创建描述性的 Git 提交

-   \[ \] 确保代码处于可合并状态（无bug、有文档、整洁）


* * *

## 关键提示词模板

### 初始化代理提示词

`你是一个项目初始化代理。你的任务是： 1. 分析用户的需求，将其拆分为100+个具体的、可测试的功能点 2. 创建 feature_list.json 文件，列出所有功能及测试步骤 3. 创建 init.sh 脚本，用于启动开发环境 4. 创建 claude-progress.txt 进度跟踪文件 5. 初始化 Git 仓库并创建首次提交 请确保每个功能都是独立的、可增量实现的。 `

### 编码代理提示词

``你是一个编码代理，负责增量开发功能。每次会话请遵循以下流程： 1. 运行 `pwd` 确认工作目录 2. 读取 claude-progress.txt 和 git log 了解当前状态 3. 读取 feature_list.json 选择一个未完成的功能 4. 运行 init.sh 启动开发环境 5. 运行基础测试确保环境正常 开发时： - 每次只开发一个功能 - 使用浏览器自动化进行端到端测试 - 只有测试通过才将 passes 设为 true 会话结束时： - 更新 claude-progress.txt - 创建 Git 提交 - 确保代码处于干净、可合并状态 ⚠️ 严禁删除或修改 feature_list.json 中的功能定义！``

* * *

##

![Image](images/img_012.png)

## 参考资源

-   Claude Agent SDK

    https://platform.claude.com/docs/en/agent-sdk/overview

-   自主编码快速入门

    https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding


# 广告

过去我已创作了 360+篇AI主题原创内容，我对继续写作充满信心，因为这是我的爱好，我非常热爱这件事。

如果喜欢我的文章和视频，欢迎加入我的知识星球，我会分享最新的 AI 资讯、源代码，回答你的问题。我们下次再见啦！

![图片](images/img_013.other)

**最近文章，请看这里：**

**[【干货】Elon Musk与 Nikhil Kamath 访谈 2小时：涵盖 AI、财富、家庭、哲学与创业](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494427&idx=1&sn=3442a81aef11b42cb10e8f0d6b65da58&scene=21#wechat_redirect)**

**[2025 最强开源大模型？DeepSeek V3.2 正式版实测](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494422&idx=1&sn=b7779033fda35762af889714ecbece0f&scene=21#wechat_redirect)**

**[4B小模型竟能操控手机！GELab-Zero实测｜本地部署教程](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494390&idx=1&sn=7ce12bd7e7502fa36dd3d5da606771c3&scene=21#wechat_redirect)**

**[Anthropic 更新了Claude 4.x 模型提示工程最佳实践](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494362&idx=1&sn=f46db55fd854d47a84a8027cc113d0ea&scene=21#wechat_redirect)**

**[最强编码模型 Opus 价格降至 1/3，实测 Claude Opus 4.5，值不值得买单？](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494328&idx=1&sn=7ae33b016247550d67b43b1a0b4374c9&scene=21#wechat_redirect)**

**[Nano Banana Pro 实测：Gemini 3 Pro Image 中文渲染完美，海量实测案例，AI 图像生成之王](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494254&idx=1&sn=af1fb0da6b18b2734c0b7cd9fe4cfd6c&scene=21#wechat_redirect)**

**[Gemini 3 Pro 实测：编码、多模态、写作，全方位超越 GPT 5.1 | Antigravity AI IDE 体验](https://mp.weixin.qq.com/s?__biz=MzI5MjQ3ODY3Mw==&mid=2247494164&idx=1&sn=8536e15a8b7136e070f01bd63ba77754&scene=21#wechat_redirect)**