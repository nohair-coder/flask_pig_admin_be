# coding: utf8
from app.common.util.input_checker import param_err, check_len, check_in, is_none

def add_station_action(params):
    '''
    添加测定站 的数据校验
    :param params:
    :return:
    '''
    stationid = params.get('stationid')
    comment = params.get('comment')
    status = params.get('status')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err('测定站')
    if is_none(comment) or not check_len(comment, 50, 'le'):
        return param_err('备注长度')
    if is_none(status) or not check_in(status, ('on', 'off')):
        return param_err('测定站状态')

    return dict(type=True)

def delete_station_action(params):
    '''
    删除加测定站 的数据校验
    :param params:
    :return:
    '''
    stationid = params.get('stationid')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err('测定站')

    return dict(type=True)
