# coding:utf-8
"""
这里写的代码是最简单的一个Python排序的程序

@TODO 后面需要实现的是：
    1. 基于模版方法模式允许用户自定义排序规则
    2. 基于策略模式允许用户自行选择排序算法
"""
import math

class Sorter(object):
    @staticmethod
    def select_sort(data):
        for left in range(len(data) - 1):
            m = left
            for i in range(left + 1, len(data)):
                if data[i] <= data[m]:
                    m = i
            data[m], data[left] = data[left], data[m]


def main():
    a = [8, 3, 7, -9, -6, 5, -1, 2]
    Sorter.select_sort(a)
    print(a)


main()
