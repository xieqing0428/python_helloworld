# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_07_05.py
@time: 2019-01-16 22:45

7-5 电影票：
有家电影院根据观众的年龄收取不同的票价：
不到3岁的观众免费；
3~12岁的观众为10美元；
超过12岁的观众为15美元。
请编写一个循环，在其中询问用户的年龄，并指出其票价

"""

while True:
    age = input("你的年龄？")
    if age == 'quit':
        break
    if int(age) < 3:
        print("免费")
    elif int(age) <= 12:
        print("票价10美元")
    else:
        print("票价15美元")
