# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_10_03.py
@time: 2019-01-13 18:20

10-3 访客：
编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中

"""

fileName = 'example/guest.txt'

guestName = input("请输入您的姓名：")
with open(fileName, 'w') as file_object:
    file_object.write(str(guestName))
