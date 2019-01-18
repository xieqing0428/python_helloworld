# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_09.py
@time: 2019-01-17 20:09

8-9 魔术师：
创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，
这个函数打印列表中每个魔术师的名字。

"""
magicians = ['魔术师1', '魔术师2', '魔术师3']


def show_magicians(names):
    for name in names:
        print(name)


show_magicians(magicians)
