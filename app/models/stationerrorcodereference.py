# coding: utf8
'测定站错误码增删改查'

from app import db


class StationErrorcodeReference(db.Model):
    '''
    通知记录表
    '''
    __tablename__ = 'station_errorcode_reference'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    errorcode = db.Column(db.String(5), )  # 故障码
    comment = db.Column(db.String(50))  # 错误码对应的解释

    def __init__(self, params):
        if params.get('id') is not None:
            self.id = params.get('id')
        if params.get('errorcode') is not None:
            self.errorcode = params.get('errorcode')
            self.comment = params.get('comment')

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    def delete_one(self):
        '''
        删除一条记录
        :return:
        '''
        target = StationErrorcodeReference.query.filter_by(id=self.id).first()
        db.session.delete(target)
        db.session.commit()

    @staticmethod
    def get_all():
        '''
        获取所有记录
        :return:
        '''
        return StationErrorcodeReference.query.all()

    def update_one(self):
        StationErrorcodeReference.query.filter_by(id=self.id).update({
            'errorcode': self.errorcode,
            'comment': self.comment,
        })
        db.session.commit()

    def __repr__(self):
        return '<StationErrorcodeReference %r>' % self.errorcode
