---
title: '最近爆火的MCP究竟有多大魅力？MCP开发初体验｜得物技术'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# 最近爆火的MCP究竟有多大魅力？MCP开发初体验｜得物技术

> Cubox 收藏 — 最近爆火的MCP究竟有多大魅力？MCP开发初体验｜得物技术

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247539225&idx=1&sn=811dee1e2b17f5b1249d14f19b69f171&chksm=c0410dd7305597ba3c7f3dc6d1f7ee85808d38011bd376b42cace90a0fbc6c687a1be00c888f&mpshare=1&scene=1&srcid=0507se7oCab5JJoikWmzE8I5&sharer_shareinfo=634900176f4a7a250585116a09ea6b5f&sharer_shareinfo_first=634900176f4a7a250585116a09ea6b5f) | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

---

# 最近爆火的MCP究竟有多大魅力？MCP开发初体验｜得物技术

## English

# 最近爆火的MCP究竟有多大魅力？MCP开发初体验｜得物技术

> 公众号: 得物技术
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247539225&idx=1&sn=811dee1e2b17f5b1249d14f19b69f171&chksm=c0410dd7305597ba3c7f3dc6d1f7ee85808d38011bd376b42cace90a0fbc6c687a1be00c888f&mpshare=1&scene=1&srcid=0507se7oCab5JJoikWmzE8I5&sharer_shareinfo=634900176f4a7a250585116a09ea6b5f&sharer_shareinfo_first=634900176f4a7a250585116a09ea6b5f

---
![Image](images/img_001.gif)

**目录**

一、前言

二、MCP 基础架构

    1. 基础架构

    2. 工作流程

三、MCP Server 开发&实践

    1. 准备 MCP Client

    2. 开发 MCP  Server

    3. 配置 MCP Server

    4. 开始体验

    5. 进阶体验

    6. 联想一下

四、总结

**一**

**前言**

MCP 全称 Model Context Protocol，是由 Anthropic 公司在 2024 年 11 月推出一个开放协议，主要用于标准化应用程序向大语言模型提供上下文的方式。可以将 MCP 想象成 AI 应用程序的 USB-C 接口。就像 USB-C 为设备连接各种外设和配件提供了标准化方式一样，MCP 为 AI 模型连接不同的数据源和工具提供了标准化方式。

![Image](images/img_002.png)

近期 MCP 的热度持续上升，网上也是喷涌出大量相关文章，相信在不远的将来 MCP 将成为每个开发者必备的技能之一，非常值得投入时间学习一下。下面会通过简单的实践来带大家理解一下 MCP 的工作原理，以及展望下 MCP 在未来可能的一些应用场景。

**二**

**MCP 基础架构**

**基础架构**

在开始实践之前，还是简单介绍一下 MCP 的基本架构和一些基础组件：

![Image](images/img_003.jpeg)

-   **MCP Host**：需要通过MCP访问数据的程序，例如 Claude Desktop、Cursor、Cline等桌面工具。

    主要职责：接受&返回你的提问、跟模型交互、内置了 MCP Client，与服务器保持一对一连接的协议客户端。


-   **MCP Server**：轻量级程序，每个程序都通过标准化的模型上下文协议 （MCP） 提供特定功能。

    主要职责：能力暴露（操作本地文件&浏览器，访问数据库，访问远程服务）。

-   **本地数据源**：MCP 服务器可以安全访问的数据库、本地文件、浏览器等。

-   **远程服务**：MCP 服务器可以通过互联网（例如通过 API）连接到的外部系统。


**工作流程**

从用户提问，到最终完成任务的完整流程可参考下图：

![Image](images/img_004.png)

百闻不如一见，百见不如一练。下面我们手把手开发一个 MCP Server，并且通过 Cline 来使用它，实践过程中会容易帮助我们去理解 MCP。

**三**

**MCP Server 开发&实践**

**准备MCP Client**

这里我用的是 Cline，是 VSCode 中的一个插件，直接在 VSCode 插件市场中搜索安装即可，其实这里的 Cline 在 MCP 的概念中是 MCP Host，只是 Host 里面内置了 MCP Client（负责跟模型&MCP Server 交互）。

_其实更推荐使用 Claude，但是 Claude注册流程相对复杂一点，对网络环境要求也更高（需要科学上网）。_

![Image](images/img_005.png)

安装好后，第一步就是需要配置大模型，这里我选择的是 DeepSeek。

_需要自行购买 API Key（https://platform.deepseek.com/api\_keys）_

![Image](images/img_006.png)

然后就可以开始配置 MCP server 了，点击右上角的第二个图标。

![Image](images/img_007.png)

这里可以使用开源的 MCP Server，也可以使用自己开发的 MCP Server，下面我们尝试自己动手开发一个简单的 MCP Server。

