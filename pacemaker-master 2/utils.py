from PySide6.QtCore import QObject, Signal, QTime
import argparse


class NameSpace(object):
    def __repr__(self):
        return str(self.__dict__)


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


def json_object_to_object(json_object):
    if isinstance(json_object, list):
        return [json_object_to_object(item) for item in json_object]
    elif isinstance(json_object, dict):
        obj = NameSpace()
        for k, v in json_object.items():
            setattr(obj, k, json_object_to_object(v))
        return obj
    return json_object


# 串口通信模块
import serial as s

_serial = ''
msg = ''


def open_serial():
    global _serial
    global msg
    try:
        _serial = s.Serial('COM3', 9600, timeout=0.5)
        msg = lambda x: [{"code": True}, {"msg": 'open success'}] if _serial.isOpen() else [{"code": False},
                                                                                            {"msg": 'open success'}]
    except Exception as e:
        print("---异常---：", e)
    return [_serial, msg]


def send(__serial, send_data):
    __serial.write(send_data.encode('utf-8'))  # 编码


def recv(__serial, data):
    while True:
        data = __serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data
