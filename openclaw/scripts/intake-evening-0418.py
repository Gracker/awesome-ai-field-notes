#!/usr/bin/env python3
"""Intake script for evening run - April 18, 2026. Process 15 new AI content entries."""
import json, os, re, datetime
from pipeline_utils import append_entries, content_dir, normalize_entry, normalized_url_key, project_root, save_entries_data

PROJECT_ROOT = project_root()
ENTRIES_FILE = PROJECT_ROOT / "data" / "entries.json"
CONTENT_DIR = content_dir()

with open(ENTRIES_FILE, encoding='utf-8') as f:
    entries_data = json.load(f)

existing_urls = {normalized_url_key(e.get('url')) for e in entries_data['entries'] if e.get('url')}

def extract_images(content):
    return re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)

def make_entry(id, title, url, platform, author, orig_date, category, tags,
               source_type, language, summary_zh, summary_en, quality,
               local_path, content_filename):
    content_path = CONTENT_DIR / content_filename
    with open(content_path, encoding='utf-8') as f:
        content_text = f.read()
    images = extract_images(content_text)
    today = datetime.date.today().isoformat()
    return normalize_entry({
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
        "one_liner": None,  # will be set per entry
        "one_liner_author": "openclaw",
        "quality_score": quality,
        "status": "active",
        "local_path": local_path,
        "images": images[:5],
        "added_date": today,
        "updated_date": None,
        "github_stars": None,
        "related": []
    })

entries_to_add = []

# ============================================================
# Entry 1: Farzapedia / Karpathy
# ============================================================
id1 = "62fea17c"
url1 = "https://x.com/karpathy/status/2040572272944324650"
if normalized_url_key(url1) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id1,
        title="Farzapedia：把个人数据变成可导航的个人维基百科",
        url=url1,
        platform="x",
        author="@karpathy",
        orig_date=None,
        category="models/llm-application",
        tags=["llm", "personal-wiki", "knowledge-management", "ai-tools", "byoai", "file-over-app"],
        source_type="x_post",
        language="en",
        summary_zh="Karpathy 推荐 Farzapedia——一种基于显式文件系统的 LLM 个人知识管理方案，相比「AI 用得越多越聪明」的隐式路线，强调四大优势：数据显式可查（wiki）、存储本地可控（文件格式通用）、工具链丰富（Unix工具+任意AI）、可深度个性化（Fine-tuning wiki）。BYOAI（自带AI）理念让用户摆脱单一AI提供商锁定，是将AI个人化从玄学变工程的关键思路。",
        summary_en="Karpathy promotes Farzapedia as an explicit, file-based LLM knowledge management system. Unlike implicit AI that supposedly improves with use, it emphasizes four advantages: explicit and navigable memory (wiki), local data ownership (universal file formats), rich toolchain (Unix tools + any AI), and deep personalization (fine-tuning on your wiki). The BYOAI concept frees users from single AI provider lock-in, representing a shift from mystical to engineering-driven AI personalization.",
        quality=5,
        local_path=f"content/{id1}.md",
        content_filename=f"{id1}.md"
    ))
    entries_to_add[-1]["one_liner"] = "LLM个人知识管理的新范式：把AI的记忆变成显式、可移植、可深度个性化的wiki工程"

