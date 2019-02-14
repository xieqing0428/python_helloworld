# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_06.py
@time: 2019-01-25 16:39

16-6 选择你感兴趣的数据：
免费的JSON格式数据非常丰富，许多著名的国际组织都在积极分享有价值的数据。
例如，Open Knowledge International（https://okfn.org/）上就有许多有趣的JSON数据。
你也可以用本节的方法获取它们，开启自己的分析项目

"""
import json
# import math
from itertools import groupby

import pygal


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file('images/16-6.svg')
    return line_chart


# 将数据加载到一个列表中
filename = 'json/gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)
# 创建5个列表，分别存储日期和收盘价
c_codes = []
c_names = []
values = []
years = []

for gdp_dict in gdp_data:
    c_codes.append(gdp_dict['Country Code'])
    c_names.append(gdp_dict['Country Name'])
    values.append(int(float(gdp_dict['Value'])))
    years.append(gdp_dict['Year'])

# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = 'GDP'
# x轴坐标每隔20天显示一次
N = 57
# Y取[0, 57)
Y = 0
# line_chart.x_labels = c_names[Y::N]
# value_log = [_ for _ in values[Y::N]]
# value_log = [math.log10(_) for _ in values[Y::N]]

line_chart = draw_line(c_names[Y::N], values[Y::N], 'GDP', 'log-values')

