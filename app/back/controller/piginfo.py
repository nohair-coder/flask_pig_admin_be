# coding: utf8
'种猪信息'

from flask import request, json
import time
from app.back import back
from app.common.auth import admin_login_req
from app.back.logic.piginfo import insert_piginfo_action
from app.models import PigInfo
from app.common.util import error_response, success_response, error_logger, warning_logger, info_logger
from app.common.errorcode import error_code


@back.route('/piginfo/insert_piginfo/', methods=['POST'])
@admin_login_req
def insert_piginfo():
    '''
    以模板的形式渲染页面
    '''
    request_data = request.json
    param_checker = insert_piginfo_action(request_data)
    if not param_checker['type']: return json.jsonify({'success': False, 'err_msg': param_checker['err_msg']})

    new_pig_info = PigInfo(dict(
        earid=request_data.get('earid'),
        stationid=request_data.get('stationid'),
        foodintake=request_data.get('foodintake'),
        weight=request_data.get('weight'),
        bodylong=request_data.get('bodylong'),
        bodywidth=request_data.get('bodywidth'),
        bodyheight=request_data.get('bodyheight'),
        bodytemperature=request_data.get('bodytemperature'),
        stationtime=request_data.get('stationtime'),
        systime = int(time.time())
    ))

    try:
        # 插入传入的数据和数据模型不一致的时候，或者由于其他原因插入失败的时候，或报异常
        new_pig_info.add_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_0001'])
        return error_response(error_code['1000_0001'])
    return success_response()
