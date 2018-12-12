# coding: utf8
'测定站的运行状况'

from flask import request, json
from app.back import back
from app.common.auth import admin_login_req
from app.back.logic.stationinfo import insert_stationinfo_action
from app.models import StationInfo
from app.common.util import error_response, success_response, error_logger
from app.config import station_errorcode_on_normal_code
from app.common.errorcode import error_code
from app.common.util.send_email import send_mail_async


@back.route('/back/piginfo/insert_stationinfo/', methods=['POST'])
@admin_login_req
def insert_stationinfo():
    '''
    以模板的形式渲染页面
    '''
    request_data = request.json
    param_checker = insert_stationinfo_action(request_data)
    if not param_checker['type']: return json.jsonify({'success': False, 'err_msg': param_checker['err_msg']})


    new_station_info = StationInfo(dict(
        stationid=request_data.get('stationid'),
        status=request_data.get('status'),
        changetime=request_data.get('changetime'),
        errorcode=request_data.get('errorcode'),
    ))

    try:
        # 插入传入的数据和数据模型不一致的时候，或者由于其他原因插入失败的时候，或报异常
        new_station_info.add_one()
        # 当错误码不是完全正常的时候，需要发送短信
        # 发送来机器运行故障的时候，发送故障通知
        if request_data.get('status') == 'on' and str(request_data.get('errorcode')) != station_errorcode_on_normal_code:
            send_mail_async(
                '测定站运行故障',
                '测定站出现<b><font color=red>故障</font></b><br>'
                '测定站id：<font color=red>' + request_data.get('stationid') + '</font><br>'
                '错误码：<font color=red>' + request_data.get('errorcode') + '</font><br>'
                '<b>请尽快检查并排除故障</b>',
                'liu3248184446@outlook.com'
            )
        # 发送来关机指令的时候，发送测定站关机通知
        if request_data.get('status') == 'off':
            send_mail_async(
                '测定站已停机',
                '测定站<b><font color=red>停机</font></b><br>'
                '测定站id：<font color=red>' + request_data.get('stationid') + '</font><br>'
                '错误码：<font color=red>' + request_data.get('errorcode') + '</font><br>'
                '<b>请尽快检查并排除故障</b>',
                'liu3248184446@outlook.com'
            )


    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_1001'])
        return error_response(error_code['1000_1001'])
    return success_response()
