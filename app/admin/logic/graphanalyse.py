# coding: utf8
from app.common.config.define_name import define_name, define_name_pigbase, define_name_pig_daily_assess
from app.common.util.input_checker import param_err, check_len, is_none, check_in


def food_intake_interval_analysis_action(params):
    stationid = params.get('stationId')
    start_time = params.get('startTime')
    end_time = params.get('endTime')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err(define_name['stationid'])

    if is_none(start_time):
        return param_err('开始时间')

    if is_none(end_time):
        return param_err('结束时间')

    return dict(type=True)


def weight_change_action(params):
    type = params.get('type')
    start_time = params.get('startTime')
    end_time = params.get('endTime')
    stationid = params.get('stationId')
    pid = params.get('pid')

    if not check_in(type, ('station', 'pig')):
        return param_err('查询类型（测定站或者种猪）')

    if type == 'station':
        if is_none(stationid) or not check_len(stationid, 12, 'le'):
            return param_err(define_name['stationid'])

    if is_none(start_time):
        return param_err('开始时间')

    if is_none(end_time):
        return param_err('结束时间')

    if type == 'pig':
        if is_none(pid):
            return param_err('种猪 id')

    return dict(type=True)
