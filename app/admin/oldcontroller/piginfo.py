# coding: utf8
'种猪信息查询'

from flask import request
from app.admin import admin
from app.models import PigInfo
from app.common.util import error_response, success_response, error_logger, get_now_timestamp, get_now_time
from app.common.errorcode import error_code
from app.config import length_per_page
import sys
from app.config import mysql_config
import subprocess

@admin.route('/admin/piginfo/', methods=['POST'])
def get_piginfo():
    '''
    获取种猪信息
    :param type: all、station、one
    :param offset: 跳过的条数
    :param earid: 对应 pig
    :param stationid: 对应 station
    :return:
    '''
    request_data = request.json
    type = request_data.get('type', None)
    from_id = request_data.get('fromId', None)
    res=None
    ret = {
        'list': [],
        'lastId': None,
        'hasNextPage': False,
    }
    try:
        from_time = request_data.get('fromTime', None)  # 直接接收10位的数字时间戳
        from_time = 0 if from_time == None else from_time
        end_time = request_data.get('endTime', None)  # 直接接收10位的数字时间戳
        end_time = get_now_timestamp() if end_time == None else end_time
        if type == 'station':
            # 'station'
            stationid = request_data.get('stationid', '').zfill(12)
            if stationid != None:
                res = PigInfo.get_station(stationid, from_id, from_time, end_time)
            else:
                return error_response('缺少测定站号')

        elif type == 'one':
            # 'one'
            earid = request_data.get('earid', '').zfill(12)
            if earid != None:
                res = PigInfo.get_one(earid, from_id, from_time, end_time)
            else:
                return error_response('缺少耳标号')

        else:
            # all
            res = PigInfo.get_all(from_id, from_time, end_time)

        # k v 赋值
        for ind, item in enumerate(res):
            if ind < length_per_page:
                ret['list'].append({
                    'id': item.id,
                    'earid': item.earid.lstrip('0'),
                    'stationid': item.stationid.lstrip('0'),
                    'foodintake': item.foodintake,
                    'weight': item.weight,
                    'bodylong': item.bodylong,
                    'bodywidth': item.bodywidth,
                    'bodyheight': item.bodyheight,
                    'bodytemperature': item.bodytemperature,
                    'systime': item.systime,
                    'stationtime': item.stationtime,
                })
            if ind == length_per_page:
                ret['hasNextPage'] = True

        if ret['hasNextPage']:
            ret['lastId'] = ret['list'][-1:][0].get('id') # 获取最后一条记录的 id， 在下一次
        else:
            ret['lastId'] = 0
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_6001'])
        return error_response(error_code['1000_6001'])
    return success_response(ret)


@admin.route('/admin/piginfo/export', methods=['POST'])
def export_piginfo():
    '''
    导出种猪信息
    :return:
    '''
    try:
        request_data = request.json
        from_time = request_data.get('fromTime', None)  # 直接接收10位的数字时间戳
        from_time = 0 if from_time == None else from_time

        end_time = request_data.get('endTime', None)  # 直接接收10位的数字时间戳
        end_time = get_now_timestamp() if end_time == None else end_time

        path = request_data.get('path', '~')

        filename = request_data.get('filename', get_now_time() + '-pig.csv')

        keys = request_data.get('keys', []) # 导出的字段名

        type = request_data.get('type', None) # 导出的数据类型

        time_asc = request_data.get('timeasc', None) # 倒数的时序

        if len(keys) == 0:
            return error_response('导出字段不能为空')

        # bin 平台区分鉴别
        if sys.platform.startswith('darwin'):
            mysql_bin = '/Applications/MAMP/Library/bin/mysql'
        else:
            mysql_bin = 'mysql'

        if type == 'station':
            stationid = request_data.get('stationid', None)
            if isinstance(stationid, str):
                stationid = stationid.zfill(12)
                where_str = " WHERE `stationid`=" + '"' + stationid + '"'
            else:
                return error_response('测定站号不合法')
        elif  type == 'one':
            # 'one'
            earid = request_data.get('earid', None)
            if isinstance(earid, str):
                earid = earid.zfill(12)
                print(earid)
                where_str = " WHERE `earid`=" + '"' + earid + '"'
            else:
                return error_response('耳标号不合法')
        else:
            where_str = ' '


        if time_asc:
            # 默认是时间逆序
            orderby_str = ' ORDER BY `systime` ASC'
        else:
            orderby_str = ' ORDER BY `systime` DESC'


        auth_str = ' -u' + mysql_config['username'] + ' -p' + mysql_config['password'] + ' --database=' + mysql_config['database']
        sql_str = " --execute='SELECT " + "`" + "`,`".join(keys) + "`" + " FROM `pig_info`" + where_str + orderby_str + "'"
        sed_str = " | sed 's/\t/,/g;' "
        dest_file = path + '/' + filename

        print(sql_str)

        # 执行的命令
        # /Applications/MAMP/Library/bin/mysql -uroot -proot --database=pig --execute='SELECT `id`,`earid` FROM `pig_info`' > ~/20181228-pig.csv
        command = mysql_bin + auth_str + sql_str + sed_str + ' > ' + dest_file

        exec_res = subprocess.call(
            command,
            shell=True,
        )
        # 为 0 则正常执行，不为0则执行出现异常
        if exec_res != 0:
            error_logger(sql_str + sed_str + ' > ' + dest_file)
            error_logger(error_code['1000_6101'])
            return error_response(error_code['1000_6101'])
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1000_6102'])
        return error_response(error_code['1000_6102'])
    return success_response()


