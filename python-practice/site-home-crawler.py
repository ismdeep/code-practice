# coding:utf-8

import requests
import threadpool
import time
from multiprocessing import Process, Lock

mutex = Lock()


def is_nginx_directory(content):
    _index_ = content.find(
        '''<html>\r\n<head><title>Index of /</title></head>\r\n<body bgcolor="white">\r\n<h1>Index of /</h1><hr>''')
    return True if _index_ >= 0 else False


def is_apache_directory(content):
    if content.find('''<th><a href="?C=N;O=D">Name</a></th>''') < 0:
        return False
    if content.find('''<th><a href="?C=M;O=A">Last modified</a></th>''') < 0:
        return False
    if content.find('''<th><a href="?C=S;O=A">Size</a></th>''') < 0:
        return False
    if content.find('''<th><a href="?C=D;O=A">Description</a></th>''') < 0:
        return False
    if content.find('''<title>Index of /''') < 0:
        return False
    return True


def append_url(url):
    print(url, 'is apache directory, and has been inserted into the database.')


def remove_url(url):
    print(url, 'is not apache directory, and has been removed from the database.')


def test_is_apache_directory(url='', true_func=None, false_func=None):
    req = requests.get(
        url=url
    )
    content = req.text
    if is_apache_directory(content):
        if true_func is not None:
            true_func(url)
        else:
            print(url, 'is apache directory')
    else:
        if false_func is not None:
            false_func(url)
        else:
            print(url, 'is not apache directory')


def test_is_apache_directory_thread_func(url):
    mutex.acquire()
    print('start at: {%s}    url: {%s}' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), url))
    mutex.release()
    test_is_apache_directory(url=url, true_func=append_url, false_func=remove_url)
    mutex.acquire()
    print('stop  at: {%s}    url: {%s}' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), url))
    mutex.release()


def main():
    url_list = ['https://merges.ubuntu.com', 'http://ftp.ebi.ac.uk', 'http://ftp.ebi.ac.uk/pub',
                'http://ftp.ebi.ac.uk/pub/databases', 'http://kairoswatches.com',
                'http://ubuntu-cd.mirror.iweb.ca',
                'http://mirror.ip-projects.de',
                'http://old-releases.ubuntu.com/releases/ubuntustudio/9.04/release',
                'http://cdimage.kali.org']
    pool = threadpool.ThreadPool(10)
    reqs = threadpool.makeRequests(test_is_apache_directory_thread_func, url_list)
    [pool.putRequest(req) for req in reqs]
    pool.wait()
    exit(0)
    url = 'http://download.ismdeep.com'
    req = requests.get(
        url=url
        , timeout=3000
    )
    content = req.text
    if is_nginx_directory(content):
        print(url, 'is nginx directory')

    if is_apache_directory(content):
        print(url, 'is apache directory')


if __name__ == '__main__':
    main()
