# coding: utf8
'测定站状态表'

import time
from app import db


class StationInfo(db.Model):
    '''
    测定站运行状态表
    '''
    __tablename__ = 'station_info'

    id = db.Column(db.Integer, primary_key=True)
    stationid = db.Column(db.String(12))  # 12 位字符串
    status = db.Column(db.String(5))  # 字符串
    changetime = db.Column(db.Integer())  # 10位整数
    errorcode = db.Column(db.String(5))  # 字符串

    def __init__(self, params):
        self.stationid = params.get('stationid')
        self.status = params.get('status')
        self.changetime = params.get('changetime')
        self.errorcode = params.get('errorcode')

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<StationInfo %r>' % self.earid
