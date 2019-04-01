# coding: utf8
'测定站周采食量统计'

from flask import request

from app import db
from app.admin import admin
from app.admin.logic.station_weekly_assessment import get_station_weekly_assessment_info_action
from app.common.errorcode import error_code
from app.common.util import error_response, success_response, error_logger
from app.common.util.time import transform_time
from app.models import PigList, PigDailyAssess


@admin.route('/admin/station_weekly_assessment_info/', methods=['GET'])
def get_station_weekly_assessment_info():
    '''
    查询种猪的基础信息
    :param stationId: 对应 station id
    :param startTime: 起始时间 10 位数字时间戳
    :param endTime: 起始时间 10 位数字时间戳
    :return:
    '''
    try:
        request_data = request.args
        param_checker = get_station_weekly_assessment_info_action(request_data)
        if not param_checker['type']:
            error_logger(param_checker['err_msg'])
            return error_response(param_checker['err_msg'])

        stationid = request_data.get('stationId')
        start_date = transform_time(int(request_data.get('startTime')), '%Y%m%d')
        end_date = transform_time(int(request_data.get('endTime')), '%Y%m%d')

        res = db.session.query(PigList.id, PigList.facnum, PigList.animalnum, PigList.earid,
                               PigDailyAssess.food_intake_total, PigDailyAssess.record_date) \
            .join(PigDailyAssess, PigList.id == PigDailyAssess.pid) \
            .filter(PigList.stationid == stationid, PigDailyAssess.record_date >= start_date, PigDailyAssess.record_date <= end_date) \
            .all()


        # 日期转换
        date_transformer = {
            str(int(start_date) + 0): 'day1',
            str(int(start_date) + 1): 'day2',
            str(int(start_date) + 2): 'day3',
            str(int(start_date) + 3): 'day4',
            str(int(start_date) + 4): 'day5',
            str(int(start_date) + 5): 'day6',
            str(int(start_date) + 6): 'day7',
        }

        ret = []
        # { pid: { day1: xx, day2: xxx } }
        intake_date_total = {}

        # k v 赋值
        # 获取到所有的猪
        for item in res:
            if intake_date_total.get(item.id):
                intake_date_total[item.id][
                    date_transformer[item.record_date.strftime('%Y%m%d')]] = item.food_intake_total
                intake_date_total[item.id]['count'] = intake_date_total[item.id]['count'] + 1
            else:
                ret.append({
                    'pid': item.id,
                    'facNum': item.facnum,
                    'animalNum': item.animalnum,
                    'earId': item.earid,
                })
                intake_date_total[item.id] = {
                    date_transformer[item.record_date.strftime('%Y%m%d')]: item.food_intake_total,
                    'count': 1,
                }
        # 映射 day ave total 的值
        for v in ret:
            pid = v.get('pid')
            day_intake_total = intake_date_total[pid]
            v['day1'] = day_intake_total.get('day1', 0)
            v['day2'] = day_intake_total.get('day2', 0)
            v['day3'] = day_intake_total.get('day3', 0)
            v['day4'] = day_intake_total.get('day4', 0)
            v['day5'] = day_intake_total.get('day5', 0)
            v['day6'] = day_intake_total.get('day6', 0)
            v['day7'] = day_intake_total.get('day7', 0)
            v['total'] = round(v['day1'] + v['day2'] + v['day3'] + v['day4'] + v['day5'] + v['day6'] + v['day7'], 2)

            v['ave'] = round(v['total'] / day_intake_total.get('count'), 2)

        return success_response(ret)

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1003_0001'])
        return error_response(error_code['1003_0001'])
