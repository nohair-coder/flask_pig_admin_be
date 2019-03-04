# coding: utf8
'用户注册的哈希字符串的生成相关'

import hashlib
import time
import random
import math

def password_encode(password):
    '''
    对明文密码进行加密存储的算法函数
    :param password:
    :return:
    '''
    h = hashlib.sha256()
    h.update(password.encode('utf8'))
    return h.hexdigest()

def generate_token():
    '''
    产生一个 token
    :return:
    '''
    start = random.randint(0, 10000)
    end = random.randint(0, 10000)
    center = math.floor(time.time())

    h = hashlib.sha256()
    random_str = str(start) + '-' + str(center) + '-' + str(end)  # random1 - timestamp - time2
    h.update(random_str.encode('utf8'))
    return h.hexdigest()

