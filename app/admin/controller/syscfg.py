# coding: utf8
'系统设置相关'

from flask import request
from app.admin import admin
from app.admin.logic.syscfg import update_kv_action
from app.models.syscfg import SysCfg, cfg_keys
from app.common.util import error_response, success_response, error_logger
from app.common.errorcode import error_code


@admin.route('/admin/syscfg/get_all_kvs', methods=['GET'])
def get_all_kvs():
    '''
    获取数据库中的所有 kv 对
    :return:
    '''
    try:
        res = SysCfg.get_all_kvs()
        ret=[]
        for r in res:
            ret.append({
                'name': r.name,
                'value': r.value,
                'comment': r.comment,
            })
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_8001'])
        return error_response(error_code['1000_8001'])
    return success_response(ret)

@admin.route('/admin/syscfg/update_kv', methods=['PUT'])
def update_kv():
    '''
    更改某个 KV 对的值
    :return:
    '''
    try:
        request_data = request.json
        param_checker = update_kv_action(request_data)
        if not param_checker['type']: return error_response(param_checker['err_msg'])
        name = request_data.get('name', None)
        value = request_data.get('value', None)

        if name == cfg_keys.get('PIG_BASE_DATA_FIELDS'):
            # 参数校验合格之后，将参数拼接成字符串
            value = ','.join(value)
        if not name:
            return error_response('缺少属性名')
        if not value:
            return error_response('缺少属性值')

        SysCfg({
            'name': name,
            'value': value,
        }).update_kv()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_8002'])
        return error_response(error_code['1000_8002'])
    return success_response()
