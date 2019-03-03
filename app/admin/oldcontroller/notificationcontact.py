# coding: utf8
'系统信息通知'

from flask import request, json
from app.admin import admin
from app.common.auth import admin_login_req
from app.admin.oldlogic.notificationcontact import add_contact_action
from app.models import NotificationContact
from app.common.util import error_response, success_response, error_logger
from app.common.errorcode import error_code


@admin.route('/admin/contact/add/', methods=['POST'])
@admin_login_req
def add_contact():
    '''
    添加消息联系方式（邮件）
    :return:
    '''
    request_data = request.json
    param_checker = add_contact_action(request_data)
    if not param_checker['type']: return json.jsonify({'success': False, 'err_msg': param_checker['err_msg']})

    new_item = NotificationContact(dict(
        email=request_data.get('email'),
        # 自动截取前250个字符存储到数据库
        comment=request_data.get('comment'),
    ))

    try:
        new_item.add_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_4001'])
        return error_response(error_code['1000_4001'])
    return success_response()
