# coding: utf8
# '本地端，连接 C 端'

from socket import *
from util import asyncFunc, write_piginfo, write_stationinfo

import json

socket_host = 'localhost'
socket_port = 10000
BUFSIZE = 4096


# 创建socket
client_socket = socket(AF_INET, SOCK_STREAM)

# 连接服务器
serAddr = (socket_host, socket_port)
client_socket.connect(serAddr)


@asyncFunc
def send_message(msg):
    try:
        client_socket.send(msg)
    except Exception as e:
        print('<<<----- send_message error  ----->>>')
        print(e)
        client_socket.close()


while True:
    try:
        raw_receive = client_socket.recv(BUFSIZE)
        if len(raw_receive) > 0:
            recv = json.loads(raw_receive, encoding='utf8')
            print('--------')
            print(recv)
            print('--------')
            # 接收到种猪信息
            if recv.get('_type') == 1:
                # 种猪信息
                res = write_piginfo(recv)
                res['_type']=recv.get('_type')
                print('----  res  -----')
                send_message(json.dumps(res).encode('utf8'))
            elif recv.get('_type') == 2:
                # 测定站工作状态 2
                res = write_stationinfo(recv)
                res['_type']=recv.get('_type')
                print('----  res  -----')
                send_message(json.dumps(res).encode('utf8'))
            elif recv.get('_type') == 3:
                # 测定站与 USBCAN 连接状态 3
                pass
    except Exception as e:
        print('<<<-----  err  ------>>>')
        print(e)
        client_socket.close()
        break
