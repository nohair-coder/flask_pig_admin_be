# coding: utf8
'测定站信息表'

from app import db

class StationInfo(db.Model):
    '''
    测定站信息表
    '''
    __tablename__ = 'station_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stationid = db.Column(db.String(12), unique=True)
    comment = db.Column(db.String(50))
    status = db.Column(db.Enum('on', 'off'))
    changetime = db.Column(db.Integer())
    errorcode = db.Column(db.String(5))

    def __init__(self, params=None):
        if params:
            self.stationid = params.get('stationid')
            self.comment = params.get('comment')
            self.status = params.get('status')
            self.changetime = params.get('changetime')
            self.errorcode = params.get('errorcode')

    def get_all_station(self):
        '''
        查询所有的测定站列表
        :return:
        '''
        return StationInfo.query.all()

    def add_one(self):
        '''
        添加一个测定站记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    def delete_one(self):
        '''
        删除一个测定站记录
        :return:
        '''
        db.session.delete(self)
        db.session.commit()

    def exist_update_or_add(self, stationid, status, errorcode, changetime):
        '''
        当stationid存在的时候，则将状态更改到数据库中，否则如果不存在该stationid，即添加到数据库中
        :return:
        '''
        res = StationInfo.query.filter_by(stationid=stationid).first()
        if res == None:
            # add
            self.add_one()
        else:
            # update
            res.status = status
            res.errorcode = errorcode
            res.changetime = changetime
            db.session.commit()

    def __repr__(self):
        return '<StationInfo %r>' % self.stationid

    # def check_stationid_exist(self, id):
    #     '''
    #     检查测定站id是否在数据库中有记录了
    #     :return:
    #     '''
    #     ret = StationInfo.query.filter_by(stationid=id).first()
    #     return ret != None
