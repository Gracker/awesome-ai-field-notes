#!/usr/bin/env python3
"""Morning Intake - 2026-05-17 - Process FwcpbCED (Agent Memory article)"""

import json, re, sys, os
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes")
OPENCLAW_SCRIPTS = PROJECT_ROOT / "openclaw" / "scripts"
sys.path.insert(0, str(OPENCLAW_SCRIPTS))

from pipeline_utils import (
    normalize_entry, content_dir, normalize_url, normalized_url_key,
    canonical_category, normalize_source_type, normalize_tags,
    clean_text, derive_one_liner, generate_entry_id, normalize_date, today_str,
    load_entries_data, save_entries_data, entries_path,
    is_low_signal_entry, is_ai_related_entry, is_placeholder_text, has_readable_text,
    VALID_STATUSES
)

ENTRIES_FILE = PROJECT_ROOT / "data" / "entries.json"
CONTENT_DIR = PROJECT_ROOT / "content"

def load_entries_list(path):
    """Load entries.json as a list."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get('entries', [])

def save_entries_list(entries, path):
    """Save entries as a list (matching actual format)."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
        f.write('\n')

def extract_images(content):
    return re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

def extract_summary_zh(content, max_len=300):
    """Extract readable body paragraphs for summary."""
    lines = content.split('\n')
    body_lines = []
    skip_patterns = ['太长不看', '参考来源', '相关阅读', '关注', '投稿', '版权', '原文：', '作者：']
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if any(p in stripped for p in skip_patterns):
            continue
        if stripped.startswith('# ') or stripped.startswith('## ') or stripped.startswith('***'):
            continue
        if stripped.startswith('* ') or stripped.startswith('- ') or stripped.startswith('1. '):
            continue
        body_lines.append(stripped)
    full = ' '.join(body_lines)
    full = re.sub(r'\*\*[^*]+\*\*', '', full)
    full = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', full)
    full = re.sub(r'\*', '', full)
    return clean_text(full, max_len=max_len) or None

# Content file for FwcpbCED
content_file = CONTENT_DIR / "FwcpbCED.md"
if not content_file.exists():
    print(f"ERROR: content file not found: {content_file}")
    sys.exit(1)

with open(content_file, encoding='utf-8') as f:
    content = f.read()

# Extract metadata from frontmatter
frontmatter = {}
in_fm = False
for line in content.split('\n'):
    if line.strip() == '---':
        in_fm = not in_fm
        continue
    if in_fm:
        if ':' in line:
            k, v = line.split(':', 1)
            frontmatter[k.strip()] = v.strip()

content_id = "FwcpbCED"

# Title
title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
title = title_match.group(1) if title_match else "Agent Memory 架构解析"

# URL from frontmatter
url = frontmatter.get('url') or ""

# Platform
platform = "wechat"

# Author
author = "架构师（JiaGouX）"

# Original date - not determinable from article, set null
original_date = None

# Tags
tags = ["agent", "memory", "harness", "context-engineering", "agentic", "architecture"]

# Source type
source_type = "article"

# Language
language = "zh"

# Summary
summary_zh = extract_summary_zh(content)
if not summary_zh or len(summary_zh) < 80:
    summary_zh = ("Agent Memory 的核心问题不是存储，而是哪些过去可以继续影响未来。"
                  "本文系统梳理了 Memory 在 Agent Harness 中的定位：写入（给历史分配未来影响力）、"
                  "读取（把合适的历史转成当前任务约束）、管理（冲突、衰减、遗忘、版本、权限、审计）。"
                  "指出 Profile 消费视图、Policy 外部规则与 Memory 三者边界，"
                  "提出 Coding Agent 四层记忆落点框架，并强调 Memory 越往生产走，越像可被工具操作的工作区资产。"
                  "值得做的是让 Agent 在具体任务域里少重复犯错，而非追求通用智能记忆。")

# Images
images = extract_images(content)

# Category
category = canonical_category(
    "agent-frameworks/memory",
    tags=tags,
    source_type=source_type,
    title=title,
    summary=summary_zh
)

# Quality score - high quality original analysis
quality_score = 4

# One-liner
one_liner = derive_one_liner(title, summary_zh, None)
if not one_liner or "未提供" in one_liner or len(one_liner) < 5:
    one_liner = "Memory 是 Agent 从玩具变产品的最后一道关卡，这篇把写入/读取/管理的本质讲透了"

# Local path
local_path = "content/FwcpbCED.md"

# Build raw entry
raw_entry = {
    "id": content_id,
    "title": title,
    "url": url,
    "source": {
        "platform": platform,
        "author": author,
        "original_date": original_date
    },
    "category": category,
    "tags": tags,
    "source_type": source_type,
    "language": language,
    "summary_zh": summary_zh[:900],
    "summary_en": None,
    "one_liner": one_liner,
    "one_liner_author": "openclaw",
    "quality_score": quality_score,
    "status": "active",
    "local_path": local_path,
    "images": images[:5],
    "added_date": today_str(),
    "updated_date": None,
    "github_stars": None,
    "related": []
}

# Load existing entries
entries_list = load_entries_list(ENTRIES_FILE)
existing_urls = {normalized_url_key(e.get('url')) for e in entries_list if e.get('url')}
existing_ids = {e['id'] for e in entries_list}

print(f"Current entries: {len(entries_list)}")

# Check for duplicate by id
if content_id in existing_ids:
    print(f"DUP by ID: {content_id} already exists, skipping")
elif url and normalized_url_key(url) in existing_urls:
    print(f"DUP by URL: {url} already exists, skipping")
else:
    # Normalize entry
    normalized = normalize_entry(raw_entry)
    
    # Low signal check (same logic as pipeline_utils)
    low_signal = is_low_signal_entry(normalized) or (
        normalized["status"] == "active"
        and quality_score >= 3
        and is_placeholder_text(summary_zh)
        and not has_readable_text(normalized.get("one_liner", ""))
    )
    if low_signal:
        normalized["quality_score"] = min(normalized["quality_score"], 2)
        normalized["status"] = "score-pending"
    
    # Append and save
    entries_list.append(normalized)
    save_entries_list(entries_list, ENTRIES_FILE)
    print(f"Added: {content_id} - {title}")
    print(f"Quality: {normalized['quality_score']}, Category: {normalized['category']}")
    print(f"Total entries now: {len(entries_list)}")

print("Done.")