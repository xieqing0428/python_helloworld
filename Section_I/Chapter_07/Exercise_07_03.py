# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_07_03.py
@time: 2019-01-16 22:14

7-3 10的整数倍：
让用户输入一个数字，并指出这个数字是否是10的整数倍

"""
num = input("请输入一个数字")
if num % 10 == 0:
    print(str(num) + "是10的整数倍")
else:
    print(str(num) + "不是10的整数倍")
