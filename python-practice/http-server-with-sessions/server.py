import json
import os
import platform
from socket import *
import threading
from urllib.parse import unquote
from ismdeep_utils import ArgvUtil
import random


HOST = '0.0.0.0'
PORT = 80
BUFSIZE = 4096
ADDR = (HOST, PORT)

PT_PATH = 1
PT_FILE = 2
PT_EMPT = 0

server_configs = None

directory_separator: str = '/'


def generate_session_id():
    items = list('0123456789abcdef')
    ans = ''
    for i in range(32):
        ans += items[random.randint(0, len(items) - 1)]
    return ans


def load_config_list(_config_list_path_):
    configs = {}
    for root, dirs, files in os.walk(_config_list_path_):
        for file in files:
            with open('%s/%s' % (_config_list_path_, file), 'r') as f:
                obj = json.loads(f.read())
                configs[obj['server_name']] = obj
    return configs


def fetch_path_type(_path_):
    if os.path.isdir(_path_):
        return PT_PATH
    if os.path.isfile(_path_):
        return PT_FILE
    return PT_EMPT


def is_file(_path_):
    return True if fetch_path_type(_path_) == PT_FILE else False


def is_dir(_path_):
    return True if fetch_path_type(_path_) == PT_PATH else False


def parse_header_http_2_url(_str_):
    try:
        ans = _str_.split(' ')[1]
        return ans.strip() if ans.find('?') < 0 else ans.split('?')[0].strip()
    except:
        return '/'


def parse_request_header(_data_):
    request_header = {}
    _data_ = _data_.split('\r\n')
    for item in _data_:
        _index_ = item.find(':')
        if _index_ >= 0:
            request_header[item[:_index_].lower().strip()] = item[_index_ + 1:].strip()
        else:
            request_header['http'] = item
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


def dump_response_header(_response_header_):
    print('---- Response Header ----')
    print(_response_header_)
    return ''


def send_file_data_handle(_config_, _response_header_, _tcpclient_, _file_path_):
    file_size = os.path.getsize(_file_path_)
    range_to = file_size - 1
    range_from = 0
    file = open(_file_path_, 'rb')
    headers = dump_response_header(_response_header_) + '\r\n'
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


def send_file_list_handle(_config_, _response_header_, _tcp_client_, _file_path_):
    dirs, files = get_files(_file_path_)
    headers = dump_response_header(_response_header_) + '\r\n'
    content = open(_config_['tpl'] + directory_separator + 'file-list.html', 'r').read()
    content_file = open(_config_['tpl'] + directory_separator + 'file-list-file.html', 'r').read()
    content_dir = open(_config_['tpl'] + directory_separator + 'file-list-dir.html', 'r').read()
    content_files = ''
    content_dirs = ''
    for file in files:
        tmp = content_file
        tmp = tmp.replace('{$file_name}', file)
        content_files += tmp
    for _dir_ in dirs:
        tmp = content_dir
        tmp = tmp.replace('{$dir_name}', _dir_)
        content_dirs += tmp
    content = content.replace('{$files}', content_files)
    content = content.replace('{$dirs}', content_dirs)
    _tcp_client_.send(headers.encode())
    _tcp_client_.send(content.encode())
    _tcp_client_.close()


def send_404_handle(_config_, _response_header_, _tcp_client_):
    file_path = _config_['tpl'] + directory_separator + '404.html'
    file_size = os.path.getsize(file_path)
    f = open(file_path, 'rb')
    headers = dump_response_header(_response_header_)
    _tcp_client_.send(headers.encode())
    _tcp_client_.send(f.read())
    _tcp_client_.close()


def send_502_handle(_config_, _response_header_, _tcp_client_):
    file_path = _config_['tpl'] + directory_separator + '404.html'
    file_size = os.path.getsize(file_path)
    f = open(file_path, 'rb')
    headers = dump_response_header(_response_header_) + '\r\n'
    _tcp_client_.send(headers.encode())
    _tcp_client_.send(f.read())
    _tcp_client_.close()


def send_redirect_data_handle(_config_, _response_header_, _tcp_client_, _redirect_url_):
    headers = dump_response_header(_response_header_) + '\r\n'
    _tcp_client_.send(headers.encode())
    _tcp_client_.close()


def tcp_handle(_tcp_client_):
    _data_ = _tcp_client_.recv(BUFSIZE)
    request_header = parse_request_header(_data_.decode().split('\r\n\r\n')[0])
    print(request_header)
    response_header = {}
    if 'cookie' in request_header:
        response_header['Cookie'] = request_header['cookie']
    else:
        response_header['Set-Cookie'] = generate_session_id()
    print(response_header)
    '''parse response header'''
    print(request_header)
    host_name = request_header['host']
    config = server_configs[host_name] if host_name in server_configs else server_configs['default']
    response_header['Server'] = config['server']

    file_path = parse_file_path(config, parse_header_http_2_url( request_header['http']))
    if os.path.isfile(file_path):
        send_file_data_handle(config, response_header, _tcp_client_, file_path)
        return
    if os.path.isdir(file_path) and os.path.isfile(file_path + directory_separator + config['default_file']):
        send_file_data_handle(config, response_header, _tcp_client_, file_path + directory_separator + config['default_file'])
        return
    _url_ =  parse_header_http_2_url(request_header['http'])
    if os.path.isdir(file_path) and _url_[len(_url_)-1:] != '/':
        send_redirect_data_handle(config, response_header, _tcp_client_, 'http://' + request_header['host'] + request_header['url'] + '/')
        return
    if os.path.isdir(file_path):
        '''send back file list'''
        send_file_list_handle(config, response_header, _tcp_client_, file_path)
        return
    send_404_handle(config, response_header, _tcp_client_)


def main():
    global server_configs
    global directory_separator
    if 'Windows' == platform.system():
        directory_separator = '\\'
    server_configs = load_config_list(ArgvUtil.get_sys_argv('-config'))
    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_server.bind(ADDR)
    tcp_server.listen(10)
    print('waiting for connection...')
    while True:
        tcp_client, addr = tcp_server.accept()
        threading.Thread(target=tcp_handle, args=(tcp_client,)).start()


if __name__ == '__main__':
    main()
