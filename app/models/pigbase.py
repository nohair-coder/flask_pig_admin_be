# coding: utf8
'种猪基础信息表'

from sqlalchemy import and_, desc

from app import db
from app.config import length_per_page
from .piglist import PigList


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
            return db.session \
                .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight, PigBase.body_long,
                       PigBase.body_width, PigBase.body_height, PigBase.body_temp, PigBase.env_temp,
                       PigBase.env_humi,
                       PigBase.start_time, PigBase.end_time, PigBase.sys_time,
                       PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid,
                       PigList.entry_time) \
                .outerjoin(PigList, PigList.id == PigBase.pid) \
                .filter(and_(PigBase.id.__lt__(from_id), PigBase.start_time.__ge__(from_time),
                             PigBase.start_time.__le__(end_time))) \
                .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)
        else:
            # stmt = db.session \
            #     .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight, PigBase.body_long,
            #            PigBase.body_width, PigBase.body_height, PigBase.body_temp, PigBase.env_temp, PigBase.env_humi,
            #            PigBase.start_time, PigBase.end_time, PigBase.sys_time,
            #            PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid, PigList.entry_time) \
            #     .outerjoin(PigList, PigList.id == PigBase.pid) \
            #     .filter(and_(PigBase.start_time.__ge__(from_time), PigBase.start_time.__le__(end_time))) \
            #     .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
            #     .limit(length_per_page + 1) \
            #     .subquery()
            #
            # print(stmt)

            # (452, 14, 7.22, 181.11, 120.33, 30.22, 50.44, 1.0, 2.0, 3.0, 1552017439, 1552017448, 1553082227, '', '', 'xxxxxxxxxcde', 'asdfghjklqwe', 1553082227)
            # 可以通过属性或者下标访问
            return db.session \
                .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight, PigBase.body_long,
                       PigBase.body_width, PigBase.body_height, PigBase.body_temp, PigBase.env_temp, PigBase.env_humi,
                       PigBase.start_time, PigBase.end_time, PigBase.sys_time,
                       PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid, PigList.entry_time) \
                .outerjoin(PigList, PigList.id == PigBase.pid) \
                .filter(and_(PigBase.start_time.__ge__(from_time), PigBase.start_time.__le__(end_time))) \
                .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)

    def get_from_one_pig(self, *, earid, from_id, from_time, end_time):
        '''
        获取某头种猪的历史信息
        :return:
        '''
        if from_id != None:
            return db.session \
                .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight,
                       PigBase.body_long,
                       PigBase.body_width, PigBase.body_height, PigBase.body_temp,
                       PigBase.env_temp, PigBase.env_humi,
                       PigBase.start_time, PigBase.end_time, PigBase.sys_time,
                       PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid, PigList.entry_time) \
                .outerjoin(PigList, PigList.id == PigBase.pid) \
                .filter(
                and_(PigList.earid.__eq__(earid), PigBase.id.__lt__(from_id), PigBase.start_time.__ge__(from_time),
                     PigBase.start_time.__le__(end_time))) \
                .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)
        else:

            # (452, 14, 7.22, 181.11, 120.33, 30.22, 50.44, 1.0, 2.0, 3.0, 1552017439, 1552017448, 1553082227, '', '', 'xxxxxxxxxcde', 'asdfghjklqwe', 1553082227)
            # 可以通过属性或者下标访问
            return db.session \
                .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight, PigBase.body_long,
                       PigBase.body_width, PigBase.body_height, PigBase.body_temp, PigBase.env_temp, PigBase.env_humi,
                       PigBase.start_time, PigBase.end_time, PigBase.sys_time,
                       PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid, PigList.entry_time) \
                .outerjoin(PigList, PigList.id == PigBase.pid) \
                .filter(and_(PigList.earid.__eq__(earid), PigBase.start_time.__ge__(from_time),
                             PigBase.start_time.__le__(end_time))) \
                .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)

    def get_from_one_station(self, *, stationid, from_id, from_time, end_time):
        '''
        获取某个测定站的种猪信息
        :return:
        '''
        if from_id != None:
            return db.session \
                .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight,
                       PigBase.body_long,
                       PigBase.body_width, PigBase.body_height, PigBase.body_temp,
                       PigBase.env_temp, PigBase.env_humi,
                       PigBase.start_time, PigBase.end_time, PigBase.sys_time,
                       PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid,
                       PigList.entry_time) \
                .outerjoin(PigList, PigList.id == PigBase.pid) \
                .filter(and_(PigList.stationid.__eq__(stationid), PigBase.id.__lt__(from_id),
                             PigBase.start_time.__ge__(from_time), PigBase.start_time.__le__(end_time))) \
                .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)
        else:

            # (452, 14, 7.22, 181.11, 120.33, 30.22, 50.44, 1.0, 2.0, 3.0, 1552017439, 1552017448, 1553082227, '', '', 'xxxxxxxxxcde', 'asdfghjklqwe', 1553082227)
            # 可以通过属性或者下标访问
            return db.session \
                .query(PigBase.id, PigBase.pid, PigBase.food_intake, PigBase.weight, PigBase.body_long,
                       PigBase.body_width, PigBase.body_height, PigBase.body_temp, PigBase.env_temp, PigBase.env_humi,
                       PigBase.start_time, PigBase.end_time, PigBase.sys_time,
                       PigList.facnum, PigList.animalnum, PigList.earid, PigList.stationid, PigList.entry_time) \
                .outerjoin(PigList, PigList.id == PigBase.pid) \
                .filter(and_(PigList.stationid.__eq__(stationid), PigBase.start_time.__ge__(from_time),
                             PigBase.start_time.__le__(end_time))) \
                .order_by(desc(PigBase.start_time), desc(PigBase.id)) \
                .limit(length_per_page + 1)

    def __repr__(self):
        return '<PigBase %r>' % self.pid
