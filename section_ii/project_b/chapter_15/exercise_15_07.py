# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_07.py
@time: 2019-01-24 19:52

15-7 两个D8骰子：
请模拟同时掷两个8面骰子1000次的结果。
逐渐增加掷骰子的次数，直到系统不堪重负为止

"""
import pygal

from python_helloworld.section_ii.project_b.chapter_15.example.die import Die

# 创建2个D6
die_1 = Die(8)
die_2 = Die(8)

# 掷骰子多次，并将结果存储到一个列表中
results = [(die_1.roll() + die_2.roll()) for x in range(1000)]
# 分析结果
frequencies = [results.count(value) for value in
               range(2, die_1.num_sides + die_2.num_sides + 1)]
# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times."
hist.x_labels = [x for x in range(2, die_1.num_sides * die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('images/15-7.svg')
