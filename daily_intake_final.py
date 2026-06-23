#!/usr/bin/env python3
"""
Daily Intake Task for awesome-ai-field-notes
处理每日新增/修改的AI相关内容，提取元数据并写入entries.json
"""

import os
import re
import json
import yaml
from datetime import datetime, timedelta
import sys
sys.path.append('/Users/gracker/.openclaw/workspace')
from openclaw.scripts import pipeline_utils

def extract_metadata_from_content(content):
    """从文件内容中提取元数据"""
    metadata = {}
    
    # 查找YAML frontmatter
    yaml_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if yaml_match:
        try:
            yaml_content = yaml_match.group(1)
            metadata.update(yaml.safe_load(yaml_content) or {})
        except:
            pass
    
    # 从正文中提取URL
    if not metadata.get('url'):
        url_matches = re.findall(r'https://[^\s\)\]\}\"]+', content)
        if url_matches:
            metadata['url'] = url_matches[0]
    
    # 清理相对日期
    if metadata.get('original_date') and isinstance(metadata['original_date'], str):
        if metadata['original_date'] in pipeline_utils.RELATIVE_DATES:
            today = pipeline_utils.today_str()
            if metadata['original_date'] == '昨天':
                yesterday = (datetime.strptime(today, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
                metadata['original_date'] = yesterday
            elif metadata['original_date'] == '今天':
                metadata['original_date'] = today
    
    return metadata

def extract_summary_and_content(content, language):
    """提取摘要和内容"""
    # 移除YAML frontmatter
    clean_content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    
    # 提取图片URL
    images = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', clean_content)
    
    # 生成摘要
    summary_zh = None
    summary_en = None
    
    # 如果是英文或双语内容
    if language in ['en', 'both']:
        # 提取英文摘要
        paragraphs = re.split(r'\n\s*\n', clean_content)
        if len(paragraphs) > 0:
            # 取第一段作为英文摘要
            english_text = paragraphs[0].strip()
            if len(english_text) > 100:
                summary_en = english_text[:300] + ('...' if len(english_text) > 300 else '')
        
        # 中文翻译摘要
        if language == 'both':
            # 这里简化处理，实际应该翻译或从中文部分提取
            summary_zh = clean_content[:300] + ('...' if len(clean_content) > 300 else '')
    
    # 如果只有中文内容
    elif language == 'zh':
        summary_zh = clean_content[:300] + ('...' if len(clean_content) > 300 else '')
    
    return summary_zh, summary_en, images

def determine_language(content):
    """确定内容语言"""
    # 简单的语言检测
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
    english_chars = len(re.findall(r'[a-zA-Z]', content))
    
    if chinese_chars > english_chars * 2:
        return 'zh'
    elif english_chars > chinese_chars * 2:
        return 'en'
    else:
        return 'both'

def classify_and_score(content, title, summary_zh):
    """分类和评分"""
    # 使用pipeline_utils的分类功能
    category = pipeline_utils.canonical_category(title + ' ' + (summary_zh or ''))
    
    # 简单评分逻辑
    content_length = len(content)
    keywords = ['AI', 'artificial intelligence', 'model', 'agent', 'neural', 'deep learning']
    keyword_score = sum(1 for keyword in keywords if keyword.lower() in content.lower())
    
    if 'breakthrough' in content.lower() or 'milestone' in content.lower():
        quality_score = 5
    elif 'research' in content.lower() or 'analysis' in content.lower():
        quality_score = 4
    elif 'tutorial' in content.lower() or 'guide' in content.lower():
        quality_score = 3
    else:
        quality_score = min(3, max(1, keyword_score))
    
    return category, quality_score

def process_markdown_file(file_path):
    """处理单个markdown文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return None
    
    # 提取元数据
    metadata = extract_metadata_from_content(content)
    
    # 确定语言
    language = determine_language(content)
    
    # 提取摘要和图片
    summary_zh, summary_en, images = extract_summary_and_content(content, language)
    
    # 生成标题
    title = metadata.get('title', '')
    if not title:
        # 从第一行标题提取
        title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            title = os.path.basename(file_path).replace('.md', '')
    
    # 分类和评分
    category, quality_score = classify_and_score(content, title, summary_zh)
    
    # 构建entry
    entry = {
        'id': pipeline_utils.generate_entry_id(),
        'title': title,
        'url': metadata.get('url'),
        'source': {
            'platform': metadata.get('platform', 'manual'),
            'author': metadata.get('author'),
            'original_date': metadata.get('original_date')
        },
        'category': category,
        'tags': metadata.get('tags', []),
        'source_type': metadata.get('source_type', 'article'),
        'language': language,
        'summary_zh': summary_zh,
        'summary_en': summary_en,
        'one_liner': pipeline_utils.derive_one_liner(title, summary_zh, category),
        'one_liner_author': 'openclaw',
        'quality_score': quality_score,
        'status': 'active',
        'local_path': os.path.relpath(file_path, '/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes'),
        'images': images,
        'added_date': pipeline_utils.today_str(),
        'updated_date': pipeline_utils.today_str(),
        'github_stars': metadata.get('github_stars'),
        'related': []
    }
    
    return entry

def main():
    """主函数"""
    # 获取文件路径
    entries_path = pipeline_utils.entries_path()
    content_dir = os.path.join(os.path.dirname(entries_path), 'content')
    
    print(f"Entries path: {entries_path}")
    print(f"Content directory: {content_dir}")
    
    # 查找最近修改的文件（过去24小时）
    recent_files = []
    cutoff_time = datetime.now().timestamp() - 24 * 60 * 60  # 24 hours ago
    
    print(f"Looking for files modified after: {cutoff_time}")
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                file_mtime = os.path.getmtime(file_path)
                if file_mtime > cutoff_time:
                    recent_files.append(file_path)
                    print(f"Found recent file: {file_path} (mtime: {file_mtime})")
    
    if not recent_files:
        # Fallback: use the hardcoded list from earlier
        print("No recent files found, using hardcoded list")
        hardcoded_files = [
            "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/content/2155d7cb.md",
            "/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes/content/b0d10e8d.md"
        ]
        for file_path in hardcoded_files:
            if os.path.exists(file_path):
                recent_files.append(file_path)
    
    if not recent_files:
        print("No files to process")
        return
    
    print(f"Found {len(recent_files)} files to process")
    
    # 加载现有entries
    entries_data = pipeline_utils.load_entries_data()
    print(f"Loaded {len(entries_data.get('entries', []))} existing entries")
    
    # 确保entries_data是正确的格式
    if isinstance(entries_data, tuple):
        entries_data = entries_data[0]  # 取第一个元素
    if not isinstance(entries_data, dict):
        entries_data = {'entries': entries_data if isinstance(entries_data, list) else [], 'last_updated': pipeline_utils.today_str(), 'total_entries': 0}
    
    # 处理每个文件
    processed_count = 0
    new_entries = []
    
    for file_path in recent_files:
        try:
            # 检查是否是AI相关内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否为AI相关
            ai_indicators = ['AI', 'artificial intelligence', 'model', 'agent', 'machine learning', 'neural', 'claude', 'gemini', 'gpt', 'anthropic', 'openai']
            is_ai_related = any(indicator.lower() in content.lower() for indicator in ai_indicators)
            
            if is_ai_related:
                print(f"Processing AI-related file: {file_path}")
                entry = process_markdown_file(file_path)
                if entry:
                    # 标准化entry
                    normalized_entry = pipeline_utils.normalize_entry(entry)
                    new_entries.append(normalized_entry)
                    
                    print(f"Added entry: {normalized_entry['title']}")
                    processed_count += 1
                    
                    # 限制单次处理数量
                    if processed_count >= 20:
                        break
            else:
                print(f"Skipping non-AI file: {file_path}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    if new_entries:
        # 使用append_entries添加新条目
        try:
            entries_data = pipeline_utils.append_entries(entries_data, new_entries)
            # 确保返回的是字典
            if isinstance(entries_data, tuple):
                entries_data = entries_data[0]
            
            # 更新统计信息
            entries_data['last_updated'] = pipeline_utils.today_str()
            entries_data['total_entries'] = len(entries_data.get('entries', []))
            
            # 保存entries
            pipeline_utils.save_entries_data(entries_data)
            print(f"Daily intake completed. Processed {processed_count} entries.")
        except Exception as e:
            print(f"Error saving entries: {e}")
            # 手动保存
            with open(entries_path, 'w', encoding='utf-8') as f:
                json.dump(entries_data, f, ensure_ascii=False, indent=2)
            print("Manual save completed")
    else:
        print("No new entries to add")

if __name__ == '__main__':
    main()
