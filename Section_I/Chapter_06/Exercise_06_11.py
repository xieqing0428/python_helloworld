# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_06_11.py
@time: 2019-01-15 22:20

6-11 城市：
创建一个名为cities的字典，其中将三个城市名用作键；
对于每座城市，都创建一个字典，
并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
在表示每座城市的字典中，应包含country、population和fact等键。
将每座城市的名字以及有关它们的信息都打印出来

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
