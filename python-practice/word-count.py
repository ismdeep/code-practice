# coding: utf-8
# author: ismdeep
# dateime: 2019-05-09 23:12:09
# filename: word-count.py
# blog: https://ismdeep.com

from collections import Counter

Text = open('/Users/ismdeep/Downloads/sss.txt', 'r').read()
for char in '·~!@#$%^&*()_+=0123456789`[]{}\|:;\"\',./<>?':
    Text = Text.replace(char, ' ')
Text = Text.lower()
word_list = Text.split()
Counter(word_list).most_common()
d = {}
for word in word_list:
    d[word] = d.get(word, 0) + 1
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

word_freq.sort(reverse=True)
for cnt, word in word_freq:
    if len(word) > 2:
        print(word)