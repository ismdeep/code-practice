# coding: utf-8
# author: ismdeep
# dateime: 2019-05-26 18:49:41
# filename: main.py
# blog: https://ismdeep.com

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
from matplotlib import style

style.use('fivethirtyeight')

data = [0]*50


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylim([0, 8.0])



# 内存信息
def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    used_memory = virtual_memory.used/1024/1024/1024
    free_memory = virtual_memory.free/1024/1024/1024
    memory_percent = virtual_memory.percent
    return used_memory


def animate(i):
    global data
    if len(data) >= 50:
        data = data[1:]
    data.append(get_memory_info())
    xs = []
    ys = []
    for i in range(len(data)):
        xs.append(i)
        ys.append(data[i])
    ax1.clear()
    ax1.set_ylim([0, 8.0])
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=300)
# plt.xlim(0, 8)
plt.show()