**开发MCP Server**

想要开发一个 MCP Server，并不需要关心协议本身的一些细节，因为官方推出了各种语言的 SDK_（https://modelcontextprotocol.io/sdk/java/mcp-server）_，通过 SDK 可以快速搭建一个 MCP Server，并且主流语言都针对 MCP 推出了自己的框架，Java 也不例外，这里我们选择使用 Spring 框架来搭建一个 MCP Server_（https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html）。_

**引入依赖**


```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webmvc</artifactId>
</dependency>
```


**定义 Tools**

这里我们定义一个发送飞书消息的工具类：


```kotlin
import org.springframework.ai.tool.annotation.Tool;
import org.springframework.ai.tool.annotation.ToolParam;
import org.springframework.stereotype.Service;
import com.lark.oapi.Client;
import com.lark.oapi.core.cache.LocalCache;
import com.lark.oapi.core.enums.AppType;
import com.lark.oapi.service.im.v1.enums.MsgTypeEnum;
import com.lark.oapi.service.im.v1.enums.ReceiveIdTypeEnum;
import com.lark.oapi.service.im.v1.model.CreateMessageReq;
import com.lark.oapi.service.im.v1.model.CreateMessageReqBody;
import com.lark.oapi.service.im.v1.model.CreateMessageResp;
import java.util.concurrent.TimeUnit;
/**
 * @author xinyi
 */
@Service
public class LarkService {
    private final Client larkClient = feishuClient();
    public Client feishuClient() {
        return Client.newBuilder(System.getenv("larkAppId"),
                  System.getenv("larkAppSecret")).appType(AppType.SELF_BUILT) // 设置app类型，默认为自建
                .tokenCache(LocalCache.getInstance()) // 设置token缓存，默认为内存缓存
                .requestTimeout(10, TimeUnit.SECONDS) // 设置httpclient 超时时间，默认永不超时
                .logReqAtDebug(false)
                .build();
    }
    @Tool(description = "用飞书给用户发消息")
    public String sendLarkCardMessage(@ToolParam(description = "接收人邮箱") String receiveEmail,
                                      @ToolParam(description = "飞书卡片内容（参考飞书文档要求的结构体）") String cardContent) throws Exception {
        CreateMessageReq req = CreateMessageReq.newBuilder().receiveIdType(ReceiveIdTypeEnum.EMAIL.getValue())
                .createMessageReqBody(CreateMessageReqBody.newBuilder()
                        .receiveId(receiveEmail)
                        .msgType(MsgTypeEnum.MSG_TYPE_INTERACTIVE.getValue())
                        .content(cardContent)
                        .build())
                .build();
        CreateMessageResp resp = larkClient.im().message().create(req);
        return resp.getMsg();
    }
}
```


这里 Spring 会自动把@Tools 注解的方法按照 MCP 标准暴露出来，大模型会根据其中的描述来决策是否可以调用此方法。

**启动类**


```typescript
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
@SpringBootApplication
public class McpServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    @Bean
    public ToolCallbackProvider weatherTools(LarkService larkService) {
        return MethodToolCallbackProvider.builder().toolObjects(larkService).build();
    }
}
```


**打包**

到这里一个简单的 MCP Server 就已经开发完成了，下面只需要执行 mvn clean package 打成可执行 jar 包就能配置到 Cline 中了。

![Image](images/img_008.png)

**配置MCP Server**

回到 VSCode 的 Cline 插件，点击第二个图标，然后点击下面的 Configure MCP Servers，然后开始编辑右侧的配置文件：

![Image](images/img_009.png)

这里的配置文件是 MCP 标准化的，下面基于我们这个 MCP Server 介绍下几个核心配置的含义：


```json
 "mcpServers": {
      "lark": {
        "disabled": false,
        "timeout": 60,
        "command": "/Users/admin/Documents/jdk-17.jdk/Contents/Home/bin/java",
        "args": [
          "-Dspring.ai.mcp.server.stdio=true",
          "-Dspring.main.web-application-type=none",
          "-Dlogging.pattern.console=",
          "-jar",
          "/Users/admin/Documents/git/open-source/spring-ai-mcp-server-demo/target/spring-ai-mcp-server-demo-1.0-SNAPSHOT.jar"
        ],
        "env": {
          "larkAppId": "xxx",
          "larkAppSecret": "xxx"
        },
        "autoApprove": [
          "sendLarkCardMessage"
        ],
        "transportType": "stdio"
      },
```


-   mcpServers：JSON 配置跟 Key

-   lark：MCP Server 唯一标识&名称

-   command：启动 MCP Server 的命令（如 Java 就是 java -jar，Node 一般是 npx，Python 一般是 uvx）

