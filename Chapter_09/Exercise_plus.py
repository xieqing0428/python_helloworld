# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_plus.py
@time: 2019-01-12 22:45

"""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name, type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印前述两项信息"""
        print("餐馆的名字叫" + self.restaurant_name.title())
        print("餐馆的烹调类别是" + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")


class User:

    def __init__(self, first_name, last_name, user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        print('用户姓名为：' + self.first_name.title() + self.last_name.title())
        print('该用户的简介：' + self.user_info)

    def greet_user(self):
        print(self.first_name.title() + self.last_name.title() + '你好呀！')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



