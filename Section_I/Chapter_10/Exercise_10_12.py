# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_10_12.py
@time: 2019-01-13 22:53

10-12 记住喜欢的数字：
将练习10-11中的两个程序合而为一。
如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
运行这个程序两次，看看它是否像预期的那样工作。

"""

import json

fileName = "Example/f_nums.json"

try:
    with open(fileName) as file_nums:
        num = json.load(file_nums)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    num = input("请输入你最喜欢的数字\n")
    with open(fileName, 'w') as file_nums:
        json.dump(num, file_nums)
else:
    print("I know your favorite number! It's " + num + ".")
