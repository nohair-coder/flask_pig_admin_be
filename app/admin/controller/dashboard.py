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
                    'id': r.id,
                    'stationid': r.stationid,
                    'status': r.status,
                    'changetime': r.changetime,
                    'errorcode': r.errorcode,
                }
            )
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5001'])
        return error_response(error_code['1000_5001'])
    return success_response(ret)
