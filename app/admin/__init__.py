# coding: utf8
from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.controller.syscfg
import app.admin.controller.login
import app.admin.controller.stationinfo
import app.admin.controller.piglist
