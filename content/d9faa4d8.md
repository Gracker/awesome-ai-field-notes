# lieflat_3: 2.83M-word controlled-corpus study of 'AI tone' — 11 features survive, no universal 'AI style'

> Source: <https://x.com/lieflat_3/status/2099746344466579566>
> GitHub: <https://github.com/larashero3-dotcom/lieflat-less-ai-tone>
> Author: lieflat_3 (GTM @moxt_ai; former Fudan journalism; GitHub 10k stars)
> Posted: 2026-09-15 06:25 UTC; full text captured 2026-09-25 via `opencli twitter article`

## Why this experiment matters

After extended use of AI for writing, the author developed a near-physiological aversion to certain constructions — including the "not A but B" parallel structure and em-dash overuse. Viewed in isolation any one of them is fine and is also commonly used by humans, but at a certain density and combination they form an immediately recognisable signal: "AI tone".

Open-source de-AI-tone projects exist and work, but over time two structural problems appear: coverage gaps (the author can feel AI-tone patterns that the rule set does not list), and collateral damage (some rules also erase the author's own expression habits). Both problems have the same root cause: most projects are built on case observations and intuition summaries, without systematic verification.

Hence the question: **collect enough human and AI articles, then use a controlled-experiment methodology in linguistics to compare the per-feature frequency difference between the two populations, and quantify what "AI tone" actually is**.

## Corpus and method

Corpus is the most important input — it directly drives script output.

- A first pass with 30 samples per model produced confident-looking results, including "em-dash is a Claude-only feature". Scaling to 300 samples per model: DeepSeek's em-dash frequency was higher than Claude's (5.16 vs 4.25 per 1,000 characters), while GPT barely used em-dashes (0.11). Generalisation requires enough sample data so that one model's individual tendency is not mistaken for AI-wide commonality.
- The final corpus is **329 real human articles** (1.648M characters) and **300 AI-generated articles** (about 1.18M characters). To produce the AI side, the author built an automated workflow with 5 agents, each on a different mainstream model: **Claude Opus 4.6, DeepSeek V4-Pro, Gemini 3.1 Pro, GPT 5.6 Sol, Kimi K3** (60 articles per model). Conditions were strictly controlled: no network, no style instruction, topic only.
- Total: **629 articles, 2.83M characters**.
- Method: per-feature frequency. If an AI feature's frequency is ≥2× the human frequency it counts as a significant AI-tone signal. 0.8 to 1.25 means no difference. <0.8 means humans use it more; rewriting in that direction makes text less human.
- Additional statistical constraints: human-side per-group values must not differ by more than 5× (rules out genre bias); features must land on locatable sentence spans and word forms (rules out semantic-judgement features).

26 candidate features were tested; **11 passed**.

## Findings: 11 features that survived

The strongest separators live at the discourse and structure level, not at vocabulary or punctuation level.

### Strongest: zero-anaphora evaluative clause at paragraph start — 4.4×

AI writing, between paragraphs, drops the connective: at the start of a new paragraph it throws out an evaluation ("sounds like a feature description") without saying what the evaluation is about; the reader has to scroll back to find the referent. Total connector use is not different (AI 14.4%, human 15.1%); the difference is only that the evaluative clauses lose the anaphora. Fix: add a "this" or other anaphoric noun; the connective stops being stiff.

### Anthropomorphic metaphor — 7.3×

The author originally believed AI metaphor sentences had especially strong AI tone, so the agent ran a script to count total metaphor sentences. AI's overall metaphor frequency is actually lower than human's. So the metaphor problem is not about quantity, it is about whether the metaphor fits. Moxt then sub-categorised metaphors, and asked which kinds of metaphor AI uses significantly more. The result: anthropomorphic metaphors — "like an indefatigable assistant" — appear far more often in AI writing.

The author's hypothesis: models do not really understand metaphor — they do not know what is like what — they just hard-couple things that look related.

### Translation-pattern: 5 of 18 candidates pass

In Chinese writing by Claude/GPT/Gemini, translation-pattern issues are obvious. Moxt initially listed 18 candidate translation patterns; only 5 passed the screen: overlong front-loaded attributives, "当……时" subordinate clauses, front-loaded topic shells, sentence-initial connectives, and "这意味着" recaps. The other 13 candidates have too-low frequency to claim an AI signature — they may be translation patterns, but data does not support flagging them.

### Counter-direction rule: data density

AI's numeric density is only 0.35× of human's, so do not invent data — keep data support as detailed as possible to make text less AI-toned.

### Features that did NOT survive (and why this matters)

- **Rhetorical questions.** "AI loves rhetorical questions" appears in nearly every de-AI-tone tip list. Measured: human frequency is 17× AI's (human 1.83/1000 chars, AI 0.10). None of the 5 models likes rhetorical questions. Following the "reduce rhetorical questions" advice will only push text further from human writing.
- **Sentence-length variance.** Initial measurement put AI's variance coefficient at 51× human's — the strongest-looking feature in the table; the author ranked it rule #1. After investigation, the sentence-segmentation script had a bug: Markdown tables and period-less long lists were treated as a single sentence; one group produced a "paragraph" of 19,335 characters. After the fix, the ratio was 0.87 — no difference on either side.

## Cross-model deltas: no unified "AI style"

A side finding: the same feature can differ by 40× between models.

- Em-dash: DeepSeek V4-Pro 5.16 / 1,000 chars, GPT 0.11.
- "Not A but B" parallel structure: GPT 5.6 Sol 1.26, Gemini 3.1 Pro 0.29.
- Prompt-colon: DeepSeek and Claude 0.43 / 0.38; GPT and Gemini are low.
- Question-headed sub-headings: Gemini 0.173; Kimi 0.

So a "AI feature" summarised from a single model does not necessarily survive a model swap.

## Limits and future direction

- 2.83M characters is far from enough. 2.83M characters cannot represent "AI", and cannot represent human writing either.
- 329 human articles, inside the larger set of human writing, is too few. Even at this sample size, source-to-source differences are already large — em-dash alone differs by 100× between sources. Extending the corpus will probably change some conclusions.
- Writing is subjective and depends heavily on human intellectual characteristics; quantification is hard. Prompt or skill-level fixes usually only solve local problems — you can stop an em-dash, but you cannot teach a model when a metaphor actually fits. Real writing-level lift has to wait for the underlying capability to move forward.
- The author's own bet: **this is more likely a pretraining-stage problem**. The study itself, in some parts, is closer to pretraining work than to post-training.

## Linkage to local writing pipelines

For anyone running a Hermes Agent / Claude Code / Codex / 自建 writing pipeline that targets long-form Chinese, the directly usable judgements:

- Eleven features in the corpus survive the screen; treat them as audit items, not as a complete list.
- Cross-model deltas reach 40× — pin the model snapshot when you compare two writing pipelines, do not just pin "the framework".
- Use-case / genre-specific de-AI-tone skills are likely to outperform a generic skill; the corpus here is media / 自媒体 deep-article oriented.
- Do not auto-apply "reduce rhetorical questions" — measured effect is the opposite direction.

## Sources

- X original: <https://x.com/lieflat_3/status/2099746344466579566>
- GitHub repository: <https://github.com/larashero3-dotcom/lieflat-less-ai-tone>
