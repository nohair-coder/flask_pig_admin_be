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
        ret = []
        for r in res:
            ret.append(
                {
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                }
            )
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5001'])
        return error_response(error_code['1000_5001'])
    return success_response(ret)
