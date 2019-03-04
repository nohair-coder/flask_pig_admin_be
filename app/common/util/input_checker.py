# coding: utf8
import re


def param_err(key):
    '''
    请求的参数不正确的返回
    :param key: 字段名
    :return:
    '''
    return dict(type=False, err_msg='参数 ' + key + ' 不正确')


def param_corect():
    '''
    请求的参数正确的返回
    :return:
    '''
    return dict(type=True)


def check_exist(param):
    '''
    检验字段是否在参数中存在
    :param param:
    :return:
    '''
    return param != None


def check_len(param, length, type='eq'):
    '''
    检查字段的长度
    :param param: 要校验的字段
    :param length: 长度
    :param type: eq 字段长度等于，lt 字段长度小于，gt 大于
    :return:
    '''

    if (type == 'eq'):
        return len(param) == length
    elif (type == 'le'):
        return len(param) <= length
    elif (type == 'lt'):
        return len(param) < length
    elif (type == 'gt'):
        return len(param) > length
    elif (type == 'ge'):
        return len(param) >= length


def check_is_timestamp_integer(ts):
    '''
    检查是否是10位时间戳数字
    :param ts:
    :return: boolean
    '''
    return len(str(ts)) == 10


def check_is_phone(phone):
    '''
    检查是否是手机号码
    :param phone: 手机号码
    :return:
    '''

    return re.match('^1[0-9]{10}$', str(phone)) != None


def check_number_str_len(number_str='', len=0):
    '''
    检查数字字符串的长度
    :param number_str: 要校验的参数
    :return: True 表示匹配成功
    '''

    return re.match('^[0-9]{' + str(len) + '}$', str(number_str)) != None


def check_in(param, tu):
    '''
    检测给定的参数是否在 tuple 中

    tu = ('a', 'b', 'c', 'd')

    'a' in tu  True

    'w' in tu  False
    :param param:
    :param tuple:
    :return:
    '''
    return param in tu

def check_arr_all_in(arr, tu):
    '''
    检测第一个参数数组中的每个值是否在第二个数组中
    :param arr:
    :param tu:
    :return:
    '''
    for v in arr:
        if v not in tu: return False
    return True

def check_is_email(email):
    '''
    检查是否是邮箱
    :return:
    '''
    # http://emailregex.com/
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(email)) != None


def check_is_str(param):
    '''
    检查是否是字符串
    :param param:
    :return:
    '''

    return type(param) == str


def check_str_len(param='', min=0, max=0):
    '''
    检查字符串是否是超过了指定长度
    :param param:
    :return:
    '''
    return len(str(param)) >= min and len(str(param)) <= max

def is_none(param):
    '''
    参数不是 None
    :param param:
    :return:
    '''
    return param == None
