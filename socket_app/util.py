# coding: utf8
'工具'

from threading import Thread
import functools, json, requests, time


def get_now_timestamp():
    '''
    获取当前时间对应的10位时间戳
    :return:
    '''
    return int(time.time())


def get_timestamp_from_raw_timenumber(timenumber):
    '''
    从时间数字解析得到时间戳表示的10位整数
    201812181233 => 1545111180
    :param timenumber:
    :return:
    '''
    timestr = str(timenumber)
    t = time.strptime(timestr, '%Y%m%d%H%M')
    return int(time.mktime(t))  # 返回十位的时间戳


def asyncFunc(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def write_piginfo(piginfo_from_c):
    '''
    将种猪数据写入数据库
    :param piginfo:
    :return:
    '''
    piginfo = {
        "stationid": str(piginfo_from_c.get('id')).zfill(12),
        "earid": str(piginfo_from_c.get('label')).zfill(12),  # 左边填充前导0，填充导12位
        "weight": piginfo_from_c.get('weight'),
        "bodytemperature": piginfo_from_c.get('temperature'),
        "foodintake": piginfo_from_c.get('feed'),
        "bodylong": piginfo_from_c.get('length'),
        "bodywidth": piginfo_from_c.get('wide'),
        "bodyheight": piginfo_from_c.get('high'),
        "stationtime": get_timestamp_from_raw_timenumber(piginfo_from_c.get('time')),
        "systime": get_now_timestamp(),
    }

    print('----  piginfo  ----')
    print(piginfo)

    r = requests.post(
        'http://localhost:5000/back/piginfo/insert_piginfo/',
        json=piginfo
    )
    return json.loads(r.content, encoding='utf8')  # dict


def write_stationinfo(stationinfo_from_c):
    '''
    将测定站数据写入数据库
    :param piginfo:
    :return:
    '''
    stationinfo = {
        "stationid": str(stationinfo_from_c.get('id')).zfill(12),
        "status": 'off' if stationinfo_from_c.get('status') == 0 else 'on',
        "changetime": get_now_timestamp(),
        "errorcode": stationinfo_from_c.get('errorcode'),
    }

    print('----  stationinfo  ----')
    print(stationinfo)

    r = requests.post(
        'http://127.0.0.1:5000/back/piginfo/stationinfo/',
        json=stationinfo
    )
    return json.loads(r.content, encoding='utf8') # dict
