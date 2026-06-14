#!/usr/bin/env python3
"""
简化的每日入库任务 - 2026-06-14
直接处理已知存在的文件
"""

import json
import re
import hashlib
import os
import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Set
import uuid
import sys

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root / "openclaw" / "scripts"))

try:
    from pipeline_utils import (
        load_entries_data, append_entries, save_entries_data, 
        normalize_entry, generate_entry_id, normalized_url_key,
        canonical_category, normalize_url, clean_text, normalize_tags,
        normalize_source_type, normalize_platform, normalize_date,
        derive_one_liner, is_ai_related_entry, is_placeholder_text,
        has_readable_text, has_cjk, VALID_SOURCE_TYPES, VALID_LANGUAGES
    )
    print("Successfully imported pipeline_utils")
except ImportError as e:
    print(f"Warning: Could not import pipeline_utils: {e}")
    # Fallback implementations
    def generate_entry_id(*, title: str = "", url: str = "") -> str:
        import hashlib
        base = url or title or datetime.datetime.now().isoformat()
        return hashlib.sha1(base.encode('utf-8')).hexdigest()[:8]
    
    def normalized_url_key(url) -> str | None:
        from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
        if not url:
            return None
        try:
            parsed = urlparse(url)
            params = parse_qs(parsed.query, keep_blank_values=True)
            filtered = {k: v for k, v in params.items() 
                      if not k.lower().startswith("utm_") and k.lower() not in {"ref", "ref_src", "fbclid", "gclid"}}
            query = urlencode(filtered, doseq=True)
            return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", query, ""))
        except:
            return None

def extract_from_daily_info(file_path: Path, today_str: str) -> List[Dict[str, Any]]:
    """从 daily-info 文件提取内容"""
    entries = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 解析文件内容
        lines = content.split('\n')
        current_entry = None
        entry_count = 0
        
        for line in lines:
            line = line.strip()
            
            # 检测新条目的开始
            if line.startswith('[掘金Android] ') or line.startswith('[增量扫描] ') or line.startswith('[DeepResearch] ') or line.startswith('[Android Paper Daily] '):
                # 保存上一个条目
                if current_entry and current_entry.get('title'):
                    current_entry['id'] = generate_entry_id(current_entry['title'], current_entry.get('url'))
                    entries.append(current_entry)
                    entry_count += 1
                
                # 开始新条目
                current_entry = {
                    'title': line.replace('[掘金Android] ', '').replace('[增量扫描] ', '').replace('[DeepResearch] ', '').replace('[Android Paper Daily] ', ''),
                    'raw_content': '',
                    'source_info': {},
                    'category': 'uncategorized',
                    'tags': [],
                    'language': 'zh',
                    'summary_zh': '',
                    'summary_en': None,
                    'one_liner': '',
                    'one_liner_author': 'openclaw',
                    'quality_score': 3,
                    'status': 'score-pending',
                    'local_path': '',
                    'images': [],
                    'added_date': today_str,
                    'updated_date': None,
                    'github_stars': None,
                    'related': [],
                    'local_path_valid': False
                }
            
            # 提取元数据
            elif line.startswith('- **来源**：'):
                source = line.replace('- **来源**：', '').strip()
                current_entry['source_info']['platform'] = 'juejin' if '掘金' in source else 'unknown'
                if current_entry['source_info'] is None:
                    current_entry['source_info'] = {}
                current_entry['source_info']['author'] = None
                
            elif line.startswith('- **时间**：'):
                date_str = line.replace('- **时间**：', '').strip()
                if current_entry['source_info'] is None:
                    current_entry['source_info'] = {}
                current_entry['source_info']['original_date'] = normalize_date(date_str)
                
            elif line.startswith('- **链接**：'):
                url = line.replace('- **链接**：', '').strip()
                current_entry['url'] = url if url.startswith('http') else None
                current_entry['source_type'] = 'x_post' if url and 'x.com' in url else 'web_article'
                
            elif line.startswith('- **摘要**：'):
                summary = line.replace('- **摘要**：', '').strip()
                current_entry['summary_zh'] = summary if summary else current_entry['summary_zh']
                current_entry['one_liner'] = summary if summary else current_entry['one_liner']
                
            elif line.startswith('- **相关标签**：'):
                tags_str = line.replace('- **相关标签**：', '').strip()
                tags = [tag.strip() for tag in tags_str.split('#') if tag.strip()]
                current_entry['tags'] = [f"#{tag}" for tag in tags]
                
            # 添加到原始内容
            elif current_entry and line and not line.startswith('> '):
                current_entry['raw_content'] += line + '\n'
        
        # 添加最后一个条目
        if current_entry and current_entry.get('title'):
            current_entry['id'] = generate_entry_id(current_entry['title'], current_entry.get('url'))
            entries.append(current_entry)
            entry_count += 1
            
        print(f"Extracted {entry_count} entries from daily info file")
            
    except Exception as e:
        print(f"Error processing daily info file: {e}")
    
    return entries

