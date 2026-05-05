#!/usr/bin/env python3
"""Morning intake — 2026-05-04"""

import json, os, datetime, re, random, string
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENTRIES_FILE = PROJECT_ROOT / "data" / "entries.json"
CONTENT_DIR = PROJECT_ROOT / "content"

with open(ENTRIES_FILE, encoding='utf-8') as f:
    entries_data = json.load(f)

existing_urls = {e.get('url', '').rstrip('/') for e in entries_data['entries'] if e.get('url')}

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def extract_images(content):
    return re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

def make_entry(id, title, url, platform, author, orig_date, category, tags,
               source_type, language, summary_zh, summary_en, one_liner, quality,
               local_path):
    content_path = os.path.join(CONTENT_DIR, f"{id}.md")
    if os.path.exists(content_path):
        with open(content_path, encoding='utf-8') as f:
            content = f.read()
        images = extract_images(content)
    else:
        images = []
    today = datetime.date.today().isoformat()
    return {
        "id": id,
        "title": title,
        "url": url,
        "source": {
            "platform": platform,
            "author": author,
            "original_date": orig_date
        },
        "category": category,
        "tags": tags,
        "source_type": source_type,
        "language": language,
        "summary_zh": summary_zh,
        "summary_en": summary_en,
        "one_liner": one_liner,
        "one_liner_author": "openclaw",
        "quality_score": quality,
        "status": "active",
        "local_path": local_path,
        "images": images[:5],
        "added_date": today,
        "updated_date": None,
        "github_stars": None,
        "related": []
    }

entries_to_add = []

# === 1. Codex最强实战课 ===
id1 = gen_id()
url1 = "https://x.com/Jason23818126/status/2050197836894257433"
if url1.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id1,
        title="Codex最强实战课：2小时玩转Codex App+GPT-5.5",
        url=url1,
        platform="x/twitter",
        author="Dr. Moyu 摸鱼局长",
        orig_date="2026-04-06",
        category="coding",
        tags=["codex", "gpt-5.5", "vibe-coding", "tutorial", "openai"],
        source_type="x_post",
        language="zh",
        summary_zh="不到 2 小时带你彻底玩转 Codex App + GPT-5.5 组合：技能和插件怎么用、自动化工作流如何搭建、多任务并行实战，全程手把手演示。教程覆盖 Codex 的核心功能，包括技能系统、插件机制和多任务并行处理，适合想快速掌握高效 Vibe Coding 方法的开发者。",
        summary_en=None,
        one_liner="Codex + GPT-5.5 的实操入门教程，适合想快速上手 Vibe Coding 的开发者",
        quality=3,
        local_path="X 文章/2026-04-06/Jason23818126-Codex最强实战课.md"
    ))

# === 2. open claude design开源 ===
id2 = gen_id()
url2 = "https://x.com/tuturetom/status/2049066330934976610"
if url2.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id2,
        title="open claude design开源：超95%还原度的逆向工程",
        url=url2,
        platform="x/twitter",
        author="Tom Huang",
        orig_date="2026-04-06",
        category="coding",
        tags=["claude-design", "open-source", "design-system", "code-agent", "skills"],
        source_type="github",
        language="zh",
        summary_zh="open claude design 正式开源，浓缩和逆向所有 claude design 最先进的设计模板，还原度超过 95%。历时 72 小时，18700+ 行代码，30+ 设计 Skills，支持超过 71 套设计系统，兼容所有 code agent，包括 claude code、codex、openclaw 等。项目为 AI 编程代理提供了开箱即用的设计能力增强。",
        summary_en=None,
        one_liner="逆向 Claude Design 的开源设计系统，71+ 套模板可直接用于 code agent 场景",
        quality=4,
        local_path="X 文章/2026-04-06/tuturetom-open-claude-design开源.md"
    ))

# === 3. PPT Skills优化 ===
id3 = gen_id()
url3 = "https://x.com/op7418/status/2049094944405737512"
if url3.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id3,
        title="PPT Skills在Codex的优化：图片一键生成",
        url=url3,
        platform="x/twitter",
        author="歸藏(guizang.ai)",
        orig_date="2026-04-06",
        category="coding",
        tags=["codex", "ppt", "image-generation", "skills", "productivity"],
        source_type="x_post",
        language="zh",
        summary_zh="歸藏优化了 Codex 中的 PPT Skills，实现了图片一键生成功能。能够调用 Codex 里的 GPT-Image-2 去生成图片，并为此做了专门的设计，支持生成独特风格的图片，根据内容生成不同类型，包括营造氛围的人文纪实图片（类似胶片机拍摄效果）。",
        summary_en=None,
        one_liner="Codex PPT Skills 新增图片生成能力，用 GPT-Image-2 实现风格化配图",
        quality=3,
        local_path="X 文章/2026-04-06/op7418-PPT-Skills优化.md"
    ))

