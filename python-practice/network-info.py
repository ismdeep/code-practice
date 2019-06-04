# coding:utf-8
import os
import socket
import uuid
import requests
from ismdeep_utils import ArgvUtil


def get_ip_info():
    info = {
        'hostname': socket.gethostname(),
        'content': os.popen('LANGUAGE=UTF-8.en_US ifconfig').read()
    }
    return info


def push_data(_data_):
    data = {
        'keyid': 'ip_info_97834',
        'data': _data_,
        'token': ArgvUtil.get_sys_argv('-token')
    }
    req = requests.post(
        url='https://info.ismdeep.com/api/info/push_data',
        data=data
    )
    print(req.text)


push_data(str(get_ip_info()))
