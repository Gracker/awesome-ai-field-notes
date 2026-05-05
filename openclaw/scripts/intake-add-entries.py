import json, os, datetime, re
from pipeline_utils import append_entries, content_dir, normalize_entry, normalized_url_key, project_root, save_entries_data

PROJECT_ROOT = project_root()
ENTRIES_FILE = PROJECT_ROOT / "data" / "entries.json"
CONTENT_DIR = content_dir()

with open(ENTRIES_FILE, encoding='utf-8') as f:
    entries_data = json.load(f)

existing_urls = {normalized_url_key(e.get('url')) for e in entries_data['entries'] if e.get('url')}

def extract_images(content):
    return re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

def make_entry(id, title, url, platform, author, orig_date, category, tags,
               source_type, language, summary_zh, summary_en, quality,
               local_path, content_file):
    with open(CONTENT_DIR / f"{id}.md", encoding='utf-8') as f:
        content = f.read()
    images = extract_images(content)
    today = datetime.date.today().isoformat()
    return normalize_entry({
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
        "one_liner": "Harness Engineering 是将 AI Agent 从好玩具变可靠工具的完整工程框架，为 Agent 系统提供约束、引导与纠正机制",
        "one_liner_author": "openclaw",
        "quality_score": quality,
        "status": "active",
        "local_path": local_path,
        "images": images[:5],
        "added_date": today,
        "updated_date": None,
        "github_stars": None,
        "related": []
    })

entries_to_add = []

# Entry 1: Harness Engineering
id1 = "72x6hfdeebbo"
url1 = "https://mp.weixin.qq.com/s?__biz=MzkxMTY4NTAyNQ==&mid=2247508809&idx=1&sn=960d705ab56f992ed504a2b735a2a515"
if normalized_url_key(url1) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id1,
        title="万字干货：理解 Harness Engineering，看这一篇就够了",
        url=url1,
        platform="wechat",
        author="咸鱼（TRAE 开发者用户）",
        orig_date="2026-04-11",
        category="agent-frameworks/harness-engineering",
        tags=["harness-engineering", "agent-frameworks", "prompt-engineering", "context-engineering", "reliability", "agent-infrastructure"],
        source_type="article",
        language="zh",
        summary_zh="Harness Engineering 是继 Prompt Engineering、Context Engineering 之后，由 Mitchell Hashimoto（HashiCorp 联合创始人）提出并因 OpenAI 报告而广为人知的第三类 AI 工程化方法。其核心隐喻是为 AI Agent 这匹野马套上缰绳，通过约束、引导与纠正确保其稳定运行。该框架以 R.E.S.T 四目标（可靠性、效率、安全性、可追溯性）为基石，通过上下文管理、Function Calling 降级策略、沙盒隔离与多层度量体系，将 Agent 从有趣的玩具变为可规模化的可靠生产力工具。",
        summary_en=None,
        quality=4,
        local_path="Cubox/万字干货：理解 Harness Engineering，看这一篇就够了-2026-04-11.md",
        content_file=f"{CONTENT_DIR}/{id1}.md"
    ))

# Entry 2: Scaling Managed Agents
id2 = "2plym2bh5ypl"
url2 = "https://www.anthropic.com/engineering/managed-agents"
if normalized_url_key(url2) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id2,
        title="Scaling Managed Agents: Decoupling the brain from the hands",
        url=url2,
        platform="anthropic",
        author="Lance Martin, Gabe Cemaj, Michael Cohen",
        orig_date="2026-04-11",
        category="infrastructure/managed-agents",
        tags=["managed-agents", "anthropic", "agent-infrastructure", "decoupling", "sandbox", "claude"],
        source_type="article",
        language="en",
        summary_zh="Anthropic 发布 Managed Agents，通过虚拟化 agent 的核心组件（session、harness、sandbox），将大脑（Claude + harness）与手（沙盒执行环境）解耦，实现了各组件可独立失败、替换而不影响整体系统的架构目标。其核心接口（execute、provision、wake、getSession、emitEvent）借鉴了 OS 虚拟化硬件的思路，使接口保持稳定而实现可演进。此设计使 p50 TTFT 降低约 60%，p95 降低 90% 以上，并支持多脑多手扩展。",
        summary_en="Anthropic introduces Managed Agents, which virtualizes the core components of an agent (session, harness, sandbox) to decouple the brain (Claude + harness) from the hands (sandboxed execution environments), allowing each component to fail or be replaced independently. By mirroring how operating systems virtualized hardware with stable interfaces (process, file), the core interfaces (execute, provision, wake, getSession, emitEvent) enable the implementation to evolve while keeping interfaces stable. This architecture reduced p50 TTFT by ~60% and p95 by over 90%, and supports many-brains-many-hands scaling.",
        quality=5,
        local_path="Cubox/Scaling Managed Agents- Decoupling the brain from the hands-2026-04-11.md",
        content_file=f"{CONTENT_DIR}/{id2}.md"
    ))

# Entry 3: ARIES RISCV+AI
id3 = "jvblhpoud3ey"
url3 = "https://mp.weixin.qq.com/s?__biz=MzUzNzg4Nzc3MQ==&mid=2247485969&idx=1&sn=32449a8c2513a5cb53f1ad2360b58e4a"
if normalized_url_key(url3) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id3,
        title="破局Agent时代：ARIES RISCV+AI架构分析",
        url=url3,
        platform="wechat",
        author=None,
        orig_date="2026-04-11",
        category="hardware-chips/risc-v-ai",
        tags=["risc-v", "ai-chip", "agent-era", "in-memory-computing", "cim", "aries", "isscc"],
        source_type="article",
        language="zh",
        summary_zh="ISSCC 2026 展示的 ARIES 架构代表了 AI 芯片从算力怪兽向有脑子的行动派的进化路线。ARIES 通过 RISC-V CPU 集成（调度控制前额叶）+ 280MB 大容量 SRAM + CIM 存内计算，实现 PD/AF 融合方案（拒绝 NVIDIA/Groq 的物理分离路线），以 14nm 工艺在能效比上超越 4nm GPU。其三引擎 NPU Core（TCE/TME/VCE）+ 相似性感知 TCAM + LUT 非均匀量化，构成 Agent 时代芯片的差异化竞争力。",
        summary_en=None,
        quality=4,
        local_path="Cubox/破局Agent时代：ARIES RISCV+AI架构分析-2026-04-11.md",
        content_file=f"{CONTENT_DIR}/{id3}.md"
    ))

print(f"New entries to add: {len(entries_to_add)}")
for e in entries_to_add:
    print(f"  - {e['id']}: {e['title'][:50]}")

# Append to entries
added_entries, skipped_entries = append_entries(entries_data, entries_to_add)
save_entries_data(entries_data, ENTRIES_FILE)

print(f"entries.json updated successfully: +{len(added_entries)}, skipped {len(skipped_entries)}.")
