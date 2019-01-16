# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_07_10.py
@time: 2019-01-16 23:39

7-10 梦想的度假胜地：
编写一个程序，调查用户梦想的度假胜地。
使用类似于
“If you could visit one place in the world, where would you go?”
的提示，并编写一个打印调查结果的代码块

"""

places = {}

active = True
while active:

    place = input(
        "If you could visit one place in the world, where would you go?")
    if place == 'quit':
        active = False
        break
    name = input("你哪位？")
    places[name] = place
    print("谢谢！")

