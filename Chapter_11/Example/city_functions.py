# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: city_functions.py
@time: 2019-01-14 14:08

编写一个函数，它接受两个形参：一个城市名和一个国家名。
这个函数返回一个格式为City, Country的字符串，如Santiago, Chile

"""


def city_country(city, country):
    return city.title() + ", " + country.title()

