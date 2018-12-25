# coding: utf8
'测定站的运行状况'

from flask import request, json
from app.back import back
from app.common.auth import admin_login_req
from app.back.logic.stationinfo import stationinfo_action
from app.models import StationInfo, NotificationContact, NotificationRecord
from app.common.util import error_response, success_response, error_logger
from app.config import station_errorcode_on_normal_code
from app.common.errorcode import error_code
from app.common.util.send_email import send_mail_async
from app.common.util import asyncFunc
from app.common.util.time import get_now_timestamp


@back.route('/back/piginfo/stationinfo/', methods=['POST'])
@admin_login_req
def stationinfo():
    '''
    以模板的形式渲染页面
    '''
    request_data = request.json
    param_checker = stationinfo_action(request_data)
    if not param_checker['type']: return json.jsonify({'success': False, 'err_msg': param_checker['err_msg']})

    station_info_record = StationInfo(dict(
        stationid=request_data.get('stationid').zfill(12),
        status=request_data.get('status'),
        changetime=get_now_timestamp(),
        errorcode=request_data.get('errorcode'),
    ))

    try:
        # 插入传入的数据和数据模型不一致的时候，或者由于其他原因插入失败的时候，或报异常
        # StationInfo.check_stationid(request_data.get('stationid'))
        station_info_record.exist_update_or_add(
            stationid=request_data.get('stationid').zfill(12),
            status=request_data.get('status'),
            changetime=get_now_timestamp(),
            errorcode=request_data.get('errorcode'),
        )

        @asyncFunc
        def notification():
            contacts_from_db = NotificationContact.get_prev(50)
            contacts = []
            for c in contacts_from_db:
                contacts.append(c[0])
            # 当错误码不是完全正常的时候，需要发送短信
            # 发送来机器运行故障的时候，发送故障通知
            if request_data.get('status') == 'on' and str(
                request_data.get('errorcode')) != station_errorcode_on_normal_code:
                mail_message = '测定站出现<b><font color=red>故障</font></b><br>' \
                               ' 测定站id：<font color=red>' + request_data.get('stationid') + '</font><br>' \
                                                                                           '错误码：<font color=red>' + request_data.get(
                    'errorcode') + '</font><br>' \
                                   '<b>请尽快检查并排除故障</b>'
                send_mail_async(
                    '测定站运行故障',
                    mail_message,
                    contacts
                )
                # 添加一条记录到通知记录表里面
                add_record = NotificationRecord(dict(
                    email='all',
                    message=mail_message,
                    created_time=get_now_timestamp()
                ))
                add_record.add_one()

            # 发送来关机指令的时候，发送测定站关机通知
            if request_data.get('status') == 'off':
                mail_message = '测定站<b><font color=red>停机</font></b><br>' \
                               '测定站id：<font color=red>' + request_data.get('stationid') + '</font><br>' \
                                                                                          '错误码：<font color=red>' + request_data.get(
                    'errorcode') + '</font><br>' \
                                   '<b>请尽快检查并排除故障</b>'
                send_mail_async(
                    '测定站已停机',
                    mail_message,
                    contacts
                )
                # 添加一条记录到通知记录表里面
                add_record = NotificationRecord(dict(
                    email='all',
                    message=mail_message,
                    created_time=get_now_timestamp()
                ))
                add_record.add_one()

        notification()

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_1001'])
        return error_response(error_code['1000_1001'])
    return success_response()
