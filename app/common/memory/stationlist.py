# coding: utf8
'内存中存储一份测定站信息'

from app.common.errorcode import error_code
from app.common.util import asyncFunc
from app.common.util import error_logger
from app.models import StationInfo

station_list = []


def initialize_station_list():
    '''
    存数据库中获取数据到内存
    :return:
    '''
    # 将原引用中的数据全部清除掉，在重新存入数据
    station_list.clear()

    try:
        res = StationInfo().get_all_station()
        for r in res:
            station_list.append(r.stationid)

        print('initialize_station_list 测定站信息载入内存成功')
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_0001'])

@asyncFunc
def initialize_station_list_async():
    '''
    分配子线程处理
    :return:
    '''
    initialize_station_list()


def stationid_exist(stationid):
    '''
    检查测定站号是否在内存中的测定站列表中
    :return:
    '''
    return stationid in station_list
