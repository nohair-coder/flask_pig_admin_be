# coding: utf8
import time, queue, json, threading
from app.CAN import UsrCAN, HttpHandle

USE_EXTENDED_FRAME = False      #使用标准帧
FUN_CODE_BIT = 7                #节点所占用位数
FUN_CODE_DICT = {               # 远程帧时的功能码
    'heart_beat': 0,
    'data_object_request': 1,
    'time_stamp_request': 2,
    'open_device': 3,
    'close_device': 4,
    'recv_complete': 5,
    'train_device': 6,
    'test_device': 7
}
DEVICE_STATUS_CODE = ['00001', 'OFF', 'ON', '00002', '00003', '00004', '00005', '00006', '00007', '00008']
device_status = {}  # 设备缓存
data_Receiving = 0  # 接收状态
dog_count = 0  # 超时计数
CANSendQueue = queue.Queue(16)
CANRecvQueue = queue.Queue(64)
dataRequestQueue = queue.Queue(16)


def getFunctionCode(msg):
    '获取功能码'
    return msg.arbitration_id >> FUN_CODE_BIT

def getNodeID(msg):
    '获取节点'
    return msg.arbitration_id &((1<<FUN_CODE_BIT)-1)

def syncTime(msg):
    '同步时间'
    time_stamp_struct = list(time.localtime())  # 获取本地时间
    time_stamp_struct[0] -= 2000  # 将2019转换成19
    time_stamp_struct[6] = 0  # 星期转成0
    time_stamp_struct[7] = (time_stamp_struct[0] + time_stamp_struct[1] + time_stamp_struct[2] + time_stamp_struct[3] +
                            time_stamp_struct[4] + time_stamp_struct[5] + time_stamp_struct[6] + time_stamp_struct[
                                7]) & 0xff  # 和校验
    time_stamp_struct.pop()
    CANSendQueue.put(
        UsrCAN.Message(arbitration_id=msg.arbitration_id, extended_id=USE_EXTENDED_FRAME, data=time_stamp_struct))


def deviceStart(node_id, cmd):
    '上位机命令'
    global device_status
    print(device_status)
    if cmd == 'open_device':
        id_cmd = node_id | FUN_CODE_DICT['open_device'] << FUN_CODE_BIT
    elif cmd == 'close_device':
        id_cmd = node_id | FUN_CODE_DICT['close_device'] << FUN_CODE_BIT
    elif cmd == 'test_device':
        id_cmd = node_id | FUN_CODE_DICT['test_device'] << FUN_CODE_BIT
    elif cmd == 'train_device':
        id_cmd = node_id | FUN_CODE_DICT['train_device'] << FUN_CODE_BIT
    CANSendQueue.put(UsrCAN.Message(arbitration_id=id_cmd, extended_id=USE_EXTENDED_FRAME, is_remote_frame=True))


def dataAnalyse(msg):
    '数据包解析'
    data_object = {}
    global device_status
    global data_Receiving
    global dog_count
    node_id = getNodeID(msg)  # 获得节点ID
    if data_Receiving == node_id and data_Receiving != 0 and getFunctionCode(msg) != 3:  # 处于接收态
        if getFunctionCode(msg) != 0:  # 不是最后一帧
            device_status[str(node_id)]['frame'].append(msg.data)  # 记录数据
            device_status[str(node_id)]['frame_status'] += 1  # 帧计数
            dog_count = 2  # 超时标志清除
        elif msg.data[0] == device_status[str(node_id)]['frame_status']:  # 最后一帧并且帧数正确
            id_ack = node_id | FUN_CODE_DICT['recv_complete'] << FUN_CODE_BIT  # 生成应答ID
            jsontext = ''
            try:
                for i in device_status[str(node_id)]['frame']:
                    jsontext += i.decode(encoding='utf-8')  # 字节数组转字符串
                data_object = json.loads(jsontext)  # JSON解码
                try:
                    data_object['start_time'] = int(
                        time.mktime(time.strptime(data_object['start_time'], "%y%m%d%H%M%S")))
                except ValueError:
                    data_object['start_time'] = int(time.mktime(time.strptime(data_object['end_time'], "%y%m%d%H%M%S")))
                data_object['end_time'] = int(time.mktime(time.strptime(data_object['end_time'], "%y%m%d%H%M%S")))
                data_object['stationid'] = '{:0>12d}'.format(node_id)  # 12位
                data_object['earid'] = '{:0>12d}'.format(int(data_object['earid']))  # 12位
                CANSendQueue.put(
                    UsrCAN.Message(arbitration_id=id_ack, extended_id=USE_EXTENDED_FRAME, is_remote_frame=True))	#发送成功接收应答
            # print(data_object['stationid'],'ok')
            except UnicodeDecodeError:
                print('UnicodeDecodeError')
                data_object = {}
            except json.decoder.JSONDecodeError:
                print(node_id, 'JSONDecodeError:', jsontext)
                data_object = {}
            except ValueError:
                print('value error ', device_status[str(node_id)])
                data_object = {}
            clearTemp()  # 清除缓存
        else:
            print(node_id, msg.data[0], 'not equare', device_status[str(node_id)]['frame_status'])  # 缺帧
            clearTemp()
        return data_object
    return None


