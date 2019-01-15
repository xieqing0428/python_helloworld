# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_03_10.py
@time: 2019-01-15 10:41

3-10 尝试使用各个函数：
想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。
编写一个程序，在其中创建一个包含这些元素的列表，
然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。

"""
travels = ['shanghai', 'beijing', 'shenzhen', 'hangzhou', 'chengdu']
print(travels[0])
print(travels[-1])
travels.append('guangzhou')
print(travels)
travels.insert(0, 'nanjing')
print(travels)
del travels[0]
print(travels)
print(travels.pop())
print(travels)
print(travels.pop(1))
print(travels)
travels.remove('shenzhen')
print(travels)
print(travels)
print(sorted(travels))
print(sorted(travels, reverse=True))
travels.reverse()
print(travels)
travels.reverse()
print(travels)
travels.sort()
print(travels)
travels.sort(reverse=True)
print(travels)
print(len(travels))
