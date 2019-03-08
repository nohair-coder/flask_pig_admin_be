# coding: utf8
from time import localtime, strftime, time


def get_now_timestamp():
    '''
    获取当前时间对应的10位时间戳
    :return:
    '''
    return int(time())


def get_now_time(format='%Y%m%d'):
    '''
    以一定的格式获取现在的时间 20181228
    :return:
    '''
    return strftime(format, localtime())
