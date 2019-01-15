# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_05_08.py
@time: 2019-01-15 20:08

5-8 以特殊方式跟管理员打招呼：
创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'。
想象你要编写代码，在每位用户登录网站后都打印一条问候消息。
遍历用户名列表，并向每位用户打印一条问候消息。

如果用户名为'admin'，就打印一条特殊的问候消息，
如“Hello admin, would you like to see a status report?”
否则，打印一条普通的问候消息，
如“Hello Eric, thank you for logging in again”

"""
users = ['admin', 'xiaohong', 'xiaoming', 'xiaowang', 'xiaocao']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again")
