# coding: utf8
from app.common.config.define_name import define_name, define_name_pigbase
from app.common.memory.facnum import facnum_exist
from app.common.memory.piglist import animalnum_exist, earid_exist
from app.common.memory.stationlist import stationid_exist
from app.common.util.input_checker import param_err, check_len, is_none


def add_one_record_action(params):
    '''
    种猪一次采食，数据插入表中 参数校验
    :param params:
    :return:
    '''
    # 测定站只会将 earid 传输过来，从数据库中获取到 earid 对应的 pid，stationid，animalnum 等相关信息
    earid = params.get('earid')
    stationid = params.get('stationid')

    food_intake = params.get('food_intake')
    weight = params.get('weight')
    body_long = params.get('body_long')
    body_width = params.get('body_width')
    body_height = params.get('body_height')
    body_temp = params.get('body_temp')
    env_temp = params.get('env_temp')
    env_humi = params.get('env_humi')
    start_time = params.get('start_time')
    end_time = params.get('end_time')

    print(params)

    if is_none(earid) or not check_len(earid, 12, 'eq'):
        return param_err(define_name['earid'])

    if is_none(stationid):
        return param_err(define_name['station'])

    if is_none(food_intake):
        return param_err(define_name_pigbase['food_intake'])

    if is_none(weight):
        return param_err(define_name_pigbase['weight'])

    if is_none(body_long):
        return param_err(define_name_pigbase['body_long'])

    if is_none(body_width):
        return param_err(define_name_pigbase['body_width'])

    if is_none(body_height):
        return param_err(define_name_pigbase['body_height'])

    # if is_none(body_temp):
    #     return param_err(define_name_pigbase['body_temp'])
    #
    # if is_none(env_temp):
    #     return param_err(define_name_pigbase['env_temp'])
    #
    # if is_none(env_humi):
    #     return param_err(define_name_pigbase['env_humi'])

    if is_none(start_time):
        return param_err(define_name_pigbase['start_time'])

    if is_none(end_time):
        return param_err(define_name_pigbase['end_time'])

    return dict(type=True)
