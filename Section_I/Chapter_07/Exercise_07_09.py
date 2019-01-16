# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_07_09.py
@time: 2019-01-16 23:36

7-9 五香烟熏牛肉（pastrami）卖完了：
使用为完成练习7-8而创建的列表sandwich_orders，
并确保'pastrami'在其中至少出现了三次。
在程序开头附近添加这样的代码：
打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。
确认最终的列表finished_sandwiches中不包含'pastrami'

"""
sandwich_orders = ['鸡肉三明治', '牛肉三明治', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
print("五香烟熏牛肉卖完了")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order)
    finished_sandwiches.append(sandwich_order)
print(finished_sandwiches)
