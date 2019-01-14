# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: city_functions_plus.py
@time: 2019-01-14 15:23

修改前面的函数，使其包含第三个必不可少的形参population，
并返回一个格式为City, Country - population xxx的字符串，如Santiago, Chile - population 5000000

修改上述函数，将形参population设置为可选的。

"""


def city_country(city, country, population):
    return city.title() + ", " + country.title() + " - population " + str(population)


def city_country_now(city, country, population="5000000"):
    return city.title() + ", " + country.title() + " - population " + str(population)


def city_country_population(city, country, population):
    return city.title() + ", " + country.title() + " - population " + str(population)
