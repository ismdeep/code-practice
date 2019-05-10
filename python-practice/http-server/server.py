import json
import os
import platform
from socket import *
import threading
from time import gmtime, strftime
from urllib.parse import unquote

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
            _path_ += directory_separator + unquote(section)
    return _path_


def parse_file_type(_file_path_):
    file_type_map = {
        'ico': 'image/x-icon',
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'html': 'text/html;charset=utf-8'
    }
    ext_name = _file_path_[_file_path_.rfind('.')+1:].lower()
    return file_type_map[ext_name] if ext_name in file_type_map else 'ostream'


def send_file_data_handle(_config_, _tcpclient_, _file_path_):
    file_size = os.path.getsize(_file_path_)
    range_to = file_size - 1
    range_from = 0
    file = open(_file_path_, 'rb')
    headers = ''
    headers += 'HTTP/1.1 200 OK\r\n'
    headers += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    headers += 'Server: %s\r\n' % _config_['server']
    headers += 'Content-Length: %d\r\n' % file_size
    headers += 'Connection: close\r\n'
    headers += 'Content-Type: %s\r\n\r\n' % parse_file_type(_file_path_)
    _tcpclient_.send(headers.encode())
    while range_from <= range_to:
        length = min(range_to - range_from + 1, 1024 * 1024 * 4)
        data = file.read(length)
        range_from += length
        _tcpclient_.send(data)
    _tcpclient_.close()


def get_files(_file_path_):
    for root, dirs, files in os.walk(_file_path_):
        if _file_path_ == root:
            return dirs, files
    return [], []


def send_file_list_handle(_config_, _tcpclient_, _file_path_):
    dirs, files = get_files(_file_path_)
    headers = ''
    headers += 'HTTP/1.1 200 OK\r\n'
    headers += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    headers += 'Server: %s\r\n' % _config_['server']
    headers += 'Connection: close\r\n'
    headers += 'Content-Type: text/html;charset=utf-8\r\n\r\n'
    content = open(_config_['tpl'] + directory_separator + 'file-list.html', 'r').read()
    content_file = open(_config_['tpl'] + directory_separator + 'file-list-file.html', 'r').read()
    content_dir = open(_config_['tpl'] + directory_separator + 'file-list-dir.html', 'r').read()
    content_files = ''
    content_dirs = ''
    for file in files:
        tmp = content_file
        tmp = tmp.replace('{$file_name}', file)
        content_files += tmp
    for dir in dirs:
        tmp = content_dir
        tmp = tmp.replace('{$dir_name}', dir)
        content_dirs += tmp
    content = content.replace('{$files}', content_files)
    content = content.replace('{$dirs}', content_dirs)
    _tcpclient_.send(headers.encode())
    _tcpclient_.send(content.encode())
    _tcpclient_.close()


def send_404_handle(_config_, _tcp_client_):
    file_path = _config_['tpl'] + directory_separator + '404.html'
    file_size = os.path.getsize(file_path)
    f = open(file_path, 'rb')
    headers = ''
    headers += 'HTTP/1.1 404 Not Found\r\n'
    headers += 'Server: %s\r\n' % _config_['server']
    headers += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    headers += 'Content-Length: %d\r\n' % file_size
    headers += 'Connection: close\r\n'
    headers += 'Status: 404\r\n'
    headers += 'Content-Type: text/html;charset=utf-8\r\n\r\n'
    _tcp_client_.send(headers.encode())
    _tcp_client_.send(f.read())
    _tcp_client_.close()


def send_502_handle(_config_, _tcp_client_):
    file_path = _config_['tpl'] + directory_separator + '404.html'
    file_size = os.path.getsize(file_path)
    f = open(file_path, 'rb')
    headers = ''
    headers += 'HTTP/1.1 502\r\n'
    headers += 'Server: Honix\r\n'
    headers += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    headers += 'Content-Length: %d\r\n' % file_size
    headers += 'Connection: close\r\n'
    headers += 'Status: 502\r\n'
    headers += 'Content-Type: text/html;charset=utf-8\r\n\r\n'
    _tcp_client_.send(headers.encode())
    _tcp_client_.send(f.read())
    _tcp_client_.close()


def send_redirect_data_handle(_config_, _tcp_client_, _redirect_url_):
    headers = ''
    headers += 'HTTP/1.1 301 Moved Permanently\r\n'
    headers += 'Server: Honix\r\n'
    headers += 'Date: %s\r\n' % strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
    headers += 'Connection: close\r\n'
    headers += 'Location: %s\r\n' % _redirect_url_
    headers += 'Content-Type: text/html;charset=utf-8\r\n\r\n'
    _tcp_client_.send(headers.encode())
    _tcp_client_.close()


def tcp_handle(_tcpclient_):
    _data_ = _tcpclient_.recv(BUFSIZE)
    request_header = parse_request_header(_data_.decode().split('\r\n\r\n')[0])
    print(request_header)
    host_name = request_header['host']
    config = server_configs[host_name] if host_name in server_configs else server_configs['default']
    file_path = parse_file_path(config, request_header['url'])
    print(file_path)
    if os.path.isfile(file_path):
        send_file_data_handle(config, _tcpclient_, file_path)
        return
    if os.path.isdir(file_path) and os.path.isfile(file_path + directory_separator + config['default_file']):
        send_file_data_handle(config, _tcpclient_, file_path + directory_separator + config['default_file'])
        return
    if os.path.isdir(file_path) and request_header['url'][len(request_header['url'])-1:] != '/':
        send_redirect_data_handle(config, _tcpclient_, 'http://' + request_header['host'] + request_header['url'] + '/')
        return
    if os.path.isdir(file_path):
        '''send back file list'''
        send_file_list_handle(config, _tcpclient_, file_path)
        return
    send_404_handle(config, _tcpclient_)


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
