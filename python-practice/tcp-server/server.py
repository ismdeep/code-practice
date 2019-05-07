import json
import os
from socket import *
import _thread
from time import gmtime, strftime

HOST = '0.0.0.0'
PORT = 80
BUFSIZE = 4096
ADDR = (HOST, PORT)

server_configs = None


def load_config_list():
    configs = {}
    for root, dirs, files in os.walk('config'):
        for file in files:
            with open('config/%s' % file, 'r') as f:
                obj = json.loads(f.read())
                configs[obj['server_name']] = obj
    return configs


def fetch_path_type(_path_):
    if os.path.isdir(_path_):
        return 1
    if os.path.isfile(_path_):
        return 2
    return 0


def is_file(_path_):
    return True if fetch_path_type(_path_) == 2 else False


def is_dir(_path_):
    return True if fetch_path_type(_path_) == 1 else False


def parse_request_header(_data_):
    request_header = {
        'http': '1.1',
        'method': '',
        'uri': '',
        'url': '',
        'args': '',
        'host': '',
        'user-agent': ''
    }
    _data_ = _data_.split('\r\n')
    for item in _data_:
        if item.lower().find('http/') >= 0:
            request_header['http'] = item[item.lower().find('http/')+5:]
            '''method'''
            request_header['method'] = item[:item.find(' ')].lower().strip()
            '''uri'''
            tmp = item[item.find(' ') + 1:]
            tmp = tmp[:tmp.find(' ')]
            request_header['uri'] = tmp
            if request_header['uri'].find('?') >= 0:
                try:
                    request_header['url'] = request_header['uri'][:request_header['uri'].find('?')]
                except:
                    request_header['url'] = '/'
                try:
                    request_header['args'] = request_header['uri'][request_header['uri'].find('?'):]
                except:
                    request_header['args'] = ''
            else:
                request_header['url'] = request_header['uri']
                request_header['args'] = ''
        if item.lower().find('user-agent') >= 0:
            request_header['user-agent'] = item[item.find(':')+1:].strip()
        if item.lower().find('host') >= 0:
            request_header['host'] = item[item.find(':')+1:].strip().lower()
    return request_header


def generate_data_package(_content_):
    ans = ('HTTP/1.1 200 OK\r\n'
           'Date: %(datetime)s\r\n'
           'Server: Honix\r\n'
           'X-Powered-By: HonixPY\r\n'
           'Content-Length: %(datalen)d\r\n\r\n%(content)s') % \
          ({
              'datetime': strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime()),
              'datalen': len(_content_),
              'content': _content_
          })
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
    request_header = parse_request_header(_data_.decode().split('\r\n\r\n')[0])
    print(json.dumps(request_header, indent=4))
    host_name = request_header['host']
    config = server_configs[host_name] if host_name in server_configs else server_configs['default']
    print(json.dumps(config, indent=4))
    # header, range_from, range_to, file = generate_file_data_package('CentOS-7-x86_64-DVD-1810.iso', range_from,range_to)
    # _tcpclient_.send(header)
    # while range_from <= range_to:
    #     length = min(range_to - range_from + 1, 1024 * 1024 * 4)
    #     data = file.read(length)
    #     range_from += length
    #     _tcpclient_.send(data)
    _tcpclient_.send('HTTP/1.1 200 OK\r\nServer: Apache\r\n\r\nhello'.encode())
    _tcpclient_.close()


def main():
    global server_configs
    server_configs = load_config_list()
    tcpserver = socket(AF_INET, SOCK_STREAM)
    tcpserver.bind(ADDR)
    tcpserver.listen(10)
    print('waiting for connection...')
    while True:
        tcpclient, addr = tcpserver.accept()
        _thread.start_new_thread(tcp_handle, (tcpclient,))


if __name__ == '__main__':
    main()