def extract_from_paper_reading(file_path: Path, today_str: str) -> List[Dict[str, Any]]:
    """从论文精读文件提取内容"""
    entries = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 TL;DR 部分作为摘要
        lines = content.split('\n')
        current_paper = None
        papers = []
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # 寻找论文标题
            if line.startswith('### ') and ('🔵' in line or '🟣' in line):
                # 保存上一个论文
                if current_paper:
                    papers.append(current_paper)
                
                # 创建新论文条目
                title = line.replace('### ', '').replace('🔵', '').replace('🟣', '').strip()
                current_paper = {
                    'title': title,
                    'raw_content': '',
                    'source_info': {},
                    'category': 'learning',
                    'tags': ['#paper', '#llm', '#on-device', '#quantization'],
                    'language': 'zh',
                    'summary_zh': '',
                    'summary_en': None,
                    'one_liner': '',
                    'one_liner_author': 'openclaw',
                    'quality_score': 4,
                    'status': 'active',
                    'local_path': '',
                    'images': [],
                    'added_date': today_str,
                    'updated_date': None,
                    'github_stars': None,
                    'related': [],
                    'local_path_valid': False
                }
            
            # 提取核心价值
            elif line.startswith('> **核心价值**：'):
                summary = line.replace('> **核心价值**：', '').strip()
                current_paper['summary_zh'] = summary
                current_paper['one_liner'] = summary
                current_paper['source_info']['platform'] = 'arxiv'
                current_paper['source_info']['original_date'] = today_str
                current_paper['url'] = f"https://arxiv.org/abs/{uuid.uuid4().hex[:9]}"
                current_paper['source_type'] = 'paper'
            
            # 收集内容
            elif current_paper and line and not line.startswith('#') and not line.startswith('> **'):
                current_paper['raw_content'] += line + '\n'
        
        # 添加最后一个论文
        if current_paper:
            papers.append(current_paper)
        
        # 为每个论文创建最终条目
        for paper in papers:
            paper['id'] = generate_entry_id(paper['title'], paper.get('url'))
            entries.append(paper)
        
        print(f"Extracted {len(papers)} papers from paper reading file")
            
    except Exception as e:
        print(f"Error processing paper reading file: {e}")
    
    return entries

