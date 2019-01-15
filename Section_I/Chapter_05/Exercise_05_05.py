# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_05_05.py
@time: 2019-01-15 19:50

5-5 外星人颜色#3：
将练习5-4中的if-else结构改为if-elif-else结构。
如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息

"""
alien_color = 'green'
print("外星人的颜色是" + alien_color)
if alien_color == 'green':
    print("恭喜你获得了5个点！")
elif alien_color == 'yellow':
    print("恭喜你获得了10个点！")
else:
    print("恭喜你获得了15个点！")

alien_color = 'yellow'
print("外星人的颜色是" + alien_color)
if alien_color == 'green':
    print("恭喜你获得了5个点！")
elif alien_color == 'yellow':
    print("恭喜你获得了10个点！")
else:
    print("恭喜你获得了15个点！")

alien_colors = 'red'
print("外星人的颜色是" + alien_color)
if alien_color == 'green':
    print("恭喜你获得了5个点！")
elif alien_color == 'yellow':
    print("恭喜你获得了10个点！")
else:
    print("恭喜你获得了15个点！")
