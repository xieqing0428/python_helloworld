# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_05.py
@time: 2019-01-23 21:56

15-5 重构：
方法fill_walk()很长。
请新建一个名为get_step()的方法，用于确定每次漫步的距离和方向，
并计算这次漫步将如何移动。

然后，在fill_walk()中调用get_step()两次：

x_step = self.get_step()
y_step = self.get_step()

通过这样的重构，可缩小fill_walk()的规模，让这个方法阅读和理解起来更容易

"""
import matplotlib.pyplot as plt

from python_helloworld.section_ii.project_b.chapter_15.example\
    .random_walk_5 import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
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

    plt.savefig('images/15-5.png', bbox_inches='tight')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
