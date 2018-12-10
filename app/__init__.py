# coding: utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import databaseURI
import pymysql # mysql 连接驱动

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from app.admin import admin as admin_blueprint
from app.back import back as back_blueprint

app.register_blueprint(admin_blueprint)
app.register_blueprint(back_blueprint)
