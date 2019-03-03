# coding: utf8
'系统设置相关'

from flask import request, json
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



#
# @admin.route('/admin/errorcode/', methods=['delete'])
# def delete_errorcode():
#     '''
#     删除故障码
#     :return:
#     '''
#     try:
#         request_data = request.json
#         target_id = request_data.get('id')
#         if not target_id:
#             return error_response('缺少id')
#         StationErrorcodeReference({ 'id': target_id }).delete_one()
#     except Exception as e:
#         error_logger(e)
#         error_logger(error_code['1000_7101'])
#         return error_response(error_code['1000_7101'])
#     return success_response()
#
# @admin.route('/admin/errorcode/', methods=['post'])
# def add_errorcode():
#     '''
#     新增故障码
#     :return:
#     '''
#     try:
#         request_data = request.json
#         errorcode = request_data.get('errorcode', None)
#         comment = request_data.get('comment', None)
#         if not errorcode:
#             return error_response('缺少故障码')
#         if not comment:
#             return error_response('缺少注释')
#
#         StationErrorcodeReference({
#             'errorcode': errorcode,
#             'comment': comment,
#         }).add_one()
#     except Exception as e:
#         error_logger(e)
#         error_logger(error_code['1000_7201'])
#         return error_response(error_code['1000_7201'])
#     return success_response()
#
#
# @admin.route('/admin/errorcode/', methods=['put'])
# def update_errorcode():
#     '''
#     更改已有的故障码
#     :return:
#     '''
#     try:
#         request_data = request.json
#         id = request_data.get('id', None)
#         errorcode = request_data.get('errorcode', None)
#         comment = request_data.get('comment', None)
#         if not id:
#             return error_response('缺少记录id')
#         if not errorcode:
#             return error_response('缺少故障码')
#         if not comment:
#             return error_response('缺少注释')
#
#         StationErrorcodeReference({
#             'id': id,
#             'errorcode': errorcode,
#             'comment': comment,
#         }).update_one()
#     except Exception as e:
#         error_logger(e)
#         error_logger(error_code['1000_7301'])
#         return error_response(error_code['1000_7301'])
#     return success_response()
