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
        """
        Selecte Sort Algorithm
        :param data:
        :param cmp_func:
        :return:
        """
        for left in range(len(data) - 1):
            m = left
            for i in range(left + 1, len(data)):
                if cmp_func(data[i], data[m]):
                    m = i
            data[m], data[left] = data[left], data[m]

    @staticmethod
    def quick_sort(data, cmp_func):
        """
        Quick Sort Algorithm
        :param data:
        :param cmp_func:
        :return:
        """
        import queue
        q = queue.Queue()
        q.put((0, len(data) - 1))
        while not q.empty():
            begin, end = q.get()
            left = begin
            right = end - 1
            if begin >= end:
                continue
            mid_value = data[end]
            while left < right:
                while cmp_func(data[left], mid_value) and left < right:
                    left += 1
                while cmp_func(mid_value, data[right]) and left < right:
                    right -= 1
                data[left], data[right] = data[right], data[left]
            if cmp_func(data[left], data[end]):
                left += 1
            data[left], data[end] = data[end], data[left]
            q.put((begin, left - 1))
            q.put((left + 1, end))

    @staticmethod
    def bubble_sort(data, cmp_func):
        """
        Bubble Sort Algorithm
        [0, n - 2]
        [0, n - 3]
        [0, 0]
        :param data:
        :param cmp_func:
        :return:
        """
        for top in range(len(data) - 2, -1, -1):
            for i in range(top + 1):
                if not cmp_func(data[i], data[i + 1]):
                    data[i], data[i + 1] = data[i + 1], data[i]


def cmp(a, b):
    return a <= b


def cmp_point(a: Point, b: Point):
    da = math.sqrt(a.x * a.x + a.y * a.y)
    db = math.sqrt(b.x * b.x + b.y + b.y)
    return da <= db


def test_quick_sort():
    for test_id in range(1000):
        a = []
        import random
        for i in range(100):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.quick_sort(a, cmp)
        assert a == sorted(b)


def test_select_sort():
    for test_id in range(1000):
        a = []
        import random
        for i in range(100):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.select_sort(a, cmp)
        assert a == sorted(b)


def test_bubble_sort():
    for test_id in range(1000):
        a = []
        import random
        for i in range(100):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.bubble_sort(a, cmp)
        assert a == sorted(b)


# test_quick_sort()
# test_select_sort()
# test_bubble_sort()
