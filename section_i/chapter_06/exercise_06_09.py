# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_06_09.py
@time: 2019-01-15 22:13

6-9 喜欢的地方：
创建一个名为favorite_places的字典。
在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。
为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。
遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来

"""

favorite_places = {
    'xiaoming': ['shanghai', 'beijing', 'hangzhou'],
    'xiaohong': ['chengdu', 'shenzhen'],
    'xiaowang': ['nanjing'],
}

for name, places in favorite_places.items():
    print(name + "喜欢的地方是：")
    for place in places:
        print(place)
