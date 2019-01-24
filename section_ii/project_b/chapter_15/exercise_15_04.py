# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_04.py
@time: 2019-01-23 00:30

15-4 改进的随机漫步：
在类RandomWalk中，x_step和y_step是根据相同的条件生成的：
从列表[1, -1]中随机地选择方向，并从列表[0, 1, 2, 3, 4]中随机地选择距离。
请修改这些列表中的值，看看对随机漫步路径有何影响。
尝试使用更长的距离选择列表，如0~8；
或者将-1从 x 或 y 方向列表中删除

"""
import matplotlib.pyplot as plt

from python_helloworld.section_ii.project_b.chapter_15.example\
    .random_walk_4 import RandomWalkPlus

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalkPlus()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=50)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('images/15-4.png', bbox_inches='tight')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
