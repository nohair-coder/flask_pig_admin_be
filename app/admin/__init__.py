# coding: utf8
from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.controller.syscfg
import app.admin.controller.login
import app.admin.controller.stationinfo
import app.admin.controller.piglist
import app.admin.controller.pigbase
import app.admin.controller.station_weekly_assessment
import app.admin.controller.pig_intake
import app.admin.controller.graphanalyse
import app.admin.controller.pig_abnormal_analyse
import app.admin.controller.errorcode
