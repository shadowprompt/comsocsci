# 本地调试配置指南

## 方法一：修改 hosts 文件（推荐）

### Windows 系统
1. 以管理员身份打开记事本
2. 打开文件：`C:\Windows\System32\drivers\etc\hosts`
3. 在文件末尾添加以下内容：

```
127.0.0.1 comsocsci.com
127.0.0.1 www.comsocsci.com
127.0.0.1 courses.comsocsci.com
127.0.0.1 lecturers.comsocsci.com
127.0.0.1 textbooks.comsocsci.com
127.0.0.1 trainings.comsocsci.com
127.0.0.1 cases.comsocsci.com
```

4. 保存文件

### macOS/Linux 系统
1. 打开终端
2. 使用管理员权限编辑 hosts 文件：
```bash
sudo nano /etc/hosts
```

3. 在文件末尾添加以下内容：
```
127.0.0.1 comsocsci.com
127.0.0.1 www.comsocsci.com
127.0.0.1 courses.comsocsci.com
127.0.0.1 lecturers.comsocsci.com
127.0.0.1 textbooks.comsocsci.com
127.0.0.1 trainings.comsocsci.com
127.0.0.1 cases.comsocsci.com
```

4. 保存并退出（Ctrl+X，然后按 Y）

### 2. 启动本地服务器

#### 使用 Python 内置服务器
```bash
# 进入你的网站目录
cd /path/to/your/website

# Python 3
python3 -m http.server 80

# Python 2
python -m SimpleHTTPServer 80
```

#### 使用 Node.js
```bash
# 安装 http-server
npm install -g http-server

# 启动服务器
http-server -p 80
```

#### 使用 PHP
```bash
# 进入网站目录
cd /path/to/your/website

# 启动 PHP 内置服务器
php -S 0.0.0.0:80
```

### 3. 测试访问
现在你可以在浏览器中访问：
- http://comsocsci.com
- http://courses.comsocsci.com
- http://courses.comsocsci.com/intro
- http://courses.comsocsci.com/slides
- http://courses.comsocsci.com/videos
- http://lecturers.comsocsci.com
- http://textbooks.comsocsci.com
- http://trainings.comsocsci.com
- http://cases.comsocsci.com

## 方法二：使用 Nginx 本地配置

### 1. 安装 Nginx
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# macOS (使用 Homebrew)
brew install nginx

# CentOS/RHEL
sudo yum install nginx
```

### 2. 配置 Nginx
```bash
# 备份默认配置
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup

# 创建新配置
sudo nano /etc/nginx/sites-available/comsocsci.com
```

将 `nginx.conf` 的内容复制到配置文件中，并修改网站路径：
```nginx
# 将 /path/to/your/website 替换为你的实际路径
root /home/yourusername/website/comsocsci;
```

### 3. 启用配置
```bash
# 创建符号链接
sudo ln -s /etc/nginx/sites-available/comsocsci.com /etc/nginx/sites-enabled/

# 删除默认配置
sudo rm /etc/nginx/sites-enabled/default

# 测试配置
sudo nginx -t

# 重启 Nginx
sudo systemctl restart nginx
```

## 方法三：使用 Docker（高级）

### 1. 创建 Dockerfile
```dockerfile
FROM nginx:alpine

# 复制网站文件
COPY . /usr/share/nginx/html

# 复制 Nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### 2. 创建 docker-compose.yml
```yaml
version: '3'
services:
  comsocsci:
    build: .
    ports:
      - "80:80"
    volumes:
      - .:/usr/share/nginx/html
```

### 3. 启动容器
```bash
docker-compose up -d
```

## 调试技巧

### 1. 浏览器开发者工具
- 按 F12 打开开发者工具
- 查看 Console 标签页的错误信息
- 查看 Network 标签页的网络请求

### 2. 检查文件路径
确保所有文件都在正确的位置：
```
your-website/
├── index.html
├── courses-intro.html
├── courses-slides.html
├── courses-videos.html
├── lecturers-main.html
├── course-grid.html
├── teachers.html
├── course-details.html
├── blog-grid.html
├── css/
├── js/
└── images/
```

### 3. 常见问题解决

#### 端口被占用
如果 80 端口被占用，可以使用其他端口：
```bash
# 使用 8080 端口
python3 -m http.server 8080
```

然后访问：http://courses.comsocsci.com:8080

#### 权限问题
```bash
# 确保文件有正确的权限
chmod -R 755 /path/to/your/website
```

#### 缓存问题
- 按 Ctrl+F5 强制刷新
- 清除浏览器缓存
- 使用无痕模式测试

### 4. 测试清单
- [ ] hosts 文件已正确配置
- [ ] 本地服务器正在运行
- [ ] 所有 HTML 文件都存在
- [ ] CSS 和 JS 文件路径正确
- [ ] 图片文件路径正确
- [ ] 浏览器可以访问所有二级域名
- [ ] 子路径可以正常访问

## 推荐调试流程

1. **先使用方法一**（hosts + Python 服务器）快速测试
2. **确认页面正常后**，再配置 Nginx 进行完整测试
3. **使用浏览器开发者工具**检查错误
4. **测试所有二级域名和子路径**
5. **确认样式和功能正常** 