#!/usr/bin/env python3
"""Daily intake processor for awesome-ai-field-notes"""

import json
import re
from datetime import datetime, date
from pathlib import Path
import sys
import os

# Add the openclaw/scripts directory to Python path for pipeline_utils
script_dir = Path(__file__).parent / "openclaw/scripts"
sys.path.insert(0, str(script_dir))

from pipeline_utils import (
    load_entries_data, 
    save_entries_data, 
    append_entries, 
    normalize_entry,
    today_str,
    content_dir
)

def extract_content_from_file(file_path: Path) -> dict:
    """Extract structured content from a markdown file"""
    
    content = file_path.read_text(encoding='utf-8')
    
    # Extract title (first h1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "未命名 AI 资源"
    
    # Extract English and Chinese sections
    english_section = ""
    chinese_section = ""
    
    # Look for standard format: English title, then "英文原文", then "中文翻译"
    lines = content.split('\n')
    in_english = False
    in_chinese = False
    
    for line in lines:
        line = line.strip()
        if line == "英文原文":
            in_english = True
            in_chinese = False
            continue
        elif line == "中文翻译":
            in_chinese = True
            in_english = False
            continue
        elif line.startswith("#") and not line.startswith("##"):
            # Skip section headers
            continue
        
        if in_english:
            english_section += line + "\n"
        elif in_chinese:
            chinese_section += line + "\n"
    
    # Clean up sections
    english_section = english_section.strip()
    chinese_section = chinese_section.strip()
    
    # Generate summary (first 200 chars of English or Chinese)
    if english_section:
        summary = english_section[:200] + "..." if len(english_section) > 200 else english_section
    else:
        summary = chinese_section[:200] + "..." if len(chinese_section) > 200 else chinese_section
    
    # Extract images
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    
    # Extract tags from content (look for common patterns)
    tags = []
    tag_patterns = [
        r'#[\w\u4e00-\u9fff]+',
        r'##[\w\u4e00-\u9fff]+',
        r'关键词[:：]\s*([^#\n]+)',
        r'tags[:：]\s*([^#\n]+)'
    ]
    
    for pattern in tag_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            # Clean up tag matches
            tag = re.sub(r'[^\w\u4e00-\u9fff]', '', match).strip()
            if tag and len(tag) > 1:
                tags.append(tag)
    
    # Remove duplicates and limit
    tags = list(dict.fromkeys(tags))[:8]
    
    # Determine source type based on title/content
    source_type = "article"
    if "anthropic" in title.lower():
        source_type = "paper"
    elif "twitter" in title.lower() or "x.com" in content.lower():
        source_type = "x_post"
    
    # Determine platform
    platform = "manual"
    if "anthropic" in title.lower() or content.lower():
        platform = "anthropic"
    elif "github" in content.lower():
        platform = "github"
    elif "arxiv" in content.lower():
        platform = "arxiv"
    elif "twitter" in content.lower() or "x.com" in content.lower():
        platform = "x"
    
    return {
        "title": title,
        "summary_zh": chinese_section[:500] + "..." if len(chinese_section) > 500 else chinese_section,
        "summary_en": english_section[:500] + "..." if len(english_section) > 500 else english_section,
        "source": {
            "platform": platform,
            "author": None,  # Will be filled if needed
            "original_date": None
        },
        "source_type": source_type,
        "language": "both" if english_section and chinese_section else "zh",
        "tags": tags,
        "images": images,
        "local_path": str(file_path),
        "one_liner_author": "openclaw",
        "quality_score": 4,  # Default high quality for manually curated content
        "status": "active"
    }

def main():
    """Process daily intake"""
    print(f"Starting daily intake processing - {today_str()}")
    
    # Load existing entries
    try:
        entries_data = load_entries_data()
        existing_count = len(entries_data.get("entries", []))
        print(f"Existing entries count: {existing_count}")
    except Exception as e:
        print(f"Error loading entries: {e}")
        entries_data = {"entries": [], "last_updated": today_str(), "total_entries": 0}
    
    # Find files modified in last 24 hours
    content_dir_path = Path(__file__).parent / "content"
    recent_files = []
    
    # Look for files with recent modification dates (in last 24 hours)
    print(f"Looking for files in: {content_dir_path}")
    for file_path in content_dir_path.glob("*.md"):
        # Check if file was modified in last 24 hours
        stat = file_path.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        time_diff = (datetime.now() - mod_time).total_seconds()
        if time_diff < 86400:  # 24 hours
            recent_files.append(file_path)
            print(f"  Found recent file: {file_path.name} (modified {time_diff/3600:.1f} hours ago)")
        else:
            print(f"  Skipping old file: {file_path.name} (modified {time_diff/3600:.1f} hours ago)")
    
    print(f"Found {len(recent_files)} recent files to process")
    
    if not recent_files:
        print("No recent files to process")
        return
    
    # Process each file
    new_entries = []
    for file_path in recent_files:
        print(f"Processing: {file_path.name}")
        
        try:
            entry_data = extract_content_from_file(file_path)
            normalized_entry = normalize_entry(entry_data, run_date=date.today())
            new_entries.append(normalized_entry)
            
            print(f"  - Title: {normalized_entry['title']}")
            print(f"  - Category: {normalized_entry['category']}")
            print(f"  - Score: {normalized_entry['quality_score']}")
            
        except Exception as e:
            print(f"  - Error processing {file_path.name}: {e}")
            continue
    
    if not new_entries:
        print("No valid entries to add")
        return
    
    # Append entries using pipeline_utils
    try:
        added, skipped = append_entries(entries_data, new_entries)
        
        print(f"Added {len(added)} entries, skipped {len(skipped)}")
        
        # Save updated entries
        save_entries_data(entries_data)
        
        # Copy content files to content/ directory (if not already there)
        content_dir_path.mkdir(exist_ok=True)
        for entry in added:
            entry_id = entry['id']
            source_file = Path(entry['local_path'])
            dest_file = content_dir / f"{entry_id}.md"
            
            if source_file.exists() and not dest_file.exists():
                dest_file.write_text(source_file.read_text(encoding='utf-8'), encoding='utf-8')
                print(f"  - Copied content to: {dest_file.name}")
        
        print(f"Total entries: {len(entries_data.get('entries', []))}")
        
        # Generate summary
        categories = {}
        for entry in added:
            cat = entry['category']
            categories[cat] = categories.get(cat, 0) + 1
        
        summary = {
            "date": today_str(),
            "processed_files": len(recent_files),
            "added_entries": len(added),
            "skipped_entries": len(skipped),
            "categories": categories,
            "total_entries": len(entries_data.get('entries', [])),
            "previous_count": existing_count
        }
        
        print("Processing summary:")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        
    except Exception as e:
        print(f"Error appending entries: {e}")
        raise

if __name__ == "__main__":
    main()