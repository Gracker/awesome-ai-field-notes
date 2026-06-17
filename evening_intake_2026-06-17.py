#!/usr/bin/env python3
"""
Evening Intake Pipeline - June 17, 2026
Process recent AI-related files and add to entries.json
"""

import json
import os
import re
from datetime import datetime, date
from pathlib import Path
from urllib.parse import urlparse
import subprocess
import sys
import requests

# Add project to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from openclaw.scripts.pipeline_utils import (
    load_entries_data, save_entries_data, normalize_entry, append_entries,
    normalize_url, clean_text, has_cjk, normalize_date, normalize_tags,
    canonical_category, normalize_source_type, normalize_platform,
    generate_entry_id, has_readable_text, derive_one_liner
)

def web_fetch(url, extractMode='markdown', maxChars=5000):
    """Simple web fetch function using requests"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        if extractMode == 'text':
            # Basic text extraction - remove HTML tags
            import re
            text = re.sub(r'<[^>]+>', '', response.text)
            text = re.sub(r'\s+', ' ', text).strip()
            return text[:maxChars]
        else:
            # Return markdown - simple attempt at converting HTML to markdown
            import re
            # Remove script and style tags
            content = re.sub(r'<script[^>]*>.*?</script>', '', response.text, flags=re.DOTALL)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
            # Convert basic HTML to markdown
            content = re.sub(r'<h[1-6]>', '\n## ', content)  # Headers to markdown
            content = re.sub(r'</h[1-6]>', '\n', content)
            content = re.sub(r'<p>', '\n', content)  # Paragraphs
            content = re.sub(r'</p>', '\n', content)
            content = re.sub(r'<br ?/?>', '\n', content)  # Line breaks
            content = re.sub(r'<li>', '\n* ', content)  # List items
            content = re.sub(r'</li>', '', content)
            content = re.sub(r'<[^>]+>', '', content)  # Remove remaining tags
            content = re.sub(r'\n\n+', '\n\n', content)  # Clean up newlines
            content = content.strip()
            return content[:maxChars] if maxChars else content
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def extract_metadata(file_path):
    """Extract metadata from file content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter if exists
    frontmatter = {}
    parts = []
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1].strip()
            # Simple YAML parsing for our known fields
            for line in yaml_content.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    frontmatter[key] = value
    
    # Extract main content
    main_content = parts[2] if len(parts) >= 3 else content
    
    # Extract title from content
    title_match = re.search(r'^#\s+(.+)$', main_content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else Path(file_path).stem
    
    # Extract URL from content
    url = frontmatter.get('url') or frontmatter.get('原文链接')
    
    # Extract platform based on directory
    platform = 'manual'
    if 'X 文章' in str(file_path):
        platform = 'x'
    elif 'Cubox' in str(file_path):
        platform = 'cubox'
    
    # Extract author
    author = frontmatter.get('作者') or frontmatter.get('author')
    
    # Extract date
    raw_date = frontmatter.get('日期') or frontmatter.get('original_date') or frontmatter.get('发表时间')
    
    # Extract tags
    tags = frontmatter.get('tags', [])
    if isinstance(tags, str):
        tags = [tag.strip() for tag in tags.split(',') if tag.strip()]
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', main_content)
    
    # Determine source type
    if platform == 'x':
        source_type = 'x_post'
    elif platform == 'cubox':
        source_type = 'article'  # Default for Cubox
    else:
        source_type = normalize_source_type(frontmatter.get('source_type'))
    
    return {
        'title': title,
        'url': normalize_url(url),
        'source': {
            'platform': normalize_platform(platform, url=url),
            'author': clean_text(author, max_len=100) if author else None,
            'original_date': normalize_date(raw_date),
        },
        'source_type': source_type,
        'tags': normalize_tags(tags),
        'local_path': str(file_path.relative_to(project_root.parent.parent)),
        'images': images,
        'raw_content': main_content,
        'frontmatter': frontmatter,
        'file_path': str(file_path)
    }

def fetch_original_content(metadata, content_dir_path):
    """Fetch original content using appropriate tools"""
    url = metadata['url']
    if not url:
        return None
    
    entry_id = metadata.get('id', generate_entry_id(title=metadata['title'], url=url))
    content_file = content_dir_path / f"{entry_id}.md"
    
    try:
        # For X/Twitter, use opencli first
        if metadata['source']['platform'] == 'x':
            if 'status/' in url:
                cmd = ['opencli', 'twitter', 'thread', url]
            else:
                cmd = ['opencli', 'twitter', 'article', url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return result.stdout
        
        # For WeChat articles
        elif metadata['source']['platform'] == 'wechat':
            cmd = ['opencli', 'weixin', 'article', url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return result.stdout
        
        # For other articles, use web_fetch
        else:
            return web_fetch(url, extractMode='markdown', maxChars=5000)
            
    except Exception as e:
        print(f"Failed to fetch content for {url}: {e}")
    
    # If all else fails, write the current content with a note
    failure_note = f"> 备注：原文抓取失败，以下为摘要。\\n\\n{metadata['raw_content']}"
    return failure_note

def generate_summaries(content, language='zh'):
    """Generate summaries from content"""
    if not content or len(content) < 50:
        return "内容过短，待补充" if language == 'zh' else "Content too short, needs supplement", None
    
    # Clean and extract meaningful content
    lines = []
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('> 备注：'):
            lines.append(line)
    
    text = ' '.join(lines)
    text = clean_text(text, max_len=900)
    
    if not text:
        return "内容过短，待补充" if language == 'zh' else "Content too short, needs supplement", None
    
    # For Chinese content, provide Chinese summary
    if language == 'zh' or has_cjk(text):
        summary_zh = text
        summary_en = None
    else:
        summary_zh = text  # For English content, provide translation summary
        summary_en = text
    
    return summary_zh, summary_en

def score_content(entry):
    """Score content based on quality criteria"""
    content = entry.get('raw_content', '')
    title = entry.get('title', '')
    summary_zh = entry.get('summary_zh', '')
    
    # Basic scoring criteria
    score = 3  # Default
    
    # Check for high-quality indicators
    if len(content) > 2000:  # Long content
        score += 1
    if '关键发现' in content or 'Key findings' in content:  # Has structured findings
        score += 1
    if any(keyword in title.lower() for keyword in ['milestone', 'breakthrough', 'revolutionary', '重大发现']):
        score += 1
    if entry.get('source', {}).get('platform') == 'manual':
        score += 1  # Manual entries are usually curated
    
    # Cap at 5
    return min(5, score)

def process_file(file_path, content_dir_path, existing_entries):
    """Process a single file and return entry data"""
    metadata = extract_metadata(file_path)
    
    # Fetch original content
    original_content = fetch_original_content(metadata, content_dir_path)
    
    # Generate summaries
    summary_zh, summary_en = generate_summaries(original_content or metadata['raw_content'])
    
    # Generate entry
    entry_data = {
        'title': metadata['title'],
        'url': metadata['url'],
        'source': metadata['source'],
        'source_type': metadata['source_type'],
        'tags': metadata['tags'],
        'language': 'both' if metadata['source']['platform'] == 'x' and summary_en else 'zh',
        'summary_zh': summary_zh,
        'summary_en': summary_en,
        'local_path': metadata['local_path'],
        'images': metadata['images'],
        'raw_content': original_content or metadata['raw_content'],
    }
    
    # Normalize entry
    normalized_entry = normalize_entry(entry_data)
    
    # Score content
    normalized_entry['quality_score'] = score_content(normalized_entry)
    
    # Determine status
    if is_low_signal_entry(normalized_entry):
        normalized_entry['status'] = 'score-pending'
    else:
        normalized_entry['status'] = 'active'
    
    # Generate one-liner
    normalized_entry['one_liner'] = derive_one_liner(
        normalized_entry['title'], 
        normalized_entry['summary_zh'] or normalized_entry['summary_en'] or '',
        normalized_entry.get('one_liner')
    )
    
    return normalized_entry

def is_low_signal_entry(entry):
    """Check if entry is low quality/placeholder"""
    title = str(entry.get("title") or "")
    summary = str(entry.get("summary_zh") or "")
    tags = {str(tag).lower() for tag in entry.get("tags", [])}
    
    return (
        title.startswith("高价值AI内容 -") or
        ("high-value" in tags and len(clean_text(summary)) < 50) or
        clean_text(summary) in ["[]", "****", "---", "内容过短，待补充"]
    )

def main():
    # Initialize
    project_root = Path(__file__).parent
    content_dir_path = project_root / "content"
    entries_file_path = project_root / "data" / "entries.json"
    
    # Load existing entries
    try:
        existing_data = load_entries_data()
    except Exception as e:
        print(f"Error loading existing entries: {e}")
        existing_data = {"entries": [], "last_updated": date.today().isoformat(), "total_entries": 0}
    
    # Find recent AI-related files
    obsidian_root = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian")
    recent_files = []
    
    # Search for files modified in last 24 hours in X articles and Cubox
    for category in ['X 文章', 'Cubox']:
        category_path = obsidian_root / category
        print(f"Checking category: {category_path}")
        if category_path.exists():
            print(f"Category path exists: {category_path}")
            md_files = list(category_path.glob("*.md"))
            print(f"Found {len(md_files)} .md files in {category}")
            for file_path in md_files:
                file_age = (datetime.now() - datetime.fromtimestamp(file_path.stat().st_mtime)).days
                print(f"  {file_path.name}: {file_age} days old")
                if file_age < 1:
                    recent_files.append(file_path)
        else:
            print(f"Category path does not exist: {category_path}")
    
    print(f"Found {len(recent_files)} recent AI-related files to process")
    
    # Process each file
    new_entries = []
    for file_path in recent_files:
        try:
            print(f"Processing: {file_path.name}")
            entry = process_file(file_path, content_dir_path, existing_data)
            new_entries.append(entry)
            print(f"  - Title: {entry['title']}")
            print(f"  - Category: {entry['category']}")
            print(f"  - Score: {entry['quality_score']}")
            print(f"  - Status: {entry['status']}")
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")
    
    if not new_entries:
        print("No new entries to add")
        return
    
    # Add entries to existing data
    added_entries, skipped_entries = append_entries(existing_data, new_entries)
    
    print(f"\nResults:")
    print(f"- Added: {len(added_entries)} entries")
    print(f"- Skipped: {len(skipped_entries)} entries")
    
    # Save updated entries
    save_entries_data(existing_data)
    print(f"Total entries: {existing_data['total_entries']}")
    
    # Save content files
    for entry in added_entries:
        if entry.get('raw_content'):
            content_file = content_dir_path / f"{entry['id']}.md"
            with open(content_file, 'w', encoding='utf-8') as f:
                f.write(entry['raw_content'])
    
    print("Content files saved")

if __name__ == "__main__":
    main()