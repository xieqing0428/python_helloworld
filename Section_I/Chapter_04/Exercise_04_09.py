# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_4_9.py
@time: 2019-01-15 11:40

4-9 立方解析：
使用列表解析生成一个列表，其中包含前10个整数的立方

"""
values = [value ** 3 for value in range(1, 11)]
for value in values:
    print(value)
