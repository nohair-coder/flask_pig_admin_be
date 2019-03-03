# coding: utf8
'系统配置表'

from app import db

# 配置对应的数据库键名
cfg_keys = {
    'FAC_NUM': 'FAC_NUM', # 系统设置-猪场代码
    'SHOW_SELECT_LANGUAGE': 'SHOW_SELECT_LANGUAGE', # 系统设置-显示选择语言
    'SHOW_TIME_SYNC': 'SHOW_TIME_SYNC', # 系统设置-显示时间同步区域
    'PIG_BASE_DATA_FIELDS': 'PIG_BASE_DATA_FIELDS', # 基础数据页面允许显示的字段
    'PIG_BASE_DATA_ALLOWED_FIELDS': 'PIG_BASE_DATA_ALLOWED_FIELDS', # 基础数据页面允许选择显示的所有字段
}

# 部分配置允许的键值
cfg_allowed_values = {
    'SHOW_SELECT_LANGUAGE': ('false', 'true'),
    'SHOW_TIME_SYNC': ('false', 'true'),
    'PIG_BASE_DATA_ALLOWED_FIELDS': ("facnum", "earid", "animalnum", "stationid", "food_intake", "weight", "body_long", "body_width", "body_height", "body_temp", "env_temp", "env_humi", "start_time", "end_time", "sys_time"),
    # 中文释义
    'PIG_BASE_DATA_ALLOWED_FIELD_COMMENTS': {
        'facnum': '猪场代码',
        'earid': '耳标号',
        'animalnum': '种猪号',
        'stationid': '测定站号',
        'food_intake': '采食量',
        'weight': '体重',
        'body_long': '体长',
        'body_width': '体宽',
        'body_height': '体高',
        'body_temp': '体温',
        'env_temp': '环境温度',
        'env_humi': '环境湿度',
        'start_time': '开始时间',
        'end_time': '结束时间',
        'duration': '持续时间'
    }
}

class SysCfg(db.Model):
    '''
    系统配置表
    '''
    __tablename__ = 'syscfg'

    name = db.Column(db.String(50), primary_key=True)
    comment = db.Column(db.String(50))
    value = db.Column(db.String(50))
    created_time = db.Column(db.Integer)

    def __init__(self, params):
        self.name = params.get('name')
        self.value = params.get('value')

    def update_kv(self):
        '''
        更新一个键
        :return:
        '''
        SysCfg.query.filter_by(name=self.name).update({
            'name': self.name,
            'value': self.value,
        })
        db.session.commit()

    @staticmethod
    def get_all_kvs():
        '''
        获取所有的键
        :return:
        '''
        return SysCfg.query.all()

    def __repr__(self):
        return '<SysCfg %r>' % self.name
