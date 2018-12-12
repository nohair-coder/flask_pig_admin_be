# coding: utf8
from app.common.util.input_checker import param_err, check_exist, check_len, check_is_timestamp_integer, \
    check_number_str_len, check_in


def insert_stationinfo_action(params):
    '''
    插入测定站信息
    :param params: 请求的 json 参数
    :return:
    '''
    stationid = params.get('stationid')
    status = params.get('status')
    changetime = params.get('changetime')
    errorcode = params.get('errorcode')

    if not check_exist(stationid) or not check_len(stationid, 12):
        return param_err('测定站id')
    if not check_exist(status) or not check_in(status, ('on', 'off')):
        return param_err('机器运行状态')
    if not check_exist(changetime) or not check_is_timestamp_integer(changetime):
        return param_err('状态变化时间')
    if not check_exist(errorcode) or not check_number_str_len(errorcode, 5):
        return param_err('故障编号')

    return {'type': True}
