# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_05.py
@time: 2019-01-25 16:05

16-5 分析更完整的数据：
本节仅使用了交易收盘价在2017年的部分数据。
如果要全面地分析价格走势，还是应该收集更加完整的数据；
目前最早的交易时间数据可以追溯到2012年。
如果你感兴趣，可以收集早期的数据进行分析

"""
import json
import math
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
    line_chart.render_to_file(title + '.svg')
    return line_chart

# 将数据加载到一个列表中
filename = 'json/btc_close_2017_request.json'
with open(filename) as f:
    btc_data = json.load(f)
# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（¥）'
line_chart.x_labels = dates
# x轴坐标每隔20天显示一次
N = 20
line_chart.x_labels_major = dates[::N]

close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('images/16-5.svg')
