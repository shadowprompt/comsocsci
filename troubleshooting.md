# 二级域名本地调试故障排除指南

## 问题：二级域名无法访问

### 1. 检查 hosts 文件配置

#### Windows 系统
```bash
# 以管理员身份打开记事本
# 打开文件：C:\Windows\System32\drivers\etc\hosts
# 确保包含以下内容：

127.0.0.1 comsocsci.com
127.0.0.1 www.comsocsci.com
127.0.0.1 courses.comsocsci.com
127.0.0.1 lecturers.comsocsci.com
127.0.0.1 textbooks.comsocsci.com
127.0.0.1 trainings.comsocsci.com
127.0.0.1 cases.comsocsci.com
```

#### macOS/Linux 系统
```bash
# 编辑 hosts 文件
sudo nano /etc/hosts

# 确保包含相同的内容
```

### 2. 清除 DNS 缓存

#### Windows
```cmd
ipconfig /flushdns
```

#### macOS
```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

#### Linux
```bash
sudo systemctl restart systemd-resolved
```

### 3. 测试 DNS 解析

运行测试脚本：
```bash
python3 test-subdomains.py
```

或者手动测试：
```bash
# Windows
nslookup courses.comsocsci.com

# macOS/Linux
nslookup courses.comsocsci.com
```

应该返回：`127.0.0.1`

### 4. 检查本地服务器

#### 确保服务器正在运行
```bash
# 启动服务器
python3 start-local-server.py

# 或者使用其他端口
python3 start-local-server.py 8080
```

#### 检查端口是否被占用
```bash
# Windows
netstat -ano | findstr :80

# macOS/Linux
lsof -i :80
```

### 5. 测试基本连接

#### 测试本地服务器
```bash
# 测试 localhost
curl http://localhost

# 测试 127.0.0.1
curl http://127.0.0.1
```

#### 测试域名解析
```bash
# 测试主域名
curl http://comsocsci.com

# 测试二级域名
curl http://courses.comsocsci.com
```

### 6. 浏览器相关检查

#### 清除浏览器缓存
- Chrome: Ctrl+Shift+Delete
- Firefox: Ctrl+Shift+Delete
- Safari: Cmd+Option+E

#### 使用无痕模式测试
- Chrome: Ctrl+Shift+N
- Firefox: Ctrl+Shift+P
- Safari: Cmd+Shift+N

#### 检查浏览器开发者工具
1. 按 F12 打开开发者工具
2. 查看 Console 标签页的错误信息
3. 查看 Network 标签页的网络请求

### 7. 防火墙和杀毒软件

#### Windows 防火墙
1. 打开 Windows Defender 防火墙
2. 允许 Python 或你的服务器程序通过防火墙

#### 杀毒软件
- 临时禁用杀毒软件测试
- 将你的网站目录添加到白名单

### 8. 使用不同的端口

如果 80 端口有问题，尝试其他端口：

#### 修改 hosts 文件
```
127.0.0.1:8080 comsocsci.com
127.0.0.1:8080 courses.comsocsci.com
```

#### 启动服务器
```bash
python3 start-local-server.py 8080
```

#### 访问地址
```
http://comsocsci.com:8080
http://courses.comsocsci.com:8080
```

### 9. 使用 Nginx 本地配置

如果 Python 服务器有问题，可以配置 Nginx：

#### 安装 Nginx
```bash
# Ubuntu/Debian
sudo apt install nginx

# macOS
brew install nginx
```

#### 配置 Nginx
```bash
# 编辑配置文件
sudo nano /etc/nginx/sites-available/comsocsci.com

# 添加配置内容（参考 nginx.conf）
```

#### 启用配置
```bash
sudo ln -s /etc/nginx/sites-available/comsocsci.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 10. 常见错误和解决方案

#### 错误：Connection refused
- 检查服务器是否正在运行
- 检查端口是否正确
- 检查防火墙设置

#### 错误：Name or service not known
- 检查 hosts 文件配置
- 清除 DNS 缓存
- 重启网络服务

#### 错误：Permission denied
- 使用管理员权限运行
- 检查文件权限
- 使用其他端口

#### 页面显示 404
- 检查文件是否存在
- 检查文件路径
- 检查服务器配置

### 11. 调试步骤总结

1. **检查 hosts 文件** - 确保所有域名都指向 127.0.0.1
2. **清除 DNS 缓存** - 刷新本地 DNS 缓存
3. **测试 DNS 解析** - 使用 nslookup 或测试脚本
4. **启动服务器** - 确保服务器正在运行
5. **测试基本连接** - 先测试 localhost
6. **测试域名访问** - 测试各个二级域名
7. **检查浏览器** - 清除缓存，使用无痕模式
8. **检查防火墙** - 确保端口未被阻止
9. **尝试其他端口** - 如果 80 端口有问题
10. **使用 Nginx** - 如果 Python 服务器有问题

### 12. 获取帮助

如果以上步骤都无法解决问题：

1. 运行测试脚本并查看输出
2. 检查浏览器开发者工具的错误信息
3. 查看服务器控制台的输出信息
4. 提供详细的错误信息和系统环境 