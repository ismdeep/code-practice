# coding: utf-8
# author: ismdeep
# dateime: 2019-06-11 21:21:31
# filename: csdn-dump.py
# blog: https://ismdeep.com


## /Volumes/ismdeep/Data/hacker-data/fr_prpr_io/data

import codecs
import time
from ismdeep_utils import DateTimeUtil
from pymongo import MongoClient


def push_mongo_data(data):
    conn = MongoClient('localhost', 27017)
    db = conn['soziale']
    collection = db['csdn']
    collection.insert_many(data)



def main():
    file_path = '/Volumes/ismdeep/Data/hacker-data/fr_prpr_io/data/csdn_600w.txt'
    csdns = []
    threshold = 10000
    with codecs.open(file_path, 'r', 'utf-8', 'ignore') as f:
        for line in f:
            try:
                tmp = line.strip()
                username = tmp[:tmp.find(' # ')].strip()
                tmp = tmp[tmp.find(' # ') + 3:]
                password = tmp[:tmp.find(' # ')].strip()
                tmp = tmp[tmp.find(' # ') + 3:]
                email = tmp.strip()
                csdns.append({
                    'username': username,
                    'password': password,
                    'email': email
                })
            except:
                print('>>>>>>>>', line)
            if len(csdns) >= threshold:
                print('%s => %d' % (DateTimeUtil.simple_date_time_string(), len(csdns)))
                push_mongo_data(csdns)
                csdns = []
        if len(csdns) > 0:
            push_mongo_data(csdns)


if __name__ == '__main__':
    main()
