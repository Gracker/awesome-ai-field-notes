#!/usr/bin/env python3
"""
Daily Intake Script for awesome-ai-field-notes
执行时间：每日 20:00
处理过去24小时内新增/修改的AI相关.md文件，提取、分类、评分并写入entries.json
"""

import json
import re
import sys
from datetime import datetime, date, timedelta
from pathlib import Path
import hashlib

# Add openclaw/scripts directory to path to import pipeline_utils
openclaw_scripts_dir = Path(__file__).parent / "openclaw" / "scripts"
sys.path.insert(0, str(openclaw_scripts_dir))
try:
    import pipeline_utils
except ImportError:
    print(f"Error: Could not import pipeline_utils from {openclaw_scripts_dir}")
    sys.exit(1)

def extract_content_from_md(file_path: Path) -> dict:
    """从markdown文件中提取内容，生成entry字典"""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    # 提取标题
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else file_path.stem

    # 提取作者
    author_match = re.search(r'-\s*\*{0,2}作者\*{0,2}\s*[:：]\s*(.+)', content)
    author = author_match.group(1).strip() if author_match else None

    # 提取URL
    url_match = re.search(r'-\s*\*{0,2}URL\*{0,2}\s*[:：]\s*(https?://[^\s]+)', content)
    url = url_match.group(1).strip() if url_match else None

    # 提取发表日期
    date_match = re.search(r'-\s*\*{0,2}(发表日期|original_date)\*{0,2}\s*[:：]\s*(.+)', content)
    original_date = date_match.group(1).strip() if date_match else None

    # 生成摘要（从内容中提取）
    lines = content.split('\n')
    summary_lines = []
    in_abstract = False
    
    for line in lines:
        line = line.strip()
        if line.startswith('## 摘要') or line.startswith('## Abstract'):
            in_abstract = True
            continue
        elif line.startswith('##') and in_abstract:
            break
        elif in_abstract and line:
            summary_lines.append(line)
    
    summary_zh = '\n'.join(summary_lines[:10]).strip() if summary_lines else content[:300].strip()
    
    # 清理摘要
    summary_zh = pipeline_utils.clean_text(summary_zh, max_len=900)
    if len(summary_zh) < 50:
        summary_zh = pipeline_utils.clean_text(content[:500], max_len=900)

    # 提取图片
    images = []
    img_matches = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
    for img in img_matches[:5]:  # 最多5张图片
        normalized_img = pipeline_utils.normalize_url(img)
        if normalized_img:
            images.append(normalized_img)

    # 生成ID
    entry_id = hashlib.md5(f"{title}_{url or file_path.stem}".encode()).hexdigest()[:8]

    # 分类判断
    category = "uncategorized"
    content_lower = content.lower()
    
    # 根据关键词分类
    if any(keyword in content_lower for keyword in ['论文', 'paper', 'research', 'arxiv']):
        category = "learning"
    elif any(keyword in content_lower for keyword in ['mcp', 'agent', 'agents', '智能体', '自动化']):
        category = "agents"
    elif any(keyword in content_lower for keyword in ['模型', 'model', 'llm', 'gpt', 'claude', 'gemini']):
        category = "models"
    elif any(keyword in content_lower for keyword in ['编码', 'code', '开发', 'programming', 'developer']):
        category = "coding"
    elif any(keyword in content_lower for keyword in ['推理', 'inference', 'rag', 'eval', 'benchmark']):
        category = "infra"

    # 生成one-liner
    one_liner = pipeline_utils.derive_one_liner(title, summary_zh)

    # 判断来源类型
    source_type = "article"
    if url and 'arxiv.org' in url:
        source_type = "paper"
    elif url and 'github.com' in url:
        source_type = "github"
    elif url and ('twitter.com' in url or 'x.com' in url):
        source_type = "x_post"

    # 评分（基于内容质量和结构）
    quality_score = 3  # 默认中等质量
    if len(content) > 2000 and len(summary_zh) > 100:
        quality_score = 4
    if len(content) > 5000 and '##' in content and len(summary_zh) > 200:
        quality_score = 5
    elif len(content) < 500 or not summary_zh:
        quality_score = 2

    return {
        "id": entry_id,
        "title": title,
        "url": url,
        "source": {
            "platform": pipeline_utils.normalize_platform("manual", url=url),
            "author": author,
            "original_date": pipeline_utils.normalize_date(original_date, allow_partial=True)
        },
        "category": category,
        "tags": [],  # 可以后续添加
        "source_type": source_type,
        "language": "zh" if pipeline_utils.has_cjk(summary_zh) else "en",
        "summary_zh": summary_zh,
        "summary_en": None,  # 中文内容暂不生成英文摘要
        "one_liner": one_liner,
        "one_liner_author": "openclaw",
        "quality_score": quality_score,
        "status": "score-pending",  # 新条目默认待评分
        "local_path": f"content/{file_path.name}",
        "images": images,
        "added_date": date.today().isoformat(),
        "updated_date": date.today().isoformat(),
        "github_stars": None,
        "related": []
    }

