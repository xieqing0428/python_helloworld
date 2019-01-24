# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_10.py
@time: 2019-01-24 20:09

15-10 练习使用本章介绍的两个库：
尝试使用matplotlib通过可视化来模拟掷骰子的情况，
并尝试使用Pygal通过可视化来模拟随机漫步的情况

"""
import pygal
import matplotlib.pyplot as plt

from python_helloworld.section_ii.project_b.chapter_15.example.die import Die
from python_helloworld.section_ii.project_b.chapter_15.example.random_walk \
    import RandomWalk

# 随机漫步
rw = RandomWalk()
rw.fill_walk()

hist = pygal.Bar()

hist.title = "RandomWalk"
hist.x_labels = [rw.x_values]
hist.x_title = "x"
hist.y_title = "y"

hist.add('D6', rw.y_values)
hist.render_to_file('images/rw.svg')

# 掷骰子
die = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(5000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
# 可视化结果
plt.plot([x for x in range(1, 7)], frequencies, linewidth=5)
plt.title("Results of rolling one D6 1000 times.", fontsize=14)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()

