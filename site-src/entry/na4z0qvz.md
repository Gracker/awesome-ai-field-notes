---
title: 'AI编程工具 System Prompt 大合集'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# AI编程工具 System Prompt 大合集

> AI 实践：AI编程工具 System Prompt 大合集

🔗 [原文链接](https://x.com/frxiaobei/status/2029561950322168284) | @凡人小北 |  | ⭐⭐⭐ 3 ⭐3 3/5 📅 2026-03-06

`claude` `cursor` `agent` `system-prompt` `github` `AI` `SystemPrompt` `GitHub`

---

# AI编程工具 System Prompt 大合集

## 简介
这是一个由削微寒（frxiaobei）整理的 AI 编程工具系统提示词大合集，收录了 35+ 主流及新兴 AI 编程工具的系统提示词和模型设计资料。

## 项目特色
- **覆盖较全**：收录 35+ 主流与新兴 AI 工具资料
- **持续更新**：持续跟踪新的提示词版本与工具变化
- **中文友好**：面向中文开发者做本地化整理
- **实用导向**：兼顾学习价值与实际参考价值
- **结构清晰**：按工具类型和用途分类整理

## 收录的工具类别

### 代码编辑器与 IDE 集成工具
- Cursor
- VSCode Agent
- Windsurf
- Xcode
- Augment Code
- Trae

### AI 编程助手与代理
- Devin AI
- Replit
- v0
- Bolt.new
- Claude Code
- Cline
- RooCode

### 主流大模型系统提示词
- ChatGPT（OpenAI）
- Grok（xAI）
- Claude（Anthropic）
- Gemini（Google）

### 国内厂商相关工具
- 豆包 / Trae（字节跳动）
- Qoder（阿里）
- CodeBuddy（腾讯）
- Z.ai（智谱）
- Kimi（月之暗面）

### 专业开发与生成平台
- Lovable
- Same.dev
- Manus Agent
- Leap.new
- Amp

### 新兴 AI 工具
- Kiro
- Emergent
- Traycer AI
- Poke
- dia
- Junie

### 企业与效率工具
- Notion AI
- Perplexity

### 开发辅助工具
- Comet Assistant
- Cluely
- Orchids.app
- Warp.dev

### 开源项目与公开提示词
- Bolt
- Cline
- RooCode
- Lumo
- Gemini CLI
- Codex CLI

## 使用价值

### 学习参考
- 了解 AI 编程工具的内部工作方式
- 优化与 AI 工具的交互方式
- 为开发类似产品提供参考
- 学习 AI Agent / Copilot 的设计思路

### 实际应用
- 代码审查辅助
- Bug 排查与修复
- 重构与优化
- 文档生成
- 信息组织方法研究

### 对比分析
- 对比不同工具在提示词设计上的差异
- 研究工具如何组织上下文、拆解问题与调用工具
- 观察不同 AI 助手如何处理代码结构调整
- 借鉴系统提示词中对解释、总结与输出格式的约束方式

## 项目结构
```
.
├── Anthropic/          # Claude 系列（含 Claude Code）
├── OpenAI/            # OpenAI 模型、Agents
├── ChatGPT/           # ChatGPT 提示词
├── Grok（xAI）/        # Grok 个性化提示词
├── Google/            # Google AI 工具集合
├── Cursor Prompts/    # Cursor 编辑器提示词
├── Devin AI/          # Devin AI 系统提示词
├── v0 Prompts and Tools/ # v0 提示词
├── 字节跳动（ByteDance）/ # 字节系工具
├── 阿里 Qoder/         # 阿里 Qoder 系列
├── 智谱清言（Z.ai）/   # Z.ai 代码助手
├── 月之暗面（Moonshot AI）/ # Kimi 相关
└── ...                # 更多工具类别
```

## 贡献方式

### 新增工具
1. Fork 本仓库
2. 为对应工具创建目录
3. 按现有结构添加文件：
   - Tool Name/Prompt.txt
   - Tool Name/Tools.json（如适用）
   - Tool Name/[Version].txt
4. 提交 Pull Request

### 文件规范
- 核心提示词放在 Prompt.txt
- 工具/函数定义放在 Tools.json
- 特定版本提示词按版本号命名

## 更新计划
- 继续审阅并分批提交新增资料
- 补充更适合中文开发者的 Rules 与实践建议
- 引入更明确的目录规范和协作记录
- 补充自动化校验脚本

---

*本合集来自削微寒（frxiaobei）的整理，项目地址：https://github.com/CreatorEdition/system-prompts-and-models-of-ai-tools-chinese*
