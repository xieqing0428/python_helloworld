# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_08_05.py
@time: 2019-01-17 19:47

8-5 城市：
编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如Reykjavik is in Iceland。
给用于存储国家的形参指定默认值。
为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家

"""


def describe_city(city='Reykjavik', country='Iceland'):
    print(city + " is in " + country)


describe_city()
describe_city('Shanghai', 'China')
describe_city('xx')
