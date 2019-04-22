# coding: utf-8
# author: ismdeep
# dateime: 2019-04-22 19:22:45
# filename: min-distance.py
# blog: https://ismdeep.com

from scipy.misc import imsave
import numpy as np
_ = float('inf')


def dijkstra(graph, n):
    dis = [0] * n
    vis = [False] * n
    pre = [0] * n
    vis[0] = True
    k = 0
    for i in range(n):
        dis[i] = graph[k][i]

    for j in range(n - 1):
        mini = _
        for i in range(n):
            if dis[i] < mini and not vis[i]:
                mini = dis[i]
                k = i
        if k == 0:
            return
        vis[k] = True
        for i in range(n):
            if dis[i] > dis[k] + graph[k][i] and not vis[i]:
                dis[i] = dis[k] + graph[k][i]
                pre[i] = k
    return dis


if __name__ == '__main__':
    n = 6
    graph = [
        [0, 6, 3, _, _, _],
        [6, 0, 2, 5, _, _],
        [3, 2, 0, 3, 4, _],
        [_, 5, 3, 0, 2, 3],
        [_, _, 4, 2, 0, 5],
        [_, _, _, 3, 5, 0],
    ]
    dis = dijkstra(graph, n)
    print(dis)