def find_recent_ai_files() -> list[Path]:
    """查找过去24小时内新增/修改的AI相关.md文件"""
    content_dir = Path(__file__).parent / "content"
    recent_files = []
    
    # 查找过去24小时内修改的文件
    cutoff_time = datetime.now() - timedelta(hours=24)
    
    for md_file in content_dir.glob("*.md"):
        try:
            stat = md_file.stat()
            if datetime.fromtimestamp(stat.st_mtime) > cutoff_time:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                # 简单检查是否为AI相关内容
                if any(keyword in content.lower() for keyword in pipeline_utils.AI_KEYWORDS):
                    recent_files.append(md_file)
        except Exception as e:
            print(f"Error checking file {md_file}: {e}")
    
    return sorted(recent_files, key=lambda x: x.stat().st_mtime, reverse=True)

def main():
    print("=== Evening Intake Process Started ===")
    print(f"Run time: {datetime.now().isoformat()}")
    
    # 获取当前entries数据
    try:
        entries_data = pipeline_utils.load_entries_data()
        current_count = len(entries_data.get("entries", []))
        print(f"Current entries count: {current_count}")
    except Exception as e:
        print(f"Error loading existing entries: {e}")
        entries_data = {"entries": []}
        current_count = 0

    # 查找最近的AI相关文件
    recent_files = find_recent_ai_files()
    print(f"Found {len(recent_files)} recent AI-related files")
    
    if not recent_files:
        print("No recent AI files found, exiting...")
        return

    # 处理每个文件
    new_entries = []
    skipped_entries = []
    
    for i, file_path in enumerate(recent_files[:20]):  # 最多处理20个文件
        print(f"Processing {i+1}/{min(len(recent_files), 20)}: {file_path.name}")
        
        entry = extract_content_from_md(file_path)
        if entry:
            new_entries.append(entry)
            print(f"  ✓ Created entry: {entry['title'][:50]}...")
        else:
            print(f"  ✗ Failed to process: {file_path.name}")

    print(f"\nGenerated {len(new_entries)} new entries")
    
    if not new_entries:
        print("No valid entries generated, exiting...")
        return

    # 使用pipeline_utils添加条目
    added, skipped = pipeline_utils.append_entries(entries_data, new_entries)
    
    print(f"\nAddition results:")
    print(f"  Added: {len(added)}")
    print(f"  Skipped: {len(skipped)}")
    
    for entry, reason in skipped:
        print(f"    Skipped: {entry['title'][:30]}... ({reason})")

    # 保存数据
    try:
        pipeline_utils.save_entries_data(entries_data)
        print(f"\n✓ Saved entries.json with {len(entries_data['entries'])} total entries")
    except Exception as e:
        print(f"✗ Error saving entries.json: {e}")
        return

    # 验证
    try:
        subprocess.run(["python3", "scripts/validate-schema.py"], check=True)
        print("✓ Schema validation passed")
    except subprocess.CalledProcessError as e:
        print(f"✗ Schema validation failed: {e}")
        return

    # 构建网站
    try:
        subprocess.run(["npm", "run", "build"], check=True)
        print("✓ Site build completed")
    except subprocess.CalledProcessError as e:
        print(f"✗ Site build failed: {e}")
        return

    # Git操作
    try:
        # 检查条目数是否减少
        new_count = len(entries_data['entries'])
        if new_count < current_count:
            print(f"✗ ERROR: Entry count decreased from {current_count} to {new_count}")
            print("This indicates data corruption. Aborting push.")
            return
        
        print(f"Entry count check passed: {current_count} → {new_count}")
        
        # Git add
        subprocess.run(["git", "add", "-A"], check=True)
        print("✓ Git add completed")
        
        # Git commit
        commit_msg = f"[openclaw] intake: evening — {len(added)} entries added"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"✓ Git commit: {commit_msg}")
        
        # Git push
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✓ Git push completed")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Git operation failed: {e}")
        return

    # 生成摘要
    summary = f"""
📊 Evening Intake Summary - {date.today().isoformat()}

📈 Processed {len(recent_files)} recent AI files
✅ Added {len(added)} new entries
❌ Skipped {len(skipped)} duplicates/invalid
📊 Total entries: {len(entries_data['entries'])}

Top categories:
{', '.join(set([e['category'] for e in added]))}
"""
    
    print("\n" + summary)
    
    # 发送到群组（如果配置了消息发送）
    try:
        # 这里可以添加发送到OpenClaw知识库群组的逻辑
        # message.send(action="send", target="chat_id", message=summary)
        print("Summary prepared for group delivery")
    except Exception as e:
        print(f"Note: Could not send summary to group: {e}")

    print("=== Evening Intake Process Completed Successfully ===")

if __name__ == "__main__":
    import subprocess
    main()