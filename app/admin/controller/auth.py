# coding: utf8
'权限校验'
from app.common.util import auth_err, auth_success
from app.models import User


def auth_checker(token=None):
    '''
    请求权限校验函数
    :return:
    '''
    if not token:
        return auth_err(err_msg='非法请求')
    user = User({'token': token}).get_from_token()

    print(user)

    if user:
        return auth_success(user)

