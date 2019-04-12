# coding: utf8
'事件相关的功能函数'
from datetime import timedelta, date
from time import localtime, strftime, time


def get_now_timestamp():
    '''
    获取当前时间对应的10位时间戳
    :return:
    '''
    return int(time())


def get_now_time(format='%Y%m%d'):
    '''
    以一定的格式获取现在的时间
    %Y%m%d 20181228
    %Y%m%d 20181228
    %Y%m%d%H%M 201812281213
    :return:
    '''
    return strftime(format, localtime())


def transform_time(t=0, format='%Y%m%d%H%M'):
    '''
    以一定的格式转换给定的时间
    %Y%m%d 20181228
    %Y%m%d 20181228
    %Y%m%d%H%M 201812281213
    %Y/%m/%d %H:%M:%S 2018/12/28 12:13:23
    :param t: 给定的时间戳 10位
    :param format:  要转换成的格式
    :return:
    '''
    return strftime(format, localtime(t))


def get_date_intervals(param_f_ts, param_e_ts):
    '''
    获取连个给定的时间戳所在日期之间的所有日期，构成一个数组返回
    :param param_f_ts: 开始时间的时间戳 10 位
    :param param_e_ts: 结束时间的时间戳 10 位
    :return: 两个时间之间的所有日期构成的数组（包含开始和结束）
    '''
    dates = []
    f_ts = int(param_f_ts)
    e_ts = int(param_e_ts)
    if f_ts <= e_ts:
        from_date = transform_time(f_ts, '%m%d')  # 开始日期
        end_date = transform_time(e_ts, '%m%d')  # 结束的日期
        temp_date = from_date
        dates.append(temp_date)
        t = date.fromtimestamp(f_ts) + timedelta(days=1)

        while temp_date != end_date:
            temp_date = t.strftime('%m%d')
            dates.append(temp_date)
            t = t + timedelta(days=1)
    return dates
