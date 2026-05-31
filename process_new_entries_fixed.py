#!/usr/bin/env python3
"""Process new AI content entries and add to entries.json"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
import os

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
        
        # Extract summary from content
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
                if len(summary_lines) >= 10:  # Limit summary length
                    break
        
        summary_zh = '\n'.join(summary_lines)
        summary_en = None
        
        # Extract images
        images = []
        image_matches = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
        for img in image_matches[:5]:  # Max 5 images
            images.append(img)
        
        # Process dates - convert relative dates to absolute
        current_date = datetime.now()
        original_date = frontmatter.get('date')
        
        if original_date:
            # Handle relative dates
            if original_date.lower() in ['today', '今天']:
                original_date = current_date.strftime('%Y-%m-%d')
            elif original_date.lower() in ['yesterday', '昨天']:
                original_date = (current_date - timedelta(days=1)).strftime('%Y-%m-%d')
            elif original_date.lower() in ['this week', '本周']:
                # This week starts on Monday
                days_since_monday = current_date.weekday()
                start_of_week = current_date - timedelta(days=days_since_monday)
                original_date = start_of_week.strftime('%Y-%m-%d')
            elif original_date.lower() in ['last week', '上周']:
                days_since_monday = current_date.weekday()
                start_of_last_week = current_date - timedelta(days=days_since_monday + 7)
                original_date = start_of_last_week.strftime('%Y-%m-%d')
        
        # Create entry dict
        entry = {
            'id': frontmatter.get('id'),
            'title': title,
            'url': frontmatter.get('url'),
            'source': {
                'platform': frontmatter.get('source', 'manual'),
                'author': frontmatter.get('author'),
                'original_date': original_date
            },
            'summary_zh': summary_zh,
            'summary_en': summary_en,
            'local_path': str(file_path.relative_to(Path.cwd())),
            'images': images,
            'tags': [],
            'source_type': 'article',
            'language': 'zh',
            'quality_score': 3,
            'status': 'score-pending',
            'one_liner_author': 'openclaw'
        }
        
        return entry
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def check_files_modified_in_last_hours(hours=24):
    """Check which files were modified in the last N hours"""
    content_dir = Path(__file__).parent / "content"
    current_time = datetime.now()
    cutoff_time = current_time - timedelta(hours=hours)
    
    modified_files = []
    
    for file_path in content_dir.glob("*.md"):
        try:
            file_mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            if file_mtime >= cutoff_time:
                modified_files.append(file_path)
        except Exception as e:
            print(f"Error checking {file_path}: {e}")
    
    return modified_files

def main():
    # Get the project root
    project_root = Path(__file__).parent
    content_dir = project_root / "content"
    
    # Load existing entries
    entries_data = load_entries_data()
    print(f"Existing entries: {len(entries_data['entries'])}")
    
    # Find content files modified in the last 24 hours
    new_entries = []
    modified_files = check_files_modified_in_last_hours(24)
    
    print(f"Found {len(modified_files)} files modified in last 24 hours")
    
    for file_path in modified_files:
        entry = extract_content_file(file_path)
        if entry:
            # Generate ID if not present
            if not entry['id']:
                from pipeline_utils import generate_entry_id
                entry['id'] = generate_entry_id(title=entry['title'], url=entry['url'])
            
            new_entries.append(entry)
            print(f"Found new entry: {entry['title']}")
    
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