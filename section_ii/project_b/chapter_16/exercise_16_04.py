# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_04.py
@time: 2019-01-24 22:54

16-4 探索：
生成一些图表，对你好奇的任何地方的其他天气数据进行研究

"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'csv/sitka_weather_2014.csv'
with open(filename) as f:
    """查看这个文件的第一行"""
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, humiditys = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            humidity = float(row[8])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            humiditys.append(humidity)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, humiditys, c='blue', alpha=0.5)

# 设置图形的格式
title = "Daily Rains - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Mean Humidity", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('images/16-4.png', bbox_inches='tight')
plt.show()
