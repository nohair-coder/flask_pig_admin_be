# coding: utf8
'用户信息表'

from app import db

class User(db.Model):
    '''
    用户表
    '''
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(64))
    token = db.Column(db.String(64))

    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(100), unique=True)  # 100 位字符串
    rank = db.Column(db.String(50))

    created_time = db.Column(db.Integer)
    last_login_time = db.Column(db.Integer)

    def __init__(self, params):
        self.username = params.get('username')
        self.password = params.get('password')
        self.token = params.get('token')
        self.phone = params.get('phone')
        self.email = params.get('email')
        self.rank = params.get('rank')
        self.created_time = params.get('created_time')
        self.last_login_time = params.get('last_login_time')


    def signup(self):
        '''
        新增一个用户
        :return:
        '''
        db.session.add(self)
        db.session.commit()

    def signin(self, *, token, last_login_time):
        '''
        用户登录
        :return:
        '''
        self.token=token
        self.last_login_time=last_login_time
        db.session.commit()

    def update(self):
        '''
        更新
        :return:
        '''
        db.session.commit()


    def get_from_username(self):
        '''
        检查用户名是否已经存在
        :return:
        '''
        return User.query.filter_by(username=self.username).first()

    def get_from_phone(self):
        '''
        检查手机号是否已经存在
        :return:
        '''
        return User.query.filter_by(phone=self.phone).first()

    def get_from_email(self):
        '''
        检查邮箱是否已经存在
        :return:
        '''
        return User.query.filter_by(email=self.email).first()

    def get_from_token(self):
        '''
        依据 token 寻找到对应的记录
        :return:
        '''
        return User.query.filter_by(token=self.token).first()

    def __repr__(self):
        return '<User %r>' % self.username
