# coding: utf8
'种猪信息表'

from app import db
from app.config import length_per_page
from sqlalchemy import desc, and_


class PigInfo(db.Model):
    '''
    种猪信息表
    '''
    __tablename__ = 'pig_info'  # 表名

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    earid = db.Column(db.String(12))  # 12 位字符串
    stationid = db.Column(db.String(12))  # 12 位字符串
    foodintake = db.Column(db.Float())  # 小数
    weight = db.Column(db.Float())  # 小数
    bodylong = db.Column(db.Float())  # 小数
    bodywidth = db.Column(db.Float())  # 小数
    bodyheight = db.Column(db.Float())  # 小数
    bodytemperature = db.Column(db.Float())  # 小数
    systime = db.Column(db.Integer)  # 10 位整数的时间戳，秒
    stationtime = db.Column(db.Integer)  # 10 位时间戳，秒

    def __init__(self, params):
        self.earid = params.get('earid')
        self.stationid = params.get('stationid')
        self.foodintake = params.get('foodintake')
        self.weight = params.get('weight')
        self.bodylong = params.get('bodylong')
        self.bodywidth = params.get('bodywidth')
        self.bodyheight = params.get('bodyheight')
        self.bodytemperature = params.get('bodytemperature')
        self.stationtime = params.get('stationtime')
        self.systime = params.get('systime')

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all(from_id, from_time, end_time):
        '''
        获取列表中的所有的种猪信息
        :param from_time:
        :param end_time:
        :return:
        '''
        if from_id != None:
            return PigInfo\
                .query\
                .filter(and_(PigInfo.id.__lt__(from_id), PigInfo.systime.__ge__(from_time), PigInfo.systime.__le__(end_time)))\
                .order_by(desc(PigInfo.systime), desc(PigInfo.id))\
                .limit(length_per_page + 1)
        else:
            return PigInfo \
                .query \
                .filter(and_(PigInfo.systime.__ge__(from_time),
                             PigInfo.systime.__le__(end_time))) \
                .order_by(desc(PigInfo.systime), desc(PigInfo.id)) \
                .limit(length_per_page + 1)

    @staticmethod
    def get_one(earid, from_id, from_time, end_time):
        '''
        获取某头种猪的历史信息
        :return:
        '''
        if from_id != None:
            return PigInfo\
                .query\
                .filter(and_(PigInfo.id.__lt__(from_id), PigInfo.earid.__eq__(earid), PigInfo.systime.__ge__(from_time), PigInfo.systime.__le__(end_time)))\
                .order_by(desc(PigInfo.systime))\
                .limit(length_per_page + 1)
        else:
            return PigInfo \
                .query \
                .filter(and_(PigInfo.earid.__eq__(earid), PigInfo.systime.__ge__(from_time),
                             PigInfo.systime.__le__(end_time))) \
                .order_by(desc(PigInfo.systime)) \
                .limit(length_per_page + 1)

    @staticmethod
    def get_station(stationid, from_id, from_time, end_time):
        '''
        获取某个测定站的种猪信息
        :param offset:
        :return:
        '''
        if from_id != None:
            return PigInfo\
                .query\
                .filter(and_(PigInfo.id.__lt__(from_id), PigInfo.stationid.__eq__(stationid), PigInfo.systime.__ge__(from_time), PigInfo.systime.__le__(end_time)))\
                .order_by(desc(PigInfo.systime))\
                .limit(length_per_page + 1)
        else:
            return PigInfo \
                .query \
                .filter(
                and_(PigInfo.stationid.__eq__(stationid), PigInfo.systime.__ge__(from_time),
                     PigInfo.systime.__le__(end_time))) \
                .order_by(desc(PigInfo.systime)) \
                .limit(length_per_page + 1)

    def __repr__(self):
        return '<PigInfo %r>' % self.earid