# === 4. replit slides设计技能模板 ===
id4 = gen_id()
url4 = "https://x.com/tuturetom/status/2049495165488808094"
if url4.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id4,
        title="replit slides设计技能模板：0限制完全本地设计Agent",
        url=url4,
        platform="x/twitter",
        author="Tom Huang",
        orig_date="2026-04-06",
        category="coding",
        tags=["replit", "slides", "design-agent", "skills", "open-source"],
        source_type="github",
        language="zh",
        summary_zh="开源了 replit slides 的全套设计 skills 模板，提供 8 套 replit 样式（helix / holm / vance / bevel / world-dark / world-mint / atlas / bluehouse），支持 0 限制、完全本地运行的设计 Agent。配合 open claude design 项目，为 AI 编程代理提供完整的幻灯片设计能力。",
        summary_en=None,
        one_liner="8 套 replit slides 设计模板开源，配合 code agent 可本地生成演示文稿",
        quality=3,
        local_path="X 文章/2026-04-06/tuturetom-replit-slides模板.md"
    ))

# === 5. Obsidian Reader更新 ===
id5 = gen_id()
url5 = "https://x.com/realCaigu/status/2048632050266320981"
if url5.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id5,
        title="Obsidian Reader更新：支持推特文章和长线程阅读",
        url=url5,
        platform="x/twitter",
        author="才谷 Saitani",
        orig_date="2026-04-06",
        category="learning",
        tags=["obsidian", "reader", "twitter", "web-clipper", "markdown"],
        source_type="product",
        language="zh",
        summary_zh="Obsidian Reader 终于支持了推特文章和长线程阅读。只要在浏览器装好 Obsidian Web Clipper 扩展，直接就能开启极致简约的阅读模式，同时支持一键转存 Markdown。推特的 API 和 url-to-markdown 运行出 bug、排版乱七八糟的时代结束了。后续 1.13 版本还有更多改进。",
        summary_en=None,
        one_liner="Obsidian Reader 支持 Twitter 文章和长线程阅读，一键转存 Markdown",
        quality=3,
        local_path="X 文章/2026-04-06/realCaigu-Obsidian-Reader更新.md"
    ))

# === 6. MCP-Flow 论文 ===
id6 = gen_id()
url6 = "https://arxiv.org/abs/2510.24284"
if url6.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id6,
        title="MCP-Flow: 自动构建大规模 MCP 工具数据集，让 0.6B 模型在工具调用上超越 GPT-4o",
        url=url6,
        platform="arxiv",
        author="TikTok & 上海交大联合研究",
        orig_date="2025-10",
        category="agents",
        tags=["mcp", "tool-calling", "fine-tuning", "dataset", "agent", "small-model"],
        source_type="paper",
        language="en",
        summary_zh="MCP-Flow 提出全自动 pipeline，从 6 个 MCP 市场自动抓取服务器配置，通过 Slot-Fill Revision + WizardLM Evolution 两阶段数据增强，产出 68733 对 instruction-function call（1166 服务器、11536 工具）。实验表明：GPT-4o 在 10 工具场景下 AST 仅 58.8%，100 工具时 Groq-8B AST 跌至 3%；而 MCP-Flow-Qwen3-0.6B 在同场景下 AST 达 81.2%，全面超越所有大模型。用 MCP-Flow 做 RAG 检索增强后，GPT-4o 在 GAIA 任务上成功率 +17%，步数减少 32%。",
        summary_en="MCP-Flow proposes a fully automated pipeline to scrape MCP server configs from 6 markets, augment data via Slot-Fill Revision + WizardLM Evolution, producing 68,733 instruction-function call pairs across 1,166 servers and 11,536 tools. Experiments show GPT-4o achieves only 58.8% AST accuracy with 10 tools; Groq-8B drops to 3% at 100 tools. MCP-Flow-Qwen3-0.6B achieves 81.2% AST, surpassing all large models. Using MCP-Flow for RAG retrieval augmentation, GPT-4o's GAIA task success rate improves by 17% with 32% fewer steps.",
        one_liner="0.6B 小模型微调后在 MCP 工具调用上全面超越 GPT-4o，证明小模型+数据工程才是正确方向",
        quality=4,
        local_path="论文/AI-2026-05-04-MCP-Flow/04-导读.md"
    ))

