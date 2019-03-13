# coding: utf8
'种猪一日信息表'

from app import db
from sqlalchemy import orm, func, desc, asc, and_


class PigDailyAssess(db.Model):
    '''
    种猪一日信息表
    '''
    __tablename__ = 'pig_daily_assess'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pid = db.Column(db.Integer)
    food_intake_count = db.Column(db.SmallInteger)
    food_intake_total = db.Column(db.Float)
    weight_ave = db.Column(db.Float)
    prev_weight_compare = db.Column(db.Float)
    prev_foodintake_compare = db.Column(db.Float)
    record_date = db.Column(db.Date)

    def __init__(self, params=None):
        if params:
            self.id = params.get('id')
            self.pid = params.get('pid')
            self.food_intake_count = params.get('food_intake_count')
            self.food_intake_total = params.get('food_intake_total')
            self.weight_ave = params.get('weight_ave')
            self.prev_weight_compare = params.get('prev_weight_compare')
            self.prev_foodintake_compare = params.get('prev_foodintake_compare')
            self.record_date = params.get('record_date')

    def get_all_last_two_days_record(self):
        '''
        获取所有种猪的最近两天的日采食记录
        不同猪的最近的两个日期是不确定的
        :return:
        '''

        alias1 = orm.aliased(PigDailyAssess)
        # 原始语句
        #  SELECT a.* from pig_daily_assess a inner join pig_daily_assess b on a.pid=b.pid and a.record_date <= b.record_date GROUP BY a.pid,a.record_date HAVING COUNT(a.pid) <=2  ORDER BY a.pid,a.record_date DESC;
        count = func.count('*').label('c')
        ret = db.session.query(PigDailyAssess)\
            .filter(PigDailyAssess.pid.__eq__(alias1.pid), PigDailyAssess.record_date.__le__(alias1.record_date))\
            .group_by(PigDailyAssess.pid,PigDailyAssess.record_date)\
            .having(count <= 2)\
            .order_by(asc(PigDailyAssess.pid), desc(PigDailyAssess.record_date))\
            .all()
        return ret

    def get_all_from_record_date(self):
        '''
        依据 record_date 查询某日所有的记录数据
        :return:
        '''
        return PigDailyAssess.query.with_entities(
            PigDailyAssess.id,
            PigDailyAssess.pid,
            PigDailyAssess.food_intake_count,
            PigDailyAssess.food_intake_total,
            PigDailyAssess.weight_ave,
        ).filter_by(record_date=self.record_date).all()

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()
        return self

    def update_one(self):
        '''
        依据种猪 pid、record_date 修改对应的当天的记录
        :return:
        '''
        PigDailyAssess.query.filter(and_(PigDailyAssess.pid.__eq__(self.pid), PigDailyAssess.pid.__eq__(self.record_date))).update({
            'food_intake_count': self.food_intake_count,
            'food_intake_total': self.food_intake_total,
            'weight_ave': self.weight_ave,
            'prev_weight_compare': self.prev_weight_compare,
            'prev_foodintake_compare': self.prev_foodintake_compare,
        })
        db.session.commit()

    def get_all_from_pid(self):
        '''
        依据 pid 查询该种猪的每天的采食、体重状况
        :return:
        '''
        return PigDailyAssess.query.filter_by(pid=self.pid).all()

    def __repr__(self):
        return '<PigDailyAssess pid=%r>' % self.pid
