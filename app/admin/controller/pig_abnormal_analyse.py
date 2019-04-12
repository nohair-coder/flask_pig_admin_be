# coding: utf8
'测定站周采食量统计'

from flask import request

from app import db
from app.admin import admin
from app.admin.logic.pig_abnormal_analyse import get_pig_abnormal_analyse_info_action
from app.common.errorcode import error_code
from app.common.util import error_response, success_response, error_logger
from app.common.util.time import transform_time, get_date_intervals
from app.models import PigList, PigDailyAssess


@admin.route('/admin/pig_abnormal_analyse/', methods=['GET'])
def get_pig_abnormal_analyse_info():
    '''
    预警分析（测定站下种猪），查询一个测定站下所有的猪的采食、体重值和同前日的差值
    :param stationId: 对应 station id
    :param startTime: 起始时间 10 位数字时间戳
    :param endTime: 起始时间 10 位数字时间戳
    :return:
    '''
    try:
        request_data = request.args
        param_checker = get_pig_abnormal_analyse_info_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationId')
        start_time = int(request_data.get('startTime'))
        end_time = int(request_data.get('endTime'))
        start_date = transform_time(start_time, '%Y%m%d')
        end_date = transform_time(end_time, '%Y%m%d')

        # 并表查询
        res = db.session.query(PigList.animalnum, PigList.earid,
                               PigDailyAssess.food_intake_total, PigDailyAssess.prev_foodintake_compare,
                               PigDailyAssess.weight_ave, PigDailyAssess.prev_weight_compare,
                               PigDailyAssess.record_date) \
            .join(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
            .filter(PigList.stationid == stationid, PigDailyAssess.record_date >= start_date,
                    PigDailyAssess.record_date <= end_date) \
            .all()

        ret = {
            'dateArr': [],  # 包含的日期区间 ['02-19', '02-20', '02-21']
            'data': [],
            # [{ animalnum, earid, '02-19': { food_intake_total, prev_foodintake_compare, weight_ave, prev_weight_compare }, ...  },]
        }

        date_arr = get_date_intervals(start_time, end_time)  # ['02-19', '02-20', '02-21']
        ret_data = []
        temp_ret_data = {}  # { earid: {xxx} }

        # 构建一个这段日期的数组
        print('日期数组', date_arr)

        for v in res:
            if temp_ret_data.get(v.earid):
                # 内部已经有该耳标号的记录了，只需要把对应日期的数据填充进去
                temp_ret_data[v.earid][v.record_date.strftime('%m%d')] = {
                    'food_intake_total': v.food_intake_total,
                    'prev_foodintake_compare': v.prev_foodintake_compare,
                    'weight_ave': v.weight_ave,
                    'prev_weight_compare': v.prev_weight_compare,
                }
            else:
                # 内部没有记录，则添加该耳标号的一个日期的记录
                temp_ret_data[v.earid] = {
                    'animalNum': v.animalnum,
                    'earId': v.earid,
                    v.record_date.strftime('%m%d'): {
                        'food_intake_total': v.food_intake_total,
                        'prev_foodintake_compare': v.prev_foodintake_compare,
                        'weight_ave': v.weight_ave,
                        'prev_weight_compare': v.prev_weight_compare,
                    }
                }

        for td_earid in temp_ret_data:
            one_pig_data = temp_ret_data[td_earid]
            for d in date_arr:
                # 对没有数据的日期进行数据填充
                if not one_pig_data.get(d):
                    one_pig_data[d] = {
                        'food_intake_total': 0,
                        'prev_foodintake_compare': 0,
                        'weight_ave': 0,
                        'prev_weight_compare': 0,
                    }

            ret_data.append(one_pig_data)

            ret['dateArr'] = date_arr
            ret['data'] = ret_data

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1006_0001'])
        return error_response(error_code['1006_0001'])