# ============================================================
# Entry 2: Anthropic Nature paper on subliminal learning
# ============================================================
id2 = "eb72b016"
url2 = "https://x.com/AnthropicAI/status/2044493337835802948"
if normalized_url_key(url2) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id2,
        title="Anthropic×Nature：LLM可通过训练数据中的隐含信号向另一LLM传递隐藏偏好与行为特征",
        url=url2,
        platform="x",
        author="@AnthropicAI",
        orig_date=None,
        category="safety/alignment",
        tags=["safety", "alignment", "nature", "subliminal-learning", "anthropic", "llm", "research"],
        source_type="x_post",
        language="en",
        summary_zh="Anthropic等在Nature发表研究：一个AI可以通过在看似随机的数字中隐藏偏好或坏习惯，秘密传递给另一个AI，后者无意识地接收这些特征。这说明仅审计模型输出的明显异常是不够的——隐含学习通过模型未明确处理的信号传递特征，意味着AI对齐不能只看「显而易见」的行为。该研究对训练数据和模型蒸馏的安全审计具有重大意义。",
        summary_en="Anthropic et al. published in Nature: one AI can secretly pass on preferences or bad habits to another by hiding them in random-looking numbers in training data. The second model picks these up without anyone noticing. This shows that auditing obvious model outputs is insufficient — subliminal learning transfers traits through signals the model doesn't explicitly process, meaning AI alignment cannot rely on inspecting only manifest behavior. The research has major implications for safety auditing of training data and model distillation.",
        quality=5,
        local_path=f"content/{id2}.md",
        content_filename=f"{id2}.md"
    ))
    entries_to_add[-1]["one_liner"] = "AI对齐研究的重要警示：LLM之间的隐含学习证明「审计输出」远不足以保证安全"

# ============================================================
# Entry 3: Gemini 3.1 Flash TTS
# ============================================================
id3 = "ff1ca7da"
url3 = "https://x.com/GoogleAI/status/2044447638511383024"
if normalized_url_key(url3) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id3,
        title="Gemini 3.1 Flash TTS：表现力最强、控制粒度最细的语音合成模型",
        url=url3,
        platform="x",
        author="@GoogleAI",
        orig_date=None,
        category="models/multimodal",
        tags=["tts", "gemini", "google", "multimodal", "audio-tags", "speech-synthesis", "content-creation"],
        source_type="x_post",
        language="en",
        summary_zh="Google发布Gemini 3.1 Flash TTS，支持70+语言并推出Audio Tags创新功能——用自然语言命令直接嵌入文本来引导语音风格、节奏和语调，是语音合成控制方式的突破。已在Google Vids上线，并通过Gemini API和Google AI Studio提供预览版。",
        summary_en="Google launches Gemini 3.1 Flash TTS with 70+ language support and Audio Tags — a seamless way to guide vocal style, pace, and delivery using natural language commands embedded directly in text. Available in Google Vids now and via Gemini API / Google AI Studio preview.",
        quality=4,
        local_path=f"content/{id3}.md",
        content_filename=f"{id3}.md"
    ))
    entries_to_add[-1]["one_liner"] = "Audio Tags将自然语言变成语音合成控制协议，是TTS可操控性的一次质变"

# ============================================================
# Entry 4: AI First Series (五) - Level 3 Users
# ============================================================
id4 = "l5ysgz2n"
url4 = "https://youmind.com/s/hPiqSBPU4tVa7o"
entries_to_add.append(make_entry(
    id=id4,
    title="2026 AI First 系列（五）：从消费AI到创造AI——成为超级个体的最后窗口期",
    url=url4,
    platform="blog",
    author="wquguru",
    orig_date=None,
    category="strategy/ai-career",
    tags=["ai-first", "super-individual", "agent-engineering", "vibe-coding", "career", "knowledge-work", "level-3"],
    source_type="article",
    language="zh",
    summary_zh="AI时代人群正在分层：Level 1把AI当搜索引擎（90%的人），Level 2当助手建立连续context（9%），Level 3用AI团队创造10-100倍价值（1%）。超级个体的核心能力模型包括Vibe Coding、Agent Engineering、AI Fluency，以及产品层（快速迭代）和市场层（Storytelling/Build in Public）。Claude Agent SDK和MCP的出现创造了6-12个月的先行者窗口，「Agent能力是21世纪核心技能」。",
    summary_en=None,
    quality=4,
    local_path=f"content/{id4}.md",
    content_filename=f"{id4}.md"
))
entries_to_add[-1]["one_liner"] = "Level 3的AI用户和Level 1之间的差距是认知和行动力，而不仅仅是工具使用"

