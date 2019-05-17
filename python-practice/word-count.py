# coding: utf-8
# author: ismdeep
# dateime: 2019-05-09 23:12:09
# filename: word-count.py
# blog: https://ismdeep.com

from collections import Counter
from ismdeep_utils import ArgvUtil


def show_help():
    print('Usage: python word-count.py -exclude simple-list.txt -in article.txt')
    exit(0)


if '' == ArgvUtil.get_sys_argv('-exclude') or '' == ArgvUtil.get_sys_argv('-in'):
    show_help()
    exit(0)


simple_words = []
with open(ArgvUtil.get_sys_argv('-exclude'), 'r') as f:
    for line in f.readlines():
        simple_words.append(line.strip())


Text = open(ArgvUtil.get_sys_argv('-in'), 'r').read()
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
    if len(word) > 2 and word not in simple_words:
        print(word)
