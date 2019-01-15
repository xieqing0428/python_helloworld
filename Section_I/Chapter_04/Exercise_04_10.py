# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_04_10.py
@time: 2019-01-15 11:53

4-10 切片：
选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。

打印消息“The first three items in the list are:”，
再使用切片来打印列表的前三个元素。
打印消息“Three items from the middle of the list are:”，
再使用切片来打印列表中间的三个元素。
打印消息“The last three items in the list are:”，
再使用切片来打印列表末尾的三个元素

"""
values = [value ** 3 for value in range(1, 11)]
for value in values:
    print(value)
print("The first three items in the list are:" + str(values[:3]))
print("Three items from the middle of the list are:" + str(values[3:6]))
print("The last three items in the list are:" + str(values[-3:]))
