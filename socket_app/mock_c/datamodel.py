# coding: utf8
'传入的数据模型'
import random


def piginfo():
    '''
    种猪信息
    :return:
    '''
    return dict(
        _type=1,  # 传送的数据的类型：1 猪，2 机器
        id=12345,  # 测定站id
        label=1234567890,  # 猪的耳标
        weight=130.5,  # 体重
        temperature=16.55,  # 体温
        feed=0.88,  # 采食量
        length=150.66,  # 长度
        wide=30.55,  # 宽度
        high=40.55,  # 身高
        time=201812181319,  # 时间
    )


def stationinfo(status=0, machineId=12345):
    '''
    测定站信息
    :param status:
    :param machineId:
    :return:
    '''
    # 完全正常运行
    on = dict(
        _type=2,  # 2 控制机器开关
        status=1,  # 0 表示关，1 表示开
        id=machineId,  # 测定站的 id
        errorcode='00000',  # 测定站的错误码 1 / 9 => '00001'
    )
    # 运行状态，但是有部分功能故障，错误码不是 '00000'
    on_with_err = dict(
        _type=2,  # 2 控制机器开关
        status=1,  # 0 表示关，1 表示开
        id=machineId,  # 测定站的 id
        errorcode='00001',  # 测定站的错误码 1 / 9 => '00001'
    )
    # 测定站停机状态
    off = dict(
        _type=2,  # 2 控制机器开关
        status=0,  # 0 表示关，1 表示开
        id=machineId,  # 测定站的 id
        errorcode='00000',  # 测定站的错误码 1 / 9 => '00001'
    )

    ran_num = random.randrange(3)
    if ran_num == 0:
        return on
    if ran_num == 1:
        return on_with_err
    else:
        return off


def station_connection(status=1):
    '''
    测定站与 USBCAN 的连接状态
    :return:
    '''
    return dict(
        _type=3,  # 传送的数据的类型：1 猪，2 机器
        id=12345,  # 测定站id
        status=status,  # 连接状态： 0 disconnect  1 connect
    )
