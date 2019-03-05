# coding: utf8
'种猪列表相关操作'

# 入栏 -> 入栏信息修改，自动全部重写
# 出栏 -> 单头出栏，整体出栏


from flask import request
from app.admin import admin
from app.admin.logic.piglist import get_piglist_from_station_action, entry_one_action
from app.models import PigList
from app.common.util import error_response, success_response, error_logger, get_now_timestamp
from app.common.memory.stationlist import initialize_station_list, stationid_exist
from app.common.errorcode import error_code

@admin.route('/admin/piglist/get_piglist_from_station/', methods=['GET'])
def get_piglist_from_station():
    '''
    查询一栏里面的所有猪的相关信息
    :return:
    '''
    try:
        request_data = request.args
        param_checker = get_piglist_from_station_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationid')
        piglist_res = PigList({
            'stationid': stationid,
        }).get_from_station()

        ret = []

        for r in piglist_res:
            ret.append({
                'id': r.id, # 记录的 id
                'facnum': r.facnum,
                'animalnum': r.animalnum,
                'earid': r.earid,
                'stationid': r.stationid,
                'entry_time': r.entry_time,
            })

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1001_0001'])
        return error_response(error_code['1001_0001'])

@admin.route('/admin/piglist/entry_one/', methods=['POST'])
def entry_one():
    '''
    入栏一头猪
    :return:
    '''
    try:
        request_data = request.json
        param_checker = entry_one_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        facnum = request_data.get('facnum')
        animalnum = request_data.get('animalnum')
        earid = request_data.get('earid')
        stationid = request_data.get('stationid')
        entry_time = get_now_timestamp()

        pig_data = {
            'facnum': facnum,
            'stationid': stationid,
            'animalnum': animalnum,
            'earid': earid,
            'entry_time': entry_time,
        }

        PigList(pig_data).entry_one()

        return success_response(pig_data)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1001_0002'])
        return error_response(error_code['1001_0002'])


