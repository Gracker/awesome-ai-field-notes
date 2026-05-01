#!/usr/bin/env python3
"""
Process new AI entries and add them to entries.json
Following the awesome-ai-field-notes schema and workflow
"""

import json
import re
import os
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CONTENT_DIR = BASE_DIR / "content"
ENTRIES_FILE = DATA_DIR / "entries.json"
CATEGORIES_FILE = DATA_DIR / "categories.json"

def load_json(file_path):
    """Load JSON file with error handling"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return {}

def save_json(data, file_path):
    """Save data to JSON file"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_id(title, date_str):
    """Generate 8-character nanoid-like ID"""
    # Simple hash-based ID generation
    import hashlib
    content = f"{title}{date_str}".encode('utf-8')
    hash_obj = hashlib.sha256(content)
    hex_digest = hash_obj.hexdigest()
    return hex_digest[:8]

def extract_images(content):
    """Extract image URLs from markdown content"""
    image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    images = re.findall(image_pattern, content)
    return images

def extract_summary(content, min_length=100, max_length=300):
    """Extract summary from content"""
    # Clean content by removing metadata and markdown
    lines = content.split('\n')
    content_lines = []
    
    # Skip metadata lines
    skip_patterns = [
        r'^\s*-\s*\*\*来源\*\*:',
        r'^\s*-\s*\*\*原文链接\*\*:',
        r'^\s*-\s*\*\*作者\*\*:',
        r'^\s*-\s*\*\*日期\*\*:',
        r'^\s*-\s*\*\*抓取时间\*\*:',
        r'^URL Source:',
        r'^Published Time:',
    ]
    
    for line in lines:
        line = line.strip()
        if any(re.match(pattern, line) for pattern in skip_patterns):
            continue
        if line and not line.startswith('#'):
            content_lines.append(line)
    
    content_text = ' '.join(content_lines)
    
    # Extract summary - take first substantial paragraph
    if len(content_text) < min_length:
        return content_text[:min_length] if len(content_text) > 0 else "内容过短，待补充"
    
    # Try to find a good summary by looking for key sentences
    sentences = re.split(r'[.!?。！？]', content_text)
    summary = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20:  # Minimum meaningful sentence length
            summary.append(sentence)
            current_length += len(sentence) + 1
            if current_length >= max_length:
                break
    
    summary_text = '. '.join(summary).strip()
    if len(summary_text) < min_length:
        summary_text = content_text[:max_length]
    
    return summary_text[:max_length]

def classify_and_score(entry_data):
    """Classify and score entry based on SCHEMA.md criteria"""
    content = entry_data.get('content', '')
    title = entry_data.get('title', '')
    
    # Category classification based on title and content
    category_keywords = {
        'models/models': ['gpt', 'gemini', 'claude', 'model', 'llm'],
        'agents/frameworks': ['agent', 'framework', 'mcp', 'orchestration'],
        'development/tools': ['claude code', 'development', 'coding', '工具'],
        'applications/knowledge': ['knowledge', '学习', 'education', '研究'],
    }
    
    category = 'uncategorized'
    for cat, keywords in category_keywords.items():
        if any(keyword.lower() in title.lower() or keyword.lower() in content.lower() for keyword in keywords):
            category = cat
            break
    
    # Quality scoring based on SCHEMA.md criteria
    score = 3  # Default: 有参考价值
    
    if any(keyword in title.lower() for keyword in ['gpt-5.5', '官方指南']):
        score = 4  # 高质量原创：官方指南，独到洞察
    
    if '知识图谱' in title or ' Buffett' in content:
        score = 4  # 高质量原创：完整实现/深度分析
    
    if 'tutorial' in title.lower() or '教程' in title:
        score = 3  # 有参考价值：信息准确，但缺少独特视角
    
    return {
        'category': category,
        'quality_score': score,
        'source_type': 'article',
        'language': 'zh' if any(char in content for char in ['中文', '教程', '指南']) else 'en',
        'status': 'active'
    }

