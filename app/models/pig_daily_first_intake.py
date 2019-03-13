# coding: utf8
'种猪每天的首次进食信息记录'

from app import db


class PigDailyFirstIntake(db.Model):
    '''
    种猪每天的首次进食信息记录
    '''
    __tablename__ = 'pig_daily_first_intake'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pid = db.Column(db.Integer)  # 种猪id, 对应到 pig_list 的id
    pigbase_id = db.Column(db.Integer)  # pig_base表中对应的记录的id
    record_date = db.Column(db.String(4))  # YYYYmmdd 这条记录对应的日期

    def __init__(self, params=None):
        if params:
            self.id = params.get('id')
            self.pid = params.get('pid')
            self.pigbase_id = params.get('pigbase_id')
            self.record_date = params.get('record_date')

    def get_all_from_record_date(self):
        '''
        依据 record_date 查询某日所有的种猪的首次采食记录
        :return:
        '''
        return PigDailyFirstIntake.query.filter_by(record_date=self.record_date).all()

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()
        return self

    def get_all_from_pid(self):
        '''
        依据 pid 查询该种猪的每天的首次采食记录
        :return:
        '''
        return PigDailyFirstIntake.query.filter_by(pid=self.pid).all()

    def __repr__(self):
        return '<PigDailyFirstIntake %r>' % self.pid
