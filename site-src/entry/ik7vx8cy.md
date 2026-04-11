---
title: '该项目在github上：https://github.com/OminousIndustries/PhoneDriver'
sidebar: false
---

::: info
[← 返回模型](/models)
:::

# 该项目在github上：https://github.com/OminousIndustries/PhoneDriver

> AI 实践：该项目在github上：https://github.com/OminousIn

🔗 [原文链接](https://github.com/OminousIndustries/PhoneDriver) | @DLKFZWilliam2 |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`agent` `qwen` `phone-ai` `automation` `github`

---

# PhoneDriver: 使用 Qwen3-VL 的 Android 手机控制

## English
A Python-based mobile automation agent that uses Qwen3-VL vision-language models to understand and interact with Android devices through visual analysis and ADB commands.

 /OminousIndustries/PhoneDriver/blob/main/Images/PhoneDriver.png

- 🤖 Vision-powered automation: Uses Qwen3-VL to visually understand phone screens

- 📱 ADB integration: Controls Android devices via ADB commands

- 🎯 Natural language tasks: Describe what you want in plain English

- 🖥️ Web UI: Built-in Gradio interface for easy control

- 📊 Real-time feedback: Live screenshots and execution logs

- Python 3.10+

- Android device with USB debugging & Developer Mode enabled

- ADB (Android Debug Bridge) installed

- GPU with sufficient VRAM (Tested on 24gb GPU with Qwen3-VL-8B Model)

- The Repo is set to use the Dense Qwen3-VL 4B/8B Model which performs very well. To swap to an MoE model, see the configuration section below

Linux/Ubuntu:

sudo apt update
sudo apt install adb

git clone https://github.com/OminousIndustries/PhoneDriver.git
cd PhoneDriver

Create a Virtual Enviornment

python -m venv phonedriver
source phonedriver/bin/activate

Install Python Deps

pip install git+https://github.com/huggingface/transformers
# pip install transformers==4.57.0 # currently, V4.57.0 is not released

# Install other requirements
pip install pillow gradio qwen_vl_utils requests

- Enable USB debugging on your Android device (Settings → Developer Options)

- Connect via USB

- Verify connection:

adb devices

You should see your device listed.

Edit qwen_vl_agent.py to choose your model:

# For 4B model
model_name: str = "Qwen/Qwen3-VL-4B-Instruct"

# For 8B model
#model_name: str = "Qwen/Qwen3-VL-8B-Instruct"

#from transformers import Qwen3VLForConditionalGeneration, AutoProcessor - Comment this import out, it is for the Dense models
# Uncomment the import below for the MoE Variants!!!
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor

You will also need to change line 61:

 self.model = Qwen3VLForConditionalGeneration.from_pretrained(

Change it to:

 self.model = Qwen3VLMoeForConditionalGeneration.from_pretrained(

The agent can auto-detect your device resolution from the Web UI settings tab, but you can manually configure it in config.json.

{
 "screen_width": 1080,
 "screen_height": 2340,
 ...
}

To get your device resolution, with the device connected to your computer type the following in the terminal:

adb shell wm size

Launch the Gradio interface:

python ui.py

Navigate to http://localhost:7860 and enter tasks like:

- "Open Chrome"

- "Search for weather in New York"

- "Open Settings and enable WiFi"

python phone_agent.py "your task here"

Example:

python phone_agent.py "Open the camera app"

- Screenshot Capture: Takes a screenshot of the phone via ADB

- Visual Analysis: Qwen3-VL analyzes the screen to understand UI elements

- Action Planning: Determines the best action to take (tap, swipe, type, etc.)

- Execution: Sends ADB commands to perform the action

- Repeat: Continues until task is complete or max cycles reached

Key settings in config.json:

- temperature: Model creativity (0.0-1.0, default: 0.1)

- max_tokens: Max response length (default: 512)

- step_delay: Wait time between actions in seconds (default: 1.5)

- max_retries: Maximum retry attempts (default: 3)

- use_flash_attention: Enable Flash Attention 2 for faster inference

Device not detected:

- Ensure USB debugging is enabled

- Run adb devices to verify connection

- Try adb kill-server && adb start-server

Wrong tap locations:

- Auto-detect resolution in Settings tab of UI

- Or manually verify with adb shell wm size

Model loading errors:

- Ensure you have sufficient VRAM

- Try the 8B model for lower memory requirements

- Check that transformers is installed from source

Out of memory:

- Use the 8B model instead of 30B

- Reduce max_tokens in config

- Close other applications using GPU memory

Apache License 2.0 - see LICENSE file for details

- Built with [Qwen3-VL](https://github.com/QwenLM/Qwen-VL) by Alibaba Cloud

- Uses [Gradio](https://gradio.app/) for the web interface

## 中文

基于 Python 的移动自动化代理，使用 Qwen3-VL 视觉语言模型通过视觉分析和 ADB 命令来理解和交互 Android 设备。

 /OminousIndustries/PhoneDriver/blob/main/Images/PhoneDriver.png

- 🤖 视觉驱动自动化：使用 Qwen3-VL 视觉理解手机屏幕

- 📱 ADB 集成：通过 ADB 命令控制 Android 设备

- 🎯 自然语言任务：用简单的英文描述你想要什么

- 🖥️ Web 界面：内置 Gradio 界面便于控制

- 📊 实时反馈：实时截图和执行日志

要求：

- Python 3.10+

- 启用 USB 调试和开发者模式的 Android 设备

- 已安装 ADB（Android 调试桥）

- 具有足够 VRAM 的 GPU（已在 24GB GPU 上测试，使用 Qwen3-VL-8B 模型）

- 仓库设置为使用密集型 Qwen3-VL 4B/8B 模型，性能很好。要切换到 MoE 模型，请参见下面的配置部分

Linux/Ubuntu：

sudo apt update
sudo apt install adb

git clone https://github.com/OminousIndustries/PhoneDriver.git
cd PhoneDriver

创建虚拟环境

python -m venv phonedriver
source phonedriver/bin/activate

安装 Python 依赖

pip install git+https://github.com/huggingface/transformers
# pip install transformers==4.57.0 # 目前 V4.57.0 还未发布

# 安装其他要求
pip install pillow gradio qwen_vl_utils requests

- 在 Android 设备上启用 USB 调试（设置 → 开发者选项）

- 通过 USB 连接

- 验证连接：

adb devices

你应该看到你的设备已列出。

编辑 qwen_vl_agent.py 来选择你的模型：

# 对于 4B 模型
model_name: str = "Qwen/Qwen3-VL-4B-Instruct"

# 对于 8B 模型
#model_name: str = "Qwen/Qwen3-VL-8B-Instruct"

#from transformers import Qwen3VLForConditionalGeneration, AutoProcessor - 注释掉这个导入，这是用于密集型模型的
# 对于 MoE 变体，取消注释下面的导入！！！
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor

你还需要更改第 61 行：

 self.model = Qwen3VLForConditionalGeneration.from_pretrained(

将其更改为：

 self.model = Qwen3VLMoeForConditionalGeneration.from_pretrained(

代理可以从 Web UI 设置选项卡自动检测你的设备分辨率，但你也可以在 config.json 中手动配置它。

{
 "screen_width": 1080,
 "screen_height": 2340,
 ...
}

要获取你的设备分辨率，将设备连接到电脑后在终端中输入以下命令：

adb shell wm size

启动 Gradio 界面：

python ui.py

导航到 http://localhost:7860 并输入类似这样的任务：

- "打开 Chrome"

- "搜索纽约的天气"

- "打开设置并启用 WiFi"

python phone_agent.py "你的任务"

示例：

python phone_agent.py "打开相机应用"

工作流程：

- 截图捕获：通过 ADB 对手机进行截图

- 视觉分析：Qwen3-VL 分析屏幕以理解 UI 元素

- 动作规划：确定最佳动作（点击、滑动、输入等）

- 执行：发送 ADB 命令来执行动作

- 重复：继续直到任务完成或达到最大周期数

config.json 中的关键设置：

- temperature：模型创造力（0.0-1.0，默认：0.1）

- max_tokens：最大响应长度（默认：512）

- step_delay：动作之间的等待时间（秒，默认：1.5）

- max_retries：最大重试次数（默认：3）

- use_flash_attention：启用 Flash Attention 2 以获得更快的推理

设备未检测到：

- 确保 USB 调试已启用

- 运行 adb devices 验证连接

- 尝试 adb kill-server && adb start-server

点击位置错误：

- 在 UI 的设置选项卡中自动检测分辨率

- 或使用 adb shell wm size 手动验证

模型加载错误：

- 确保你有足够的 VRAM

- 尝试使用 8B 模型以降低内存要求

- 检查 transformers 是否从源安装

内存不足：

- 使用 8B 模型而不是 30B

- 减少 config 中的 max_tokens

- 关闭使用 GPU 内存的其他应用程序

Apache 许可证 2.0 - 详见 LICENSE 文件

- 使用 [Qwen3-VL](https://github.com/QwenLM/Qwen-VL) by Alibaba Cloud 构建

- 使用 [Gradio](https://gradio.app/) 作为 Web 界面


---

*来源：https://github.com/OminousIndustries/PhoneDriver*
*质量评分：4*
