# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_08.py
@time: 2019-01-24 19:54

15-8 同时掷三个骰子：
如果你同时掷三个D6骰子，可能得到的最小点数为3，而最大点数为18。
请通过可视化展示同时掷三个D6骰子的结果

"""
import pygal

from python_helloworld.section_ii.project_b.chapter_15.example.die import Die

# 创建3个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = [(die_1.roll() + die_2.roll() + die_3.roll()) for x in range(5000)]
# 分析结果
frequencies = [results.count(value) for value in
               range(3, die_1.num_sides + die_2.num_sides +
                     die_3.num_sides + 1)]
# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [x for x in range(3, die_1.num_sides + die_2.num_sides +
                                  die_3.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('images/15-8.svg')
