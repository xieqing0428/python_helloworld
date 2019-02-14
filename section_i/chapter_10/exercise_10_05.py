# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_10_05.py
@time: 2019-01-13 18:33

10-5 关于编程的调查：
编写一个while循环，询问用户为何喜欢编程。
每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中

"""

fileName = 'example_15/why_coding.txt'

print("您为什么喜欢编程呢？(如需退出请输入Exit) \n")
n = 0
while True:
    reason = input("原因" + str(n) + ":")
    n += 1
    if reason == "Exit":
        break
    with open(fileName, 'a') as file_object:
        file_object.write(str(reason) + "\n")
