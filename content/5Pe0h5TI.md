# AI编程蓝皮书2.0

> 原文链接: https://superhuang.feishu.cn/wiki/CBBPwvgEuicVhFkx0s7cPmhpn4e

---
header-v2

Super黄和他的朋友们

AI编程蓝皮书2.0

Last updated: Apr 22

Log In or Sign Up

-   [AI编程蓝皮书2.0](#SfQadlBHRogYNBxXJiEcqIDEnbg)
-   [全文知识目录](#Bx5Jd2WUDoglCtxye0gcyWKxnT2)
-   [Part1：基础知识](#MXARdMTT5olvzlxZorlcdRbAnXg)
-   [01 Windsurf做的产品](#NwGEdXD51oSQvhxycIocauJGneh)
-   [02 AI编程构成了双杠杆的重要一环](#ZkrhdaRwsoLvVkxcdLxcGZnin9b)
-   [03 不管黑猫白猫，做出产品就是好猫](#Diovdbq95o6q6TxOOkvcoPgPnFd)
-   [04 Windsurf，不是Cursor？](#SbAbdWJXDoVvqEx0bGycL0Nan6e)
-   [05 Trae可免费使用Claude 3.7](#DvWLd7XfBo4B58x2UTTcqMZon3c)
-   [06 必备的Windsurf技巧](#ZN0rdIUiroTXt1xXNXicvdEanRf)
-   [第一，开始的开始，是先下载软件](#DfkbdWCiyoZULSxXrRAcbjaPnzb)
-   [第二，在你的电脑上，新建个文件夹，并用Windsurf打开](#EzdRdS4xDoFHaBxhubAcCDj5nDb)
-   [第三，让AI更听话：Set Global AI Rules](#Je1Rdby1vonH2DxA5nycuKL1nFc)
-   [第四，安装中文插件](#NSqZdtlBDoo3ccxSC3UcdX4YnRp)
-   [07 一些AI编程的心得](#YufDd0vrgoYoxBxYpVrcY2Ahnib)
-   [你写的越慢，你写的越快](#SKeodxqFgo7G7Sx1ABXcpZPHnSh)
-   [Part2：使用AI IDE作为你的个人工作台](#WZH1d1UMPoJ3Y2xUlG4cUvknnwg)
-   [01 使用AI IDE进行创作](#SOSbdLuBzo6ntfxpPCaciqEPnCg)
-   [改写提示词](#RMxednuJQovUU2xkda6cTHZ9nug)
-   [02 使用提示词生成精美图片](#Edyzdt122oKoNwxt0t6cdCvMn9f)
-   [最终版本的提示词](#DEdGdjdoCoPXOdxpZDOcSQGVnNf)
-   [03 10分钟搞定高德地图MCP！我用AI解决了约会地点选择难题](#DfY4d3uoloSFUFxqt5gcocpcnLc)
-   [第一步：给Windsurf安装高德MCP](#N1wGdtmE2oDRXWxSFbacx9uAnXr)
-   [第二步：开始说出你的需求](#F26mdLwEaoQURXxUR3rcLuN8n9e)
-   [MCP解决了什么问题？](#L0hbdxnUnoRSArxATUWcyFOTn0g)
-   [Part3：网页开发](#Lu0JdSJ8Som4rYxvcMJcce6znkg)
-   [01 图片字幕生成器](#SsHTdiXXQok0T0xFb4ocUWjznZg)
-   [用多模态复刻产品](#IWIfdsR5OoQixfxuqbeceEYdnwb)
-   [课后练习](#EOwFdZu6IoCcU1xJtYxcxA2Jn3g)
-   [02 注册硅基流动，获赠4000万Token](#LTCldtlfqoTR47xeNrocqgTqn0c)
-   [03 使用Deepseek R1，帮老外起中文名吧！](#EpPNdVA0aoqHpjxywCCcBggznud)
-   [第一，本地新建一个文件夹](#DV0XdPPoToLKCMxlibUcSsR7nUg)
-   [第二，使用Windsurf打开它](#KvPJdCadcoyjkixH26tchOa3nzc)
-   [第三，设置WorkSpace AI Rules](#BUkBdyCwWocVf7xnKgHcuWlznNe)
-   [第四，接入大模型](#PkfydRT0LowUAkxxq8RcqZemnXI)
-   [第五，检查开发完成的网页产品](#EtandHZC4ovgiZxHlqkcXIwknGd)
-   [进阶1：优化名字生成质量](#Y6VUdoMxKo4EWWxnch7cvoYGnPb)
-   [进阶2：优化页面](#XJUydIIOmoH06Dxq3e4colPknMg)
-   [课后练习：](#IuyzdpFt8osrRVxKfHRcZmGJnIe)
-   [小结](#I5Ykdr1aMow5XZxdxqRcF1G3n1g)
-   [04 做一档你自己的AI播客](#OR7BdX4wGo8dOKxfsLgcqSvtnxg)

#

AI编程蓝皮书2.0​

Modified April 22

大家好，我是AI产品黄叔，目前给两家大厂做AI产品顾问，在使用Cursor和Windsurf（这两个都是AI编程的软件）开发产品后，意识到这才是创造者的天堂，最近举办了多场线下AI编程培训，根据学员的反馈有了这份手册，我会在本手册里持续更新，不断把更多的技巧，思考分享出来，希望能够帮助想要创造的你走进这个天堂！如果你觉得有帮助，欢迎分享给你的朋友。​

​

​

🏝️

特别感谢 @Orange.ai 和 @歸藏 两位老师对AI编程蓝皮书的支持与分享。​

你们的助力让更多渴望创造的朋友能够接触到AI编程的魅力。​

（如果更多的朋友也愿意推广/参与优化，欢迎拉到文末添加我）​

​

​

🌅

@唯庸 和@杜昭 也有不少贡献，一并感谢！​

​

​

12月28日更新：​

黄叔和风变科技合作办了个AI编程社团，持续运营三个多月，现在已经很成熟了，每周五直播，双月办黑客松，每周邀请系列嘉宾做分享（AI编程技巧+如何搞钱）持续了6周，可开发票，课程内容也更加体系化和全面（包括数据库、域名、支付接入、最新模型能力和接入、出海产品等等），最近大量更新Claude Agent Skills相关玩法，能帮助大家把各类场景用AI完成SOP自动化操作。欢迎大家感兴趣的话加入，已经有1000多位同路人：​

（当前福利：赠送1月 Youmind Pro会员+ 1月 YouWare Pro会员）​

​

Unable to print

![Feishu Docs - Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/ObVBbbQw6o4QNtxLNesc5Y0Nn7d/?fallback_source=1&height=1280&mount_node_token=QZgAdo4oeoeRezxGDycclxfAnwb&mount_point=docx_image&policy=equal&width=1280)

​

Comments (60)

Go to the first comment

0 words