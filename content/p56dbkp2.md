# Pick up exactly where you left off with Session Management in Gemini CLI

> 原文链接: https://developers.googleblog.com/pick-up-exactly-where-you-left-off-with-session-management-in-gemini-cli/

---

## 背景

Context is everything when working with Gemini CLI. Whether you are refactoring a complex codebase or debugging a tricky error, your conversation history contains valuable reasoning, tool outputs, and decisions.

Previously, closing your terminal meant losing that context. Starting over required re-explaining the problem to the model. This is no longer the case, Gemini CLI now automatically saves your sessions and lets you search through your session history to resume right where you left off!

## Automatic Saving: Peace of mind

Every time you interact with Gemini CLI, your session is now automatically saved in the background. You don't need to remember to save or export your chat; we handle it for you with our new Session Management system.

We capture the complete state of your work, including:

- Your prompts and the model's responses.
- All tool executions (inputs and outputs).
- Token usage statistics.
- Assistant thoughts and reasoning summaries.

Crucially, these sessions are project-specific. If you switch directories to a different project, Gemini CLI automatically switches context to that project's session history, ensuring Gemini CLI is always on the same page as you.

## Resuming Sessions

We have made it incredibly easy to jump back into a previous workflow, whether you prefer command-line flags or our interactive UI.

### The Interactive Session Browser

Within Gemini CLI, you can simply type `/resume` to open the new Session Browser.

This interactive interface allows you to:

- **Browse**: Scroll through a chronologically sorted list of your past sessions.
- **Preview**: See details like message counts and 1-line summary to identify the right chat.
- **Search**: Press `/` to filter sessions by ID or content keywords.
- **Select**: Press Enter to instantly restore the full context of that conversation.

### Command Line Power

For those who prefer flags, you can resume sessions right from the start when you launch Gemini CLI.

- **Resume latest**: `gemini --resume` will immediately load your most recent session.
- **Resume specific session**: `gemini --resume 5` (by index) or `gemini --resume` (by session ID).

You can list all available sessions for your current project as well:

```bash
gemini --list-sessions
```

Output example:

```
Available sessions for this project (3):

1. Fix bug in auth (2 days ago) [a1b2c3d4]
2. Refactor database schema (5 hours ago) [e5f67890]
3. Update documentation (Just now) [abcd1234]
```

## Managing your History

With great power comes great responsibility… or in this case, a lot of history files! We've added the tools to help you keep your environment clean.

To prevent your history from growing indefinitely, you can enable automatic cleanup policies in your `settings.json` configuration file.

```json
{
  "general": {
    "sessionRetention": {
      "enabled": true,
      "maxAge": "30d", // Keep sessions for 30 days
      "maxCount": 50 // Keep the 50 most recent sessions
    }
  }
}
```

## Tracking your Gemini CLI usage

With detailed message, thought, tool call, and token usage information being recorded automatically, you can now analyze your Gemini CLI usage. You can use community developed tools like [Splitrail](https://github.com/Piebald-AI/splitrail), or develop your own!

## Get started today

Session management is available in Gemini CLI and on by default as of v0.20.0+.

All you need to do is update to make sure you can take advantage of the new feature:

```bash
npm install -g @google/gemini-cli@latest
```

Make sure to check out our [official documentation on session management](https://geminicli.com/docs/cli/session-management/) for further details.

You can also follow [Gemini CLI on X](https://x.com/geminicli) to stay up to date with the latest news and announcements.
