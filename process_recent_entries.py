#!/usr/bin/env python3
"""Process recent content files and append them to entries.json"""

import json
import re
import sys
from pathlib import Path
from datetime import date, datetime, timedelta

# Add the scripts directory to the path
sys.path.append('./openclaw/scripts')
from pipeline_utils import load_entries_data, save_entries_data, append_entries, normalize_entry

def extract_metadata_from_file(file_path: Path) -> dict:
    """Extract metadata and content from markdown files"""
    content = file_path.read_text(encoding='utf-8')
    
    # Extract metadata from header
    metadata = {}
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('> **Source:**'):
            metadata['url'] = line.replace('> **Source:**', '').strip()
        elif line.startswith('> **Author:**'):
            metadata['author'] = line.replace('> **Author:**', '').strip().replace('@', '')
        elif line.startswith('> **Platform:**'):
            metadata['platform'] = line.replace('> **Platform:**', '').strip()
        elif line.startswith('> **Original Date:**'):
            metadata['original_date'] = line.replace('> **Original Date:**', '').strip()
        elif line.startswith('> **Quality Score:**'):
            metadata['quality_score'] = int(line.replace('> **Quality Score:**', '').strip())
    
    # Extract title
    title_match = re.match(r'# (.+)', content.split('\n')[0])
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # Extract summaries
    sections = content.split('---')
    if len(sections) > 1:
        content_section = sections[1]
        
        # Extract English summary
        english_match = re.search(r'## English\n(.+?)(?=##|\Z)', content_section, re.DOTALL)
        if english_match:
            metadata['summary_en'] = english_match.group(1).strip()
        
        # Extract Chinese summary  
        chinese_match = re.search(r'## 中文\n(.+?)(?=##|\Z)', content_section, re.DOTALL)
        if chinese_match:
            metadata['summary_zh'] = chinese_match.group(1).strip()
    
    # Extract one-liner
    one_liner_match = re.search(r'一句话总结：(.+)', content)
    if one_liner_match:
        metadata['one_liner'] = one_liner_match.group(1).strip()
    
    # Set default values
    metadata.setdefault('source_type', 'x_post')
    metadata.setdefault('language', 'both')
    metadata.setdefault('tags', ['attention-mechanism', 'llm-optimization', 'efficiency'])
    metadata.setdefault('status', 'score-pending')
    metadata.setdefault('local_path', str(file_path.relative_to(Path('./content'))))
    
    return metadata

def main():
    # Load existing entries
    entries_data = load_entries_data()
    
    # Find recent content files
    content_dir = Path('./content')
    recent_files = []
    for file_path in content_dir.glob('*.md'):
        if datetime.fromtimestamp(file_path.stat().st_mtime) > datetime.now() - timedelta(days=1):
            recent_files.append(file_path)
    
    print(f"Found {len(recent_files)} recent files to process")
    
    # Process each file
    raw_entries = []
    for file_path in recent_files:
        print(f"Processing {file_path.name}")
        metadata = extract_metadata_from_file(file_path)
        
        # Normalize the entry
        normalized_entry = normalize_entry(metadata, run_date=date.today())
        raw_entries.append(normalized_entry)
    
    # Append entries to the data
    added, skipped = append_entries(entries_data, raw_entries)
    
    print(f"Added {len(added)} entries, skipped {len(skipped)}")
    
    # Save the updated entries
    save_entries_data(entries_data)
    
    # Print summary
    if added:
        print("\nAdded entries:")
        for entry in added:
            print(f"- {entry['title']} ({entry['id']})")
    
    if skipped:
        print("\nSkipped entries:")
        for entry, reason in skipped:
            print(f"- {entry['title']} ({reason})")

if __name__ == "__main__":
    main()