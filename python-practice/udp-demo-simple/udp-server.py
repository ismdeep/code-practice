# coding: utf-8
from socket import socket, AF_INET, SOCK_DGRAM

# create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

# bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)

# recvfrom
data, address = sock.recvfrom(4096)
print('received {} bytes from {}'.format(len(data), address))

# sendto
sent = sock.sendto(data, address)
print('sent {} bytes back to {}'.format(sent, address))
