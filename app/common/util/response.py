# coding: utf8
from flask import jsonify


def success_response(data=None):
    '''
    请求成功时的返回模板
    :param data:
    :return:
    '''
    return jsonify({
        'success': True,
        'data': data
    }) if data else jsonify({
        'success': True,
    })


def error_response(err_msg):
    '''
    请求失败时的返回模板
    :param err_msg:
    :return:
    '''
    return jsonify({
        'success': False,
        'err_msg': err_msg,
    })
