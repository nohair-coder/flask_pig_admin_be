# coding: utf8
'通知记录表，系统发送邮件通知之后，在该表形成一条记录'

from app import db


class NotificationRecord(db.Model):
    '''
    通知记录表
    '''
    __tablename__ = 'notification_record'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), )  # 100 位字符串
    message = db.Column(db.String(255))  # 255 位字符串
    created_time = db.Column(db.Integer)  # 10 位数字

    def __init__(self, params):
        self.email = params.get('email')
        self.message = params.get('message')
        self.created_time = params.get('created_time')

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
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<NotificationRecord %r>' % self.email
