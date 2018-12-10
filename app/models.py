# coding: utf8
import time
from app import db


class PigInfo(db.Model):
    '''
    种猪信息表
    '''
    __tablename__ = 'pig_info'  # 表名

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
        self.systime = params.get('systime') if params.get('systime') else int(time.time())

    id = db.Column(db.Integer, primary_key=True)
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

    def __repr__(self):
        return '<PigInfo %r>' % self.earid


class StationInfo(db.Model):
    '''
    测定站运行状态表
    '''
    __tablename__ = 'station_info'

    def __init__(self, params):
        self.stationid = params.get('stationid')
        self.status = params.get('status')
        self.changetime = params.get('changetime')
        self.errorcode = params.get('errorcode')

    id = db.Column(db.Integer, primary_key=True)
    stationid = db.Column(db.String(12))  # 12 位字符串
    status = db.Column(db.String(5))  # 字符串
    changetime = db.Column(db.Integer())  # 10位整数
    errorcode = db.Column(db.String(5))  # 字符串

    def __repr__(self):
        return '<StationInfo %r>' % self.earid
