# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_09.py
@time: 2019-01-24 19:59

15-9 将点数相乘：
同时掷两个骰子时，通常将它们的点数相加。
请通过可视化展示将两个骰子的点数相乘的结果

"""
import pygal

from python_helloworld.section_ii.project_b.chapter_15.example.die import Die

# 创建2个D6
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = [(die_1.roll() * die_2.roll()) for x in range(5000)]
# 分析结果
frequencies = [results.count(value) for value in
               range(1, die_1.num_sides * die_2.num_sides + 1)]
# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [x for x in range(1, die_1.num_sides * die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('images/15-9.svg')
