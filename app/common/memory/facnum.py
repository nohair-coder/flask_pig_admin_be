# coding: utf8
'内存中存储一份猪场代码信息'

from app.models import SysCfg
from app.common.util import error_logger
from app.common.errorcode import error_code
from app.common.util import asyncFunc

facnum = []

@asyncFunc
def initialize_facnum(fac=facnum):
    '''
    从数据库中获取数据到内存
    :return:
    '''
    fac.clear()
    try:
        res = SysCfg({
            'name': 'FAC_NUM',
        }).get_one()

        fac.append(res.value)
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_0002'])


def facnum_exist(fac):
    '''
    检查输入的 facnum 是否存在
    :return:
    '''
    try:
        return fac in facnum
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_0003'])
