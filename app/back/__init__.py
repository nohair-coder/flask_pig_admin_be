# coding: utf8
from flask import Blueprint

back = Blueprint('back', __name__, url_prefix='/back')

import app.back.controller.piginfo
import app.back.controller.stationinfo

