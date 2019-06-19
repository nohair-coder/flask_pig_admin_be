# coding: utf8

'每隔 30 秒进行测定站的数据同步任务'

from threading import Timer
from app.models import StationInfo
from app.common.util import get_now_time

def sync_stationinfo():
    '''
    执行同步测定站状态定时任务
    每隔30秒执行一次，每次先从数据库获取到所有测定站的 stationid，再循环式的查询测定站的状态
    :return:
    '''
    # 获取到所有测定站的id
    print('同步测定站状态 ----------------->>> ' + get_now_time('%Y/%m/%d %H:%M:%S'))
    original_station_list =  StationInfo().get_all_station()
    # 获取到所有测定站运行状态的 list => [{ 'stationid', 'status', 'errorcode' }]
    station_running_info_list = get_all_station_running_info(original_station_list)
    # 将最新的状态数据更新到数据库
    update_all_station_running_info(station_running_info_list)
    Timer(5, sync_stationinfo).start() # 执行定时处理


def update_all_station_running_info(station_running_info_list):
    '''
    更改所有测定站的状态信息
    :return:
    '''
    for v in station_running_info_list:
        StationInfo(v).update_one()

def get_all_station_running_info(original_station_list):
    station_running_info_list = []
    for v in original_station_list:
        stationid = v.stationid
        # 获取到单个测定站的状态
        info = getDeviceStatus(stationid)
        # 构建数据库相同的字段，直接写入
        station_running_info_list.append({
            'stationid': stationid,
            'status': info[0].lower(), # 需要小写插入数据库
            'errorcode': info[1]
        })
    return station_running_info_list

def getDeviceStatus(stationid):
    '''
    从 CAN 通信模块获取到测定站的数据
    :return:
    '''
    return ['ON', '00000']