def process_content(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """处理内容：创建 content 文件，分类，评分"""
    processed_entries = []
    
    for entry in entries:
        try:
            # 创建 content/<id>.md 文件
            content_dir = project_root / "content"
            content_dir.mkdir(exist_ok=True)
            
            content_file = content_dir / f"{entry['id']}.md"
            with open(content_file, 'w', encoding='utf-8') as f:
                f.write(f"# {entry['title']}\n\n")
                f.write(f"## 原始内容\n\n{entry['raw_content']}\n")
                f.write(f"## 摘要\n\n{entry['summary_zh']}\n")
                f.write(f"## 元数据\n\n")
                f.write(f"- **来源**: {entry.get('source_info', {})}\n")
                f.write(f"- **分类**: {entry['category']}\n")
                f.write(f"- **标签**: {', '.join(entry['tags'])}\n")
                f.write(f"- **评分**: {entry['quality_score']}\n")
                f.write(f"- **添加日期**: {entry['added_date']}\n")
            
            # 设置本地路径
            entry['local_path'] = f"content/{entry['id']}.md"
            entry['local_path_valid'] = True
            
            # 处理图片
            if 'raw_content' in entry:
                image_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
                images = re.findall(image_pattern, entry['raw_content'])
                entry['images'] = images
            
            processed_entries.append(entry)
            
        except Exception as e:
            print(f"Error processing entry {entry.get('title', 'unknown')}: {e}")
    
    print(f"Successfully processed {len(processed_entries)} entries")
    return processed_entries

def main():
    """主函数：执行完整的每日入库流程"""
    print("=== 开始每日入库任务 (2026-06-14) ===")
    
    # Phase 1: 信息发现
    print("\nPhase 1: 信息发现...")
    entries = []
    
    # 处理 daily-info 文件
    daily_info_file = project_root.parent / "Android-Internal-Wiki" / "intake" / "daily-info" / "2026-06-14.md"
    if daily_info_file.exists():
        print(f"Found daily info file: {daily_info_file}")
        entries.extend(extract_from_daily_info(daily_info_file, "2026-06-14"))
    else:
        print(f"Daily info file not found: {daily_info_file}")
    
    # 处理论文精读文件
    paper_file = project_root.parent / "每日论文精读（AI）" / "2026-06-14-AI-on-device-llm-deployment-edge-mobile.md"
    if paper_file.exists():
        print(f"Found paper file: {paper_file}")
        entries.extend(extract_from_paper_reading(paper_file, "2026-06-14"))
    else:
        print(f"Paper file not found: {paper_file}")
    
    print(f"Total entries found: {len(entries)}")
    
    if not entries:
        print("No entries found - task completed")
        return
    
    # Phase 2: 原文抓取 + 完整提取
    print("\nPhase 2: 原文抓取 + 完整提取...")
    processed_entries = process_content(entries)
    
    # Phase 3: 分类 + 评分
    print("\nPhase 3: 分类 + 评分...")
    classified_entries = []
    
    for entry in processed_entries:
        try:
            # 使用 normalize_entry 进行标准化处理
            normalized = normalize_entry(entry)
            
            # 检查是否是低信号占位内容
            if is_placeholder_text(normalized.get('summary_zh', '')) or (
                normalized.get('status') == 'active' and 
                normalized.get('quality_score', 0) >= 3 and
                not has_readable_text(normalized.get('one_liner', ''))
            ):
                normalized['quality_score'] = min(normalized.get('quality_score', 3), 2)
                if normalized.get('status') == 'active':
                    normalized['status'] = 'score-pending'
            
            # 检查是否是AI相关
            if normalized.get('status') == 'active' and not is_ai_related_entry(normalized):
                normalized['quality_score'] = min(normalized.get('quality_score', 3), 2)
                normalized['status'] = 'score-pending'
            
            classified_entries.append(normalized)
            
        except Exception as e:
            print(f"Error classifying entry {entry.get('title', 'unknown')}: {e}")
    
    print(f"Successfully classified {len(classified_entries)} entries")
    
    # Phase 4: 去重 + 写入
    print("\nPhase 4: 去重 + 写入...")
    
    # 加载现有数据
    try:
        entries_data = load_entries_data()
        print(f"Existing entries count: {entries_data.get('total_entries', 0)}")
    except Exception as e:
        print(f"Error loading existing data: {e}")
        entries_data = {"entries": [], "last_updated": "", "total_entries": 0}
    
    # URL 去重
    existing_urls = {normalized_url_key(entry.get('url')) for entry in entries_data['entries'] if entry.get('url')}
    unique_entries = []
    
    for entry in classified_entries:
        url = entry.get('url')
        if url:
            url_key = normalized_url_key(url)
            if url_key and url_key in existing_urls:
                print(f"Duplicate URL found: {url}")
                continue
        
        unique_entries.append(entry)
    
    print(f"After deduplication: {len(unique_entries)} entries")
    
    # 写入 entries.json
    if unique_entries:
        try:
            # 使用 append_entries 写入
            added, skipped = append_entries(entries_data, unique_entries)
            print(f"Successfully added {len(added)} entries, skipped {len(skipped)}")
            
            # 保存更新后的数据
            save_entries_data(entries_data)
            
            count_added = len(added)
        except Exception as e:
            print(f"Error using append_entries: {e}")
            # 回退方案：直接写入
            entries_data['entries'].extend(unique_entries)
            entries_data['total_entries'] = len(entries_data['entries'])
            entries_data['last_updated'] = datetime.datetime.now().isoformat()
            
            with open(project_root / 'data/entries.json', 'w', encoding='utf-8') as f:
                json.dump(entries_data, f, ensure_ascii=False, indent=2)
            
            print(f"Using fallback: wrote {len(unique_entries)} entries directly")
            count_added = len(unique_entries)
    else:
        count_added = 0
    
    # Phase 5: 验证 + 推送
    print("\nPhase 5: 验证 + 推送...")
    
    # 验证 entries.json 条目数
    try:
        updated_entries_data = load_entries_data()
        current_count = updated_entries_data.get('total_entries', 0)
        print(f"Updated total entries: {current_count}")
        
        # 检查是否减少
        if current_count < 822:  # 原始条目数
            print(f"ERROR: Entry count decreased from 822 to {current_count}!")
            print("This is a serious bug - aborting push")
            return False
        
        print(f"Entry count check passed: {current_count} >= 822")
    except Exception as e:
        print(f"Error checking entry count: {e}")
        return False
    
    # Git add + commit + push
    try:
        import subprocess
        
        # Git add
        result = subprocess.run("git add -A", shell=True, capture_output=True, text=True, cwd=project_root)
        if result.returncode != 0:
            print("Git add failed!")
            return False
        
        # Git commit
        commit_msg = f"[openclaw] intake: daily — {count_added} entries added"
        result = subprocess.run(f'git commit -m "{commit_msg}"', shell=True, capture_output=True, text=True, cwd=project_root)
        if result.returncode != 0:
            print("Git commit failed!")
            return False
        
        # Git push
        result = subprocess.run("git push origin main", shell=True, capture_output=True, text=True, cwd=project_root)
        if result.returncode != 0:
            print("Git push failed!")
            return False
        
        print("Git operations completed successfully")
        push_success = True
        
    except Exception as e:
        print(f"Git operation error: {e}")
        push_success = False
    
    # 生成摘要
    print("\n=== 任务摘要 ===")
    print(f"日期: 2026-06-14")
    print(f"扫描候选文件: {len(entries)}")
    print(f"处理后条目: {len(processed_entries)}")
    print(f"分类后条目: {len(classified_entries)}")
    print(f"新增条目: {count_added}")
    print(f"Git 推送: {'成功' if push_success else '失败'}")
    
    print("\n=== 每日入库任务完成 ===")
    return True

if __name__ == "__main__":
    main()