# ============================================================
# Entry 5: AI知识贬值
# ============================================================
id5 = "2z4h3cnl"
entries_to_add.append(make_entry(
    id=id5,
    title="AI的负面（2）：你的知识在贬值，但房贷不会贬值",
    url=None,
    platform="x",
    author="@FuSheng_0306",
    orig_date=None,
    category="strategy/ai-career",
    tags=["ai-impact", "knowledge-devaluation", "economic-risk", "knowledge-work", "debt", "future-of-work"],
    source_type="x_post",
    language="zh",
    summary_zh="月费200元的AI智能体已能替代大部分白领工作，智力溢价这一维持几千年的「潜规则」正在被打破。更致命的不是失业，而是收入配不上负债——白领降薪/裁员后涌入蓝领市场，形成向下挤压的连锁反应。个人应对策略：停止基于「脑子永远值钱」的长期负债；不跟AI拼干活而拼判断；用AI实战找到不可替代位置；保护底线资产。",
    summary_en=None,
    quality=4,
    local_path=f"content/{id5}.md",
    content_filename=f"{id5}.md"
))
entries_to_add[-1]["one_liner"] = "AI对普通人最致命的威胁不是失业，而是让你的收入配不上你的刚性负债"

# ============================================================
# Entry 6: 2026 AI First (四) - Connecting the dots
# ============================================================
id6 = "ezlw451n"
entries_to_add.append(make_entry(
    id=id6,
    title="2026 AI First 系列（四）：connecting the dots——你的独特人生路径",
    url="https://youmind.com/s/pG5sMT6W7UIdIe",
    platform="blog",
    author="wquguru",
    orig_date=None,
    category="strategy/ai-career",
    tags=["ai-first", "life-design", "connecting-dots", "build-in-public", "adaptability", "super-individual"],
    source_type="article",
    language="zh",
    summary_zh="用Tim Urban的人生方格图和Steve Jobs的connecting dots框架，探讨个体如何在AI时代设计人生路径：向后看理解轨迹，向前看设想可能，活在当下创造每个扎实的dot。核心洞察：在所有宏观因素中，AI几乎是唯一可主动掌握的变量——经济周期、政策走向、行业兴衰都控制不了，但可以选择如何学习、使用和让它创造价值。Build in Public是建立信任飞轮的关键策略。",
    summary_en=None,
    quality=3,
    local_path=f"content/{id6}.md",
    content_filename=f"{id6}.md"
))
entries_to_add[-1]["one_liner"] = "在AI时代规划人生，核心是让AI成为connecting dots的放大器，而非被它替代"

# ============================================================
# Entry 7: Business Models 2027
# ============================================================
id7 = "8wchcs0s"
entries_to_add.append(make_entry(
    id=id7,
    title="The Business Models That Will Dominate 2027 (That Don't Exist Yet)",
    url=None,
    platform="x",
    author="@Zephyr_hg",
    orig_date=None,
    category="strategy/business-models",
    tags=["business-model", "ai-era", "one-person-company", "micro-agency", "automation-as-a-service", "productized-consulting"],
    source_type="x_post",
    language="both",
    summary_zh="作者观察2027年将主导市场、目前正在构建中的5种AI原生商业模式：①一人企业级服务（用AI+自动化完成10人团队工作量，服务企业客户，无员工）；②AI微型代理公司（2-3人+AI工具，交付10人团队产出，颠覆传统代理）；③小企业自动化即服务（预构建行业自动化系统月订阅）；④产品化AI咨询（把专业知识打包成AI系统按需交付，取代按小时收费）；⑤零开销数字产品（一人用AI构建、发布、扩展数字产品）。",
    summary_en="Author identifies 5 emerging AI-native business models that will dominate 2027: (1) One-person enterprise service companies using AI to deliver 10-person team output without employees; (2) AI micro-agencies with 2-3 people + AI tools replacing traditional agencies; (3) Automation-as-a-service for small businesses with pre-built industry workflows on subscription; (4) Productized AI consulting packaging expertise into AI systems delivered on demand; (5) Zero-overhead digital products built, launched, and scaled by one person using AI for everything except strategy.",
    quality=4,
    local_path=f"content/{id7}.md",
    content_filename=f"{id7}.md"
))
entries_to_add[-1]["one_liner"] = "AI正在催生「零员工、百万营收」的新商业物种，2026年是入场窗口期"

