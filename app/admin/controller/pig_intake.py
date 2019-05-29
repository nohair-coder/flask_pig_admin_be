# coding: utf8
'个体采食量趋势图、采食总量'

from flask import request

from app import db
from app.admin import admin
from app.admin.logic.pig_intake import intake_trend_action, total_perstation_action
from app.common.errorcode import error_code
from app.common.util import error_response, success_response, error_logger
from app.common.util.time import transform_time
from app.models import PigDailyAssess, PigList


@admin.route('/admin/pig_intake/intake_trend/', methods=['GET'])
def intake_trend():
    '''
    个体采食量趋势图数据获取
    :param pid: 种猪 id
    :param startTime: 起始时间 10 位数字时间戳
    :param endTime: 起始时间 10 位数字时间戳
    :return:
    '''
    try:
        request_data = request.args
        param_checker = intake_trend_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        pid = request_data.get('pid')
        start_date = transform_time(int(request_data.get('startTime')), '%Y%m%d')
        end_date = transform_time(int(request_data.get('endTime')), '%Y%m%d')

        # 查询
        res = db.session.query(PigDailyAssess.food_intake_total, PigDailyAssess.record_date) \
            .filter(PigDailyAssess.pid == pid, PigDailyAssess.record_date >= start_date,
                    PigDailyAssess.record_date <= end_date) \
            .all()

        ret = {
            'data': [],  # [{ date: '2019-01-02', intake_total: 100.11 }]
            'total': 0,  # 这段时间的总采食量
            'ave': 0,  # 这段时间的平均采食量
        }

        day_count = 0  # 统计的天数

        for item in res:
            ret['data'].append({
                'date': item.record_date.strftime('%m-%d'),
                'intake_total': item.food_intake_total,
            })
            ret['total'] = ret['total'] + item.food_intake_total
            day_count = day_count + 1

        ret['total'] = round(ret['total'], 2)
        if day_count:
            ret['ave'] = round(ret['total'] / day_count, 2)

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1004_0001'])
        return error_response(error_code['1004_0001'])


@admin.route('/admin/pig_intake/total_perstation/', methods=['GET'])
def total_perstation():
    '''
    测定站某日所有猪的采食总量的统计表
    :param stationId: 测定站 id
    :param time: 日期（当天开始的时间戳 10 位）
    :return:
    '''
    try:
        request_data = request.args
        param_checker = total_perstation_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationId')
        date = transform_time(int(request_data.get('time')), '%Y%m%d')

        # 查询
        res = db.session.query(PigList.id, PigList.earid, PigList.animalnum, PigList.facnum, PigDailyAssess.food_intake_total) \
            .outerjoin(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
            .filter(PigList.stationid == stationid, PigDailyAssess.record_date == date) \
            .all()

        ret = {
            'data': [],  # [{ facNum: 'xxxx', earId: 'xxxxxxxxxxx', animalNum: 'asdasdasdasd', intake: xxx }]
            'total': 0,  # 这段时间的总采食量
            'ave': 0,  # 这段时间的平均采食量
        }

        pig_count = 0  # 统计到的种猪的头数

        for item in res:
            ret['data'].append({
                'id': item.id,
                'facNum': item.facnum,
                'earId': item.earid,
                'animalNum': item.animalnum,
                'intake': item.food_intake_total,
            })
            ret['total'] = ret['total'] + item.food_intake_total
            pig_count = pig_count + 1

        ret['total'] = round(ret['total'], 2)
        if pig_count:
            ret['ave'] = round(ret['total'] / pig_count, 2)

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1004_0001'])
        return error_response(error_code['1004_0001'])
