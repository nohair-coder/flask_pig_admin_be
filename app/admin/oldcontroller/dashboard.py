# coding: utf8
'仪表盘：测定站运行状态'

from app.admin import admin
from app.models import StationInfo
from app.common.util import error_response, success_response, error_logger
from app.common.errorcode import error_code


@admin.route('/admin/dashboard/stationinfo/', methods=['GET'])
def stationinfo():
    try:
        res = StationInfo.query.all()
        station_off = [] # off 状态的排在前面
        station_err = [] # err 状态排在中间
        station_on = [] # on 正常状态的排在第三类
        for r in res:
            if r.status == 'off':
                station_off.append({
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                })
            elif r.status == 'on' and r.errorcode != '00000':
                station_err.append({
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                })
            else:
                station_on.append({
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                })

        ret = station_off + station_err + station_on
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5001'])
        return error_response(error_code['1000_5001'])
    return success_response(ret)
