# coding: utf8
'邮件找回密码表'

from app import db

class UserFindPass(db.Model):
    '''
    邮件找回密码表
    '''
    __tablename__ = 'user_find_pass'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    verifycode = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(64))
    created_time = db.Column(db.Integer)

    def __init__(self, params):
        self.email = params.get('email')
        self.verifycode = params.get('verifycode')
        self.password = params.get('password')
        self.created_time = params.get('created_time')

    def add(self):
        '''
        新增一条记录
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    def find(self):
        '''
        找到指定记录
        :return:
        '''
        return UserFindPass.query.filter_by(verifycode=self.verifycode).first()

    def delete(self):
        '''
        删除指定记录
        :return:
        '''
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<UserFindPass %r>' % self.email
