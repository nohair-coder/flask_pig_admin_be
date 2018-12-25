# coding: utf8
from app.common.util.input_checker import param_err, check_exist, check_len


def insert_piginfo_action(params):
    '''
    插入种猪信息
    :param params: 请求的 json 参数
    :return:
    '''
    earid = params.get('earid')
    stationid = params.get('stationid')
    foodintake = params.get('foodintake')
    weight = params.get('weight')
    bodylong = params.get('bodylong')
    bodywidth = params.get('bodywidth')
    bodyheight = params.get('bodyheight')
    bodytemperature = params.get('bodytemperature')
    stationtime = params.get('stationtime')

    if not check_exist(earid) or not check_len(earid, 12, 'le'):
        return param_err('耳标号')
    if not check_exist(stationid) or not check_len(stationid, 12, 'le'):
        return param_err('测定站id')
    if not check_exist(foodintake):
        return param_err('进食量')
    if not check_exist(weight):
        return param_err('体重')
    if not check_exist(bodylong):
        return param_err('体长')
    if not check_exist(bodywidth):
        return param_err('体宽')
    if not check_exist(bodyheight):
        return param_err('体高')
    if not check_exist(bodytemperature):
        return param_err('温度')
    if not check_exist(stationtime):
        return param_err('测定站的时间')

    return {'type': True}
