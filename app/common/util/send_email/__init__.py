# coding: utf8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from app.config import mail_config
from app.common.util import asyncFunc, error_logger
from app.common import errorcode

# 第三方 SMTP 服务
mail_host = mail_config['mail_host']  # 设置服务器
mail_user = mail_config['mail_user']  # 用户名
mail_pass = mail_config['mail_pass']  # 口令
sender = mail_config['mail_user']  # sender 必须与 user 一直


def send_mail(title, content, receivers):
    '''
    发送邮件
    :return:
    '''
    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # receivers 是 tuple，可以群发
    # receivers = [receiver]

    message = MIMEText(content, 'html')  # 邮件的正文内容
    message['From'] = formataddr((mail_config['sender_name'], mail_config['mail_user']))
    message['To'] = formataddr(('种猪信息测定管理系统用户', 'all user'))
    message['Subject'] = Header(title)  # 邮件主题

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return True
    except smtplib.SMTPException as e:
        error_logger(e)
        error_logger(errorcode['1000_3001'])
        print("Error: 无法发送邮件")
        return False


@asyncFunc
def send_mail_async(*args, **kwargs):
    '''
    异步发送邮件，不会等待当前执行完毕再执行
    :param args:
    :param kwargs:
    :return:
    '''
    send_mail(*args, **kwargs)
