# coding:utf-8

import requests


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


def test_is_apache_directory(url):
    req = requests.get(
        url=url
    )
    content = req.text
    if is_apache_directory(content):
        print(url, 'is apache directory')
    else:
        print(url, 'is not apache directory')


def main():
    test_is_apache_directory('https://ismdeep.com')
    test_is_apache_directory('https://merges.ubuntu.com')
    test_is_apache_directory('http://ftp.ebi.ac.uk')
    test_is_apache_directory('http://ftp.ebi.ac.uk/pub')
    test_is_apache_directory('http://ftp.ebi.ac.uk/pub/databases')
    test_is_apache_directory('http://kairoswatches.com')
    test_is_apache_directory('http://ubuntu-cd.mirror.iweb.ca')
    test_is_apache_directory('http://mirror.ip-projects.de')
    test_is_apache_directory('http://old-releases.ubuntu.com/releases/ubuntustudio/9.04/release')
    test_is_apache_directory('http://cdimage.kali.org')
    exit(0)
    url = 'http://download.ismdeep.com'
    req = requests.get(
        url=url
    )
    content = req.text
    if is_nginx_directory(content):
        print(url, 'is nginx directory')

    if is_apache_directory(content):
        print(url, 'is apache directory')

'''
https://merges.ubuntu.com
http://ftp.ebi.ac.uk
http://ftp.ebi.ac.uk/pub
http://ftp.ebi.ac.uk/pub/databases
http://kairoswatches.com
http://ubuntu-cd.mirror.iweb.ca
http://mirror.ip-projects.de
http://old-releases.ubuntu.com/releases/ubuntustudio/9.04/release
http://cdimage.kali.org
'''

if __name__ == '__main__':
    main()