# === 7. OpenAI 入驻 AWS Bedrock ===
id7 = gen_id()
url7 = "https://openai.com/index/openai-on-aws/"
if url7.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id7,
        title="OpenAI 携 GPT-5.5 入驻 AWS Bedrock，结束微软七年独家云托管",
        url=url7,
        platform="blog",
        author="OpenAI",
        orig_date="2026-04-28",
        category="industry",
        tags=["openai", "aws", "bedrock", "gpt-5.5", "cloud", "multi-cloud"],
        source_type="article",
        language="en",
        summary_zh="OpenAI 与 AWS 联合宣布 GPT-5.5、Codex 编程代理及 Bedrock Managed Agents 进入有限预览。此前微软与 OpenAI 重签合作协议，取消 Azure 独家许可、废除 AGI 条款。GPT-5.4 已可调用，GPT-5.5 将在未来两周内上线。AWS 客户可通过现有 Bedrock API 调用 OpenAI 模型，复用统一的安全与治理框架。云计算 AI 模型市场从\"独家绑定\"转向\"多平台分发\"。",
        summary_en="OpenAI and AWS jointly announced that GPT-5.5, Codex programming agents, and Bedrock Managed Agents are entering limited preview. This follows Microsoft and OpenAI renegotiating their partnership to remove Azure exclusivity and AGI clauses. AWS customers can access OpenAI models through existing Bedrock APIs with unified security and governance frameworks.",
        one_liner="OpenAI 结束微软独家云托管，AWS 客户可直接调用 GPT-5.5，AI 模型市场进入多云时代",
        quality=4,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 8. 微软与 OpenAI 重签协议 ===
id8 = gen_id()
url8 = "https://www.reuters.com/legal/litigation/microsoft-end-exclusive-license-openais-technology-2026-04-27/"
if url8.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id8,
        title="微软与 OpenAI 重签合作协议：取消独家许可，废除 AGI 条款",
        url=url8,
        platform="news",
        author="Reuters",
        orig_date="2026-04-27",
        category="industry",
        tags=["microsoft", "openai", "partnership", "licensing", "agi"],
        source_type="article",
        language="en",
        summary_zh="微软与 OpenAI 宣布修改合作协议：IP 许可从独家改为非独家（延续至 2032 年）；删除 AGI 限制性条款；收入分成机制重设。此前 2025 年 10 月重组中 OpenAI 取消利润上限并给予微软 27% 股权。这次修改为 OpenAI 接入 AWS 等其他云平台扫清法律障碍，标志着 AI 行业最核心的商业关系发生结构性变化。",
        summary_en="Microsoft and OpenAI revised their partnership: IP licensing changed from exclusive to non-exclusive (through 2032), AGI restrictive clauses removed, and revenue sharing restructured. This clears the path for OpenAI to access other cloud platforms like AWS, marking a structural shift in the AI industry's most critical business relationship.",
        one_liner="微软放弃 OpenAI 独家许可，AI 行业最核心商业关系发生结构性变化",
        quality=4,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 9. DeepSeek V4 ===
id9 = gen_id()
url9 = "https://www.36kr.com/p/3780290045121801"
if url9.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id9,
        title="DeepSeek V4 发布：1.6 万亿参数、适配华为昇腾，API 价格再砍至首发价十分之一",
        url=url9,
        platform="news",
        author="36氪",
        orig_date="2026-04-30",
        category="models",
        tags=["deepseek", "v4", "huawei", "ascend", "open-source", "pricing"],
        source_type="article",
        language="zh",
        summary_zh="DeepSeek 发布 V4 系列，包含 1.6 万亿参数的 V4-Pro 和 2840 亿参数的 V4-Flash，均支持 100 万 token 上下文窗口，MIT 开源。V4 发布前未向英伟达和 AMD 提供早期访问，而是提前数周让华为进行软件适配优化，这是大模型行业首次。API 缓存命中价格降至首发价的十分之一，V4-Pro 已成为 DeepSeek 内部 Agentic Coding 模型。",
        summary_en=None,
        one_liner="国产大模型首次明确绑定国产算力生态发布，API 价格再创新低",
        quality=4,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 10. 三星芯片利润暴涨 ===
