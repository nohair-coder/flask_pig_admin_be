# coding: utf8
from app.common.config.define_name import define_name, define_name_pigbase, define_name_pig_daily_assess
from app.common.util.input_checker import param_err, check_len, is_none


def get_station_weekly_assessment_info_action(params):
    '''
    测定站周采食量统计 参数校验
    :param params:
    :return:
    '''
    stationid = params.get('stationId')
    start_time = params.get('startTime')
    end_time = params.get('endTime')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err(define_name['stationid'])

    if is_none(start_time):
        return param_err(define_name_pig_daily_assess['start_time'])

    if is_none(end_time):
        return param_err(define_name_pig_daily_assess['end_time'])

    return dict(type=True)
