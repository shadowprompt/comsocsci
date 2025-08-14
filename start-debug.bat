@echo off
echo 🔧 ComSocSci 本地调试服务器启动脚本
echo ========================================

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到Python，请先安装Python
    pause
    exit /b 1
)

REM 启动服务器
echo 🚀 启动本地调试服务器...
python start-local-server.py %1

pause 