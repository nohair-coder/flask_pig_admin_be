# coding: utf8
import socket, time, threading, struct
from app.CAN import UsrCAN, CAN_Analysis

exit_flag = False
socket_conn=0
def CANSocket() :
	global socket_conn
	socket_server = socket.socket()
	host = socket.gethostname()
	port = 22222
	socket_server.bind((host,port))
	socket_server.listen(1)
	socket_conn,addr = socket_server.accept()
	print('CAN connected',addr)
	CANRecvThread=threading.Thread(target=CANRecv)
	CANSendThread=threading.Thread(target=CANSend)
	CANRecvThread.start()
	CANSendThread.start()
	CANRecvThread.join()
	CANSendThread.join()
def CANSend () :
	'CAN发送'
	print(threading.current_thread().name,'CANSend is running...')
	databyte=bytearray()
	while exit_flag != True :
		msg=CAN_Analysis.CANSendQueue.get(block=True) 
		databyte=bytearray(13)
		databyte[0]=msg.is_extended_id<<7|msg.is_remote_frame<<6|msg.dlc
		databyte[4:0:-1]=struct.pack('<i', msg.arbitration_id)
		databyte[5:13]=msg.data
		socket_conn.send(databyte)
		time.sleep(0.001)
def CANRecv () :
	'CAN接收'
	print(threading.current_thread().name,'CANRecv is running...')
	while exit_flag != True :
		try :
			databyte = socket_conn.recv(16)
			if databyte != None : 
				msg=UsrCAN.Message(arbitration_id=struct.unpack('i',databyte[4:0:-1]),is_remote_frame=databyte[0]&0x40,extended_id=databyte[0]&0x80,dlc=databyte[0]&0x0f,data=databyte[5:13])
				CAN_Analysis.CANRecvQueue.put(msg)
		except  TimeoutError :
			print('disconnect')
CANSocketThread=threading.Thread(target=CANSocket)
CANSocketThread.start()
input('press enter to exit...')
