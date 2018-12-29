# coding: utf8
from flask import Blueprint

admin = Blueprint('admin', __name__)

import app.admin.controller.notificationcontact
import app.admin.controller.dashboard
import app.admin.controller.piginfo
import app.admin.controller.errorcode
