# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: 9-5.py
@time: 2019-01-12 17:06

9-5 尝试登录次数：
在为完成练习9-3而编写的User类中，添加一个名为login_attempts 的属性。
编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。
再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0
根据User类创建一个实例，再调用方法increment_login_attempts()多次。
打印属性login_attempts的值，确认它被正确地递增；
然后，调用方法reset_login_attempts()，
并再次打印属性login_attempts的值，确认它被重置为0
"""


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


user_xiaoming = User('小', '明', '喜欢打篮球')
user_xiaoming.increment_login_attempts()
user_xiaoming.increment_login_attempts()
user_xiaoming.increment_login_attempts()
user_xiaoming.increment_login_attempts()
user_xiaoming.increment_login_attempts()
print(str(user_xiaoming.login_attempts))
user_xiaoming.reset_login_attempts()
print(str(user_xiaoming.login_attempts))
