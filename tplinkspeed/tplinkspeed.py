# coding: utf-8
# author: Del Cooper
# dateime: 2018-02-17 18:18:09
# filename: main.py
# blog: https://ismdeep.com

import os
import sys
import codecs
import time
import base64

ip = sys.argv[1]
basic_auth = str(base64.b64encode(sys.argv[2].encode('utf-8')), 'utf-8')

html_path = '/Users/ismdeep/tmp/tplink_statusrpm.htm'
shell_code = '''curl -s 'http://%(ip)s/userRpm/StatusRpm.htm' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6,zh-TW;q=0.5,de;q=0.4,ja;q=0.3,fr;q=0.2,id;q=0.1,ru;q=0.1,es;q=0.1,am;q=0.1,pt;q=0.1,pl;q=0.1,ca;q=0.1,hu;q=0.1,lt;q=0.1,sq;q=0.1,nb;q=0.1,mt;q=0.1,cy;q=0.1,it;q=0.1,da;q=0.1,so;q=0.1,tr;q=0.1,la;q=0.1,nl;q=0.1,su;q=0.1,ro;q=0.1,vi;q=0.1,lb;q=0.1,ko;q=0.1' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Authorization: Basic %(basic_auth)s' -H 'Connection: keep-alive' -H 'Referer: http://%(ip)s/userRpm/StatusRpm.htm' --compressed -o /Users/ismdeep/tmp/tplink_statusrpm.htm'''%({
    'ip': ip,
    'basic_auth': basic_auth
})


def between(_content_, _start_, _end_):
    _content_ = _content_[_content_.find(_start_) + len(_start_):]
    _content_ = _content_[:_content_.find(_end_)]
    return _content_


if __name__ == '__main__':
    first_receive_byte = 0
    first_send_byte = 0
    last_receive_byte = 0
    last_send_byte = 0
    last_time = time.time()
    while True:
        os.system(shell_code)
        content = codecs.open(html_path, 'r', 'gb2312').read()
        l = between(content, '''var statistList=new Array(''', ''');''').strip().split('\n')
        receive_byte = int(l[0].replace(',', '').strip())
        send_byte = int(l[1].replace(',', '').strip())
        if 0 == first_receive_byte:
            first_receive_byte = receive_byte
            first_send_byte = send_byte
        cur_time = time.time()
        receive_speed = (receive_byte - last_receive_byte) / (cur_time - last_time)
        send_speed = (send_byte - last_send_byte) / (cur_time - last_time)
        print(
            'receive speed : %10.2fkB/s          send speed : %10.2fkB/s          receive byte: %10.2fMB          send byte: %10.2fMB' % (
                receive_speed / 1000,
                send_speed / 1000,
                (receive_byte - first_receive_byte) / 1000000.0,
                (send_byte - first_send_byte) / 1000000.0)
        )
        last_receive_byte = receive_byte
        last_send_byte = send_byte
        last_time = cur_time
        time.sleep(1)