-   args：执行命令后面的自定义参数

-   env：环境变量，用于配置一些可配置参数，比如密钥、外部 URL 等


这里配置好了后，如果右上角的点变成了绿色说明 MCP Server 加载成功，而且在下面还可以看到 MCP Server 提供的所有 Tools，以及每个 Tool 的参数跟描述。

![Image](images/img_010.png)

**开始体验**

点击右上角的+号开始聊天：**给我发一条下午好的飞书卡片消息，附带一下今日的热点新闻。**

![Image](images/img_011.png)

可以看到 Cline 调用了大模型开始思考，并且根据 MCP Server 提供的 Tools 开始选择发送消息接口并执行。

![Image](images/img_012.png)

而且如果第一次尝试失败，还会自动纠错，最后成功调用了我们 MCP Server 提供的 Tools，发送了一条消息给我。

![Image](images/img_013.png)

![Image](images/img_014.png)

**进阶体验**

上面的例子我们只用到了一个 Tools，我们可以尝试组合多个 Tools&多个 MCP Server 来实现更复杂的任务，比如我们现在再开发一个可以操作 ES 的 MCP Server，然后打包后配置到 Cline 中。


```python
@Tool(description = """
        通用ES查询工具，参数示例：
        path: 请求路径
        method: HTTP请求方法 GET 或 POST
        queryJson: 具体请求体
        """)
public String searchByQuery(
        String path,
        String method,
        String queryJson) {
    String url = String.format("%s/%s", System.getEnv("esBaseUrl"), path);
    HttpEntity<String> request = buildEsRequest(queryJson);
    ResponseEntity<String> response = restTemplate.exchange(
            url, HttpMethod.valueOf(method), request, String.class);
    return response.getBody();
}
```


配置好后，在对话中发送：**分析一下 es 集群目前的索引分布，重点分析一下哪些索引的分片设置不合理，最终整理后飞书发给我。**

![Image](images/img_015.png)

然后会根据请求 ES 返回的结果，再次吐给模型进行分析。

![Image](images/img_016.png)

最终整理后通过飞书发送一份简单报告。

![Image](images/img_017.jpeg)

**联想一下**

想象一下，如果组合一下飞书文档、浏览器操作、文件系统、发布系统对接等 MCP Server，一句话就可以让大模型从自动连接浏览器，打开飞书文档，分析需求，分析视觉稿，然后自己写代码，对比视觉稿，你就喝杯咖啡，静静的看着它工作。

顺带推荐一下常用的 MCP Client 以及一些现成的 MCP Server。

-   MCP Client List：


-   https://modelcontextprotocol.io/clients


-   MCP Server List：


-   https://github.com/modelcontextprotocol/servers

-   https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-zh.md


**四**

**总结**

相信大家通过上面的实践后，对 MCP 有了一个基本的认识，组合多个 MCP Server 的工作流可以自主完成非常复杂的任务，关键是这协议统一了连接标准，有大量现成的 MCP Server 可以即插即用，大幅降低建设成本。总之 MCP 协议的持续落地，让 AI 不再只是聊天工具，而是工业智能革命的万能操作平台，在未来潜力无限，想象无限，值得每一位开发者去学习并掌握它！

**往期回顾**

1. [得物可观测平台架构升级：基于GreptimeDB的全新监控体系实践](https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247539175&idx=1&sn=6dc5659dc94a0bc356dddf69df69a83b&scene=21#wechat_redirect)

2. [得物业务参数配置中心架构综述](https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247539161&idx=1&sn=7affe5c5e39fe81bc33fb31a75333ba6&scene=21#wechat_redirect)

3. [得物增长兑换商城的构架演进](https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247539092&idx=1&sn=6fc02ccebc5c838f143d5128691a635b&scene=21#wechat_redirect)

4. [得物自研DGraph4.0推荐核心引擎升级之路](https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247539014&idx=1&sn=90a168b730490ae84a0917863ad3e077&scene=21#wechat_redirect)

5. [大语言模型的训练后量化算法综述 | 得物技术](https://mp.weixin.qq.com/s?__biz=MzkxNTE3ODU0NA==&mid=2247538986&idx=1&sn=b6b82a790a3c696bce27704472e799b2&scene=21#wechat_redirect)

文 / 新一

关注得物技术，每周一、三更新技术干货

要是觉得文章对你有帮助的话，欢迎评论转发点赞～

未经得物技术许可严禁转载，否则依法追究法律责任。

“

**扫码添加小助手微信**

如有任何疑问，或想要了解更多技术资讯，请添加小助手微信：

![Image](images/img_018.jpeg)

## 中文

[翻译失败，原文保留]

*Generated as part of AI Field Notes automated content fetching process*
