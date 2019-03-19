# coding: utf8
'种猪列表相关操作'

# 种猪基础信息
# 基础信息查看，时间限定，种猪号限定，测定站限定

from flask import request

from app.admin import admin
from app.admin.logic.pigbase import add_one_record_action
from app.admin.logic.piglist import get_piglist_from_station_action
from app.common.errorcode import error_code
from app.common.memory.daily_first_intake_record import has_pig_today_intook, reset_record, is_record_outdated, add_pid
from app.common.memory.daily_intake_start_time import is_after_intake_start_time
from app.common.memory.pig_daily_assess_record import calc_today_intake
from app.common.memory.piglist import initialize_piglist_async, get_pig_info
from app.common.memory.stationlist import stationid_exist, initialize_station_list_async
from app.common.util import error_response, success_response, error_logger, get_now_timestamp, get_now_time, \
    transform_time, asyncFunc
from app.models import PigBase, StationInfo, PigList, PigDailyFirstIntake


@asyncFunc
def today_first_intook_proc(*, sys_time, pid, pigbase_id):
    '''
    判断本次采食是否是当天 intake_start_time 时间之后的首次采食
    如果是则存入 首次采食数据表，并刷新
    否则忽略
    :param sys_time: 10 位的时间戳
    :param pid: 种猪 id
    :param pigbase_id: 对应的 pigbase 表的记录 id
    :return:
    '''
    # 1、判断 sys_time 是否在当天的 intake_start_time 之后
    # 2、判断 今天的 datestring（YYYYmmdd）和内存的 datestring，今天的大于内存的则 reset_record
    # 3、相等的则再判断 pid 是否已经存在，已经存在则不处理，不存在则添加到数据库，同时更新到内存
    try:

        transformed_time = transform_time(sys_time, '%Y%m%d')

        if is_after_intake_start_time(sys_time):
            # 如果内存中的记录已经过期，则 reset_record
            if is_record_outdated(sys_time):
                reset_record(sys_time)
            # 如果该猪当天没有采食
            if not has_pig_today_intook(pid):
                PigDailyFirstIntake({
                    'pid': pid,
                    'pigbase_id': pigbase_id,
                    'record_date': transformed_time,
                }).add_one()
                # 添加到内存中之后，将 pid 也更新到内存中
                add_pid(pid)
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1002_0002'])


def daily_assess(*, pid, intake, weight, sys_time):
    '''
    日评估，每次采食都会归入到该评估中
    :param pid:
    :param intake:
    :param weight:
    :param sys_time:
    :return:
    '''
    # 将采食记录归入日采食记录
    calc_today_intake(pid, intake=intake, weight=weight, intake_date=transform_time(sys_time, '%Y%m%d'))


@admin.route('/admin/pigbase/', methods=['POST'])
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
            new_pigbase_record = PigBase({
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
            # 今日首次采食判断处理
            today_first_intook_proc(sys_time=sys_time, pid=pid, pigbase_id=new_pigbase_record.id)
            # 将当前记录归入日评估
            daily_assess(pid=pid, sys_time=sys_time, intake=food_intake, weight=weight)
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
            new_piglist_record = PigList({
                'facnum': '',  # 系统自动生成的记录，不分配 facnum
                'stationid': stationid,
                'animalnum': '',  # 系统自动生成的记录，不分配种猪号
                'earid': earid,
                'entry_time': get_now_timestamp(),
            }).entry_one()
            new_pigbase_record = PigBase({
                'pid': new_piglist_record.id,
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
            # 今日首次采食判断处理
            today_first_intook_proc(sys_time=sys_time, pid=new_piglist_record.id, pigbase_id=new_pigbase_record.id)
            # 将当前记录归入日评估
            daily_assess(pid=new_piglist_record.id, sys_time=sys_time, intake=food_intake, weight=weight)

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
        noexit = False if request_data.get('noexit') == 'false' else True  # 默认 为 True，不查询已经出栏的

        piglist_res = PigList({
            'stationid': stationid,
        }).get_from_station(noexit)

        ret = []

        for r in piglist_res:
            ret.append({
                'id': r.id,  # 记录的 id
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
        error_logger(error_code['1002_0003'])
        return error_response(error_code['1002_0003'])
