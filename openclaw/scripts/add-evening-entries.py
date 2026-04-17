import json, datetime, re, os

PROJECT_ROOT = "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes"
ENTRIES_FILE = os.path.join(PROJECT_ROOT, "data", "entries.json")
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")

with open(ENTRIES_FILE, encoding='utf-8') as f:
    entries_data = json.load(f)

existing_urls = {e.get('url') for e in entries_data['entries'] if e.get('url')}

def extract_images(content):
    return re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

def make_entry(id, title, url, platform, author, orig_date, category, tags,
               source_type, language, summary_zh, summary_en, quality,
               local_path, content_file):
    with open(os.path.join(CONTENT_DIR, f"{id}.md"), encoding='utf-8') as f:
        content = f.read()
    images = extract_images(content)
    today = datetime.date.today().isoformat()
    return {
        "id": id,
        "title": title,
        "url": url,
        "source": {
            "platform": platform,
            "author": author,
            "original_date": orig_date
        },
        "category": category,
        "tags": tags,
        "source_type": source_type,
        "language": language,
        "summary_zh": summary_zh,
        "summary_en": summary_en,
        "one_liner": None,
        "one_liner_author": "openclaw",
        "quality_score": quality,
        "status": "active",
        "local_path": local_path,
        "images": images[:5],
        "added_date": today,
        "updated_date": None,
        "github_stars": None,
        "related": []
    }

entries_to_add = []

# Entry 1: Claude Code vs Codex
id1 = "a23ba478"
url1 = "https://x.com/shao__meng/status/2044769904608604295"
if url1 not in existing_urls:
    entries_to_add.append(make_entry(
        id=id1,
        title="Claude Code vs Codex: 两种AI编程助手的深度对比",
        url=url1,
        platform="x",
        author="shao__meng",
        orig_date="2026-04-17",
        category="coding-ai/claude-code",
        tags=["claude-code", "codex", "openai", "coding-agents", "anthropic", "productivity", "code-quality", "engineering-workflow"],
        source_type="x_post",
        language="zh",
        summary_zh="基于 Reddit 真实数据(Claude Code Opus 4.6 ~100小时 vs Codex GPT-5.4 ~20小时，8万行 Python/TypeScript，2800测试用例)的深度对比。发现两种截然不同的工程师人格:Claude Code 像赶工期的资深工程师，速度快3-4倍但倾向堆砌技术债务;Codex 像稳妥的5-6年经验开发者，深思熟虑但交付质量更高。作者提出实用的互补工作流:用 Claude Code 快速原型探索，Codex 重构架构补测试。核心结论:AI 编程助手是放大器而非替代品，Claude 需要技艺精湛的驾驶员，Codex 对实时介入要求更低。",
        summary_en=None,
        quality=4,
        local_path="X 文章/2026-04-17-1200-shao__meng-Claude-Code-vs-Codex.md",
        content_file=f"{CONTENT_DIR}/{id1}.md"
    ))

# Entry 2: Claude Opus 4.7 tips
id2 = "654d1a18"
url2 = "https://x.com/dotey/status/2044868344256381254"
if url2 not in existing_urls:
    entries_to_add.append(make_entry(
        id=id2,
        title="Claude Opus 4.7 实用技巧与工作流程",
        url=url2,
        platform="x",
        author="dotey",
        orig_date="2026-04-17",
        category="coding-ai/claude-code",
        tags=["claude", "claude-opus", "anthropic", "claude-code", "workflow", "productivity", "auto-mode", "computer-use"],
        source_type="x_post",
        language="zh",
        summary_zh="Boris Cherny 深度使用 Claude Opus 4.7 后分享的实用技巧总结。核心功能包括:Auto mode(Claude 自动判断命令安全性并批准执行)、/fewer-permission-prompts(智能白名单)、Recaps(任务回顾)、Focus mode(隐藏中间步骤)、灵活的努力程度设定(低-max)。推荐工作流:让 Claude 验证自己的工作成果(端到端测试)，结合 /go 自定义技能实现自我测试+精简代码+PR 提交流程。引发 211 次点赞和 41 次转发的热门讨论。",
        summary_en=None,
        quality=4,
        local_path="X 文章/2026-04-17-1200-dotey-Claude-Opus-47-实用技巧与.md",
        content_file=f"{CONTENT_DIR}/{id2}.md"
    ))

