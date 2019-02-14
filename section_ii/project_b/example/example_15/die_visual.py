# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: die_visual.py
@time: 2019-01-24 19:30

"""
from section_ii.project_b.example.example_15.die import Die
import pygal

# 创建1个D6
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

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('images/die_visual.svg')