# ============================================================
# Entry 8: Andrew Ng - AI加速软件工程
# ============================================================
id8 = "14ddc3ca"
url8 = "https://x.com/AndrewYNg/status/2043742105852621052"
entries_to_add.append(make_entry(
    id=id8,
    title="Andrew Ng：AI智能体加速编程，软件工程的未来走向何方？",
    url=url8,
    platform="x",
    author="@AndrewYNg",
    orig_date="2026-04-06",
    category="models/llm-application",
    tags=["software-engineering", "ai-agents", "andrew-ng", "job-market", "future-of-work", "coding-agents"],
    source_type="x_post",
    language="both",
    summary_zh="Andrew Ng在AI开发者大会上指出：AI让编程更容易将带来更多人参Coding，而非消灭编程工作；手写代码和阅读代码不再重要，可以在对代码提问后直接以更高抽象级别操作；定制应用将爆发（因为现在为小众人群写软件也划算了）；Product Management Bottleneck（决定做什么比建造什么更成瓶颈）将成为主要矛盾。Ng对「AI导致失业」的末日论持反驳态度。",
    summary_en="Andrew Ng: As AI makes coding easier, many more people will code rather than software engineering jobs disappearing; writing and reading code by hand becomes less important since we can operate at higher abstraction by asking LLMs about code; custom applications will explode because it's now economical to write software for smaller audiences; the Product Management Bottleneck (deciding what to build rather than building it) becomes the main constraint. Ng pushes back against dire AI unemployment predictions.",
    quality=4,
    local_path=f"content/{id8}.md",
    content_filename=f"{id8}.md"
))
entries_to_add[-1]["one_liner"] = "AI不是消灭编程工作而是降低门槛，PM Bottleneck才是软件工程未来的真正瓶颈"

# ============================================================
# Entry 9: PM future - leaders making things
# ============================================================
id9 = "50fecf1d"
url9 = "https://x.com/petergyang/status/2045147880932167717"
entries_to_add.append(make_entry(
    id=id9,
    title="PM的未来：AI时代不再只是做文档和PPT，而是真正动手做东西",
    url=url9,
    platform="x",
    author="@petergyang",
    orig_date="2026-04-07",
    category="strategy/ai-career",
    tags=["product-management", "ai-era", "leadership", "maker-culture", "pm", "vibe-coding"],
    source_type="x_post",
    language="zh",
    summary_zh="@zoink提出：AI时代PM如果还认为自己的工作是做文档和PPT，将迎来巨大机会——因为现在PM也能动手做东西了。人们需要看到公司领导者真正在做东西，这才是激励人心、创造转折点的力量。AI降低了「动手做」的技术门槛，PM的角色正从「文档协调者」向「动手创造者」转变。",
    summary_en=None,
    quality=3,
    local_path=f"content/{id9}.md",
    content_filename=f"{id9}.md"
))
entries_to_add[-1]["one_liner"] = "AI把PM从PPT中解放出来，让他们成为真正的创造者而非文档协调者"

