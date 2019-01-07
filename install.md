# 系统安装

## 环境依赖(当前运行环境)
- python3 python3.7.1
- nodejs 10.11.0
- mysql 5.7.23

## 安装注意事项
### Mysql
Mysql 初始用户为root，需要新建一个用户 lxfriday，并授予pig数据库的所有权限

用户名：lxfriday

密码：lxfriday

创建方法
```mysql
CREATE USER 'lxfriday'@'%' IDENTIFIED BY 'lxfriday';  # 第一个 lxfriday 为用户名，% 代表 localhost 和 任意的外部IP都可以访问，第二个 lxfriday 是密码

GRANT ALL ON pig.* TO 'lxfriday'@'%'; # 授予 pig 数据库的所有权限到 lxfriday 用户

FLUSH PRIVILEGES; # 刷新，使修改生效

```
