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

    #
    # def get_from_station(self, noexit):
    #     '''
    #     依据测定站查询猪列表
    #     :return:
    #     '''
    #     if noexit:
    #         # exit_time is None 表示还没有出栏
    #         return PigList.query.filter(
    #             and_(PigList.stationid.__eq__(self.stationid), PigList.exit_time.is_(None))
    #         ).all()
    #     else:
    #         return PigList.query.filter_by(stationid=self.stationid).all()
    #
    # def entry_one(self):
    #     '''
    #     一个种猪入栏
    #     :return:
    #     '''
    #     db.session.add(self)
    #     db.session.commit()
    #     return self
    #
    # def exit_one(self):
    #     '''
    #     一个种猪出栏
    #     :return:
    #     '''
    #     PigList.query.filter_by(id=self.id).update({
    #         'exit_time': self.exit_time,
    #     })
    #     db.session.commit()
    #
    # def exit_one_station(self, exit_time):
    #     '''
    #     一个测定站的种猪全部出栏
    #     :return:
    #     '''
    #     PigList.query.filter(
    #         and_(PigList.stationid.__eq__(self.stationid), PigList.exit_time.is_(None))
    #     ).update({
    #         'exit_time': exit_time,
    #     })
    #     db.session.commit()
    #
    # def update_piginfo(self):
    #     '''
    #     更改一头猪的信息
    #     :return:
    #     '''
    #     PigList.query.filter_by(id=self.id).update({
    #         'facnum': self.facnum,
    #         'animalnum': self.animalnum,
    #         'earid': self.earid,
    #     })
    #     db.session.commit()
    #
    # def update_stationid(self):
    #     '''
    #     更新所属测定站
    #     :return:
    #     '''
    #     PigList.query.filter_by(id=self.id).update({
    #         'stationid': self.stationid,
    #     })
    #     db.session.commit()

    def __repr__(self):
        return '<PigDailyFirstIntake %r>' % self.pid
