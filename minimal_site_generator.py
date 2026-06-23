#!/usr/bin/env python3
"""
Minimal site generator for awesome-ai-field-notes
"""

import os
import json
from datetime import datetime

def generate_site():
    """Generate the site with entries data"""
    entries_path = 'openclaw/data/entries.json'
    
    # Read entries
    with open(entries_path, 'r', encoding='utf-8') as f:
        entries_data = json.load(f)
    
    print(f"Found {len(entries_data.get('entries', []))} entries")
    
    # Create basic index page
    dist_dir = 'dist'
    os.makedirs(dist_dir, exist_ok=True)
    
    # Generate index.html
    index_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome AI Field Notes</title>
    <style>
        body {{ font-family: system-ui, sans-serif; margin: 2rem; line-height: 1.6; }}
        .entry {{ border: 1px solid #e1e4e8; margin: 1rem 0; padding: 1rem; border-radius: 8px; }}
        .entry-title {{ font-weight: bold; font-size: 1.2rem; color: #0366d6; }}
        .entry-meta {{ color: #586069; font-size: 0.9rem; margin: 0.5rem 0; }}
        .entry-summary {{ color: #24292e; margin: 0.5rem 0; }}
        .entry-category {{ background: #0366d6; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem; }}
    </style>
</head>
<body>
    <h1>Awesome AI Field Notes</h1>
    <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p>Total entries: {len(entries_data.get('entries', []))}</p>
    
    <div class="entries">
"""
    
    for entry in entries_data.get('entries', []):
        index_content += f"""
        <div class="entry">
            <div class="entry-title">{entry.get('title', 'No Title')}</div>
            <div class="entry-meta">
                Category: <span class="entry-category">{entry.get('category', 'uncategorized')}</span> | 
                Score: {entry.get('quality_score', 0)} | 
                Date: {entry.get('added_date', 'Unknown')}
            </div>
            <div class="entry-summary">{entry.get('summary_zh', 'No summary available')}</div>
        </div>
"""
    
    index_content += """
    </div>
</body>
</html>
"""
    
    with open(os.path.join(dist_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"Site generated successfully in {dist_dir}/")
    print("Daily intake task completed!")

if __name__ == '__main__':
    generate_site()
