# coding:utf-8
"""
基于模版方法模式允许用户自定义排序规则
"""
import time

test_count = 100
test_size = 1000


class Sorter(object):
    @staticmethod
    def select_sort(data, cmp_func):
        """
        Select Sort Algorithm
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
        :param data:
        :param cmp_func:
        :return:
        """
        for top in range(len(data) - 2, -1, -1):
            for i in range(top + 1):
                if not cmp_func(data[i], data[i + 1]):
                    data[i], data[i + 1] = data[i + 1], data[i]

    @staticmethod
    def __merge_sort_divide(data, begin, end, cmp_func):
        """
        Merge Sort Divide
        :param data:
        :param begin:
        :param end:
        :param cmp_func:
        :return:
        """
        mid = (begin + end) // 2
        """
        Left : [begin ~ mid]
        Right: [mid + 1 ~ end]
        """
        if mid - begin + 1 >= 2:
            Sorter.__merge_sort_divide(data, begin, mid, cmp_func)
        if end - mid >= 2:
            Sorter.__merge_sort_divide(data, mid + 1, end, cmp_func)
        Sorter.__merge_sort_merge(data, begin, mid + 1, end, cmp_func)

    @staticmethod
    def __merge_sort_merge(data, begin, mid, end, cmp_func):
        """
        Merge Data: [begin ~ mid - 1] and [mid ~ end]
        :param data:
        :param begin:
        :param mid:
        :param end:
        :param cmp_func:
        :return:
        """
        index1 = begin
        index2 = mid
        while index1 < mid and index2 <= end:
            if cmp_func(data[index1], data[index2]):
                index1 += 1
            else:
                data[index1], data[index2] = data[index2], data[index1]
                index1 += 1
                i = index2
                while i < end and not cmp_func(data[i], data[i + 1]):
                    data[i], data[i + 1] = data[i + 1], data[i]
                    i += 1

    @staticmethod
    def merge_sort(data, cmp_func):
        Sorter.__merge_sort_divide(data, 0, len(data) - 1, cmp_func)


def cmp(a, b):
    return a <= b


def test_quick_sort():
    for test_id in range(test_count):
        a = []
        import random
        for i in range(test_size):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.quick_sort(a, cmp)
        assert a == sorted(b)


def test_select_sort():
    for test_id in range(test_count):
        a = []
        import random
        for i in range(test_size):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.select_sort(a, cmp)
        assert a == sorted(b)


def test_bubble_sort():
    for test_id in range(test_count):
        a = []
        import random
        for i in range(test_size):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.bubble_sort(a, cmp)
        assert a == sorted(b)


def test_merge_sort():
    for test_id in range(test_count):
        a = []
        import random
        for i in range(test_size):
            a.append(random.randint(1, 100))
        b = []
        for item in a:
            b.append(item)
        Sorter.merge_sort(a, cmp)
        assert a == sorted(b)


time_start = time.time()
# test_quick_sort()
# test_select_sort()
# test_bubble_sort()
# test_merge_sort()
time_end = time.time()
print(time_end - time_start)
