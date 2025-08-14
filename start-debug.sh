#!/bin/bash

echo "🔧 ComSocSci 本地调试服务器启动脚本"
echo "========================================"

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到Python3，请先安装Python3"
    exit 1
fi

# 给脚本执行权限
chmod +x start-local-server.py

# 启动服务器
echo "🚀 启动本地调试服务器..."
python3 start-local-server.py "$1" 