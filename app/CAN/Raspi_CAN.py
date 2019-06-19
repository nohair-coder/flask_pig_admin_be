# coding: utf8
import queue, socket, time, threading, pickle
from app.CAN import UsrCAN, CAN_Analysis, HttpHandle
exit_flag = False
timer_cnt=0

def CANSocket() :
    'CAN Socket 初始化'
    global socket_server,CANaddr
    port = 40001
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    print('socket_server.getsockname()', socket_server.getsockname())

    # host = socket.gethostname()
    # ip = socket.gethostbyname(host)
    # print('localhost:', host, ip)

    print('sock   address      ---->', (s.getsockname()[0], port))
    socket_server.bind(('192.168.1.104', port))
    # s.close()
    data,CANaddr = socket_server.recvfrom(1024)
    print('CAN connected',CANaddr)
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
        print("Send:",msg," to ",CANaddr)
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
                        print(msg)
                        CAN_Analysis.CANRecvQueue.put(msg)
                    else :
                        print("Recvive 0 error")
            else :
                print('err Recv')
        except  TimeoutError :
            print('can disconnect')

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
                data_obj = CAN_Analysis.dataAnalyse(msg)
                if data_obj !=None and data_obj!= {}:
                    serverSendQueue.put(data_obj)
                    # print('data_obj',data_obj)
                    with open('data_object.pickle', 'wb') as f:
                        # Pickle the 'data' dictionary using the highest protocol available.
                        pickle.dump(data_obj, f, pickle.HIGHEST_PROTOCOL)
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

def timer() :
    '定时任务'
    global timer_cnt
    if exit_flag != True :
        timerThread=threading.Timer(0.01,timer)
        timerThread.start()
        timer_cnt += 1
        if timer_cnt >0xffffffff :
            timer_cnt = 0
        if(timer_cnt%1000 == 1) :
            CAN_Analysis.nodeMonitor()
        if(timer_cnt%5 == 1) :
            CAN_Analysis.timeoutHandler()

try:
    with open('data_object.pickle', 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        serverSendQueue = pickle.load(f)
except:
    serverSendQueue = queue.Queue()

# @asyncFunc
# def CANCommunication():
#     'CAN模块，阻塞型'
#     try:
#         print('before init')
#         CAN_Analysis.sysInit()
#         print("sys init")
#         CANSocketThread=threading.Thread(target=CANSocket)
#         CANSocketThread.start()
#         CANHandThread=threading.Thread(target=CANHand)
#         CANHandThread.start()
#         serverSendThread=threading.Thread(target=serverSend)
#         serverSendThread.start()

#         timer()
#         while(True) :
#             cmd=input ('Press enter to exit...\n')
#             if cmd == 'open' :
#                 CAN_Analysis.deviceStart(9,'open_device')
#             elif cmd == 'close' :
#                 CAN_Analysis.deviceStart(9,'close_device')
#             elif cmd == 'test' :
#                 CAN_Analysis.deviceStart(9,'test_device')
#             elif cmd == 'train' :
#                 CAN_Analysis.deviceStart(9,'train_device')
#             elif cmd == 'exit' :
#                 print('exit system ...')
#                 break
#         CANHandThread.join()
#         CANSocketThread.join()
#         serverSendThread.join()
#         time.sleep(3+1)
#         exit()
#     except:
#         return False

CAN_Analysis.sysInit()
print("CANsys init")
CANSocketThread = threading.Thread(target=CANSocket)
CANSocketThread.start()
CANHandThread = threading.Thread(target=CANHand)
CANHandThread.start()
serverSendThread = threading.Thread(target=serverSend)
serverSendThread.start()
timer()

def setDeviceStatus(cmd):
    '设定测定站状态，[[nodeId,"open_device"],[nodeId,"close_device"]]'
    try:
        for i in cmd:
            CAN_Analysis.deviceStart(int(i[0]),i[1])
        return True
    except Exception as e:
        print(e)
        return False

def getDeviceStatus(nodeId):
    '获得测定站状态,返回["ON","00000"]获取一个'
    try:
        status = CAN_Analysis.device_status[str(int(nodeId))]
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
