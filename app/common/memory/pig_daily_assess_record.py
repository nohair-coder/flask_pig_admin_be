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

def has_prev_record(pid):
    '''
    种猪有 prev 对应的记录
    :param pid:
    :return:
    '''
    record = pig_daily_assess_record.get(pid)
    return record.get('prev') != None

def has_recent_record(pid):
    '''
    种猪有 recent 对应的记录
    :param pid:
    :return:
    '''
    record = pig_daily_assess_record.get(pid)
    return record.get('recent') != None


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

def update_today_record(pid, *, record_date, food_intake_count, food_intake_total, weight_ave, prev_weight_compare, prev_foodintake_compare):
    '''
    将当天计算好的数据保存到数据库，更新当天数据
    :param params:
    :return:
    '''
    try:
        return PigDailyAssess({
            'pid': pid,
            'food_intake_count': food_intake_count,
            'food_intake_total': food_intake_total,
            'weight_ave': weight_ave,
            'prev_weight_compare': prev_weight_compare,
            'prev_foodintake_compare': prev_foodintake_compare,
            'record_date': record_date,
        }).update_one() == 1
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_5004'])

@asyncFunc
def calc_today_intake(pid, *, intake, weight, intake_date):
    '''
    计算当天的采食数据
    - 可能的情形（这是一种增长性的情形，从无到有，从1条记录到2条记录）
        - 该猪没有任何采食记录，这是该猪第一次采食，进入统计
        - 该猪在内存有一次采食记录
            - 这条记录的日期是昨天的：这次数据直接和前一天进行比较，创建记录，转移 recent 和 prev
            - 这条记录的日期是今天的：直接进行今天的当日计算，不用进行比较
        - 该猪在内存有两次采食记录
            - 最新的记录日期已经过期：这次数据直接和前一天进行比较，创建记录，转移 recent 和 prev
            - 最新的记录日期是今天：提取今天的数据，和前一天进行比较，保存
    :param pid: 种猪 id
    :param intake: 采食量
    :param weight: 体重
    :param intake_date: 20190311
    :return:
    '''
    try:
        record = get_pig_last_two_days_record(pid)

        # 没有记录，则 prev_weight_compare = 0, prev_foodintake_compare = 0
        if record == None:
            # print('没有记录')

            recent = {
                'record_date': intake_date,
                'food_intake_count': 1,
                'food_intake_total': intake,
                'weight_ave': weight,
                'prev_weight_compare': 0,
                'prev_foodintake_compare': 0,
            }
            # 在数据库中添加记录
            add_today_record(pid, **recent)
            # 在内存中添加记录
            pig_daily_assess_record[pid] = {
                'recent': recent,
            }
            # print('record == None ', recent)
            # print('record == None 添加到内存中了')
        # 下面的都是有记录的
        else:
            recent = record.get('recent')
            prev = record.get('prev')
            has_prev = prev != None

            # print('prev => ', prev)

            if not has_prev:
                # - 该猪在内存有一次采食记录
                #     - 这条记录的日期是昨天的：这次数据直接和前一天进行比较，创建记录，转移 recent 和 prev
                #     - 这条记录的日期是今天的：直接进行今天的当日计算，不用进行比较
                # print('<---------------------->')
                # print('pid {pid}，没有 prev 记录'.format(pid=pid))
                # print('在计算之前')
                # print('recent ', recent)
                # print('prev ', prev)
                # print('<---------------------->')
                if recent.get('record_date') != intake_date:
                    # 日期已经过期了，需要将 recent 变更为 prev
                    new_recent = {
                        'record_date': intake_date,
                        'food_intake_count': 1,
                        'food_intake_total': intake,
                        'weight_ave': weight,
                        'prev_weight_compare': weight - recent.get('weight_ave'),
                        'prev_foodintake_compare': intake - recent.get('food_intake_total'),
                    }
                    # print('<---------------------->')
                    # print('recent 的 record_date 不等于 intake_date')
                    # print('在计算之后')
                    # print('recent ', new_recent)
                    # print('prev ', recent)
                    # print('<---------------------->')
                    # 更改数据库中数据
                    add_today_record(pid, **new_recent)
                    # 更新到内存
                    pig_daily_assess_record[pid] = {
                        'recent': new_recent,
                        'prev': recent,
                    }

                else:
                    # recent.get('record_date') == intake_date  => recent 对应的是今天的日期不用变更指向
                    new_count = recent.get('food_intake_count') + 1
                    new_intake_total = recent.get('food_intake_total') + intake
                    new_weight_ave = (recent.get('weight_ave') * recent.get('food_intake_count') + weight) / new_count

                    new_recent = {
                        'record_date': intake_date,
                        'food_intake_count': new_count,
                        'food_intake_total': new_intake_total,
                        'weight_ave': new_weight_ave,
                        'prev_weight_compare': 0,
                        'prev_foodintake_compare': 0,
                    }
                    # print('<---------------------->')
                    # print('recent 的 record_date 等于 intake_date')
                    # print('在计算之后')
                    # print('recent ', new_recent)
                    # print('prev ', recent)
                    # print('<---------------------->')
                    # 更改数据库中的数据
                    if update_today_record(pid, **new_recent):
                        # 更新到内存
                        pig_daily_assess_record[pid]['recent'] = new_recent
            else:
                # 有 prev、recent 记录
                # print('pid {pid}，有 prev、recent 记录'.format(pid=pid))
                # - 该猪在内存有两次采食记录
                #     - 最新的记录日期已经过期：这次数据直接和前一天进行比较，创建记录，转移 recent 和 prev
                #     - 最新的记录日期是今天：提取今天的数据，和前一天进行比较，保存
                if recent.get('record_date') != intake_date:
                    # recent 的 record_date 记录已经过期了
                    # add_today_record()
                    new_recent = {
                        'record_date': intake_date,
                        'food_intake_count': 1,
                        'food_intake_total': intake,
                        'weight_ave': weight,
                        'prev_weight_compare': weight - recent.get('weight_ave'),
                        'prev_foodintake_compare': intake - recent.get('food_intake_total'),
                    }
                    # 更改数据库中数据
                    add_today_record(pid, **new_recent)
                    # 更新到内存
                    pig_daily_assess_record[pid] = {
                        'recent': new_recent,
                        'prev': recent,
                    }
                else:
                    # recent 的 record_date 是当天
                    # update_today_record()
                    new_count = recent.get('food_intake_count') + 1
                    new_intake_total = recent.get('food_intake_total') + intake
                    new_weight_ave = (recent.get('weight_ave') * recent.get('food_intake_count') + weight) / new_count

                    new_recent = {
                        'record_date': intake_date,
                        'food_intake_count': new_count,
                        'food_intake_total': new_intake_total,
                        'weight_ave': new_weight_ave,
                        'prev_weight_compare': new_weight_ave - prev.get('weight_ave'),
                        'prev_foodintake_compare': new_intake_total - prev.get('food_intake_total'),
                    }

                    update_today_record(pid, **new_recent)
                    # 更新到内存
                    pig_daily_assess_record[pid]['recent'] = new_recent

        # print('pig_daily_assess_record ', pig_daily_assess_record)
    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_5005'])
