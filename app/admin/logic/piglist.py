# coding: utf8
from app.common.util.input_checker import param_err, check_len, is_none
from app.common.config.define_name import define_name
from app.common.memory.stationlist import stationid_exist
from app.common.memory.piglist import animalnum_exist, earid_exist


def get_piglist_from_station_action(params):
    '''
    按测定站查询测定站下的所有猪信息 参数校验
    :param params:
    :return:
    '''
    stationid = params.get('stationid')

    if is_none(stationid) or not check_len(stationid, 12, 'le'):
        return param_err(define_name['station'])

    return dict(type=True)

def entry_one_action(params):
    '''
    入栏一头猪 参数校验
    :param params:
    :return:
    '''
    facnum = params.get('facnum')
    animalnum = params.get('animalnum')
    earid = params.get('earid')
    stationid = params.get('stationid')

    if is_none(facnum) or not check_len(facnum, 4, 'eq'):
        return param_err(define_name['facnum'])
    if is_none(stationid) or not stationid_exist(stationid):
        return param_err(define_name['station'])
    if is_none(animalnum) or not check_len(animalnum, 12, 'eq'):
        return param_err(define_name['animalnum'])
    if animalnum_exist(animalnum):
        return dict(type=False, err_msg=define_name['animalnum'] + '已经存在')
    if is_none(earid) or not check_len(earid, 12, 'eq'):
        return param_err(define_name['earid'])
    if earid_exist(earid):
        return dict(type=False, err_msg=define_name['earid'] + '已经存在')

    return dict(type=True)
