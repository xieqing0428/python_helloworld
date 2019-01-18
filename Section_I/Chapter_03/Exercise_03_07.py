# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_03_07.py
@time: 2019-01-14 20:27

3-7 缩减名单：
你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，
打印一条你只能邀请两位嘉宾共进晚餐的消息。
使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
使用del将最后两位嘉宾从名单中删除，让名单变成空的。
打印该名单，核实程序结束时名单确实是空的。

"""
friends = ['xiaohong', 'xiaoming', 'xiaowang']
print(friends[0] + "你愿意和我共进晚餐吗？")
print(friends[1] + "你愿意和我共进晚餐吗？")
print(friends[2] + "你愿意和我共进晚餐吗？")


print("找到了更大的餐桌")
friends.insert(0, 'xiaoli')
friends.insert(1, 'xiaozhang')
friends.append('xiaocao')

print(friends[-1] + "你愿意和我共进晚餐吗？")
print(friends[-2] + "你愿意和我共进晚餐吗？")
print(friends[-3] + "你愿意和我共进晚餐吗？")
print(friends[-4] + "你愿意和我共进晚餐吗？")
print(friends[-5] + "你愿意和我共进晚餐吗？")
print(friends[-6] + "你愿意和我共进晚餐吗？")

print("餐桌未送达，只能邀请两位")
print(friends.pop() + "很抱歉，无法邀请你来共进晚餐")
print(friends.pop() + "很抱歉，无法邀请你来共进晚餐")
print(friends.pop() + "很抱歉，无法邀请你来共进晚餐")
print(friends.pop() + "很抱歉，无法邀请你来共进晚餐")

print(friends[0] + "你依然在受邀人之列")
print(friends[1] + "你依然在受邀人之列")

del friends[0]
del friends[0]

print(friends)

