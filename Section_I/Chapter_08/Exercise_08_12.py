# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_08_12.py
@time: 2019-01-17 20:59

8-12 三明治：
编写一个函数，它接受顾客要在三明治中添加的一系列食材。
这个函数只有一个形参（它收集函数调用中提供的所有食材），
并打印一条消息，对顾客点的三明治进行概述。
调用这个函数三次，每次都提供不同数量的实参

"""


def support_sandwich(*ingredients):
    """接受顾客要在三明治中添加的一系列食材"""
    # 不加料
    if ingredients:
        for ingredient in ingredients:
            print(ingredient)
    else:
        print("不加料")


support_sandwich('培根', '芝士')
support_sandwich('鸡肉')
support_sandwich()