def clearTemp():
    '解除接收态'
    global data_Receiving
    device_status[str(data_Receiving)]['frame'] = []
    device_status[str(data_Receiving)]['frame_status'] = 0
    data_Receiving = 0
    if dataRequestQueue.empty() == False:
        promiseRequest(dataRequestQueue.get())


def timeoutHandler():
    '接收超时处理'
    global data_Receiving
    global dog_count
    if data_Receiving != 0:  # 正在接收中
        dog_count -= 1
        if dog_count < 0:
            # print(data_Receiving,'time_out     ---',time.asctime())
            # print(device_status[str(data_Receiving)])
            clearTemp()


def network_management(msg):
    '节点状态'
    global device_status
    node_id = getNodeID(msg)
    if str(node_id) not in device_status:  # 新建一个设备缓存
        device_status[str(node_id)] = {"frame": [], 'frame_status': 0, "can_status": 0, "work_status": 0,
                                       "put_status": 0}
        jsonobject = {
            'stationid': '{:0>12d}'.format(node_id),
            'comment': '',
            'status': 'off',
            'errorcode': '00000',
        }
        HttpHandle.devicePost(jsonobject)  # 上传新建的设备状态
    device_status[str(node_id)]['work_status'] = DEVICE_STATUS_CODE[msg.dlc]
    device_status[str(node_id)]['can_status'] = 2
    CANSendQueue.put(
        UsrCAN.Message(arbitration_id=msg.arbitration_id, extended_id=USE_EXTENDED_FRAME, is_remote_frame=True, dlc=0))
    # print("device_status",device_status)

def nodeMonitor():
    '节点监控定时函数'
    # 此函数由定时任务调用
    global device_status
    for i in device_status:
        if device_status[i]['can_status'] > 0:  # 设备在线
            device_status[i]['can_status'] -= 1
        elif i != '255':  # 设备断线
            device_status[i]['work_status'] = DEVICE_STATUS_CODE[9]

        if device_status[i]['work_status'] != device_status[i]['put_status']:  # 本地状态和服务器状态不一致
            json_object = {
                'stationid': '{:0>12d}'.format(int(i)),
                'comment': '',
                'errorcode': '00000'
            }
            if device_status[i]['work_status'] == 'OFF':
                json_object['status'] = 'off'
            elif device_status[i]['work_status'] == 'ON':
                json_object['status'] = 'on'
            else:
                json_object['status'] = 'on'
                json_object['errorcode'] = device_status[i]['work_status']
            HttpHandle.devicePut(json_object)  # 修改服务器记录
            device_status[i]['put_status'] = device_status[i]['work_status']
    with open('sys_info.txt', 'w') as fou:
        # fou.truncate()
        fou.write(json.dumps(device_status))
    print("device_status:",device_status)

def promiseRequest(msg):
    '处理数据包发送请求'
    global data_Receiving  # 如果是0表示非接收态，否则等于正在发送的节点ID
    global dog_count
    global device_status
    node_id = getNodeID(msg)
    if str(node_id) in device_status:	#设备已运行然后接收到数据
        if data_Receiving != 0:
            dataRequestQueue.put(msg)		#接收任务阻塞中，暂存队列
        # print(msg,'received but can not handle')
        elif time.time() - msg.timestamp < 2 and device_status[str(node_id)]['can_status'] > 0:  # 等待时间不超过2秒，并且CAN设备在线
            CANSendQueue.put(
                UsrCAN.Message(arbitration_id=msg.arbitration_id, extended_id=USE_EXTENDED_FRAME, is_remote_frame=True))
            data_Receiving = getNodeID(msg)	#开始接收
            dog_count = 2
        # print(msg.arbitration_id,' start handle')
        else:
            print("Can't handle it", node_id, data_Receiving)	#超时不接收

def sysInit():
    '设备状态初始化'
    global device_status
    with open('./sys_info.txt', 'r') as fin:
        try:
            text = fin.read()
            # print(text)
            device_status = json.loads(text)
        except json.decoder.JSONDecodeError:
            print('sys_info create')
    for i in device_status:
        device_status[i] = {"frame": [], 'frame_status': 0, "can_status": 0, "work_status": 0, "put_status": 0}



