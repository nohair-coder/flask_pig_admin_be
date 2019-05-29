# coding: utf8
from app.common.config.define_name import define_name
from app.common.memory.facnum import facnum_exist
from app.common.memory.piglist import animalnum_exist, earid_exist
from app.common.memory.stationlist import stationid_exist
from app.common.util.input_checker import param_err, check_len, is_none


def get_piglist_from_station_action(params):
    '''
    按测定站查询测定站下的所有猪信息 参数校验
    :param params:
    :return:
    '''
    stationid = params.get('stationId')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err(define_name['stationid'])
    if not stationid_exist(stationid):
        return dict(type=False, err_msg=define_name['stationid'] + '不存在')

    return dict(type=True)


def entry_one_action(params):
    '''
    入栏一头猪 参数校验
    :param params:
    :return:
    '''
    pid = params.get('pid')
    animalnum = params.get('animalNum')
    earid = params.get('earId')
    stationid = params.get('stationId')

    if is_none(pid) or not check_len(pid, 15, 'le'):
        return param_err(define_name['pid'])

    if is_none(stationid):
        return param_err(define_name['station'])
    if not stationid_exist(stationid):
        return dict(type=False, err_msg=define_name['stationid'] + '不存在')

    if is_none(animalnum) or not check_len(animalnum, 15, 'le'):
        return param_err(define_name['animalnum'])

    if is_none(earid) or not check_len(earid, 12, 'le'):
        return param_err(define_name['earid'])


    return dict(type=True)


def exit_one_action(params):
    '''
    出栏一头猪 参数校验
    :param params:
    :return:
    '''
    record_id = params.get('recordId')

    if is_none(record_id):
        return param_err('记录 id')

    return dict(type=True)


def exit_one_station_action(params):
    '''
    出栏一个测定站的所有猪
    :param params:
    :return:
    '''
    stationid = params.get('stationId')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err(define_name['stationid'])
    if not stationid_exist(stationid):
        return dict(type=False, err_msg=define_name['stationid'] + '不存在')

    return dict(type=True)


def update_piginfo_action(params):
    '''
    更改一头种猪信息 参数校验
    :param params:
    :return:
    '''
    pid = params.get('pid')
    recordId = params.get('recordId')
    animalnum = params.get('animalNum')
    earid = params.get('earId')

    if is_none(pid) or not check_len(pid, 15, 'le'):
        return param_err(define_name['pid'])

    if is_none(animalnum) or not check_len(animalnum, 15, 'le'):
        return param_err(define_name['animalnum'])

    if is_none(earid) or not check_len(earid, 12, 'le'):
        return param_err(define_name['earid'])
    # 检测耳标号是否已经存在
    # if earid_exist(earid):
    #     return dict(type=False, err_msg=define_name['earid'] + '已经存在')

    return dict(type=True)
