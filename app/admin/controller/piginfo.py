# coding: utf8
'种猪信息查询'

from flask import request
from app.admin import admin
from app.models import PigInfo
from app.common.util import error_response, success_response, error_logger, get_now_timestamp
from app.common.errorcode import error_code
from app.config import length_per_page

@admin.route('/admin/piginfo/', methods=['POST'])
def station_piginfo():
    '''
    获取种猪信息
    :param type: all、station、one
    :param offset: 跳过的条数
    :param earid: 对应 pig
    :param stationid: 对应 station
    :return:
    '''
    request_data = request.json
    type = request_data.get('type', None)
    from_id = request_data.get('fromId', None)
    res=None
    ret = {
        'list': [],
        'lastId': None,
        'hasNextPage': False,
    }
    try:
        from_time = request_data.get('fromTime')  # 直接接收10位的数字时间戳
        from_time = 0 if not from_time else from_time
        end_time = request_data.get('endTime', get_now_timestamp())  # 直接接收10位的数字时间戳
        end_time = 0 if not end_time else end_time
        if type == 'station':
            # 'station'
            stationid = request_data.get('stationid', '').zfill(12)
            if stationid != None:
                res = PigInfo.get_station(stationid, from_id, from_time, end_time)
            else:
                return error_response('缺少测定站号')

        elif type == 'one':
            # 'one'
            earid = request_data.get('earid', '').zfill(12)
            if earid != None:
                res = PigInfo.get_one(earid, from_id, from_time, end_time)
            else:
                return error_response('缺少耳标号')

        else:
            # all
            res = PigInfo.get_all(from_id, from_time, end_time)

        # k v 赋值
        for ind, item in enumerate(res):
            if ind < length_per_page:
                ret['list'].append({
                    'id': item.id,
                    'earid': item.earid.lstrip('0'),
                    'stationid': item.stationid.lstrip('0'),
                    'foodintake': item.foodintake,
                    'weight': item.weight,
                    'bodylong': item.bodylong,
                    'bodywidth': item.bodywidth,
                    'bodyheight': item.bodyheight,
                    'bodytemperature': item.bodytemperature,
                    'systime': item.systime,
                    'stationtime': item.stationtime,
                })
            if ind == length_per_page:
                ret['hasNextPage'] = True

        if ret['hasNextPage']:
            ret['lastId'] = ret['list'][-1:][0].get('id') # 获取最后一条记录的 id， 在下一次
        else:
            ret['lastId'] = 0
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_6001'])
        return error_response(error_code['1000_6001'])
    return success_response(ret)
