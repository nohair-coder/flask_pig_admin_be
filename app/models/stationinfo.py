# coding: utf8
'测定站状态表'

from app import db


class StationInfo(db.Model):
    '''
    测定站运行状态表
    '''
    __tablename__ = 'station_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stationid = db.Column(db.String(12), unique=True, index=True)  # 12 位字符串
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

    # def check_stationid_exist(self, id):
    #     '''
    #     检查测定站id是否在数据库中有记录了
    #     :return:
    #     '''
    #     ret = StationInfo.query.filter_by(stationid=id).first()
    #     return ret != None

    # def update(self):
    #     '''
    #     修改数据库中的数据
    #     :return:
    #     '''


    def exist_update_or_add(self, stationid, status, errorcode, changetime):
        '''
        当stationid存在的时候，则将状态更改到数据库中，否则如果不存在该stationid，即添加到数据库中
        :return:
        '''
        res = StationInfo.query.filter_by(stationid=stationid).first()
        if res == None:
            # updates
            self.add_one()
        else:
            # add
            res.status=status
            res.errorcode=errorcode
            res.changetime=changetime
            db.session.commit()

    def __repr__(self):
        return '<StationInfo %r>' % self.stationid
