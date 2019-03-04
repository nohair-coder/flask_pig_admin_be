# coding: utf8
'用户注册、登录、忘记密码'

# - signIn -> 提供用户名，密码
# - signUp -> 提供用户名，密码，邮箱，手机号
# - forgetPass -> 邮箱，新密码

from flask import request
from app.admin import admin
from app.admin.logic.login import signup_action, signin_action
from app.models.user import User
from app.common.util import error_response, success_response, error_logger, password_encode, generate_token, get_now_timestamp
from app.common.errorcode import error_code

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
    return success_response()
