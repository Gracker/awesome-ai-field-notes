#!/usr/bin/env python3
"""Daily intake script for AI content - June 8, 2026"""

import json
import os
import re
import datetime
from pathlib import Path
from pipeline_utils import append_entries, normalize_entry, content_dir, project_root, save_entries_data

def extract_images(content):
    """Extract image URLs from markdown content"""
    return re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

def make_entry_from_content(id, title, url, platform, author, orig_date, category, tags,
                           source_type, language, summary_zh, summary_en, quality,
                           local_path, content_filename):
    """Create a normalized entry from content"""
    content_path = content_dir() / content_filename
    if not content_path.exists():
        print(f"Warning: Content file {content_path} does not exist")
        return None
    
    with open(content_path, encoding='utf-8') as f:
        content_text = f.read()
    
    images = extract_images(content_text)
    today = datetime.date.today().isoformat()
    
    entry = {
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
        "one_liner": None,  # Will be set by normalization
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
    
    return normalize_entry(entry)

def main():
    """Process new AI content entries"""
    project_root = Path(__file__).parent
    entries_file = project_root / "data" / "entries.json"
    
    # Load existing entries
    with open(entries_file, encoding='utf-8') as f:
        entries_data = json.load(f)
    
    # Define new entries to process
    new_entries = [
        {
            "id": "anthropic_petri_3_0_2026_001",
            "title": "Anthropic 开源对齐工具 Petri 捐赠给 Meridian Labs：版本 3.0 更新",
            "url": "https://www.anthropic.com/research/donating-open-source-petri",
            "platform": "anthropic",
            "author": "AnthropicAI",
            "orig_date": "2026-05-07",
            "category": "learning/research",
            "tags": ["alignment", "petri", "anthropic", "open-source", "meridian-labs", "2026"],
            "source_type": "article",
            "language": "both",
            "summary_zh": "Anthropic将开源对齐工具Petri 3.0捐赠给Meridian Labs，新版本增强了适应性、真实性和深度评估能力。Petri 3.0支持独立调整审计员和目标模型，通过Dish组件提高测试真实性，并与Bloom工具集成进行更深入的行为评估。",
            "summary_en": "Anthropic donates Petri 3.0 to Meridian Labs, enhancing adaptability, realism, and depth assessment. The new version allows separate tweaking of auditor and target models, improves testing realism through Dish component, and integrates with Bloom for deeper behavioral assessment.",
            "quality": 4,
            "local_path": "content/65f18ea8.md",
            "content_filename": "65f18ea8.md"
        },
        {
            "id": "ai_first_reflection_2026_001", 
            "title": "反思AI-First: 99% 代码由 AI 写, 为什么产品还是输了?",
            "url": "https://x.com/JustinLin610/status/2043749803780432338",
            "platform": "x",
            "author": "JustinLin610",
            "orig_date": "2026-06-07",
            "category": "coding-agents/best-practices",
            "tags": ["ai-first", "development", "critical-thinking", "agents", "productivity", "2026"],
            "source_type": "x_post",
            "language": "zh",
            "summary_zh": "JustinLin610反思AI-First开发模式：批判性思维在Agent时代变得更为重要，人类与AI代理一起深度思考和全面分析问题；设计健康的组织和系统架构对于创建和构建至关重要；新时代往往 favors 新手，因为过去经验少，对当前困难恐惧也少。",
            "summary_en": None,
            "quality": 4,
            "local_path": "content/a8c9a35b.md",
            "content_filename": "a8c9a35b.md"
        },
        {
            "id": "enterprise_analytics_automation_2026_001",
            "title": "Paul Smith 现场观察: 普通企业数据团队也能自动化 95% 分析查询",
            "url": "https://x.com/realpaulsmith/status/2062948966291939843", 
            "platform": "x",
            "author": "realpaulsmith",
            "orig_date": "2026-06-06",
            "category": "coding",
            "tags": ["analytics", "automation", "enterprise", "data-team", "ai-tools", "2026"],
            "source_type": "x_post",
            "language": "zh",
            "summary_zh": "Paul Smith观察到普通企业数据团队也能自动化95%的分析查询。模型给出的分析答案可以通过硬数据来校验，这是大多数知识工作做不到的优势。实现不需要前沿实验室的独特技能，定义就在BI文档里，评估只需要一个下午的时间写下团队能凭记忆回答的问题。",
            "summary_en": None,
            "quality": 4,
            "local_path": "content/447e9cf2.md",
            "content_filename": "447e9cf2.md"
        },
        {
            "id": "gemini_macos_tips_2026_001",
            "title": "Gemini macOS 隐藏技巧: 双击 把当前窗口丢进对话",
            "url": "https://x.com/joshwoodward/status/2062667951485108354",
            "platform": "x", 
            "author": "joshwoodward",
            "orig_date": "2026-06-05",
            "category": "uncategorized",
            "tags": ["gemini", "macos", "tips", "productivity", "ai-tools", "2026"],
            "source_type": "x_post",
            "language": "zh",
            "summary_zh": "Gemini macOS应用支持一个隐藏功能：同时按下两个Command⌘键，可以将当前窗口无缝连接到对话中，无需手动截图或切换标签页。这为获取针对当前屏幕内容的定制化帮助提供了便捷方式。",
            "summary_en": None,
            "quality": 4,
            "local_path": "content/0e59b0eb.md",
            "content_filename": "0e59b0eb.md"
        }
    ]
    
    # Process each new entry
    processed_entries = []
    skipped_entries = []
    
    for entry_data in new_entries:
        entry = make_entry_from_content(**entry_data)
        if entry:
            processed_entries.append(entry)
        else:
            skipped_entries.append(entry_data["id"])
    
    print(f"Processed {len(processed_entries)} new entries")
    if skipped_entries:
        print(f"Skipped {len(skipped_entries)} entries: {skipped_entries}")
    
    # Add to entries using append_entries
    added_entries, duplicates = append_entries(entries_data, processed_entries)
    
    print(f"Added {len(added_entries)} new entries")
    print(f"Found {len(duplicates)} duplicates")
    
    if duplicates:
        print("Duplicates found:")
        for entry, reason in duplicates:
            print(f"  - {entry['id']}: {reason}")
    
    # Save updated entries
    save_entries_data(entries_data)
    
    # Generate one-liners for new entries
    for entry in added_entries:
        if not entry.get("one_liner"):
            # Generate simple one-liner based on title and category
            if entry["category"] == "learning/research":
                entry["one_liner"] = f"研究性AI内容：{entry['title']}"
            elif entry["category"] == "coding-agents/best-practices":
                entry["one_liner"] = f"AI编程最佳实践：{entry['title']}"
            elif entry["category"] == "coding":
                entry["one_liner"] = f"AI开发工具：{entry['title']}"
            else:
                entry["one_liner"] = f"AI技术动态：{entry['title']}"
    
    # Save again with one-liners
    save_entries_data(entries_data)
    
    return len(added_entries)

if __name__ == "__main__":
    added_count = main()
    print(f"\nDaily intake completed: {added_count} new entries added")