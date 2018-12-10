# coding: utf8

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
    elif (type == 'lt'):
        return len(param) < length
    elif (type == 'gt'):
        return len(param) > length

def check_is_timestamp_integer(ts):
    '''
    检查是否是10位时间戳数字
    :param ts:
    :return: boolean
    '''
    return len(str(ts)) == 10