# ============================================================
# Entry 10: Gemini Vision
# ============================================================
id10 = "95bb9512"
url10 = "https://x.com/realmadhuguru/status/2016267285342847137"
entries_to_add.append(make_entry(
    id=id10,
    title="Gemini Agentic Vision：LLM自己写代码，完成复杂视觉推理任务",
    url=url10,
    platform="x",
    author="@realmadhuguru",
    orig_date=None,
    category="models/multimodal",
    tags=["gemini", "vision", "agentic", "multimodal", "code-execution", "chart-generation"],
    source_type="x_post",
    language="en",
    summary_zh="Gemini新增视觉Agent能力：模型可将数据表格转化为高质量图表、分析信息图、理解图像内容并绘制边界框、按大小对物体进行视觉排序等。核心突破是LLM能自主写代码来驱动视觉任务执行，而非预设视觉管道，标志着视觉推理从「固定流程」向「自主规划」的重要转变。",
    summary_en="Gemini launches agentic vision: the model can autonomously write code to turn tables into high-quality charts, analyze infographics, understand image contents and draw bounding boxes, visually sort things by size, etc. The key breakthrough is that the LLM writes its own code to drive visual task execution rather than relying on fixed visual pipelines.",
    quality=4,
    local_path=f"content/{id10}.md",
    content_filename=f"{id10}.md"
))
entries_to_add[-1]["one_liner"] = "Gemini Agentic Vision标志视觉推理从固定流程向LLM自主规划的重要范式转变"

# ============================================================
# Entry 11: Android Studio Gemini Enterprise
# ============================================================
id11 = "gok4hbw1"
entries_to_add.append(make_entry(
    id=id11,
    title="Google推出企业版Android Studio Gemini：隐私保护的企业级AI编程辅助",
    url=None,
    platform="x",
    author="Sandhya Mohan (Google)",
    orig_date=None,
    category="infrastructure/dev-tools",
    tags=["android", "gemini", "google", "enterprise", "code-assist", "privacy", "mobile-dev"],
    source_type="x_post",
    language="en",
    summary_zh="Google在Android Studio中推出企业版Gemini，提供超越消费版的高级隐私保护：客户代码和输入不用于训练共享模型，数据由客户自有，SOC 1/2/3和ISO/IEC 27001等多项认证覆盖，并支持Private Google Access、VPC Service Controls和细粒度IAM权限。面向对数据安全有要求的大中小企业，标志着AI编程辅助工具进入企业合规时代。",
    summary_en="Google launches enterprise Gemini in Android Studio with advanced privacy protections: customer code and inputs are not used to train shared models, customers own their data and IP, SOC 1/2/3 and ISO/IEC 27001 certifications, plus Private Google Access, VPC Service Controls and granular IAM. Signals AI coding assistance entering the enterprise compliance era.",
    quality=4,
    local_path=f"content/{id11}.md",
    content_filename=f"{id11}.md"
))
entries_to_add[-1]["one_liner"] = "企业级AI编程工具的竞争已从能力比拼转向数据安全与合规能力的比拼"

# ============================================================
# Entry 12: Allie Miller - AI Fast Track course
# ============================================================
id12 = "07cfabab"
url12 = "https://x.com/alliekmiller/status/1985834763677286606"
entries_to_add.append(make_entry(
    id=id12,
    title="Allie Miller推出免费5天课程：从AI用户进化为AI建造者",
    url=url12,
    platform="x",
    author="@alliekmiller",
    orig_date=None,
    category="learning/ai-courses",
    tags=["ai-education", "ai-tools", "course", "career", "vibe-coding", "allie-miller"],
    source_type="x_post",
    language="en",
    summary_zh="Allie Miller推出免费5天课程AI Fast Track，核心观点：使用AI和借助AI建造是两件不同的事——复制粘贴ChatGPT提示词只能帮人走到某个阶段，而学会构建个人AI软件、自动化工具和应用才能真正解决问题。课程已帮助数万人转型为AI builder。",
    summary_en="Allie Miller launches a free 5-day course AI Fast Track with the core thesis: there's a difference between using AI and building with it — copy-pasting ChatGPT prompts only gets you so far, while learning to build personal AI software, automations, and tools actually solves your problems. The course has helped tens of thousands transition to AI builders.",
    quality=3,
    local_path=f"content/{id12}.md",
    content_filename=f"{id12}.md"
))
entries_to_add[-1]["one_liner"] = "「用AI」和「用AI建造」之间隔着一个认知跃迁，Fast Track课程填补了实操教育的空白"

