# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 16:30:54
# filename: python3-pyplot-demo-3.py
# blog: https://ismdeep.com
# -*-coding:utf-8-*-

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
axes1 = fig.add_subplot(111)
line, = axes1.plot(np.random.rand(10))


# 因为update的参数是调用函数data_gen,所以第一个默认参数不能是framenum
def update(data):
    line.set_ydata(data)
    return line,


# 每次生成10个随机数据
def data_gen():
    while True:
        yield np.random.rand(10)


ani = animation.FuncAnimation(fig, update, data_gen, interval=2 * 1000)
plt.show()
