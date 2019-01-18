# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_04_04.py
@time: 2019-01-15 11:30

4-4 一百万：
创建一个列表，其中包含数字1~1 000 000，
再使用一个for循环将这些数字打印出来
（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）

"""
values = []
for value in range(1, 1000001):
    values.append(value)
    print(value)
