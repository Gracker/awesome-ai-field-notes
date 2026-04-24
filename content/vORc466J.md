# 保姆级教程：利用大模型与高德地图API，轻松实现查找附近咖啡店

> 来源：微信公众号「智能体AI」
> 原文链接：https://mp.weixin.qq.com/s/UMFpj2ysGyHiaxvdPfehAQ

随着人工智能和地图服务的迅速发展，我们可以轻松地利用这些工具实现各种便捷功能。例如，通过整合OpenAI的大模型和高德地图API，可以快速查找某个地址附近的咖啡店。本文将介绍如何通过远程调用和多功能调用大模型，结合高德地图API，实现这一功能，并分享具体的代码示例。

## 一、步骤解析

1. **用户查询** — 用户向ChatBot提出查询请求，例如"长沙证券大厦附近的咖啡店"。
2. **解析用户请求** — ChatBot（通过OpenAI API）解析用户的请求内容，理解用户想要查询的地点和兴趣点。
3. **调用高德地图API获取地理坐标** — ChatBot调用高德地图API，使用 `get_location_coordinate` 函数获取用户查询地点的地理坐标（经纬度）。
4. **高德地图API返回地理坐标** — 高德地图API返回查询地点的地理坐标信息（例如经度和纬度）。
5. **解析地理坐标** — ChatBot解析从高德地图API返回的地理坐标，为后续查询做好准备。
6. **调用高德地图API搜索附近兴趣点** — ChatBot调用高德地图API，使用 `search_nearby_pois` 函数，根据获取的地理坐标和用户提供的关键词（如"咖啡"），搜索附近的兴趣点（POIs）。
7. **高德地图API返回附近兴趣点** — 高德地图API返回查询坐标附近的兴趣点信息，包括咖啡店的名称、地址和距离等。
8. **整理并生成回复内容** — ChatBot整理高德地图API返回的兴趣点信息，并生成用户所需的回复内容。
9. **返回结果给用户** — ChatBot将生成的回复内容返回给用户，展示附近的咖啡店信息。
10. **用户继续对话或结束** — 用户可以根据返回的信息继续进行对话，提出更多查询或结束对话。

## 二、完整代码

```python
import openai
import os
import json
import requests
import logging
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = os.getenv('OPENAI_API_URL')
model = os.getenv('MODEL')
amap_key = os.getenv('GAODE_MAP_API_KEY')


def get_location_coordinate(location, city="长沙"):
    """根据地点和城市名称，使用高德地图API查询并返回该地点的坐标。"""
    url = f"https://restapi.amap.com/v5/place/text?key={amap_key}&keywords={location}&region={city}"
    r = requests.get(url)
    result = r.json()
    if "pois" in result and result["pois"]:
        return result["pois"][0]
    return None


def search_nearby_pois(longitude, latitude, keyword):
    """根据给定的经纬度和关键词，使用高德地图API查询并返回附近的兴趣点信息。"""
    url = f"https://restapi.amap.com/v5/place/around?key={amap_key}&keywords={keyword}&location={longitude},{latitude}"
    r = requests.get(url)
    result = r.json()
    ans = ""
    if "pois" in result and result["pois"]:
        for i in range(min(3, len(result["pois"]))):
            name = result["pois"][i]["name"]
            address = result["pois"][i]["address"]
            distance = result["pois"][i]["distance"]
            ans += f"{name}\n{address}\n距离：{distance}米\n\n"
    return ans


def get_completion(messages, model=model):
    """根据输入的消息列表，使用OpenAI API生成并返回聊天对话的回复。"""
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        seed=1024,
        tool_choice="auto",
        tools=[{
            "type": "function",
            "function": {
                "name": "get_location_coordinate",
                "description": "根据POI名称，获得POI的经纬度坐标",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "POI名称，必须是中文"},
                        "city": {"type": "string", "description": "POI所在的城市名，必须是中文"},
                    },
                    "required": ["location", "city"],
                }
            }
        }, {
            "type": "function",
            "function": {
                "name": "search_nearby_pois",
                "description": "搜索给定坐标附近的poi",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "longitude": {"type": "string", "description": "中心点的经度"},
                        "latitude": {"type": "string", "description": "中心点的纬度"},
                        "keyword": {"type": "string", "description": "目标poi的关键字"},
                    },
                    "required": ["longitude", "latitude", "keyword"],
                }
            }
        }],
    )
    return response.choices[0].message


def handle_tool_call(response, messages):
    """处理聊天对话中的工具函数调用。"""
    if response.tool_calls is not None:
        for tool_call in response.tool_calls:
            try:
                args = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError:
                logging.error("解析工具函数参数失败")
                continue
            logging.info(f"调用: {tool_call.function.name}")
            try:
                if tool_call.function.name == "get_location_coordinate":
                    result = get_location_coordinate(**args)
                elif tool_call.function.name == "search_nearby_pois":
                    result = search_nearby_pois(**args)
            except Exception as e:
                logging.error(f"调用 {tool_call.function.name} 出错: {e}")
                continue
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": tool_call.function.name,
                "content": str(result)
            })


def test_prompt():
    """测试聊天助手的功能，模拟用户查询长沙证券大厦附近的咖啡店。"""
    prompt = "长沙证券大厦附近的咖啡"
    messages = [
        {"role": "system", "content": "你是一个地图通，你可以找到任何地址。"},
        {"role": "user", "content": prompt}
    ]
    response = get_completion(messages)
    if response.content is None:
        response.content = "null"
    messages.append(response)

    while True:
        handle_tool_call(response, messages)
        response = get_completion(messages)
        if response.content is None:
            response.content = "null"
            messages.append(response)
        if not hasattr(response, 'tool_calls'):
            break

    print("=====最终回复=====")
    print(response.content)


if __name__ == '__main__':
    test_prompt()
```

## 三、输出示例

查询"长沙证券大厦附近的咖啡"，系统返回：

1. **luckin coffee 瑞幸咖啡(步步高生活广场店)** — 车站北路王府步步高生活商场1层1048号，距离约178米。
2. **咖啡因(车站路店)** — 车站北路170号瑞丰家园111门面，距离约356米。
3. **Wheat Espresso小麦咖啡(梦泽园商务楼店)** — 晚报大道63号梦泽园商务楼，距离约417米。

## 结语

通过本文介绍的方法和代码示例，我们可以轻松地结合OpenAI的大模型和高德地图API，实现查找某个地址附近咖啡店的功能。这不仅可以提升开发效率，也为我们提供了强大的工具来应对各种实际需求。
