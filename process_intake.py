import sys
sys.path.append('/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/openclaw/scripts')
from pipeline_utils import (
    load_entries_data, save_entries_data, append_entries,
    canonical_category, clean_text, normalize_url,
    normalize_platform, normalize_source_type, generate_entry_id,
    normalize_tags, is_placeholder_text, has_readable_text
)
import re
import json
from pathlib import Path
import datetime

def parse_frontmatter(yaml_text):
    """Parse YAML frontmatter manually"""
    frontmatter = {}
    for line in yaml_text.strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle nested objects
            if key == 'source' and value.startswith('{') and value.endswith('}'):
                try:
                    frontmatter[key] = json.loads(value)
                except:
                    frontmatter[key] = value
            # Handle arrays
            elif value.startswith('[') and value.endswith(']'):
                try:
                    frontmatter[key] = json.loads(value)
                except:
                    frontmatter[key] = value
            else:
                frontmatter[key] = value
    return frontmatter

def process_content_file(file_path_str):
    file_path = Path(file_path_str)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter manually
    frontmatter = {}
    content_start = 0
    if content.strip().startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parse_frontmatter(parts[1])
            content_start = len(parts[0]) + len(parts[1]) + 6
    
    content_body = content[content_start:]
    
    # Extract fields from frontmatter and content
    source_info = {}
    if isinstance(frontmatter.get('source'), dict):
        source_info = frontmatter['source']
    else:
        # Try to parse source as string
        try:
            source_info = json.loads(frontmatter.get('source', '{}'))
        except:
            source_info = {'platform': 'cubox', 'author': None, 'original_date': None}
    
    entry = {
        'id': None,
        'title': frontmatter.get('title', ''),
        'url': normalize_url(frontmatter.get('url')),
        'source': {
            'platform': source_info.get('platform', 'cubox'),
            'author': source_info.get('author'),
            'original_date': source_info.get('original_date')
        },
        'category': frontmatter.get('category'),
        'tags': frontmatter.get('tags', []),
        'source_type': normalize_source_type(frontmatter.get('source_type', 'article')),
        'language': frontmatter.get('language', 'zh'),
        'summary_zh': frontmatter.get('description', ''),
        'summary_en': frontmatter.get('summary_en'),
        'one_liner': frontmatter.get('one_liner', ''),
        'one_liner_author': frontmatter.get('one_liner_author', 'openclaw'),
        'quality_score': frontmatter.get('quality_score', 3),
        'status': frontmatter.get('status', 'active'),
        'local_path': str(file_path),
        'images': re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content_body),
        'added_date': datetime.date.today().isoformat(),
        'updated_date': datetime.date.today().isoformat(),
        'related': []
    }
    
    # Clean and normalize text
    entry['title'] = clean_text(entry['title'], max_len=120)
    entry['summary_zh'] = clean_text(entry['summary_zh'], max_len=300)
    
    # Apply canonical category
    entry['category'] = canonical_category(
        entry['category'], 
        tags=entry['tags'], 
        source_type=entry['source_type'],
        title=entry['title'],
        summary=entry['summary_zh']
    )
    
    # Normalize tags
    entry['tags'] = normalize_tags(entry['tags'])
    
    # Generate ID and one_liner if missing
    if not entry['id']:
        entry['id'] = generate_entry_id(title=entry['title'], url=entry['url'])
    if not entry['one_liner']:
        entry['one_liner'] = f'有参考价值的{entry["category"]}类内容'
    
    # Remove null and empty fields where appropriate
    entry = {k: v for k, v in entry.items() if v not in [None, ''] or k in ['summary_en', 'source.author']}
    
    return entry

# Process files
files_to_process = [
    'content/klbtvlqs.md',
    'content/pLFMQKqL.md', 
    'content/wri21wds.md',
    'content/dw7v9v1j.md'
]

new_entries = []
for file_path in files_to_process:
    if Path(file_path).exists():
        entry = process_content_file(file_path)
        new_entries.append(entry)
        print(f'Processed: {entry["id"]} - {entry["title"]}')

print(f'\nTotal new entries: {len(new_entries)}')

# Add to entries.json
if new_entries:
    try:
        current_data = load_entries_data()
        append_entries(current_data, new_entries)
        print(f'Successfully added {len(new_entries)} entries to entries.json')
    except Exception as e:
        print(f'Error adding entries: {e}')
else:
    print('No new entries to add')
