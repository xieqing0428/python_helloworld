# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_04_12.py
@time: 2019-01-15 14:05

4-12 使用多个循环：
在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印列表。
请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表都打印出来

"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_foods)
for friend_food in friend_foods:
    print(friend_food)
