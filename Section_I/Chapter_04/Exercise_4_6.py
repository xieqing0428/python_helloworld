# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_4_6.py
@time: 2019-01-15 11:35

4-6 奇数：
通过给函数range()指定第三个参数来创建一个列表，其中包含1~20的奇数；
再使用一个for循环将这些数字都打印出来

"""
values = []
for value in range(1, 20, 2):
    values.append(value)

for value in values:
    print(value)

