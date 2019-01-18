# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_09_03.py
@time: 2019-01-12 16:13

9-3 用户：
创建一个名为User的类，其中包含属性first_name和last_name，
还有用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法

"""


class User:

    def __init__(self, first_name, last_name, user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print('用户姓名为：' + self.first_name.title() + self.last_name.title())
        print('该用户的简介：' + self.user_info)

    def greet_user(self):
        print(self.first_name.title() + self.last_name.title() + '你好呀！')


user_xiaoming = User('小', '明', '喜欢打篮球')
user_xiaohong = User('小', '红', '喜欢画画')

user_xiaoming.describe_user()
user_xiaoming.greet_user()
user_xiaohong.describe_user()
user_xiaohong.greet_user()
