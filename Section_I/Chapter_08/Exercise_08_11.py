# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_11.py
@time: 2019-01-17 20:55

8-11 不变的魔术师：
修改你为完成练习8-10而编写的程序，在调用函数make_great()时，向它传递魔术师列表的副本。
由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
分别使用这两个列表来调用show_magicians()，
确认一个列表包含的是原来的魔术师名字，
而另一个列表包含的是添加了字样“the Great”的魔术师名字

"""
magicians = ['魔术师1', '魔术师2', '魔术师3']
great_magicians = []


def show_magicians(names):
    for name in names:
        print(name)


def make_great(copies, names):
    for i in range(len(copies)):
        names.append('the Great ' + copies[i])


show_magicians(magicians)
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
