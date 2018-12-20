# coding: utf8
'种猪信息查询'

from flask import request
from app.admin import admin
from app.models import PigInfo
from app.common.util import error_response, success_response, error_logger, get_now_timestamp
from app.common.errorcode import error_code


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
    from_id = request_data.get('fromId', 0)
    res=None
    ret = []
    try:
        from_time = request_data.get('fromTime', 0)  # 直接接收10位的数字时间戳
        end_time = request_data.get('endTime', get_now_timestamp())  # 直接接收10位的数字时间戳

        if type == 'station':
            # 'station'
            stationid = request_data.get('stationid', None)
            if stationid != None:
                res = PigInfo.get_station(stationid, from_id, from_time, end_time)
            else:
                return error_response('缺少测定站号')

        elif type == 'one':
            # 'one'
            earid = request_data.get('earid', None)
            if earid != None:
                res = PigInfo.get_one(earid, from_id, from_time, end_time)
            else:
                return error_response('缺少耳标号')

        else:
            # all
            res = PigInfo.get_all(from_id, from_time, end_time)

        # k v 赋值
        for item in res:
            ret.append({
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

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_6001'])
        return error_response(error_code['1000_6001'])
    return success_response(ret)
