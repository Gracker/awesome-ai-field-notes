#!/usr/bin/env python3
"""Process recently modified AI-related .md entries and add to entries.json"""

import re
import json
import sys
import os
from pathlib import Path
from datetime import date, datetime
from urllib.parse import urlparse
import hashlib

# Add the openclaw/scripts directory to Python path
sys.path.append('openclaw/scripts')

from pipeline_utils import (
    load_entries_data, save_entries_data, normalize_entry, append_entries,
    normalize_url, clean_text, generate_entry_id
)

def extract_metadata_and_content(content):
    """Extract metadata and main content from markdown file"""
    metadata = {}
    
    # Extract title from first line
    lines = content.split('\n')
    if lines:
        first_line = lines[0].strip()
        if first_line.startswith('# '):
            metadata['title'] = first_line[2:].strip()
        else:
            metadata['title'] = first_line
    
    # Extract metadata from the YAML-like header section
    for line in lines:
        line = line.strip()
        
        # Extract URL
        if '原文链接' in line or '链接' in line:
            url_match = re.search(r'https?://[^\s\)]+', line)
            if url_match:
                metadata['url'] = normalize_url(url_match.group(0))
        
        # Extract author
        if '作者' in line:
            author_match = re.search(r'作者[:：]\s*(.+)', line)
            if author_match:
                metadata['author'] = author_match.group(1).strip()
            else:
                # Try to extract from parentheses
                paren_match = re.search(r'\(([^)]+)\)', line)
                if paren_match:
                    metadata['author'] = paren_match.group(1).strip()
        
        # Extract date
        if '日期' in line or '发表时间' in line:
            date_match = re.search(r'日期[:：]\s*(.+)', line)
            if date_match:
                metadata['date'] = date_match.group(1).strip()
        
        # Extract category
        if '分类' in line:
            category_match = re.search(r'分类[:：]\s*(.+)', line)
            if category_match:
                metadata['category'] = category_match.group(1).strip()
        
        # Extract tags
        if '标签' in line:
            tags_match = re.search(r'标签[:：]\s*(.+)', line)
            if tags_match:
                tags_str = tags_match.group(1).strip()
                # Handle different tag formats
                if ',' in tags_str:
                    metadata['tags'] = [tag.strip() for tag in tags_str.split(',')]
                else:
                    metadata['tags'] = [tag.strip() for tag in tags_str.split()]
        
        # Extract quality score
        if '质量评分' in line or '评分' in line:
            score_match = re.search(r'评分[:：]\s*(\d+)', line)
            if score_match:
                metadata['quality_score'] = int(score_match.group(1))
        
        # Extract source information
        if '来源' in line:
            source_match = re.search(r'来源[:：]\s*(.+)', line)
            if source_match:
                source_text = source_match.group(1).strip()
                metadata['source_platform'] = 'manual'
                
                # Determine platform from source
                if '掘金' in source_text or 'juejin.cn' in source_text:
                    metadata['source_platform'] = 'blog'
                elif 'baoyu.io' in source_text:
                    metadata['source_platform'] = 'blog'
                elif 'x.com' in source_text or 'twitter.com' in source_text:
                    metadata['source_platform'] = 'x'
                elif 'github.com' in source_text:
                    metadata['source_platform'] = 'github'
                elif 'medium.com' in source_text:
                    metadata['source_platform'] = 'blog'
    
    return metadata

def extract_main_content(content):
    """Extract main content from markdown file"""
    # Split by --- and find the main content section
    sections = content.split('---')
    if len(sections) > 2:
        main_content = sections[2].strip()
    else:
        # If no --- separator, find content after first few lines
        lines = content.split('\n')
        main_content = '\n'.join(lines[3:]).strip()
    
    # Remove the warning note at the end if present
    warning_note = "**⚠️ 重要说明**"
    if warning_note in main_content:
        main_content = main_content.split(warning_note)[0].strip()
    
    return main_content

