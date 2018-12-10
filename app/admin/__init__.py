# coding: utf8
from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/back')

import app.admin.views
