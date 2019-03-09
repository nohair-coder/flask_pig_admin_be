# coding: utf8
'种猪每日在指定时间之后首次采食数据，内存数据'

from app.common.errorcode import error_code
from app.common.util import asyncFunc
from app.common.util import error_logger
from app.common.util import get_now_time, transform_time
from app.models import PigDailyFirstIntake

daily_first_intake_record = dict(
    time=get_now_time('%Y%m%d'),  # YYYYmmdd 表示当前数据是某天的
    pids=set([]) # 当天已经进行了首次采食的种猪的id
)


def reset_record(r_time = get_now_time('%Y%m%d')):
    '''
    重置 daily_first_intake_record
    :return:
    '''
    daily_first_intake_record['time'] = r_time  # YYYYmmdd
    daily_first_intake_record['pids'] = set([])


def initialize_daily_first_intake_record():
    '''
    从数据库中获取数据到内存
    :return:
    '''
    # 清理数据
    try:
        reset_record()
        res = PigDailyFirstIntake({
            'record_date': get_now_time('%Y%m%d'),
        }).get_all_from_record_date()

        for r in res:
            daily_first_intake_record['pids'].add(r.pid)

        print(daily_first_intake_record)

        print('initialize_daily_first_intake_record 日首次采食数据载入内存成功')
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_4001'])


@asyncFunc
def initialize_daily_first_intake_record_async():
    '''
    分配子线程处理
    :return:
    '''
    initialize_daily_first_intake_record()

def has_pig_today_intook(pid):
    '''
    判断种猪今天是否进行了采食
    :param pid:
    :return:
    '''
    try:
        return pid in daily_first_intake_record['pids']
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_4002'])
