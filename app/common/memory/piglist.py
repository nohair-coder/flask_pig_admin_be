# coding: utf8
'内存中存储种猪信息列表'

from app.models import PigList
from app.common.util import error_logger
from app.common.errorcode import error_code
from app.common.util import asyncFunc

pig_animalnum_list = []
pig_earid_list = []

@asyncFunc
def initialize_piglist(animalnum_list = pig_animalnum_list, earid_list = pig_earid_list):
    '''
    从数据库中获取数据到内存
    :return:
    '''
    animalnum_list.clear()
    earid_list.clear()
    try:
        res = PigList().get_all()

        for r in res:
            animalnum_list.append(r.animalnum)
            earid_list.append(r.earid)
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_2001'])

def animalnum_exist(animalnum):
    '''
    检查 animalnum 是否已经存在
    :return:
    '''
    return animalnum in pig_animalnum_list

def earid_exist(earid):
    '''
    检查 earid 是否已经存在
    :return:
    '''
    return earid in pig_earid_list
