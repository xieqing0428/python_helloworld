# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_02.py
@time: 2019-01-24 22:05

16-2 比较锡特卡和死亡谷的气温：
在有关锡特卡和死亡谷的图表中，气温刻度反映了数据范围的不同。
为准确地比较锡特卡和死亡谷的气温范围，需要在y轴上使用相同的刻度。
为此，请修改图16-5和图16-6所示图表的y轴设置，
对锡特卡和死亡谷的气温范围进行直接比较（你也可以对任何两个地方的气温范围进行比较）。
你还可以尝试在一个图表中呈现这两个数据集

"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename_1 = 'csv/death_valley_2014.csv'
filename_2 = 'csv/sitka_weather_2014.csv'
with open(filename_1) as f:
    """查看这个文件的第一行"""
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


with open(filename_2) as f:
    """查看这个文件的第一行"""
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates_1, highs_1, lows_1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_1.append(current_date)
            highs_1.append(high)
            lows_1.append(low)

# 根据数据绘制图形
plt.plot(dates_1, highs_1, c='yellow', alpha=0.5)
plt.plot(dates_1, lows_1, c='green', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='red', alpha=0.1)


# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley vs Sitka, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('images/16-2.png', bbox_inches='tight')
plt.show()
