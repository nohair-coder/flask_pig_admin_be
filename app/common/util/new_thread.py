# coding: utf8
from threading import Thread
import functools

def asyncFunc(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper
