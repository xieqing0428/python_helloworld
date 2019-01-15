# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_06_02.py
@time: 2019-01-15 20:47

6-2 喜欢的数字：
使用一个字典来存储一些人喜欢的数字。
请想出5个人的名字，并将这些名字用作字典中的键；
想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。
打印每个人的名字和喜欢的数字。
为让这个程序更有趣，通过询问朋友确保数据是真实的

"""
name_nums = {
    'xiaoming': '1',
    'xiaohong': '2',
    'xiaofang': '3',
    'xiaowang': '4',
    'xiaocao': '5',
}
name = 'xiaoming'
print(name + "喜欢的数字是" + name_nums[name])
name = 'xiaohong'
print(name + "喜欢的数字是" + name_nums[name])
name = 'xiaofang'
print(name + "喜欢的数字是" + name_nums[name])
name = 'xiaowang'
print(name + "喜欢的数字是" + name_nums[name])
name = 'xiaocao'
print(name + "喜欢的数字是" + name_nums[name])
