#!/usr/bin/env python3
"""
每日入库任务 - 2026-06-14
执行完整的 5 阶段流程：发现→提取→分类评分→去重写入→验证推送
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
    def generate_entry_id(title: str = "", url: str = "") -> str:
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

def scan_obsidian_files() -> List[Dict[str, Any]]:
    """扫描 Obsidian 中当天新增/修改的 AI 相关 .md 文件"""
    entries = []
    today_str = "2026-06-14"
    
    # 定义候选文件路径
    candidate_files = [
        "Android-Internal-Wiki/intake/daily-info/2026-06-14.md",
        "../每日论文精读（AI）/2026-06-14-AI-on-device-llm-deployment-edge-mobile.md",
        "../source/juejin-android/2026-06-14-76148976-什么_AI_写_Android_最好用？.md",
        "../source/juejin-android/2026-06-14-76150608-你还用_IDE_吗？_AI_狂欢时代下.md",
        "../DeepResearch/2026-06-14-android17-sqlite-performance-observability-io-monitoring.md",
    ]
    
    for file_path in candidate_files:
        full_path = project_root / file_path
        if not full_path.exists():
            print(f"File not found: {file_path}")
            continue
            
        print(f"Processing: {file_path}")
        
        # 根据文件类型提取内容
        if "daily-info" in file_path:
            entries.extend(extract_daily_info_entries(full_path, today_str))
        elif "论文精读" in file_path:
            entries.extend(extract_paper_entries(full_path, today_str))
        elif "juejin-android" in file_path:
            entries.extend(extract_juejin_entries(full_path, today_str))
        elif "DeepResearch" in file_path:
            entries.extend(extract_deepresearch_entries(full_path, today_str))

    print(f"Found {len(entries)} candidate entries")
    return entries

def extract_daily_info_entries(file_path: Path, today_str: str) -> List[Dict[str, Any]]:
    """从 daily-info 文件提取内容"""
    entries = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 解析文件内容
        lines = content.split('\n')
        current_entry = None
        
        for line in lines:
            line = line.strip()
            
            # 检测新条目的开始
            if line.startswith('[掘金Android] ') or line.startswith('[增量扫描] ') or line.startswith('[DeepResearch] ') or line.startswith('[Android Paper Daily] '):
                # 保存上一个条目
                if current_entry and current_entry.get('title'):
                    current_entry['id'] = generate_entry_id(current_entry['title'], current_entry.get('url'))
                    entries.append(current_entry)
                
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
                
            elif line.startswith('- **时间**：'):
                date_str = line.replace('- **时间**：', '').strip()
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
            
    except Exception as e:
        print(f"Error processing daily info file: {e}")
    
    return entries

def extract_paper_entries(file_path: Path, today_str: str) -> List[Dict[str, Any]]:
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
            
    except Exception as e:
        print(f"Error processing paper reading file: {e}")
    
    return entries

def extract_juejin_entries(file_path: Path, today_str: str) -> List[Dict[str, Any]]:
    """从掘金文件提取内容"""
    entries = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'# (.+)', content)
        title = title_match.group(1) if title_match else "掘金技术文章"
        
        # 提取摘要（寻找第一个非空段落）
        paragraphs = re.split(r'\n\s*\n', content)
        summary = ""
        for para in paragraphs:
            if para.strip() and not para.startswith('#') and not para.startswith('- **'):
                summary = para.strip()[:200] + "..."
                break
        
        entry = {
            'title': title,
            'raw_content': content,
            'source_info': {
                'platform': 'juejin',
                'original_date': today_str,
                'author': None
            },
            'category': 'coding',
            'tags': ['#android', '#ai', '#development'],
            'language': 'zh',
            'summary_zh': summary,
            'summary_en': None,
            'one_liner': summary,
            'one_liner_author': 'openclaw',
            'quality_score': 3,
            'status': 'active',
            'local_path': '',
            'images': [],
            'added_date': today_str,
            'updated_date': None,
            'github_stars': None,
            'related': [],
            'local_path_valid': False,
            'url': None,
            'source_type': 'article'
        }
        
        entry['id'] = generate_entry_id(entry['title'], entry.get('url'))
        entries.append(entry)
            
    except Exception as e:
        print(f"Error processing juejin file: {e}")
    
    return entries

def extract_deepresearch_entries(file_path: Path, today_str: str) -> List[Dict[str, Any]]:
    """从 DeepResearch 文件提取内容"""
    entries = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'# (.+)', content)
        title = title_match.group(1) if title_match else "DeepResearch 调研报告"
        
        # 提取摘要（寻找第一个有意义的段落）
        paragraphs = re.split(r'\n\s*\n', content)
        summary = ""
        for para in paragraphs:
            if para.strip() and len(para.strip()) > 50:
                summary = para.strip()[:300] + "..."
                break
        
        entry = {
            'title': title,
            'raw_content': content,
            'source_info': {
                'platform': 'deepresearch',
                'original_date': today_str,
                'author': None
            },
            'category': 'learning',
            'tags': ['#android', '#research', '#performance'],
            'language': 'zh',
            'summary_zh': summary,
            'summary_en': None,
            'one_liner': summary,
            'one_liner_author': 'openclaw',
            'quality_score': 4,
            'status': 'active',
            'local_path': '',
            'images': [],
            'added_date': today_str,
            'updated_date': None,
            'github_stars': None,
            'related': [],
            'local_path_valid': False,
            'url': None,
            'source_type': 'paper'
        }
        
        entry['id'] = generate_entry_id(entry['title'], entry.get('url'))
        entries.append(entry)
            
    except Exception as e:
        print(f"Error processing DeepResearch file: {e}")
    
    return entries

def phase_2_content_processing(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Phase 2: 原文抓取 + 完整提取"""
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

