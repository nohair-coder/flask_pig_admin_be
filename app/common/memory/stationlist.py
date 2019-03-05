# coding: utf8
'内存中存储一份测定站信息'

from app.models import StationInfo
from app.common.util import error_logger
from app.common.errorcode import error_code

station_list = []

def initialize_station_list(slist=station_list):
    '''
    存数据库中获取数据到内存
    :return:
    '''
    # 将原引用中的数据全部清除掉，在重新存入数据
    slist.clear()

    try:
        res = StationInfo().get_all_station()
        for r in res:
            slist.append(r.stationid)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_0001'])

def stationid_exist(stationid):
    '''
    检查测定站号是否在内存中的测定站列表中
    :return:
    '''
    return stationid in station_list

