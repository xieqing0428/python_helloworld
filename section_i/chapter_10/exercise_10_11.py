# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_10_11.py
@time: 2019-01-13 22:46

10-11 喜欢的数字：
编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
再编写一个程序，从文件中读取这个值，
并打印消息“I know your favorite number! It's _____.”

"""
import json

fileName = "example/f_nums.json"
num = input("请输入你最喜欢的数字\n")

with open(fileName, 'w') as file_nums:
    json.dump(num, file_nums)

with open(fileName) as file_nums:
    nums = json.load(file_nums)
    print("I know your favorite number! It's " + nums + ".")
