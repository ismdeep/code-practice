# coding: utf-8
# author: ismdeep
# dateime: 2019-02-16 13:20:00
# filename: 1935.py
# blog: https://ismdeep.com


def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
            if m[i + 1][j + 1] > mmax:
                mmax = m[i + 1][j + 1]
                p = i + 1
    return s1[p - mmax:p], mmax  # 返回最长子串及其长度

while True:
    try:
        s = input()
        lcs, length = find_lcsubstr(s, s[::-1])
        print(length)
    except:
        break
