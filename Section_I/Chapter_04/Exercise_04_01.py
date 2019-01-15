# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_4_1.py
@time: 2019-01-15 10:53

4-1 比萨：
想出至少三种你喜欢的比萨，将其名称存储在一个列表中，
再使用for循环将每种比萨的名称都打印出来。

修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。
对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢比萨。
输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。

"""
pizzas = ['鸡肉披萨', '牛肉披萨', '水果披萨']
for pizza in pizzas:
    print(pizza.title())

for pizza in pizzas:
    print("I like " + pizza.title())
print("I really love pizza!")
