import os
from socket import *
import _thread
import time
from time import gmtime, strftime

HOST = '0.0.0.0'
PORT = 11113
BUFSIZE = 4096
ADDR = (HOST, PORT)


def generate_data_package(_content_):
    ans = '''HTTP/1.1 200 OK\r\nDate: %s\r\nServer: Honix\r\nX-Powered-By: HonixPY\r\nContent-Length: %d\r\n\r\n%s''' % (
        strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime()),
        len(_content_),
        _content_
    )
    return ans


def generate_file_data_package(_file_path_, _range_from_, _range_to_):
    file_size = os.path.getsize(_file_path_)
    _range_to_ = min(_range_to_, file_size - 1)
    f = open(_file_path_, 'rb')
    f.seek(_range_from_)
    ans = ''
    ans += 'HTTP/1.1 200 OK\r\n'
    ans += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    ans += 'Server: Apache\r\n'
    ans += 'Accept-Ranges: bytes\r\n'
    ans += 'Content-Length: %d\r\n' % file_size
    ans += 'Cache-Control: max-age=600\r\n'
    ans += 'Connection: close\r\n'
    ans += 'Content-Type: application/x-msdownload\r\n\r\n'
    return ans.encode(), _range_from_, _range_to_, f


def tcp_handle(_tcpclient_):
    _data_ = _tcpclient_.recv(BUFSIZE)
    request_header = _data_.decode().split('\r\n')
    range_from = 0
    range_to = 18446744073709551615
    for item in request_header:
        item = item.lower()
        if item.find('range') >= 0:
            print(item)
            tmp = item[item.find('bytes') + 5:]
            if tmp.find('=') >= 0:
                tmp = tmp[tmp.find('=')+1:]
            if tmp.find('/'):
                tmp = tmp[:tmp.find('/')]
            v = tmp.split('-')
            try:
                range_from = int(v[0])
            except:
                range_from = 0
            try:
                range_to = int(v[1])
            except:
                range_to = 18446744073709551615
            print(range_from, range_to)
    header, range_from, range_to, file = generate_file_data_package('CentOS-7-x86_64-DVD-1810.iso', range_from, range_to)
    _tcpclient_.send(header)
    while range_from <= range_to:
        length = min(range_to - range_from + 1, 1024 * 1024 * 4)
        data = file.read(length)
        range_from += length
        _tcpclient_.send(data)
    _tcpclient_.close()


def main():
    tcpserver = socket(AF_INET, SOCK_STREAM)
    tcpserver.bind(ADDR)
    tcpserver.listen(10)
    print('waiting for connection...')
    while True:
        tcpclient, addr = tcpserver.accept()
        _thread.start_new_thread(tcp_handle, (tcpclient,))


if __name__ == '__main__':
    main()
