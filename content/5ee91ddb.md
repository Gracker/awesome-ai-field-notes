---
id: 5ee91ddb
title: "Fixing an NZXT Signal 4K30 part 2: the green/pink video bug"
authors: "Doug Brown"
original_date: 2026-09-13
url: https://www.downtowndougbrown.com/2026/09/fixing-an-nzxt-signal-4k30-part-2-the-green-pink-video-bug/
source: blog
tags: [reverse-engineering claude-as-subagent hardware-bug firmware]
---

# Fixing an NZXT Signal 4K30 part 2: the green/pink video bug

> Source: [https://www.downtowndougbrown.com/2026/09/fixing-an-nzxt-signal-4k30-part-2-the-green-pink-video-bug/](https://www.downtowndougbrown.com/2026/09/fixing-an-nzxt-signal-4k30-part-2-the-green-pink-video-bug/) · platform: blog · authors: Doug Brown · date: 2026-09-13

## TL;DR（中文摘要）

Doug Brown 用 Claude 逆向分析停产采集卡 NZXT Signal 4K30 的 DVI 绿粉画面 bug：问题出在 ITE IT6805 HDMI 接收器参考驱动里寄存器 0x6B 颜色模式赋值——作者把「00: RGB」误读成「01: RGB」，导致 DVI 分支写错值。他让 Claude 逆向 NZXT 固件升级器、找到 MCU 固件没做 checksum 的位置，做一次性 patch 工具把 movs r2, #16 改成 movs r2, #0，烧写后颜色恢复。范本意义：没让 LLM 越界做 hardware exploit，只把它当 subagent 跑结构化反向分析——agent 时代硬件 hobbyist 用模型的正确姿势。

## Summary (English)

Doug Brown uses Claude to reverse-engineer a green/pink DVI capture bug on the discontinued NZXT Signal 4K30: an ITE IT6805 reference-driver misread of register 0x6B color-mode bits, plus an unchecksummed MCU firmware. A one-shot patch tool flips movs r2, #16 to movs r2, #0 and the colors are fixed - a template for using LLMs as structured reverse-engineering subagents without crossing into exploit territory.

## 入库依据（同日 digest 交叉验证）

AK-RSS 2026-09-16 第 8 条；原文全文抓取核实（IT6805、寄存器 0x6B、patch 细节均在文中）。

