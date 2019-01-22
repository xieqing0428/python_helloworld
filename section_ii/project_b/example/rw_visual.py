# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: rw_visual.py
@time: 2019-01-22 23:32

将随机漫步的所有点都绘制出来

"""
import matplotlib.pyplot as plt

from python_helloworld.section_ii.project_b.example.random_walk import \
    RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=50)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('images/randomwalk_50000.png', bbox_inches='tight')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

