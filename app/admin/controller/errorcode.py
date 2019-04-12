# coding: utf8
'错误码的增删改查'

from flask import request
from app.admin import admin
from app.models import StationErrorcodeReference
from app.common.util import error_response, success_response, error_logger
from app.common.errorcode import error_code


@admin.route('/admin/errorcode/', methods=['GET'])
def get_errorcode():
    '''
    查询故障码
    :return:
    '''
    try:
        res = StationErrorcodeReference.get_all()
        ret=[]
        for r in res:
            ret.append({
                'id': r.id,
                'errorcode': r.errorcode,
                'comment': r.comment,
            })
        ret = sorted(ret, key=lambda item: item['errorcode'], reverse=True)
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_7001'])
        return error_response(error_code['1000_7001'])
    return success_response(ret)

@admin.route('/admin/errorcode/', methods=['delete'])
def delete_errorcode():
    '''
    删除故障码
    :return:
    '''
    try:
        request_data = request.json
        target_id = request_data.get('id')
        if not target_id:
            return error_response('缺少id')
        StationErrorcodeReference({ 'id': target_id }).delete_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_7101'])
        return error_response(error_code['1000_7101'])
    return success_response()


@admin.route('/admin/errorcode/', methods=['post'])
def add_errorcode():
    '''
    新增故障码
    :return:
    '''
    try:
        request_data = request.json
        errorcode = request_data.get('errorcode', None)
        comment = request_data.get('comment', None)
        if not errorcode:
            return error_response('缺少故障码')
        if not comment:
            return error_response('缺少注释')

        StationErrorcodeReference({
            'errorcode': errorcode,
            'comment': comment,
        }).add_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_7201'])
        return error_response(error_code['1000_7201'])
    return success_response()


@admin.route('/admin/errorcode/', methods=['PUT'])
def update_errorcode():
    '''
    更改已有的故障码
    :return:
    '''
    try:
        request_data = request.json
        id = request_data.get('id', None)
        errorcode = request_data.get('errorcode', None)
        comment = request_data.get('comment', None)
        if not id:
            return error_response('缺少记录id')
        if not errorcode:
            return error_response('缺少故障码')
        if not comment:
            return error_response('缺少注释')

        StationErrorcodeReference({
            'id': id,
            'errorcode': errorcode,
            'comment': comment,
        }).update_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_7301'])
        return error_response(error_code['1000_7301'])
    return success_response()