# Entry 3: AI dev toolchain
id3 = "276058ca"
url3 = "https://x.com/RookieRicardoR/status/2044630408894271549"
if url3 not in existing_urls:
    entries_to_add.append(make_entry(
        id=id3,
        title="AI开发工具链完整方案推荐",
        url=url3,
        platform="x",
        author="RookieRicardoR",
        orig_date="2026-04-17",
        category="agent-frameworks/agent-infrastructure",
        tags=["agent-sdk", "claude-agent-sdk", "openai-agent-sdk", "vercel-ai-sdk", "assistant-ui", "tools-ui", "code-pilot", "memory-layer", "agent-development"],
        source_type="x_post",
        language="zh",
        summary_zh="RookieRicardoR 系统梳理当前 AI Agent 开发工具链全貌:底层(模型协议层)推荐 Claude Agent SDK(子进程方式兼容所有 Claude 协议模型)和 OpenAI Agent SDK / Vercel AI SDK / Pi-mono;上层 Runtime 推荐 assistant-ui + tools.ui(完整事件流+UI组件);开源完整方案推荐 CodePilot;记忆层建议可插拔设计(better sqlite + F5，或 markdown)。线程讨论深入，延伸至 Human-in-the-loop 审批、Wiki 模式不是真正记忆层等工程细节。",
        summary_en=None,
        quality=3,
        local_path="X 文章/2026-04-17-1200-RookieRicardoR-AI开发工具链完整方案推荐.md",
        content_file=f"{CONTENT_DIR}/{id3}.md"
    ))

# Entry 4: Claude Code 12 GitHub projects
id4 = "4b29f474"
url4 = "https://x.com/wsl8297/status/2044582054780895599"
if url4 not in existing_urls:
    entries_to_add.append(make_entry(
        id=id4,
        title="Claude Code 最强配置单: 12个 GitHub 项目推荐",
        url=url4,
        platform="x",
        author="wsl8297",
        orig_date="2026-04-17",
        category="coding-ai/claude-code",
        tags=["claude-code", "github", "lightrag", "superpowers", "obsidian-skills", "awesome-claude-code", "n8n-mcp", "tools", "productivity"],
        source_type="x_post",
        language="zh",
        summary_zh="wsl8297 推荐 12 个 GitHub 项目用于配置 Claude Code: LightRAG(知识图谱)、Superpowers(Claude 增强)、Obsidian Skills(上下文管理)、Everything Claude Code(功能汇总)、Claude Mem(记忆)、n8n-MCP(自动化集成)、Awesome Claude Code(用法汇总)、UI UX Pro Max(设计审美)、GSD(目标导向执行)等。社区补充 Oh My Claude Code 应排第一;GSD 中 Nyquist 规则(每步60s内验证)被单独点名实用。引发 1189 次点赞、260 次转发的高热度讨论。",
        summary_en=None,
        quality=3,
        local_path="X 文章/2026-04-17-1200-wsl8297-Claude-Code最强配置单12个G.md",
        content_file=f"{CONTENT_DIR}/{id4}.md"
    ))

print(f"New entries to add: {len(entries_to_add)}")
for e in entries_to_add:
    print(f"  - {e['id']}: {e['title'][:50]}")

entries_data['entries'].extend(entries_to_add)
entries_data['last_updated'] = datetime.datetime.now().isoformat()

with open(ENTRIES_FILE, 'w', encoding='utf-8') as f:
    json.dump(entries_data, f, ensure_ascii=False, indent=2)

print("entries.json updated successfully.")
