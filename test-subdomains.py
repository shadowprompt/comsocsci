#!/usr/bin/env python3
"""
二级域名测试脚本
用于测试二级域名是否正常工作
"""

import requests
import sys
import time
import socket

def test_dns_resolution(domain):
    """测试DNS解析"""
    try:
        ip = socket.gethostbyname(domain)
        if ip == '127.0.0.1':
            print(f"✅ {domain} -> {ip} (本地解析正确)")
            return True
        else:
            print(f"❌ {domain} -> {ip} (应该解析到127.0.0.1)")
            return False
    except socket.gaierror as e:
        print(f"❌ {domain} - DNS解析失败: {e}")
        return False

def test_url(domain, path="", expected_status=200):
    """测试URL访问"""
    url = f"http://{domain}{path}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == expected_status:
            print(f"✅ {url} - 状态码: {response.status_code}")
            return True
        else:
            print(f"❌ {url} - 状态码: {response.status_code} (期望: {expected_status})")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ {url} - 错误: {e}")
        return False

def main():
    """主函数"""
    print("🧪 二级域名测试脚本")
    print("=" * 50)
    
    # 测试域名列表
    domains = [
        'comsocsci.com',
        'www.comsocsci.com',
        'courses.comsocsci.com',
        'lecturers.comsocsci.com',
        'textbooks.comsocsci.com',
        'trainings.comsocsci.com',
        'cases.comsocsci.com'
    ]
    
    print("1. 测试DNS解析...")
    print("-" * 30)
    
    dns_success = 0
    for domain in domains:
        if test_dns_resolution(domain):
            dns_success += 1
    
    print(f"\nDNS解析结果: {dns_success}/{len(domains)} 成功")
    
    if dns_success < len(domains):
        print("\n⚠️  DNS解析有问题，请检查hosts文件配置")
        print("hosts文件应该包含以下内容：")
        for domain in domains:
            print(f"   127.0.0.1 {domain}")
        return 1
    
    print("\n2. 测试URL访问...")
    print("-" * 30)
    
    # 测试URL列表
    test_urls = [
        ('comsocsci.com', ''),
        ('courses.comsocsci.com', ''),
        ('courses.comsocsci.com', '/intro'),
        ('courses.comsocsci.com', '/slides'),
        ('courses.comsocsci.com', '/videos'),
        ('lecturers.comsocsci.com', ''),
        ('textbooks.comsocsci.com', ''),
        ('trainings.comsocsci.com', ''),
        ('cases.comsocsci.com', '')
    ]
    
    url_success = 0
    for domain, path in test_urls:
        if test_url(domain, path):
            url_success += 1
        time.sleep(0.5)
    
    print(f"\nURL访问结果: {url_success}/{len(test_urls)} 成功")
    
    if url_success < len(test_urls):
        print("\n⚠️  URL访问有问题，请检查：")
        print("1. 本地服务器是否正在运行")
        print("2. 端口是否正确")
        print("3. 防火墙设置")
        return 1
    
    print("\n🎉 所有测试通过！二级域名工作正常")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 