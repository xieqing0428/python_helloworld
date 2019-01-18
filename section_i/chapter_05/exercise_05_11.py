# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_05_11.py
@time: 2019-01-15 20:29

5-11 序数：
序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
在一个列表中存储数字1~9。
遍历这个列表。
在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。
输出内容应为1st、2nd、3rd、4th、5th、6th、7th、8th和9th，但每个序数都独占一行

"""
nums = [value for value in range(1, 10)]
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(str(num) + "th")
