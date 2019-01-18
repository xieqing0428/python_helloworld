# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_06_12.py
@time: 2019-01-15 22:28

6-12 扩展：
本章的示例足够复杂，可以以很多方式进行扩展了。
请对本章的一个示例进行扩展：
添加键和值、调整程序要解决的问题或改进输出的格式

"""
cities = {
    'nanjing': {
        'country': 'zhongguo',
        'population': '1000000',
        'fact': 'zhenshi'
    },
    'beijing': {
        'country': 'zhongguo',
        'population': '2000000',
        'fact': 'bucuo'
    },
    'dongjing': {
        'country': 'riben',
        'population': '3000000',
        'fact': 'yiban'
    },
}

for name, infos in cities.items():
    print(name + "的情况如下：")
    for key, value in infos.items():
        print(key + ": " + value)

cities['shanghai'] = {
    'country': 'zhongguo',
    'population': '5000000',
    'fact': 'yiliu'
}

for name, infos in cities.items():
    print(name + "的情况如下：")
    for key, value in infos.items():
        print(key + ": " + value)
