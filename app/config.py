# coding: utf8
'configs all here'

# 连接数据库的 url
database_URI = 'mysql+pymysql://root:root@127.0.0.1:8889/pig'
# 测定站完全正常状态的状态码
station_errorcode_on_normal_code = '00000'
# 发送邮件的配置
mail_config = dict(
    mail_host='smtp.qq.com',
    mail_user='3248184446@qq.com',
    mail_pass='vsjqxqduqbppdafb',
    sender_name='种猪信息测定管理系统'
)
