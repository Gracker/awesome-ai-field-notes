#!/usr/bin/env python3
"""Fix validation errors in entries.json"""

import json
from pathlib import Path

def main():
    # Load entries
    with open('entries.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Fix errors
    for entry in data['entries']:
        # Fix source_type
        if entry.get('source_type') == 'blog_post':
            entry['source_type'] = 'article'
            print(f"Fixed source_type for entry {entry.get('id', 'unknown')}: blog_post -> article")
        
        # Fix missing local_path
        if entry.get('local_path') is None or entry.get('local_path') == 'MISSING':
            entry['local_path'] = f"content/{entry.get('id', 'unknown')}.md"
            print(f"Fixed local_path for entry {entry.get('id', 'unknown')}")
    
    # Save fixed entries
    with open('entries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Validation errors fixed")

if __name__ == '__main__':
    main()
