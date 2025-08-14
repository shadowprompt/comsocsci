# Nginx 二级域名部署指南 - comsocsci.com

## 概述
本指南将帮助你配置 Nginx 服务器以支持 comsocsci.com 的二级域名访问。通过二级域名，用户可以更直观地访问不同的页面内容。

## 支持的二级域名映射

| 二级域名 | 对应页面 | 说明 |
|---------|---------|------|
| courses.comsocsci.com | course-grid.html | 课程列表 |
| courses.comsocsci.com/intro | courses-intro.html | 课程介绍 |
| courses.comsocsci.com/slides | courses-slides.html | 课程幻灯片 |
| courses.comsocsci.com/videos | courses-videos.html | 教学视频 |
| courses.comsocsci.com/lecturers | teachers.html | 授课讲师 |
| lecturers.comsocsci.com | lecturers-main.html | 讲师团队 |
| textbooks.comsocsci.com | course-details.html | 教材详情 |
| trainings.comsocsci.com | course-grid.html | 培训课程 |
| cases.comsocsci.com | blog-grid.html | 案例研究 |

## 新创建的页面文件

### 课程相关页面
- **courses-intro.html** - 课程介绍页面，包含课程概述、目标、特色等内容
- **courses-slides.html** - 课程幻灯片页面，展示各章节的幻灯片资源
- **courses-videos.html** - 教学视频页面，包含特色视频和视频列表

### 讲师相关页面
- **lecturers-main.html** - 讲师团队主页，展示所有讲师的详细信息

## Nginx 部署步骤

### 1. 安装 Nginx（如果未安装）
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS/RHEL
sudo yum install nginx
```

### 2. 配置 Nginx

将 `nginx.conf` 文件的内容添加到 Nginx 配置中：

```bash
# 备份原配置
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup

# 编辑配置文件
sudo nano /etc/nginx/sites-available/comsocsci.com
```

将 `nginx.conf` 的内容复制到配置文件中，并修改以下内容：
- 将 `/path/to/your/website` 替换为实际的网站路径

### 3. 启用站点配置
```bash
# 创建符号链接
sudo ln -s /etc/nginx/sites-available/comsocsci.com /etc/nginx/sites-enabled/

# 删除默认配置（可选）
sudo rm /etc/nginx/sites-enabled/default
```

### 4. 测试配置
```bash
sudo nginx -t
```

### 5. 重启 Nginx
```bash
sudo systemctl restart nginx
sudo systemctl enable nginx
```

## DNS 配置

在域名管理面板中添加以下 A 记录：

```
courses.comsocsci.com     A    YOUR_SERVER_IP
lecturers.comsocsci.com   A    YOUR_SERVER_IP
textbooks.comsocsci.com   A    YOUR_SERVER_IP
trainings.comsocsci.com   A    YOUR_SERVER_IP
cases.comsocsci.com       A    YOUR_SERVER_IP
```

## 测试

部署完成后，测试以下链接：

### 课程二级域名及其子路径
- http://courses.comsocsci.com → 应该显示课程页面
- http://courses.comsocsci.com/intro → 应该显示课程介绍页面
- http://courses.comsocsci.com/slides → 应该显示课程幻灯片页面
- http://courses.comsocsci.com/videos → 应该显示教学视频页面
- http://courses.comsocsci.com/lecturers → 应该显示授课讲师页面

### 其他二级域名
- http://lecturers.comsocsci.com → 应该显示讲师团队页面
- http://textbooks.comsocsci.com → 应该显示教材页面
- http://trainings.comsocsci.com → 应该显示培训页面
- http://cases.comsocsci.com → 应该显示案例页面

## 页面特色功能

### 课程介绍页面 (courses-intro.html)
- 课程概述和目标说明
- 适用人群介绍
- 课程特色展示
- 侧边栏导航菜单

### 课程幻灯片页面 (courses-slides.html)
- 幻灯片网格展示
- 下载统计功能
- 分类筛选功能
- 幻灯片预览

### 教学视频页面 (courses-videos.html)
- 特色视频播放
- 视频列表展示
- 观看统计功能
- 视频分类筛选

### 讲师团队页面 (lecturers-main.html)
- 讲师信息展示
- 社交媒体链接
- 专业领域介绍
- 联系方式

## SSL/HTTPS 配置（推荐）

### 使用 Let's Encrypt 免费证书

1. **安装 Certbot**
```bash
# Ubuntu/Debian
sudo apt install certbot python3-certbot-nginx

# CentOS/RHEL
sudo yum install certbot python3-certbot-nginx
```

2. **获取证书**
```bash
sudo certbot --nginx -d comsocsci.com -d www.comsocsci.com -d courses.comsocsci.com -d lecturers.comsocsci.com -d textbooks.comsocsci.com -d trainings.comsocsci.com -d cases.comsocsci.com
```

3. **自动续期**
```bash
sudo crontab -e
# 添加以下行
0 12 * * * /usr/bin/certbot renew --quiet
```

## 性能优化

### 1. 启用 Gzip 压缩
在 Nginx 配置中添加：
```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;
```

### 2. 静态资源缓存
```nginx
location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### 3. 启用 HTTP/2
```nginx
listen 443 ssl http2;
```

## 故障排除

### 常见问题

1. **二级域名无法访问**
   - 检查 DNS 配置是否正确
   - 确认 Nginx 配置已重启
   - 检查防火墙设置

2. **页面显示 404 错误**
   - 确认文件路径是否正确
   - 检查文件权限设置
   - 验证 Nginx 配置语法

3. **静态资源无法加载**
   - 检查 CSS、JS、图片文件路径
   - 确认文件权限设置正确

4. **子路径无法访问**
   - 检查 location 块配置是否正确
   - 确认目标文件存在
   - 验证 try_files 指令

### 调试命令

```bash
# 检查 Nginx 配置语法
sudo nginx -t

# 检查 Nginx 状态
sudo systemctl status nginx

# 查看 Nginx 错误日志
sudo tail -f /var/log/nginx/error.log

# 查看 Nginx 访问日志
sudo tail -f /var/log/nginx/access.log

# 测试 DNS 解析
nslookup courses.comsocsci.com

# 测试 HTTP 响应
curl -I http://courses.comsocsci.com
curl -I http://courses.comsocsci.com/intro
```

## 安全建议

1. **防火墙配置**
```bash
# 只允许 HTTP 和 HTTPS 端口
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

2. **隐藏 Nginx 版本**
在配置文件中添加：
```nginx
server_tokens off;
```

3. **限制请求大小**
```nginx
client_max_body_size 10M;
```

4. **防止恶意请求**
```nginx
# 阻止常见恶意请求
location ~* \.(php|asp|aspx|jsp|cgi)$ {
    deny all;
}
```

## 监控和维护

### 1. 日志轮转
```bash
sudo logrotate /etc/logrotate.d/nginx
```

### 2. 性能监控
```bash
# 查看 Nginx 进程
ps aux | grep nginx

# 查看连接数
netstat -an | grep :80 | wc -l
```

### 3. 定期备份
```bash
# 备份配置文件
sudo cp /etc/nginx/sites-available/comsocsci.com /backup/nginx-config-$(date +%Y%m%d).conf
```

## 联系支持

如果遇到问题，请检查：
1. Nginx 错误日志
2. DNS 配置
3. 防火墙设置
4. 文件权限
5. 配置文件语法 