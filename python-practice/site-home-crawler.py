# coding:utf-8

import requests


def is_nginx_directory(content):
    _index_ = content.find(
        '''<html>\r\n<head><title>Index of /</title></head>\r\n<body bgcolor="white">\r\n<h1>Index of /</h1><hr>''')
    return True if _index_ >= 0 else False


def main():
    url = 'http://download.ismdeep.com'
    req = requests.get(
        url=url
    )
    content = req.text
    if is_nginx_directory(content):
        print(url)


if __name__ == '__main__':
    main()
