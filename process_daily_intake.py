#!/usr/bin/env python3
"""
Daily Intake Task - Processing newly discovered AI content
Phase 1-5 complete workflow from task-intake.md
"""

import json
import os
import re
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Add openclaw scripts to path
sys.path.insert(0, str(Path(__file__).parent / "openclaw" / "scripts"))

try:
    from pipeline_utils import (
        load_entries_data, save_entries_data, append_entries, normalize_entry,
        normalize_url, clean_text, today_str
    )
except ImportError as e:
    print(f"Error importing pipeline_utils: {e}")
    sys.exit(1)

# Configuration
PROJECT_ROOT = Path(__file__).parent
CONTENT_DIR = PROJECT_ROOT / "content"
DATA_DIR = PROJECT_ROOT / "data"
ENTRIES_FILE = DATA_DIR / "entries.json"

# Keywords for AI-related content
AI_KEYWORDS = {
    "ai", "artificial intelligence", "llm", "gpt", "claude", "gemini", 
    "transformer", "neural", "machine learning", "深度学习", "人工智能",
    "大模型", "语言模型", "智能体", "automation", "智能"
}

def is_ai_related(text: str) -> bool:
    """Check if text is AI-related"""
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in AI_KEYWORDS)

def extract_content_from_x_file(file_path: Path) -> Dict:
    """Extract content from X (Twitter) post files"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata from frontmatter
    import re
    frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not frontmatter_match:
        return None
    
    frontmatter, body = frontmatter_match.groups()
    
    # Parse frontmatter
    metadata = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    # Extract actual content from body
    original_section = None
    translation_section = None
    
    lines = body.split('\n')
    in_original = False
    in_translation = False
    
    for line in lines:
        if '原文 / English' in line:
            in_original = True
            in_translation = False
            original_section = []
        elif '译文 / 中文' in line:
            in_original = False
            in_translation = True
            translation_section = []
        elif line.startswith('#') or line.startswith('---'):
            in_original = False
            in_translation = False
        elif in_original:
            original_section.append(line)
        elif in_translation:
            translation_section.append(line)
    
    original_text = '\n'.join(original_section).strip() if original_section else ""
    translation_text = '\n'.join(translation_section).strip() if translation_section else ""
    
    return {
        'title': metadata.get('title', ''),
        'url': metadata.get('url', ''),
        'language': metadata.get('language', 'zh'),
        'quality_score': int(metadata.get('quality_score', 3)),
        'original_text': original_text,
        'translation_text': translation_text,
        'source_platform': metadata.get('platform', 'x.com'),
        'file_path': str(file_path)
    }

def get_twitter_content(url: str) -> str:
    """Fetch Twitter/X content using opencli"""
    try:
        # Check if we can use opencli
        import subprocess
        result = subprocess.run(['opencli', 'twitter', 'article', url], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"> 备注：原文抓取失败，以下为摘要。"
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return f"> 备注：原文抓取失败，以下为摘要。"

def process_x_posts() -> List[Dict]:
    """Process X posts in content directory"""
    entries = []
    
    # Find X post files modified recently
    x_files = []
    for md_file in CONTENT_DIR.glob("*.md"):
        if 'x.com' in str(md_file) or 'twitter' in str(md_file):
            x_files.append(md_file)
    
    for file_path in x_files[:10]:  # Limit to 10 files
        print(f"Processing {file_path}")
        content_data = extract_content_from_x_file(file_path)
        
        if not content_data:
            continue
            
        # Fetch original content if needed
        if "[根据内容长度和复杂性" in content_data.get('translation_text', ''):
            print(f"Fetching original content for {content_data['url']}")
            original_content = get_twitter_content(content_data['url'])
            content_data['original_text'] = original_content
        
        # Generate summaries
        original_text = content_data.get('original_text', '')
        translation_text = content_data.get('translation_text', '')
        
        summary_zh = clean_text(translation_text, max_len=300) if translation_text else clean_text(original_text, max_len=300)
        summary_en = clean_text(original_text, max_len=300) if original_text else None
        
        # Create entry
        entry = {
            'title': content_data['title'],
            'url': content_data['url'],
            'source': {
                'platform': content_data['source_platform'],
                'author': content_data['url'].split('/')[-1].split('_')[0].replace('@', ''),
                'original_date': date.today().isoformat()
            },
            'source_type': 'x_post',
            'language': content_data['language'],
            'summary_zh': summary_zh,
            'summary_en': summary_en,
            'one_liner': f"{content_data['title'][:100]}..." if len(content_data['title']) > 100 else content_data['title'],
            'local_path': str(file_path.relative_to(PROJECT_ROOT)),
            'quality_score': content_data['quality_score']
        }
        
        entries.append(entry)
    
    return entries

def process_ai_influence_daily() -> List[Dict]:
    """Process AI影响力日报 content"""
    entries = []
    daily_file = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/Twitter/AI影响力日报/2026-06-13.md")
    
    if not daily_file.exists():
        return entries
        
    with open(daily_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the daily content
    sections = content.split('---')
    in_section = False
    current_section = {}
    
    for section in sections[1:]:  # Skip first section (header)
        lines = section.strip().split('\n')
        if not lines or not lines[0]:
            continue
            
        # Extract title and link
        title_line = lines[0]
        if title_line.startswith('###'):
            title = title_line.replace('###', '').strip()
            # Extract link from the section
            link_match = re.search(r'链接：(.+)', section)
            url = link_match.group(1) if link_match else ''
            
            # Extract description
            desc_lines = [line for line in lines if not line.startswith('#') and line.strip()]
            description = '\n'.join(desc_lines).strip()
            
            if is_ai_related(title) or is_ai_related(description):
                entry = {
                    'title': title,
                    'url': url,
                    'source': {
                        'platform': 'twitter',
                        'author': title.split('@')[-1].split()[0] if '@' in title else 'unknown',
                        'original_date': date.today().isoformat()
                    },
                    'source_type': 'article',
                    'language': 'zh',
                    'summary_zh': clean_text(description, max_len=300),
                    'summary_en': None,
                    'one_liner': f"{title[:100]}..." if len(title) > 100 else title,
                    'local_path': f"content/daily_{date.today().isoformat()}.md",
                    'quality_score': 4  # Daily content gets higher quality score
                }
                entries.append(entry)
    
    return entries

def main():
    """Main processing workflow"""
    print("Starting daily intake process...")
    
    # Load existing entries
    try:
        entries_data = load_entries_data()
        print(f"Loaded existing entries: {entries_data.get('total_entries', 0)} entries")
    except Exception as e:
        print(f"Error loading entries: {e}")
        entries_data = {"entries": [], "last_updated": today_str(), "total_entries": 0}
    
    # Process new content
    new_entries = []
    
    # Process X posts
    print("Processing X posts...")
    x_entries = process_x_posts()
    new_entries.extend(x_entries)
    print(f"Found {len(x_entries)} X posts to process")
    
    # Process AI影响力日报
    print("Processing AI影响力日报...")
    daily_entries = process_ai_influence_daily()
    new_entries.extend(daily_entries)
    print(f"Found {len(daily_entries)} daily entries to process")
    
    if not new_entries:
        print("No new entries found to process")
        return
    
    # Normalize and append entries
    print("Normalizing entries...")
    added_entries, skipped_entries = append_entries(entries_data, new_entries)
    
    print(f"Added {len(added_entries)} entries, skipped {len(skipped_entries)} entries")
    
    # Save updated entries
    save_entries_data(entries_data)
    print(f"Saved entries with total: {entries_data['total_entries']}")
    
    # Generate summary
    summary = f"""
Daily Intake Summary - {date.today().isoformat()}
===============================================
Total entries processed: {len(new_entries)}
Entries added: {len(added_entries)}
Entries skipped: {len(skipped_entries)}
Total entries in database: {entries_data['total_entries']}
"""
    
    print(summary)
    
    # Save summary to log
    log_file = PROJECT_ROOT / "logs" / f"intake_{date.today().isoformat()}.md"
    log_file.parent.mkdir(exist_ok=True)
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"# Daily Intake Log - {date.today().isoformat()}\n\n")
        f.write(summary)
        f.write("\n## Processed Entries\n\n")
        for entry in added_entries:
            f.write(f"- {entry.get('title', 'No title')}\n")
            f.write(f"  URL: {entry.get('url', 'No URL')}\n")
            f.write(f"  Category: {entry.get('category', 'uncategorized')}\n")
            f.write(f"  Quality: {entry.get('quality_score', 0)}\n\n")

if __name__ == "__main__":
    main()