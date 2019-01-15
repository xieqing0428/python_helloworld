# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_3_6.py
@time: 2019-01-14 20:23

3-6 添加嘉宾：
你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
以完成练习3-4或练习3-5时编写的程序为基础，
在程序末尾添加一条print语句，指出你找到了一个更大的餐桌。
使用insert()将一位新嘉宾添加到名单开头。
使用insert()将另一位新嘉宾添加到名单中间。
使用append()将最后一位新嘉宾添加到名单末尾。
打印一系列消息，向名单中的每位嘉宾发出邀请。

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