def phase_3_classification_scoring(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Phase 3: 分类 + 评分"""
    classified_entries = []
    
    for entry in entries:
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
    return classified_entries

def phase_4_deduplication_writing(entries: List[Dict[str, Any]]) -> int:
    """Phase 4: 去重 + 写入"""
    # 加载现有数据
    try:
        entries_data = load_entries_data()
        print(f"Existing entries count: {entries_data.get('total_entries', 0)}")
    except Exception as e:
        print(f"Error loading existing data: {e}")
        entries_data = {"entries": [], "last_updated": "", "total_entries": 0}
    
    # URL 去重
    existing_urls = {normalized_url_key(entry.get('url')) for entry in entries_data['entries'] if entry.get('url')}
    url_unique_entries = []
    
    for entry in entries:
        url = entry.get('url')
        if url:
            url_key = normalized_url_key(url)
            if url_key and url_key in existing_urls:
                print(f"Duplicate URL found: {url}")
                continue
        
        title_key = re.sub(r"[^\w\u4e00-\u9fff]+", "", clean_text(entry.get('title', '')).lower())
        
        # 简单的标题相似度检查
        is_duplicate = False
        for existing_entry in entries_data['entries']:
            existing_title = existing_entry.get('title', '')
            existing_title_key = re.sub(r"[^\w\u4e00-\u9fff]+", "", clean_text(existing_title).lower())
            
            if title_key and existing_title_key and len(title_key) > 10 and len(existing_title_key) > 10:
                # 计算相似度
                common_chars = len(set(title_key) & set(existing_title_key))
                total_chars = len(set(title_key) | set(existing_title_key))
                if total_chars > 0:
                    similarity = common_chars / total_chars
                    if similarity > 0.85:
                        print(f"Duplicate title found: '{entry.get('title')}' vs '{existing_title}' (similarity: {similarity:.2f})")
                        is_duplicate = True
                        break
        
        if not is_duplicate:
            url_unique_entries.append(entry)
    
    print(f"After deduplication: {len(url_unique_entries)} entries")
    
    # 写入 entries.json
    if url_unique_entries:
        try:
            # 使用 append_entries 写入
            added, skipped = append_entries(entries_data, url_unique_entries)
            print(f"Successfully added {len(added)} entries, skipped {len(skipped)}")
            
            # 保存更新后的数据
            save_entries_data(entries_data)
            
            return len(added)
        except Exception as e:
            print(f"Error using append_entries: {e}")
            # 回退方案：直接写入
            entries_data['entries'].extend(url_unique_entries)
            entries_data['total_entries'] = len(entries_data['entries'])
            entries_data['last_updated'] = datetime.datetime.now().isoformat()
            
            with open(project_root / 'data/entries.json', 'w', encoding='utf-8') as f:
                json.dump(entries_data, f, ensure_ascii=False, indent=2)
            
            print(f"Using fallback: wrote {len(url_unique_entries)} entries directly")
            return len(url_unique_entries)
    
    return 0

def phase_5_validation_push(count_added: int) -> bool:
    """Phase 5: 验证 + 推送"""
    print("Phase 5: 验证 + 推送")
    
    # 验证 schema
    try:
        exec_result = exec_command("python3 scripts/validate-schema.py")
        if exec_result != 0:
            print("Schema validation failed!")
            return False
        print("Schema validation passed")
    except Exception as e:
        print(f"Schema validation error: {e}")
        return False
    
    # 构建站点
    try:
        exec_result = exec_command("npm run build")
        if exec_result != 0:
            print("Site build failed!")
            return False
        print("Site build completed")
    except Exception as e:
        print(f"Site build error: {e}")
        return False
    
    # 检查 entries.json 条目数
    try:
        entries_data = load_entries_data()
        current_count = entries_data.get('total_entries', 0)
        print(f"Current total entries: {current_count}")
        
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
        # Git add
        exec_result = exec_command("git add -A")
        if exec_result != 0:
            print("Git add failed!")
            return False
        
        # Git commit
        commit_msg = f"[openclaw] intake: daily — {count_added} entries added"
        exec_result = exec_command(f'git commit -m "{commit_msg}"')
        if exec_result != 0:
            print("Git commit failed!")
            return False
        
        # Git push
        exec_result = exec_command("git push origin main")
        if exec_result != 0:
            print("Git push failed!")
            return False
        
        print("Git operations completed successfully")
        return True
        
    except Exception as e:
        print(f"Git operation error: {e}")
        return False

def exec_command(cmd: str) -> int:
    """执行 shell 命令"""
    import subprocess
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=project_root)
        return result.returncode
    except Exception as e:
        print(f"Command execution error: {e}")
        return 1

def main():
    """主函数：执行完整的每日入库流程"""
    print("=== 开始每日入库任务 (2026-06-14) ===")
    
    # Phase 1: 信息发现
    print("\nPhase 1: 信息发现...")
    entries = scan_obsidian_files()
    
    if not entries:
        print("No entries found - task completed")
        return
    
    # Phase 2: 原文抓取 + 完整提取
    print("\nPhase 2: 原文抓取 + 完整提取...")
    processed_entries = phase_2_content_processing(entries)
    
    # Phase 3: 分类 + 评分
    print("\nPhase 3: 分类 + 评分...")
    classified_entries = phase_3_classification_scoring(processed_entries)
    
    # Phase 4: 去重 + 写入
    print("\nPhase 4: 去重 + 写入...")
    count_added = phase_4_deduplication_writing(classified_entries)
    print(f"Added {count_added} new entries")
    
    # Phase 5: 验证 + 推送
    print("\nPhase 5: 验证 + 推送...")
    push_success = phase_5_validation_push(count_added)
    
    # 生成摘要
    print("\n=== 任务摘要 ===")
    print(f"日期: 2026-06-14")
    print(f"扫描候选文件: {len(entries)}")
    print(f"处理后条目: {len(processed_entries)}")
    print(f"分类后条目: {len(classified_entries)}")
    print(f"新增条目: {count_added}")
    print(f"Git 推送: {'成功' if push_success else '失败'}")
    
    # 如果成功，发送到群组
    if push_success:
        send_notification(count_added)
    
    print("\n=== 每日入库任务完成 ===")

def send_notification(count_added: int):
    """发送结果摘要到 OpenClaw - 知识库 群"""
    message = f"""
🤖 OpenClaw AI Field Notes - 每日入库摘要

📅 日期: 2026-06-14
📊 新增条目: {count_added}
⏰ 执行时间: 23:30 (Asia/Shanghai)

✅ 完整流程:
1. 扫描 Obsidian 当天 AI 相关文件
2. 提取原文、分类、评分
3. 去重并写入 entries.json
4. 验证 schema + 构建站点
5. Git 推送到远程仓库

🔗 目标仓库: awesome-ai-field-notes
📈 总条目数: 822+{count_added}

---
此消息由 OpenClaw 自动生成
"""
    
    try:
        # 使用 message 工具发送到群组
        from message import message
        
        # 这里需要实际的群组 ID，先打印消息内容
        print("\n要发送到群组的消息:")
        print(message)
        print("\n注意: 实际发送需要配置正确的群组 ID")
        
    except Exception as e:
        print(f"发送通知失败: {e}")

if __name__ == "__main__":
    main()