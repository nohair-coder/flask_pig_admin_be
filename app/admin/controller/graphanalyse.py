# coding: utf8
'图表分析相关接口'

from flask import request

from app import db
from app.admin import admin
from app.admin.logic.graphanalyse import food_intake_interval_analysis_action
from app.common.errorcode import error_code
from app.common.util import error_response, success_response, error_logger
from app.models import PigList, PigBase


@admin.route('/admin/graphanalyse/food_intake_interval_analysis/', methods=['GET'])
def food_intake_interval_analysis():
    '''
    采食量区间分析
    :param stationId: 测定站 id
    :param starTime: 开始时间（代表当天的时间戳 10 位）
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

        ret = {
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

        for item in res:
            record_count = record_count + 1
            if item.food_intake < 200:
                ret['0-200'] = ret['0-200'] + 1
            elif item.food_intake < 400:
                ret['200-400'] = ret['200-400'] + 1
            elif item.food_intake < 600:
                ret['400-600'] = ret['400-600'] + 1
            elif item.food_intake < 800:
                ret['600-800'] = ret['600-800'] + 1
            elif item.food_intake < 1000:
                ret['800-1000'] = ret['800-1000'] + 1
            elif item.food_intake < 1200:
                ret['1000-1200'] = ret['1000-1200'] + 1
            elif item.food_intake < 1400:
                ret['1200-1400'] = ret['1200-1400'] + 1
            elif item.food_intake < 1600:
                ret['1400-1600'] = ret['1400-1600'] + 1
            else:
                ret['>1600'] = ret['>1600'] + 1

        if record_count != 0:
            # 计算百分数
            for k in ret:
                ret[k] = round(ret[k] / record_count, 2)

        ret['count'] = record_count

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1005_0001'])
        return error_response(error_code['1005_0001'])
