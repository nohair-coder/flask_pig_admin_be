# coding: utf8
'configs all here'

mysql_config = dict(
    username='root',
    password='root',
    host='127.0.0.1',
    port='8889',
    database='pig',
)

# 连接数据库的 url
database_URI = 'mysql+pymysql://' + mysql_config['username'] + ':' + mysql_config['password'] + '@' + mysql_config['host'] + ':'+ mysql_config['port'] +'/'+ mysql_config['database']
# 测定站完全正常状态的状态码
station_errorcode_on_normal_code = '00000'
# 发送邮件的配置
mail_config = dict(
    mail_host='smtp.qq.com',
    mail_user='3248184446@qq.com',
    mail_pass='zdwzcwtgkhdfdbdh',
    sender_name='种猪测定信息管理系统'
)

# 分页加载时，每次加载的条目数
length_per_page = 50
