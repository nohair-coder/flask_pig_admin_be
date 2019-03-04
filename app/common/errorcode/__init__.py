# coding: utf8
'定义错误码'

error_code = {
    # `app/back/controller/piginfo`
    '1000_0001': '1000_0001: 向数据库插入数据失败',
    # `app/back/controller/stationinfo`
    '1000_1001': '1000_1001: 向数据库插入数据失败',
    # `app/back/controller/phonemessage`
    '1000_2001': '1000_2001: 短信发送失败',
    # `app/common/util/send_mail/__init__`
    '1000_3001': '1000_3001: 邮件发送失败',
    # `app/admin/controller/notificationcontact`
    '1000_4001': '1000_4001: 通知邮箱添加失败',
    # `app/admin/controller/dashboard`
    '1000_5001': '1000_5001: 获取测定站信息失败',
    # `app/admin/controller/piginfo`
    '1000_6001': '1000_6001: 获取种猪信息失败',
    # `app/admin/controller/piginfo`
    '1000_6101': '1000_6101: 导出种猪信息失败，具体原因请查看日志',
    '1000_6102': '1000_6102: 导出种猪信息失败',
    # `app/admin/controller/errorcode`
    '1000_7001': '1000_7001: 查询故障码失败',
    '1000_7101': '1000_7101: 删除故障码失败',
    '1000_7201': '1000_7201: 添加故障码失败',
    '1000_7301': '1000_7301: 更改故障码失败',

    # `app/admin/controller/syscfg
    '1000_8001': '1000_8001: 获取系统全部配置失败',
    '1000_8002': '1000_8002: 更改系统部分配置失败',

# `app/admin/controller/login
    '1000_9001': '1000_9001: 注册失败',
    '1000_9002': '1000_9002: 登录失败',
}
