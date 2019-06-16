# coding: utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import database_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from app.admin import admin as admin_blueprint
from app.back import back as back_blueprint

app.register_blueprint(admin_blueprint)
app.register_blueprint(back_blueprint)

# ------------------------------------------------
# 初始化内存数据
from .common.memory.stationlist import initialize_station_list
from .common.memory.facnum import initialize_facnum
from .common.memory.piglist import initialize_piglist
from .common.memory.daily_intake_start_time import initialize_intake_start_time
from .common.memory.daily_first_intake_record import initialize_daily_first_intake_record
from .common.memory.pig_daily_assess_record import initialize_pig_daily_assess_record
from app.CAN.Raspi_CAN import CANCommunication

# 从数据库初始化信息到内存中，方便直接进行比对
# 初始化内存中的测定站号列表
initialize_station_list()
# 初始化内存中的猪场代码
initialize_facnum()
# 初始化种猪列表信息
initialize_piglist()
# 种猪日采食开始允许的时间，用来做测定站停止之后的第二日首次采食数据统计
initialize_intake_start_time()
# 种猪每日在指定时间之后首次采食数据，内存数据
initialize_daily_first_intake_record()
# 种猪最近两日采食、体重数据
initialize_pig_daily_assess_record()

# 进行 CAN 连接
CANCommunication()

# ------------------------------------------------
