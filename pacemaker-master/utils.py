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