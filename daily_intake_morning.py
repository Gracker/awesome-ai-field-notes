#!/usr/bin/env python3
"""Daily intake morning pipeline for AAIF"""

import os
import re
import sys
from datetime import datetime, timedelta, date
from pathlib import Path
import json

# Add pipeline utils to path
sys.path.insert(0, str(Path(__file__).parent / "openclaw/scripts"))
from pipeline_utils import (
    load_entries_data, 
    save_entries_data, 
    append_entries,
    normalize_entry,
    today_str,
    normalize_url,
    clean_text,
    generate_entry_id
)

def extract_paper_metadata(content_path: Path) -> dict | None:
    """Extract metadata from arxiv paper content files"""
    try:
        content = content_path.read_text(encoding="utf-8")
        
        # Extract arxiv ID from content
        arxiv_match = re.search(r'\[(\d+\.\d+)\]', content[:2000])
        if not arxiv_match:
            return None
            
        arxiv_id = arxiv_match.group(1)
        
        # Extract title
        title_match = re.search(r'\[([^\]]+)\]', content)
        title = title_match.group(1) if title_match else f"Paper {arxiv_id}"
        
        # Generate metadata
        entry = {
            "id": generate_entry_id(title=title, url=f"https://arxiv.org/abs/{arxiv_id}"),
            "title": title,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "source": {
                "platform": "arxiv",
                "author": None,
                "original_date": None
            },
            "source_type": "paper",
            "summary_zh": f"ArXiv论文: {title} - 需要进一步提取摘要",
            "summary_en": f"ArXiv paper: {title} - Summary needs extraction",
            "category": "learning",
            "tags": ["arxiv", "paper", "research"],
            "one_liner": f"AI research paper: {title[:80]}{'...' if len(title) > 80 else ''}",
            "one_liner_author": "openclaw",
            "quality_score": 3,
            "status": "active",
            "local_path": str(content_path),
            "images": [],
            "added_date": today_str(),
            "updated_date": None,
            "language": "both",
            "related": []
        }
        
        return entry
        
    except Exception as e:
        print(f"Error processing {content_path}: {e}")
        return None

def main():
    repo_root = Path(__file__).parent
    content_dir = repo_root / "content"
    
    # Load existing entries
    print("Loading existing entries...")
    entries_data = load_entries_data()
    print(f"Current entries: {len(entries_data.get('entries', []))}")
    
    # Find recent content files (within 24h)
    print("Scanning for recent content files...")
    recent_files = []
    cutoff_time = datetime.now() - timedelta(hours=24)
    
    for content_file in content_dir.glob("*.md"):
        if content_file.stat().st_mtime > cutoff_time.timestamp():
            recent_files.append(content_file)
    
    print(f"Found {len(recent_files)} recent files")
    
    # Process recent files
    new_entries = []
    for content_file in recent_files:
        print(f"Processing: {content_file.name}")
        entry = extract_paper_metadata(content_file)
        if entry:
            # Check if already exists
            url_key = normalize_url(entry.get("url"))
            existing_urls = {
                normalize_url(e.get("url")) 
                for e in entries_data.get("entries", [])
                if e.get("url")
            }
            
            if url_key not in existing_urls:
                new_entries.append(entry)
                print(f"  ✓ New entry: {entry['title']}")
            else:
                print(f"  - Entry already exists: {entry['title']}")
    
    # Add new entries
    if new_entries:
        print(f"\nAdding {len(new_entries)} new entries...")
        added, skipped = append_entries(entries_data, new_entries)
        
        print(f"Added: {len(added)} entries")
        print(f"Skipped: {len(skipped)} entries")
        
        # Save updated entries
        save_entries_data(entries_data)
        print(f"Total entries now: {len(entries_data['entries'])}")
    else:
        print("No new entries to add")
    
    # Generate site
    print("\nGenerating site...")
    try:
        generate_script = repo_root / "scripts" / "generate-site.py"
        result = os.system(f"python3 {generate_script}")
        if result == 0:
            print("✓ Site generated successfully")
        else:
            print(f"✗ Site generation failed with code {result}")
    except Exception as e:
        print(f"✗ Error generating site: {e}")
    
    # Report results
    print(f"\n=== Daily Intake Morning Report ===")
    print(f"Date: {today_str()}")
    print(f"Processed files: {len(recent_files)}")
    print(f"New entries added: {len(new_entries)}")
    print(f"Total entries: {len(entries_data['entries'])}")
    print(f"Last updated: {entries_data.get('last_updated', 'N/A')}")
    print("Push status: No push (as per mode instruction)")

if __name__ == "__main__":
    main()
