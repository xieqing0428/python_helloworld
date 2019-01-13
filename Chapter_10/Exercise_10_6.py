# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_10_6.py
@time: 2019-01-13 20:23

10-6 加法运算：
提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
在这种情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
在用户输入的任何一个值不是数字时都捕获ValueError异常，并打印一条友好的错误消息。
对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字

"""


try:
    first = int(input("请输入一个数字：\n"))
    second = int(input("请输入另一个数字：\n"))
except ValueError:
    print("你输入的不是数字！")
else:
    print("相加结果是：\n" + str(int(first) + int(second)))