id10 = gen_id()
url10 = "https://www.reuters.com/sustainability/sustainable-finance-reporting/samsung-elec-q1-profit-surges-eightfold-record-2026-04-30/"
if url10.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id10,
        title="三星芯片利润暴涨近 50 倍至 53.7 万亿韩元，预警 2027 年供应缺口将进一步扩大",
        url=url10,
        platform="news",
        author="Reuters / Bloomberg",
        orig_date="2026-04-30",
        category="infra",
        tags=["samsung", "semiconductor", "hbm", "ai-infrastructure", "supply-chain"],
        source_type="article",
        language="en",
        summary_zh="三星电子 Q1 营业利润 57.2 万亿韩元（约 386 亿美元），创历史新高，半导体部门贡献 53.7 万亿韩元，利润率超 70%，超过英伟达和台积电同期。三星已签多年期约束性合同锁定产能，警告 2027 年存储芯片供需缺口将比 2026 年更大。AI 数据中心对 HBM 的需求是核心驱动力。",
        summary_en="Samsung Electronics Q1 operating profit reached a record 57.2 trillion KRW (~$38.6B), with the semiconductor division contributing 53.7 trillion KRW. Profit margins exceeded 70%, surpassing Nvidia and TSMC. Samsung has signed multi-year binding contracts and warned that the 2027 memory chip supply-demand gap will be larger than 2026, driven by AI data center demand for HBM.",
        one_liner="AI 对存储芯片的拉动已从预期变成财报数字，2027 年供应继续紧缺",
        quality=4,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 11. 华为昇腾 AI 芯片 ===
id11 = gen_id()
url11 = "https://www.heygotrade.com/en/news/huawei-targets-ai-chip-revenue-up-60-percent-2026-vs-nvidia/"
if url11.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id11,
        title="华为昇腾 AI 芯片 2026 年营收预计达 120 亿美元，同比增长 60%",
        url=url11,
        platform="news",
        author="FT / HeyGoTrade",
        orig_date="2026-04-28",
        category="infra",
        tags=["huawei", "ascend", "ai-chip", "semiconductor", "china"],
        source_type="article",
        language="en",
        summary_zh="华为预计 2026 年 AI 芯片营收约 120 亿美元，同比增长 60%。下一代昇腾 950PR 已进入量产，DeepSeek V4 发布后字节跳动、腾讯、阿里加速抢购。华为计划今年出货约 75 万颗 950PR。黄仁勋此前警告：如果 DeepSeek 新模型率先在华为芯片上全面适配，对美国在全球 AI 领域的战略地位将是灾难性打击。",
        summary_en="Huawei expects 2026 AI chip revenue of ~$12B, up 60% YoY. The next-gen Ascend 950PR has entered mass production with ByteDance, Tencent, and Alibaba accelerating purchases after DeepSeek V4's release. Huawei plans ~750K 950PR shipments this year.",
        one_liner="英伟达在中国高端 AI 市场的空白正在被华为快速填补，国产算力生态规模化拐点已至",
        quality=4,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 12. Ineffable Intelligence 种子轮 ===
id12 = gen_id()
url12 = "https://www.cnbc.com/2026/04/27/deepmind-ineffable-intelligence-record-seed-funding-nvidia-google.html"
if url12.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id12,
        title="前谷歌 DeepMind 研究员创办 Ineffable Intelligence，种子轮融 11 亿美元创纪录",
        url=url12,
        platform="news",
        author="CNBC",
        orig_date="2026-04-27",
        category="industry",
        tags=["ai-startup", "deepmind", "funding", "superintelligence", "nvidia"],
        source_type="article",
        language="en",
        summary_zh="前谷歌 DeepMind 顶级研究员为其初创公司 Ineffable Intelligence 完成 11 亿美元种子轮融资，创种子轮金额纪录。投资方包括英伟达和谷歌，目标是追求超级智能。Dealroom 数据显示 2026 年风投已向新成立的 AI 初创公司注入 188 亿美元，英伟达 2026 年已投资超过 36 家公司。",
        summary_en="Former Google DeepMind researcher raised $1.1B seed round for Ineffable Intelligence, a record seed funding. Investors include Nvidia and Google, targeting superintelligence. Dealroom data shows VCs have invested $18.8B in AI startups founded since 2025, with Nvidia investing in 36+ companies in 2026.",
        one_liner="种子轮 11 亿美元刷新纪录，顶级 AI 人才创业正在从大厂分流资本",
        quality=3,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 13. 大厂 AI 人才出走 ===
