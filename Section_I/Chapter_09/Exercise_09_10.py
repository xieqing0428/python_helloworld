# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_09_10.py
@time: 2019-01-12 21:41

9-10 导入Restaurant类：
将最新的Restaurant类存储在一个模块中。
在另一个文件中，导入Restaurant类，创建一个Restaurant实例，
并调用Restaurant的一个方法，以确认import语句正确无误

"""

from helloworld.section_i.chapter_09.example.exercise_plus import Restaurant

restaurant = Restaurant('饭店', '炒菜')
restaurant.describe_restaurant()


