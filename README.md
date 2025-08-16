# ComSocSci 计算社会科学研究中心

## 🎯 项目概述

ComSocSci是一个基于二级域名的计算社会科学研究中心网站，采用现代化的网站架构和nginx服务器配置。

## 📁 项目结构

```
comsocsci/
├── index.html                 # 主站首页
├── about.html                 # 关于我们
├── contact.html               # 联系我们
├── courses/                   # 课程中心 (courses.comsocsci.com)
│   ├── index.html
│   ├── courses-intro.html
│   ├── courses-slides.html
│   └── courses-videos.html
├── lecturers/                 # 讲师团队 (lecturers.comsocsci.com)
│   ├── index.html
│   ├── lecturers-main.html
│   ├── teachers.html
│   └── teacher-detail.html
├── textbooks/                 # 教材资源 (textbooks.comsocsci.com)
│   └── index.html
├── trainings/                 # 培训项目 (trainings.comsocsci.com)
│   └── index.html
├── cases/                     # 案例研究 (cases.comsocsci.com)
│   └── index.html
├── css/                       # 样式文件
├── js/                        # JavaScript文件
├── images/                    # 图片资源
├── fonts/                     # 字体文件
└── nginx-local.conf          # Nginx本地测试配置
```

## 🌐 二级域名配置

| 二级域名 | 目录 | 功能 |
|---------|------|------|
| `comsocsci.com` | `/` | 主站首页 |
| `courses.comsocsci.com` | `/courses/` | 课程中心 |
| `lecturers.comsocsci.com` | `/lecturers/` | 讲师团队 |
| `textbooks.comsocsci.com` | `/textbooks/` | 教材资源 |
| `trainings.comsocsci.com` | `/trainings/` | 培训项目 |
| `cases.comsocsci.com` | `/cases/` | 案例研究 |

## 🚀 本地测试

### 1. 配置hosts文件

在 `/etc/hosts` 文件中添加：

```
127.0.0.1 comsocsci.com
127.0.0.1 www.comsocsci.com
127.0.0.1 courses.comsocsci.com
127.0.0.1 lecturers.comsocsci.com
127.0.0.1 textbooks.comsocsci.com
127.0.0.1 trainings.comsocsci.com
127.0.0.1 cases.comsocsci.com
```

### 2. 启动Nginx

```bash
# 复制配置文件
sudo cp nginx-local.conf /usr/local/etc/nginx/sites-available/
sudo ln -s /usr/local/etc/nginx/sites-available/nginx-local.conf /usr/local/etc/nginx/sites-enabled/

# 重启Nginx
sudo nginx -s reload
```

### 3. 访问测试

- 主站: http://comsocsci.com
- 课程中心: http://courses.comsocsci.com
- 讲师团队: http://lecturers.comsocsci.com
- 教材资源: http://textbooks.comsocsci.com
- 培训项目: http://trainings.comsocsci.com
- 案例研究: http://cases.comsocsci.com

## ⚙️ Nginx配置说明

### 主要特性

1. **静态资源处理**: 所有二级域名共享主目录的CSS、JS、图片文件
2. **用户权限**: 以当前用户(shadow)运行，避免权限问题
3. **端口配置**: 使用80端口进行本地测试
4. **缓存优化**: 静态资源设置长期缓存

### 关键配置

```nginx
# 静态资源处理
location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    root /Users/shadow/Dev/website/comsocsci;
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# 用户配置
user shadow staff;
```

## 📝 更新日志

### 最新更新 (2025-08-16)

- ✅ 完成二级域名架构搭建
- ✅ 配置nginx本地测试环境
- ✅ 更新首页内容为ComSocSci品牌
- ✅ 修复所有样式和权限问题
- ✅ 优化静态资源加载

## 🔧 故障排除

### 常见问题

1. **样式加载失败**: 检查nginx配置中的静态资源路径
2. **权限错误**: 确保nginx以正确用户运行
3. **端口冲突**: 检查80端口是否被占用

### 调试命令

```bash
# 检查nginx配置
sudo nginx -t

# 查看nginx进程
ps aux | grep nginx

# 查看错误日志
sudo tail -f /usr/local/var/log/nginx/error.log

# 测试静态资源
curl -I http://courses.comsocsci.com/css/style.css
```

## 📞 联系信息

- 网站: http://comsocsci.com
- 邮箱: contact@comsocsci.com
- 电话: 400-123-4567

---

**ComSocSci - 计算社会科学研究中心**  
*探索计算社会科学的奥秘* 