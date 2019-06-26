# coding: utf-8
from socket import socket, AF_INET, SOCK_DGRAM

# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message.  It will be repeated.'

# Send data
sent = sock.sendto(message, server_address)

# Receive response
data, server = sock.recvfrom(4096)

print('received {!r}'.format(data))
