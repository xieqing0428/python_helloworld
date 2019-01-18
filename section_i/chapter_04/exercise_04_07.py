# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_04_07.py
@time: 2019-01-15 11:36

4-7 3的倍数：
创建一个列表，其中包含3~30内能被3整除的数字；
再使用一个for循环将这个列表中的数字都打印出来

"""
values = []
for value in range(3, 31, 3):
    values.append(value)

for value in values:
    print(value)

