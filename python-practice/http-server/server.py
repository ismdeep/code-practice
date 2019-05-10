import json
import os
import platform
from socket import *
import threading
from time import gmtime, strftime

HOST = '0.0.0.0'
PORT = 80
BUFSIZE = 4096
ADDR = (HOST, PORT)

server_configs = None

directory_separator: str = '/'


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


def parse_file_path(_config_, _url_):
    _path_ = _config_['root']
    sections = _url_.split('/')
    for section in sections:
        if len(section) > 0:
            _path_ += directory_separator + section
    return _path_


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
    ans += 'Content-Length: %d\r\n' % file_size
    ans += 'Connection: close\r\n'
    ans += 'Content-Type: text/html;charset=utf-8\r\n\r\n'
    return ans.encode(), _range_from_, _range_to_, f


def generate_404(_config_):
    file_path = _config_['root'] + directory_separator + _config_['error_page_404']
    file_size = os.path.getsize(file_path)
    f = open(file_path, 'rb')
    ans = ''
    ans += 'HTTP/1.1 404 Not Found\r\n'
    ans += 'Server: Honix\r\n'
    ans += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    # ans += 'Accept-Ranges: bytes\r\n'
    ans += 'Content-Length: %d\r\n' % file_size
    # ans += 'Cache-Control: max-age=600\r\n'
    ans += 'Connection: close\r\n'
    ans += 'Status: 404\r\n'
    ans += 'Content-Type: text/html;charset=utf-8\r\n\r\n'
    return ans.encode(), f


def tcp_handle(_tcpclient_):
    _data_ = _tcpclient_.recv(BUFSIZE)
    request_header = parse_request_header(_data_.decode().split('\r\n\r\n')[0])
    print(request_header)
    host_name = request_header['host']
    config = server_configs[host_name] if host_name in server_configs else server_configs['default']
    file_path = parse_file_path(config, request_header['url'])
    if os.path.isdir(file_path):
        if os.path.isfile(file_path + directory_separator + config['default_file']):
            file_path = file_path + directory_separator + config['default_file']
            header, range_from, range_to, file = generate_file_data_package(file_path, 0, 239847289374927)
            _tcpclient_.send(header)
            while range_from <= range_to:
                length = min(range_to - range_from + 1, 1024 * 1024 * 4)
                data = file.read(length)
                range_from += length
                _tcpclient_.send(data)
            _tcpclient_.close()
        else:
            '''send back file list'''
            _tcpclient_.send('test'.encode())
            _tcpclient_.close()
    elif os.path.isfile(file_path):
        header, range_from, range_to, file = generate_file_data_package(file_path, 0, 239847289374927)
        _tcpclient_.send(header)
        while range_from <= range_to:
            length = min(range_to - range_from + 1, 1024 * 1024 * 4)
            data = file.read(length)
            range_from += length
            _tcpclient_.send(data)
        _tcpclient_.close()
    else:
        header, file = generate_404(config)
        _tcpclient_.send(header)
        _tcpclient_.send(file.read())
        _tcpclient_.close()


def main():
    global server_configs
    global directory_separator
    if 'Windows' == platform.system():
        directory_separator = '\\'
    server_configs = load_config_list()
    tcpserver = socket(AF_INET, SOCK_STREAM)
    tcpserver.bind(ADDR)
    tcpserver.listen(10)
    print('waiting for connection...')
    while True:
        tcpclient, addr = tcpserver.accept()
        threading.Thread(target=tcp_handle, args=(tcpclient,)).start()


if __name__ == '__main__':
    main()
