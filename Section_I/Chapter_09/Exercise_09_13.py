# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_09_13.py
@time: 2019-01-12 23:25

9-13 使用OrderedDict：
在练习6-4中，你使用了一个标准字典来表示词汇表。
请使用OrderedDict类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的顺序一致。

"""

from collections import OrderedDict


glossarys = OrderedDict()

glossarys['print'] = '打印'
glossarys['def'] = '方法'
glossarys['class'] = '类'
glossarys['import'] = '引用'
glossarys['module'] = '模块'

for word, mean in glossarys.items():
    print(word.title() + '的意思是' + mean.title())
