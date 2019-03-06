# coding: utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import database_URI
import pymysql  # mysql 连接驱动

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

# 从数据库初始化信息到内存中，方便直接进行比对
# 初始化内存中的测定站号列表
initialize_station_list()
# 初始化内存中的猪场代码
initialize_facnum()
# 初始化种猪列表信息
initialize_piglist()

# ------------------------------------------------
