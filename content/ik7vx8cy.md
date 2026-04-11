# 该项目在github上：https://github.com/OminousIndustries/PhoneDriver

## English
A Python-based mobile automation agent that uses Qwen3-VL vision-language models to understand and interact with Android devices through visual analysis and ADB commands.

- 🤖 Vision-powered automation: Uses Qwen3-VL to visually understand phone screens
- 📱 ADB integration: Controls Android devices via ADB commands
- 🎯 Natural language tasks: Describe what you want in plain English
- 🖥️ Web UI: Built-in Gradio interface for easy control
- 📊 Real-time feedback: Live screenshots and execution logs

Requirements:
- Python 3.10+
- Android device with USB debugging & Developer Mode enabled
- ADB (Android Debug Bridge) installed
- GPU with sufficient VRAM (Tested on 24gb GPU with Qwen3-VL-8B Model)

Installation:
```bash
sudo apt update
sudo apt install adb
git clone https://github.com/OminousIndustries/PhoneDriver.git
cd PhoneDriver
python -m venv phonedriver
source phonedriver/bin/activate
pip install git+https://github.com/huggingface/transformers
pip install pillow gradio qwen_vl_utils requests
```

Usage:
- Edit qwen_vl_agent.py to choose model (4B or 8B)
- Launch with python ui.py or python phone_agent.py "task"
- Agent uses visual analysis + ADB commands for automation

## 中文
基于 Python 的移动自动化代理，使用 Qwen3-VL 视觉语言模型通过视觉分析和 ADB 命令来理解并与 Android 设备交互。

- 🤖 视觉驱动自动化：使用 Qwen3-VL 视觉理解手机屏幕
- 📱 ADB 集成：通过 ADB 命令控制 Android 设备  
- 🎯 自然语言任务：用纯英语描述你想要的
- 🖥️ Web UI：内置 Gradio 界面便于控制
- 📊 实时反馈：实时截图和执行日志

系统要求：
- Python 3.10+
- Android 设备（开启 USB 调试模式和开发者选项）
- ADB（Android Debug Bridge）已安装
- 具备足够 VRAM 的 GPU（在 Qwen3-VL-8B 模型上测试了 24GB GPU）

安装步骤：
```bash
sudo apt update
sudo apt install adb
git clone https://github.com/OminousIndustries/PhoneDriver.git
cd PhoneDriver
python -m venv phonedriver
source phonedriver/bin/activate
pip install git+https://github.com/huggingface/transformers
pip install pillow gradio qwen_vl_utils requests
```

使用方法：
- 编辑 `qwen_vl_agent.py` 选择模型（4B 或 8B）
- 启动：`python ui.py` 或 `python phone_agent.py "任务"`
- 代理使用视觉分析 + ADB 命令进行自动化
