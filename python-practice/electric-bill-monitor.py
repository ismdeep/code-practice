# coding:utf-8

'''
POST /epay/electric/queryelectricbill HTTP/1.1
Host: ecard.jxust.edu.cn
Connection: keep-alive
Content-Length: 41
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://ecard.jxust.edu.cn
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
DNT: 1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://ecard.jxust.edu.cn/epay/electric/load4electricbill?elcsysid=2
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6,zh-TW;q=0.5,de;q=0.4,ja;q=0.3,fr;q=0.2,id;q=0.1,ru;q=0.1,es;q=0.1,am;q=0.1,pt;q=0.1,pl;q=0.1,ca;q=0.1,hu;q=0.1,lt;q=0.1,sq;q=0.1,nb;q=0.1,mt;q=0.1,cy;q=0.1,it;q=0.1,da;q=0.1,so;q=0.1,tr;q=0.1,la;q=0.1,nl;q=0.1,su;q=0.1,ro;q=0.1,vi;q=0.1,lb;q=0.1,ko;q=0.1,et;q=0.1
Cookie: JSESSIONID=A89F2BD81602867376FFB3A9890731C9
'''

import requests


def fetch_electric_bill():
    req = requests.post(
        url='http://ecard.jxust.edu.cn/epay/electric/queryelectricbill'
        , data={'sysid': 2, 'roomNo': 18606, 'elcarea': 1, 'elcbuis': 53}
        , headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            , 'Cookie': 'JSESSIONID=A89F2BD81602867376FFB3A9890731C9'
        }
    )
    content = req.text
    print(content)


if __name__ == '__main__':
    fetch_electric_bill()
