# coding: utf8
'种猪列表相关操作'

# 入栏 -> 入栏信息修改，自动全部重写
# 出栏 -> 单头出栏，整体出栏


from flask import request
from app.admin import admin
from app.admin.logic.piglist import get_piglist_from_station_action, entry_one_action, exit_one_action, exit_one_station_action, update_piginfo_action
from app.models import PigList
from app.common.util import error_response, success_response, error_logger, get_now_timestamp
from app.common.memory.piglist import initialize_piglist
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
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationid')
        noexit = False if request_data.get('noexit') == 'false' else True # 默认 为 True，不查询已经出栏的

        piglist_res = PigList({
            'stationid': stationid,
        }).get_from_station(noexit)

        ret = []

        for r in piglist_res:
            ret.append({
                'id': r.id, # 记录的 id
                'facnum': r.facnum,
                'animalnum': r.animalnum,
                'earid': r.earid,
                'stationid': r.stationid,
                'entry_time': r.entry_time,
                'exit_time': r.exit_time,
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
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

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

        initialize_piglist()

        return success_response(pig_data)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1001_0002'])
        return error_response(error_code['1001_0002'])

@admin.route('/admin/piglist/exit_one/', methods=['PUT'])
def exit_one():
    '''
    出栏一头猪，出栏不是删除一头猪，而是将该猪的出栏时间填充上即可
    :return:
    '''
    try:
        request_data = request.json
        param_checker = exit_one_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        id = request_data.get('id')

        PigList({
            'id': id,
            'exit_time': get_now_timestamp(),
        }).exit_one()

        initialize_piglist()

        return success_response()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1001_0003'])
        return error_response(error_code['1001_0003'])

@admin.route('/admin/piglist/exit_one_station/', methods=['PUT'])
def exit_one_station():
    '''
    出栏一个测定站的所有猪
    :return:
    '''
    try:
        request_data = request.json
        param_checker = exit_one_station_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationid')

        PigList({
            'stationid': stationid,
        }).exit_one_station(get_now_timestamp())

        initialize_piglist()

        return success_response()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1001_0004'])
        return error_response(error_code['1001_0004'])

@admin.route('/admin/piglist/update_piginfo/', methods=['PUT'])
def update_piginfo():
    '''
    修改一头种猪的信息，不包括出栏
    :return:
    '''
    try:
        request_data = request.json
        param_checker = update_piginfo_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])
        # 不需要修改测定站 id，后面猪进食的时候，系统会自动将猪所属哪个测定站作比对，确定是否进行修正（换栏智能处理）
        #------------------------------------------------
        id = request_data.get('id')
        facnum = request_data.get('facnum')
        animalnum = request_data.get('animalnum')
        earid = request_data.get('earid')

        PigList({
            'id': id,
            'facnum': facnum,
            'animalnum': animalnum,
            'earid': earid,
        }).update_piginfo()

        initialize_piglist()

        return success_response()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1001_0005'])
        return error_response(error_code['1001_0005'])
