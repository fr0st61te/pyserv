# -*- coding: utf8 -*-
import traceback
import json
import sys
from server.core.lxml import create_rsp as xml_create_rsp
from server.core.lxml import parse_rsp as xml_parse_rsp
from datetime import datetime
from datetime import timedelta


def validate_time(text, _format):
    try:
        if datetime.strptime(text, _format):
            return True
    except ValueError:
        return False


def parse_time(time):
    if (validate_time(time, '%H:%M')):
        date = datetime.strptime(time, '%H:%M')
        return date.hour, date.minute
    elif validate_time(time, '%H-%M'):
        date = datetime.strptime(time, '%H-%M')
        return date.hour, date.minute
    elif validate_time(time, '%H.%M'):
        date = datetime.strptime(time, '%H.%M')
        return date.hour, date.minute
    elif validate_time(time, '%H'):
        date = datetime.strptime(time, '%H')
        return date.hour, 0


def total_secs(time):
    hour, minute = parse_time(time)
    return timedelta(hours=hour, minutes=minute).total_seconds()


def format_exception(level=10000):
    error_type, error_value, trbk = sys.exc_info()
    tb_list = traceback.format_tb(trbk, level)
    info = "Error: %s \nDescription: %s \n" % (error_type.__name__, error_value)
    info += "Traceback:\n"
    for tb in tb_list:
        info += tb
    return info + "\n"


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Mlang(metaclass=Singleton):
    """ convert json/xml data """

    def __init__(self, mlang_type=None):
        self.mlang_type = 'xml'
        if mlang_type == 'xml':
            self.mlang_type = 'xml'
        elif mlang_type == 'json':
            self.mlang_type = 'json'

    def parse_rsp(self, data):
        if self.mlang_type == 'xml':
            return xml_parse_rsp(data)
        elif self.mlang_type == 'json':
            return data

    def create_rsp(self, data, _id=None):
        if self.mlang_type == 'xml':
            return xml_create_rsp(data, _id)
        elif self.mlang_type == 'json':
            data['id'] = _id
            return json.dumps(data)