id13 = gen_id()
url13 = "https://www.cnbc.com/2026/04/28/meta-google-big-tech-staff-ai-labs-investors.html"
if url13.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id13,
        title="大厂 AI 人才持续出走创业：2026 年风投已投 188 亿美元给新 AI 公司",
        url=url13,
        platform="news",
        author="CNBC",
        orig_date="2026-04-28",
        category="industry",
        tags=["ai-talent", "startup", "venture-capital", "meta", "google", "openai"],
        source_type="article",
        language="en",
        summary_zh="Meta、谷歌、OpenAI 等大厂的顶级研究员持续离职创办 AI 初创公司。Dealroom 数据显示 2025 年初至今成立的 AI 初创公司已获得 188 亿美元风投资金。AI 行业的人才流动模式已从\"大厂之间跳槽\"升级为\"大厂出走创业\"，大厂已成为 AI 人才的\"培训基地\"。",
        summary_en="Top researchers from Meta, Google, and OpenAI continue leaving to found AI startups. Dealroom data shows AI startups founded since early 2025 have received $18.8B in VC funding. The talent flow pattern has evolved from inter-company moves to mass exodus for entrepreneurship.",
        one_liner="AI 人才流动从大厂间跳槽升级为出走创业，188 亿美元验证了这条路径",
        quality=3,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 14. Qwen3.6-Max-Preview ===
id14 = gen_id()
url14 = "https://github.com/QwenLM/Qwen3.6"
if url14.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id14,
        title="阿里发布 Qwen3.6-Max-Preview：六项 Agent/Coding 基准测试第一，但旗舰模型转向闭源",
        url=url14,
        platform="github",
        author="Alibaba / Qwen Team",
        orig_date="2026-04-27",
        category="models",
        tags=["qwen", "alibaba", "agent", "coding", "benchmark", "open-source", "closed-source"],
        source_type="article",
        language="zh",
        summary_zh="阿里发布 Qwen3.6-Max-Preview，在 SWE-Bench Pro、Terminal-Bench 2.0、SkillsBench、SciCode、QwenClawBench、QwenWebBench 六项 Agent 和编程基准测试中排名第一。输入价格 1.04 美元/百万 token，输出 6.24 美元/百万 token。但旗舰 Max 版本不再完全开源，阿里转向\"小模型开源、旗舰闭源\"的中间路线。",
        summary_en=None,
        one_liner="六项 Agent/Coding 基准第一，但阿里旗舰模型转向闭源，开源策略生变",
        quality=4,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 15. 欧盟 AI 法案 ===
id15 = gen_id()
url15 = "https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/"
if url15.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id15,
        title="欧盟 AI 法案修改谈判破裂：12 小时协商未果，八月合规期限悬而未决",
        url=url15,
        platform="news",
        author="Reuters / POLITICO",
        orig_date="2026-04-29",
        category="industry",
        tags=["eu", "ai-act", "regulation", "compliance", "policy"],
        source_type="article",
        language="en",
        summary_zh="欧盟成员国与欧洲议会经 12 小时谈判未能就 AI 法案修订达成一致。修订方案原计划推迟 2026 年 8 月的高风险系统合规期限、缩窄适用范围，并将 AI 义务与现有行业法规整合。主要分歧在于部分国家坚持已受行业安全法规约束的领域应豁免 AI 法案额外要求。5 月将是截止日期前的最后谈判窗口。",
        summary_en="EU member states and European Parliament failed to reach agreement on AI Act revisions after 12 hours of negotiations. The revision aimed to delay the August 2026 high-risk system compliance deadline and narrow scope. Key disagreement: some countries insist sectors already under industry safety regulations should be exempt from additional AI Act requirements. May is the last negotiation window.",
        one_liner="欧盟 AI 法案修订谈判破裂，8 月合规期限是否推迟悬而未决",
        quality=3,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 16. 神经符号 AI ===
