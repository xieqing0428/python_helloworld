# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_10.py
@time: 2019-01-17 20:30

8-10 了不起的魔术师：
在你为完成练习8-9而编写的程序中，编写一个名为make_great()的函数，
对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
调用函数show_magicians()，确认魔术师列表确实变了

"""
magicians = ['魔术师1', '魔术师2', '魔术师3']


def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    for i in range(len(names)):
        names[i] = 'the Great ' + names[i]


make_great(magicians)
show_magicians(magicians)