def process_entry(content_file_path, content):
    """Process a single entry"""
    # Extract metadata from content
    lines = content.split('\n')
    
    title_match = re.search(r'# (.+)', content)
    title = title_match.group(1) if title_match else content_file_path.stem
    
    # Extract metadata
    source_info = {}
    author = None
    url = None
    date = None
    
    for line in lines:
        if '**来源**' in line or '来源：' in line:
            source_match = re.search(r'X/Twitter|X 文章', line)
            if source_match:
                source_info['platform'] = 'x' if source_match.group() == 'X/Twitter' else 'x'
        
        if '**作者**' in line or '作者：' in line:
            author_match = re.search(r'[\u4e00-\u9fff]+', line)
            if author_match:
                author = author_match.group()
        
        if '**原文链接**' in line or '原文链接：' in line:
            url_match = re.search(r'https?://[^)]+', line)
            if url_match:
                url = url_match.group()
        
        if '**日期**' in line or '日期：' in line:
            date_match = re.search(r'2026-\d{2}-\d{2}', line)
            if date_match:
                date = date_match.group()
    
    # Generate entry data
    entry_data = {
        'id': generate_id(title, date or datetime.now().strftime('%Y-%m-%d')),
        'title': title,
        'url': url,
        'source': {
            'platform': source_info.get('platform', 'x'),
            'author': author,
            'original_date': date
        },
        'summary_zh': extract_summary(content),
        'summary_en': None,
        'one_liner': '',
        'one_liner_author': 'openclaw',
        'local_path': str(content_file_path.relative_to(BASE_DIR.parent.parent)),
        'images': extract_images(content),
        'added_date': datetime.now().strftime('%Y-%m-%d'),
        'updated_date': None,
        'tags': [],
        'github_stars': None,
        'related': []
    }
    
    # Classify and score
    classification = classify_and_score(entry_data)
    entry_data.update(classification)
    
    # Generate one-liner
    if entry_data['quality_score'] >= 4:
        entry_data['one_liner'] = f"高质量{entry_data['category'].split('/')[-1]}资源，值得关注"
    elif entry_data['quality_score'] == 3:
        entry_data['one_liner'] = f"有参考价值的{entry_data['category'].split('/')[-1]}内容"
    else:
        entry_data['one_liner'] = f"{entry_data['category'].split('/')[-1]}相关资源"
    
    return entry_data

def main():
    """Main processing function"""
    print("🚀 Processing new AI entries...")
    
    # Load existing data
    existing_entries = load_json(ENTRIES_FILE)
    if isinstance(existing_entries, dict) and 'entries' in existing_entries:
        entries = existing_entries['entries']
    else:
        entries = existing_entries if isinstance(existing_entries, list) else []
    
    # Find content files that don't have entries yet
    content_files = list(CONTENT_DIR.glob("*.md"))
    content_bases = {f.stem for f in content_files}
    
    # Process each content file
    new_entries = []
    for content_file in content_files:
        content_base = content_file.stem
        
        # Skip if already in entries
        if any(entry.get('id') == content_base for entry in entries):
            continue
        
        # Read content
        try:
            content = content_file.read_text(encoding='utf-8')
            entry_data = process_entry(content_file, content)
            
            # Check for duplicates by URL and title
            is_duplicate = False
            for existing_entry in entries:
                if (existing_entry.get('url') == entry_data['url'] and entry_data['url'] is not None):
                    is_duplicate = True
                    break
                # Simple title similarity check (basic implementation)
                if existing_entry.get('title') == entry_data['title']:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                new_entries.append(entry_data)
                print(f"✅ New entry: {entry_data['title']} (ID: {entry_data['id']}, Score: {entry_data['quality_score']})")
            else:
                print(f"⚠️  Duplicate skipped: {entry_data['title']}")
                
        except Exception as e:
            print(f"❌ Error processing {content_file}: {e}")
    
    # Add new entries
    if new_entries:
        entries.extend(new_entries)
        
        # Sort by date (newest first)
        entries.sort(key=lambda x: x.get('added_date', '0000-00-00'), reverse=True)
        
        # Save updated entries
        output_data = {
            'entries': entries,
            'last_updated': datetime.now().isoformat(),
            'total_entries': len(entries)
        }
        
        save_json(output_data, ENTRIES_FILE)
        print(f"✅ Added {len(new_entries)} new entries to entries.json")
        
        # Run site generation
        print("🔄 Generating site...")
        import subprocess
        result = subprocess.run([
            'python3', 
            str(BASE_DIR / 'openclaw' / 'scripts' / 'generate-site.py')
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Site generation completed")
            print(f"📊 Stats: {result.stdout.strip()}")
        else:
            print(f"❌ Site generation failed: {result.stderr}")
    else:
        print("✅ No new entries to add")
    
    print("🎉 Processing completed!")

if __name__ == "__main__":
    main()