def create_summary(content, max_chars=300):
    """Create a summary from the content"""
    # Clean the content first
    cleaned = clean_text(content, max_len=1000)
    
    # Try to find the main content sections
    lines = cleaned.split('\n')
    summary_lines = []
    
    # Look for substantial content
    for line in lines:
        line = line.strip()
        if len(line) > 20 and not line.startswith('#') and not line.startswith('-'):
            summary_lines.append(line)
            if len(' '.join(summary_lines)) >= max_chars:
                break
    
    summary = ' '.join(summary_lines)
    if len(summary) > max_chars:
        # Truncate at the last sentence
        for separator in ('。', '！', '？', '. ', '; ', '；'):
            pos = summary.rfind(separator, 0, max_chars)
            if pos >= max_chars // 2:
                summary = summary[:pos + len(separator)]
                break
        else:
            summary = summary[:max_chars] + '...'
    
    return summary if summary else "内容过短，待补充"

def extract_images(content):
    """Extract image URLs from markdown content"""
    image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    return images

def process_file(file_path):
    """Process a single markdown file and return entry data"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata and content
    metadata = extract_metadata_and_content(content)
    main_content = extract_main_content(content)
    
    # Create ID if not present
    if 'id' not in metadata:
        metadata['id'] = generate_entry_id(
            title=metadata.get('title', ''),
            url=metadata.get('url', '')
        )
    
    # Set default values
    if 'title' not in metadata:
        metadata['title'] = Path(file_path).stem
    if 'category' not in metadata:
        metadata['category'] = 'uncategorized'
    if 'quality_score' not in metadata:
        metadata['quality_score'] = 3
    
    # Create entry
    entry = {
        'id': metadata.get('id'),
        'title': metadata.get('title', '未命名 AI 资源'),
        'url': metadata.get('url'),
        'source': {
            'platform': metadata.get('source_platform', 'manual'),
            'author': metadata.get('author'),
            'original_date': metadata.get('date')
        },
        'category': metadata.get('category'),
        'tags': metadata.get('tags', []),
        'source_type': 'article',
        'language': 'zh',
        'summary_zh': create_summary(main_content),
        'summary_en': None,
        'one_liner': '',
        'one_liner_author': 'openclaw',
        'quality_score': metadata.get('quality_score', 3),
        'status': 'active',
        'local_path': f"content/{metadata.get('id', 'unknown')}.md",
        'images': extract_images(content),
        'added_date': date.today().isoformat(),
        'updated_date': date.today().isoformat(),
        'github_stars': None,
        'related': []
    }
    
    return entry, main_content

def main():
    """Main processing function"""
    # Get recently modified files
    content_dir = Path('content')
    cutoff_date = datetime(2026, 6, 16, 8, 0, 0)  # Files modified since yesterday 08:00
    
    # Find recently modified files
    recent_files = []
    for md_file in content_dir.glob('*.md'):
        if md_file.stat().st_mtime >= cutoff_date.timestamp():
            recent_files.append(md_file)
    
    print(f"Found {len(recent_files)} recently modified files")
    
    # Load existing entries
    try:
        entries_data = load_entries_data()
        print(f"Loaded existing entries: {len(entries_data['entries'])}")
    except Exception as e:
        print(f"Error loading entries.json: {e}")
        entries_data = {"entries": [], "last_updated": date.today().isoformat(), "total_entries": 0}
    
    # Process each file
    new_entries = []
    for file_path in recent_files:
        try:
            print(f"Processing {file_path.name}...")
            entry, content = process_file(file_path)
            
            # Check if entry already exists
            existing_ids = {ex['id'] for ex in entries_data['entries']}
            if entry['id'] in existing_ids:
                print(f"  Entry {entry['id']} already exists, skipping...")
                continue
            
            # Add content to entry
            entry['content'] = content
            
            new_entries.append(entry)
            print(f"  New entry: {entry['title']} (ID: {entry['id']}, Category: {entry['category']})")
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")
            continue
    
    print(f"\nProcessed {len(new_entries)} new entries")
    
    # Add entries using pipeline_utils
    if new_entries:
        added, skipped = append_entries(entries_data, new_entries)
        print(f"Added {len(added)} entries, skipped {len(skipped)}")
        
        # Save the updated entries
        save_entries_data(entries_data)
        print(f"Total entries: {len(entries_data['entries'])}")
        
        # Save content files (they already exist, but just to confirm)
        for entry in added:
            content_file = Path(entry['local_path'])
            if not content_file.exists():
                with open(content_file, 'w', encoding='utf-8') as f:
                    f.write(entry.get('content', ''))
        
        print("Processing completed successfully")
    else:
        print("No new entries to add")

if __name__ == '__main__':
    main()
