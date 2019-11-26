# coding:utf-8
"""
基于模版方法模式允许用户自定义排序规则
"""
import math


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Sorter(object):
    @staticmethod
    def select_sort(data, cmp_func):
        for left in range(len(data) - 1):
            m = left
            for i in range(left + 1, len(data)):
                if cmp_func(data[i], data[m]):
                    m = i
            data[m], data[left] = data[left], data[m]


def cmp_point(a: Point, b: Point):
    da = math.sqrt(a.x * a.x + a.y * a.y)
    db = math.sqrt(b.x * b.x + b.y + b.y)
    return da <= db


def main():
    a = [8, 3, 7, -9, -6, 5, -1, 2]
    b = [1, 3, 4, 5, 6, 7, 2, 1]
    l = []
    for i in range(len(a)):
        l.append(Point(a[i], b[i]))
    Sorter.select_sort(l, cmp_point)
    for item in l:
        print("(%2d,%2d)" % (item.x, item.y))


main()
