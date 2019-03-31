# coding: utf-8
# author: ismdeep
# dateime: 2019-03-30 13:07:27
# filename: board.py
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
    url = 'https://gplt.patest.cn/api/cached/board?timestamp=%d' % timestamp
    req = requests.get(url=url)
    obj = json.loads(req.text)
    ans = []
    for item in obj['data']['rawData']['score']['teams']:
        s = obj['data']['rawData']['score']['teams'][item]
        if s['name'] in pre_team:
            ans.append((s['schoolShortname'], s['name'], s['tScore']))
            # print(ans)
    ans = sorted(ans, key=lambda score: score[2], reverse=True)
    x = PrettyTable(["School", "Nicename", "Score"])
    for item in ans:
        x.add_row([item[0], item[1], item[2]])
    os.system('clear')
    # print(url)
    print(x)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
