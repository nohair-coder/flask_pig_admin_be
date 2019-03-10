# coding: utf8
'种猪日采食开始允许的时间，用来做测定站停止之后的第二日首次采食数据统计'

from app.common.errorcode import error_code
from app.common.util import asyncFunc
from app.common.util import error_logger
from app.common.util import get_now_time, transform_time
from app.models import SysCfg

daily_intake_start_time = []


def initialize_intake_start_time():
    '''
    从数据库中获取数据到内存
    :return:
    '''
    # 清理数据
    daily_intake_start_time.clear()
    try:
        res = SysCfg({
            'name': 'PIG_DAILY_INTAKE_START_TIME',
        }).get_one()

        daily_intake_start_time.append(res.value)

        print('initialize_intake_start_time 每日首次采食时间载入内存成功')
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_3001'])


@asyncFunc
def initialize_intake_start_time_async():
    '''
    分配子线程处理
    :return:
    '''
    initialize_intake_start_time()


def is_after_intake_start_time(ts):
    '''
    检查输入的时间是否是在这个开始时间之后
    :param t: 给定一个10位时间戳
    :return:
    '''
    try:
        # 201903082112 > 201903080800 True
        return transform_time(ts, '%Y%m%d%H%M') > get_now_time('%Y%m%d') + daily_intake_start_time[0]
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_3002'])
