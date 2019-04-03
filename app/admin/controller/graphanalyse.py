# coding: utf8
'图表分析相关接口'

from flask import request

from app import db
from app.admin import admin
from app.admin.logic.graphanalyse import food_intake_interval_analysis_action, weight_change_action, intake_frequency_in_day_interval_action
from app.common.errorcode import error_code
from app.common.util import error_response, success_response, error_logger
from app.common.util.time import transform_time
from app.models import PigList, PigBase, PigDailyAssess


@admin.route('/admin/graphanalyse/food_intake_interval_analysis/', methods=['GET'])
def food_intake_interval_analysis():
    '''
    采食量区间分析
    :param stationId: 测定站 id
    :param startTime: 开始时间（代表当天的时间戳 10 位）
    :param endTime: 结束时间（代表当天的时间戳 10 位）
    :return:
    '''
    try:
        request_data = request.args
        param_checker = food_intake_interval_analysis_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationId')
        start_time = request_data.get('startTime')
        end_time = request_data.get('endTime')

        # 查询，时间都是用的 PigBase.start_time
        res = db.session.query(PigList.id, PigBase.food_intake) \
            .outerjoin(PigBase, PigList.id == PigBase.pid) \
            .filter(PigList.stationid == stationid, PigBase.start_time >= start_time, PigBase.start_time <= end_time) \
            .all()

        record_count = 0  # 记录的总数，用来统计百分数

        intake_percent = {
            '0-200': 0,  # [0, 200)
            '200-400': 0,  # [200, 400)
            '400-600': 0,
            '600-800': 0,
            '800-1000': 0,
            '1000-1200': 0,
            '1200-1400': 0,
            '1400-1600': 0,
            '>1600': 0,
            'count': 0,
        }

        ret = {
            'count': 0, # 统计的总量
            'data': [],
        }

        for item in res:
            record_count = record_count + 1
            if item.food_intake < 200:
                intake_percent['0-200'] = intake_percent['0-200'] + 1
            elif item.food_intake < 400:
                intake_percent['200-400'] = intake_percent['200-400'] + 1
            elif item.food_intake < 600:
                intake_percent['400-600'] = intake_percent['400-600'] + 1
            elif item.food_intake < 800:
                intake_percent['600-800'] = intake_percent['600-800'] + 1
            elif item.food_intake < 1000:
                intake_percent['800-1000'] = intake_percent['800-1000'] + 1
            elif item.food_intake < 1200:
                intake_percent['1000-1200'] = intake_percent['1000-1200'] + 1
            elif item.food_intake < 1400:
                intake_percent['1200-1400'] = intake_percent['1200-1400'] + 1
            elif item.food_intake < 1600:
                intake_percent['1400-1600'] = intake_percent['1400-1600'] + 1
            else:
                intake_percent['>1600'] = intake_percent['>1600'] + 1

        if record_count != 0:
            # 计算百分数
            for k in intake_percent:
                ret['data'].append({
                    'intake': k,
                    'frequency': round(intake_percent[k] / record_count, 2),
                })

        ret['count'] = record_count

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1005_0001'])
        return error_response(error_code['1005_0001'])


