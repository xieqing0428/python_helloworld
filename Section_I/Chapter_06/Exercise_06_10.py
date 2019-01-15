# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_06_10.py
@time: 2019-01-15 22:17

6-10 喜欢的数字：
修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，
然后将每个人的名字及其喜欢的数字打印出来

"""
name_nums = {
    'xiaoming': ['1', '2'],
    'xiaohong': ['3', '4'],
    'xiaofang': ['5', '6'],
    'xiaowang': ['7', '8'],
    'xiaocao': ['9', '0'],
}

for name, nums in name_nums.items():
    print(name + "喜欢的数字是：")
    for num in nums:
        print(num)
