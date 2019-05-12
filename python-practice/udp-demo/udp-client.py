# coding: utf-8
# author: ismdeep
# dateime: 2019-05-12 12:29:39
# filename: udp-client.py
# blog: https://ismdeep.com

import socket
from ismdeep_utils import ArgvUtil

while True:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ArgvUtil.get_sys_argv('-h'), int(ArgvUtil.get_sys_argv('-p')))
    message = input(':> ').encode()
    if message.decode() == 'exit':
        exit(0)
    try:
        # Send data
        sent = sock.sendto(message, server_address)
        # Receive response
        data, server = sock.recvfrom(4096)
        print(data.decode())
    finally:
        sock.close()
