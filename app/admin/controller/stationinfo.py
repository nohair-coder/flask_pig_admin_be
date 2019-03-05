# coding: utf8
'仪表盘：测定站运行状态'

from flask import request
from app.admin import admin
from app.admin.logic.stationinfo import add_station_action, delete_station_action, update_station_action
from app.models import StationInfo
from app.common.util import error_response, success_response, error_logger, get_now_timestamp
from app.common.memory.stationlist import initialize_station_list, stationid_exist
from app.common.errorcode import error_code


@admin.route('/admin/stationinfo/', methods=['GET'])
def get_all_station():
    '''
    获取所有测定站信息
    :return:
    '''
    try:
        res = StationInfo().get_all_station()
        station_off = [] # off 状态的排在前面
        station_err = [] # err 状态排在中间
        station_on = [] # on 正常状态的排在第三类
        for r in res:
            if r.status == 'off':
                station_off.append({
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'comment': r.comment,
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                })
            elif r.status == 'on' and r.errorcode != '00000':
                station_err.append({
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'comment': r.comment,
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                })
            else:
                station_on.append({
                    'id': r.id, # 记录的 id
                    'stationid': r.stationid.lstrip('0'), # 测定站 id
                    'comment': r.comment,
                    'status': r.status, # 测定站状态
                    'changetime': r.changetime, # 测定站状态修改时间
                    'errorcode': r.errorcode, # 错误码
                })

        ret = station_off + station_err + station_on
        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5001'])
        return error_response(error_code['1000_5001'])

@admin.route('/admin/stationinfo/', methods=['POST'])
def add_station():
    '''
    添加一条测定站记录
    :return:
    '''
    try:
        # 参数校验
        request_data = request.json
        param_checker = add_station_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationid')
        if stationid_exist(stationid): return error_response('测定站已存在')

        comment = request_data.get('comment')
        status = request_data.get('status')

        # 将该条记录添加到数据库中
        ret = StationInfo({
            'stationid': stationid,
            'comment': comment,
            'status': status,
            'errorcode': '00000',
            'changetime': get_now_timestamp(),
        }).add_one()

        # 重新获取新的测定站号列表数据
        initialize_station_list()

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5002'])
        return error_response(error_code['1000_5002'])

@admin.route('/admin/stationinfo/', methods=['DELETE'])
def delete_station():
    '''
    删除一个测定站记录
    :return:
    '''
    try:
        # 参数校验
        request_data = request.json
        param_checker = delete_station_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationid')
        if not stationid_exist(stationid): return error_response('测定站不存在')

        # 将记录删除
        ret = StationInfo({
            'stationid': stationid,
        }).delete_one()

        # 重新获取新的测定站号列表数据
        initialize_station_list()

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5003'])
        return error_response(error_code['1000_5003'])

@admin.route('/admin/stationinfo/', methods=['PUT'])
def update_station():
    '''
    更改一个测定站的记录信息
    :return:
    '''
    try:
        # 参数校验
        request_data = request.json
        param_checker = update_station_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationid')
        if not stationid_exist(stationid): return error_response('测定站不存在')

        comment = request_data.get('comment')
        status = request_data.get('status')
        errorcode = request_data.get('errorcode')
        changetime = get_now_timestamp()

        # 将记录修改
        StationInfo({
            'stationid': stationid,
            'comment': comment,
            'status': status,
            'errorcode': errorcode,
            'changetime': changetime,
        }).update_one()

        return success_response()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_5004'])
        return error_response(error_code['1000_5004'])
