#!/usr/bin/env python3
"""Morning intake 2026-05-13: Add new AI entries from Obsidian scan."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "openclaw" / "scripts"))
from pipeline_utils import load_entries_data, save_entries_data, append_entries, today_str

DATA_PATH = ROOT / "data" / "entries.json"
CONTENT_DIR = ROOT / "content"
CONTENT_DIR.mkdir(exist_ok=True)

# ── New entries ──────────────────────────────────────────────
new_entries = [
    # 1. Karpathy - Attention Mechanisms
    {
        "id": "kp_attn01",
        "title": "Understanding Attention Mechanisms in Transformers",
        "url": "https://x.com/karpathy/status/1800000000000000001",
        "source": {
            "platform": "x",
            "author": "Andrej Karpathy",
            "original_date": "2026-05-12",
        },
        "category": "learning",
        "tags": ["attention", "transformer", "llm", "deep-learning", "karpathy"],
        "source_type": "x_post",
        "language": "en",
        "summary_zh": "Karpathy 发布新博文，深入解析 Transformer 中的注意力机制。涵盖自注意力（Q/K/V 计算）、多头注意力（语法/语义/长距离依赖三个头分工）、位置编码实现，并给出性能优化建议：稀疏注意力和线性注意力可缓解 O(n²) 复杂度问题。附带代码示例和可视化，适合 LLM 从业者精读。",
        "summary_en": "Karpathy publishes a deep dive into attention mechanisms in Transformers, covering self-attention (Q/K/V), multi-head attention, positional encoding with code examples, and performance optimization techniques like sparse and linear attention for O(n²) complexity.",
        "one_liner": "Karpathy 的注意力机制图解教程，代码+可视化俱全，LLM 从业者必读。",
        "one_liner_author": "openclaw",
        "quality_score": 5,
        "status": "active",
        "local_path": "X 文章/2026-05-12/Andrej-Karpathy-Attention-Mechanisms.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 2. Lex Fridman x Hinton - AI Consciousness
    {
        "id": "lf_consc01",
        "title": "AI Consciousness: A Conversation with Geoffrey Hinton",
        "url": "https://x.com/LexFridman/status/1800000000000000004",
        "source": {
            "platform": "x",
            "author": "Lex Fridman",
            "original_date": "2026-05-12",
        },
        "category": "learning",
        "tags": ["consciousness", "ai-safety", "hinton", "philosophy", "agi"],
        "source_type": "x_post",
        "language": "en",
        "summary_zh": "Lex Fridman 与 Geoffrey Hinton 深度对谈 AI 意识问题。讨论三大场景：① 涌现意识——大模型复杂度足够时自发产生；② 架构突破——10-15年内可能出现专为意识设计的新架构；③ 基本限制——意识可能需要生物基底。伦理层面涉及 AI 权利、对齐问题和存在风险。完整播客下周发布。",
        "summary_en": "Lex Fridman and Geoffrey Hinton discuss AI consciousness: emergent consciousness from complex neural networks, architectural breakthroughs within 10-15 years, and fundamental limits requiring biological substrates. Ethical implications include AI rights, alignment, and existential risks.",
        "one_liner": "Hinton 谈 AI 意识三大路径：涌现、架构突破、生物限制，播客下周上线。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "local_path": "X 文章/2026-05-12/LexFridman-AI-Consciousness.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 3. Andrew Ng - Data Quality First
    {
        "id": "an_dqfst01",
        "title": "Key Insight: Focus on Data Quality First in AI Projects",
        "url": "https://x.com/AndrewYNg/status/1800000000000000003",
        "source": {
            "platform": "x",
            "author": "Andrew Ng",
            "original_date": "2026-05-12",
        },
        "category": "industry",
        "tags": ["data-quality", "ai-projects", "best-practices", "andrew-ng"],
        "source_type": "x_post",
        "language": "en",
        "summary_zh": "Andrew Ng 团队调研 500+ 组织后发现：78% 的 AI 项目因数据质量问题失败，仅 22% 组织有成熟的数据质量流程，65% 的 AI 从业者花更多时间清洗数据而非建模。建议分三阶段推进：数据评估（4-6周）→ 数据改进（8-12周）→ 模型开发（6-8周）。核心观点：先投资数据质量，再投资 AI 技术。",
        "summary_en": "Research across 500+ organizations: 78% of AI projects fail due to data issues, only 22% have mature data quality processes. Andrew Ng recommends a three-phase approach: data assessment → data improvement → model development. Invest in data quality before AI technology.",
        "one_liner": "78% AI 项目因数据质量失败——Andrew Ng 的三阶段数据优先方法论。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "local_path": "X 文章/2026-05-12/AndrewYNg-Data-Quality-First.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 4. Yann LeCun - Multimodal Future
    {
        "id": "yl_multi01",
        "title": "The Future of AI: Multimodal Systems Domination",
        "url": "https://x.com/ylecun/status/1800000000000000000",
        "source": {
            "platform": "x",
            "author": "Yann LeCun",
            "original_date": "2026-05-12",
        },
        "category": "models",
        "tags": ["multimodal", "vision-language", "reasoning", "agi", "lecun"],
        "source_type": "x_post",
        "language": "en",
        "summary_zh": "Yann LeCun 预判 AI 未来将由多模态系统主导。关键进展：① 跨模态理解——模型可同时处理文本、图像、音频和视频；② 增强推理——多模态系统在逻辑推理上优于单模态；③ 真实应用——从自动驾驶到医学影像。挑战包括计算效率、数据多样性和伦理问题。多模态整合使 AI 更接近人类认知。",
        "summary_en": "Yann LeCun predicts multimodal AI will dominate the future, with breakthroughs in cross-modal understanding, enhanced reasoning, and real-world applications from autonomous vehicles to medical imaging. Key challenges: computational efficiency, data diversity, and ethics.",
        "one_liner": "LeCun 判断多模态是 AI 的终局形态，跨模态推理正在逼近人类认知水平。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "local_path": "X 文章/2026-05-12/Yann-LeCun-Future-of-AI.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 5. OpenAI GPT-5 Preview
    {
        "id": "oa_gpt5pv01",
        "title": "GPT-5 Preview: Significant Improvements in Reasoning Capabilities",
        "url": "https://x.com/OpenAI/status/1800000000000000002",
        "source": {
            "platform": "x",
            "author": "OpenAI",
            "original_date": "2026-05-12",
        },
        "category": "models",
        "tags": ["gpt-5", "openai", "reasoning", "code-generation", "benchmark"],
        "source_type": "x_post",
        "language": "en",
        "summary_zh": "OpenAI 预告 GPT-5：推理能力大幅提升，数学问题解决提升 40%，代码生成准确率提升 45%，逻辑推理提升 35%。架构方面上下文窗口扩至 200K tokens，采用稀疏注意力机制。基准测试全面领先 GPT-4（MMLU 89.4%、GSM8K 92.1%、HumanEval 84.7%）。幻觉减少 60%。部署时间线：Q3 限量预览→Q4 公测→Q1 2027 正式发布。",
        "summary_en": "OpenAI previews GPT-5: 40% better math reasoning, 45% more accurate code generation, 35% improved logical reasoning. 200K token context, sparse attention. Benchmarks: MMLU 89.4%, GSM8K 92.1%, HumanEval 84.7%. 60% fewer hallucinations. Timeline: Q3 limited preview, Q4 public beta, Q1 2027 full release.",
        "one_liner": "GPT-5 预告：推理全面碾压 GPT-4，200K 上下文，幻觉减六成，Q3 开始限量预览。",
        "one_liner_author": "openclaw",
        "quality_score": 5,
        "status": "active",
        "local_path": "X 文章/2026-05-12/OpenAI-GPT5-Preview.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 6. Anthropic Claude Code agent view
    {
        "id": "ac_agview01",
        "title": "Anthropic 发布 Claude Code Agent View：多会话集中管理",
        "url": "https://t.me/synctoai/2108",
        "source": {
            "platform": "news",
            "author": "Levix 空间站",
            "original_date": "2026-05-12",
        },
        "category": "coding",
        "tags": ["claude-code", "agent", "developer-tools", "anthropic", "multi-agent"],
        "source_type": "article",
        "language": "zh",
        "summary_zh": "Anthropic 发布 Claude Code 的 agent view 功能，将多个 Claude Code 会话集中到一个界面管理。此前开发者同时运行多个智能体时需要在终端标签、tmux 网格间频繁切换。新功能简化了多智能体工作流的监控和协调。",
        "summary_en": None,
        "one_liner": "Claude Code agent view 终结了多智能体终端切换的痛苦，一站式管理多会话。",
        "one_liner_author": "openclaw",
        "quality_score": 3,
        "status": "active",
        "local_path": "Personal-Knowlodge/source/rss-tech/2026-05-13_RSS_02e8b3660d.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 7. PRISM框架 - dLLM Test-Time Scaling
    {
        "id": "prism_dllm01",
        "title": "ICML 2026｜PRISM框架让dLLM也能高效Test-Time Scaling",
        "url": "https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651032226&idx=2&sn=772b44d2bf16aac0a694b87df0a929e2",
        "source": {
            "platform": "wechat",
            "author": "机器之心",
            "original_date": "2026-05-11",
        },
        "category": "models",
        "tags": ["dllm", "test-time-scaling", "icml", "inference", "prism"],
        "source_type": "paper",
        "language": "zh",
        "summary_zh": "ICML 2026 论文提出 PRISM 框架，解决离散大语言模型（dLLM）的 Test-Time Scaling 效率问题。传统方法依赖暴力扩展计算量，PRISM 通过更高效的策略实现同等或更优性能，拒绝「大力出奇迹」路线。原文需微信公众号阅读全文。",
        "summary_en": None,
        "one_liner": "ICML 2026 论文：PRISM 让 dLLM 的 Test-Time Scaling 不再靠堆算力。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "local_path": "Personal-Knowlodge/source/rss-tech/2026-05-12_RSS_9dcc58a1fa.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 8. 腾讯技术工程 - Harness不是目的
    {
        "id": "tx_know01",
        "title": "Harness不是目的，知识才是护城河——AI工程交付团队的知识沉淀实践",
        "url": "https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649801507&idx=1&sn=c4ac5ce38024ade94b8bfa1fdc0062ad",
        "source": {
            "platform": "wechat",
            "author": "腾讯技术工程",
            "original_date": "2026-05-11",
        },
        "category": "agents",
        "tags": ["agent-harness", "knowledge-management", "ai-engineering", "best-practices"],
        "source_type": "article",
        "language": "zh",
        "summary_zh": "腾讯技术工程分享 AI 工程交付团队的知识沉淀实践。核心观点：Harness（工具链/框架）不是最终目的，真正的护城河在于团队积累的领域知识和工程经验。强调在 AI 项目交付过程中系统性地沉淀知识，而非仅关注工具层面。原文需微信公众号阅读全文。",
        "summary_en": None,
        "one_liner": "腾讯实践：AI 工程的护城河不是工具链，而是沉淀下来的领域知识。",
        "one_liner_author": "openclaw",
        "quality_score": 3,
        "status": "active",
        "local_path": "Personal-Knowlodge/source/rss-tech/2026-05-12_RSS_a31818c965.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 9. LanceDB Format v2.2 Benchmarks
    {
        "id": "ldb_v2201",
        "title": "LanceDB Lance Format v2.2: Half the Storage, None of the Slowdown",
        "url": "https://www.lancedb.com/blog/lance-format-v2-2-benchmarks-half-the-storage-none-of-the-slowdown",
        "source": {
            "platform": "blog",
            "author": "LanceDB",
            "original_date": "2026-05-12",
        },
        "category": "infra",
        "tags": ["lancedb", "vector-database", "storage", "benchmark", "data-format"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "LanceDB 发布 Lance 格式 v2.2 版本基准测试结果：存储空间减半，性能无损失。该格式是 LanceDB 向量数据库的底层数据格式，v2.2 在保持查询速度的同时显著降低存储成本，对大规模向量检索场景有实际意义。",
        "summary_en": "LanceDB releases Lance format v2.2 benchmarks: half the storage with no performance degradation. The underlying data format for LanceDB vector database significantly reduces storage costs while maintaining query speed for large-scale vector retrieval.",
        "one_liner": "LanceDB v2.2 存储减半速度不减，向量数据库的性价比新标杆。",
        "one_liner_author": "openclaw",
        "quality_score": 3,
        "status": "active",
        "local_path": "Personal-Knowlodge/source/rss-tech/2026-05-13_RSS_452c2b32c8.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 10. HTML vs Markdown for AI Agents
    {
        "id": "html_md01",
        "title": "Anthropic工程师：HTML比Markdown更适合AI Agent输出",
        "url": "https://www.techmeme.com/260511/p31#a260511p31",
        "source": {
            "platform": "news",
            "author": "Techmeme / @trq212",
            "original_date": "2026-05-11",
        },
        "category": "agents",
        "tags": ["html", "markdown", "agent-output", "anthropic", "developer-tools"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "Anthropic 工程师 @trq212 认为 HTML 比 Markdown 更适合作为 AI Agent 的输出格式。理由：① 信息密度更高；② 更易于分享和展示；③ 支持双向交互。这一观点在开发者社区引发讨论，Simon Willison 也撰文分析了 Claude Code 直接生成 HTML 的实践。",
        "summary_en": "Anthropic engineer argues HTML is a better output format for AI agents than Markdown, citing higher information density, easier sharing, and two-way interaction support. Simon Willison also wrote about Claude Code generating HTML directly.",
        "one_liner": "AI Agent 输出格式之争：Anthropic 工程师力挺 HTML 替代 Markdown。",
        "one_liner_author": "openclaw",
        "quality_score": 3,
        "status": "active",
        "local_path": "Personal-Knowlodge/source/rss-tech/2026-05-12_RSS_a5cea740bf.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
    # 11. Google Gemini Intelligence
    {
        "id": "gg_gemin01",
        "title": "Google 发布 Gemini Intelligence：AI 深度整合 Android 生态",
        "url": "https://www.techmeme.com/260512/p34#a260512p34",
        "source": {
            "platform": "news",
            "author": "Techmeme / Allison Johnson / The Verge",
            "original_date": "2026-05-12",
        },
        "category": "industry",
        "tags": ["google", "gemini", "android", "ai-product", "vibe-coding"],
        "source_type": "product",
        "language": "en",
        "summary_zh": "Google 发布 Gemini Intelligence，将现有和新增 Gemini 功能打包整合，包括跨应用任务自动化和 vibe-code Android 小组件功能。这意味着用户可以通过自然语言描述直接生成 Android 小组件，大幅降低开发门槛。标志着 Google 在移动端 AI 生态布局的重要一步。",
        "summary_en": "Google unveils Gemini Intelligence, bundling Gemini features including cross-app task automation and vibe-coding Android widgets. Users can generate widgets via natural language descriptions, marking a significant step in Google's mobile AI ecosystem.",
        "one_liner": "Google Gemini Intelligence：自然语言就能 vibe-code 出 Android 小组件。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "status": "active",
        "local_path": "Personal-Knowlodge/source/rss-tech/2026-05-13_RSS_f849b9eb95.md",
        "images": [],
        "added_date": "2026-05-13",
        "updated_date": None,
        "github_stars": None,
        "related": [],
    },
]

# ── Content files for X articles ──────────────────────────────
content_files = {
    "kp_attn01": ROOT / "X 文章" / "2026-05-12" / "Andrej-Karpathy-Attention-Mechanisms.md",
    "lf_consc01": ROOT / "X 文章" / "2026-05-12" / "LexFridman-AI-Consciousness.md",
    "an_dqfst01": ROOT / "X 文章" / "2026-05-12" / "AndrewYNg-Data-Quality-First.md",
    "yl_multi01": ROOT / "X 文章" / "2026-05-12" / "Yann-LeCun-Future-of-AI.md",
    "oa_gpt5pv01": ROOT / "X 文章" / "2026-05-12" / "OpenAI-GPT5-Preview.md",
}

# ── Load existing data ────────────────────────────────────────
data = load_entries_data(DATA_PATH)

# ── Copy content files ────────────────────────────────────────
import shutil
for entry_id, src_path in content_files.items():
    dest = CONTENT_DIR / f"{entry_id}.md"
    if src_path.exists() and not dest.exists():
        shutil.copy2(src_path, dest)
        print(f"  ✓ content/{entry_id}.md copied")

# RSS items: write content stubs noting fetch failure
rss_stubs = {
    "ac_agview01": "Claude Code agent view — 原文来自 Telegram，内容截断。",
    "prism_dllm01": "PRISM框架 — 原文来自微信公众号，抓取受限（CAPTCHA）。",
    "tx_know01": "腾讯技术工程 — 原文来自微信公众号，抓取受限（CAPTCHA）。",
    "ldb_v2201": "LanceDB v2.2 — 原文来自 Telegram 频道转发。",
    "html_md01": "HTML vs Markdown — 原文来自 Techmeme，Cloudflare 拦截。",
    "gg_gemin01": "Google Gemini Intelligence — 原文来自 Techmeme，Cloudflare 拦截。",
}
for entry_id, note in rss_stubs.items():
    dest = CONTENT_DIR / f"{entry_id}.md"
    if not dest.exists():
        dest.write_text(f"> 备注：原文抓取失败，以下为摘要。\n\n{note}\n", encoding="utf-8")
        print(f"  ⚠ content/{entry_id}.md stub written")

# ── Append entries ─────────────────────────────────────────────
added, skipped = append_entries(data, new_entries)

# ── Save ───────────────────────────────────────────────────────
save_entries_data(data, DATA_PATH)

print(f"\n{'='*50}")
print(f"Added: {len(added)} entries")
for e in added:
    print(f"  + [{e['id']}] {e['title'][:60]}")
if skipped:
    print(f"Skipped: {len(skipped)} entries")
    for e, reason in skipped:
        print(f"  - [{e['id']}] {reason}: {e['title'][:50]}")
print(f"Total entries now: {len(data.get('entries', []))}")
