#!/bin/bash

# Nginx本地测试管理脚本
# 用于快速启动、停止和重启本地nginx测试环境

CONFIG_FILE="nginx-local.conf"
NGINX_CONF_DIR="/usr/local/etc/nginx/sites-available"
NGINX_ENABLED_DIR="/usr/local/etc/nginx/sites-enabled"
SITE_NAME="comsocsci-local"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

# 检查nginx是否安装
check_nginx() {
    if ! command -v nginx &> /dev/null; then
        print_error "Nginx未安装"
        echo "请先安装nginx:"
        echo "  macOS: brew install nginx"
        echo "  Ubuntu: sudo apt install nginx"
        exit 1
    fi
}

# 检查配置文件是否存在
check_config() {
    if [ ! -f "$CONFIG_FILE" ]; then
        print_error "配置文件 $CONFIG_FILE 不存在"
        exit 1
    fi
}

# 安装配置
install_config() {
    print_header "安装Nginx配置"
    
    # 创建目录（如果不存在）
    sudo mkdir -p "$NGINX_CONF_DIR"
    sudo mkdir -p "$NGINX_ENABLED_DIR"
    
    # 复制配置文件
    sudo cp "$CONFIG_FILE" "$NGINX_CONF_DIR/$SITE_NAME"
    
    # 创建软链接
    if [ -L "$NGINX_ENABLED_DIR/$SITE_NAME" ]; then
        sudo rm "$NGINX_ENABLED_DIR/$SITE_NAME"
    fi
    sudo ln -s "$NGINX_CONF_DIR/$SITE_NAME" "$NGINX_ENABLED_DIR/$SITE_NAME"
    
    print_message "配置文件已安装到 $NGINX_CONF_DIR/$SITE_NAME"
    print_message "软链接已创建到 $NGINX_ENABLED_DIR/$SITE_NAME"
}

# 测试配置
test_config() {
    print_header "测试Nginx配置"
    
    if sudo nginx -t; then
        print_message "Nginx配置语法正确"
        return 0
    else
        print_error "Nginx配置语法错误"
        return 1
    fi
}

# 启动nginx
start_nginx() {
    print_header "启动Nginx"
    
    if systemctl is-active --quiet nginx 2>/dev/null; then
        print_message "Nginx已在运行"
    else
        if sudo systemctl start nginx 2>/dev/null; then
            print_message "Nginx启动成功"
        elif sudo nginx; then
            print_message "Nginx启动成功"
        else
            print_error "Nginx启动失败"
            return 1
        fi
    fi
}

# 停止nginx
stop_nginx() {
    print_header "停止Nginx"
    
    if sudo systemctl stop nginx 2>/dev/null; then
        print_message "Nginx停止成功"
    elif sudo nginx -s stop; then
        print_message "Nginx停止成功"
    else
        print_warning "Nginx可能已经停止"
    fi
}

# 重启nginx
restart_nginx() {
    print_header "重启Nginx"
    
    if systemctl is-active --quiet nginx 2>/dev/null; then
        if sudo systemctl restart nginx; then
            print_message "Nginx重启成功"
        else
            print_error "Nginx重启失败"
            return 1
        fi
    else
        stop_nginx
        sleep 2
        start_nginx
    fi
}

# 显示状态
show_status() {
    print_header "Nginx状态"
    
    if systemctl is-active --quiet nginx 2>/dev/null; then
        print_message "Nginx正在运行"
        systemctl status nginx --no-pager -l
    elif pgrep nginx > /dev/null; then
        print_message "Nginx正在运行"
        ps aux | grep nginx | grep -v grep
    else
        print_warning "Nginx未运行"
    fi
}

# 显示测试URL
show_test_urls() {
    print_header "测试URL"
    echo "请在hosts文件中添加以下条目:"
    echo "127.0.0.1 comsocsci.com"
    echo "127.0.0.1 www.comsocsci.com"
    echo "127.0.0.1 courses.comsocsci.com"
    echo "127.0.0.1 lecturers.comsocsci.com"
    echo "127.0.0.1 textbooks.comsocsci.com"
    echo "127.0.0.1 trainings.comsocsci.com"
    echo "127.0.0.1 cases.comsocsci.com"
    echo ""
    echo "测试URL:"
    echo "  http://comsocsci.com"
    echo "  http://courses.comsocsci.com"
    echo "  http://courses.comsocsci.com/intro"
    echo "  http://courses.comsocsci.com/slides"
    echo "  http://courses.comsocsci.com/videos"
    echo "  http://lecturers.comsocsci.com"
    echo "  http://lecturers.comsocsci.com/teachers"
    echo "  http://lecturers.comsocsci.com/teacher-detail"
    echo "  http://textbooks.comsocsci.com"
    echo "  http://trainings.comsocsci.com"
    echo "  http://cases.comsocsci.com"
}

# 卸载配置
uninstall_config() {
    print_header "卸载Nginx配置"
    
    # 停止nginx
    stop_nginx
    
    # 删除软链接
    if [ -L "$NGINX_ENABLED_DIR/$SITE_NAME" ]; then
        sudo rm "$NGINX_ENABLED_DIR/$SITE_NAME"
        print_message "软链接已删除"
    fi
    
    # 删除配置文件
    if [ -f "$NGINX_CONF_DIR/$SITE_NAME" ]; then
        sudo rm "$NGINX_CONF_DIR/$SITE_NAME"
        print_message "配置文件已删除"
    fi
    
    print_message "配置卸载完成"
}

# 显示帮助
show_help() {
    echo "用法: $0 [命令]"
    echo ""
    echo "命令:"
    echo "  install    安装nginx配置"
    echo "  start      启动nginx"
    echo "  stop       停止nginx"
    echo "  restart    重启nginx"
    echo "  status     显示nginx状态"
    echo "  test       测试配置"
    echo "  urls       显示测试URL"
    echo "  uninstall  卸载配置"
    echo "  help       显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 install    # 安装配置"
    echo "  $0 start      # 启动nginx"
    echo "  $0 urls       # 显示测试URL"
}

# 主函数
main() {
    case "${1:-help}" in
        install)
            check_nginx
            check_config
            install_config
            test_config
            ;;
        start)
            check_nginx
            start_nginx
            ;;
        stop)
            check_nginx
            stop_nginx
            ;;
        restart)
            check_nginx
            restart_nginx
            ;;
        status)
            check_nginx
            show_status
            ;;
        test)
            check_nginx
            test_config
            ;;
        urls)
            show_test_urls
            ;;
        uninstall)
            check_nginx
            uninstall_config
            ;;
        help|*)
            show_help
            ;;
    esac
}

# 运行主函数
main "$@" 