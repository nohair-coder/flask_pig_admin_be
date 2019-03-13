# coding: utf8
'种猪最近两日采食、体重数据'

from app.common.errorcode import error_code
from app.common.util import asyncFunc
from app.common.util import error_logger
from app.common.util import get_now_time, transform_time, get_now_timestamp
from app.models import PigDailyAssess

# 初始数据载入：查询到种猪最近两天（如果有）的日采食数据，将当前 datestring 和 最新的时间做比较，如果某头猪的最新两天采食记录时间更早，则删除最早的时间记录，保存今天和今天的前一天（有数据的前一天）的记录
# 每次采食：将当前数据提取出来，计算当天的采食次数、总采食、体重均值，采食变化、体重变化，存入数据库，存入内存


pig_daily_assess_record = {
    # 数据存储格式
    # 'pid1': {
    #     # 最近的第二天
    #     'prev': {
    #         # 'food_intake_count': '',
    #         # 'food_intake_total': '',
    #         # 'weight_ave': '',
    #         # 'prev_weight_compare': '',
    #         # 'prev_foodintake_compare': '',
    #         # 'record_date': '',
    #     },
    #     # 最近的一天
    #     'recent': {
    #         # 'food_intake_count': '',
    #         # 'food_intake_total': '',
    #         # 'weight_ave': '',
    #         # 'prev_weight_compare': '',
    #         # 'prev_foodintake_compare': '',
    #         # 'record_date': '',
    #     }
    # }, # ...
}

def initialize_pig_daily_assess_record():
    '''
    从数据库中获取数据到内存
    这个数据初始化一次开销较大，只在最初始系统启动的时候，才会初始化一次
    :return:
    '''
    try:
        res = PigDailyAssess().get_all_last_two_days_record()
        for r in res:
            pid = r.pid
            # print(r.record_date.strftime('%Y%m%d'), '20190311' == r.record_date.strftime('%Y%m%d'))
            if not pig_daily_assess_record.get(pid):
                # 这是 recent 的数据
                recent = {
                    'food_intake_count': r.food_intake_count,
                    'food_intake_total': r.food_intake_total,
                    'weight_ave': r.weight_ave,
                    'prev_weight_compare': r.prev_weight_compare,
                    'prev_foodintake_compare': r.prev_foodintake_compare,
                    'record_date': r.record_date.strftime('%Y%m%d'),
                }
                pig_daily_assess_record[pid] = {
                    'recent': recent,
                }
            else:
                # 这是 prev 的数据
                prev = {
                    'food_intake_count': r.food_intake_count,
                    'food_intake_total': r.food_intake_total,
                    'weight_ave': r.weight_ave,
                    'prev_weight_compare': r.prev_weight_compare,
                    'prev_foodintake_compare': r.prev_foodintake_compare,
                    'record_date': r.record_date.strftime('%Y%m%d'),
                }
                pig_daily_assess_record[pid]['prev'] = prev

        print(__name__, pig_daily_assess_record)
        print('initialize_pig_daily_assess_record 种猪一日信息数据载入内存成功')
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_5001'])

@asyncFunc
def initialize_pig_daily_assess_record_async():
    '''
    分配子线程处理
    :return:
    '''
    initialize_pig_daily_assess_record()

def has_today_intake(pid=0):
    '''
    该种猪今天是否已经采食
    :param pid:
    :return:
    '''
    try:
        today_date = get_now_time('%Y%m%d')
        pig_record = pig_daily_assess_record.get(pid)

        if pig_record:
            # 找不到记录说明该猪之前没有进食过
            return pig_record['recent']['record_date'] == today_date

        return False
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_5002'])

def get_pig_last_two_days_record(pid):
    '''
    获取 pid 种猪的采食数据
    :param pid:
    :return:
    '''
    record = pig_daily_assess_record.get(pid)
    if record:
        return record
    return None

def calc_today_intake(pid, *, intake, weight, intake_date):
    '''
    计算当天的采食数据
    :param pid:
    :param food_intake_count:
    :param food_intake_total:
    :param weight_ave:
    :param prev_weight_compare:
    :param prev_foodintake_compare:
    :param record_date:
    :return:
    '''
    # @Todo 计算当天的数据

    record = get_pig_last_two_days_record(pid)

    # 没有记录，则 prev_weight_compare = 0, prev_foodintake_compare = 0
    if record == None:
        print('没有记录')

        # add_today_record()

    # 下面的都是有记录的
    if has_today_intake(pid):
        # 今天采食过了，需要把今天的数据提取到，计算之后和前一天比对，再存入内存数据库
        print('今天采食过了')
        # update_today_record()
    else:
        # 今天没有采食过，和前一天比对之后，存入内存、数据库
        print('今天没有采食过')
        # add_today_record()

def add_today_record(pid, *, record_date, food_intake_count, food_intake_total, weight_ave, prev_weight_compare, prev_foodintake_compare):
    '''
    将当天计算好的数据保存到数据库，新增一条当天数据
    :param params:
    :return:
    '''
    try:
        PigDailyAssess({
            'pid': pid,
            'food_intake_count': food_intake_count,
            'food_intake_total': food_intake_total,
            'weight_ave': weight_ave,
            'prev_weight_compare': prev_weight_compare,
            'prev_foodintake_compare': prev_foodintake_compare,
            'record_date': record_date,
        }).add_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_5003'])

def update_today_record(*,pid, record_date, food_intake_count, food_intake_total, weight_ave, prev_weight_compare, prev_foodintake_compare):
    '''
    将当天计算好的数据保存到数据库，更新当天数据
    :param params:
    :return:
    '''
    try:
        PigDailyAssess({
            'pid': pid,
            'food_intake_count': food_intake_count,
            'food_intake_total': food_intake_total,
            'weight_ave': weight_ave,
            'prev_weight_compare': prev_weight_compare,
            'prev_foodintake_compare': prev_foodintake_compare,
            'record_date': record_date,
        }).update_one()
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_5004'])


