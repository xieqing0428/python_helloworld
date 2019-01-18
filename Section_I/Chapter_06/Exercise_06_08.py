# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_06_08.py
@time: 2019-01-15 21:56

6-8 宠物：
创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
在每个字典中，包含宠物的类型及其主人的名字。
将这些字典存储在一个名为pets的列表中，
再遍历该列表，并将宠物的所有信息都打印出来

"""
pets = []

tony = {'pet_type': 'cat', 'pet_master': 'xiaohong'}
jerry = {'pet_type': 'mouse', 'pet_master': 'xiaoming'}

pets.append(tony)
pets.append(jerry)

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value)
