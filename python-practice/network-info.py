# coding:utf-8
import os
import socket
import uuid

# 获取主机名
hostname = socket.gethostname()
#获取IP
ip = socket.gethostbyname(hostname)
# 获取Mac地址
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

# ipList = socket.gethostbyname_ex(hostname)
# print(ipList)
info = {
    'hostname': hostname,
    'ip': ip,
    'mac': get_mac_address()
}


def get_ip_info_from_windows():
    os.system('mode con cp select=437')
    content = os.popen('ipconfig /all').read()
    print(content)


def get_ip_info_from_linux():
    content = os.popen('ifconfig').read()
    print(content)



# get_ip_info_from_windows()
get_ip_info_from_linux()
exit(0)


print(info)