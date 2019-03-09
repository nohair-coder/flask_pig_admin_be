# coding: utf8
'种猪列表相关操作'

# 种猪基础信息
# 基础信息查看，时间限定，种猪号限定，测定站限定

from flask import request
from app.admin import admin
from app.admin.logic.piglist import get_piglist_from_station_action
from app.admin.logic.pigbase import add_one_record_action
from app.models import PigBase, StationInfo, PigList
from app.common.util import error_response, success_response, error_logger, get_now_timestamp, get_now_time
from app.common.memory.piglist import initialize_piglist_async, get_pig_info
from app.common.memory.stationlist import stationid_exist, initialize_station_list_async
from app.common.memory.daily_intake_start_time import is_after_intake_start_time
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

        # 从内存中 依据耳标号查询到种猪的 pid，animanum，earid 信息
        pig_identity_info = get_pig_info(earid, 'earid')

        if pig_identity_info:
            pid = pig_identity_info.get('pid')

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
            # 检查是否更换了测定站
            if stationid != pig_identity_info.get('stationid'):
                PigList({
                    'id': pid,
                    'stationid': stationid,
                }).update_stationid()
                initialize_piglist_async()
        else:
            # 1、新增种猪记录
            # 2、刷新内存数据
            # 3、获取到 pid，将基础数据写入
            new_record = PigList({
                'facnum': '', # 系统自动生成的记录，不分配 facnum
                'stationid': stationid,
                'animalnum': '', # 系统自动生成的记录，不分配种猪号
                'earid': earid,
                'entry_time': get_now_timestamp(),
            }).entry_one()
            PigBase({
                'pid': new_record.id,
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
            initialize_piglist_async()

        # ------------------- 智能测定站转换 -------------------
        # 如果测定站不存在，说明种猪被投放到了一个新的测定站
        # 需要新创建一个测定站
        if not stationid_exist(stationid):
            # 1、先创建测定站
            StationInfo({
                'stationid': stationid,
                'comment': '测定站号自动生成，生成时间 ' + get_now_time('%Y年%m月%d日 -- %H:%M:%S'),
                'status': 'on',
                'changetime': get_now_timestamp(),
                'errorcode': '00000',
            }).add_one()
            # 刷新内存中的测定站数据
            initialize_station_list_async()

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


# @Todo
# 1、指定时间之后的第一次数据的采集
# 2、每天的体重均值，进食次数 => 表的完善
