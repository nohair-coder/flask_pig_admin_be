# coding: utf8
'种猪基础信息表'

from sqlalchemy import and_, desc

from app import db
from app.config import length_per_page


class PigBase(db.Model):
    '''
    种猪信息表
    '''
    __tablename__ = 'pig_base'  # 表名

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    pid = db.Column(db.Integer)  # 种猪id, 对应到 pig_list 的id
    food_intake = db.Column(db.Float())  # 进食量（料重）
    weight = db.Column(db.Float())  # 猪体重
    body_long = db.Column(db.Float())  # 体长
    body_width = db.Column(db.Float())  # 体宽
    body_height = db.Column(db.Float())  # 体高
    body_temp = db.Column(db.Float())  # 温度(度)
    env_temp = db.Column(db.Float())  # 环境温度
    env_humi = db.Column(db.Float())  # 环境湿度百分数

    start_time = db.Column(db.Integer)  # 开始进食时间
    end_time = db.Column(db.Integer)  # 结束进食时间
    sys_time = db.Column(db.Integer)  # 服务器本地时间

    def __init__(self, params=None):
        if params:
            self.pid = params.get('pid')
            self.food_intake = params.get('food_intake')
            self.weight = params.get('weight')
            self.body_long = params.get('body_long')
            self.body_width = params.get('body_width')
            self.body_height = params.get('body_height')
            self.body_temp = params.get('body_temp')
            self.env_temp = params.get('env_temp')
            self.env_humi = params.get('env_humi')
            self.start_time = params.get('start_time')
            self.end_time = params.get('end_time')
            self.sys_time = params.get('sys_time')

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()
        return self

    def delete_one(self):
        '''
        删除一条记录
        :return:
        '''
        db.session.delete(self)
        db.session.commit()

    def get_from_all_stations(self, *, from_id, from_time, end_time):
        '''
        获取全部种猪信息的基础数据
        :param from_time:
        :param end_time:
        :return:
        '''
        if from_id != None:
            return PigBase \
                .query \
                .filter(
                and_(PigBase.id.__lt__(from_id), PigBase.sys_time.__ge__(from_time), PigBase.sys_time.__le__(end_time))) \
                .order_by(desc(PigBase.sys_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)
        else:
            return PigBase \
                .query \
                .filter(and_(PigBase.sys_time.__ge__(from_time),
                             PigBase.sys_time.__le__(end_time))) \
                .order_by(desc(PigBase.sys_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)

    def get_from_one_pig(self, *, pid, from_id, from_time, end_time):
        '''
        获取某头种猪的历史信息
        :return:
        '''
        if from_id != None:
            return PigBase \
                .query \
                .filter(and_(PigBase.id.__lt__(from_id), PigBase.pid.__eq__(pid), PigBase.sys_time.__ge__(from_time),
                             PigBase.sys_time.__le__(end_time))) \
                .order_by(desc(PigBase.sys_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)
        else:
            return PigBase \
                .query \
                .filter(and_(PigBase.pid.__eq__(pid), PigBase.sys_time.__ge__(from_time),
                             PigBase.sys_time.__le__(end_time))) \
                .order_by(desc(PigBase.sys_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)

    def get_from_one_stations(self, *, stationid, from_id, from_time, end_time):
        '''
        获取某个测定站的种猪信息
        :param offset:
        :return:
        '''
        # if from_id != None:
        #     return PigBase \
        #         .query \
        #         .filter(
        #         and_(PigBase.id.__lt__(from_id), PigBase.stationid.__eq__(stationid), PigBase.systime.__ge__(from_time),
        #              PigBase.systime.__le__(end_time))) \
        #         .order_by(desc(PigBase.systime)) \
        #         .limit(length_per_page + 1)
        # else:
        #     return PigBase \
        #         .query \
        #         .filter(
        #         and_(PigBase.stationid.__eq__(stationid), PigBase.systime.__ge__(from_time),
        #              PigBase.systime.__le__(end_time))) \
        #         .order_by(desc(PigBase.systime)) \
        #         .limit(length_per_page + 1)

    def __repr__(self):
        return '<PigBase %r>' % self.pid
