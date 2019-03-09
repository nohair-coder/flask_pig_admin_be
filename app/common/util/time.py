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
    以一定的格式获取现在的时间
    %Y%m%d 20181228
    %Y%m%d 20181228
    %Y%m%d%H%M 201812281213
    :return:
    '''
    return strftime(format, localtime())


def transform_time(t=0, format='%Y%m%d%H%M'):
    '''
    以一定的格式转换给定的时间
    %Y%m%d 20181228
    %Y%m%d 20181228
    %Y%m%d%H%M 201812281213
    %Y/%m/%d %H:%M:%S 2018/12/28 12:13:23
    :param t: 给定的时间戳 10位
    :param format:  要转换成的格式
    :return:
    '''
    return strftime(format, localtime(t))