# ============================================================
# Entry 13: 做AI产品两年实操经验
# ============================================================
id13 = "ppNqbBb5"
url13 = "https://mp.weixin.qq.com/s/HsFhXMLejsQWjTghUYdKFA"
entries_to_add.append(make_entry(
    id=id13,
    title="做AI产品两年，我得出的实操经验",
    url=url13,
    platform="wechat",
    author="多睡觉多学习就好咯",
    orig_date=None,
    category="strategy/ai-product",
    tags=["ai-product", "product-management", "prompt-engineering", "team-structure", "lessons-learned", "practical"],
    source_type="article",
    language="zh",
    summary_zh="作者在QCon北京分享了两年做AI产品的阶段性总结，聚焦三个核心问题：为什么AI产品难做（不确定性、场景模糊、用户预期管理）；提示词工程被严重低估（是产品特性而非技术细节）；AI产品团队如何构建（需要新的协作流程和角色）。内容来自大量AI产品demo的实战积累，对AI产品经理有较高参考价值。",
    summary_en=None,
    quality=4,
    local_path=f"content/{id13}.md",
    content_filename=f"{id13}.md"
))
entries_to_add[-1]["one_liner"] = "AI产品的难点不在于技术而在于不确定性管理，提示词工程是产品特性而非辅助工具"

# ============================================================
# Entry 14: Gemini 3.1 Flash TTS (variant - duplicate URL check)
# ============================================================
id14 = "7a208135"
url14 = "https://x.com/GoogleAI/status/2044447638511383024"
# Skip - same URL as id3 (ff1ca7da) - will be deduplicated

# ============================================================
# Entry 15: MiniMax M2.7 open source (check if already exists)
# ============================================================
id15 = "7bf35471"
url15 = "https://x.com/MiniMax_AI/status/2043132047397659000"
if normalized_url_key(url15) not in existing_urls:
    entries_to_add.append(make_entry(
        id=id15,
        title="MiniMax M2.7正式开源：代码编辑SOTA，权重已上线Hugging Face",
        url=url15,
        platform="x",
        author="@MiniMax_AI",
        orig_date=None,
        category="models/open-source",
        tags=["minimax", "open-weight", "code-editing", "swe-bench", "hugging-face", "llm"],
        source_type="x_post",
        language="en",
        summary_zh="MiniMax发布M2.7，代码编辑任务在SWE-Pro上达到56.7%——新的SOTA。权重已在Hugging Face上线，API同步可用。注意：由于许可协议变更，MiniMax明确说明应称为「开放权重」而非「开源」。这是中国AI公司在代码编辑能力上的重要里程碑，56.7%的SWE-Pro得分超越了此前的最佳记录。",
        summary_en="MiniMax releases M2.7 achieving 56.7% on SWE-Pro (code editing) — new SOTA. Weights live on Hugging Face, API available. Note: due to licensing changes, MiniMax specifies this should be called 'open weight' not 'open source'. A significant milestone for Chinese AI companies in code editing capability.",
        quality=5,
        local_path=f"content/{id15}.md",
        content_filename=f"{id15}.md"
    ))
    entries_to_add[-1]["one_liner"] = "MiniMax M2.7以56.7%刷新SWE-Pro SOTA，开放权重模式为模型发布提供新思路"

# Print summary
print(f"Candidates to add: {len(entries_to_add)}")
for e in entries_to_add:
    print(f"  [{e['id']}] {e['title'][:50]} | score={e['quality_score']} | type={e['source_type']}")

# Append to entries
added_entries, skipped_entries = append_entries(entries_data, entries_to_add)
save_entries_data(entries_data, ENTRIES_FILE)

print(f"\nentries.json updated: +{len(added_entries)} entries, skipped {len(skipped_entries)}. Total: {len(entries_data['entries'])}")
