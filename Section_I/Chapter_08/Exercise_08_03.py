# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_03.py
@time: 2019-01-17 19:36

8-3 T恤：
编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
这个函数应打印一个句子，概要地说明T恤的尺码和字样

使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数

"""


def make_shirt(size, description):
    print("T恤的尺码是：" + str(size) + ", 印到T恤的字样为：" + str(description))


make_shirt('M', '你猜')
make_shirt(size='M', description='你猜')
