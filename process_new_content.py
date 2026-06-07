#!/usr/bin/env python3
"""Process new content files and add them to entries.json"""

import re
import json
from pathlib import Path
import sys
import os

# Add the openclaw/scripts path to Python path
sys.path.insert(0, 'openclaw/scripts')

from pipeline_utils import (
    append_entries, save_entries_data, normalize_url, clean_text,
    generate_entry_id, canonical_category, normalize_tags, normalize_source_type, 
    normalize_platform, derive_one_liner
)

def parse_content_file(file_path: Path) -> dict:
    """Parse a content file and extract metadata"""
    content = file_path.read_text(encoding='utf-8')
    
    # Extract title (first line after #)
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "未命名标题"
    
    # Extract metadata
    metadata = {}
    metadata_patterns = {
        'Author': r'\*\*Author:\*\* ([^\n]+)',
        'Source': r'\*\*Source:\*\* \[([^\]]+)\]\(([^)]+)\)',
        'Date': r'\*\*Date:\*\* ([^\n]+)',
        'Quality Score': r'\*\*Quality Score:\*\* (\d+)',
        'Tags': r'\*\*Tags:\*\* ([^\n]+)',
        'Category': r'\*\*Category:\*\* ([^\n]+)',
        'Fetch Date': r'\*\*Fetch Date:\*\* ([^\n]+)'
    }
    
    for key, pattern in metadata_patterns.items():
        match = re.search(pattern, content)
        if match:
            if key == 'Source':
                metadata[key] = {
                    'text': match.group(1),
                    'url': match.group(2)
                }
            elif key == 'Tags':
                metadata[key] = [tag.strip() for tag in match.group(1).split(',')]
            else:
                metadata[key] = match.group(1)
    
    # Extract English original content
    english_match = re.search(r'## English Original\s*\n(.*?)\s*\n\s*## 中文翻译', content, re.DOTALL)
    summary_en = clean_text(english_match.group(1).strip(), max_len=300) if english_match else ""
    
    # Extract Chinese translation  
    chinese_match = re.search(r'## 中文翻译\s*\n(.*?)$', content, re.DOTALL)
    summary_zh = clean_text(chinese_match.group(1).strip(), max_len=300) if chinese_match else ""
    
    # Generate entry ID
    entry_id = generate_entry_id(title=title, url=metadata.get('Source', {}).get('url', ''))
    
    # Create entry dict
    entry = {
        'id': entry_id,
        'title': title,
        'url': metadata.get('Source', {}).get('url'),
        'summary_zh': summary_zh,
        'summary_en': summary_en if summary_en else None,
        'source': {
            'platform': normalize_platform(metadata.get('Author', ''), url=metadata.get('Source', {}).get('url')),
            'author': metadata.get('Author', '').replace('@', ''),
            'original_date': metadata.get('Date')
        },
        'source_type': normalize_source_type('x_post'),
        'tags': normalize_tags(metadata.get('Tags', [])),
        'category': metadata.get('Category', 'uncategorized'),
        'local_path': str(file_path),
        'quality_score': int(metadata.get('Quality Score', 3)),
        'one_liner': derive_one_liner(title, summary_zh or summary_en or ""),
        'status': 'active',
        'one_liner_author': 'openclaw'
    }
    
    return entry

def main():
    # Load existing entries
    entries_path = Path('entries.json')
    if entries_path.exists():
        with open(entries_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = {'entries': [], 'last_updated': '', 'total_entries': 0}
    
    # Find recent content files
    content_dir = Path('content')
    recent_files = list(content_dir.glob('*.md'))
    
    print(f"Found {len(recent_files)} content files to process")
    
    new_entries = []
    for file_path in recent_files:
        try:
            entry = parse_content_file(file_path)
            new_entries.append(entry)
            print(f"Processed: {entry['title']} ({entry['id']})")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    if new_entries:
        # Add entries using pipeline_utils
        added, skipped = append_entries(existing_data, new_entries)
        
        print(f"\nResults:")
        print(f"Added: {len(added)} entries")
        print(f"Skipped: {len(skipped)} entries")
        
        # Save the updated data
        save_entries_data(existing_data)
        print(f"Total entries: {existing_data['total_entries']}")
    else:
        print("No new entries to process")

if __name__ == '__main__':
    main()
