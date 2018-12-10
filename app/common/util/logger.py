# coding: utf8
'日志'

from app import app

error_logger = app.logger.error
warning_logger = app.logger.warning
info_logger = app.logger.info
