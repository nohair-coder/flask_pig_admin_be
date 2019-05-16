# coding: utf8
'图表分析相关接口'

from flask import request
from sqlalchemy import asc

from app import db
from app.admin import admin
from app.admin.logic.graphanalyse import food_intake_interval_analysis_action, weight_change_action, \
    intake_frequency_in_day_interval_action, daily_weight_gain_and_fcr_action
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

        s_type = request_data.get('type')
        stationid = request_data.get('stationId')
        start_time = request_data.get('startTime')
        end_time = request_data.get('endTime')

        if s_type == 'one':
            # 查询，时间都是用的 PigBase.start_time
            res = db.session.query(PigList.id, PigBase.food_intake) \
                .outerjoin(PigBase, PigList.id == PigBase.pid) \
                .filter(PigList.stationid == stationid, PigBase.start_time >= start_time,
                        PigBase.start_time <= end_time) \
                .all()
        else:
            # 查询所有测定站的数据
            res = db.session.query(PigList.id, PigBase.food_intake) \
                .outerjoin(PigBase, PigList.id == PigBase.pid) \
                .filter(PigBase.start_time >= start_time, PigBase.start_time <= end_time) \
                .all()

        record_count = 0  # 记录的总数，用来统计百分数

        intake_interval_count = {
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
            'count': 0,  # 统计的总量
            'data': [],
        }

        for item in res:
            record_count = record_count + 1
            if item.food_intake < 200:
                intake_interval_count['0-200'] = intake_interval_count['0-200'] + 1
            elif item.food_intake < 400:
                intake_interval_count['200-400'] = intake_interval_count['200-400'] + 1
            elif item.food_intake < 600:
                intake_interval_count['400-600'] = intake_interval_count['400-600'] + 1
            elif item.food_intake < 800:
                intake_interval_count['600-800'] = intake_interval_count['600-800'] + 1
            elif item.food_intake < 1000:
                intake_interval_count['800-1000'] = intake_interval_count['800-1000'] + 1
            elif item.food_intake < 1200:
                intake_interval_count['1000-1200'] = intake_interval_count['1000-1200'] + 1
            elif item.food_intake < 1400:
                intake_interval_count['1200-1400'] = intake_interval_count['1200-1400'] + 1
            elif item.food_intake < 1600:
                intake_interval_count['1400-1600'] = intake_interval_count['1400-1600'] + 1
            else:
                intake_interval_count['>1600'] = intake_interval_count['>1600'] + 1

        if record_count != 0:
            # 计算百分数
            for k in intake_interval_count:
                ret['data'].append({
                    'intake': k,
                    'count': intake_interval_count[k],
                    'frequency': round(intake_interval_count[k] / record_count, 2),
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
    :param type: 是选则的一个测定站还是所有的测定站 `all` `one`
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

        s_type = request_data.get('type')
        stationid = request_data.get('stationId')
        start_time = request_data.get('startTime')
        end_time = request_data.get('endTime')

        ret = {
            'count': 0,  # 统计的总量
            'data': [],  # [ { 'date': '01-10', 'animalNum1': xx } ]
        }

        if s_type == 'one':
            # 查询一个测定站里面的猪的体重变化
            res = db.session.query(PigList.id, PigBase.start_time) \
                .outerjoin(PigBase, PigList.id == PigBase.pid) \
                .filter(PigList.stationid == stationid, PigBase.start_time >= start_time,
                        PigBase.start_time <= end_time) \
                .all()
        else:
            # s_type == 'all' 查询所有测定站的数据
            res = db.session.query(PigList.id, PigBase.start_time) \
                .outerjoin(PigBase, PigList.id == PigBase.pid) \
                .filter(PigBase.start_time >= start_time, PigBase.start_time <= end_time) \
                .all()

        time_interval_arr = [
            '00:00-02:00',  # [0 , 2)  time_interval_arr[0]
            '02:00-04:00',  # [2 , 4)
            '04:00-06:00',
            '06:00-08:00',
            '08:00-10:00',
            '10:00-12:00',
            '12:00-14:00',
            '14:00-16:00',
            '16:00-18:00',
            '18:00-20:00',
            '20:00-22:00',
            '22:00-24:00',
        ]

        record_inter_count = [0 for i in range(12)]  # 每个时间段的记录数

        one_day_seconds = 86400
        local_time_zone_add = 28800  # 8 * 3600
        interval_seconds = 7200  # 2 * 3600

        for v in res:
            ret['count'] = ret['count'] + 1
            inter = int((v.start_time + local_time_zone_add) % one_day_seconds / interval_seconds)  # 0 , 1, 2
            record_inter_count[inter] = record_inter_count[inter] + 1
            # print(' pid => {pid}, time => {time} '.format(pid=v.id, time=v.start_time))
            # print('inter => {inter}'.format(inter=inter))

        # 构建返回的数据
        for k, v in enumerate(record_inter_count):
            if ret['count'] != 0:
                ret['data'].append({
                    'interval': time_interval_arr[k],
                    'count': v,
                    'frequency': round(v / ret['count'], 2)
                })
            else:
                ret['data'].append({
                    'interval': time_interval_arr[k],
                    'count': v,
                    'frequency': 0
                })

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1005_0003'])
        return error_response(error_code['1005_0003'])


@admin.route('/admin/graphanalyse/daily_weight_gain_and_fcr/', methods=['GET'])
def daily_weight_gain_and_fcr():
    '''
    日增重和饲料转化率统计（FCR）
    :param startTime: 开始时间（代表当天的时间戳 10 位）
    :param endTime: 结束时间（代表当天的时间戳 10 位）
    :param stationId: 测定站 id
    :return:
    '''
    try:
        request_data = request.args
        param_checker = daily_weight_gain_and_fcr_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationId')
        start_date = transform_time(int(request_data.get('startTime')), '%Y%m%d')
        end_date = transform_time(int(request_data.get('endTime')), '%Y%m%d')

        ret = []

        res = db.session.query(PigList.id, PigList.earid, PigList.animalnum, PigDailyAssess.food_intake_total,
                               PigDailyAssess.weight_ave, PigDailyAssess.record_date) \
            .outerjoin(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
            .filter(PigList.stationid == stationid, PigDailyAssess.record_date >= start_date,
                    PigDailyAssess.record_date <= end_date) \
            .order_by(asc(PigDailyAssess.record_date)) \
            .all()

        start_date_weight = {}  # 开始日期的体重 { pid: xxx } xxx 体重
        end_date_weight = {}  # 结束日期的体重 { pid: xxx } xxx 体重
        day_count = {}  # 统计的总天数 { pid: xxx } xxx 天数
        period_food_intake_total = {}  # { pid: xxx } xxx 这段时间总的采食量
        pig_info = {}  # { pid: { pid: xxx, earId: xxx, animalNum: xxx } }
        pid_set = set()

        for v in res:
            if v.id in pid_set:
                # 如果有该种猪的信息记录了
                end_date_weight[v.id] = v.weight_ave
            else:
                # 如果没有该种猪的信息记录
                pid_set.add(v.id)
                pig_info[v.id] = {
                    'pid': v.id,
                    'earId': v.earid,
                    'animalNum': v.animalnum,
                }
                start_date_weight[v.id] = v.weight_ave
                end_date_weight[v.id] = v.weight_ave
                day_count[v.id] = 0
                period_food_intake_total[v.id] = 0
            day_count[v.id] = day_count[v.id] + 1
            period_food_intake_total[v.id] = period_food_intake_total[v.id] + 1

        for pid in pid_set:
            one_pig_all_info = {
                'pid': pid,
                'earId': pig_info[pid]['earId'],
                'animalNum': pig_info[pid]['animalNum'],
                'dailyWeightGain': round((end_date_weight[pid] - start_date_weight[pid]) / day_count[pid], 3),
            }

            if (end_date_weight[pid] - start_date_weight[pid]) != 0:
                print(period_food_intake_total[pid], end_date_weight[pid] - start_date_weight[pid], round(
                    period_food_intake_total[pid] / (end_date_weight[pid] - start_date_weight[pid]), 2))
                one_pig_all_info['fcr'] = round(
                    period_food_intake_total[pid] / (end_date_weight[pid] - start_date_weight[pid]), 2)
            else:
                one_pig_all_info['fcr'] = 0

            ret.append(one_pig_all_info)

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1005_0004'])
        return error_response(error_code['1005_0004'])
