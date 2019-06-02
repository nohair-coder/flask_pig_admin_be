import queue, os, json, socket, time, threading, struct
from app.CAN import UsrCAN, CAN_Analysis, HttpHandle
from app.common.util import asyncFunc
exit_flag = False
dog_cnt=0

def CANSocket() :
    'CAN Socket 初始化'
    global socket_server,CANaddr
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 40001
    print('localhost:',host,ip)
    socket_server.bind(('192.168.1.104',port))
    data,CANaddr = socket_server.recvfrom(1024)
    print('CAN connected',data,CANaddr)
    CANRecvThread=threading.Thread(target=CANRecv,args=(socket_server,CANaddr))
    CANSendThread=threading.Thread(target=CANSend,args=(socket_server,CANaddr))
    CANRecvThread.start()
    CANSendThread.start()
    CANRecvThread.join()
    CANSendThread.join()
    socket_server.close()

def CANSend (socket_server,CANaddr) :
    'CAN发送'
    print(threading.current_thread().name,'CANSend is running...')
    databyte=bytearray()
    while exit_flag != True :
        msg=CAN_Analysis.CANSendQueue.get(block=True)
        # print("Send:",msg)
        databyte=msg.msg2byte()
        socket_server.sendto(databyte,CANaddr)

def CANRecv (socket_server,CANaddr) :
    'CAN接收'
    print(threading.current_thread().name,'CANRecv is running...')
    while exit_flag != True :
        try :
            databyte=socket_server.recv(13*50)
            if len(databyte)%13==0 :
                for i in range(len(databyte)//13) :
                    msg=UsrCAN.Message()
                    msg.byte2msg(databyte[i*13:i*13+13])
                    if msg.arbitration_id!=0 :
                        # print(msg)
                        CAN_Analysis.CANRecvQueue.put(msg)
                    else :
                        print("Recvive 0 error")
            else :
                print('err Recv')
        except  TimeoutError :
            print('disconnect')

def CANHand () :
    'CAN处理'
    print(threading.current_thread().name+'running...')
    while exit_flag != True :
        msg=CAN_Analysis.CANRecvQueue.get()
        if msg != None :
            if msg.is_remote_frame == True :#如果是远程帧
                func_code = CAN_Analysis.getFunctionCode(msg)#获取功能码
                if(msg.arbitration_id==0x0ff) :
                    pass
                elif func_code == CAN_Analysis.FUN_CODE_DICT['time_stamp_request'] :
                    CAN_Analysis.syncTime(msg)
                elif func_code == CAN_Analysis.FUN_CODE_DICT['heart_beat'] :
                    CAN_Analysis.network_management(msg)
                    #print('heart_beat',msg)
                elif func_code == CAN_Analysis.FUN_CODE_DICT['data_object_request'] :
                    CAN_Analysis.promiseRequest (msg)
                    #print('data_object_request',msg)
                else :
                    print('Node',CAN_Analysis.getFunctionCode(msg),' can not identify !')
            else :
                #print('data_obj',msg)
                data_obj = CAN_Analysis.dataAnalyse(msg)
                if data_obj !=None :
                    serverSendQueue.put(data_obj)

def serverSend():
    '上传数据'
    print(threading.current_thread().name,'serverSend is running...')
    while exit_flag != True :
        data_obj={}
        try :
            data_obj=serverSendQueue.get(timeout=3)
            if HttpHandle.dataPost(data_obj)!=True :
                serverSendQueue.put(data_obj)
            time.sleep(0.1)
        except :
            pass

def watchDog () :
    '定时任务'
    global dog_cnt
    if exit_flag != True :
        watchDogThread=threading.Timer(0.01,watchDog)
        watchDogThread.start()
        dog_cnt += 1
        if dog_cnt >0xffffffff :
            dog_cnt = 0
        if(dog_cnt%1000 == 1) :
            CAN_Analysis.nodeMonitor()
        if(dog_cnt%5 == 1) :
            CAN_Analysis.timeoutHandler()

serverSendQueue=queue.Queue()

@asyncFunc
def CANCommunication():
    'CAN模块，阻塞型'
    try:
        CAN_Analysis.sysInit()
        print("sys init")
        CANSocketThread=threading.Thread(target=CANSocket)
        CANSocketThread.start()
        CANHandThread=threading.Thread(target=CANHand)
        CANHandThread.start()
        serverSendThread=threading.Thread(target=serverSend)
        serverSendThread.start()
        watchDog()
        while(True) :
            cmd=input ('Press enter to exit...\n')
            if cmd == 'open' :
                CAN_Analysis.deviceStart(9,'open_device')
            elif cmd == 'close' :
                CAN_Analysis.deviceStart(9,'close_device')
            elif cmd == 'test' :
                CAN_Analysis.deviceStart(9,'test_device')
            elif cmd == 'train' :
                CAN_Analysis.deviceStart(9,'train_device')
            elif cmd == 'exit' :
                print('exit system ...')
                break
        CANHandThread.join()
        CANSocketThread.join()
        serverSendThread.join()
        time.sleep(3+1)
        exit()
    except:
        return False
def setDeviceStatus(cmd):
    '设定测定站状态，[[nodeId,"open_device"],[nodeId,"close_device"]]'
    try:
        for i in cmd:
            CAN_Analysis.deviceStart(i[0],i[1])
        return True
    except:
        return False

def getDeviceStatus(nodeId):
    '获得测定站状态,返回["ON","00000"]'
    try:
        status = CAN_Analysis.device_status[nodeId]
        res=[]
        if status['work_status'] == 'OFF':
            res[0] = 'OFF'
            res[1] = '00000'
        elif status['work_status'] == 'ON':
            res[0] = 'ON'
            res[1] = '00000'
        else:
            res[0] == 'ON'
            res[1] = status['work_status']
        return res
    except:
        return False
