#!/bin/bash

echo "启动 Excel关键词搜索工具..."
echo "Starting Excel Keyword Search Tool..."
echo

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "错误：未找到Python，请先安装Python"
        echo "Error: Python not found, please install Python first"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# 检查依赖是否安装
$PYTHON_CMD -c "import openpyxl" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "正在安装依赖包..."
    echo "Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

# 优先启动多语言版本
if [ -f "excel_gui_search_i18n.py" ]; then
    echo "启动多语言版本..."
    echo "Starting multilingual version..."
    $PYTHON_CMD excel_gui_search_i18n.py
else
    echo "启动基础版本..."
    echo "Starting basic version..."
    $PYTHON_CMD excel_gui_search.py
fi
