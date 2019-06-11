# coding:utf-8
import os

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn['soinxdb']
collection = db['163']

result_files = []
for dir in os.listdir('E:\\Data\\data\\passwds\\163com'):
    result_files.append('E:\\Data\\data\\passwds\\163com\\' + dir)

for result_file_path in result_files:
    result_file = open(result_file_path, 'r')

    emails = []

    for line in result_file.readlines():
        tmp = line.strip()
        email = line[:line.find('----')]
        password = line[line.find('----') + 4:]
        emails.append({
            'email': email,
            'password': password
        })
    collection.insert_many(emails)
