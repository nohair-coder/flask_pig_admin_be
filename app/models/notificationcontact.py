# coding: utf8
'测定站故障通知联系方式表（发送邮件的手机号记录表）'

from app import db


class NotificationContact(db.Model):
    '''
    测定站故障通知联系方式表
    '''
    __tablename__ = 'notification_contact'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)  # 100 位字符串
    comment = db.Column(db.String(255))  # 255 位字符串

    def __init__(self, params):
        self.email = params.get('email')
        self.comment = params.get('comment')

    def add_one(self):
        '''
        添加一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    def get_prev(limit=50):
        # 或者 NotificationContact.query.with_entities(NotificationContact.email).limit(50).all()
        return db.session.query(NotificationContact.email).limit(limit).all()

    def __repr__(self):
        return '<NotificationContact %r>' % self.email
