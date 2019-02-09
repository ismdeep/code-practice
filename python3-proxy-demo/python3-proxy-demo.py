# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 19:08:00
# filename: python3-proxy-demo.py
# blog: https://ismdeep.com

import requests


def main():
    req = requests.get(
        url='http://mirrors.163.com/freebsd/releases/amd64/11.2-RELEASE/doc.txz',
        headers={
            'User-Agent': 'curl'
        },
        stream=False
    )
    print(req.headers)


if __name__ == '__main__':
    main()

