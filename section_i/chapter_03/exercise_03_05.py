# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_03_05.py
@time: 2019-01-14 20:21

3-5 修改嘉宾名单：
你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。

以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。
修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
再次打印一系列消息，向名单中的每位嘉宾发出邀请。

"""
friends = ['xiaohong', 'xiaoming', 'xiaowang']
print(friends[0] + "你愿意和我共进晚餐吗？")
print(friends[1] + "你愿意和我共进晚餐吗？")
print(friends[2] + "你愿意和我共进晚餐吗？")


print("xiaohong 无法赴约")
friends[1] = 'xiaoli'

print(friends[-1] + "你愿意和我共进晚餐吗？")
print(friends[-2] + "你愿意和我共进晚餐吗？")
print(friends[-3] + "你愿意和我共进晚餐吗？")
