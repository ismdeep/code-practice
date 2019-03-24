# coding: utf-8
# author: ismdeep
# datetime: 2019-03-15 10:11:04

import requests
import json
import re


def http_proxy_test(_ip_, _port_):
    try:
        proxies = {
            'http': '%s:%d' % (_ip_, _port_)
        }
        req = requests.get(
            url='http://ip.sb',
            headers={
                'User-Agent': 'curl'
            },
            proxies=proxies
        )
        print(req.text.strip())
        return True
    except:
        return False


def https_proxy_test(_ip_, _port_):
    try:
        proxies = {
            'https': '%s:%d' % (_ip_, _port_)
        }
        req = requests.get(
            url='https://ipv4.ip.sb/addrinfo.php',
            proxies=proxies
        )
        j = json.loads(req.text)
        print(j['address'])
        return True
    except:
        return False


def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


def fetch_proxy_list(_pageid_=1):
    url = 'https://www.xicidaili.com/nn/%d' % _pageid_
    req = requests.get(
        url=url,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
    )
    print(req.text)
    proxy_list = findall(req.text, open('re.txt', 'r').read())
    print(proxy_list)
    proxies = []
    for item in proxy_list:
        # print(item)
        try:
            proxies.append((item[3], int(item[4]), item[8].lower()))
        except:
            pass
    # print(url)
    return proxies


def main():
    proxy_list = fetch_proxy_list(1)
    print(len(proxy_list))
    print(proxy_list)
    for ip, port, proxy_type in proxy_list:
        print(ip)
    exit(0)
    if http_proxy_test('127.0.0.1', 1080):
        print('http://127.0.0.1:1080')
    if https_proxy_test('127.0.0.1', 1080):
        print('https://127.0.0.1:1080')


if __name__ == '__main__':
    main()
