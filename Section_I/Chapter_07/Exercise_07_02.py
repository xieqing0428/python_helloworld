# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_07_02.py
@time: 2019-01-16 22:13

7-2 餐馆订位：
编写一个程序，询问用户有多少人用餐。
如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌

"""
num = input("请问有多少人用餐？")
if int(num) > 8:
    print("没有空桌")
else:
    print("有空桌")
