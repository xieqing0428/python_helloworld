# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_07_08.py
@time: 2019-01-16 23:29

7-8 熟食店：
创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；
再创建一个名为finished_sandwiches的空列表。
遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，
如I made your tuna sandwich，并将其移到列表finished_sandwiches。
所有三明治都制作好后，打印一条消息，将这些三明治列出来

"""
sandwich_orders = ['鸡肉三明治', '牛肉三明治']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order)
    finished_sandwiches.append(sandwich_order)
print(finished_sandwiches)
