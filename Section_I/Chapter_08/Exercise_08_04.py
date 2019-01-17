# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_08_04.py
@time: 2019-01-17 19:44

8-4 大号T恤：
修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
调用这个函数来制作如下T恤：
一件印有默认字样的大号T恤、
一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）

"""


def make_shirt(size, description='I love Python'):
    print("T恤的尺码是：" + str(size) + ", 印到T恤的字样为：" + str(description))


make_shirt('L')
make_shirt('M')
make_shirt(size='M', description='你猜')
