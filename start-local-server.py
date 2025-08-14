#!/usr/bin/env python3
"""
本地调试服务器启动脚本
用于在本地测试二级域名网站
"""

import http.server
import socketserver
import os
import sys
import webbrowser
import time
from pathlib import Path
from urllib.parse import urlparse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """自定义HTTP请求处理器，支持二级域名路由"""
    
    def do_GET(self):
        """处理GET请求，实现简单的路由"""
        # 获取请求的路径和主机头
        path = self.path
        host = self.headers.get('Host', '')
        
        print(f"请求: {host}{path}")
        
        # 二级域名路由映射
        domain_routes = {
            'courses.comsocsci.com': {
                '/': '/course-grid.html',
                '/intro': '/courses-intro.html',
                '/slides': '/courses-slides.html', 
                '/videos': '/courses-videos.html',
                '/lecturers': '/teachers.html'
            },
            'lecturers.comsocsci.com': {
                '/': '/lecturers-main.html'
            },
            'textbooks.comsocsci.com': {
                '/': '/course-details.html'
            },
            'trainings.comsocsci.com': {
                '/': '/course-grid.html'
            },
            'cases.comsocsci.com': {
                '/': '/blog-grid.html'
            },
            'comsocsci.com': {
                '/': '/index.html'
            },
            'www.comsocsci.com': {
                '/': '/index.html'
            }
        }
        
        # 从Host头中提取域名
        domain = host.split(':')[0] if ':' in host else host
        
        # 检查是否有对应的路由配置
        if domain in domain_routes:
            routes = domain_routes[domain]
            
            # 检查路径是否需要重定向
            if path in routes:
                target_file = routes[path]
                print(f"重定向: {path} -> {target_file}")
                
                # 检查目标文件是否存在
                if os.path.exists(target_file.lstrip('/')):
                    # 直接返回目标文件内容
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    with open(target_file.lstrip('/'), 'rb') as f:
                        self.wfile.write(f.read())
                    return
                else:
                    print(f"文件不存在: {target_file}")
        
        # 默认处理 - 尝试直接访问文件
        if path == '/':
            # 根据域名返回默认页面
            default_pages = {
                'courses.comsocsci.com': 'course-grid.html',
                'lecturers.comsocsci.com': 'lecturers-main.html',
                'textbooks.comsocsci.com': 'course-details.html',
                'trainings.comsocsci.com': 'course-grid.html',
                'cases.comsocsci.com': 'blog-grid.html',
                'comsocsci.com': 'index.html',
                'www.comsocsci.com': 'index.html'
            }
            
            if domain in default_pages:
                default_file = default_pages[domain]
                if os.path.exists(default_file):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    with open(default_file, 'rb') as f:
                        self.wfile.write(f.read())
                    return
        
        # 如果以上都不匹配，使用默认的静态文件服务
        super().do_GET()

def check_hosts_file():
    """检查hosts文件是否已配置"""
    hosts_paths = {
        'windows': r'C:\Windows\System32\drivers\etc\hosts',
        'linux': '/etc/hosts',
        'darwin': '/etc/hosts'  # macOS
    }
    
    system = sys.platform
    if system.startswith('win'):
        hosts_path = hosts_paths['windows']
    elif system.startswith('linux'):
        hosts_path = hosts_paths['linux']
    elif system.startswith('darwin'):
        hosts_path = hosts_paths['darwin']
    else:
        print("❌ 不支持的操作系统")
        return False
    
    try:
        with open(hosts_path, 'r') as f:
            content = f.read()
            required_domains = [
                'comsocsci.com',
                'courses.comsocsci.com',
                'lecturers.comsocsci.com'
            ]
            
            missing_domains = []
            for domain in required_domains:
                if domain not in content:
                    missing_domains.append(domain)
            
            if missing_domains:
                print("⚠️  hosts文件缺少以下域名配置：")
                for domain in missing_domains:
                    print(f"   127.0.0.1 {domain}")
                print("\n请按照 hosts-setup.md 中的说明配置hosts文件")
                return False
            else:
                print("✅ hosts文件配置正确")
                return True
    except Exception as e:
        print(f"❌ 无法读取hosts文件: {e}")
        return False

def check_files():
    """检查必要的文件是否存在"""
    required_files = [
        'index.html',
        'courses-intro.html',
        'courses-slides.html', 
        'courses-videos.html',
        'lecturers-main.html',
        'course-grid.html',
        'teachers.html',
        'course-details.html',
        'blog-grid.html'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ 缺少以下文件：")
        for file in missing_files:
            print(f"   {file}")
        return False
    else:
        print("✅ 所有必要文件都存在")
        return True

def start_server(port=80):
    """启动本地服务器"""
    try:
        # 检查端口是否可用
        with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
            print(f"🚀 服务器启动成功！")
            print(f"📍 访问地址：")
            print(f"   http://comsocsci.com")
            print(f"   http://courses.comsocsci.com")
            print(f"   http://courses.comsocsci.com/intro")
            print(f"   http://courses.comsocsci.com/slides")
            print(f"   http://courses.comsocsci.com/videos")
            print(f"   http://lecturers.comsocsci.com")
            print(f"   http://textbooks.comsocsci.com")
            print(f"   http://trainings.comsocsci.com")
            print(f"   http://cases.comsocsci.com")
            print(f"\n⏹️  按 Ctrl+C 停止服务器")
            
            # 自动打开浏览器
            time.sleep(2)
            webbrowser.open('http://comsocsci.com')
            
            # 启动服务器
            httpd.serve_forever()
            
    except PermissionError:
        print(f"❌ 端口 {port} 需要管理员权限")
        print("请尝试使用其他端口，例如：")
        print(f"   python {sys.argv[0]} 8080")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ 端口 {port} 已被占用")
            print("请尝试使用其他端口，例如：")
            print(f"   python {sys.argv[0]} 8080")
        else:
            print(f"❌ 启动服务器失败: {e}")

def main():
    """主函数"""
    print("🔧 ComSocSci 本地调试服务器")
    print("=" * 40)
    
    # 检查hosts文件
    if not check_hosts_file():
        print("\n请先配置hosts文件，然后重新运行此脚本")
        return
    
    # 检查文件
    if not check_files():
        print("\n请确保所有必要文件都在当前目录中")
        return
    
    # 获取端口
    port = 80
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ 端口号必须是数字")
            return
    
    print(f"\n🎯 使用端口: {port}")
    print("=" * 40)
    
    # 启动服务器
    start_server(port)

if __name__ == "__main__":
    main() 