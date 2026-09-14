# Fable 5.1 solves Sir Thomas Urquhart's Cyphral Distich, a 370-year-old cipher

> Source: https://www.vals.ai/blogs/fable-solves-cyphral-distich
> Author: Vals AI Team
> Published: 2026-09-13
> Platform: blog

## 中文概要

Vals 团队让 Claude Fable 5.1 在零干预下解 370 年悬而未决的 Cyphral Distich（Urquhart 的 Logopandecteision 末尾由两行共 64 个数字组成的密码）该谜题 1899 年由 Notes and Queries 公开登载，被密码学史家 Klaus Schmeh 列入 Top 50 未解密文，此前所有频率分析替换同音替换尝试均失败Fable 用了 44 分钟176k tokens 解出，突破口是 Urquhart 把密文紧接在 32 个 Proquiritations 之后并强调数字 32，加上诗中承诺诚实读者能在其中找到自己的心愿与作者的心意解码后的明文正是这 32 条 Proquirtation，每条长度恰好 32 个字符，对齐到 32 的笛卡尔积产生 64 个数字这是 LLM 自主完成开放密码学推理的实证样本，区别于已有基准的结构化子任务

## English Summary

Vals AI gave Claude Fable 5.1 an open task: solve the Cyphral Distich, a 370-year-old cryptogram appended to Sir Thomas Urquhart's Logopandecteision (two lines of 32 numbers). It was posed in Notes and Queries in 1899 and remains on Klaus Schmeh's Top-50 unsolved list; prior attempts via frequency analysis, substitution, and homophonic substitution all failed. After 44 minutes and 176k tokens with zero human interjection, Fable produced the solution using two insights: (1) Urquhart emphasises the number 32 because the 32 Proquiritations precede the cipher, and (2) the accompanying poem promises an honest reader will find 'his owne hearts wishes, and the Authors minde'. Decoding reveals the 32 Proquiritations, each exactly 32 characters long their Cartesian product over length-32 slots generates the 64 numbers....
