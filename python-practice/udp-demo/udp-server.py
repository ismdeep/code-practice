# coding: utf-8
# author: ismdeep
# dateime: 2019-05-12 12:29:19
# filename: udp-server.py
# blog: https://ismdeep.com

import socket
from ismdeep_utils import ArgvUtil
import os

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the port
server_address = (ArgvUtil.get_sys_argv('-h'), int(ArgvUtil.get_sys_argv('-p')))
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)
    if data:
        print('==>', data.decode())
        f = os.popen(data.decode(), 'r', 1)
        ans = f.read()
        f.close()
        sent = sock.sendto(ans.encode(), address)
