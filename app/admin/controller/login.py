# coding: utf8
'用户注册、登录、忘记密码'

# - signIn -> 提供用户名，密码
# - signUp -> 提供用户名，密码，邮箱，手机号
# - forgetPass -> 邮箱，新密码

from flask import request
from app.admin import admin
from app.admin.logic.login import signup_action, signin_action, forget_pass_action, forget_pass_confirm_action
from app.models import User, UserFindPass
from app.common.util import error_response, success_response, error_logger, password_encode, generate_token, get_now_timestamp
from app.common.util.send_email import send_mail_async
from app.common.errorcode import error_code
from app.config import mail_config

@admin.route('/admin/login/signup', methods=['POST'])
def sigup():
    '''
    用户注册
    :return:
    '''
    try:
        # 参数校验
        request_data = request.json
        param_checker = signup_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        # 数据写入
        username = request_data.get('username')
        # 加密过后的密文密码
        password_hash = password_encode(request_data.get('password'))
        email = request_data.get('email')
        phone = request_data.get('phone')
        token = generate_token()
        rank = 'common'
        created_time = get_now_timestamp()
        last_login_time = created_time

        new_user = User({
            'username': username,
            'password': password_hash,
            'email': email,
            'phone': phone,

            'token': token,
            'rank': rank,
            'created_time': created_time,
            'last_login_time': last_login_time,
        })

        # 检查是否已经有相同的用户名、邮箱、手机号注册
        if new_user.get_from_username():
            return error_response('用户名已存在')
        if new_user.get_from_email():
            return error_response('邮箱已存在')
        if new_user.get_from_phone():
            return error_response('手机号已存在')

        # 重复性校验没有问题，则将用户数据写入，并返回信息
        new_user.signup()

        return success_response({
            'user': {
                'username': new_user.username,
                'token': new_user.token,
                'rank': new_user.rank,
            },
        })

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_9001'])
        return error_response(error_code['1000_9001'])


@admin.route('/admin/login/signin', methods=['POST'])
def signin():
    '''
    用户登录
    :return:
    '''
    try:
        # 参数校验
        request_data = request.json
        param_checker = signin_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        # 数据写入
        username = request_data.get('username')
        # 加密过后的密文密码
        password_hash = password_encode(request_data.get('password'))
        last_login_time = get_now_timestamp()
        token = generate_token()

        user = User({
            'username': username,
            'password': password_hash,
        })

        user_in_db = user.get_from_username()

        # 用户的登录信息校验通过，则把用户的信息保存到数据库
        if user_in_db and user_in_db.password == user.password:
            user_in_db.signin(token=token, last_login_time=last_login_time)
            return success_response({
                'user': {
                    'username': user_in_db.username,
                    'token': user_in_db.token,
                    'rank': user_in_db.rank,
                },
            })
        else:
            return error_response('用户名或密码错误')

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_9002'])
        return error_response(error_code['1000_9002'])


@admin.route('/admin/login/forget_pass', methods=['POST'])
def forget_pass():
    '''
    用户忘记密码
    :return:
    '''
    try:
        # 参数校验
        request_data = request.json
        param_checker = forget_pass_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        # 数据写入
        email = request_data.get('email')
        # 加密过后的密文密码
        password_hash = password_encode(request_data.get('password'))
        verifycode = generate_token() + generate_token()
        created_time = get_now_timestamp()

        user = User({
            'email': email,
        })

        user_exist = user.get_from_email() != None

        if user_exist:
            user_find_pass_record = UserFindPass({
                'email': email,
                'verifycode': verifycode,
                'password': password_hash,
                'created_time': created_time,
            })

            user_find_pass_record.add()

            email_verify_link = 'http://localhost:5000/admin/login/forget_pass_confirm?code=' + verifycode
            # 邮件的标题
            email_title = '新密码激活'

            # 邮件的内容
            email_content = '''<!doctype html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>新密码激活邮件</title>
</head>
<body style="text-align: center">
    <h1>{title}</h1>
    <p><a href="{link}">点击</a>即可激活新设置的密码</p>
    <p>或者复制下方字符串到浏览器打开</p>
    <p>{link}</p>
</body>
</html>
'''.format(link=email_verify_link, title=mail_config['sender_name'])
            send_mail_async(email_title, email_content, [email])

            return success_response()
        else:
            return error_response('该用户邮箱未注册')

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_9003'])
        return error_response(error_code['1000_9003'])

@admin.route('/admin/login/forget_pass_confirm', methods=['GET'])
def forget_pass_confirm():
    '''
    邮件找回密码，确认的网页
    :return:
    '''

    def temp(result, extra=''):
        return '''<!doctype html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{result}</title>
    </head>
    <body style="text-align: center">
        <h1>{result}</h1>
        <p>{extra}</p>
    </body>
    </html>
    '''.format(result=result, extra=extra)

    try:
        # 参数校验
        request_data = request.args
        param_checker = forget_pass_confirm_action(request_data)
        if not param_checker['type']: return temp('激活<font color=red>失败</font>', param_checker['err_msg'])

        verifycode = request_data.get('code')

        user_find_pass = UserFindPass({
            'verifycode': verifycode,
        })

        user_find_pass_record = user_find_pass.find() # 从数据库查询到高 verifycode 对应的数据库记录

        if not user_find_pass_record: return temp('激活<font color=red>失败</font>', '校验码错误，无记录')

        user = User({
            'email': user_find_pass_record.email,
        }).get_from_email()

        user.password = user_find_pass_record.password
        user.update() # 将密码更新过来

        user_find_pass_record.delete() # 删除数据库中的该条记录

        return temp('激活<font color=green>成功</font>', '请使用新密码登录系统')

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_9004'])
        return error_response(error_code['1000_9004'])
