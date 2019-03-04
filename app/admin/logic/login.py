# coding: utf8
from app.common.util.input_checker import param_err, check_len, check_is_phone, check_is_email, is_none

def signup_action(params):
    '''
    校验注册
    :param params:
    :return:
    '''
    username = params.get('username')
    password = params.get('password')
    email = params.get('email')
    phone = params.get('phone')

    # 用户名长度在 [1,30] 之间
    if is_none(username) or not (check_len(username, 1, 'ge') and check_len(username, 30, 'le')):
        return param_err('用户名长度')
    # 密码长度在 [6-30] 之间
    if is_none(password) or not (check_len(password, 6, 'ge') and check_len(password, 30, 'le')):
        return param_err('密码长度')
    if is_none(email) or not check_is_email(email):
        return param_err('邮箱')
    if is_none(phone) or not check_is_phone(phone):
        return param_err('手机号')

    return dict(type=True)

def signin_action(params):
    '''
    校验登录
    :param params:
    :return:
    '''
    username = params.get('username')
    password = params.get('password')

    # 用户名长度在 [1,30] 之间
    if is_none(username) or not (check_len(username, 1, 'ge') and check_len(username, 30, 'le')):
        return param_err('用户名长度')
    # 密码长度在 [6-30] 之间
    if is_none(password) or not (check_len(password, 6, 'ge') and check_len(password, 30, 'le')):
        return param_err('密码长度')

    return dict(type=True)

def forget_pass_action(params):
    '''
    校验忘记密码
    :param params:
    :return:
    '''
    email = params.get('email')
    password = params.get('password')

    if is_none(email) or not check_is_email(email):
        return param_err('邮箱')
    if is_none(password) or not (check_len(password, 6, 'ge') and check_len(password, 30, 'le')):
        return param_err('密码长度')

    return dict(type=True)

def forget_pass_confirm_action(params):
    '''
    忘记密码，激活密码页面的qs参数
    :param params:
    :return:
    '''
    verifycode = params.get('code') # 清除首尾空白字符

    if is_none(verifycode) or len(verifycode.strip()) != 128:
        return param_err('校验码格式')

    return dict(type=True)