id16 = gen_id()
url16 = "https://www.sciencedaily.com/releases/2026/04/260405003952.htm"
if url16.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id16,
        title="Tufts 大学研究：神经符号 AI 在机器人操控任务中能耗降低 100 倍，准确率反升",
        url=url16,
        platform="news",
        author="ScienceDaily",
        orig_date="2026-04-05",
        category="models",
        tags=["neuro-symbolic", "ai-research", "energy-efficiency", "robotics", "icra"],
        source_type="article",
        language="en",
        summary_zh="Tufts 大学 Matthias Scheutz 实验室论文（将在 ICRA 2026 维也纳会议展示）表明，神经符号 AI 方法在结构化长时序机器人操控任务中，训练能耗降低至纯端到端方法的百分之一，同时任务准确率更高。该方法将传统神经网络与符号推理结合，用逻辑规则分解任务步骤，为 AI 能耗瓶颈提供了替代路径。",
        summary_en="Tufts University research (to be presented at ICRA 2026 Vienna) shows neuro-symbolic AI achieves 100x lower training energy consumption than pure end-to-end methods in structured long-horizon robotic manipulation tasks, while maintaining higher accuracy. The approach combines neural networks with symbolic reasoning using logical rules to decompose task steps.",
        one_liner="神经符号 AI 训练能耗降至 1/100 且准确率更高，为 AI 能耗瓶颈提供替代路径",
        quality=3,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

# === 17. Centaur 认知模型 ===
id17 = gen_id()
url17 = "https://www.sciencedaily.com/releases/2026/04/260429102035.htm"
if url17.rstrip('/') not in existing_urls:
    entries_to_add.append(make_entry(
        id=id17,
        title="Centaur 认知模型遭质疑：号称模拟人类思维 160 项任务，实际\"知道答案但不懂问题\"",
        url=url17,
        platform="news",
        author="ScienceDaily",
        orig_date="2026-04-29",
        category="models",
        tags=["ai-research", "cognitive-science", "centaur", "criticism"],
        source_type="article",
        language="en",
        summary_zh="此前被报道为认知心理学突破的 AI 模型 Centaur，声称能在 160 项认知任务上模拟人类思维。但新研究发现其最大局限在于语言理解——能给出正确答案但无法识别问题背后的意图。数据拟合层面的表现不等于认知模拟能力，对\"AI 已接近人类认知能力\"的叙事提出了重要修正。",
        summary_en="The AI model Centaur, previously reported as a cognitive psychology breakthrough claiming to simulate human thinking across 160 tasks, has been challenged. New research finds its key limitation is language understanding — it can produce correct answers but cannot identify the intent behind questions. Surface-level data fitting does not equal cognitive simulation capability.",
        one_liner="Centaur 模型能答对题但不懂题意，对\"AI 模拟人类认知\"的断言提出重要修正",
        quality=3,
        local_path="OpenClaw定时任务/资讯简报（综合）/2026-05-03-资讯简报（综合）.md"
    ))

print(f"New entries to add: {len(entries_to_add)}")
for e in entries_to_add:
    print(f"  [{e['id']}] {e['title'][:60]}")

# Write content files
for e in entries_to_add:
    content_path = os.path.join(CONTENT_DIR, f"{e['id']}.md")
    if not os.path.exists(content_path):
        # Create a minimal content file from the entry data
        lines = [f"# {e['title']}\n"]
        lines.append(f"\n- **来源**：{e['source']['platform']}")
        if e['source']['author']:
            lines.append(f"- **作者**：{e['source']['author']}")
        lines.append(f"- **原文链接**：{e['url']}")
        if e['source']['original_date']:
            lines.append(f"- **日期**：{e['source']['original_date']}")
        lines.append(f"\n---\n")
        lines.append(e['summary_zh'])
        if e.get('summary_en'):
            lines.append(f"\n## English Summary\n\n{e['summary_en']}")
        with open(content_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"  Created content/{e['id']}.md")

# Append to entries
entries_data['entries'].extend(entries_to_add)
entries_data['last_updated'] = datetime.datetime.now().isoformat()

with open(ENTRIES_FILE, 'w', encoding='utf-8') as f:
    json.dump(entries_data, f, ensure_ascii=False, indent=2)

print(f"\nentries.json updated: {len(entries_data['entries'])} total entries")
