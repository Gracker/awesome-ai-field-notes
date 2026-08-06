# Atlassian Rovo Exfiltrates Data, Bypassing Controls

- **ID**: 06d0cdff
- **Original URL**: https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data
- **Author(s)**: PromptArmor
- **Date**: Unknown
- **Category**: agents
- **Source type**: article
- **Tags**: prompt-injection, data-exfiltration, rovo, agent-security, tool-permissions
- **Quality score**: 4/5
- **Fetched at**: 2026-08-06T15:43:42+00:00
- **Obsidian evidence**: OpenClaw定时任务/ClawFeed24小时高价值一览/2026-08-06-ClawFeed24小时高价值一览.md

---

## 中文导读

PromptArmor 披露 Atlassian Rovo 的间接 prompt injection 外泄链：攻击内容诱导 Rovo 把 Jira / Confluence 数据拼进攻击者控制 URL，再借“打开 URL”工具完成外泄。关键点是组织关闭 web search 并不等于移除所有外联工具，动态 URL 构造也需要权限与数据流约束。这条案例适合作为企业 agent 连接内部知识库时的默认威胁模型。

## 为什么值得关注

企业 agent 权限、工具外联和间接 prompt injection 的可复现案例。

## English Summary

PromptArmor describes an indirect prompt-injection chain where Atlassian Rovo can be manipulated into embedding Jira and Confluence data in attacker-controlled URLs and opening them, bypassing controls that only disable web search.

## 原文摘要 / Source Excerpt

# Atlassian Rovo Exfiltrates Data, Bypassing Controls
> 原文链接: https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data

---

![Atlassian Rovo AI exfiltrates data, bypassing controls: attacker logs contain Jira tickets and Confluence docs.](https://www.promptarmor.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fqbcmjtpr%2Fproduction%2Fbad3f6a2c8f1087ad9cdfbf1049fa6f293c65848-1558x1326.png&w=3840&q=75)

Atlassian Rovo AI exfiltrates data, bypassing controls: attacker logs contain Jira tickets and Confluence docs.

## Context

Atlassian’s Rovo AI is a multi-purpose agent that operates across Atlassian’s product suite (Jira, Confluence, etc.).

Vulnerabilities have been identified that enable data exfiltration across an Atlassian tenant (Jira tickets, Confluence docs, etc.) via indirect prompt injection. This attack executes without requiring any human-in-the-loop approval, and succeeds by exploiting Rovo's URL retrieval tool.

**This attack succeeds even if an organization has disabled web search for Rovo. This is because the web search setting fails to remove the tool for opening the search results.**

PromptArmor disclosed the vulnerabilities covered in this article to Atlassian on May 23rd. Atlassian assigned a case number and expressed thanks, but after multiple follow-ups by PromptArmor over more than two months, Atlassian has made no further communication, and Rovo remains vulnerable. As such, we are publishing to inform users of the risks.

## The Attack Chain

1.  1.

    **The victim prepares a query asking Rovo to organize Jira tickets**

    ![The victim enters a query into Rovo](https://www.promptarmor.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fqbcmjtpr%2Fproduction%2F98f8bb6bf826fe58e5c4f57bb8038eb6586d47fa-977x830.png&w=3840&q=75)

    The victim enters a query into Rovo

2.  2.

    **The victim uploads a file to Rovo that contains a hidden prompt injection**

    For general use cases, this is quite common: a user finds a file online and uploads it to Rovo. This attack is not dependent on the injection source - other injection sources include, but are not limited to: external data in Atlassian (e.g., support tickets), web data (if search is enabled), third-party ‘connectors’, etc.

    ![The 'Backlog Guide' document uploaded by the user contains a concealed prompt injection.](https://www.promptarmor.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fqbcmjtpr%2Fproduction%2F8914206adc067d8aaf6665e154a435574fb8987c-1496x1437.png&w=3840&q=75)

    The 'Backlog Guide' document uploaded by the user contains a concealed prompt injection.

3.  3.

    **The victim asks Rovo to organize their Jira tickets**

    ![Rovo processes the request and begins searching Jira and Confluence.](https://www.promptarmor.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fqbcmjtpr%2Fproduction%2F091e951706510e698b228ca8c619c025b9ffc3b3-978x797.png&w=3840&q=75)

    Rovo processes the request and begins searching Jira and Confluence.

4.  4.

    **The injection manipulates Rovo to submit Jira tickets and Confluence documents to the attacker’s website**

    Rovo's URL retrieval tool is insecure: **there are no protections against opening a URL that has been dynamically created by the agent**. Here, Rovo is manipulated to append sensitive data to an attacker's URL. When Rovo calls the insecure tool to open the URL, the attacker's site logs the request, including the appended sensitive data.

    ![Rovo is manipulated by the injection to submit Jira and Confluence data to the attacker's URL.](https://www.promptarmor.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fqbcmjtpr%2Fproduction%2Fad6796287de08da173efbed2488af7d8df716a2e-1186x963.png&w=3840&q=75)

    Rovo is manipulated by the injection to submit Jira and Confluence data to the attacker's URL.

    Note: This attack succeeds even if an organization has disabled web search for Rovo. This is because the web search setting fails to remove the tool for opening the search results.

    ![The organization-wide 'Enable web search' setting for Rovo is toggled off.](https://www.promptarmor.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fqbcmjtpr%2Fproduction%2F57d408835d430ad7ae4b164e5e18dcb813bd9dd2-1002x132.png&w=3840&q=75)

    The organization-wide 'Enable web search' setting for Rovo is toggled off.

    If the user returns to the chat later, they see the agent's suggested ticket updates, but no evid

...[excerpt truncated, fetched body length=8754 chars]...
