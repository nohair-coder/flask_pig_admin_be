# coding: utf8
'模拟服务端：C端'
from socket import *
from threading import Thread
import functools
from datamodel import piginfo, stationinfo, station_connection
import json
import time

server = socket(AF_INET, SOCK_STREAM)

BUFSIZE = 4096
host = 'localhost'
port = 10000
address = (host, port)
server.bind(address)
server.listen(1)


def asyncFunc(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


while True:
    print('waiting for connection: ')
    new_socket, clent_address = server.accept()


    @asyncFunc
    def receive_data():
        while True:
            # 在另一个线程中接收数据，打印到控制台
            try:
                receive_data = new_socket.recv(BUFSIZE)
                if len(receive_data) > 0:
                    print('receive: {}'.format(receive_data.decode('utf8')))
            except Exception as e:
                new_socket.close()
                print('---- receive data closed ---')
                print(e)
                break


    def send_piginfo():
        time.sleep(5)
        new_socket.send(json.dumps(piginfo()).encode('utf8'))


    def send_stationinfo():
        time.sleep(5)
        new_socket.send(json.dumps(stationinfo()).encode('utf8'))


    def send_station_connectioninfo():
        time.sleep(5)
        new_socket.send(json.dumps(station_connection()).encode('utf8'))


    # 开启在另一个线程接收数据
    receive_data()
    while True:
        try:
            # 在当前线程发送数据
            # 种猪信息
            send_piginfo()
            # 测定站运行状态
            send_stationinfo()
            # 测定站 USBCAN 的连接状态信息
            send_station_connectioninfo()
        except Exception as e:
            print('-----  connection closed  ----')
            print(e)
            new_socket.close()
            break
