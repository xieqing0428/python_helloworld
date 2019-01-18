# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_07_04.py
@time: 2019-01-16 22:17

7-4 比萨配料：
编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。
每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料

"""
burdens = []

while True:
    burden = input("请输入配料")
    if burden == 'quit':
        break
    burdens.append(burden)
    print("我们会在披萨中添加" + str(burden))
