# coding: utf8
from app import app
import logging

if __name__ == '__main__':
    app.debug = True
    # 放置日志文件
    # https://www.cnblogs.com/itxb/p/8635056.html
    # debug 状态，则输出到命令行
    # producton 状态，则输出到日志文件
    if (app.debug):
        logging.basicConfig(format='%(asctime)s - %(funcName)s - line: %(lineno)d - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(filename='./log.txt',
                            format='%(asctime)s - %(funcName)s - line: %(lineno)d - %(levelname)s - %(message)s')

    app.run() # 这让你的操作系统监听所有公开的 IP
