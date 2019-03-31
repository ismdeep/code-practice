# coding: utf-8
# author: ismdeep
# dateime: 2019-03-30 14:40:08
# filename: team-info.py
# blog: https://ismdeep.com
import os

import requests
import json
import time
from prettytable import PrettyTable

pre_team = [
    'jxust_team1', 'jxust_team2', 'jxust_team3', '酱菜软件A套餐', '酱菜软件B套餐', '酱菜软件C套餐', '乒乒乓乓', 'NCHU_Software1',
    'NCHU_Software2', 'NCHU_Software3', 'NCHU_Software4', '华东交大1队', '华东交大2队',
    '华东交大3队', '华东交大4队', '大菊已定', '爱，死亡和机器人', 'I&E_FIRE', '酱菜信管Go_For_Accepted!']


def main():
    timestamp = int(time.time() * 1000)
    url = 'https://gplt.patest.cn/api/cached/board/team/5c83640de130e56976836cbe?timestamp=%d' % timestamp
    req = requests.get(url=url)
    obj = json.loads(req.text)
    amt = 0
    os.system('clear')
    for item in obj['data']['data']['members']:
        print(item['v']['s'], sum(item['v']['s'][0]) + sum(item['v']['s'][1]) + sum(item['v']['s'][2]), item['name'])
        amt += sum(item['v']['s'][0]) + sum(item['v']['s'][1]) + sum(item['v']['s'][2])
    print('amount:', amt)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
