#!/usr/bin/env python3
"""Add new unprocessed entries from git status"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

# Add scripts directory to path
sys.path.append(str(Path(__file__).parent / "openclaw" / "scripts"))
from pipeline_utils import load_entries_data, save_entries_data, append_entries, normalize_entry

def extract_content_file(file_path):
    """Extract content from markdown file and create entry dict"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata from frontmatter
        frontmatter = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter_lines = parts[1].strip().split('\n')
                for line in frontmatter_lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        frontmatter[key.strip()] = value.strip()
        
        # Extract title
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = frontmatter.get('title') or (title_match.group(1) if title_match else 'Untitled')
        
        # Extract summary from content (Chinese version)
        lines = content.split('\n')
        summary_lines = []
        in_english = False
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('---') or line.startswith('#'):
                continue
            if line.startswith('## 中文版') or line.startswith('## 概述'):
                break
            if line.startswith('## English Version'):
                in_english = True
                continue
            if in_english and line.startswith('##'):
                break
            if line and not line.startswith('- ') and not line.startswith('**'):
                summary_lines.append(line)
                if len(summary_lines) >= 15:
                    break
        
        summary_zh = '\n'.join(summary_lines)
        
        # Parse quality_score
        quality_str = frontmatter.get('quality_score', '3')
        try:
            quality_score = int(float(quality_str))
        except (ValueError, TypeError):
            quality_score = 3
        
        # Create entry dict
        entry = {
            'id': frontmatter.get('id'),
            'title': title,
            'url': frontmatter.get('url'),
            'source': {
                'platform': frontmatter.get('platform') or frontmatter.get('source', 'manual'),
                'author': frontmatter.get('author') or frontmatter.get('source'),
                'original_date': frontmatter.get('original_date') or frontmatter.get('date')
            },
            'summary_zh': summary_zh,
            'summary_en': None,
            'local_path': str(Path(file_path).name),
            'images': [],
            'tags': frontmatter.get('tags', []),
            'source_type': 'article',
            'language': 'zh',
            'quality_score': quality_score,
            'status': 'score-pending' if quality_score < 4 else 'active',
            'one_liner_author': 'openclaw'
        }
        
        return entry
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    # Load existing entries
    entries_data = load_entries_data()
    print(f"Existing entries: {len(entries_data['entries'])}")
    
    # Process files from git status that are new/untracked
    files_to_process = [
        'content/b3802f09.md',
        'content/e4598e7d.md',
        'content/ff9b22ff.md'
    ]
    
    new_entries = []
    
    for file_path in files_to_process:
        full_path = Path(__file__).parent / file_path
        if full_path.exists():
            entry = extract_content_file(full_path)
            if entry:
                # Check if this entry already exists
                existing_ids = [e['id'] for e in entries_data['entries']]
                if entry['id'] not in existing_ids:
                    new_entries.append(entry)
                    print(f"Found new entry: {entry['title']} (ID: {entry['id']})")
                else:
                    print(f"Entry already exists: {entry['title']} (ID: {entry['id']})")
    
    print(f"Found {len(new_entries)} new entries to process")
    
    if new_entries:
        # Use pipeline_utils to append entries
        added, skipped = append_entries(entries_data, new_entries)
        
        print(f"Added: {len(added)} entries")
        print(f"Skipped: {len(skipped)} entries")
        
        # Save the updated entries
        save_entries_data(entries_data)
        
        print(f"Total entries after processing: {len(entries_data['entries'])}")
        
        # Show added entries
        for entry in added:
            print(f"Added: {entry['title']} (ID: {entry['id']}, Category: {entry.get('category', 'uncategorized')})")
        
        return True
    else:
        print("No new entries found to process")
        return False

if __name__ == "__main__":
    main()