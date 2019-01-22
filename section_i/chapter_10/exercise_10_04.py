# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_10_04.py
@time: 2019-01-13 18:23

10-4 访客名单：
编写一个while循环，提示用户输入其名字。
用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
确保这个文件中的每条记录都独占一行

"""

fileName = 'example/guest_book.txt'

while True:
    guestName = input("请输入您的姓名：(如需退出请输入Exit) \n")
    if guestName == "Exit":
        break
    print(str(guestName) + "你好呀！")
    with open(fileName, 'a') as file_object:
        file_object.write(str(guestName) + "\n")
