# coding: utf-8
# author: ismdeep
# dateime: 2019-05-27 09:42:03
# filename: client.py
# blog: https://ismdeep.com
# coding: utf-8
# author: ismdeep
# dateime: 2019-05-27 09:34:00
# filename: server.py
# blog: https://ismdeep.com

import threading

from ismdeep_utils import ArgvUtil
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

BUFSIZE = 4096

def generate_host_port():
    host = ArgvUtil.get_sys_argv('-host')
    port = ArgvUtil.get_sys_argv('-port')
    if '' == host:
        host = '0.0.0.0'

    if port == '':
        port = '8888'
    port = int(port)
    return host, port


def tcp_handle(_tcp_client_):
    _data_ = _tcp_client_.recv(BUFSIZE)
    _tcp_client_.send(_data_)
    _tcp_client_.close()


def main():
    tcpclient = socket(AF_INET, SOCK_STREAM)
    addr, port = generate_host_port()
    print(addr, port)
    tcpclient.connect((addr, port))
    tcpclient.send('hello'.encode())
    data = tcpclient.recv(BUFSIZE)
    print(data.decode())


if __name__ == '__main__':
    main()
