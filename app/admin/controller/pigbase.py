# coding: utf8
'种猪列表相关操作'

# 种猪基础信息
# 基础信息查看，时间限定，种猪号限定，测定站限定

from flask import request
from app.admin import admin
from app.admin.logic.piglist import get_piglist_from_station_action
from app.admin.logic.pigbase import add_one_record_action
from app.models import PigBase
from app.common.util import error_response, success_response, error_logger, get_now_timestamp
from app.common.memory.piglist import initialize_piglist, get_pig_info
from app.common.memory.stationlist import stationid_exist
from app.common.errorcode import error_code

@admin.route('/admin/pigbase/add_one_record', methods=['POST'])
def add_one_record():
    '''
    种猪一次采食，数据插入表中
    :return:
    '''
    try:
        request_data = request.json
        param_checker = add_one_record_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        # 需要使用到的数据初始化
        earid = request_data.get('earid')
        stationid = request_data.get('stationid')

        # 种猪身体信息相关指标
        food_intake = request_data.get('food_intake')
        weight = request_data.get('weight')
        body_long = request_data.get('body_long')
        body_width = request_data.get('body_width')
        body_height = request_data.get('body_height')
        # 系统初期没有这些指标
        body_temp = 0 if request_data.get('body_temp') == None else request_data.get('body_temp')
        env_temp = 0 if request_data.get('env_temp') == None else request_data.get('env_temp')
        env_humi = 0 if request_data.get('env_humi') == None else request_data.get('env_humi')
        # 时间相关的指标
        start_time = request_data.get('start_time')
        end_time = request_data.get('end_time')
        sys_time = get_now_timestamp()

        # 依据耳标号查询到种猪的 pid，animanum，earid 信息
        pig_identity_info = get_pig_info(earid, 'earid')
        pid = pig_identity_info.get('pid')

        if stationid_exist(stationid):
            print('测定站存在')
        else:
            print('测定站不存在')

        print('body_temp', body_temp)

        PigBase({
            'pid': pid,
            'food_intake': food_intake,
            'weight': weight,
            'body_long': body_long,
            'body_width': body_width,
            'body_height': body_height,
            'body_temp': body_temp,
            'env_temp': env_temp,
            'env_humi': env_humi,
            'start_time': start_time,
            'end_time': end_time,
            'sys_time': sys_time,
        }).add_one()

        return success_response()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1002_0001'])
        return error_response(error_code['1002_0001'])


@admin.route('/admin/pigbase/', methods=['GET'])
def get_baseinfo():
    '''
    查询种猪基础信息
    :return:
    '''
    try:
        request_data = request.json
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
