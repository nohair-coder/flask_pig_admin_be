# coding: utf8
'权限校验的拦截器'
from functools import wraps

def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function
