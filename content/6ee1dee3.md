# Hide your slop PR descriptions behind <details><summary>

- **ID**: 6ee1dee3
- **来源**: https://simonwillison.net/2026/Nov/9/details-summary/
- **作者**: Simon Willison
- **发表**: 2026-11-09
- **证据**: AK-RSS Digest 2026-11-09（source/ 全文抓取，2026-11-09 20:16 Asia/Shanghai）

## 原文全文

# Hide your slop PR descriptions behind <details><summary>
> 作者: Simon Willison
> 原文链接: https://simonwillison.net/2026/Nov/9/details-summary/

---

## Hide your slop PR descriptions behind <details><summary>

9th November 2026

Most of the changes I make to my projects these days come in the form of PRs opened for me by Claude Code or Codex. The PR is my unit of work—I use them to bundle commits together, iterating on them until a feature is complete, document decisions and then merge the finished result. Today’s coding agents are great at writing PR descriptions.

#### They’re too good at describing the work [#](https://simonwillison.net/2026/Nov/9/details-summary/#they-re-too-good-at-describing-the-work)

The problem is that they are _too_ good. An agent-written PR description is accurate and comprehensive. It describes the problem, the detailed solution, and the steps taken to verify it. That’s a lot of information to absorb.

It’s not necessarily slop, but it _reads_ like slop!

It’s very easy to spot an AI-written PR, and as with other forms of AI writing my instant reaction is best summarized as “I’m not reading all of that”. It doesn’t matter how accurate or useful the information is, I’m instantly put off by the thought that it will take me longer to read than it took the driving author to write... even when that driving author is me!

I want human editorial judgement. I want someone to have thought just long enough about the PR to give me a human-approved introduction that helps me understand, at a high level, what the PR is for and whether it deserves more of my attention.

I think I’ve found a low-effort way to do this that feels right.

#### Hide most of it in a details/summary [#](https://simonwillison.net/2026/Nov/9/details-summary/#hide-most-of-it-in-a-details-summary)

The HTML `<details><summary>` elements render as a collapsed heading (the summary) that can be expanded to view the larger piece of text. The code looks like this:

```html
<details>
  <summary>Claude Opus 5.5</summary>
  <h2>The hook</h2>
  Plugins implement <code>register_agent_reference_types(datasette)</code>...
</details>
```

When rendered, it looks [like this](https://github.com/datasette/datasette-agent/pull/51):

![Screenshot of a GitHub PR. The text "Claude Opus 5.5" sits next to a little black arrow. Clicking on that text expands a full description inside the PR body.](https://static.simonwillison.net/static/2026/details-summary-pr.gif)

Crucially, `<details><summary>` _is supported in GitHub Markdown_. You can drop those tags directly into an issue comment or PR description and GitHub will hide the details and display just the summary plus an expansion arrow.

I’ve started using this for my AI-generated pull requests.

The opening paragraph of my PRs will be carefully selected to act as a high-level explanation of what’s going on—the shortest text a human can read that will help get them up to speed.

I’ll sometimes throw in a screenshot as well, since images are often the best way to quickly illustrate a new feature.

The full agent-written essay then follows in a `<details><summary>`. I use the model name and often the effort level as that summary, to make it abundantly clear what is going on—“Claude Opus 5.5 Medium” for example.

My PRs don’t feel nearly as sloppy now! The information is all still there, but a reader can glance at it and get the top, human-curated information without their eyes glazing over at multiple paragraphs of agent-written details.

I don’t always write the introduction myself—sometimes the agent has given me what I need already, hidden away in the avalanche of other text. My promise to the reader is that the short opener will represent my human judgement as to what is definitely worth their time.

Here are some recent examples where I’ve used this pattern, including the opener I used:

-   [datasette PR #3052: Redesign row page as a vertical list of fields](https://github.com/simonw/datasette/pull/3052)—"The row page showed its single row as a one-row table. For wide tables, like a 46-column GitHub `repos` table, that scrolled far off to the right and left most of the page blank." (then a screenshot)
-   [datasette PR #3043: Pagination bar showing which rows are on the current page](https://github.com/simonw/datasette/pull/3043)—“Table pages that span more than one page now make it obvious where you are, and offer navigation at the top of the page as well as the bottom.” (plus screenshot)
-   [datasette PR #3042: Load edit-tools.js on demand via a small loader](https://github.com/simonw/datasette/pull/3042)—"`edit-tools.js` (~220KB) was loaded on every table, row and database page, even for users who couldn’t edit anything. Now only load it for users who can edit when they first interact with an edit feature (including mouse over an edit link)."
-   [datasette-agent PR #51: register\_agent\_reference\_types plugin hook](https://github.com/datasette/datasette-agent/pull/51)—"Lets plugins add their own kinds of item to the `#` tagging in the chat composer using a new `register_agent_reference_types(datasette)` plugin hook."—pictured above.
-   [llm PR #1838: Add llm openai endpoint add/list/remove/path commands](https://github.com/simonw/llm/pull/1838)—"Adds commands for managing the records in `extra-openai-models.yaml`, so OpenAI-compatible endpoints can be saved from the command line instead of by hand-editing YAML."—then copied `--help` output.

#### The mnemonic [#](https://simonwillison.net/2026/Nov/9/details-summary/#the-mnemonic)

I used to have trouble remembering the order of the tags—is it `<details><summary>` or `<summary><details>`?

Here are two tricks that helped me.

First, and most obviously, the `<summary>` is clearly the bit where you summarize the details. That’s the tag for your line of text that can be clicked to expand—the `<details>` element must then wrap everything else.

An even better trick is to always refer to these two tags as “details-summary”.

“details-summary” is two syllables followed by three syllables. That rolls off the tongue more smoothly than the three-two punch of “summary-details”.

Say “details-summary” out loud just a few times and you’ll never forget the order of the tags again.

(I still wish GitHub would add a button to their Markdown editor for this—partly to save me painstakingly typing it on my mobile keyboard, and partly to help spread the word to more GitHub users that this feature exists.)

Posted [9th November 2026](https://simonwillison.net/2026/Nov/9/) at 4:25 am · Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe)

## 中文要点

Simon Willison 介绍用 <details><summary> 折叠 AI 生成 PR 描述的工作流。他的 PR 大多由 Claude Code 或 Codex 开，描述「准确、完整却读起来像 slop」，连驱动作品的作者本人都不想读完。解法：手写一段人批准的引子说明 PR 做什么、值不值得花时间，agent 写的全文塞进折叠区，summary 直接标模型名与 effort（如 Claude Opus 5.5 Medium），读者一眼知道下面是谁写的。他立下规矩：开头引子代表本人判断，只写确实值得读者花时间的东西。实际例子包括 datasette #3052/#3043/#3042、datasette-agent #51、llm #1838。

## Field Notes

- 来源证据：AK-RSS Digest 2026-11-09（source/ 全文抓取，2026-11-09 20:16 Asia/Shanghai）
- 入库批次：daily-intake-evening 2026-11-09
