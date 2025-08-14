#!/usr/bin/env python3
"""
URL测试脚本
用于测试所有二级域名和子路径是否正常工作
"""

import requests
import sys
import time
from urllib.parse import urljoin

def test_url(base_url, path="", expected_status=200):
    """测试单个URL"""
    url = urljoin(base_url, path)
    try:
        response = requests.get(url, timeout=10)
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
    print("🧪 ComSocSci URL测试脚本")
    print("=" * 40)
    
    # 获取基础URL
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = "http://localhost"
    
    print(f"📍 测试基础URL: {base_url}")
    print("=" * 40)
    
    # 测试URL列表
    test_urls = [
        # 主域名
        ("http://comsocsci.com", ""),
        
        # 课程二级域名
        ("http://courses.comsocsci.com", ""),
        ("http://courses.comsocsci.com", "intro"),
        ("http://courses.comsocsci.com", "slides"),
        ("http://courses.comsocsci.com", "videos"),
        ("http://courses.comsocsci.com", "lecturers"),
        
        # 讲师二级域名
        ("http://lecturers.comsocsci.com", ""),
        
        # 教材二级域名
        ("http://textbooks.comsocsci.com", ""),
        
        # 培训二级域名
        ("http://trainings.comsocsci.com", ""),
        
        # 案例二级域名
        ("http://cases.comsocsci.com", ""),
    ]
    
    success_count = 0
    total_count = len(test_urls)
    
    for base, path in test_urls:
        if test_url(base, path):
            success_count += 1
        time.sleep(0.5)  # 避免请求过快
    
    print("=" * 40)
    print(f"📊 测试结果: {success_count}/{total_count} 成功")
    
    if success_count == total_count:
        print("🎉 所有URL测试通过！")
    else:
        print("⚠️  部分URL测试失败，请检查配置")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 