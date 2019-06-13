# coding: utf-8
# author: ismdeep
# dateime: 2019-06-13 15:54:47
# filename: redis-client-auth-demo.py
# blog: https://ismdeep.com

from redis import Redis


client = Redis(
    host='',
    port=6379,
    password=''
)

print(client.get('email_config'))