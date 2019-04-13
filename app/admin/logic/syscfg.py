# coding: utf8
from app.common.util.input_checker import param_err, check_len, check_in, check_arr_all_in
from app.models.syscfg import cfg_allowed_values, cfg_keys

def get_one_kv_action(params):
    name = params.get('name')
    if name not in list(cfg_keys.keys()):
        return param_err('键名')
    return dict(type=True)


def update_kv_action(params):
    '''
    更改数据库的 kv 配置，处理之前的参数合格性校验
    :param params:
    :return:
    '''
    name = params.get('name')
    value = params.get('value')

    if name == cfg_keys.get('FAC_NUM'):
        if check_len(value, 4):
            return dict(type=True)
        else:
            return param_err('猪场代码')
    elif name == cfg_keys.get('SHOW_SELECT_LANGUAGE'):
        if check_in(value, ('false', 'true')):
            return dict(type=True)
        else:
            return param_err('显示选择语言')
    elif name == cfg_keys.get('SHOW_TIME_SYNC'):
        if check_in(value, ('false', 'true')):
            return dict(type=True)
        else:
            return param_err('显示时间同步')
    elif name == cfg_keys.get('PIG_BASE_DATA_FIELDS'):
        # value 是一个数组，数组中的所有制必须在执行的列中
        if type(value) == list\
            and check_arr_all_in(value, cfg_allowed_values.get('PIG_BASE_DATA_ALLOWED_FIELDS')):
            return dict(type=True)
        else:
            return param_err('种猪基础信息')

    return param_err('键名')
