# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_01.py
@time: 2019-01-24 21:50

16-1 旧金山：
旧金山的气温更接近于锡特卡还是死亡谷呢？
请绘制一个显示旧金山最高气温和最低气温的图表，并进行比较。
可从http://www.wunderground.com/history/下载几乎任何地方的天气数据。
为此，请输入相应的地方和日期范围，滚动到页面底部，
找到名为Comma-Delimited File的链接，再单击该链接，将数据存储为CSV文件

"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 网站好像下不到数据了，就用源代码中的数据文件吧
filename = 'csv/death_valley_2014.csv'
with open(filename) as f:
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
# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('images/example_5.png', bbox_inches='tight')
plt.show()
