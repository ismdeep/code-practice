# coding:utf-8
import os
import socket
import uuid
import requests
from ismdeep_utils import ArgvUtil
from ismdeep_utils import DateTimeUtil
import logging

logging.basicConfig(
    filename='run.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_ip_info():
    info = {
        'hostname': socket.gethostname(),
        'create_datetime': DateTimeUtil.simple_date_time_string(),
        'content': os.popen('LANGUAGE=UTF-8.en_US ifconfig').read()
    }
    return info


def push_data(_key_id_, _data_):
    data = {
        'keyid': _key_id_,
        'data': _data_,
        'token': ArgvUtil.get_sys_argv('-token')
    }
    req = requests.post(
        url='https://info.ismdeep.com/api/info/push_data',
        data=data
    )
    return req.text


res_content = push_data('ip_info_%s' % (get_mac_address()), str(get_ip_info()))
logging.info(res_content)