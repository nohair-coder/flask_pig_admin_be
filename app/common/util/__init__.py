# coding: utf8

from .response import error_response, success_response

from .logger import error_logger, info_logger, warning_logger

from .new_thread import asyncFunc

from .time import get_now_timestamp, get_now_time, transform_time

from .user import password_encode, generate_token



def auth_err(err_msg='非法请求'):
    '''
    非法请求
    :return:
    '''
    return dict(type=False, err_msg=err_msg)

def auth_success(user):
    '''
    合法的请求
    :return:
    '''
    return dict(type=True, data=user)
