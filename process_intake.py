#!/usr/bin/env python3
"""Daily intake script for processing recent AI content files."""

import sys
import re
import json
from pathlib import Path
from datetime import date, datetime, timedelta

# Add the scripts directory to the path
sys.path.append('./openclaw/scripts')

try:
    from pipeline_utils import (
        load_entries_data, append_entries, normalize_entry, normalize_url, 
        clean_text, today_str, content_dir, normalize_date
    )
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

def extract_metadata(content):
    """Extract metadata from the YAML frontmatter"""
    metadata = {}
    metadata_lines = []
    in_metadata = False
    
    lines = content.split('\n')
    for line in lines:
        if line.strip() == '---':
            if not in_metadata:
                in_metadata = True
                continue
            else:
                break
        if in_metadata:
            metadata_lines.append(line)
    
    # Parse metadata
    for line in metadata_lines:
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Remove quotes from string values
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            
            metadata[key] = value
    
    return metadata

def extract_content(content):
    """Extract the main content after YAML frontmatter"""
    lines = content.split('\n')
    in_metadata = False
    content_lines = []
    
    for line in lines:
        if line.strip() == '---':
            in_metadata = True
            continue
        if in_metadata and line.strip() == '---':
            in_metadata = False
            continue
        if not in_metadata:
            content_lines.append(line)
    
    return '\n'.join(content_lines)

def extract_images(content):
    """Extract image URLs from markdown content"""
    image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    return [normalize_url(img) for img in images if normalize_url(img)]

def extract_summary(content):
    """Extract a summary from the content"""
    # Find the first non-empty paragraph after the metadata
    lines = content.split('\n')
    in_metadata = False
    content_lines = []
    reading_content = False
    
    for line in lines:
        if line.strip() == '---':
            in_metadata = True
            reading_content = False
            continue
        if in_metadata and line.strip() == '---':
            in_metadata = False
            reading_content = True
            continue
        if not in_metadata and reading_content:
            content_lines.append(line)
    
    # Join content and clean it
    full_content = '\n'.join(content_lines)
    # Remove markdown elements and get clean text
    clean_content = re.sub(r'!\[.*?\]\([^)]*\)', '', full_content)
    clean_content = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', clean_content)
    clean_content = re.sub(r'`([^`]+)`', r'\1', clean_content)
    clean_content = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean_content)
    
    # Get first few sentences as summary
    sentences = re.split(r'[。！？.!?]', clean_content)
    summary = sentences[0] if sentences else ""
    
    # Clean and limit summary length
    summary = clean_text(summary, max_len=200)
    if not summary:
        summary = "内容过短，待补充"
    
    return summary

def process_file(file_path):
    """Process a single markdown file and extract entry data"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Extract metadata
        metadata = extract_metadata(content)
        
        # Extract content
        content_body = extract_content(content)
        
        # Extract images
        images = extract_images(content_body)
        
        # Extract summary
        summary_zh = extract_summary(content_body)
        
        # Create entry dict
        entry = {
            'title': metadata.get('title', '未命名AI资源'),
            'url': normalize_url(metadata.get('source')),
            'source': {
                'platform': 'blog',  # Default to blog
                'author': None,
                'original_date': normalize_date(metadata.get('date'))
            },
            'category': metadata.get('category', 'uncategorized'),
            'tags': metadata.get('tags', []),
            'source_type': 'article',  # Default to article
            'language': 'zh',  # Default to Chinese
            'summary_zh': summary_zh,
            'summary_en': None,
            'one_liner': '待补充可读摘要后再发布',
            'one_liner_author': 'openclaw',
            'quality_score': int(metadata.get('quality_score', 3)),
            'status': 'score-pending',
            'local_path': str(file_path.relative_to(content_dir())),
            'images': images,
            'added_date': today_str(),
            'updated_date': today_str(),
            'github_stars': None,
            'related': []
        }
        
        # Normalize the entry
        normalized_entry = normalize_entry(entry, run_date=date.today())
        
        return normalized_entry
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    # Load existing entries data
    entries_data = load_entries_data()
    
    # Find recent files (modified yesterday or today)
    content_dir_path = content_dir()
    recent_files = []
    
    # Look for files from yesterday
    yesterday = datetime.now() - timedelta(days=1)
    cutoff_time = yesterday.timestamp()
    
    for file_path in content_dir_path.glob('*.md'):
        try:
            mod_time = file_path.stat().st_mtime
            if mod_time >= cutoff_time:
                recent_files.append(file_path)
        except:
            continue
    
    print(f"Found {len(recent_files)} recent files to process")
    
    # Process each file
    new_entries = []
    for file_path in recent_files:
        print(f"Processing {file_path.name}...")
        entry = process_file(file_path)
        if entry:
            new_entries.append(entry)
    
    # Add entries to the data
    if new_entries:
        added, skipped = append_entries(entries_data, new_entries)
        print(f"Added {len(added)} entries, skipped {len(skipped)}")
        
        # Save the updated data
        save_entries_data(entries_data)
        print("Entries saved to entries.json")
    else:
        print("No new entries to add")

if __name__ == "__main__":
    main()
