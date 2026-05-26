#!/usr/bin/env python3
"""Daily intake script for awesome-ai-field-notes"""

import json
import re
import os
from pathlib import Path
from datetime import date
from urllib.parse import urlparse

# Add the scripts directory to path to import pipeline_utils
import sys
sys.path.append('openclaw/scripts')

from pipeline_utils import (
    append_entries, save_entries_data, normalize_url, 
    content_dir, entries_path, has_readable_text,
    derive_one_liner, canonical_category
)

def extract_metadata_and_content(file_path):
    """Extract metadata and content from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first heading or filename
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else Path(file_path).stem
    
    # Extract URL if present
    url_match = re.search(r'https?://[^\s\)]+', content)
    url = normalize_url(url_match.group(0)) if url_match else None
    
    # Extract source info
    source = {}
    platform_match = re.search(r'来源[：:]\s*([^\n]+)', content)
    if platform_match:
        source_text = platform_match.group(1).strip().lower()
        if 'x' in source_text or 'twitter' in source_text:
            source['platform'] = 'x'
        elif 'cubox' in source_text:
            source['platform'] = 'manual'
        elif 'wechat' in source_text or '微信' in source_text:
            source['platform'] = 'wechat'
        else:
            source['platform'] = 'manual'
    
    author_match = re.search(r'作者[：:]\s*([^\n]+)', content)
    if author_match:
        source['author'] = author_match.group(1).strip()
    
    date_match = re.search(r'日期[：:]\s*([^\n]+)', content)
    if date_match:
        source['original_date'] = date_match.group(1).strip()
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    images = [normalize_url(img) for img in images if normalize_url(img)]
    images = list(dict.fromkeys(images))  # Remove duplicates
    images = images[:5]  # Limit to 5 images
    
    # Extract text content for summaries
    # Remove markdown formatting and get plain text
    plain_text = re.sub(r'#+\s+', '', content)  # Remove headings
    plain_text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', plain_text)  # Remove images
    plain_text = re.sub(r'\[[^\]]*\]\([^)]*\)', '', plain_text)  # Remove links
    plain_text = re.sub(r'`[^`]*`', '', plain_text)  # Remove code blocks
    plain_text = re.sub(r'\*\*[^*]*\*\*', '', plain_text)  # Remove bold
    plain_text = re.sub(r'\*[^*]*\*', '', plain_text)  # Remove italics
    plain_text = re.sub(r'\s+', ' ', plain_text).strip()  # Normalize whitespace
    
    # Generate Chinese summary (100-300 characters)
    summary_zh = plain_text[:300].strip()
    if len(summary_zh) > 100 and not summary_zh.endswith(('.', '。', '!', '！', '?', '？')):
        # Try to find a good cutoff point
        for cutoff in range(min(len(summary_zh), 300), max(100, len(summary_zh)-50), -1):
            if summary_zh[cutoff-1] in ('。', '！', '？', '.', '!', '?'):
                summary_zh = summary_zh[:cutoff]
                break
    
    # Generate English summary if needed
    summary_en = None
    if not has_cjk(title):  # If title is not Chinese
        summary_en = summary_zh
        summary_zh = None
    
    # Generate one-liner
    one_liner = derive_one_liner(title, summary_zh or summary_en or "")
    
    # Determine category
    category = canonical_category(
        None,  # Let pipeline determine
        tags=[],
        source_type="article",
        title=title,
        summary=summary_zh or summary_en or ""
    )
    
    return {
        'title': title,
        'url': url,
        'source': source,
        'summary_zh': summary_zh,
        'summary_en': summary_en,
        'one_liner': one_liner,
        'one_liner_author': 'openclaw',
        'category': category,
        'tags': [],
        'source_type': 'article',
        'language': 'zh' if has_cjk(title) else 'en',
        'quality_score': 3,  # Default score (integer)
        'status': 'score-pending',
        'local_path': str(file_path).replace('Obsidian/', ''),  # Relative path
        'images': images,
        'added_date': date.today().isoformat(),
        'updated_date': date.today().isoformat(),
        'github_stars': None,
        'related': []
    }

def has_cjk(text):
    """Check if text contains CJK characters"""
    return re.search(r'[\u4e00-\u9fff]', text or "") is not None

def process_new_files():
    """Process new AI-related files and add to entries"""
    # Load existing entries
    entries_data = {}
    try:
        with open(entries_path(), 'r', encoding='utf-8') as f:
            entries_data = json.load(f)
    except FileNotFoundError:
        entries_data = {'entries': []}
    
    # Find new files from today
    today_str = date.today().isoformat()
    new_files = []
    
    # Scan for files modified today
    base_path = Path('.')
    for md_file in base_path.rglob('*.md'):
        if 'task-intake.md' in str(md_file) or 'intake' in md_file.parts:
            continue
            
        # Check if file was modified today
        file_mtime = md_file.stat().st_mtime
        from datetime import datetime
        file_date = datetime.fromtimestamp(file_mtime).date().isoformat()
        
        if file_date == today_str:
            # Check if it's AI-related
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if re.search(r'ai|artificial|intelligence|machine|learning|neural|model|agent|llm|gpt|claude|gemini|openai', content, re.IGNORECASE):
                    new_files.append(md_file)
    
    print(f"Found {len(new_files)} AI-related files from today")
    
    if not new_files:
        print("No new AI files found to process")
        return
    
    # Process each file
    new_entries = []
    for file_path in new_files[:20]:  # Limit to 20 entries per run
        try:
            print(f"Processing: {file_path}")
            entry = extract_metadata_and_content(file_path)
            new_entries.append(entry)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    if new_entries:
        # Use pipeline_utils to append entries
        added, skipped = append_entries(entries_data, new_entries)
        
        print(f"Added {len(added)} new entries")
        print(f"Skipped {len(skipped)} entries")
        
        # Save using pipeline_utils
        save_entries_data(entries_data)
        
        return len(added)
    
    return 0

if __name__ == "__main__":
    added_count = process_new_files()
    print(f"Daily intake completed. Added {added_count} new entries.")