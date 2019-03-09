# coding: utf8
'内存中存储一份猪场代码信息'

from app.common.errorcode import error_code
from app.common.util import asyncFunc
from app.common.util import error_logger
from app.models import SysCfg

facnum = []


def initialize_facnum():
    '''
    从数据库中获取数据到内存
    :return:
    '''
    facnum.clear()
    try:
        res = SysCfg({
            'name': 'FAC_NUM',
        }).get_one()

        facnum.append(res.value)

        print('initialize_facnum 猪场代码载入内存成功')
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_1002'])


@asyncFunc
def initialize_facnum_async():
    '''
    分配子线程处理
    :return:
    '''
    initialize_facnum()


def facnum_exist(fac):
    '''
    检查输入的 facnum 是否存在
    :return:
    '''
    try:
        return fac in facnum
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_2003'])
