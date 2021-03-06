# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_03.py
@time: 2019-01-23 00:19

15-3 分子运动：
修改rw_visual.py，将其中的plt.scatter()替换为plt.plot()。
为模拟花粉在水滴表面的运动路径，
向plt.plot()传递rw.x_values和rw.y_values，并指定实参值linewidth。
使用5000个点而不是50 000个点

"""
import matplotlib.pyplot as plt

from python_helloworld.section_ii.project_b.chapter_15.example.random_walk_3 \
    import RandomWalk

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

    plt.savefig('images/15-3.png', bbox_inches='tight')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
