---
title: 'NevaMind-AI/memU'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# NevaMind-AI/memU

> AI 实践：NevaMind-AI/memU

🔗 [原文链接](https://github.com/NevaMind-AI/memU") | @NevaMindAI |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-03-02

`agent` `memory` `context-management` `github`

---

## English

memU is a memory framework built for 24/7 proactive agents.
It is designed for long-running use and greatly reduces the LLM token cost of keeping agents always online, making always-on, evolving agents practical in production systems.
memU continuously captures and understands user intent. Even without a command, the agent can tell what you are about to do and act on it by itself.
[memU Bot](https://github.com/NeVaMind-AI/memUBot) — Now open source. The enterprise-ready OpenClaw. Your proactive AI assistant that remembers everything.
- Download-and-use and simple to get started (one-click install, Try now: [memu.bot](https://memu.bot) · Source: [memUBot on GitHub](https://github.com/NeVaMind-AI/memUBot)
memU treats memory like a file system—structured, hierarchical, and instantly accessible.
File System
memU Memory
🏷️ Categories (auto-organized topics)
🧠 Memory Items (extracted facts, preferences, skills)
🔄 Cross-references (related memories linked)
📥 Resources (conversations, documents, images)
Why this matters:
- Navigate memories like browsing directories—drill down from broad categories to specific facts
- Mount new knowledge instantly—conversations and documents become queryable memory
- Cross-link everything—memories reference each other, building a connected knowledge graph
- Persistent & portable—export, backup, and transfer memory like files
memory/
├── preferences/
│   ├── communication_style.md
│   └── topic_interests.md
├── relationships/
│   ├── contacts/
│   └── interaction_history/
├── knowledge/
│   ├── domain_expertise/
│   └── learned_skills/
└── context/
├── recent_conversations/
└── pending_tasks/
Just as a file system turns raw bytes into organized data, memU transforms raw interactions into structured, searchable, proactive intelligence.
If you find memU useful or interesting, a GitHub Star ⭐️ would be greatly appreciated.
Capability
Description
🤖 24/7 Proactive Agent
Always-on memory agent that works continuously in the background—never sleeps, never forgets
🎯 User Intention Capture
Understands and remembers user goals, preferences, and context across sessions automatically
💰 Cost Efficient
Reduces long-running token costs by caching insights and avoiding redundant LLM calls
---
## Architecture Overview
The memU system operates through a continuous sync loop between the main agent and the memory bot:
```
USER QUERY
↓     ↓
🤖 MAIN AGENT ◄───► 🧠 MEMU BOT
↑     ↑
PLAN & EXECUTE   MONITOR, MEMORIZE & PROACTIVE INTELLIGENCE
```
### Key Features:
1. **Proactive Content Monitoring**
- Tracks user interests and research patterns
- Automatically surfaces relevant new content
- Learns topic preferences from browsing behavior
2. **Communication Pattern Learning**
- Builds response templates for common scenarios
- Identifies priority contacts and urgent keywords
- Adapts communication style based on learned preferences
3. **Market Context Awareness**
- Learns trading preferences from historical decisions
- Provides proactive alerts based on defined thresholds
- Correlates news events with portfolio impact
---
## Proactive Behaviors
### Content Recommendations
The system monitors user research patterns and automatically suggests relevant content:
```
User researching AI topics → New RAG optimization papers found
↓
Agent surfaces papers aligned with recent research
↓
Highlights relevant authors and their latest work
```
### Email Management
MemU learns from email patterns over time:
- Auto-drafts context-aware responses
- Categorizes and prioritizes inbox
- Detects scheduling conflicts
- Summarizes long threads with key decisions
### Investment Monitoring
- Tracks market movements against user preferences
- Provides proactive alerts based on thresholds
- Learns from executed vs ignored recommendations
---
## Technical Implementation
### Three-Layer Memory System
| Layer | Reactive Use | Proactive Use |
|-------|-------------|--------------|
| Resource | Direct access to original data | Background monitoring for new patterns |
| Item | Targeted fact retrieval | Real-time extraction from ongoing interactions |
| Category | Summary-level overview | Automatic context assembly for anticipation |
### API Endpoints
- **POST /api/v3/memory/memorize** - Register continuous learning task
- **GET /api/v3/memory/memorize/status/{task_id}** - Check processing status
- **POST /api/v3/memory/categories** - List auto-generated categories
- **POST /api/v3/memory/retrieve** - Query memory with proactive context loading
### Retrieval Methods
**RAG (Fast Context)**
- ⚡ Milliseconds response time
- 💰 Embedding-only cost
- Best for: Real-time suggestions
**LLM (Deep Reasoning)**
- 🐢 Seconds response time
- 💰💰 LLM inference cost
- Best for: Complex anticipation
### Installation & Usage
```bash
pip install -e .
# Test with OpenAI API key
export OPENAI_API_KEY=your_api_key
python examples/example_1_conversation_memory.py
```
### Supported Features
- **Continuous Learning**: Processes inputs in real-time with immediate memory updates
- **Proactive Filtering**: User-specific and multi-agent context awareness
- **Custom LLM Support**: Supports OpenRouter, custom embeddings, and vision models
- **Multi-modal Support**: Handles conversations, documents, images, videos, and audio
---
## Example Implementations
### Conversation Memory
```python
export OPENAI_API_KEY=your_api_key
python examples/example_1_conversation_memory.py
```
**Proactive Behaviors:**
- Automatically extracts preferences from casual mentions
- Builds relationship models from interaction patterns
- Surfaces relevant context in future conversations
- Adapts communication style based on learned preferences
### Skill Extraction
```python
export OPENAI_API_KEY=your_api_key
python examples/example_2_skill_extraction.py
```
**Proactive Behaviors:**
- Learns from execution logs and interaction history
- Suggests optimizations based on patterns
- Extracts reusable skills from successful task completions
- Continuously improves performance metrics

## 中文

memU 是为 24/7 主动代理构建的记忆框架。
它专为长时间运行而设计，大大降低了保持代理始终在线的 LLM token 成本，使始终保持在线、不断发展的代理在实际生产系统中变得实用。

memU 持续捕获并理解用户意图。即使没有命令，代理也能告诉您将要做什么并自主行动。

memU 将记忆视为文件系统——结构化的、分层的、即时可访问的。

文件系统
memU 记忆

📁 文件夹
🏷️ 类别（自动组织的主题）

📄 文件
🧠 记忆项（提取的事实、偏好、技能）

🔗 符号链接
🔄 交叉引用（相关记忆链接）

📂 挂载点
📥 资源（对话、文档、图像）

为什么这很重要：

- 像浏览目录一样导航记忆——从广泛类别到具体事实逐层深入
- 即时挂载新知识——对话和文档变成可查询的记忆
- 交叉链接一切——记忆相互引用，构建连接的知识图谱
- 持久且可移植——像文件一样导出、备份和传输记忆

memU 的三层系统既支持响应式查询，也支持主动上下文加载：

| 层级 | 响应式使用 | 主动使用 |
|------|------------|----------|
| 资源 | 直接访问原始数据 | 背景监控新模式 |
| 项目 | 目标化事实检索 | 从持续交互中实时提取 |
| 类别 | 概述级别概览 | 为预期自动组装上下文 |

memU 的主要功能：

🤖 24/7 主动代理：永远在线的记忆代理，在后台持续工作——永不睡眠，永不忘记
🎯 用户意图捕获：自动跨会话理解和记住用户目标、偏好和上下文
💰 成本高效：通过缓存洞察和避免冗余 LLM 调用来降低长时间运行成本

### 架构概览

memU 系统通过主代理和记忆机器人之间的连续同步循环运行：

```
用户查询
     ↓     ↓
🤖 主代理 ◄───► 🧠 memU 机器人
     ↑     ↑
计划与执行   监控、记忆与主动智能
```

### 主要功能：

1. **主动内容监控**
   - 跟踪用户兴趣和研究模式
   - 自动推送相关新内容
   - 从浏览行为中学习主题偏好

2. **通信模式学习**
   - 为常见场景构建响应模板
   - 识别优先联系人和紧急关键词
   - 根据学习的偏好调整通信风格

3. **市场上下文感知**
   - 从历史决策中学习交易偏好
   - 根据定义的阈值提供主动警报
   - 将新闻事件与投资组合影响关联

### API 端点：

- POST /api/v3/memory/memorize - 注册持续学习任务
- GET /api/v3/memory/memorize/status/{task_id} - 检查处理状态
- POST /api/v3/memory/categories - 列出自动生成的类别
- POST /api/v3/memory/retrieve - 查询记忆（支持主动上下文加载）

### 检索方法

**RAG（快速上下文）**
- ⚡ 毫秒级响应时间
- 💰 仅嵌入成本
- 适用于：实时建议

**LLM（深度推理）**
- 🐢 秒级响应时间
- 💰💰 LLM 推理成本
- 适用于：复杂预期

### 安装与使用

```bash
pip install -e .

# 使用 OpenAI API key 测试
export OPENAI_API_KEY=your_api_key
python examples/example_1_conversation_memory.py
```

### 示例实现

**对话记忆**
从对话中自动提取偏好并建立关系模型，在未来的对话中推送相关上下文。

**技能提取**
从执行日志和交互历史中学习，根据模式建议优化，从成功的任务完成中提取可重用技能。
