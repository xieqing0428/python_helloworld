# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_06_05.py
@time: 2019-01-15 21:23

6-5 河流：
创建一个字典，在其中存储三条大河流及其流经的国家。
其中一个键—值对可能是'nile': 'egypt'。

使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
使用循环将该字典中每条河流的名字都打印出来。
使用循环将该字典包含的每个国家的名字都打印出来

"""
river_countrys = {
    'nile': 'egypt',
    'changjiang': 'zhongguo',
    'huanghe': 'zhongguo',
}

for river, country in river_countrys.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
for river in river_countrys:
    print(river.title())
for river in river_countrys.keys():
    print(river.title())
for country in river_countrys.values():
    print(country.title())
