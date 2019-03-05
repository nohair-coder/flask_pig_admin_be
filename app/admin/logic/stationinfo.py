# coding: utf8
from app.common.util.input_checker import param_err, check_len, check_in, is_none, check_is_errorcode

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

def update_station_action(params):
    '''
    编辑加测定站 的数据校验
    :param params:
    :return:
    '''
    stationid = params.get('stationid')
    comment = params.get('comment')
    status = params.get('status')
    errorcode = params.get('errorcode')


    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        # 必须有 测定站id
        return param_err('测定站')
    if not is_none(comment) and not check_len(comment, 50, 'le'):
        # 可以没有 comment，如果有，则必须限制长度
        return param_err('备注长度')
    if not is_none(status) and not check_in(status, ('on', 'off')):
        # 可以没有 status，如果有，则只能 on 或者 off
        return param_err('测定站状态')
    if not is_none(errorcode) and not check_is_errorcode(errorcode):
        # 可以没有 status，如果有，则只能 on 或者 off
        return param_err('故障码')

    return dict(type=True)
