#!/usr/bin/env python3
"""
Daily intake pipeline for AI-related content
Follows the exact workflow from task-intake.md
"""

import os
import re
import json
import hashlib
from datetime import datetime, date
from pathlib import Path
import sys

# Add the openclaw scripts to path
sys.path.append('openclaw/scripts')
from pipeline_utils import (
    normalize_url, 
    generate_entry_id, 
    normalize_entry, 
    append_entries,
    save_entries_data,
    clean_text,
    canonical_category
)

def extract_metadata_from_file(file_path):
    """Extract metadata from markdown files"""
    content = Path(file_path).read_text(encoding='utf-8')
    
    metadata = {
        'title': '',
        'url': '',
        'author': '',
        'date': '',
        'source_platform': '',
        'summary_zh': '',
        'tags': [],
        'raw_content': ''
    }
    
    # Extract basic info from header
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            metadata['title'] = line[2:].strip()
        elif line.startswith('- **来源**：') or line.startswith('- **来源**：'):
            source_info = line.replace('- **来源**：', '').strip()
            if 'X/Twitter' in source_info:
                metadata['source_platform'] = 'x'
            elif 'Cubox' in source_info:
                metadata['source_platform'] = 'cubox'
        elif line.startswith('- **原文链接**：') or line.startswith('- **原文链接**：'):
            metadata['url'] = line.replace('- **原文链接**：', '').strip()
        elif line.startswith('- **作者**：') or line.startswith('- **作者**：'):
            metadata['author'] = line.replace('- **作者**：', '').strip()
        elif line.startswith('- **日期**：') or line.startswith('- **日期**：'):
            metadata['date'] = line.replace('- **日期**：', '').strip()
        elif line.startswith('tags:'):
            tags_line = line.replace('tags:', '').strip()
            if tags_line.startswith('[') and tags_line.endswith(']'):
                metadata['tags'] = eval(tags_line)
    
    # Extract summary (content after the metadata section)
    content_start = 0
    for i, line in enumerate(lines):
        if line.strip() == '---' and i > 0:
            content_start = i + 1
            break
    
    if content_start < len(lines):
        content_section = '\n'.join(lines[content_start:])
        # Clean up the content
        content_section = re.sub(r'!\[.*?\]\([^)]+\)', '', content_section)  # Remove images
        content_section = re.sub(r'\[.*?\]\([^)]+\)', '', content_section)   # Remove links
        metadata['summary_zh'] = clean_text(content_section[:500]) or clean_text(content_section)
    
    metadata['raw_content'] = content
    return metadata

def fetch_original_content(metadata, content_dir):
    """Fetch original content and save to content/<id>.md"""
    entry_id = generate_entry_id(title=metadata['title'], url=metadata['url'])
    content_file = content_dir / f"{entry_id}.md"
    
    original_content = f"""---
title: "{metadata['title']}"
url: "{metadata['url']}"
source_platform: "{metadata['source_platform']}"
author: "{metadata['author']}"
date: "{metadata['date']}"
tags: {metadata['tags']}
---

{metadata['raw_content']}
"""
    
    content_file.write_text(original_content, encoding='utf-8')
    return entry_id

def extract_images(content):
    """Extract image URLs from content"""
    image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    return images

def process_ai_files():
    """Main processing function"""
    base_dir = Path('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian')
    content_dir = Path('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/content')
    entries_file = Path('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/data/entries.json')
    
    # Find AI-related files from the last 24 hours
    ai_files = [
        base_dir / 'X 文章/2026-06-01-1234-xiaogaifun-Harness工程最透彻演讲.md',
        base_dir / 'X 文章/2026-06-01-1234-XudongHan-Codex网络优化技巧.md',
        base_dir / 'X 文章/2026-06-01-1234-BetterCallMedhi-Huawei-tau-scaling-law.md',
        base_dir / 'Cubox/一文讲透企业级  Harness Coding 架构落地实战！-2026-06-01.md',
        base_dir / 'Cubox/更好的处理major page faults-2026-06-01.md',
        base_dir / 'Cubox/深入解析Chromium的 AI Coding 开发体系-2026-06-01.md'
    ]
    
    new_entries = []
    
    for file_path in ai_files:
        if not file_path.exists():
            continue
            
        print(f"Processing: {file_path.name}")
        
        # Extract metadata
        metadata = extract_metadata_from_file(file_path)
        
        # Generate entry ID and save content
        entry_id = fetch_original_content(metadata, content_dir)
        
        # Extract images
        images = extract_images(metadata['raw_content'])
        
        # Create entry dict
        entry = {
            'id': entry_id,
            'title': metadata['title'],
            'url': normalize_url(metadata['url']),
            'source': {
                'platform': metadata['source_platform'],
                'author': metadata['author'] if metadata['author'] else None,
                'original_date': metadata['date'] if metadata['date'] else None
            },
            'summary_zh': metadata['summary_zh'],
            'summary_en': None,
            'one_liner': '',
            'one_liner_author': 'openclaw',
            'local_path': f"Obsidian/awesome-ai-field-notes/content/{entry_id}.md",
            'images': images,
            'added_date': date.today().isoformat(),
            'updated_date': date.today().isoformat(),
            'tags': metadata['tags'],
            'category': 'uncategorized',
            'quality_score': 3,
            'source_type': 'x_post' if metadata['source_platform'] == 'x' else 'article',
            'language': 'zh',
            'status': 'score-pending'
        }
        
        new_entries.append(entry)
        print(f"  - Created entry: {entry['title']}")
    
    # Load existing entries
    if entries_file.exists():
        existing_data = json.loads(entries_file.read_text(encoding='utf-8'))
    else:
        existing_data = {'entries': []}
    
    # Add new entries using pipeline_utils
    if new_entries:
        added, skipped = append_entries(existing_data, new_entries)
        save_entries_data(existing_data)
        
        print(f"\nProcessing complete:")
        print(f"  - Added: {len(added)} entries")
        print(f"  - Skipped: {len(skipped)} entries")
        
        for entry in added:
            print(f"    + {entry['title']}")
        
        if skipped:
            print(f"  - Skipped entries:")
            for entry, reason in skipped:
                print(f"    - {entry['title']} ({reason})")
    else:
        print("No new AI-related entries found")

if __name__ == "__main__":
    process_ai_files()