@admin.route('/admin/graphanalyse/weight_change/', methods=['GET'])
def weight_change():
    '''
    体重变化趋势图
    :param type: 是显示一个测定站的数据还是显示一头猪的数据 `station` 查询一个测定站的所有猪的体重变化，`pig` 一头猪的体重变化
    :param startTime: 开始时间（代表当天的时间戳 10 位）
    :param endTime: 结束时间（代表当天的时间戳 10 位）
    :param stationId: 测定站 id，`type=station` 时
    :param pid: 种猪 id，`type=pig` 时
    :return:
    '''
    try:
        request_data = request.args
        param_checker = weight_change_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        r_type = request_data.get('type')
        pid = request_data.get('pid')
        stationid = request_data.get('stationId')
        start_date = transform_time(int(request_data.get('startTime')), '%Y%m%d')
        end_date = transform_time(int(request_data.get('endTime')), '%Y%m%d')

        earIdArr = set()
        ret = {
            'earIdArr': [],  # 种猪号构成的数组
            'data': [],  # [ { 'date': '01-10', 'animalNum1': xx } ]
        }

        if r_type == 'station':
            # 查询一个测定站里面的猪的体重变化
            res = db.session.query(PigList.earid, PigDailyAssess.weight_ave, PigDailyAssess.record_date) \
                .outerjoin(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
                .filter(PigList.stationid == stationid, PigDailyAssess.record_date >= start_date,
                        PigDailyAssess.record_date <= end_date) \
                .all()

            date_weight_info = {}  # { '01-10': { 'animalNum1': xxx } }
            for v in res:
                date = v.record_date.strftime('%m-%d')
                earIdArr.add(v.earid)
                if date_weight_info.get(date):
                    date_weight_info[date][v.earid] = v.weight_ave
                else:
                    date_weight_info[date] = {
                        v.earid: v.weight_ave
                    }

            for date in date_weight_info:
                temp_data = {
                    'date': date,
                }

                for animalNum in date_weight_info[date]:
                    temp_data[animalNum] = date_weight_info[date][animalNum]

                ret['data'].append(temp_data)
        else:
            # r_type == 'pig'
            # 查询一头猪的体重变化
            res = db.session.query(PigList.earid, PigDailyAssess.weight_ave, PigDailyAssess.record_date) \
                .outerjoin(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
                .filter(PigList.id == pid, PigDailyAssess.record_date >= start_date,
                        PigDailyAssess.record_date <= end_date) \
                .all()

            date_weight_info = {}  # { '01-10': { 'animalNum1': xxx } }
            for v in res:
                date = v.record_date.strftime('%m-%d')
                earIdArr.add(v.earid)
                if date_weight_info.get(date):
                    date_weight_info[date][v.earid] = v.weight_ave
                else:
                    date_weight_info[date] = {
                        v.earid: v.weight_ave
                    }

            for date in date_weight_info:
                temp_data = {
                    'date': date,
                }

                for animalNum in date_weight_info[date]:
                    temp_data[animalNum] = date_weight_info[date][animalNum]

                ret['data'].append(temp_data)


        ret['earIdArr'] = list(earIdArr)
        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1005_0002'])
        return error_response(error_code['1005_0002'])


@admin.route('/admin/graphanalyse/intake_frequency_in_day_interval/', methods=['GET'])
def intake_frequency_in_day_interval():
    '''
    不同时段采食频率分布图
    :param startTime: 开始时间（代表当天的时间戳 10 位）
    :param endTime: 结束时间（代表当天的时间戳 10 位）
    :param stationId: 测定站 id
    :return:
    '''
    try:
        request_data = request.args
        param_checker = intake_frequency_in_day_interval_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationId')
        start_date = request_data.get('startTime')
        end_date = request_data.get('endTime')

        ret = {
            'count': 0,  # 统计的总量
            'data': [],  # [ { 'date': '01-10', 'animalNum1': xx } ]
        }

        # 查询一个测定站里面的猪的体重变化
        res = db.session.query(PigList.earid, PigDailyAssess.weight_ave, PigDailyAssess.record_date) \
            .outerjoin(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
            .filter(PigList.stationid == stationid, PigDailyAssess.record_date >= start_date,
                    PigDailyAssess.record_date <= end_date) \
            .all()

        date_weight_info = {}  # { '01-10': { 'animalNum1': xxx } }
        for v in res:
            date = v.record_date.strftime('%m-%d')
            if date_weight_info.get(date):
                date_weight_info[date][v.earid] = v.weight_ave
            else:
                date_weight_info[date] = {
                    v.earid: v.weight_ave
                }

        for date in date_weight_info:
            temp_data = {
                'date': date,
            }

            for animalNum in date_weight_info[date]:
                temp_data[animalNum] = date_weight_info[date][animalNum]

            ret['data'].append(temp_data)

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1005_0003'])
        return error_response(error_code['1005_0003'])
