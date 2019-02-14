# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_03.py
@time: 2019-01-24 22:41

16-3 降雨量：
选择你感兴趣的任何地方，通过可视化将其降雨量呈现出来。
为此，可先只涵盖一个月的数据，确定代码正确无误后，再使用一整年的数据来运行它

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

    dates, rains = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rains.append(rain)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rains, c='blue', alpha=0.5)

# 设置图形的格式
title = "Daily Rains - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("PrecipitationIn", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('images/16-3.png', bbox_inches='tight')
plt.show()
