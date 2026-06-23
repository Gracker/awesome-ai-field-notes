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
    # 获取最近24小时内修改的文件
    entries_path = pipeline_utils.entries_path()
    content_dir = os.path.join(os.path.dirname(entries_path), 'content')
    
    # 扫描content目录下最近修改的文件
    recent_files = []
    cutoff_time = os.path.getmtime(entries_path)
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if os.path.getmtime(file_path) > cutoff_time:
                    recent_files.append(file_path)
    
    if not recent_files:
        print("No recent files found")
        return
    
    print(f"Found {len(recent_files)} recent files to process")
    
    # 加载现有entries
    entries_data = pipeline_utils.load_entries_data()
    
    # 处理每个文件
    processed_count = 0
    for file_path in recent_files:
        # 检查是否是AI相关内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pipeline_utils.is_ai_related_entry({'local_path': os.path.relpath(file_path, os.path.dirname(entries_path))}):
            entry = process_markdown_file(file_path)
            if entry:
                # 标准化entry
                normalized_entry = pipeline_utils.normalize_entry(entry)
                
                # 添加到entries
                entries_data = pipeline_utils.append_entries(entries_data, [normalized_entry])
                
                # 保存content文件
                content_file_path = os.path.join(os.path.dirname(entries_path), normalized_entry['local_path'])
                os.makedirs(os.path.dirname(content_file_path), exist_ok=True)
                with open(content_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Processed: {normalized_entry['title']}")
                processed_count += 1
                
                # 限制单次处理数量
                if processed_count >= 20:
                    break
    
    # 保存entries
    pipeline_utils.save_entries_data(entries_data)
    print(f"Daily intake completed. Processed {processed_count} entries.")

if __name__ == '__main__':
    main()
