# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_10_07.py
@time: 2019-01-13 20:57

10-7 加法计算器：
将你为完成练习10-6而编写的代码放在一个while循环中，
让用户犯错（输入的是文本而不是数字）后能够继续输入数字。

"""
first = 0
n = 0
while n < 2:
    try:
        first += int(input("请输入一个数字：\n"))
    except ValueError:
        pass
    else:
        n += 1
print("相加结果是" + str(first))
