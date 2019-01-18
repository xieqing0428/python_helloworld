# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_07_06.py
@time: 2019-01-16 22:49

7-6 三个出口：
以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。

在while循环中使用条件测试来结束循环。
使用变量active来控制循环结束的时机。
使用break语句在用户输入'quit'时退出循环

"""
burdens = []
active = True
while active:
    burden = input("请输入配料")
    if burden == 'quit':
        active = False
    else:
        burdens.append(burden)
        print("我们会在披萨中添加" + str(burden))
